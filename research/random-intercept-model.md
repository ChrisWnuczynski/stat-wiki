# Random intercept model research notes

## Scope and baseline

- **Checked:** Rank 141 is a Concept/Section page. Baseline has 554 words and one figure. The source definition uses $Y_{ji}$, group effect $\alpha_j$, variances $\sigma_A^2$ and $\sigma^2$; the new prose follows that notation and retains the formula, covariance, figure, infobox and all six question links.
- **Checked:** The baseline explains nonnegative intraclass correlation and the $-1/(K-1)$ lower bound for general exchangeable correlation. The new collapsed proof derives both covariance eigenvalues and the general equicorrelation bound.

## Sources opened

- **Checked:** Laird and Ware (1982), original full paper from a University of South Carolina statistics course host, `https://people.stat.sc.edu/hansont/stat740/LairdWare1982.pdf`, with publisher DOI `https://doi.org/10.2307/2529876`. Summary and §§1–2 pp. 963–965 set out the two-stage longitudinal random-effects model and marginal covariance $R_i+Z_iDZ_i^{\mathsf T}$; §3.1 p. 966 gives conditional random-effect prediction and shrinkage. Existing `laird_ware1982` key.
- **Checked:** Bates et al. (2015), full author paper distributed in the official CRAN `lme4` vignette `https://cran.r-project.org/web/packages/lme4/vignettes/lmer.pdf`; journal record `https://www.jstatsoft.org/article/view/v067i01`. Introduction and §1.1 pp. 2–3 give fixed and random design matrices and normal conditional/marginal structure; §3 describes ML and REML. Existing `bates_lme4_2015` key.
- **Checked:** Dodge (2008), printed p. 322 (`pdf-0323.txt`), “Longitudinal Data,” describes repeated measurements and a mixed model with fixed and random terms. Used for orientation; its OCR has dimension errors, so the page cites Laird–Ware and Bates instead.

## Audit

- **Checked:** The collapsed proof derives within-group covariance, intraclass correlation, variance of a group mean, equal-size design effect, eigenvalues and normal conditional pooling. These are the stated results; the regression use of the design effect is explicitly limited to a simple mean.
- **Checked:** All new example and practice values are independently recomputed in `checks/random-intercept-model.py`, including $9/17$ pooling, $108/17$ group effect and $72/17$ conditional variance. The baseline's $3\times3$ negative-equicorrelation bound is also checked.
- **Checked:** `q-40` has a worked answer for a binary random-intercept treatment-time model, `q-41` has a worked answer about allowing random slopes, and `ex-orthodont-lmm` has a worked answer contrasting random intercepts and slopes in real repeated measurements. Their examples use different data and calculations from this page.
- **Assumed:** The constructed hospital numerical example treats fixed effects and variance parameters as known for transparent conditional prediction; fitted analyses must account for estimation uncertainty.
- **Disputed:** The source chapter’s equality wording for positive definiteness at the lower negative-equicorrelation boundary is incorrect; rank 129 pending already asks root to correct it to positive semidefinite at equality. The source’s suggestion that negative exchangeable correlation is not worth modelling is too broad: competition or finite-population constraints can make it relevant. The new page supplies a concrete counterexample without deleting the source paragraph.
