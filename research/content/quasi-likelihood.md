## Motivating example
Count data can have a useful log-linear mean while their variance is not equal to that mean. Fitting a quasi-model specifies the mean and a variance relationship without demanding a complete probability distribution. This allows a mean fit and its uncertainty to use different amounts of distributional detail. It also places limits on likelihood-based model comparison and simulation.{{cite:firth1993_quasi}} (§1, pp. 341–342)

## Intuition — Start with an unbiased estimating equation
For independent observations, assume $E(Y_i)=\mu_i(\beta)$ and $\operatorname{Var}(Y_i)=\phi V(\mu_i)$ with $\phi>0$ and $V(\mu_i)>0$ at the fitted means. Let $D$ have rows $\partial\mu_i/\partial\beta^\top$. The quasi-score is
$$U(\beta)=D^\top\operatorname{diag}\{\phi V(\mu_i)\}^{-1}(Y-\mu).$$
The residual vector has mean zero, proving $E(U)=0$. At the true mean and variance, its covariance is $D^\top\operatorname{diag}\{\phi V(\mu_i)\}^{-1}D$, also the negative expected derivative. Derivatives of the weights multiply a mean-zero residual and disappear after expectation. These identities explain the similarity to a likelihood score without specifying every outcome probability.{{cite:firth1993_quasi}} (§1, eqs. (1)–(4))

## Properties — What the variance function does and does not specify
For a scalar observation, integrating the quasi-score from a fixed admissible reference mean gives a quasi-likelihood whose derivative is $(y-\mu)/\{\phi V(\mu)\}$. The often-used reference $y$ requires the integral to be finite; endpoints with zero variance can make that normalization inappropriate. With $V(\mu)=\mu$ and positive $y,\mu$, the integral normalized at $\mu=y$ is
$$Q(\mu;y)=\{y\log(\mu/y)-\mu+y\}/\phi.$$
Differentiation recovers the quasi-score. At $y=0$, the continuous convention $0\log0=0$ gives $Q=-\mu/\phi$.{{cite:firth1993_quasi}} (§1, independent Poisson variance function){{cite:wuthrich_merz2022_glm}} (§5.2.1, Poisson deviance)

A common $\phi$ cancels from the estimating equation, so it does not change its roots. The model-based covariance for $\widehat\beta$ is approximately $\phi\{D^\top\operatorname{diag}(V)^{-1}D\}^{-1}$. The Pearson estimate divides a weighted residual sum of squares by $n-p$; it is a degrees-of-freedom adjustment, rather than an exact unbiased estimator in every nonlinear model. If the mean is right and the working variance is wrong, a sandwich covariance may be needed.{{cite:firth1993_quasi}} (§2, pp. 343–344){{cite:wuthrich_merz2022_glm}} (§5.3.1, eq. (5.30))

Moments must still be compatible with the response support. For a binary outcome, $Y^2=Y$ forces $\operatorname{Var}(Y)=\mu(1-\mu)$; a free dispersion describes an estimating framework or aggregated/dependent data rather than another single Bernoulli law. Likewise, $0\le Y\le1$ implies $\operatorname{Var}(Y)\le\mu(1-\mu)$. A mathematically positive variance curve is not a promise that every mean–dispersion pair yields a distribution on the desired support.{{cite:firth1993_quasi}} (§§1, 5, mean–variance models and overdispersed data)

A useful counterexample to reasoning from names alone is $Y\sim N(\mu,\phi\mu)$ with fixed $\phi>0$ and $\mu>0$. Expanding its log density gives
$$\log f(y;\mu)=-\tfrac12\log(2\pi\phi)-\tfrac12\log\mu-\frac{y^2}{2\phi\mu}+\frac y\phi-\frac\mu{2\phi}.$$
This has exponential-family statistic $y^2$ and natural parameter $-1/(2\phi\mu)$. Differentiation gives the likelihood score $(y^2-\phi\mu-\mu^2)/(2\phi\mu^2)$, which differs from the quasi-score $(y-\mu)/(\phi\mu)$. At $y=3,\mu=2,\phi=1.5$, they are $1/6$ and $1/3$. The same mean–variance relationship need not imply the same likelihood score unless the relevant linear-exponential-family structure is specified.{{cite:firth1993_quasi}} (§1, equivalence for linear exponential families)

## Worked example — An intercept-only quasi-Poisson fit
For $y=(1,3,2,6)$ and a common mean, the score is proportional to $\sum_i(y_i-\mu)/\mu$, so $\widehat\mu=3$. The squared residuals sum to fourteen. With one fitted parameter, the Pearson dispersion is $(14/3)/(4-1)=14/9$. The variance estimate for the fitted mean is $\widehat\phi\widehat\mu/4=7/6$, giving standard error $\sqrt{7/6}\approx1.080123$. It equals $s/\sqrt4$ here because the intercept-only quasi-Poisson calculation reduces to the sample variance divided by sample size. The fixed-dispersion Poisson calculation would give $\sqrt{3/4}\approx0.866025$.{{cite:firth1993_quasi}} (§2, intercept-only example)

**Your turn.** At mean $\mu=2$, response $y=3$ and dispersion $\phi=1.5$, compute the scalar quasi-score for $V(\mu)=\mu$.

::: {.callout-tip collapse="true" title="Answer"}
The score is $(3-2)/(1.5\times2)=1/3$. Its variance under the specified moments is $1/(1.5\times2)=1/3$.
:::

## Assumptions and limits
The leaf-blotch examples compare variance assumptions for plot-level proportions. Treating variety and site as factors uses nine variety contrasts and eight site contrasts plus an intercept, for eighteen coefficients in ninety observations. A saturated interaction would use ninety cell means and leave no residual degrees of freedom for estimating dispersion without further structure. A fractional response also changes how a quasi-binomial dispersion should be interpreted: the numeric scale of a proportion differs from a count or a proportion with an explicit binomial denominator. Small dispersion alone does not identify pseudo-replication or any other cause.{{cite:wuthrich_merz2022_glm}} (§§5.1, 5.3.1){{cite:firth1993_quasi}} (§5, overdispersed data)

A quasi-likelihood is not generally a normalized sampling density. Ordinary likelihood AIC values therefore cannot be obtained by plugging an arbitrary quasi-integral into the usual formula; extended quasi-likelihood or a justified quasi-information criterion introduces further assumptions. Model comparison should state its criterion and response scale. The mean–variance equations also do not establish that no exponential family of any form could have a proposed variance function: support and admissible mean domain matter.{{cite:firth1993_quasi}} (§8, Extended quasi-likelihood){{cite:wuthrich_merz2022_glm}} (§5.3, model validation)
