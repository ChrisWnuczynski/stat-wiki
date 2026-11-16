# Fixed and random effects — rank 129

Type: Concept/section. Baseline: 657 body words, zero figures, eight question links. Read the generated article and the full inherited random-intercepts chapter section. Preserved all three hospital, fertilizer–species–block and jokes examples, source citations, infobox values, exercises and eight links by adding page-local content only.

## Material checked

- **Checked:** Andrew Gelman's author-hosted [2005 discussion paper](https://sites.stat.columbia.edu/gelman/research/published/AOS259.pdf), DOI 10.1214/009053604000001048, §6 pp. 20–22 and introductory pp. 1–2. It documents multiple incompatible definitions of fixed/random effects, the existing-versus-new-levels estimand, shrinkage, and historical Eisenhart reference.
- **Checked:** Bates, Mächler, Bolker and Walker's author-hosted [lme4 article](https://lme4.github.io/lme4/articles/lmer.pdf), *Journal of Statistical Software* 67(1), §1.1 pp. 2–3 and §3. Its Gaussian mixed-model conditional law, normal random effects, fixed/random terms, likelihood and REML structure support the model description.
- **Checked by code:** the example's fixed contrast, pooling weight, conditional predictions, intraclass correlation, new-group marginal variance, hidden practice, and equicorrelation eigenvalue boundary are asserted in `checks/fixed-and-random-effects.py`.
- **Assumed:** the small hospital numbers and known variance parameters are illustrative, not an empirical fit. The normal shrinkage calculation treats the common mean and two variances as known; actual fitted uncertainty is larger.
- **Disputed:** there is no universally binding definition of “fixed effect” across disciplines. The page defines the particular fixed-indicator versus random-intercept model it uses, while noting Gelman's broader terminology. The inherited chapter says a negative 3×3 equicorrelation matrix is positive definite for $\rho\le1/2$; the equality case is only semidefinite. It also loosely says covariance parameters depend on $\beta$. Both source corrections are in the pending shared-change manifest for integration.

## Dodge and question bank

The authorized Dodge index has no direct entry for fixed/random effects or variance components, so it supplies no claim here. Answered bank items `q-39` and `c-35` genuinely exercise fixed versus patient-specific random terms and random intercept/slope roles. Their calculations differ from the article's hospital pooling example. The IDs are in the pending manifest for the shared self-check map.

## Result

One collapsed proof derives the intraclass correlation and the normal conditional shrinkage weight. No new result needs a proof override. The article retains zero figures; the source chapter's random-intercept diagram is unaffected by page-local additions.
