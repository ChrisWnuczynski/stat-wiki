## Motivating example

Suppose a manufacturer wants a probability for the fraction of components that pass a test. A preliminary estimate and a short new sample both contain information, but they need not be weighted equally. A beta prior records a range of plausible pass rates; a binomial likelihood records the new successes and failures. Their product is still a beta density, so the updated uncertainty can be calculated by adding the two observed counts to the two prior shape parameters{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example).

## Statement

The displayed update applies when the trials are conditionally independent given one common probability $\theta$, the sample size $n$ is fixed, and both beta shapes are strictly positive. The binomial coefficient depends on the observed count but not on $\theta$, so it disappears when the posterior kernel is identified. Normalising that kernel still matters: only after division by its beta integral is it a probability density{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example).

## Intuition — why the beta shape survives

Successes add to the first beta shape and failures to the second. This is a computational form of learning, but the shapes are not necessarily records of literal earlier trials. A $\operatorname{Beta}(1,1)$ density is uniform on $(0,1)$, for example, rather than evidence that one success and one failure were actually seen. What matters is that the prior powers of $\theta$ and $1-\theta$ match the likelihood's powers, allowing multiplication to keep the same family{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example).

The update does not say the observed rate is the posterior mean. With $\operatorname{Beta}(\alpha,\beta)$ prior, the posterior mean is $(\alpha+x)/(\alpha+\beta+n)$. It is a weighted average of prior mean $\alpha/(\alpha+\beta)$ and observed rate $x/n$, with weights $\alpha+\beta$ and $n$ after normalization by their sum. The total concentration $\alpha+\beta$ controls the prior's influence in this mean calculation. {{cite:dodge2008}} (p. 40, beta mean)

## Key results

If two independent batches contain $x_1$ successes in $n_1$ trials and $x_2$ in $n_2$, updating twice gives $\operatorname{Beta}(\alpha+x_1+x_2,\beta+n_1+n_2-x_1-x_2)$. Updating on their pooled counts gives the same answer. This *sequential coherence* follows because addition commutes; it does not require the batches to arrive in a particular order. The common-rate and conditional-independence assumptions make the joint likelihood a product of the two binomial kernels{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example).

For one further Bernoulli trial $Y$, the posterior predictive chance of success is $\Pr(Y=1\mid x)=\mathbb E(\theta\mid x)=(\alpha+x)/(\alpha+\beta+n)$. For several future trials, averaging the conditional binomial probabilities over the posterior gives a beta–binomial predictive distribution, which accounts for uncertainty about $\theta$. Simply inserting the posterior mean into a binomial distribution does not make the full predictive law identical{{cite:dodge2008}} (p. 40, beta mean).

## Proof

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The prior density is $p(\theta)=\theta^{\alpha-1}(1-\theta)^{\beta-1}/B(\alpha,\beta)$ for $0<\theta<1$, where $B(a,b)=\int_0^1t^{a-1}(1-t)^{b-1}\,dt$. For $X=x$, the binomial likelihood is ${n\choose x}\theta^x(1-\theta)^{n-x}$. Their product is proportional to $\theta^{\alpha+x-1}(1-\theta)^{\beta+n-x-1}$. Because $\alpha+x>0$ and $\beta+n-x>0$, its integral is the finite beta function $B(\alpha+x,\beta+n-x)$. Dividing by that integral proves that $\theta\mid X=x\sim\operatorname{Beta}(\alpha+x,\beta+n-x)$. The same multiplication with separate likelihoods for two conditionally independent batches adds both sets of exponents and proves the sequential result{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example).

Finally, for one future Bernoulli $Y$, conditional expectation gives $\Pr(Y=1\mid x)=\int_0^1\theta p(\theta\mid x)\,d\theta=B(\alpha+x+1,\beta+n-x)/B(\alpha+x,\beta+n-x)=(\alpha+x)/(\alpha+\beta+n)$. This integral makes clear why a posterior predictive probability averages across uncertain rates. {{cite:dodge2008}} (p. 40, beta mean)::::::

## Generalizations

The same algebra works with individually recorded Bernoulli outcomes: their likelihood is $\theta^x(1-\theta)^{n-x}$ when $x$ of $n$ outcomes are successes. A geometric sampling scheme that counts successes before a first failure can also produce a beta update because its likelihood has the same powers of $\theta$ and $1-\theta$; the observation and stopping rule still need to be reported{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example).

## Statistical use

Report the prior shapes, observed counts and posterior shapes together. A point estimate such as the posterior mean is only one summary; posterior quantiles answer uncertainty questions, and a predictive calculation answers a different question about future observations. Prior sensitivity matters most when $n$ is small relative to $\alpha+\beta$. The displayed figure illustrates three prior choices that yield visibly different posteriors after $3$ successes in $10$ trials but much closer posteriors after $30$ in $100$; that observation depends on those particular priors and data{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example).

## Worked example

### Updating and predicting a pass rate
Start with $\theta\sim\operatorname{Beta}(2,3)$ and observe $7$ passes in $20$ independent tests. The posterior is $\operatorname{Beta}(9,16)$: seven successes add to the first shape and thirteen failures to the second. Its mean is $9/25=0.36$, between the prior mean $2/5=0.40$ and the observed rate $7/20=0.35$. Its variance is $9\cdot16/(25^2\cdot26)=144/16250\approx0.00886$. The probability that the next two independent components both pass, conditional on the same unknown $\theta$, is $\mathbb E(\theta^2\mid x)=9\cdot10/(25\cdot26)=9/65\approx0.1385$. Squaring the posterior mean instead gives $0.1296$; the difference reflects uncertainty about the common rate.{{cite:dodge2008}} (p. 40, beta moments)

**Your turn.** Use a $\operatorname{Beta}(1,1)$ prior, then observe four successes in five independent trials. Find the posterior, its mean, and the posterior predictive probability of at least one success in the next two trials under the same common-rate model.

::: {.callout-tip collapse="true" title="Answer"}
The posterior is $\operatorname{Beta}(5,2)$ with mean $5/7\approx0.7143$. The chance of two failures is $\mathbb E[(1-\theta)^2\mid x]=2\cdot3/(7\cdot8)=3/28$, so the chance of at least one success is $1-3/28=25/28\approx0.8929$. Using $(1-5/7)^2$ would treat the uncertain rate as known and give a different answer.
:::

## Common misconceptions

The posterior is not $\operatorname{Beta}(\alpha+x,\beta+x)$: failures, not successes, increment the second shape. The prior shapes are not automatically past trial counts; they specify a density even when no earlier physical trials were observed. A binomial plug-in at the posterior mean is not the full multi-trial predictive distribution because it omits variation in the shared $\theta$. Finally, conjugacy is a computational convenience, not a requirement for a valid Bayesian prior: a proper nonconjugate prior can still produce a well-defined posterior{{cite:diaconis_ylvisaker1979}} (§1, pp. 269–270, beta-binomial example).

## History

Bayes's investigation of inference from repeated successes and failures was published in 1763 after Richard Price prepared his papers. That early inverse-probability setting is historically related to updating an unknown success chance, but the compact beta-family terminology is a later way to organise the calculation.{{cite:dodge2008}} (p. 32, Bayes entry)
