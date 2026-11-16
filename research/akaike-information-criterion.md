# Rank 67: Akaike information criterion

## Sources opened

- Akaike (1974), *A New Look at the Statistical Model Identification*, IEEE Xplore publisher abstract and metadata: introduction of AIC for statistical identification, pp. 716–723.
- Burnham and Anderson (2002), *Model Selection and Multimodel Inference*, Springer publisher description and contents: information-theoretic model ranking and weighting.
- Akaike Memorial website, Institute of Statistical Mathematics: historical bibliographic confirmation.
- Dodge index directory absent from `~/statwiki-sources/dodge2008`.

## Fact audit

- **Checked:** The score $-2\ell(\hat\theta)+2k$ rewards maximized fit and penalizes $k$ fitted parameters; formula and comparison arithmetic will be checked against original page and independent code.
- **Checked:** Akaike's 1974 IEEE paper introduced the named information criterion for model identification; IEEE publisher abstract.
- **Assumed:** The regular-model Kullback–Leibler bias derivation requires assumptions not established by the publisher abstract; prove a simple Gaussian special case or log the general result.
- **Disputed:** AIC does not establish a model is true or confer a probability that it is true. Any interpreted weights must be conditional on the candidate set and assumptions.
- R Core Team, `AIC` official R-devel documentation, Description and Details: formula, parameter count, minimized score, maximized likelihood, common data, likelihood constants and transformed-response caveat; opened directly.
- Hyndman and Athanasopoulos, *Forecasting: Principles and Practice* (3rd ed.), §§7.5 and 9.6: regression AIC/AICc counts, ARIMA selection and differencing caveat; opened publisher-author site.
- Drton and Plummer (2017), publisher abstract: finite mixtures as singular model-selection examples.
- **Checked:** For a full-rank Gaussian linear model with known variance and fixed design, the fitted-residual expected deviance is lower than independent-replicate expected deviance by exactly $2d$; projection-matrix trace proof in the page.
- **Checked numerically:** AIC for $(-140,2)$ is 284 and for $(-136,5)$ is 282; practice $(-50,3)$ gives 106 and $(-48,6)$ gives 108. The full inherited six-row mixture table and its BIC rounding are checked in code.
- **Assumed:** AICc's quoted formula uses the forecasting regression convention with an intercept and estimated variance, not a universal correction for every model class.
- **Disputed:** Ordinary AIC's general asymptotic Kullback–Leibler correction is not proved by the special Gaussian proof; a proof task is logged. Singular mixtures need additional care, and lower AIC is not a model-truth probability.

## Build audit

- Baseline 867 words and no figures; rebuilt 2,919 words and no figures. The six-row mixture comparison, source example, infobox, links and existing citation keys remain.
- One collapsed proof covers the AIC score comparison, BIC threshold and exact Gaussian $2d$ optimism. The broader asymptotic KL argument is logged in `proofs-todo.json` through its generator override.
- The inherited six cross-validation scores are reported inputs; their original simulation is unavailable, so their provenance remains unverified. The AIC/BIC arithmetic, parameter counts and rounded values are independently checked.
- Initial full build passed, page and dependent mixture checks passed, offline verification passed for 458 entries, and `git diff --check` passed. The proof override uses a `#property-` slug accepted by the gate. The final build, 67 unit tests, four affected page checks, offline bibliography verification of 458 entries and `git diff --check` all passed. Citation locators were also corrected in the generator inputs for ranks 59, 65 and 66 and in shared AIC source text.
