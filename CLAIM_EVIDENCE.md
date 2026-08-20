# Claim evidence — Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information

Paper: arXiv 2510.01499, version 2
Repository scope: clean-room audit with exact formal checks, CPU simulation,
published-table reconstruction, and a blocked real-data route

## C1 — OW is Bayes/MAP optimal

Paper anchor: Theorem 1.

Production path:

1. repro/claims/claim1_ow_bayes.py implements the conditional likelihood
   factorization and OW score.
2. An independent Fraction checker exhausts 418 answer profiles without
   importing the production aggregator.
3. A deliberately dependent joint distribution is used as a negative control.

Observed result: the OW argmax set matches MAP for the checked profiles, while
the dependence-violation control breaks the conclusion.

Verdict: VERIFIED_SCOPED. The universal factorization is checked under the
paper’s assumptions; the negative control records that independence matters.

## C2 — ISP dominates MV and MV dominates SP

Paper anchor: Theorem 2.

Production path: repro/claims/claim2_isp_ordering.py expands the two expected
advantage gaps as exact sparse polynomials. The independent checker exhausts 55
profiles and compares the closed forms with simulation at K=2, 4, and 6.

Observed result: ISP >= MV >= SP under x_i >= 1/K, with the closed-form and
simulation gaps matching within the recorded evidence. A below-random premise
control reverses the ordering as intended.

Verdict: VERIFIED_SCOPED. The premise is treated as load-bearing.

## C3 — synthetic simulation and asymptotic gap

Paper anchor: the N=4, M=10,000 simulation and the Theta(1/K) gap.

Production path: repro/claims/claim3_simulation.py runs the calibrated 89-seed
campaign across nine K values, covering 801 full-size simulations. It compares
ISP, MV, SP, and OW and checks the exact asymptotic expression separately.

Observed result: the independent means are 90.16% ISP versus 85.00% MV at K=2
and 94.41% versus 92.38% at K=4, close to the paper’s 90.48%/85.13% and
94.45%/92.64%. The exact gap certificate has a log-log slope near -0.983.

Verdict: VERIFIED_SCOPED. This is an independent CPU simulation, not a claim
that the original private LLM inference records were recovered.

## C4 — real-data Table 3

Paper anchor: the OW-L results on UltraFeedback, MMLU, and ARMMAN.

Production path: repro/claims/claim4_real_data.py executes four routes:
public artifact discovery, faithful regeneration capability audit, aggregate
reconstruction, and assumption-preserving falsification.

Observed result: exact prediction caches, row IDs and shuffle maps, Azure
deployment/stochastic provenance, ARMMAN records, and OW-L implementation are
unavailable. Aggregate percentages do not identify the underlying joint
predictions, and no valid assumption-preserving counterexample was found.

Verdict: BLOCKED. No real-data accuracy or current score is claimed.

## C5 — 47 of 48 ensemble wins

Paper anchor: Appendix E.4.

Production path: repro/claims/claim5_tables.py parses the 16 ensembles on each
of UltraFeedback, MMLU, and ARMMAN and checks the complete 2x2x2x2 design.
Integer and quantifier mutations are rejected.

Observed result: OW-L beats majority voting in 47 of 48 published rows:
16/16 on UltraFeedback, 16/16 on MMLU, and 15/16 on ARMMAN. The published
0.54–14.20 percentage-point range is separately identified as a best-method
range rather than OW-L’s own range.

Verdict: VERIFIED_SCOPED. This verifies published aggregate tables, not raw
inference caches.

## C6 — Bradley–Terry inverse-logit connection

Paper anchor: Corollary 1.

Production path: repro/claims/claim6_bt.py derives the binary OW score as
log(x/(1-x)), derives the same score difference from Bradley–Terry, and checks
the identity with exact rational composition and 60-digit Decimal arithmetic.
Endpoint, offset, and positive/negative scaling controls are included.

Observed result: the exact identity passes all recorded controls.

Verdict: VERIFIED_SCOPED. The result is algebraic and scoped to the stated
binary model.
