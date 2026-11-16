# Conditional expectation

Type: Concept/topic.

## Existing material read

- `articles/conditional-expectation.qmd` before the edit: the conditional-mean definition, the random-variable and tower-property sentence, the best-predictor and jointly normal claims, and the sample conditional-mean line from the multivariate-normal chapter. Citations present: Kolmogorov 1933, Doob 1953, Grimmett–Stirzaker 2020, and Durrett 2019. Seventeen linked questions. No figures. Leading body: 317 words under the `PROGRESS.md` count.
- `sources/stat2003/chapters/prob-04-joint-distributions.qmd`, the conditional-expectation paragraph, the triangle example, and the tower-property statement; `sources/stat3006/chapters/sl-01-multivariate-normal.qmd`, the conditional-mean line and least-squares comparison.

## Sources opened and facts used

1. Rick Durrett, *Probability: Theory and Examples*, version of 11 January 2019 of the fifth edition, [author PDF](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf). Read §4.1, pp. 205–213 of that PDF. The definition and almost-sure uniqueness are on pp. 205–206. Example 4.1.5 on p. 208 is the average over a positive-probability atom. Example 4.1.6 on p. 209 is the joint-density ratio, including the remark that the function is arbitrary where the marginal integral is zero. Theorem 4.1.13 on p. 211 is the tower property. Theorem 4.1.14 on p. 212 is the pull-out property. Theorem 4.1.15 on pp. 212–213 is the mean-square projection, with the cross-term proof. Example 4.1.3 and Example 4.1.4 give the known-variable and independence cases. Existing key `durrett2019`. The Cambridge printing’s pagination was not compared with this author PDF, so the article cites the book and the page numbers are recorded only for this opened file.
2. The bivariate normal formulas were derived in the proof from the joint exponent and Durrett’s density-ratio mean. No separate Gaussian monograph was opened.
3. Kolmogorov’s English translation, Doob 1953, and Grimmett–Stirzaker 2020 are already cited by the source excerpt. Their full texts were not reopened for this page, and no new sentence depends on them. The Yale copy of Kolmogorov’s translation used for the previous page returned an error on this attempt.

## Verification and decisions

- Added a formula-free lead, motivation tied to the existing random-sum idea, the integral definition, atom and density formulas, the tower and projection properties, the bivariate normal mean and variance, one collapsed proof, a discrete worked example with the variance decomposition, a normal numerical case, a hidden exercise, and a history limited to the opened section.
- The proof also derives the existing claim that \(s_{YX}/s_{XX}\) is the least-squares slope. The original definition, the sample-line display, the four citation keys, and the seventeen question links remain.
- `checks/conditional-expectation.py` checks the discrete means, tower identity, variance split, normal formulas, exercise, and a four-point least-squares slope with exact fractions.
- No figure, definition, example, or practice question was removed. The triangle and shop examples stay in the source chapter; they were not copied onto this article before the edit, so they were not deleted from it.

## Correction pass

- Corrected the conditional-density formula to integrate over the response (y), holding the conditioning value (x) fixed. The arithmetic check now asserts the formula and printed worked values.
- Added locations to citations of Durrett §4.1 and removed the History section, which repeated the mathematical explanation without establishing a historical event. Rephrased references to page assembly as reader-facing exposition.
