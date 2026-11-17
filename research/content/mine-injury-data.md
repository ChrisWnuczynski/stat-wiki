## Motivating example
Forty-four mines have injury counts and measurements of inner burden thickness, extraction below the seam and mine age. A log-link count model expresses changes in the fitted mean as multiplicative factors. Its coefficients describe conditional associations in these observations; unequal exposure, selection into operating mines and omitted working conditions can all matter to the interpretation. A count alone is not an injury rate per worker-hour.{{cite:wuthrich_merz2022_glm}} (§§5.1.1, 5.2.4, regression and exposure offsets)

## Intuition — Change one coordinate while holding the others fixed
With mean $\mu(x)=\exp(\beta_0+\beta_1x_1+\beta_2x_2+\beta_3x_3)$, changing coordinate $j$ by $d$ gives the ratio
$$\frac{\mu(x+d e_j)}{\mu(x)}=e^{d\beta_j}.$$
The other coordinates cancel. This identity explains the units of a log-link coefficient: a percentage-point change in extraction and a year of age are different increments. Centering a covariate at a meaningful value changes the intercept's interpretation without changing fitted means.{{cite:wuthrich_merz2022_glm}} (§5.1, log-link regression){{cite:holmes_huber2019_msmb}} (§8.8.3, count-data GLMs)

## Worked example — Recomputing the fitted summaries
Using `mine` from the official `locfit` data package, the specified Poisson fit gives coefficients $(-3.7206821,-0.0014793,0.0627011,-0.0316514)$, with $44-4=40$ residual degrees of freedom. The quasi-Poisson fit gives the same coefficients because dividing the score by a common positive dispersion does not change its roots. Its estimated Pearson dispersion is $0.9049145$. Multiplying the Poisson standard errors by $\sqrt{0.9049145}\approx0.951269$ gives the quasi-Poisson standard errors. R uses normal reference tails for the fixed-dispersion Poisson summary and $t_{40}$ tails for the estimated-dispersion quasi summary.{{cite:wuthrich_merz2022_glm}} (§§5.3.1–5.3.2, residuals, dispersion and Wald statistics){{cite:firth1993_quasi}} (§1, eqs. (1)–(4))

For the age coefficient, these choices give $z=-1.94068$, two-sided normal $p=0.05230$, and $t=-2.04007$, two-sided $t_{40}$ $p=0.04798$. Crossing $0.05$ is a small numerical change in evidence, not a discontinuity in a scientific conclusion. The estimated dispersion being below one is a property of residual variation relative to the chosen conditional mean model; it does not identify a cause of underdispersion.

For an illustrative covariate profile $(x_1,x_2,x_3)=(100,70,5)$, the rounded equation gives $\eta=0.3598$ and $\widehat\mu=e^{0.3598}\approx1.433043$. Increasing extraction by ten percentage points changes the mean by $e^{0.627}\approx1.871986$, to about $2.68264$. Increasing age by ten years gives multiplier $e^{-0.317}\approx0.728331$, a decrease of about $27.17\%$ under the fitted equation. These calculations use the rounded coefficients for a transparent comparison, rather than the more precise coefficients of the refit.

**Your turn.** Using the rounded coefficient $0.0627$, what is the fitted mean multiplier for five additional percentage points of extraction? Does it describe a causal effect?

::: {.callout-tip collapse="true" title="Answer"}
The multiplier is $e^{5(0.0627)}=e^{0.3135}\approx1.368205$. It is a conditional fitted association; a causal interpretation would require additional design and confounding assumptions.
:::

## Properties — Score and dispersion are distinct tasks
For independent Poisson counts with log link, differentiating the log-likelihood gives $U(\beta)=\sum_i x_i(y_i-\mu_i)$. Its negative derivative is $X^\top\operatorname{diag}(\mu_i)X$, so the log-likelihood is concave. For an intercept model at a finite stationary point, the first score component implies $\sum_i\widehat\mu_i=\sum_i y_i$. This balance is algebraic and does not prove that the mean model is correct.{{cite:wuthrich_merz2022_glm}} (§§5.1.3, 5.2.4, canonical link and balance property)

The Pearson estimate $\widehat\phi=(n-p)^{-1}\sum_i(y_i-\widehat\mu_i)^2/\widehat\mu_i$ estimates residual dispersion after estimating the mean. Quasi-Poisson assumes variance proportional to that mean with one common multiplier. It cannot by itself account for an arbitrary variance pattern, dependence or omitted exposure. A model with worker-hours $e_i$ would commonly include $\log e_i$ as an offset when the target is a rate, which changes the interpretation of the response mean.{{cite:firth1993_quasi}} (§1){{cite:wuthrich_merz2022_glm}} (§§5.2.4, 5.3.1)

## Assumptions and limits
The measurements are observational. Survivor selection is a possible explanation for an age association, but the fitted coefficient and dispersion cannot determine whether such selection occurred. Variable selection also changes the meaning of ordinary coefficient p-values when its randomness is ignored. Scientific interpretation should therefore report the conditioning variables and exposure definition, examine residual patterns and uncertainty, and distinguish a fitted association from a policy intervention.{{cite:holmes_huber2019_msmb}} (§8.10, further statistical concepts){{cite:wuthrich_merz2022_glm}} (§5.3, model validation)
