# Binary responses in a GLM — research notes (rank 213)

## Sources read

- Checked: Nelder and Wedderburn (1972), *Generalized Linear Models*, full original article from McGill University course archive, https://jhanley.biostat.mcgill.ca/bios601/Likelihood/NelderWedderburn1972.pdf, opened 2026-11-16. §§1 and 3, pp. 370–380 unify exponential-family response, linear predictor, link and binomial/probit examples.
- Checked: Geyer (2022), *Stat 5421 Lecture Notes: Exponential Families*, full author-hosted course chapter, https://www.stat.umn.edu/geyer/f22/5421/notes/expfam.html, opened 2026-11-16. §7.1 gives binomial natural parameter as logit, mean and cumulant.
- Checked: sources/book/chapters/01-introduction-to-glms.qmd and generated topic, including cholesterol figure and existing links. Keep the Bernoulli expression and three links.
- Checked by code: Bernoulli mean and variance, sample likelihood and logistic predictions in numerical examples.
- Assumed: conditional independence of patients, correct link and linear predictor specification, and recorded binary outcome without substantial misclassification.
- Disputed: a GLM does not make the binary response itself normally distributed or its raw mean linear in predictors; a Bernoulli model does not automatically handle within-person dependence.
- Dodge: no direct binary GLM entry.

## Preservation

Baseline has 1,396 words and one figure. Keep figure, original likelihood, examples, and question links.
