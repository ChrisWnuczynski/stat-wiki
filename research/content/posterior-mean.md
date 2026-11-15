## Lead context
The posterior distribution describes plausible parameter values after observing data; its mean compresses that distribution into one number. In conjugate models, the mean can show explicitly how prior information combines with the sample. As a decision rule, the posterior mean is appropriate when errors are measured by squared loss and the needed moments exist.{{cite:hoff2013_bayes_estimators}} (pp. 9, 11–13)

## Motivating example
Suppose a researcher initially regards a coin as roughly balanced and then observes seven heads in ten tosses. The observed fraction is $0.7$, while a Beta prior with mean $1/2$ gives a posterior mean between $1/2$ and $0.7$. The estimate uses both the prior distribution and the likelihood.{{cite:hoff2013_bayes_estimators}} (p. 11)

## Intuition
Imagine all possible values of an unknown parameter, each weighted by its posterior probability. The posterior mean is their weighted average. A long tail can pull it away from the most probable values, so it need not equal the posterior mode or median. The difference matters when a skewed posterior is summarised by one number.{{cite:wang2025_foundations}} (Ch. 20, Sec. 24.1)

## Definition
Let $\Theta$ denote a scalar random parameter, $\theta$ a possible value, and $Y=y$ the observed data. If the posterior has density $p(\theta\mid y)$ and $\int|\theta|p(\theta\mid y)\,d\theta$ is finite, its posterior mean is

$$
m(y)=\mathbb E(\Theta\mid Y=y)=\int\theta p(\theta\mid y)\,d\theta.
$$

The integral is over the parameter's support; a discrete posterior uses a weighted sum instead. The mean exists when the posterior expectation of $|\Theta|$ is finite. A posterior variance additionally requires a finite second moment.{{cite:hoff2013_bayes_estimators}} (p. 9)

Under squared-error loss $L(\theta,d)=(d-\theta)^2$ for a reported value $d$, the posterior mean uniquely minimizes posterior risk when the posterior second moment is finite. It is a Bayes estimator when the overall Bayes risk is finite. Under absolute-error loss, a posterior median is optimal instead; the maximum-a-posteriori estimate maximizes density.{{cite:hoff2013_bayes_estimators}} (pp. 8–10)

## Properties
With a $\operatorname{Beta}(a,b)$ prior on a Bernoulli success probability $\Theta$, $a,b>0$, and $x$ successes in $n$ independent trials, the posterior is $\operatorname{Beta}(a+x,b+n-x)$ and has mean

$$
\mathbb E(\Theta\mid x)=\frac{a+x}{a+b+n}
=\frac{a+b}{a+b+n}\frac{a}{a+b}
+\frac{n}{a+b+n}\frac{x}{n},\qquad n>0.
$$

Here $a/(a+b)$ is the prior mean and $x/n$ is the observed success fraction. Both weights are nonnegative and add to one. In this model, $a+b$ sets the weight of the prior mean relative to the $n$ observations.{{cite:hoff2013_bayes_estimators}} (p. 11)

For a normal prior $\Theta\sim\operatorname{N}(m_0,\tau^2)$ and independent observations $Y_i\mid\Theta=\theta\sim\operatorname{N}(\theta,\sigma^2)$ with known positive variances, the posterior mean is

$$
m(y)=\frac{m_0/\tau^2+n\overline y/\sigma^2}{1/\tau^2+n/\sigma^2},
\qquad
\operatorname{Var}(\Theta\mid y)=\frac{1}{1/\tau^2+n/\sigma^2}.
$$

Here $m_0$ is the prior mean, $\tau^2$ its variance, $\sigma^2$ the observation variance, and $\overline y$ the observed sample mean. The posterior mean weights $m_0$ and $\overline y$ by their respective precisions.{{cite:hoff2013_bayes_estimators}} (pp. 12–13)

The average of posterior draws approximates $m(y)$. For independent exact draws with a finite mean, the law of large numbers gives convergence as the number of draws grows. A stationary, ergodic Markov chain can also estimate the mean, but its dependent draws affect the Monte Carlo standard error. The spread of the parameter draws describes posterior uncertainty, while the Monte Carlo standard error describes uncertainty in the numerical average.{{cite:geyer1992}} (pp. 473–476)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $m=\mathbb E(\Theta\mid y)$ and assume a finite posterior second moment. Expanding $d-\Theta=(d-m)+(m-\Theta)$ gives

$$
\mathbb E[(d-\Theta)^2\mid y]
=\mathbb E[(m-\Theta)^2\mid y]+(d-m)^2,
$$

because the cross term contains $\mathbb E(m-\Theta\mid y)=0$. The first term does not depend on $d$, and the second is uniquely smallest at $d=m$. Integrating this pointwise result over the distribution of $Y$ proves the Bayes-risk statement when the overall risk exists. For absolute error, moving $d$ toward a posterior median decreases expected absolute deviation until at least half the posterior mass lies on each side.{{cite:hoff2013_bayes_estimators}} (pp. 8–10)

Multiplying the Beta prior kernel $\theta^{a-1}(1-\theta)^{b-1}$ by the binomial likelihood kernel $\theta^x(1-\theta)^{n-x}$ gives the Beta parameters $a+x,b+n-x$. The Beta mean formula yields $(a+x)/(a+b+n)$. Expanding the two weighted terms on the right gives $a/(a+b+n)+x/(a+b+n)$, proving the identity and the sum-to-one weights. For the normal model, collect the quadratic terms of $\theta$ in prior times likelihood: the coefficient of $\theta^2$ is $1/\tau^2+n/\sigma^2$, and the coefficient of $-2\theta$ is $m_0/\tau^2+n\overline y/\sigma^2$. Completing the square gives the displayed normal posterior mean and variance.{{cite:hoff2013_bayes_estimators}} (pp. 11–13)

For independent draws $\Theta^{(1)},\ldots,\Theta^{(L)}$ from the posterior with finite absolute mean, the strong law of large numbers makes $L^{-1}\sum_l\Theta^{(l)}$ converge to $m(y)$ almost surely. For a Markov chain, the corresponding conclusion uses an ergodic theorem for a chain with the posterior as stationary distribution and an integrable target function.{{cite:geyer1992}} (pp. 473–476)
:::
:::

## Statistical use
Report the posterior mean when squared-error consequences make it an appropriate point summary, alongside a credible interval that shows the spread of the posterior. A single mean cannot show skewness or multiple modes. The figure compares an equal-tailed interval with a shorter highest-density interval for a skewed posterior.{{cite:hoff2013_bayes_estimators}} (p. 9) {{cite:wang2025_foundations}} (Ch. 20, Thm. 35)

When posterior expectations lack a closed form, simulated draws can approximate them. Check that the simulation explores the distribution and distinguish the spread of the parameter draws from the error of their numerical average. More draws can reduce Monte Carlo error, while the posterior distribution continues to represent uncertainty from the same observed data.{{cite:geyer1992}} (pp. 473–476)

## Worked example
Use a $\operatorname{Beta}(2,2)$ prior for a coin and observe seven heads in ten trials. The posterior is $\operatorname{Beta}(9,5)$ and its mean is $9/14\approx0.643$. Equivalently, the prior mean $1/2$ gets weight $4/14$ and the observed fraction $7/10$ gets weight $10/14$: $(4/14)(1/2)+(10/14)(7/10)=9/14$. The interior posterior mode is $(9-1)/(9+5-2)=2/3$, which is larger than the mean of this skewed posterior.{{cite:hoff2013_bayes_estimators}} (p. 11) {{cite:wang2025_foundations}} (Ch. 20, Example 11)

The posterior variance is $(9\cdot5)/(14^2\cdot15)=3/196\approx0.0153$, giving a posterior standard deviation of $\sqrt{3}/14\approx0.124$. The mean $0.643$ is therefore a location summary, while the standard deviation describes how dispersed plausible probabilities remain after ten tosses. For comparison, the observed fraction alone is $0.700$; the posterior mean lies about $0.057$ below it because the prior assigns more weight near $1/2$.{{cite:wang2025_foundations}} (Ch. 20, Example 11)

As a normal example, take prior mean $m_0=0$, prior variance $\tau^2=4$, four observations with $\overline y=3$, and known observation variance $\sigma^2=4$. Prior precision is $1/4$ and data precision is $4/4=1$, so the posterior mean is $(0/4+4\cdot3/4)/(1/4+1)=2.4$, with posterior variance $1/(1/4+1)=0.8$.{{cite:hoff2013_bayes_estimators}} (pp. 12–13)

The combined precision is $1/4+1=5/4$. Dividing each contribution by $5/4$ gives weights $1/5$ for the prior mean and $4/5$ for the sample mean: $(1/5)(0)+(4/5)(3)=2.4$. The posterior standard deviation is $\sqrt{0.8}\approx0.894$, smaller than the prior standard deviation $2$. This describes uncertainty about the unknown mean; individual observations have sampling standard deviation $2$ in this model.{{cite:hoff2013_bayes_estimators}} (pp. 12–13)

**Your turn.** With a $\operatorname{Beta}(1,1)$ prior and three heads in ten trials, find the posterior mean and compare it with the observed fraction and the posterior mode.{{cite:hoff2013_bayes_estimators}} (p. 11)

::: {.callout-tip collapse="true" title="Answer"}
The posterior is $\operatorname{Beta}(4,8)$. Its mean is $4/12=1/3$, the observed fraction is $3/10$, and its interior mode is $(4-1)/(4+8-2)=3/10$. The mean and mode differ because the posterior is skewed.{{cite:wang2025_foundations}} (Ch. 20, Example 11)
:::

## Common misconceptions
The posterior mean need not be a value with high posterior density: a long tail or several modes can move the average between peaks. In the Beta example, the prior contributes to the answer. The average of simulated draws is an *estimate of the posterior mean*, and its simulation error differs from the posterior spread those draws represent.{{cite:wang2025_foundations}} (Ch. 20, Sec. 24.1) {{cite:geyer1992}} (pp. 473–476)

## Assumptions and limits
A proper posterior can still have no finite mean if its tails are too heavy. Squared-error optimality requires a finite second moment and the specified loss; absolute error selects a posterior median. The normal formula assumes known observation variance. Dependent Markov-chain draws require convergence and dependence-aware error assessment.{{cite:hoff2013_bayes_estimators}} (pp. 9–13) {{cite:geyer1992}} (pp. 473–476)

## Connections
[Bayes' rule](bayes-rule.qmd) produces the posterior distribution whose mean is taken here. The [posterior median](posterior-median.qmd) minimizes absolute-error loss, while a [maximum-a-posteriori estimate](maximum-a-posteriori-estimate.qmd) maximizes posterior density. [Beta–Binomial conjugacy](beta-binomial-conjugacy.qmd) gives the first worked update, and [normal–normal conjugacy](normal-normal-conjugacy.qmd) gives the second. A [credible interval](bayesian-credible-interval.qmd) describes posterior uncertainty alongside the point estimate.{{cite:hoff2013_bayes_estimators}} (pp. 9–13) {{cite:wang2025_foundations}} (Ch. 20, Secs. 24–29)

## Check yourself
Work [the squared-error derivation](../questions/ex-applied-mmse.qmd), then [compare MAP with the squared-error estimate](../questions/c-07.qmd). For computational practice, [summarise one thousand posterior draws](../questions/exr-one-thousand-posterior-draws.qmd); identify which numbers describe posterior uncertainty and which measure simulation error.{{cite:hoff2013_bayes_estimators}} (pp. 9–10) {{cite:geyer1992}} (pp. 473–476)

## History
In Bayes's 1763 essay, communicated by Richard Price, the central question was what could be learned about an unknown success chance from observed successes and failures. The posterior distribution in the coin example addresses the same kind of inverse-probability question.{{cite:bayes1763}} (pp. 370–372)

Decision theory connects the choice of posterior summary to the loss from an error: squared error selects the posterior mean, while absolute error selects a median. Hoff's derivation makes this connection explicit.{{cite:hoff2013_bayes_estimators}} (pp. 9–10)

Computation broadened the use of posterior expectations. Metropolis and Ulam described random-sampling methods in 1949, and Geyer's 1992 treatment discusses dependent Markov-chain averages and their numerical error.{{cite:metropolis_ulam1949}} (pp. 335–336) {{cite:geyer1992}} (pp. 473–476)
