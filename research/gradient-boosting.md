# gradient-boosting

Depth pass: batch AD, rank 516.

## Sources read

- `natekin_knoll2013`: (§2.4); (§2.4, Algorithm1; §4.2); (§3.1.1; §4.2); (§§2.1–2.3; §4.2); (§§2.3–2.4); (§§2.3–2.4; §§3.1.1–3.1.2); (§§3.1.1–3.1.2)
- `freund_schapire1997`: (§4.1, pp.125–126, Fig.2)

The full peer-reviewed Natekin–Knoll2013 Frontiers paper §§2.1–2.4,3.1.1–3.1.2 and4.2 was read, together with Freund–Schapire1997 §4.1pp125–126. Friedman2001 author URLs failed and the CMI copy was scan-only; accessible peer-reviewed treatments support the added text.

External reference PDFs/text remain outside the repository.

## Mathematical verification

`checks/gradient-boosting.py` independently recomputes numerical/algebraic claims and inspects the generated article. It passed after the final successful build.

## Generated audit

The article has 9 located inline citations from at least two independent proper works and two answered self-checks. There are no raw citation markers, hidden-answer citations, banned editorial wording or proof debts. Exact unchanged source/header/script predicates pass.

## Validation

The final build passed. The previous complete repository run passed all 517 numerical scripts and 71 of 72 test methods; its only failure was an unrelated shared heading check. After both shared heading corrections, another successful build and the unchanged focused method passed. All 15 AD checks passed on that build. Offline verification passed all 665 bibliography entries; final generated audits and global git diff --check passed. The coordinator will run the complete final suite after integration. No unit tests, fixtures, generator or shared inputs were edited by this batch.

## Integration

The coordinator integrated 47 exact shared substitutions, proper-source metadata and five theorem self-check mappings from ignored pending JSON. Only the 45 assigned AD content/log/check files are included in the commit; pending, shared and generated files are excluded.
