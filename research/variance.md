# Variance

Type: Concept/definition.

## Existing material read

- `articles/variance.qmd` before the edit: definition, unit-uniform worked example, two-dice game, 116 linked questions, no figures. Leading body had 393 words under the counting method in `PROGRESS.md`.
- `notes/prob-02-random-variables.qmd`, “Expectation and variance,” especially definition `def-variance` and the immediately following scaling paragraph. Also checked the original source at `sources/stat2003/chapters/prob-02-random-variables.qmd`.
- `questions/ex-prob-second-moment.qmd`, `questions/ex-prob-normal-variance.qmd`, and `questions/ex-prob-uniform-variance.qmd`, including their existing hidden answers.

## Sources opened and facts used

1. Grinstead, C. M. and Snell, J. L., *Introduction to Probability*, 2nd revised edition, AMS, 1997. [Dartmouth full text](https://math.dartmouth.edu/~prob/prob/prob.pdf), chapter 6, §§6.2–6.3, pp. 257–261, 268–269. Read the definition, second-moment identity, affine scaling, independent-sum proof, and average-of-independent-trials formula. Used for the definition, properties, proof, and sampling interpretation. The freely available PDF is a later 2006 revision of the 1997 edition; formulas were checked in that revision. Citation key `grinstead_snell1997`.
2. Fisher, R. A., “[The Correlation between Relatives on the Supposition of Mendelian Inheritance](https://www.cambridge.org/core/journals/earth-and-environmental-science-transactions-of-royal-society-of-edinburgh/article/abs/xvthe-correlation-between-relatives-on-the-supposition-of-mendelian-inheritance/A60675052E0FB78C561F66C670BC75DE),” *Transactions of the Royal Society of Edinburgh* 52(2), 1919, pp. 399–433, especially p. 399 where he motivates the square of standard deviation and names variance. The paper was read in 1918 and printed in the 1919 volume. Used only for the historical paragraph. Citation key `fisher1919_variance`.
3. NIST/SEMATECH, [e-Handbook of Statistical Methods, §1.3.5.6 “Measures of Scale”](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm), first published 2002. Read variance/standard deviation definitions and discussion of long tails, Cauchy data, and median absolute deviation. Used for the tail caution and unit interpretation. Citation key `nist_handbook2002`.
4. [Wikipedia: Variance](https://en.wikipedia.org/wiki/Variance), definition and properties, opened as a cross-check only; not cited.

## Verification and decisions

- Every added formula was checked against Grinstead–Snell §§6.2–6.3 or the source chapter. The numeric example and prompt were recomputed in `checks/variance.py` using exact rational arithmetic.
- The statement about zero variance is accompanied by a proof using a nonnegative random variable and Markov's inequality. The covariance identity proof covers dependent variables and the independent special case.
- The original page had no figures. Its definition, citations, and both existing worked examples remain. No existing content was removed.
- Fisher's read year and publication year are explicitly distinguished because different catalogues display 1918 and 1919.
