# full-conditionals-under-independent-priors

Depth pass: batch AD, rank 515.

## Sources read

- `gelfand_smith1990`: (§3.5, p.405); (§§2.3–2.4, pp.400–401); (§§2.3–2.4, pp.400–401; §3.5, p.405); (§§3.4–3.5, p.405)
- `deisenroth_faisal_ong2020`: (§6.5.2, p.201, Eqs.6.74–6.75; §6.6.1, p.209, Table6.2); (§6.6.1, p.209, Table6.2)

The full published Gelfand–Smith1990 paper was read. Gibbs sampling is in §§2.3–2.4pp400–401, rather than §2.2. Its normal-means model §3.5p405 and MML Gaussian-product/conjugacy sections support the independent-prior calculations.

MML uses the official Cambridge2020 author copy, revision2024-01-15, with printed page labels.

External reference PDFs/text remain outside the repository.

## Mathematical verification

`checks/full-conditionals-under-independent-priors.py` independently recomputes numerical/algebraic claims and inspects the generated article. It passed after the final successful build.

## Generated audit

The article has 12 located inline citations from at least two independent proper works and two answered self-checks. There are no raw citation markers, hidden-answer citations, banned editorial wording or proof debts. Exact unchanged source/header/script predicates pass.

## Validation

The final build passed. The previous complete repository run passed all 517 numerical scripts and 71 of 72 test methods; its only failure was an unrelated shared heading check. After both shared heading corrections, another successful build and the unchanged focused method passed. All 15 AD checks passed on that build. Offline verification passed all 665 bibliography entries; final generated audits and global git diff --check passed. The coordinator will run the complete final suite after integration. No unit tests, fixtures, generator or shared inputs were edited by this batch.

## Integration

The coordinator integrated 47 exact shared substitutions, proper-source metadata and five theorem self-check mappings from ignored pending JSON. Only the 45 assigned AD content/log/check files are included in the commit; pending, shared and generated files are excluded.
