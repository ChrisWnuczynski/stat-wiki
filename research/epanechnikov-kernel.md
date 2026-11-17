# epanechnikov-kernel

Depth pass: batch AD, rank 507.

## Sources read

- `silverman1986`: (§2.4); (§2.4, Eqs.2.2–2.2a)
- `epanechnikov1969`: (§2, pp.155–156); (§2, pp.155–156, Eq.13); (§§1–2, pp.154–156)
- `deisenroth_faisal_ong2020`: (§6.5, pp.197–199)

The full Epanechnikov1969 SIAM paper §§1–2pp154–156 and Silverman1986 book excerpt §2.4 were read. The unit-variance scaling in Eq13 was distinguished from support-one scaling. The fixed-second-moment L2 minimisation has a direct proof in the article.

MML uses the official Cambridge2020 author copy, revision2024-01-15, with printed page labels.

External reference PDFs/text remain outside the repository.

## Mathematical verification

`checks/epanechnikov-kernel.py` independently recomputes numerical/algebraic claims and inspects the generated article. It passed after the final successful build.

## Generated audit

The article has 10 located inline citations from at least two independent proper works and two answered self-checks. There are no raw citation markers, hidden-answer citations, banned editorial wording or proof debts. Exact unchanged source/header/script predicates pass.

## Validation

The final build passed. The previous complete repository run passed all 517 numerical scripts and 71 of 72 test methods; its only failure was an unrelated shared heading check. After both shared heading corrections, another successful build and the unchanged focused method passed. All 15 AD checks passed on that build. Offline verification passed all 665 bibliography entries; final generated audits and global git diff --check passed. The coordinator will run the complete final suite after integration. No unit tests, fixtures, generator or shared inputs were edited by this batch.

## Integration

The coordinator integrated 47 exact shared substitutions, proper-source metadata and five theorem self-check mappings from ignored pending JSON. Only the 45 assigned AD content/log/check files are included in the commit; pending, shared and generated files are excluded.
