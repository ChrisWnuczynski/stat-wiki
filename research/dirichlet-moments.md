# dirichlet-moments

Depth pass: batch AD, rank 503.

## Sources read

- `blei_ng_jordan2003`: (§3, p.996, Eq.1); (§A.1, p.1018)
- `deisenroth_faisal_ong2020`: (§6.6.1, pp.208–210, Table6.2)

The full Blei–Ng–Jordan2003 JMLR paper was read for its Dirichlet density and log-moment appendix. The restaurant table was reproduced exactly to three decimals using R4.5.0, seed3500 and100000 gamma-normalised draws. Python also verifies all four means, three exact beta intervals and an independent contrast simulation.

MML uses the official Cambridge2020 author copy, revision2024-01-15, with printed page labels.

External reference PDFs/text remain outside the repository.

## Mathematical verification

`checks/dirichlet-moments.py` independently recomputes numerical/algebraic claims and inspects the generated article. It passed after the final successful build.

## Generated audit

The article has 14 located inline citations from at least two independent proper works and two answered self-checks. There are no raw citation markers, hidden-answer citations, banned editorial wording or proof debts. Exact unchanged source/header/script predicates pass.

## Validation

The final build passed. The previous complete repository run passed all 517 numerical scripts and 71 of 72 test methods; its only failure was an unrelated shared heading check. After both shared heading corrections, another successful build and the unchanged focused method passed. All 15 AD checks passed on that build. Offline verification passed all 665 bibliography entries; final generated audits and global git diff --check passed. The coordinator will run the complete final suite after integration. No unit tests, fixtures, generator or shared inputs were edited by this batch.

## Integration

The coordinator integrated 47 exact shared substitutions, proper-source metadata and five theorem self-check mappings from ignored pending JSON. Only the 45 assigned AD content/log/check files are included in the commit; pending, shared and generated files are excluded.
