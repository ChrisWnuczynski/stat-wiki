# Least squares research notes

- **Checked:** Legendre (1805), original public-domain appendix “Sur la Méthode des moindres quarrés,” pp. 72–75, institutional reproduction https://www.bibnum.education.fr/sites/default/files/legendre-texte.pdf . Read minimization of squared errors, normal equations, and mean example. Existing bibliography key `legendre1805`.
- **Checked:** NIST/SEMATECH *e-Handbook of Statistical Methods*, §4.4.3.1 https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd431.htm and §4.1.4.1 https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd141.htm . Read definitions, line formulas, linear-in-parameters examples, and outlier/extrapolation limits. Pending keys `nist_least_squares_pmd2002` and `nist_linear_least_squares_pmd2002`.
- **Checked:** NIST/SEMATECH §4.4.5.3 https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd453.htm on response/predictor transformations and transformed-error interpretation. Pending key `nist_nonnormal_errors_pmd2002`.
- **Checked:** Dodge (2008) authorized extraction, printed pp. 304–305, least-squares method and Legendre history.
- **Checked by code:** All advertising and melanoma table entries and rounded coefficients, unit interpretation, Your turn values, and outlier counterexample in `checks/least-squares.py`.
- **Assumed:** Fixed predictor values for the minimization formulas and full column rank only where a unique coefficient formula is stated. Gaussian independent equal-variance errors only for likelihood equivalence.
- **Disputed:** Least squares by itself is not a causal method and does not assume normality merely to compute its minimizer. Transformed-response fits minimize errors on the transformed scale.
