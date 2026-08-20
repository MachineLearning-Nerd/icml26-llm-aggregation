# Branch audit

The original experiment tree used opaque `orx/*` refs. Each ref is mapped to a
purpose-driven public branch below; the legacy names are retained only as
lineage, not as the final branch interface.

| Final branch | Legacy source ref | Source tip before documentation changes | Purpose |
| --- | --- | --- | --- |
| `main` | `master` | `644d3c454b3d8e35053c9302e8257a00dcb520ee` | Documentation and publication surface |
| `historical/judged-baseline` | `orx/baseline-judged-reproduction-with-locked-uv-envi` | `5b8f7635f426857cbe69747eac1c1f18652e6d55` | Frozen judged baseline and locked environment |
| `release/c1-evidence` | `orx/claim-1-evaluator-visible-evidence-milestone` | `a618fe5bd19968cd8dd820039cf7cb166928cec2` | Evaluator-visible c1 evidence |
| `audit/c1-ow-bayes` | `orx/claim-1-universal-ow-bayes-proof-certificate` | `058717d1224728e1aa64f2067eb3e6ecb266206b` | Universal OW/MAP certificate |
| `release/c2-evidence` | `orx/claim-2-evaluator-visible-exact-evidence` | `541fb31b267a531a9913193a2438119c5715ab4a` | Evaluator-visible c2 evidence |
| `audit/c2-isp-ordering` | `orx/claim-2-universal-isp-mv-sp-proof-certificate` | `389613ee48ec988d25c64b66a91349ba5e89e386` | Universal ISP/MV/SP certificate |
| `audit/c3-full-simulation` | `orx/claim-3-89-replicate-full-simulation` | `487619616606323f25dbac108c646cfd023ec2cf` | 89-seed full simulation |
| `audit/c3-calibration-pilot` | `orx/claim-3-calibrated-simulation-pilot` | `3e07ac79de32326520774e79c0fa62a5625caa21` | Simulation repeat-count calibration |
| `release/c3-evidence` | `orx/claim-3-evaluator-visible-full-evidence` | `ea2e67932166b98b7266e3c4fbfeacf570fed5b1` | Evaluator-visible c3 evidence |
| `release/c4-blocked-evidence` | `orx/claim-4-evaluator-visible-blocked-evidence` | `f63729b0422a787501c1fae2afa4a70668a6644f` | Evaluator-visible blocked c4 package |
| `audit/c4-real-data` | `orx/claim-4-four-route-real-data-access-audit` | `75d54637917cc31e247149c389154b73f13272af` | Four-route real-data audit |
| `release/c5-evidence` | `orx/claim-5-evaluator-visible-exact-evidence` | `2b75e12762c75b3ccbbf5df7485aedc2b2196940` | Evaluator-visible c5 evidence |
| `audit/c5-ensemble-aggregate` | `orx/claim-5-exact-48-row-ensemble-aggregate` | `fdcb642148ffb3872e43ac2d5f013b5ef4c91d3a` | Exact 48-row Appendix audit |
| `audit/c6-bradley-terry` | `orx/claim-6-bradley-terry-inverse-logit-certificate` | `94301164890bf3985097517e9e08b1aa46b22fc5` | Bradley–Terry inverse-logit certificate |
| `release/c6-evidence` | `orx/claim-6-evaluator-visible-proof-evidence` | `6df1b080dacd40ad5ab01293d75c23120404c3bb` | Evaluator-visible c6 evidence |
| `release/final-gates` | `orx/final-report-notebook-and-release-gates` | `000a32f61fe88d7f5e16f9df47d05ed4dc99a077` | Final report, notebook, and gates |
| `release/gate-closure` | `orx/release-gate-closure-and-publication-candidate` | `6c246ece1fe260ff40bcd0cd8a293697f24a732e` | Publication-candidate closure |
| `release/metadata-audit` | `orx/release-metadata-and-evaluator-blind-audit` | `9aa15b7a8c85ba0d90eb42d8f9f7f19063cd577e` | Metadata and visibility audit |

## Final verification contract

After normalization, the public repository must satisfy all of the following:

- exactly the 18 final branches in the table are present;
- `main` is the default branch;
- every branch contains the current README and this audit record;
- every reachable commit author and committer uses
  MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>;
- active README/report links use the renamed repository and final branch names; and
- whitespace, identity, branch, and GitHub API metadata checks pass.

The historical Space and OpenResearch records may mention the original runner
names as provenance; those names are not active public branch refs.
