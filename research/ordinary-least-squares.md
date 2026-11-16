# Ordinary least squares — rank 101

Type: Theorem/proposition in the generator, describing a method. Frozen baseline 2,712 body words and one figure. The original full-rank formula, normal and Student results, least-squares decomposition, eight-point regression, Bayesian example, prediction figure and infobox remain generated. The researched layer separates algebra from sampling assumptions and adds a compact three-point fit.

## Sources read

- **Checked:** Cosma R. Shalizi, *The Truth about Linear Regression* (author-hosted complete manuscript, 20 October 2025), https://www.stat.cmu.edu/~cshalizi/TALR/TALR.pdf. Read Chapter 4 §§4.1–4.7 pp. 50–63, Chapter 7 §§7.1–7.2 pp. 115–124, Chapter 11 §§11.1–11.3 pp. 187–195, Chapter 12 §§12.2–12.5 pp. 202–210, Chapter 13 §13.2 pp. 216–223, Chapter 15 §15.4 pp. 265–270, and Chapter 21 §21.1–21.2 pp. 351–362. The author explicitly distinguishes algebraic fitting, mean/variance claims and exact Gaussian inference.
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics* (2008), local authorized printed pp. 304–305, “Least-Squares Method,” for the minimisation and the 1805 Legendre history.
- **Checked:** The Springer publisher page for Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning* (2009), Ch. 3, identifies the chapter, but the full text was not accessible there. It is not used as a new citation. The existing page's historical Legendre, Gauss and Fisher citations are inherited from the source, not newly asserted here.
- **Checked by code:** `checks/ordinary-least-squares.py` recomputes the new three-point and four-point examples, the inherited eight-point least-squares coefficients, residual sum of squares and selected interval/prediction numbers, plus algebraic projector identities.
- **Assumed:** The numerical examples are illustrative fits to fixed design points. The probabilistic proof explicitly states fixed full-rank design, zero-mean spherical errors, and Gaussian errors for exact normal and Student laws; $n>p$ is needed for the residual variance estimate.
- **Disputed:** The stock lead places OLS only “in Bayesian statistics.” This is too narrow for a general regression method, so pending `article_lead` proposes a one-sentence replacement. Existing Bayesian worked examples are retained as one application.

## Proof and bank

One collapsed proof covers the normal equations, uniqueness, Pythagorean decomposition, unbiasedness, covariance, expected SSE, Gaussian projection laws, Student pivot and the MLE/unbiased variance divisors. The three proposed answered bank questions cover normal equations, a line through the origin and an advertising regression interval. They do not duplicate the inherited eight-point or Bayesian-posterior examples. No unresolved mathematical result is added.
