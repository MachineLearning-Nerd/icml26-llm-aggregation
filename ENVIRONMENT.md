# Environment and rerun contract

## Runtime

- Python: 3.12
- Dependency management: uv with committed uv.lock
- Standard command: uv run python repro/src/verify.py
- Platform used for the formal campaign: CPU-only Hugging Face cpu-upgrade
- No GPU or proxy real-data run is claimed

## Protocol

- C1 independent Fraction checker: 418 answer profiles
- C2 exact ISP ordering checker: 55 profiles
- C3: N=4 agents, M=10,000 questions, 89 calibrated seeds, nine K values
- C5: 48 published ensemble rows across UltraFeedback, MMLU, and ARMMAN
- C6: exact binary identity with rational and 60-digit Decimal controls

Claim 3 covers 801 full-size settings across the nine K values. The formal
campaign is CPU-intensive; the committed reports retain the command, allocated
CPU, run history, and outputs.

## Local rerun

Install the locked environment and run the cumulative verifier:

    uv sync --frozen
    uv run python repro/src/verify.py
    uv run python repro/tests/test_controls.py

The cumulative verifier updates outputs/verify_results.json. The committed
outputs and the evaluator-visible evidence mirrors are the audit snapshot
checked by verify_final.py.

## Missing inputs

The exact real-data prediction caches, retained row IDs and shuffle maps, Azure
deployment/stochastic provenance, ARMMAN records, and paper OW-L implementation
are absent. C4 therefore cannot be rerun faithfully from this repository.
