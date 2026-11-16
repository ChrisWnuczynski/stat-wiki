# Score function

Type: Concept/definition. Rank 175.

## Material checked

- **Checked:** Frozen baseline: 1,122 body words, no figures, logistic score and Hessian, a concavity theorem, regularity conditions and five question links. The researched source retains these passages and adds a single proof covering the identity and logistic calculus.
- **Checked:** Nelder and Wedderburn (1972), full original GLM article, §1.1 p. 371 gives score mean/information identities and the differentiation condition; §2.1 pp. 372–374 derives the GLM score equations and iterative weighted least squares.
- **Checked:** Albert and Anderson (1984), full *Biometrika* article pp. 1–10, university scholarly archive copy. §§1–4 classify overlap and separation and show why finite logistic maxima may be absent.
- **Checked:** Dodge (2008), printed p. 203, identifies Fisher's 1922 and 1925 estimation papers; it is used only for that historical pointer.
- **Checked by code:** Intercept-only logistic score, Hessian, Newton step, MLE, probabilities and all displayed decimals; vector score/Hessian identities checked with SymPy in `checks/score-function.py`.
- **Assumed:** Interchange of differentiation and integration, fixed support and the required moments for the information identity. The worked example treats outcomes as independent Bernoulli data with one shared probability.
- **Disputed:** The original one-line topic definition says every MLE solves a zero-score equation; that fails for boundary or nonattained maxima. A scoped shared-topic correction is recorded in pending changes. Original text is preserved until root integration, and the new Definition states the precise condition.

## Sources opened and used

1. Nelder and Wedderburn, “Generalized Linear Models,” *JRSS A* **135** (1972), §§1.1, 2.1, pp. 371–374, full paper via McGill faculty archive `https://jhanley.biostat.mcgill.ca/bios601/Likelihood/NelderWedderburn1972.pdf`; existing key `nelder_wedderburn1972`.
2. Albert and Anderson, “On the Existence of Maximum Likelihood Estimates in Logistic Regression Models,” *Biometrika* **71** (1984), §§1–4, pp. 1–7, full paper via university scholarly archive `https://citeseerx.ist.psu.edu/document?doi=358552a30531c785796a3ab041bc702e17f1d09a&repid=rep1&type=pdf`; existing key `albert_anderson1984`.
3. Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 203, Fisher entry; existing key `dodge2008`.

## Changes and checks

Two existing fully answered bank questions are requested as hidden self-checks. The single collapsed proof covers mean-zero score, information equality and logistic concavity. Full gate results recorded in commit run.
