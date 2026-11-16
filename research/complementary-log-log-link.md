# Complementary log-log link — research notes (rank 210)

## Sources read

- Checked: McCullagh (1980), *Regression Models for Ordinal Data*, full original paper from the author's University of Chicago page, https://www.stat.uchicago.edu/~pmcc/pubs/paper2.pdf, opened 2026-11-16. §3.1, pp. 113–114 derives the complementary log-log transformation from proportional hazards; §3.2, pp. 114–115 applies it to grouped family-income data; §4.1, pp. 115–116 compares link interpretations and notes reversal asymmetry.
- Checked: sources/book/chapters/01-introduction-to-glms.qmd and 04-categorical-responses.qmd. Preserve the binomial link equation and original linked questions. The chapter's phrase “coefficient is a log-hazard, an instantaneous risk” compresses a conditional interpretation; the page should say precisely that a coefficient multiplies the cumulative hazard (or interval integrated hazard in a grouped-time model) by its exponential, under the corresponding model.
- Checked by code: inverse-link probabilities, link values, asymmetry and hazard-ratio calculations in examples.
- Assumed: independent Bernoulli response when used as a binary GLM, and a genuine grouped survival interpretation only if the event variable and time intervals warrant it.
- Disputed: a cloglog coefficient is not an odds ratio, and the link's mere use does not prove a proportional-hazards data-generating mechanism.
- Dodge: the printed “Complementary” entry on p. 102 concerns complement events, not this link; no direct link entry found.

## Preservation

Baseline has 563 words and zero figures. Retain source equation, question and infobox facts.
