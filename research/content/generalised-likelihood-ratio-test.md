## Motivating example

A laboratory wants to test whether two populations have the same normal mean while allowing their shared mean to be unknown. Fitting under equality estimates that nuisance mean; fitting without equality estimates two means. The likelihood ratio measures the loss of fit imposed by equality.{{cite:siegrist2022_lrt}} (§9.5, Composite Hypotheses)

## Definition — Restricted fit against the full model

Write the full parameter space as $\Theta$ and the null subset as $\Theta_0\subseteq\Theta$. Use
$$
\Lambda(x)=\frac{\sup_{\theta\in\Theta_0}L(\theta;x)}{\sup_{\theta\in\Theta}L(\theta;x)},\qquad
D=-2\log\Lambda.
$$
Here the denominator includes the null: this convention ensures $0\le\Lambda\le1$ when the denominator is finite and positive. Suprema accommodate parameter values approached at a boundary. The statistic ranks disagreement with the restriction; its null distribution supplies a rejection threshold.{{cite:siegrist2022_lrt}} (§9.5, Composite Hypotheses)

Likelihood-ratio testing compares model fit on the same observations and sampling model. The ratio itself is neither the probability that the null is true nor a posterior odds ratio.{{cite:dodge2008}} (p. 309)

## Properties — An exact normal calibration

For independent $X_i\sim N(\mu,\sigma^2)$ with known positive $\sigma$, the null $\mu=\mu_0$ restricts the normal likelihood at one point. Its unrestricted maximiser is $\bar X$. Expanding the squared deviations gives
$$
D=\frac{n(\bar X-\mu_0)^2}{\sigma^2}=Z^2,
\qquad Z=\frac{\sqrt n(\bar X-\mu_0)}{\sigma}.
$$
Under the null, $Z$ is exactly standard normal and $D$ is exactly chi-squared with one degree of freedom. This calculation needs no large-sample approximation. Composite-model likelihood ratios can instead require an asymptotic calibration, whose regularity conditions must be checked for the model at hand.{{cite:siegrist2022_lrt}} (§9.5, Normal Distribution)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The identity $\sum_i(x_i-\mu_0)^2=\sum_i(x_i-\bar x)^2+n(\bar x-\mu_0)^2$ follows because $\sum_i(x_i-\bar x)=0$. Subtract the maximised normal log likelihoods and multiply by two. The normal law of $\bar X$ gives the displayed null distribution.
:::
:::

## Worked example

Suppose $n=16$, $\sigma=2$, $\bar x=1$, and the null mean is zero. Then $Z=2$, $D=4$, and $\Lambda=e^{-2}\approx0.1353$. The two-sided tail probability is $\mathbb{P}(|Z|\ge2)\approx0.04550$. A level-$0.05$ test rejects. The ratio $0.1353$ and the tail probability $0.04550$ answer different questions: the first compares maximised likelihoods at the observed sample, and the second counts samples at least this discrepant under the null.{{cite:siegrist2022_lrt}} (§9.5, Normal Distribution)

**Your turn.** Keep $n$ and $\sigma$ fixed but set $\bar x=0.5$. Compute $D$ and $\Lambda$.

::: {.callout-tip collapse="true" title="Answer"}
$Z=1$, so $D=1$ and $\Lambda=e^{-1/2}\approx0.6065$. The two-sided standard-normal tail is about $0.3173$.
:::

## Connections — Deviance differences

If two nested models use the same saturated model to define their deviances, subtracting the deviances cancels that saturated likelihood. What remains is twice the difference between the two fitted log likelihoods. The comparison requires both likelihoods to refer to the same observed data; fitting one model after dropping additional observations changes the comparison.{{cite:siegrist2022_lrt}} (§9.5, Composite Hypotheses)

## Check yourself

### [Two normal means](../questions/ex-inf-glrt-two-means.qmd) {#self-check-ex-inf-glrt-two-means}

Two groups each have eight observations, known variance four, and means twelve and fifteen. Find the between-group sum of squares and the likelihood-ratio statistic.

::: {.callout-tip collapse="true" title="Answer"}
The pooled mean is $13.5$. Thus $SS_B=8(12-13.5)^2+8(15-13.5)^2=36$, and $D=36/4=9$. It exceeds the stated $3.84$ cutoff.
:::

### [How many restrictions?](../questions/ex-inf-which-restriction.qmd) {#self-check-ex-inf-which-restriction}

For an intercept, nitrogen, phosphorus and their product, how many independent restrictions remove all three non-intercept terms?

::: {.callout-tip collapse="true" title="Answer"}
Three. Set each of those three coefficients to zero; the intercept remains free under the null.
:::
