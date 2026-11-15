# Degrees of freedom

Type: Concept/topic.

## Existing material read

- `articles/degrees-of-freedom.qmd` before the edit: chi-squared definition, $n-1$ and $n-p$ interpretations, table count, two-normal-observation calculation, 31 linked questions, no figures. Leading body: 524 words under the `PROGRESS.md` count.
- `sources/stat2004/chapters/inf-01-statistical-inference.qmd`, sample variance and chi-squared derivations; `sources/stat2004/chapters/inf-05-chi-square.qmd`, table dimension count; and `sources/stat2004/chapters/inf-06-regression.qmd`, normal-error residual argument.
- `questions/ex-inf-degrees-of-freedom.qmd` and `questions/ex-ur-basis-dimension.qmd`, with their hidden answers.

## Sources opened and facts used

1. R. A. Fisher, [“On the Interpretation of χ² from Contingency Tables, and the Calculation of P”](https://jhanley.biostat.mcgill.ca/bios601/Proportion/FisherChiSqDegreesFreedom1922.pdf), *Journal of the Royal Statistical Society* 85 (1922), pp. 87–94, especially pp. 87–90. Read the original explanation that fixed row and column margins reduce the dimension of discrepancies and its $(r-1)(c-1)$ calculation. Used for the table proof sketch and history. Citation key `fisher1922_chisq`.
2. NIST/SEMATECH, [e-Handbook of Statistical Methods, §5.5.9.9.2](https://www.itl.nist.gov/div898/handbook/pri/section5/pri5992.htm), first published 2002. Read the residual-standard-deviation formula using $n-p$ fitted coefficients. Used for the regression definition, example, and interpretation. Citation key `nist_residual_std2002` (added in this commit).
3. The source chapter's normal-sample and regression arguments cite Casella and Berger, *Statistical Inference*, 2nd ed. (2002), as `casella_berger2002`. The book's full text was not available here, so each formula used in the new prose was independently checked through the source chapters and the proof in this article; no claim about an unseen passage of the book is made.

## Verification and decisions

- The lead was changed to plural agreement: “degrees of freedom are”. The infobox and existing interpretation remain.
- The proof uses projection rank for the exact normal-model result and a dimension count plus Fisher's large-sample argument for tables. It also checks the existing equal-pairwise-correlation expectation formula. Exact table and regression counts and every new numerical example are recomputed in `checks/degrees-of-freedom.py`.
- The OpenStax formula review was opened during source discovery but has a restriction against ingesting it into generative AI offerings, so no article claim or citation was taken from it.
- No existing figure, definition, citation, or example was removed.
