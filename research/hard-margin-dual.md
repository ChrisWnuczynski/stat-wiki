# hard-margin-dual

Depth pass: batch AD, rank 517.

## Sources read

- `deisenroth_faisal_ong2020`: (§12.2.2, pp.376–377); (§12.3, pp.383–385); (§12.3.1, pp.383–385)
- `burges1998`: (§§3.1–3.2); (§§3.1–3.2; §3.5)

The corrected Burges1998 ENS-hosted author preprint was read: §§3.1–3.2 cover separability/KKT, while §3.5 covers soft margins. Section labels avoid mixing preprint and journal pagination. MML §§12.2.2 and12.3.1 were read.

MML uses the official Cambridge2020 author copy, revision2024-01-15, with printed page labels.

External reference PDFs/text remain outside the repository.

## Mathematical verification

`checks/hard-margin-dual.py` independently recomputes numerical/algebraic claims and inspects the generated article. It passed after the final successful build.

## Generated audit

The article has 11 located inline citations from at least two independent proper works and two answered self-checks. There are no raw citation markers, hidden-answer citations, banned editorial wording or proof debts. Exact unchanged source/header/script predicates pass.

## Validation

The final build passed. The previous complete repository run passed all 517 numerical scripts and 71 of 72 test methods; its only failure was an unrelated shared heading check. After both shared heading corrections, another successful build and the unchanged focused method passed. All 15 AD checks passed on that build. Offline verification passed all 665 bibliography entries; final generated audits and global git diff --check passed. The coordinator will run the complete final suite after integration. No unit tests, fixtures, generator or shared inputs were edited by this batch.

## Integration

The coordinator integrated 47 exact shared substitutions, proper-source metadata and five theorem self-check mappings from ignored pending JSON. Only the 45 assigned AD content/log/check files are included in the commit; pending, shared and generated files are excluded.
