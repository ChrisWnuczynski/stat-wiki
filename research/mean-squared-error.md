# Mean squared error — rank 106

Type: concept. Frozen baseline 802 body words, zero figures. Source definition, bias-variance identity, two variance-estimator and uniform-maximum worked examples, shrunken-mean answer, infobox and supported citations remain generated.

## Sources read

- **Checked:** Gelman et al., *Bayesian Data Analysis*, third ed., author-hosted authorized PDF https://sites.stat.columbia.edu/gelman/book/BDA3.pdf, Ch. 2 §§2.1 and 2.4 printed pp. 31–32, 35 (Beta-binomial and posterior mean), Ch. 4 §4.4 pp. 91–92 (frequentist estimator MSE), Ch. 7 §7.1 pp. 166–167 (prediction MSE), Ch. 9 §9.1 pp. 205–206 (squared loss).
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics* (2008), printed pp. 304–305 “Least-Squares Method”, p. 337 “Mean Squared Error”, p. 141 “Criterion of Total Mean Squared Error”.
- **Checked by code:** `checks/mean-squared-error.py` evaluates all new binomial moments/MSEs, practice numbers and the inherited normal-variance and uniform-maximum figures.
- **Assumed:** Four independent Bernoulli trials in the worked example; MSE treats $p$ as fixed and averages over binomial samples. Prediction formula assumes finite conditional variance.
- **Disputed:** In-sample residual MSE and out-of-sample prediction MSE are not interchangeable. The source's Cramér, Casella–Berger and Lehmann–Casella citations remain, but were not newly relied upon.

## Proof and bank

One collapsed proof establishes bias-variance and prediction decompositions and exact binomial estimator MSEs. Answered questions `ex-inf-poisson-mle` and `ex-applied-mmse` exercise frequentist and conditional posterior meanings without duplicating the source's shrunken-mean question.
