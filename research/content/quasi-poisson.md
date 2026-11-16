## Motivating example
Two groups of machines may have failure counts whose averages follow a clear log-linear pattern but whose scatter exceeds the Poisson prediction. A quasi-Poisson model keeps the regression mean and allows variance to be a constant multiple of it. This can preserve useful coefficient estimates while widening uncertainty to reflect extra variation.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Intuition
A Poisson regression has conditional variance equal to its conditional mean. Quasi-Poisson replaces that equality by $\operatorname{Var}(Y_i\mid x_i)=\phi\mu_i$. The factor $\phi$ changes the spread, not the expected count. When $\phi>1$, overdispersion makes the same fitted effect less precise than a Poisson standard error would suggest; when $0<\phi<1$, the assumed spread is smaller. The formula describes two moments, so it does not by itself assign probabilities to individual count values.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Definition
For count observations with $\mu_i=\exp(x_i^\top\beta)>0$, the quasi-Poisson specification is $E(Y_i\mid x_i)=\mu_i$ and $\operatorname{Var}(Y_i\mid x_i)=\phi\mu_i$, with one common $\phi>0$. A log exposure offset can be included when observation times or populations differ. The variance function is $V(\mu)=\mu$; specifying it and the mean supports a quasi-score, not a unique count probability mass function. At $\phi=1$ the first two moments match Poisson regression, while the quasi specification alone still does not assert the full Poisson law.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Interpretation
With the same data, design, link and unpenalised fitting rule, a common $\phi$ divides the Poisson score by a positive scalar. Thus the fitted coefficient vector is the same whenever the score has a well-defined solution. Its usual model-based covariance is multiplied by $\phi$ and each standard error by $\sqrt\phi$. A ratio of expected counts remains $e^{\beta_j}$ for a one-unit change in $x_j$ at fixed other covariates and exposure; overdispersion changes confidence in that ratio, not its point value.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Properties
The Pearson dispersion estimate is commonly based on $\sum_i(Y_i-\widehat\mu_i)^2/\widehat\mu_i$ divided by residual degrees of freedom $n-p$, where $p$ is the number of fitted coefficients. It measures excess or reduced residual variation against the fitted mean and variance shape. Its reliability depends on the mean model, independence and enough residual information. Because quasi-Poisson has no fully specified likelihood, ordinary Poisson likelihood-ratio tests and AIC cannot simply be reused after multiplying standard errors.{{cite:wuthrich_merz2022_glm}} (§5.3.1, Pearson dispersion; §5.4)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $\mu_i=e^{x_i^\top\beta}$, differentiation gives $\partial\mu_i/\partial\beta=\mu_ix_i$. In the quasi-score, $U(\beta)=\sum_i (Y_i-\mu_i)(\phi\mu_i)^{-1}\partial\mu_i/\partial\beta=\phi^{-1}\sum_i x_i(Y_i-\mu_i)$.
The final sum is the Poisson log-link score, so a positive common multiplier cannot alter its zeros. Under the independent working covariance $\operatorname{diag}(\phi\mu_i)$, the model-based inverse information is $\phi(X^\top W X)^{-1}$ with $W=\operatorname{diag}(\mu_i)$, giving the square-root standard-error factor. This covariance statement requires the working moments and adequate rank.{{cite:wuthrich_merz2022_glm}} (§5.4)
:::
:::

## Statistical use
Begin with the count, its exposure and the covariates that determine its mean. Fit the log-mean equation, examine residual variation against fitted means, and estimate $\phi$ only after checking for missing covariates, clustering or a wrong mean shape. Report coefficient estimates alongside dispersion-adjusted uncertainty. If the research question requires probabilities of zero counts, simulated new counts or a genuine likelihood comparison, choose and check a full count distribution, such as an appropriate negative-binomial model.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Worked example
Suppose equal-exposure groups have observed counts $(0,0,6)$ and $(0,0,12)$. Their fitted group means in a two-level log-mean model are $2$ and $4$, so the coefficient for the second group is $\log(4/2)=\log2\approx0.69315$ and its expected-count ratio is $2$. The Pearson residual sum is $12$ for the first group and $24$ for the second: for example, the first contributes $2+2+8=12$. With six observations and two fitted coefficients, $\widehat\phi=(12+24)/(6-2)=9$. If the Poisson standard error for the group coefficient is $0.20$, the quasi-Poisson version is $\sqrt9(0.20)=0.60$. The point ratio stays $2$; its uncertainty grows. Four zero counts also invite a check of the mean and count mechanism, and six observations make the dispersion estimate fragile.{{cite:wuthrich_merz2022_glm}} (§5.3.1, Pearson dispersion; §5.4)

**Your turn.** In another fit, $\widehat\phi=4$ and a coefficient's Poisson standard error is $0.15$. Find the quasi-Poisson standard error and say whether the common dispersion changes the fitted coefficient.

::: {.callout-tip collapse="true" title="Answer"}
The standard error is $\sqrt4(0.15)=0.30$. With the same mean model and one common $\phi$, the quasi-score is only a constant multiple of the Poisson score, so the coefficient estimate remains the same. A different variance shape or observation-specific dispersion would not give this cancellation.{{cite:wuthrich_merz2022_glm}} (§5.4)
:::

## Common misconceptions
Quasi-Poisson is not a probability distribution from which one can simulate merely by choosing $\mu$ and $\phi$. Dispersion greater than one does not change the fitted mean if the quasi-score is just the rescaled Poisson score. Standard errors scale by $\sqrt\phi$, not $\phi$. And extra variation does not prove a particular cause: omitted predictors, dependence and latent heterogeneity can all produce it.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Assumptions and limits — When quasi-Poisson is inadequate
If one equipment cluster fails together, counts on its machines are dependent; multiplying independent-case variances by one common $\phi$ does not model the covariance. If the mean has a sharp age threshold but the regression forces a straight log-mean line, correcting dispersion leaves systematic bias. If variance grows roughly as $\mu^2$ rather than $\mu$, a constant multiplier of $\mu$ fits the wrong variance shape. And a question about the chance of zero failures needs a full distribution, which this moment model does not supply.{{cite:wuthrich_merz2022_glm}} (§5.4)

## Connections
The [quasi-score](quasi-score-and-quasi-likelihood.qmd) explains why the coefficients can agree with Poisson regression. The answered [overdispersion question](../questions/q-47.qmd) asks how a variance factor changes inference without a full likelihood; the [fish-count question](../questions/ex-fish-poisson.qmd) shows why a badly dispersed Poisson fit should prompt further modelling. They connect the moment specification to two different diagnostic tasks.{{cite:wuthrich_merz2022_glm}} (§5.4)

## History
Wedderburn introduced quasi-likelihood in 1974 to make regression estimation possible from a mean–variance relation instead of a complete observation law. Quasi-Poisson applies that idea to counts whose variance is proportional to their mean, giving a practical response to overdispersion in a Poisson-style regression.{{cite:wuthrich_merz2022_glm}} (§5.4, opening discussion)
