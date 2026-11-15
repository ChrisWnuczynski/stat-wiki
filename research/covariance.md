# Covariance

Type: Concept/definition.

## Existing material read

- `articles/covariance.qmd` before the edit: definition, affine-normal property, figure `prob-correlation.png`, uncorrelated-but-dependent and sign-covariance examples, and 39 linked questions. Leading body: 601 words; one figure.
- `sources/stat2003/chapters/prob-04-joint-distributions.qmd`, “Expectation, covariance and matrices,” including the source covariance formula, bilinearity, sum variance, correlation bound, and normal-law discussion.
- `questions/ex-prob-sign-covariance.qmd` and `questions/ex-sl-02-1.qmd`, including their answers.

## Sources opened and facts used

1. Charles M. Grinstead and J. Laurie Snell, [*Introduction to Probability*](https://math.dartmouth.edu/~prob/prob/prob.pdf), 2nd revised edition, AMS; read the freely available later revision, chapter 6, especially exercises 6.2.23 and 6.3.17–20, which state covariance identities, independence's implication, the correlation bound, and the bivariate normal setting. Used for definitions, properties, and proof. Citation key `grinstead_snell1997`.
2. NIST/SEMATECH, [e-Handbook §6.5.4.1](https://www.itl.nist.gov/div898/handbook/pmc/section5/pmc541.htm), first published 2002. Read the worked multivariate-data example, sample covariance calculation, and matrix interpretation. Used for statistical use and connections. Citation key `nist_covariance2002`, added in this commit.
3. NIST/SEMATECH, [e-Handbook §3.1.3.3](https://www.itl.nist.gov/div898/handbook/ppc/section1/ppc133.htm), first published 2002. Read the measurement-error example and variance-of-a-linear-combination formula with its covariance term. Used for motivation and statistical use. Citation key `nist_error_propagation2002`, added in this commit.
4. Karl Pearson, [“Regression, Heredity, and Panmixia”](https://doi.org/10.1098/rsta.1896.0007), *Philosophical Transactions A* 187 (1896), pp. 253–318. The Royal Society publisher record and abstract were available through indexed search, but full text access was blocked. History is limited to the paper's title, stated aim, date, and relation to Galton; it makes no priority claim about the word *covariance*. Citation key `pearson1896`.

## Verification and decisions

- The old figure, definition, affine-normal statement, two examples, citations, and question links remain. No substantive text or figure was removed.
- The new collapsed proof covers the equivalent covariance formula, bilinearity, sum variance, independence, correlation bound and equality, the existing affine-normal result, and unbiasedness of sample covariance. It uses the same $X,Y$ notation as the body.
- All new numerical values and the two existing discrete examples were recomputed with exact fractions in `checks/covariance.py`.
- The first sentence remains plain-language; the new context explains why covariance matters. The inaccessible original paper is reported here rather than used for unsupported historical priority claims.

## Correction pass

- Replaced unopened Pearson, Anderson, Grimmett–Stirzaker, Casella–Berger, and Schwarz citations attached to the source definition and correlation bound with the Grinstead–Snell exercises actually read. Added locations to the NIST and Grinstead–Snell citations throughout the researched prose.
- The History section now makes only the publication-scope claim supported by Pearson's publisher abstract. Rephrased editor-facing references, cited the worked example and answer, and connected the printed values and inherited figure to the arithmetic check. The observational-causality caution uses the opened CDC chapter.
- The first preservation check found the dependent Cauchy–Schwarz article four substantive words below its source baseline after the citation change. The source now states the zero-variance case explicitly, which also explains why the correlation ratio requires positive variances.
