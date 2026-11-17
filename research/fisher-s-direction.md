# fisher-s-direction

Depth pass: batch AD, rank 513.

## Sources read

- `witten_tibshirani2011_fisher`: (§2.1); (§§1–2.1)
- `deisenroth_faisal_ong2020`: (§3.2, pp.73–74; §3.3, p.75); (§3.3, p. 75, Eq. 3.17); (§3.3, p.75, Eq.3.17)

Witten–Tibshirani2011 full peer-reviewed PMC manuscript §2.1 and MML §3.3p75 Eq3.17 were read. The factor1/2 in the criterion is preserved. Fisher1936 scans were unreadable, so the added account uses the accessible proper treatment.

MML uses the official Cambridge2020 author copy, revision2024-01-15, with printed page labels.

External reference PDFs/text remain outside the repository.

## Mathematical verification

`checks/fisher-s-direction.py` independently recomputes numerical/algebraic claims and inspects the generated article. It passed after the final successful build.

## Generated audit

The article has 9 located inline citations from at least two independent proper works and two answered self-checks. There are no raw citation markers, hidden-answer citations, banned editorial wording or proof debts. Exact unchanged source/header/script predicates pass.

## Validation

The final build passed. The previous complete repository run passed all 517 numerical scripts and 71 of 72 test methods; its only failure was an unrelated shared heading check. After both shared heading corrections, another successful build and the unchanged focused method passed. All 15 AD checks passed on that build. Offline verification passed all 665 bibliography entries; final generated audits and global git diff --check passed. The coordinator will run the complete final suite after integration. No unit tests, fixtures, generator or shared inputs were edited by this batch.

## Integration

The coordinator integrated 47 exact shared substitutions, proper-source metadata and five theorem self-check mappings from ignored pending JSON. Only the 45 assigned AD content/log/check files are included in the commit; pending, shared and generated files are excluded.
