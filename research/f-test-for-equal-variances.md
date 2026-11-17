# f-test-for-equal-variances

Depth pass: batch AD, rank 510.

## Sources read

- `siegrist2022_normals`: (§6.08, “Ratios of Sample [Variances](variance.qmd); (§6.8, “Ratios of Sample Variances”); (§6.8, “Ratios of Sample [Variances](variance.qmd); (§6.8, “The Sample Variance”; “Ratios of Sample Variances”); (§6.8, “The Two Sample Model”)
- `dodge2008`: (p.205)

Siegrist full textbook §6.8 was read for the normal-sample chi-square and F pivots. Dodge printed p205 (PDF page208) was read for the independent chi-square ratio. The named result has a proper non-Dodge derivation.

External reference PDFs/text remain outside the repository.

## Mathematical verification

`checks/f-test-for-equal-variances.py` independently recomputes numerical/algebraic claims and inspects the generated article. It passed after the final successful build.

## Generated audit

The article has 10 located inline citations from at least two independent proper works and two answered self-checks. There are no raw citation markers, hidden-answer citations, banned editorial wording or proof debts. Exact unchanged source/header/script predicates pass.

## Validation

The final build passed. The previous complete repository run passed all 517 numerical scripts and 71 of 72 test methods; its only failure was an unrelated shared heading check. After both shared heading corrections, another successful build and the unchanged focused method passed. All 15 AD checks passed on that build. Offline verification passed all 665 bibliography entries; final generated audits and global git diff --check passed. The coordinator will run the complete final suite after integration. No unit tests, fixtures, generator or shared inputs were edited by this batch.

## Integration

The coordinator integrated 47 exact shared substitutions, proper-source metadata and five theorem self-check mappings from ignored pending JSON. Only the 45 assigned AD content/log/check files are included in the commit; pending, shared and generated files are excluded.
