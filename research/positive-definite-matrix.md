# Positive definite matrix

Type: Concept/topic.

## Existing material read

- `articles/positive-definite-matrix.qmd` before the edit: quadratic-form definition, covariance semi-definiteness, Sylvester's strict and weak tests, three inline citations, and ten question links. Leading body: 216 words; no figures.
- `sources/stat3006/chapters/sl-01-multivariate-normal.qmd` around covariance, best linear prediction, and multivariate-normal density; `sources/stat3006/chapters/sl-19-graphical-models.qmd` for invertible covariance and precision use.
- `questions/ex-sl-01-1.qmd`, `questions/ex-sl-17-5.qmd`, and `questions/ex-sl-02-7.qmd`, including available answers.

## Sources opened and facts used

1. James Joseph Sylvester, [1852 paper on reducing quadratic polynomials](https://en.wikisource.org/wiki/A_demonstration_of_the_theorem_that_every_homogeneous_quadratic_polynomial_is_reducible_by_real_orthogonal_substitutions_to_the_form_of_a_sum_of_positive_and_negative_squares), original text transcribed on Wikisource. Read its treatment of orthogonal reduction, real characteristic roots, principal determinants, and invariant signs of quadratic forms. Existing key `sylvester1852`.
2. Golub and Van Loan, [*Matrix Computations*, 4th edition, chapter 4](https://www.ee.iitb.ac.in/~belur/uplod/golub-van-loan-matrix-computations-2012-edition-4th.pdf), especially §4.2 and the Cholesky factorisation theorem. [Publisher record](https://www.press.jhu.edu/books/title/10678/matrix-computations) confirms the fourth edition and 2013 publication. Existing key `golub_vanloan2013`.
3. Korbinian Strimmer, [*Multivariate Statistics and Machine Learning*, Ch. 1 §1.1](https://strimmerlab.github.io/publications/lecture-notes/MATH38161/01-multivariate.html), opened for covariance symmetry, semi-definiteness, eigenvalues, and the linear-combination variance identity. Key `strimmer2025_mva`.

The first draft cited Anderson (2003) without opening the book. Its citations in this article and the copied covariance paragraph were replaced with Strimmer's located lecture notes. The original Sylvester paper is used for its quadratic-form and eigenvalue history, while the modern matrix text supports the leading-minor and Cholesky claims.

## Verification and decisions

- The definition, strict and weak Sylvester statements, and ten question links remain. No figure or example was removed. The added link-only “Check yourself” section was removed because those links are already in the generated question list.
- The hand-specified lead now uses the correct indefinite article and names linear algebra as well as statistics.
- The single collapsed proof covers the spectral and principal-minor criteria, covariance semi-definiteness, invertibility, diagonal adjustment, Cholesky factorisation, and the Gram-matrix relationship.
- `checks/positive-definite-matrix.py` verifies the 2-by-2 example and counterexample, asserts their printed values, and checks the linked question's impossible 3-by-3 correlation matrix.
- History attributes quadratic-form and determinant analysis to the opened Sylvester paper; it does not claim he introduced covariance matrices or Cholesky algorithms.
