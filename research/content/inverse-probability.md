## Lead context

A direct probability runs from a known chance to the observations: if the chance of success is one half, the probability of a success is one half. Inverse probability runs the other way. It states a probability for the unknown chance given the observations. In current vocabulary that step is Bayesian inference, and the probability it produces is a posterior probability. {{cite:dodge2008}} (pp. 32–33) {{cite:gelman_bda2013}} (Ch. 1, §1.1, p. 3)

## Motivating example

One trial is a success, and before the trial the unknown chance $\theta$ was taken as uniform on the unit interval. The direct probability of a success at $\theta=1/2$ is $1/2$. The inverse question is different: after the success, what is the probability that $\theta$ itself exceeds $1/2$? The uniform assignment and Bayes’ theorem answer $3/4$. The data have moved the probability attached to the upper half of the chance. {{cite:dodge2008}} (p. 33)

## Definition

Inverse probability is the historical practice of assigning a probability to an unknown given the observations. Dodge’s account of the modern calculation is Bayes’ theorem in continuous form. If $f(\theta)$ is the distribution assigned to the unknown before the data and $f(D\mid\theta)$ is the sampling model, the distribution after the data is

$$
f(\theta\mid D)=\frac{f(D\mid\theta)\,f(\theta)}{\int f(D\mid\theta)\,f(\theta)\,d\theta}.
$$


The first two steps — name the observations, and name a parametric family for them — are shared with every parametric analysis. The third step, a distribution for $\theta$ before the data, is the one that makes a probability for $\theta$ available afterwards. The distribution $f(\theta\mid D)$ is the final distribution in that vocabulary, and the posterior in the current one. {{cite:dodge2008}} (pp. 32–33)

Gelman’s statement of the same inversion in odds form is short. The posterior odds of one value against another equal the prior odds multiplied by the likelihood ratio of the observed data. The marginal probability of the data cancels, which is why the odds form is the convenient one. A probability for the unknown given the data is what the older name “inverse probability” was pointing at. {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8)

## Properties

Take $\theta$ uniform on $[0,1]$, so $f(\theta)=1$, and let $y$ successes occur in $n$ independent Bernoulli trials. The likelihood is $\theta^y(1-\theta)^{n-y}$. The posterior density is proportional to that likelihood. For one success in one trial the kernel is $\theta$, and $\int_0^1\theta\,d\theta=1/2$, so the posterior density is $2\theta$. Then

$$
\mathbb{P}(\theta>1/2\mid y=1)=\int_{1/2}^1 2\theta\,d\theta=1-\left(\frac{1}{2}\right)^2=\frac{3}{4}.
$$


The marginal probability of the success, the denominator in Bayes’ theorem, is $1/(1+1)=1/2$. {{cite:dodge2008}} (p. 33)

For a single failure the kernel is $1-\theta$, the posterior density is $2(1-\theta)$, and

$$
\mathbb{P}(\theta>1/2\mid y=0)=\int_{1/2}^1 2(1-\theta)\,d\theta=\frac{1}{4}.
$$


A success pushes probability toward larger chances. A failure pushes it toward smaller ones. The uniform assignment is one choice of $f(\theta)$. A different initial distribution produces a different inverse probability from the same count. {{cite:dodge2008}} (pp. 32–33)

The hemophilia example in Gelman is the same inversion with a discrete unknown. A woman has prior probability $1/2$ of being a carrier. Two unaffected sons have likelihood $0.25$ if she is a carrier and $1$ if she is not. The prior odds are $1$. The likelihood ratio is $0.25$. The posterior odds are $0.25$, and the posterior probability is $0.25/(1+0.25)=0.2$. Adding a third unaffected son updates that probability to $0.111$ without rebuilding the whole table: the previous posterior becomes the next prior. {{cite:gelman_bda2013}} (Ch. 1, §1.4, pp. 8–9)

## Worked example

One trial, one success, $\theta$ uniform on $[0,1]$. The posterior density is $2\theta$. The probability that the chance exceeds one half is $3/4$. The direct probability of a success when the chance equals one half remains $1/2$. Those are different probabilities. The first is about $\theta$ after the data. The second is about the data at a fixed $\theta$. {{cite:dodge2008}} (p. 33) {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8)

**Your turn.** The single trial is a failure, so the posterior density is $2(1-\theta)$. Find $\mathbb{P}(\theta>1/2\mid y=0)$.

::: {.callout-tip collapse="true" title="Answer"}
The integral is $\int_{1/2}^1 2(1-\theta)\,d\theta=\bigl[2\theta-\theta^2\bigr]_{1/2}^1=(2-1)-(1-1/4)=1/4$.
:::

## Assumptions and limits

The inversion needs a distribution for the unknown before the data. Dodge is explicit that this step is the problematic one: without supplementary information one looks for a reference distribution, and the uniform distribution on a chance is one such choice, not a requirement of Bayes’ theorem. A posterior probability computed under that choice is not the relative frequency of the interval in repeated samples. [Frequentist inference](frequentist-inference.qmd) scores procedures by those frequencies. Inverse probability scores the unknown. {{cite:dodge2008}} (pp. 32–33) {{cite:gelman_bda2013}} (Ch. 1, §1.1, p. 3)

The likelihood has to be the sampling model for the observations that were actually used. In the Bernoulli case the trials are independent given $\theta$. If they are not, the product $\theta^y(1-\theta)^{n-y}$ is the wrong likelihood and the posterior is the posterior for a different experiment. The hemophilia calculation ignores the mutation rate, which Gelman notes is small enough to set aside for that example. Putting the mutation rate back would change both likelihoods and the posterior probability of being a carrier. {{cite:gelman_bda2013}} (Ch. 1, §1.4, p. 9) {{cite:dodge2008}} (p. 33)

## History

Bayes’s theorem is named for Thomas Bayes and was presented by Richard Price to the Royal Society on 23 December 1763, two years after Bayes’s death. The continuous form used above is the form in which a density for a parameter is updated by a likelihood. Laplace’s analytic theory of probabilities carried the same inversion into astronomical and demographic calculations. The twentieth-century name for the practice is Bayesian statistics: identify the data, name a sampling model, name an initial distribution, and calculate the final distribution. Inverse probability is the older name for that final distribution’s probabilities. {{cite:dodge2008}} (pp. 31–33) {{cite:gelman_bda2013}} (Ch. 1, §1.3, p. 8)
