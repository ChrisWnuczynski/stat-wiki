## Lead context
Two models may both fit the observed data well at their best parameter values yet make different predictions before those parameters are known. A marginal likelihood averages each model's sampling probability over its own parameter prior. A Bayes factor divides two such averages, reporting how much the observed data shift the odds between the models. The direction of that ratio and the priors used in the averages must be stated.{{cite:kass_raftery1995}} (§3.1, pp. 777–778; §5, pp. 783–786)

## Motivating example
Suppose a quality team compares a fixed success probability of $1/2$ with a model allowing an unknown success probability. Observing one success may fit both models, but the flexible model must say *beforehand* which success probabilities it regards as plausible. If its parameter prior is $\operatorname{Beta}(2,1)$, its predictive probability of one success is the prior mean $2/3$, versus $1/2$ under the fixed model. Their ratio is $4/3$. A different proper prior on the flexible model would give a different predictive probability. The factor measures the relative predictive support of this datum under these stated models; it is not itself the probability that either model is true.{{cite:kass_raftery1995}} (§§3.1, 5.1, pp. 777–778, 783–784)

## Intuition
Think of each model as committing to a distribution over possible data. In a model with an unknown parameter, that commitment requires averaging its conditional data distributions against a prior distribution for the parameter. Parameters with high likelihood but negligible prior mass contribute little to the average. Maximising the likelihood instead picks a favourable parameter *after seeing the data*, so the two operations answer different questions. A model with more ways to fit data does not automatically have a higher marginal likelihood for the data actually observed.{{cite:kass_raftery1995}} (§§3.1, 5.1, pp. 777–778, 783–784)

Bayes factors operate on odds. If prior odds for $M_1$ versus $M_0$ are $1:4$, a Bayes factor of $2$ for $M_1$ changes them to $1:2$, not to a posterior probability of $2$. Converting odds $1:2$ to probability gives $1/3$ for $M_1$. This is the coin example's distinction between data favouring a model and that model having the larger posterior probability.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

## Definition
For a model $M_j$ with parameter $\theta_j$ and proper prior $\pi_j(\theta_j)$, its marginal likelihood for data $x$ is $m_j(x)=p(x\mid M_j)=\int p(x\mid\theta_j,M_j)\pi_j(\theta_j)\,\mathrm d\theta_j$. For discrete parameters, replace the integral by a sum. The Bayes factor in favour of $M_1$ over $M_0$ is $\operatorname{BF}_{10}=m_1(x)/m_0(x)$ when $m_0(x)>0$. Its reciprocal is $\operatorname{BF}_{01}$ when both marginals are positive. Both models must use the same observed data and a common way of measuring its probability or density.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

A prior over the *models*, such as $\mathbb P(M_1)=q$, is a separate input from the parameter prior within each model. For exactly two models with positive prior probabilities, posterior odds equal $\operatorname{BF}_{10}$ times prior odds. With more than two models, normalise the products $m_j(x)\mathbb P(M_j)$ over all models under consideration. A ratio of marginal likelihoods does not by itself encode the prior model odds or the posterior model probability.{{cite:kass_raftery1995}} (§3.1, pp. 777–778; §6, pp. 789–790)

## Properties
The marginal likelihood is a prior predictive probability or density for the observed data. If a model has no unknown parameter, it reduces to that model's ordinary sampling probability. If both models are simple, the Bayes factor is their likelihood ratio. If one has unknown parameters, integration rather than maximisation is essential: the prior predictive distribution accounts for how much parameter space supports the observation.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

For a binomial count $X=x$ out of $n$ and a $\operatorname{Beta}(a,b)$ parameter prior under $M_1$, direct integration gives
$$
m_1(x)=\binom nx\frac{B(x+a,n-x+b)}{B(a,b)}.
$$
The binomial coefficient belongs in this mass when the data are the count. It cancels in a Bayes factor against another binomial-count model using the same $n$ and $x$, but dropping it from only one side would give a false factor. Under a point model $M_0:p=p_0$, the other marginal is $\binom nx p_0^x(1-p_0)^{n-x}$. The uniform-prior example is the special case $a=b=1$.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Under $M_1$, the binomial likelihood is $\binom nx p^x(1-p)^{n-x}$ and the beta prior density is $p^{a-1}(1-p)^{b-1}/B(a,b)$. Their product integrates to $\binom nx B(x+a,n-x+b)/B(a,b)$, proving the displayed marginal. Under $M_0$, $p=p_0$ is fixed, so no integration is needed. For a single success with $a=2,b=1$, $B(3,1)/B(2,1)=(1/3)/(1/2)=2/3$; for a single failure, $B(2,2)/B(2,1)=(1/6)/(1/2)=1/3$.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

Bayes' rule over the model labels gives $\mathbb P(M_j\mid x)=m_j(x)\mathbb P(M_j)/\sum_km_k(x)\mathbb P(M_k)$. Taking the ratio for two models cancels the common denominator and yields posterior odds $=\operatorname{BF}_{10}\times$ prior odds. This also proves that swapping the model order inverts the factor but does not alter the underlying comparison.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)
:::
:::

## Statistical use
Before computing a factor, state the sampling model, what constitutes the data, each parameter prior, and the prior probabilities of the competing models if posterior model probabilities are wanted. Compute the integral with analytic beta functions, numerical quadrature, or a justified approximation. Report the direction of the factor, the data scale, and sensitivity to reasonable prior choices. The battery-lifetime example illustrates why the same data can look different under exponential and gamma models whose prior predictions differ.{{cite:kass_raftery1995}} (§§3.1, 4, 5, pp. 777–786)

A proper parameter prior is normally needed to make each marginal a defined probability distribution. An arbitrary multiplicative constant in an improper prior can remain in the marginal and hence in the factor. Some specialised constructions handle shared nuisance priors, but they require explicit justification; simply inserting a flat improper density into a one-model-only parameter is not a valid shortcut. Comparing model probabilities also requires a set of alternatives: adding a plausible third model changes the normalising denominator of posterior probabilities even when a pairwise factor stays the same.{{cite:kass_raftery1995}} (§§3.1, 5.3, 6, pp. 777–778, 785–790)

## Worked example
Let $M_0$ fix a success probability at $1/2$ and let $M_1$ assign it a $\operatorname{Beta}(2,1)$ prior. A single success has $m_0(1)=1/2$ and $m_1(1)=2/3$, so $\operatorname{BF}_{10}=(2/3)/(1/2)=4/3$. Suppose the model prior probabilities are $\mathbb P(M_1)=3/10$ and $\mathbb P(M_0)=7/10$. Prior odds for $M_1$ are $3/7$; posterior odds are $(4/3)(3/7)=4/7$. Normalising gives $\mathbb P(M_1\mid X=1)=4/11\approx0.3636$. The observation favours $M_1$ relative to $M_0$, but the posterior probability of $M_0$ remains $7/11$.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

**Your turn.** Keep these two models and their prior model probabilities, but suppose the single trial is a failure, $X=0$. Find both marginal probabilities, the Bayes factor favouring $M_1$, and the posterior probability of $M_1$. Explain which model the failure favours.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)

::: {.callout-tip collapse="true" title="Answer"}
Under $M_0$, $m_0(0)=1/2$. Under the $\operatorname{Beta}(2,1)$ prior, the predictive failure probability is $m_1(0)=1-\mathbb E(p)=1/3$. Thus $\operatorname{BF}_{10}=(1/3)/(1/2)=2/3$, favouring $M_0$. Posterior odds for $M_1$ are $(2/3)(3/7)=2/7$, so $\mathbb P(M_1\mid X=0)=2/9\approx0.2222$. The posterior probability follows from the prior odds and the factor together.{{cite:kass_raftery1995}} (§3.1, pp. 777–778)
:::

## Common misconceptions
A factor of $4/3$ does not mean a $4/3$ probability, a $75\%$ probability, or a guarantee that $M_1$ is right. It is a multiplier of *model odds*. The factor can favour a model that still has less than half the posterior probability when its prior model odds were low. Replacing the integral by the maximum likelihood changes the quantity. A p-value is another probability about data under a null model, not the posterior probability of that null model or a Bayes factor.{{cite:kass_raftery1995}} (§§3.1, 8.2, pp. 777–778, 791–792)

## Assumptions and limits
Bayes factors compare the specified models and priors, not every conceivable explanation. Their sensitivity to within-model priors can be substantial, especially for a sharp null against a diffuse alternative. A density ratio also depends on using a common observation and reference measure; a binomial count probability cannot be divided by a probability for a different data event. When a marginal in the denominator is zero, the finite-ratio expression is unavailable. Prior predictive checks and sensitivity analysis remain useful even after the arithmetic is exact.{{cite:kass_raftery1995}} (§§3.1, 5, pp. 777–786)

## Connections
[Bayes' rule](bayes-rule.qmd) produces the posterior model probabilities, while [posterior odds](posterior-odds-factorisation.qmd) expose the multiplication by the factor. A [likelihood function](likelihood-function.qmd) conditions on a parameter; a marginal likelihood averages over it. [Bayesian information criterion](bayesian-information-criterion.qmd) supplies an asymptotic approximation in suitable settings, not an exact replacement for the integral. Model averaging uses posterior model probabilities when several models remain plausible.{{cite:kass_raftery1995}} (§§3.1, 4.1.3, 6, pp. 777–782, 789–790)

## History
Kass and Raftery's 1995 review traces modern Bayes-factor model comparison to Jeffreys's 1930s work and discusses the later separation of prior odds from the data multiplier. Its examples include comparisons that are not nested, a reason the method extends beyond a single parameter restriction. {{cite:kass_raftery1995}} (§§1, 3.1, pp. 773–778)
