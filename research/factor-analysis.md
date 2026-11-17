# factor-analysis

Depth pass: batch AD, rank 511.

## Sources read

- `deisenroth_faisal_ong2020`: (§10.3, pp.331–332, Eqs.10.43–10.44); (§10.7, p.346); (§10.7, pp.345–346); (§6.5.2, p.201, Eqs.6.74–6.75)
- `dempster_laird_rubin1977`: (§3, p.10; §4.7, pp.20–21); (§4.7, pp.20–21; discussion, p.30)

MML factor analysis p346, Gaussian products p201 and squared reconstruction error pp331–332 were read. Dempster–Laird–Rubin1977 §4.7pp20–21, rotation discussion p10 and Heywood discussion p30 were read.

MML uses the official Cambridge2020 author copy, revision2024-01-15, with printed page labels.

External reference PDFs/text remain outside the repository.

## Mathematical verification

`checks/factor-analysis.py` independently recomputes numerical/algebraic claims and inspects the generated article. It passed after the final successful build.

## Generated audit

The article has 11 located inline citations from at least two independent proper works and two answered self-checks. There are no raw citation markers, hidden-answer citations, banned editorial wording or proof debts. Exact unchanged source/header/script predicates pass.

## Validation

The final build passed. The previous complete repository run passed all 517 numerical scripts and 71 of 72 test methods; its only failure was an unrelated shared heading check. After both shared heading corrections, another successful build and the unchanged focused method passed. All 15 AD checks passed on that build. Offline verification passed all 665 bibliography entries; final generated audits and global git diff --check passed. The coordinator will run the complete final suite after integration. No unit tests, fixtures, generator or shared inputs were edited by this batch.

## Integration

The coordinator integrated 47 exact shared substitutions, proper-source metadata and five theorem self-check mappings from ignored pending JSON. Only the 45 assigned AD content/log/check files are included in the commit; pending, shared and generated files are excluded.
