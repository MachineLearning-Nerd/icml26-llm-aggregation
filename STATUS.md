# Status — Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information

Paper: arXiv 2510.01499, version 2, accepted at ICML 2026
Repository: MachineLearning-Nerd/icml26-llm-aggregation
Audit state: PARTIAL_C1_C2_C3_C5_C6_VERIFIED_C4_BLOCKED_HISTORICAL_SCORE_0_OF_12_NO_CURRENT_SCORE

This is a clean-room reproduction audit. It preserves the prior live judge
result as historical provenance and does not claim a current score.

## Claim status

| Claim | Scope | Evidence | Status |
| --- | --- | --- | --- |
| C1 — Theorem 1 | OW is Bayes/MAP optimal under conditional independence | exact likelihood factorization and 418 Fraction profiles | VERIFIED_SCOPED |
| C2 — Theorem 2 | ISP dominates MV and MV dominates SP under x_i >= 1/K | exact sparse-polynomial certificate and 55 profiles | VERIFIED_SCOPED |
| C3 — simulation | N=4, M=10,000 ISP/MV gains and Theta(1/K) gap | calibrated 89-seed full-size campaign | VERIFIED_SCOPED |
| C4 — real-data Table 3 | OW-L on UltraFeedback, MMLU, and ARMMAN | four routes completed; caches and provenance unavailable | BLOCKED |
| C5 — Appendix E.4 | OW-L wins 47 of 48 published ensemble cases | all 48 table rows reconstructed and checked | VERIFIED_SCOPED |
| C6 — Corollary 1 | binary OW weights equal Bradley–Terry inverse-logit scores | exact algebra, rational, Decimal, endpoint, and scaling checks | VERIFIED_SCOPED |

The clean-room evidence total is 10/12 points: two points for each of C1–C3,
C5, and C6, with no points claimed for blocked C4. The historical judge result
was 0/12. The 10/12 value is an evidence-package total, not a current judge
score.

## Evidence boundary

C1, C2, and C6 are proof-level or exact algebraic checks under the paper’s
assumptions. C3 is an independent CPU simulation with 89 calibrated seeds and
801 full-size settings. C5 verifies published aggregate rows, not raw LLM
inference. C4 remains blocked after discovery, faithful-regeneration,
aggregate-reconstruction, and assumption-preserving falsification routes.

## Verification inputs

- outputs/verify_results.json
- outputs/verdict.json
- publication_gate.json
- GATE_READY.md
- reports/llm-aggregation-reproduction/report.md
- docs/CLAIMS_PINNED.md
- space_candidate/evidence/claim-1 through claim-6

Run verify_final.py after checking out the published main branch to validate
branch policy, canonical attribution, claim statuses, raw evidence, the
historical score boundary, and the required dossier paths.
