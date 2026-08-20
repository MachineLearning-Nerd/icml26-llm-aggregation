#!/usr/bin/env python3
"""Verify the multi-branch publication contract without rerunning experiments."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_IDENTITY = (
    "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
)
EXPECTED_STATUS = (
    "PARTIAL_C1_C2_C3_C5_C6_VERIFIED_C4_BLOCKED_"
    "HISTORICAL_SCORE_0_OF_12_NO_CURRENT_SCORE"
)
EXPECTED_RECOVERY_SHA = (
    "0f50937f36b993735c22037b5c3f96ffc5f62809ddcf818ea7e21b5fb45d53e4"
)
EXPECTED_BRANCHES = {
    "audit/c1-ow-bayes",
    "audit/c2-isp-ordering",
    "audit/c3-calibration-pilot",
    "audit/c3-full-simulation",
    "audit/c4-real-data",
    "audit/c5-ensemble-aggregate",
    "audit/c6-bradley-terry",
    "historical/judged-baseline",
    "main",
    "release/c1-evidence",
    "release/c2-evidence",
    "release/c3-evidence",
    "release/c4-blocked-evidence",
    "release/c5-evidence",
    "release/c6-evidence",
    "release/final-gates",
    "release/gate-closure",
    "release/metadata-audit",
}


def fail(reason: str) -> None:
    print("FINAL_AUDIT=FAILED reason=" + reason)
    raise SystemExit(1)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail("git_" + "_".join(args))
    return result.stdout.strip()


def load(relative_path: str) -> dict:
    try:
        with (ROOT / relative_path).open(encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as error:
        fail(relative_path + "_invalid_" + type(error).__name__)
    raise AssertionError("unreachable")


local_branches = {
    line
    for line in git(
        "for-each-ref",
        "refs/heads",
        "--format=%(refname:short)",
    ).splitlines()
    if line
}
remote_branches = {
    line.removeprefix("origin/")
    for line in git(
        "for-each-ref",
        "refs/remotes/origin",
        "--format=%(refname:short)",
    ).splitlines()
    if line not in {"origin", "origin/HEAD"}
}
if local_branches == EXPECTED_BRANCHES:
    branch_inventory = local_branches
elif local_branches == {"main"} and remote_branches == EXPECTED_BRANCHES:
    branch_inventory = remote_branches
else:
    observed = sorted(local_branches | remote_branches)
    fail("branches_" + ",".join(observed))
if git("branch", "--show-current") != "main":
    fail("head_not_main")

commit_count = int(git("rev-list", "--count", "--all"))
if commit_count != 42:
    fail("commit_count_" + str(commit_count))

identity_rows = git(
    "log",
    "--all",
    "--format=%an <%ae>|%cn <%ce>",
).splitlines()
expected_row = EXPECTED_IDENTITY + "|" + EXPECTED_IDENTITY
if not identity_rows or any(row != expected_row for row in identity_rows):
    fail("noncanonical_commit_identity")

claims_doc = load("claims.json")
claims = {claim["id"]: claim for claim in claims_doc["claims"]}
expected_claims = {
    "C1": "VERIFIED_SCOPED",
    "C2": "VERIFIED_SCOPED",
    "C3": "VERIFIED_SCOPED",
    "C4": "BLOCKED",
    "C5": "VERIFIED_SCOPED",
    "C6": "VERIFIED_SCOPED",
}
if {claim_id: claims[claim_id]["status"] for claim_id in expected_claims} != expected_claims:
    fail("claim_statuses")
if claims_doc["audit"]["status"] != EXPECTED_STATUS:
    fail("claims_audit_status")
if claims_doc["audit"]["evidence_points"] != 10:
    fail("claims_evidence_points")

results = load("outputs/verify_results.json")
if results.get("c1_ok") is not True:
    fail("c1")
for key in ("2", "4", "6"):
    if results.get("c1_thm1", {}).get(key, {}).get("identical") is not True:
        fail("c1_profile_" + key)
for key in ("2", "4", "6"):
    if results.get("c2_thm2", {}).get(key, {}).get("order_ok") is not True:
        fail("c2_order_" + key)
if results.get("c3_gap_slope", 0) >= -0.7:
    fail("c3_gap_slope")
if results.get("c5_ensemble", {}).get("win_rate", 0) <= 0.99:
    fail("c5_ensemble")
if results.get("c5_ensemble", {}).get("min_gap", -1) < 0:
    fail("c5_min_gap")
if results.get("c6_ok") is not True:
    fail("c6")

gate = load("publication_gate.json")
if gate.get("tests_passed") is not True or gate.get("publication_gate_passed") is not True:
    fail("legacy_gate")
if (gate.get("claims_verified"), gate.get("claims_total"), gate.get("points")) != (5, 6, 10):
    fail("legacy_gate_score")

verdicts = load("reproduction_verdicts.json")
if verdicts.get("audit_status") != EXPECTED_STATUS:
    fail("verdict_status")
if verdicts.get("evidence", {}).get("historical_score") != "0/12":
    fail("historical_score")
if verdicts.get("evidence", {}).get("current_score_claim") is not False:
    fail("current_score_claim")
if verdicts.get("evidence", {}).get("publication_allowed") is not False:
    fail("publication_boundary")

state = load("AUTONOMOUS_STATE.json")
if state.get("status") != EXPECTED_STATUS:
    fail("state_status")
if state.get("recovery", {}).get("bundle_sha256") != EXPECTED_RECOVERY_SHA:
    fail("recovery_sha")

manifest = load("EVIDENCE_MANIFEST.json")
missing = [
    path
    for path in manifest["required_paths"]
    if not (ROOT / path).is_file()
]
if missing:
    fail("missing_paths_" + ",".join(missing))

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for marker in (
    "2510.01499",
    "STATUS.md",
    "CLAIM_EVIDENCE.md",
    "Thank you",
    "not a live judge result",
):
    if marker not in readme:
        fail("readme_" + marker.replace(" ", "_"))

branch_audit = (ROOT / "branch-audit.md").read_text(encoding="utf-8")
if EXPECTED_IDENTITY not in branch_audit:
    fail("branch_audit_identity")

print(
    "FINAL_AUDIT=VERIFIED "
    "branches=18 "
    "commits=42 "
    "claims=C1:C2:C3:C5:C6_verified_scoped,C4_blocked "
    "evidence_points=10 "
    "historical_score=0/12 "
    "current_score_claim=false "
    "publication_allowed=false"
)
