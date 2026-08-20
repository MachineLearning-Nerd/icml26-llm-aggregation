# Reproduction report

## Executive result

This repository provides a partial, transparent clean-room audit of Beyond
Majority Voting. Five of six claim routes are supported within their stated
scope, for 10/12 evidence points. The historical live judge result is 0/12;
there is no current live-judge score claim.

## Results

| Claim | Result | Boundary |
| --- | --- | --- |
| C1 | exact OW/MAP factorization; 418 profiles | theorem assumptions |
| C2 | exact ISP/MV/SP ordering; 55 profiles | premise x_i >= 1/K |
| C3 | 89-seed N=4/M=10,000 simulation | independent CPU campaign |
| C4 | blocked after four routes | real caches and provenance absent |
| C5 | OW-L wins 47 of 48 published rows | aggregate tables, not raw predictions |
| C6 | exact binary OW/Bradley–Terry identity | stated binary model |

## Interpretation

The higher-order aggregation mechanism is supported in the exact theory and
synthetic setting, and the Appendix aggregate is arithmetically reconstructed.
The real-data Table 3 claim remains scientifically inaccessible without the
authors’ finite prediction object. That limitation is a result of the audit,
not a reason to substitute a different LLM run.

## Publication recommendation

The repository is suitable for publication as an explicitly partial audit with
the historical score and C4 block visible. It is not suitable for a claim of
complete paper reproduction or a current judge result.
