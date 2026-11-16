# Linear mixed model research notes

Type: concept/model. Baseline: 299 words and no figures. Preserve the original normal versus nonnormal covariance distinction, random-intercept correlation range, main-article link, infobox and all three inherited citations.

## Sources opened

- Bates, Mächler, Bolker and Walker (2015), “Fitting Linear Mixed-Effects Models Using lme4,” *Journal of Statistical Software* 67(1), DOI 10.18637/jss.v067.i01. Read the full 51-page author-hosted/JSS-published PDF at https://lme4.github.io/lme4/articles/lmer.pdf: §1.1–1.3, §2.2, §3.4, and the discussion of singular fits in §4. Checked the conditional normal model, random-effect covariance, nested/crossed and random-slope designs, ML/REML distinction and boundary fits. Existing bibliography key `bates_lme4_2015`.
- Laird and Ware (1982), “Random-Effects Models for Longitudinal Data,” *Biometrics* 38(4), pp. 963–974, DOI 10.2307/2529876. Opened PubMed's original-paper bibliographic page and abstract, https://pubmed.ncbi.nlm.nih.gov/7168798/, for orientation. The new historical paragraph cites the full Bates et al. account of the paper's longitudinal role.
- Henderson (1975), “Best Linear Unbiased Estimation and Prediction under a Selection Model,” *Biometrics* 31(2), pp. 423–447, DOI 10.2307/2529430. Opened the PubMed bibliographic search record, https://pubmed.ncbi.nlm.nih.gov/1174616/, for orientation; the original full text was unavailable. The new historical paragraph cites Bates et al. §3.5 for Henderson's equations.
- Dodge (2008), *The Concise Encyclopedia of Statistics*, consulted index at `/workspace/statwiki-sources/dodge2008/index.tsv`. No direct mixed-model, random-effect or variance-component entry was present; used only for orientation and did not cite it for this page.
- The historical prose now uses the full Bates et al. §1.1 account for Laird–Ware's repeated-measurement role and §3.5 for Henderson's mixed-model equations; it does not infer technical claims from the unavailable original full papers.

## Fact ledger

- **Checked:** $Y=X\beta+Zb+\varepsilon$ with independent zero-mean normal $b,\varepsilon$ has marginal covariance $ZGZ^\top+R$. Bates et al. §1.1; algebra in the collapsed proof.
- **Checked:** A random intercept has within-group correlation $\tau^2/(\tau^2+\sigma^2)$ and cannot give negative within-group correlation. Bates et al. §1.1–2.2.
- **Checked:** For $\tau^2=9,\sigma^2=4$, variance 13, covariance 9, correlation $9/13=0.6923077$, difference variance 8. The independent-error comparison yields 26. Focused check verifies every number.
- **Checked:** For $\tau^2=4,\sigma^2=6$, variance 10, correlation 0.4 and difference variance 12.
- **Assumed:** Clinic measurements and coefficients in the worked example are hypothetical. A Gaussian random-intercept model is posited, not inferred from observed data.
- **Disputed:** The broad historical origins of mixed models predate the three cited papers. History describes their documented contributions without claiming a first invention.

## Bank selection

`c-34` has an answered definition question on fixed and random effects. `ex-orthodont-lmm` has a detailed answered numeric longitudinal random-intercept/slope problem, distinct from the page's simple random-intercept exercise. Both directly test the model.
