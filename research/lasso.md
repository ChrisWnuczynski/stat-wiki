# Lasso research notes

Type: concept/method. Baseline: 1,938 words, no figures. The article already has a broad comparison with subset selection and ridge, the raw-sum-of-squares objective, a geometric explanation, soft thresholding, a five-coefficient example, penalty tuning, a path discussion and adaptive lasso. Preserve those sections, links, examples, bibliography entries and infobox; add a separate narrative through the key ideas, a fresh worked calculation, a collapsed proof and concrete failure cases.

## Sources opened

- Tibshirani (1996), “Regression Shrinkage and Selection Via the Lasso,” *JRSS B* 58(1):267–288, DOI 10.1111/j.2517-6161.1996.tb02080.x. Opened original publisher/DOI record and abstract for orientation. Full publisher text was inaccessible, so revised prose cites the full Friedman–Hastie–Tibshirani §1 account for the original attribution and method history.
- Friedman, Hastie and Tibshirani (2010), “Regularization Paths for Generalized Linear Models via Coordinate Descent,” *Journal of Statistical Software* 33(1), DOI 10.18637/jss.v033.i01. Opened full author-hosted original PDF https://web.stanford.edu/~hastie/Papers/glmnet.pdf; read §1–3, including lasso/ridge/elastic-net objective scaling, standardisation, coordinate updates, correlation degeneracy and GLM extensions. Existing key `friedman_glmnet2010`.
- Stanford STATS 202 “Model selection” course notes, https://web.stanford.edu/class/stats202/notes/Model-selection/Model-selection.html, opened full HTML around “Lasso regression” and “A very special case: LASSO.” Cross-checked raw-sum-of-squares objective and $\lambda/2$ threshold; the JSS paper is cited for added mathematics.
- Hastie, Tibshirani and Friedman (2009), publisher's *Elements of Statistical Learning* chapter 3 page https://link.springer.com/chapter/10.1007/978-0-387-84858-7_3, opened; preview was unavailable, so no new claim relies on that chapter. Existing citations to it remain from the source chapter.
- Dodge (2008), *The Concise Encyclopedia of Statistics*, “Ridge Regression,” printed p. 458 at `/workspace/statwiki-sources/dodge2008/pages/pdf-0456.txt`, read for historical orientation on shrinkage and collinearity. Index has no direct lasso entry, so new lasso history cites the original paper rather than Dodge.

## Fact ledger

- **Checked:** The raw-sum-of-squares lasso objective has orthonormal-design threshold $\lambda/2$; JSS §2, Stanford course notes and subgradient proof in the page.
- **Checked:** For $b=(1.8,-0.4,0.9)$ and $\lambda=1.2$, the threshold is 0.6, lasso gives $(1.2,0,0.3)$ and ridge gives approximately $(0.8182,-0.1818,0.4091)$. For the Your turn numbers, $b=(2,-0.7,0.2)$ and $\lambda=1$ gives $(1.5,-0.2,0)$. `checks/lasso.py` computes these.
- **Checked:** Identical columns in $(3-\beta_1-\beta_2)^2+2(|\beta_1|+|\beta_2|)$ yield optimum fitted sum two with nonunique coefficient allocations; direct optimisation check in `checks/lasso.py`.
- **Checked:** Existing $2^{30}>10^9$ and $2^{100}\approx10^{30}$ counts, and the five-coefficient ridge/lasso/hard-threshold comparison are recomputed in the focused check.
- **Assumed:** Hospital predictors and the orthonormal numerical example are hypothetical. No real clinical effect is inferred.
- **Disputed:** A stable coefficient list does not follow merely from accurate cross-validated prediction; collinearity and finite samples can change selection.

## Bank selection

Answered `ex-sl-18-5` computes soft thresholding with numbers different from the page. Answered `ex-sl-18-6` diagnoses feature-selection leakage before cross-validation. Answered `ex-sl-18-9` distinguishes predictive accuracy from exact support recovery. They test calculation, validation and interpretation, respectively.

## Shared-source issue

The generated article inherits malformed punctuation around inline citation HTML from `notes/sl-18-high-dimensional.qmd` near lines 267, 308 and 369. The underlying claims and citations should be preserved; pending `shared_changes` specifies a grammatical repair for the root integration and asks for the dependent note and article to be rebuilt and checked.
