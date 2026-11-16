## Motivating example
Suppose four repeated measurements are modelled as independent normal observations with an unknown common mean and variance. The data can estimate both quantities, but before seeing them a Bayesian calculation still needs a prior measure on each. A flat coefficient measure together with a log-scale measure for the variance is a convenient reference choice for this particular regression model. Its simplicity comes with a condition: because the measure has infinite mass, the data must make the resulting posterior integrable.

## Intuition — How data and prior combine
The likelihood asks which parameter values make the observed responses plausible. For a normal regression it rewards coefficients that keep residual squares small and variances that match their size. The reference factor $1/\sigma^2$ weights equal *multiplicative* intervals of the variance equally: moving from $1$ to $2$ receives the same prior mass as moving from $2$ to $4$. This is what “flat in log variance” means. It does not make the prior a probability distribution, nor does it make inference automatically objective.

The distinction between the coefficient vector and the variance is essential. The coefficient measure is flat in the chosen coordinate system; the variance measure is flat only after taking a logarithm. Changing coordinates changes density factors through a Jacobian. Thus the short formula for the prior has meaning only alongside its stated parameterization and likelihood.

## Definition
For fixed design matrix $X$ with $n$ rows and $p$ columns, the normal linear model is $Y\mid\beta,\sigma^2,X\sim N_n(X\beta,\sigma^2I_n)$. Its likelihood is proportional to $(\sigma^2)^{-n/2}\exp\{-\|y-X\beta\|^2/(2\sigma^2)\}$. The conventional joint reference measure used here has density $\pi(\beta,\sigma^2)\propto1/\sigma^2$ with respect to $d\beta\,d\sigma^2$. The factor cannot be normalized over $\mathbb R^p\times(0,\infty)$, so it is an improper prior. The posterior is meaningful only if the product of likelihood and prior has a finite, positive integral.

The label *reference prior* in this article names this conventional regression choice. It is not a universal prescription for every likelihood or every target parameter. In particular, a flat density in $\sigma$ would be a different measure from a flat density in $\log\sigma^2$.

## Properties
With $X$ of full column rank, write $\widehat\beta=(X^\top X)^{-1}X^\top y$, $s=\|y-X\widehat\beta\|^2$, and $\nu=n-p$. Completing the square separates coefficient uncertainty from residual uncertainty:
$$
\|y-X\beta\|^2=s+(\beta-\widehat\beta)^\top X^\top X(\beta-\widehat\beta).
$$
Consequently $\beta\mid\sigma^2,y\sim N_p(\widehat\beta,\sigma^2(X^\top X)^{-1})$ and $\sigma^2\mid y\sim\operatorname{InvGamma}(\nu/2,s/2)$, with the second argument in the inverse-Gamma density $b^a x^{-a-1}e^{-b/x}/\Gamma(a)$. These are probability distributions when $\nu>0$ and $s>0$. The marginal coefficient posterior is multivariate Student with $\nu$ degrees of freedom, centre $\widehat\beta$ and scale matrix $(s/\nu)(X^\top X)^{-1}$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The normal equations give $X^\top(y-X\widehat\beta)=0$. Expanding $\|y-X\beta\|^2$ around $\widehat\beta$ therefore eliminates the cross-term and gives the stated decomposition. Multiplying the likelihood by $1/\sigma^2$ yields $(\sigma^2)^{-n/2-1}\exp[-\{s+(\beta-\widehat\beta)^\top X^\top X(\beta-\widehat\beta)\}/(2\sigma^2)]$. The coefficient kernel is the displayed normal law. Integrating it over $\beta$ contributes $(\sigma^2)^{p/2}$ times a constant, leaving $(\sigma^2)^{-\nu/2-1}e^{-s/(2\sigma^2)}$, the inverse-Gamma kernel. Its integral is finite exactly when $\nu>0$ and $s>0$. Mixing the normal coefficient law over this inverse-Gamma law yields the Student law. If $X$ lacks rank, the likelihood is constant along a nonzero coefficient direction and the flat coefficient measure gives infinite posterior mass. If $s=0$, the remaining variance kernel diverges near zero. These establish the stated propriety conditions.
:::
:::

## Interpretation — when the likelihood dominates
The reference posterior reproduces a familiar least-squares centre, but it describes uncertainty in the unknown coefficients conditional on the observed data. The Student tails reflect the fact that the variance is estimated too. With known variance, the coefficient posterior conditional on it is normal. The marginal Student degrees of freedom are residual degrees of freedom, not the number of coefficients. A large $n$ can make the Student approximation close to normal, but neither a large sample nor a posterior formula repairs a rank-deficient design.

The prior itself cannot generate a predictive distribution before observing data because it is not a probability law. Once the posterior is proper, it can generate a posterior predictive distribution by integrating the sampling model over posterior uncertainty. That distinction matters whenever a prior predictive check or a Bayes factor is proposed: an arbitrary multiplicative constant in an improper prior does not cancel across different models in general.

## Statistical use
For a regression analysis, verify the design's rank and calculate its residual sum of squares before invoking the formula. Then summarize coefficients using the posterior Student distribution and predict a new response by retaining both parameter and new-observation uncertainty. Proper weakly informative priors offer another route when the reference measure's behaviour near extreme parameter values is undesirable, especially with small data sets or model comparisons.

## Worked example
Take an intercept-only model for observations $2,4,3,5$. Here $n=4$, $p=1$, $X^\top X=4$, and $\widehat\beta=3.5$. The residuals are $-1.5,0.5,-0.5,1.5$, giving $s=5$ and $\nu=3$. The variance posterior is $\operatorname{InvGamma}(3/2,5/2)$. The marginal posterior for the mean is Student with $3$ degrees of freedom, centre $3.5$, and scale $\sqrt{(5/3)/4}=\sqrt{5/12}\approx0.6455$. The Student scale is not its posterior standard deviation: for three degrees of freedom the variance is $(3/(3-2))(5/12)=1.25$. The data contain residual variation, so this posterior is proper. Four identical measurements would instead give $s=0$ and the reference posterior would fail to normalize.

**Your turn.** Under the same reference prior, suppose an intercept-only model has observations $1,2,3$. Find $\widehat\beta$, $s$, the residual degrees of freedom and the inverse-Gamma posterior parameters for $\sigma^2$. Is the posterior proper?

::: {.callout-tip collapse="true" title="Answer"}
The fitted mean is $2$ and the residuals are $-1,0,1$, so $s=2$. With $n=3$ and $p=1$, $\nu=2$ and $\sigma^2\mid y\sim\operatorname{InvGamma}(1,1)$. The posterior is proper because $X$ has rank one, $\nu>0$ and $s>0$. Its posterior mean for $\sigma^2$ does not exist, despite propriety, because an inverse-Gamma shape of one is too small for a finite mean.
:::

## Common misconceptions
“Flat” does not mean neutral to all transformations: a flat measure in variance differs from a flat measure in standard deviation. An improper prior is not a diffuse proper distribution; it has infinite mass and cannot be sampled as a prior law. Full rank alone is insufficient for a proper posterior here if the residual sum of squares is zero. Finally, equal numerical endpoints for a Bayesian credible interval and a classical confidence interval in this model do not make the two probability statements identical.

## Assumptions and limits
If two columns of $X$ are identical, the likelihood cannot identify their coefficients separately and the posterior integral diverges along their difference. If $n=p$ and $X$ is square and invertible, the fit is exact and no residual degrees of freedom remain for learning the variance. If all four measurements in the worked example equal $3$, then $s=0$ and the posterior concentrates toward zero variance without a finite normalizing constant. A heavy-tailed data-generating process can also make the normal likelihood a poor description even when the posterior is algebraically proper.

## Connections
The [likelihood function](likelihood-function.qmd) supplies the data-dependent factor. The [least-squares decomposition](least-squares-decomposition.qmd) makes the posterior derivation transparent. [Normal–inverse-Gamma conjugacy](normal-inverse-gamma-conjugacy.qmd) gives a proper-prior counterpart, while [posterior prediction under the reference prior](posterior-prediction-under-the-reference-prior.qmd) carries uncertainty into a new response. Jeffreys-style constructions are related but should not be treated as synonyms without checking their parameter and model conventions.

## History
Harold Jeffreys published *Theory of Probability* in 1939; Dodge's biographical account singles it out among his works.{{cite:dodge2008}} (p. 274, “Jeffreys, Harold”) Historical importance does not settle the analytic question for this regression model: its posterior still needs a finite normalizing constant.
