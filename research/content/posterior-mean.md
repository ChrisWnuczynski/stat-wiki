## Lead context
The posterior distribution describes plausible parameter values after observing data; its mean compresses that distribution into one number. It balances prior information with the likelihood in some conjugate models, but the balance depends on the model and the posterior must have a finite mean. For decisions, a point estimate is useful only after saying what errors the decision is meant to penalise.{{cite:gelman_bda2013,hoff2013_bayes_estimators}}

## Motivating example
Suppose a researcher initially regards a coin as roughly balanced and then observes seven heads in ten tosses. The observed fraction is $0.7$, but a posterior mean can lie between that fraction and the prior average. It reports the centre of the updated uncertainty rather than discarding the prior or pretending the observed fraction is exact.{{cite:gelman_bda2013}}

## Intuition
Imagine all possible values of an unknown parameter, each weighted by its posterior plausibility. The posterior mean is their weighted average. A long tail can pull it away from the most plausible single value, so it need not equal the posterior mode or median. This difference matters when a skewed posterior is summarised by one number, as the credible-region figure retained below illustrates for intervals.{{cite:gelman_bda2013}}

## Definition
Let $\Theta$ denote a scalar random parameter, $\theta$ a possible value, and $Y=y$ the observed data. If the posterior has density $p(\theta\mid y)$ and $\int|\theta|p(\theta\mid y)\,d\theta$ is finite, its posterior mean is

$$
m(y)=\mathbb E(\Theta\mid Y=y)=\int\theta p(\theta\mid y)\,d\theta.
$$

The integral is over the parameter's support; a discrete posterior uses a weighted sum instead. The old formulas above use $x$ for realised data and $\theta$ inside the posterior expectation; they describe the same conditional average with a different data label. A posterior variance requires a finite second moment, which is stronger than the condition for the mean alone.{{cite:gelman_bda2013,hoff2013_bayes_estimators}}

Under squared-error loss $L(\theta,d)=(d-\theta)^2$ for a reported value $d$, the posterior mean is the unique finite-risk Bayes action when the posterior second moment is finite. For absolute-error loss a posterior median is optimal instead; a maximum-a-posteriori estimate maximises density and is generally a different point. The phrase “best estimate” therefore needs a loss function.{{cite:hoff2013_bayes_estimators,gelman_bda2013}}

## Properties
With a $\operatorname{Beta}(a,b)$ prior on a Bernoulli success probability $\Theta$, $a,b>0$, and $x$ successes in $n$ independent trials, the posterior is $\operatorname{Beta}(a+x,b+n-x)$ and has mean

$$
\mathbb E(\Theta\mid x)=\frac{a+x}{a+b+n}
=\frac{a+b}{a+b+n}\frac{a}{a+b}
+\frac{n}{a+b+n}\frac{x}{n},\qquad n>0.
$$

Here $a/(a+b)$ is the prior mean and $x/n$ is the observed success fraction. Both weights are nonnegative and add to one; $a+b$ acts as a prior sample size *for this posterior-mean identity*. It is not an automatic pseudo-count interpretation for every posterior summary.{{cite:gelman_bda2013,raiffa_schlaifer1961}}

For a normal prior $\Theta\sim\operatorname{N}(m_0,\tau^2)$ and independent observations $Y_i\mid\Theta=\theta\sim\operatorname{N}(\theta,\sigma^2)$ with known positive variances, the posterior mean is

$$
m(y)=\frac{m_0/\tau^2+n\overline y/\sigma^2}{1/\tau^2+n/\sigma^2},
\qquad
\operatorname{Var}(\Theta\mid y)=\frac{1}{1/\tau^2+n/\sigma^2}.
$$

Here $m_0$ is the prior mean, $\tau^2$ its variance, $\sigma^2$ the observation variance, and $\overline y$ the observed sample mean. The mean weights $m_0$ and $\overline y$ by prior and data precision. This is a different weighting rule from the Beta count identity, though both show an explicit tradeoff between prior and data.{{cite:gelman_bda2013,hoff2013_bayes_estimators}}

The original draw average is a computational approximation to $m(y)$. For independent exact posterior draws with finite mean, its law of large numbers gives convergence as the number of draws grows. Markov-chain draws are dependent; their average may still estimate the posterior mean under suitable ergodicity conditions, but its Monte Carlo error must account for that dependence. The sample variance of the draws is a summary of *posterior uncertainty*, whereas the Monte Carlo standard error quantifies numerical uncertainty in the estimated mean.{{cite:metropolis_ulam1949,geyer1992}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $m=\mathbb E(\Theta\mid y)$ and assume a finite posterior second moment. Expanding $d-\Theta=(d-m)+(m-\Theta)$ gives

$$
\mathbb E[(d-\Theta)^2\mid y]
=\mathbb E[(m-\Theta)^2\mid y]+(d-m)^2,
$$

because the cross term contains $\mathbb E(m-\Theta\mid y)=0$. The first term does not depend on $d$, and the second is uniquely smallest at $d=m$. Integrating this pointwise result over the distribution of $Y$ proves the Bayes-risk statement when the overall risk exists. For absolute error, moving $d$ toward a posterior median decreases expected absolute deviation until at least half the posterior mass lies on each side; this proves the stated median qualification.{{cite:hoff2013_bayes_estimators}}

Multiplying the Beta prior kernel $\theta^{a-1}(1-\theta)^{b-1}$ by the binomial likelihood kernel $\theta^x(1-\theta)^{n-x}$ gives the Beta parameters $a+x,b+n-x$. The Beta mean formula yields $(a+x)/(a+b+n)$. Expanding the two weighted terms on the right gives $a/(a+b+n)+x/(a+b+n)$, proving the identity and the sum-to-one weights. For the normal model, collect the quadratic terms of $\theta$ in prior times likelihood: the coefficient of $\theta^2$ is $1/\tau^2+n/\sigma^2$, and the coefficient of $-2\theta$ is $m_0/\tau^2+n\overline y/\sigma^2$. Completing the square gives the displayed normal posterior mean and variance.{{cite:gelman_bda2013,hoff2013_bayes_estimators}}

For independent draws $\Theta^{(1)},\ldots,\Theta^{(L)}$ from the posterior with finite absolute mean, the strong law of large numbers makes $L^{-1}\sum_l\Theta^{(l)}$ converge to $m(y)$ almost surely. For a Markov chain, the corresponding conclusion uses an ergodic theorem for a chain with the posterior as stationary distribution and an integrable target function; independence cannot simply be assumed. This proves the approximation claim under the stated, different conditions.{{cite:geyer1992}}
:::
:::

## Statistical use
Report the posterior mean when squared-error consequences make it an appropriate point summary, alongside an interval or another description of uncertainty. A posterior mean by itself does not show skewness or multimodality; the two interval constructions in the preserved figure answer questions a single point cannot. For prediction under squared-error loss, average the future response over its posterior predictive distribution, rather than automatically plugging the parameter mean into a nonlinear prediction formula.{{cite:gelman_bda2013,hoff2013_bayes_estimators}}

When posterior expectations lack a closed form, simulated draws can approximate them. Check that the simulation explores the distribution and distinguish the spread of the parameter draws from the error of their numerical average. More draws can reduce Monte Carlo error; they do not create more observed data or shrink the underlying posterior uncertainty.{{cite:geyer1992}}

## Worked example
Use a $\operatorname{Beta}(2,2)$ prior for a coin and observe seven heads in ten trials. The posterior is $\operatorname{Beta}(9,5)$ and its mean is $9/14\approx0.643$. Equivalently, the prior mean $1/2$ gets weight $4/14$ and the observed fraction $7/10$ gets weight $10/14$: $(4/14)(1/2)+(10/14)(7/10)=9/14$. The interior posterior mode is $(9-1)/(9+5-2)=2/3$, so reporting the mode instead would answer a different question.{{cite:gelman_bda2013}}

As a normal example, take prior mean $m_0=0$, prior variance $\tau^2=4$, four observations with $\overline y=3$, and known observation variance $\sigma^2=4$. Prior precision is $1/4$ and data precision is $4/4=1$, so the posterior mean is $(0/4+4\cdot3/4)/(1/4+1)=2.4$, with posterior variance $1/(1/4+1)=0.8$.{{cite:hoff2013_bayes_estimators}}

**Your turn.** With a $\operatorname{Beta}(1,1)$ prior and three heads in ten trials, find the posterior mean and compare it with the observed fraction and the posterior mode.

::: {.callout-tip collapse="true" title="Answer"}
The posterior is $\operatorname{Beta}(4,8)$. Its mean is $4/12=1/3$, the observed fraction is $3/10$, and its interior mode is $(4-1)/(4+8-2)=3/10$. The mean and mode differ because the posterior is skewed.
:::

## Common misconceptions
The posterior mean need not be a value with high posterior density: a long tail or several modes can move the average between peaks. Nor is it a frequency computed solely from the data. In the Beta example the prior contributes to the answer. The average of simulated draws is an *estimate of the posterior mean*, and its simulation error differs from the posterior spread those draws represent.{{cite:gelman_bda2013,geyer1992}}

## Assumptions and limits
A proper posterior can still have no finite mean if its tails are too heavy. The squared-error optimality claim needs a finite second moment and the specified loss; a different loss gives a different optimal summary. The conjugate weighted-average formulas require their stated likelihoods, priors, and parameter conventions. The normal example assumes known observation variance; treating an estimated variance as exactly known changes the model. Dependent Markov-chain draws require convergence and dependence-aware error assessment before their average is trusted.{{cite:gelman_bda2013,hoff2013_bayes_estimators,geyer1992}}

## Connections
[Bayes' rule](bayes-rule.qmd) produces the posterior distribution whose mean is taken here. The [posterior median](posterior-median.qmd) minimises absolute-error loss, while a [maximum-a-posteriori estimate](maximum-a-posteriori-estimate.qmd) is a density maximiser; neither generally equals the squared-error Bayes action. [Beta–Binomial conjugacy](beta-binomial-conjugacy.qmd) gives the first worked update, and [normal–normal conjugacy](normal-normal-conjugacy.qmd) gives the second. A [credible interval](bayesian-credible-interval.qmd) describes posterior uncertainty that no single posterior mean can convey.{{cite:gelman_bda2013,hoff2013_bayes_estimators}}

## Check yourself
Work [the squared-error derivation](../questions/ex-applied-mmse.qmd), then [compare MAP with the squared-error estimate](../questions/c-07.qmd). For computational practice, [summarise one thousand posterior draws](../questions/exr-one-thousand-posterior-draws.qmd); identify which numbers describe posterior uncertainty and which measure simulation error.

## History
In Bayes's 1763 essay, communicated by Richard Price, the central inverse-probability question was what could be learned about an unknown success chance from observed successes and failures. Its mathematical setting anticipates the posterior distribution for a success probability used in the Beta example, without using today's point-estimate terminology. The posterior mean is one possible later summary of such an updated distribution, rather than a result the essay needs to be credited with naming.{{cite:bayes1763}}

Decision-theoretic treatments then made the choice of a posterior summary depend on the loss from a wrong decision. Raiffa and Schlaifer's 1961 work is an early cited source for applied statistical decision theory, while Hoff's modern derivation makes the squared-error rule explicit. Computation also broadened the use of posterior expectations: Metropolis and Ulam described random-sampling methods in 1949, and Geyer's 1992 treatment addresses dependent Markov-chain averages used in posterior integration. These sources document distinct developments; they do not establish a single inventor of the posterior mean.{{cite:raiffa_schlaifer1961,hoff2013_bayes_estimators,metropolis_ulam1949,geyer1992}}
