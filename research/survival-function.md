# Survival function — research notes (rank 203)

## Source record

- Checked: NIST/SEMATECH, *Engineering Statistics Handbook*, §8.1.2.2, full public page at https://www.itl.nist.gov/div898/handbook/apr/section1/apr122.htm, opened 2026-11-16. It defines survival/reliability as `1-F` and gives independent-system calculation.
- Checked: Kaplan and Meier (1958), pp. 457–467, full original paper hosted by McGill biostatistics course at https://jhanley.biostat.mcgill.ca/bios601/SurvivalAnalysis/KaplanMeier1958.pdf, opened 2026-11-16. First page states the target `P(T>t)`, censoring independence assumption and product-limit formula; §2 gives definition and mean-lifetime discussion.
- Checked: Cox (1972), pp. 187–190, full original journal scan hosted by Stanford at https://web.stanford.edu/~lutian/coursepdf/cox1972paper.pdf, opened 2026-11-16. Defines survivor and hazard and states the motivation for regression with censored failures. Cox uses `P(T≥t)`; for continuous lifetimes this equals `P(T>t)`, but not for atomic lifetimes.
- Checked: original chapter `sources/stat2003/chapters/prob-07-reliability.qmd`, Survival function and Hazard sections, for preservation of the reliability-system figure and formulas.
- Checked by algebra/code: exponential example, conditional survival ratio, mean-as-area, and two-component series/parallel probabilities.
- Assumed: in the censoring example, independent censoring within groups; explicitly stated where relevant.
- Disputed: no claim that survival and hazard alone identify the effect of treatment in observational data. No priority claim for the survival-function terminology.
- Dodge: index has no dedicated survival/reliability/hazard entry; source present and searched.

## Preservation

Baseline has 616 words and one figure. The generator retains the source chapter's system-survival figure, definition, and linked question. Research prose develops those features rather than replacing them.
