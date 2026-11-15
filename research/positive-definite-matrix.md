# Positive definite matrix

Type: Concept/topic.

## Existing material read

- `articles/positive-definite-matrix.qmd` before the edit: quadratic-form definition, covariance semi-definiteness, Sylvester's strict and weak tests, three inline citations, and ten question links. Leading body: 216 words; no figures.
- `sources/stat3006/chapters/sl-01-multivariate-normal.qmd` around covariance, best linear prediction, and multivariate-normal density; `sources/stat3006/chapters/sl-19-graphical-models.qmd` for invertible covariance and precision use.
- `questions/ex-sl-01-1.qmd`, `questions/ex-sl-17-5.qmd`, and `questions/ex-sl-02-7.qmd`, including available answers.

## Sources opened and facts used

1. James Joseph Sylvester, [1852 paper on reducing quadratic polynomials](https://en.wikisource.org/wiki/A_demonstration_of_the_theorem_that_every_homogeneous_quadratic_polynomial_is_reducible_by_real_orthogonal_substitutions_to_the_form_of_a_sum_of_positive_and_negative_squares), original text transcribed on Wikisource. Read its treatment of orthogonal reduction, real characteristic roots, principal determinants, and invariant signs of quadratic forms. Existing key `sylvester1852`.
2. Golub and Van Loan, [*Matrix Computations*, 4th edition, chapter 4](https://www.ee.iitb.ac.in/~belur/uplod/golub-van-loan-matrix-computations-2012-edition-4th.pdf), especially §4.2 and the Cholesky factorisation theorem. [Publisher record](https://www.press.jhu.edu/books/title/10678/matrix-computations) confirms the fourth edition and 2013 publication. Existing key `golub_vanloan2013`.
3. Anderson, *An Introduction to Multivariate Statistical Analysis* (2003), existing source-chapter reference for covariance and normal-density use. Full book text unavailable; the quadratic-form covariance identity is present in the source chapter and proved in the new collapsed box. Existing key `anderson2003_mva`.

## Verification and decisions

- The original definition, strict and weak Sylvester statements, citations, and ten question links remain. No figure or example was removed.
- The hand-specified lead now uses the correct indefinite article and names linear algebra as well as statistics.
- The single collapsed proof covers the spectral and principal-minor criteria, covariance semi-definiteness, invertibility, diagonal adjustment, Cholesky factorisation, and the Gram-matrix relationship.
- `checks/positive-definite-matrix.py` verifies the new 2-by-2 example and counterexample and the retained linked question's impossible 3-by-3 correlation matrix.
- History attributes quadratic-form and determinant analysis to the opened Sylvester paper; it does not claim he introduced covariance matrices or Cholesky algorithms.
