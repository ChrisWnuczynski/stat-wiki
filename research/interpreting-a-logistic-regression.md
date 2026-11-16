# Interpreting a logistic regression: research notes

## Sources opened

- **Checked:** Agresti, Tarantola & Varriale (2023), “Simple Ways to Interpret Effects in Modeling Binary Data,” full Springer chapter through an institutional repository, §5.1, printed pp. 155–157. Gives the adjusted $e^\beta$ odds ratio, one-unit conditional interpretation, difference from a risk ratio, and the value of probability-scale summaries.
- **Checked:** Cox (1958), “The Regression Analysis of Binary Sequences,” publisher DOI abstract and an excerpt of the original logistic-law equations reproduced in an Imperial College lecture PDF. The paper concerns a sequence of binary responses and covariates; use it only for the historical development and model form, not for modern effect-interpretation nuances that were not read in full.
- **Checked:** Nelder & Wedderburn (1972), original *JRSS A* article via a McGill-hosted journal scan, §3.3, printed p. 379. Presents binomial regression, the logit transformation, and its inverse mean function within the GLM framework.
- **Checked:** inherited `sources/book/chapters/01-introduction-to-glms.qmd`, “Interpreting a logistic regression” and adjacent cholesterol fit. Preserve its conditional-coefficient and intercept explanations; avoid transplanting its unrelated fitted-data numbers into the new example.
- **Checked with caution:** Dodge, *The Concise Encyclopedia of Statistics*, “Logistic Regression,” printed pp. 319–320 (PDF pp. 320–321). It gives the binary-response model and $e^{\beta}$ odds-ratio reading for binary predictors. It also calls a continuous slope “relative risk” and has inconsistent numbers/notation in its heart-disease example. Use it for historical orientation and the sound odds-ratio statement only.

## Mathematical checks

- **Checked:** In a hypothetical no-interaction model with baseline odds $1/3$ and group odds multiplier $2$, probabilities are $p_0=1/4$ and $p_1=2/5=0.4$. The risk ratio is $8/5=1.6$ and risk difference $3/20=0.15$, while the odds ratio is $2$.
- **Checked:** With baseline probability $1/5$ and odds multiplier $3$, the other group's odds are $3/4$ and probability $3/7\approx0.4285714$; risk difference $8/35\approx0.2285714$ and risk ratio $15/7\approx2.1428571$.
- **Checked:** If $\operatorname{logit}p=\alpha+\beta z+\gamma x$, subtracting the two predictors at the same $x$ yields log odds ratio $\beta$ and OR $e^\beta$. Solving odds multiplication gives $p_1=rp_0/(1-p_0+rp_0)$.

## Scope decisions

- **Assumed:** The group comparison is hypothetical, not an estimated treatment effect or causal claim.
- **Disputed:** A logistic slope is a constant change in event probability or a risk ratio. Its fixed interpretation is on the conditional log-odds scale; probability changes vary with baseline risk.
- **Disputed:** An intercept evaluated at an impossible covariate value should be reported as a real-world baseline prediction.
