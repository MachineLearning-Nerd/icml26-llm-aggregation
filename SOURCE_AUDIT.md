# Source audit

## Paper record

- Title: Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information
- Authors: Rui Ai, Yuqi Pan, David Simchi-Levi, Milind Tambe, and Haifeng Xu
- Source: arXiv 2510.01499, version 2
- Venue context: accepted at ICML 2026
- Paper URL: https://arxiv.org/abs/2510.01499

The source-anchored claim contracts and hashes are retained under
docs/CLAIMS_PINNED.md, .openresearch/artifacts, and
space_candidate/evidence. This repository records an independent audit and does
not claim ownership of the paper’s models, data, or inference records.

## Claim-to-source mapping

| Audit claim | Paper anchor | Local implementation or record |
| --- | --- | --- |
| C1 | Theorem 1 | repro/claims/claim1_ow_bayes.py and space_candidate/evidence/claim-1 |
| C2 | Theorem 2 | repro/claims/claim2_isp_ordering.py and space_candidate/evidence/claim-2 |
| C3 | simulation and Theta(1/K) gap | repro/claims/claim3_simulation.py and space_candidate/evidence/claim-3 |
| C4 | real-data Table 3 | repro/claims/claim4_real_data.py and space_candidate/evidence/claim-4 |
| C5 | Appendix E.4 | repro/claims/claim5_tables.py and space_candidate/evidence/claim-5 |
| C6 | Corollary 1 | repro/claims/claim6_bt.py and space_candidate/evidence/claim-6 |

## Scope and divergence audit

- C1, C2, and C6 use exact symbolic, rational, or high-precision checks under
  the paper’s assumptions.
- C3 is a seeded CPU simulation; its 89 seeds and 801 settings are independent
  evidence, not the authors’ original inference trace.
- C5 reconstructs published aggregate rows and does not recover raw LLM
  predictions.
- C4 is blocked because caches, provenance, row mappings, and the paper’s OW-L
  implementation are unavailable. The four completed routes are preserved as
  evidence for the block.
- The historical live judge result is 0/12. The repository makes no current
  score claim.

## Attribution audit

The paper authors remain the authors of the paper and its claims. The
MachineLearning-Nerd identity applies only to this independent audit repository,
its documentation, and its normalized reachable history.
