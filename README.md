# Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information

[![Open in Molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-llm-aggregation/blob/main/notebooks/llm_aggregation_tutorial.py)

This repository is an independent, claim-by-claim reproduction audit of
[arXiv:2510.01499](https://arxiv.org/abs/2510.01499), accepted at ICML 2026. The
paper studies how to aggregate answers from multiple language models when their
accuracies and errors are heterogeneous and correlated. It introduces Optimal
Weight (OW) and Inverse Surprising Popularity (ISP), using first- and second-order
information instead of treating every answer as an independent equal vote.

## Current verdict

The committed publication gate records **5/6 claims and 10 points**. This is the
reproduction audit result, not a live judge result. Five claims have executable
evidence; the real-data Table 3 claim remains **BLOCKED** because the exact
prediction caches and provenance are unavailable.

| Claim | Paper statement | Audit verdict | How the verdict is produced |
| --- | --- | --- | --- |
| c1 — Theorem 1 | Under the stated conditional-independence model, OW is Bayes/MAP optimal. | **VERIFIED EXACT** | `claim1_ow_bayes.py` checks the likelihood factorization, an independent Fraction certificate exhausts 418 profiles, and a dependence-violation control breaks the conclusion. |
| c2 — Theorem 2 | Under `x_i ≥ 1/K`, expected ISP advantage is at least MV advantage, which is at least SP advantage. | **VERIFIED EXACT** | `claim2_isp_ordering.py` expands exact sparse polynomials, matches closed-form gaps to simulation, checks 55 profiles, and tests the below-random premise control. |
| c3 — simulation | The N=4, M=10,000 synthetic simulation shows ISP/MV gains and an approximately `Theta(1/K)` gap. | **VERIFIED** | `claim3_simulation.py` runs the calibrated 89-seed full-size campaign, the paper K=2/K=4 values fall inside predictive ranges, and the asymptotic gap certificate is checked separately. |
| c4 — real-data Table 3 | OW-L improves aggregation on UltraFeedback, MMLU, and ARMMAN. | **BLOCKED** | `claim4_real_data.py` completes four discovery, regeneration, aggregate-reconstruction, and falsification routes; exact caches, ARMMAN records, shuffle maps, Azure provenance, and OW-L code are missing. |
| c5 — Appendix E.4 | OW-L beats majority voting in 47 of 48 published ensemble cases. | **VERIFIED** | `claim5_tables.py` independently recomputes all 48 rows and rejects the common conflation between the OW-L-only range and the best-method range. |
| c6 — Corollary 1 | Binary OW weights are Bradley–Terry inverse-logit scores. | **VERIFIED EXACT** | `claim6_bt.py` proves the algebra, then uses exact rational composition, 60-digit Decimal arithmetic, endpoint controls, and positive/negative scaling controls. |

The audit reproduces the paper’s synthetic headline values closely: across 89
full-size seeds, mean ISP/MV is `90.16%/85.00%` at `K=2` and
`94.41%/92.38%` at `K=4`, compared with the paper’s `90.48%/85.13%` and
`94.45%/92.64%`. These are independent CPU simulations, not the unreleased real
LLM inference records.

## How each claim is produced

All formal nodes inherit the fixed command `uv run python repro/src/verify.py`.
The cumulative verifier runs the claim modules in order and writes the committed
verdict/evidence records.

| Claim | Production path | Evidence and controls |
| --- | --- | --- |
| c1 | `repro/claims/claim1_ow_bayes.py` | The source certificate is checked without importing the production aggregator; the independent checker exhausts exact answer profiles and tests conditional-independence failure. |
| c2 | `repro/claims/claim2_isp_ordering.py` | Exact rational polynomials establish the ordering; simulation and a below-random mutation verify that the premise is load-bearing. |
| c3 | `repro/claims/claim3_simulation.py` | Seeded agent answers are generated for the N=4/M=10,000 setting, calibrated to 89 repetitions, then compared with MV, SP, ISP, and OW across K. |
| c4 | `repro/claims/claim4_real_data.py` | A capability contract distinguishes faithful rerun from table-only arithmetic; four routes record why the real-data claim cannot be promoted. |
| c5 | `repro/claims/claim5_tables.py` | The 16 ensembles on each of UltraFeedback, MMLU, and ARMMAN are parsed and checked as a complete 2×2×2×2 design; integer and quantifier mutations are rejected. |
| c6 | `repro/claims/claim6_bt.py` | The binary OW link is inverted to `log(x/(1-x))`, independently compared with Bradley–Terry, and checked over interior, endpoint, offset, and scaling cases. |

The evaluator-visible source and proof artifacts are mirrored under
`space_candidate/evidence/claim-*`; the historical OpenResearch artifacts under
`.openresearch/artifacts/` preserve the source contracts, commands, outputs, and
limitations.

## Standardized audit dossier

The review and machine-readable audit records are:

- [STATUS.md](STATUS.md) — current scope, verdict, historical score, and publication boundary.
- [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) — claim-by-claim evidence production paths.
- [SOURCE_AUDIT.md](SOURCE_AUDIT.md) — paper anchors, implementation mapping, and source limitations.
- [ENVIRONMENT.md](ENVIRONMENT.md) — pinned environment, compute, and rerun contract.
- [REPORT.md](REPORT.md) — concise reproduction report.
- [AUTHOR_THANK_YOU.md](AUTHOR_THANK_YOU.md) — thank-you note to the paper authors.
- [CITATION.cff](CITATION.cff) — citation metadata for this audit and the paper.
- [claims.json](claims.json) and [reproduction_verdicts.json](reproduction_verdicts.json) — normalized claim records.
- [EVIDENCE_MANIFEST.json](EVIDENCE_MANIFEST.json) — required evidence paths.
- [AUTONOMOUS_STATE.json](AUTONOMOUS_STATE.json) — normalization and recovery record.
- [verify_final.py](verify_final.py) — final repository-integrity verifier.

The standardized state is PARTIAL_C1_C2_C3_C5_C6_VERIFIED_C4_BLOCKED_HISTORICAL_SCORE_0_OF_12_NO_CURRENT_SCORE.
The historical 0/12 judge result is preserved as provenance only. There is no
current live-judge score claim. C4 remains blocked because exact real-data
prediction caches and provenance are unavailable.

## Branch map

The branch names describe the scientific or release purpose. The full
[branch audit](branch-audit.md) records the legacy source ref, source tip, clean
branch, and final verification contract.

| Final branch | Purpose | Result |
| --- | --- | --- |
| [`main`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/main) | Documentation and publication surface | 5 verified; c4 blocked |
| [`historical/judged-baseline`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/historical/judged-baseline) | Frozen judged baseline and locked environment | Historical baseline |
| [`audit/c1-ow-bayes`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/audit/c1-ow-bayes) | Universal OW/MAP proof certificate | c1 VERIFIED |
| [`release/c1-evidence`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/c1-evidence) | Evaluator-visible c1 evidence | c1 VERIFIED |
| [`audit/c2-isp-ordering`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/audit/c2-isp-ordering) | Universal ISP/MV/SP ordering certificate | c2 VERIFIED |
| [`release/c2-evidence`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/c2-evidence) | Evaluator-visible c2 evidence | c2 VERIFIED |
| [`audit/c3-full-simulation`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/audit/c3-full-simulation) | 89-seed full simulation | c3 VERIFIED |
| [`audit/c3-calibration-pilot`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/audit/c3-calibration-pilot) | Simulation repeat-count calibration | c3 support |
| [`release/c3-evidence`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/c3-evidence) | Evaluator-visible c3 evidence | c3 VERIFIED |
| [`audit/c4-real-data`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/audit/c4-real-data) | Four-route real-data access and falsification audit | c4 BLOCKED |
| [`release/c4-blocked-evidence`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/c4-blocked-evidence) | Evaluator-visible blocked c4 package | c4 BLOCKED |
| [`audit/c5-ensemble-aggregate`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/audit/c5-ensemble-aggregate) | Exact 48-row Appendix audit | c5 VERIFIED |
| [`release/c5-evidence`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/c5-evidence) | Evaluator-visible c5 evidence | c5 VERIFIED |
| [`audit/c6-bradley-terry`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/audit/c6-bradley-terry) | Bradley–Terry inverse-logit certificate | c6 VERIFIED |
| [`release/c6-evidence`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/c6-evidence) | Evaluator-visible c6 evidence | c6 VERIFIED |
| [`release/final-gates`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/final-gates) | Final report, notebook, and release gates | cumulative PASS |
| [`release/gate-closure`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/gate-closure) | Publication-candidate closure | 5 verified; c4 blocked |
| [`release/metadata-audit`](https://github.com/MachineLearning-Nerd/icml26-llm-aggregation/tree/release/metadata-audit) | Evaluator-blind metadata and visibility audit | release audit |

## Reproduce locally

```bash
uv sync --frozen
uv run python repro/src/verify.py
```

The environment is pinned to Python 3.12 in `uv.lock`. Claim 3 runs 801 full-size
simulations and is CPU-intensive; the formal campaign used Hugging Face
`cpu-upgrade` with 8 allocated vCPU and no GPU or proxy real-data run. The
[technical report](reports/llm-aggregation-reproduction/report.md),
[command/release records](.openresearch/release/command_ledger.md),
[marimo tutorial](notebooks/llm_aggregation_tutorial.py), and
[Space evidence mirror](space_candidate/pages/index.md) provide the detailed
commands, inputs, outputs, and limitations.

## Paper and citation

Rui Ai, Yuqi Pan, David Simchi-Levi, Milind Tambe, and Haifeng Xu. “Beyond
Majority Voting: LLM Aggregation by Leveraging Higher-Order Information.” arXiv
preprint arXiv:2510.01499v2, 2026.
[Paper and abstract](https://arxiv.org/abs/2510.01499).

```bibtex
@article{ai2025beyond,
  title   = {Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information},
  author  = {Ai, Rui and Pan, Yuqi and Simchi-Levi, David and Tambe, Milind and Xu, Haifeng},
  journal = {arXiv preprint arXiv:2510.01499},
  year    = {2025},
  doi     = {10.48550/arXiv.2510.01499}
}
```

The arXiv record notes acceptance at ICML 2026 and has a 2026 revision; the
BibTeX year follows the original 2025 submission.

## Thank you

Thank you to Rui Ai, Yuqi Pan, David Simchi-Levi, Milind Tambe, and Haifeng Xu
for making the OW/ISP formulation, higher-order aggregation perspective, and
synthetic/real-data claims available for careful independent study. This audit
documents what can be reproduced from public equations and tables, and clearly
marks the real-data result as blocked rather than substituting a different LLM
inference run.

## Attribution and scope

Repository documentation and approved history normalization are published under
the `MachineLearning-Nerd` GitHub identity. Paper claims and paper authorship
remain attributed to the authors cited above. This is a reproduction audit, not
an official implementation release or a claim of authorship.
