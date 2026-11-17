## Lead context
Uniformity means that the same testing rule wins at every parameter value allowed by the alternative.

## Motivating example
A production process has a nominal mean, and a test is intended to detect any increase. Optimising power for a small increase is useful only if it does not demand a different rejection rule from the one needed for a large increase. A one-sided normal mean problem has this compatibility; a two-sided problem usually does not.{{cite:siegrist2022_testing}} (§9.1, power and uniformly most powerful tests)

## Definition — One rule across an alternative
Write the power function as $\pi_\phi(\theta)=\mathbb E_\theta\phi(X)$. A test has level $\alpha$ if $\sup_{\theta\in\Theta_0}\pi_\phi(\theta)\le\alpha$. It is uniformly most powerful when, for every other level-$\alpha$ test $\psi$,
$$
\pi_\phi(\theta)\ge\pi_\psi(\theta)\quad\hbox{for every }\theta\in\Theta_1.
$$
The competitor is allowed to change, but the proposed test must dominate it at every alternative. A test can meet this definition while having low power near the null. The comparison is relative to the same size constraint.{{cite:siegrist2022_testing}} (§9.1, power function)

## Properties — A common likelihood-ratio ordering
For independent normal observations with known variance $\sigma^2$, the log likelihood ratio of mean $\mu_1>\mu_0$ against mean $\mu_0$ is
$$
\frac{n(\mu_1-\mu_0)}{\sigma^2}\overline X-
\frac{n(\mu_1^2-\mu_0^2)}{2\sigma^2}.
$$
It is increasing in the sample mean for every such $\mu_1$. The Neyman–Pearson cutoff with a fixed null probability therefore has the same rejection region for all upper alternatives. This establishes uniform optimality.{{cite:siegrist2022_lrt}} (§9.5, normal distribution applications) The underlying optimality compares rejection probabilities, including randomised tests when needed.{{cite:boyd_vandenberghe2004}} (§7.3.5, pp. 370–372)

For a composite one-sided null $\mu\le\mu_0$, the same rule controls size because $\Pr_\mu(\overline X>c)$ increases with $\mu$; its largest null rejection probability occurs at $\mu_0$. This step checks the whole null rather than only its boundary label.{{cite:siegrist2022_testing}} (§9.1, significance level)

## Worked example
Take $n=25$, $\sigma=2$, $\mu_0=10$ and $\alpha=0.05$. The standard error is $0.4$, giving cutoff
$$
c=10+1.644854(0.4)=10.657941.
$$
The power at $\mu=11$ is
$$
1-\Phi\left(\frac{10.657941-11}{0.4}\right)=0.803765.
$$
The level-$0.05$ two-sided normal rule has power $0.705418$ at this same mean. It spends some of its null rejection probability in the lower tail, which contributes very little power against an increase. These values illustrate the common-ordering argument rather than relying on asymptotic normality: the sampling distribution of the mean is exactly normal in this model.{{cite:siegrist2022_lrt}} (§9.5, normal distribution applications)

**Your turn.** With all other quantities unchanged, what is the upper-tail power at the boundary $\mu=10$?

::: {.callout-tip collapse="true" title="Answer"}
It is $1-\Phi(1.644854)=0.05$, the size. Power approaches this value as an upper alternative approaches the boundary.
:::

## Common misconceptions — Why two sides compete
If $\mu_1>\mu_0$, the most powerful normal test rejects for a large sample mean. If $\mu_1<\mu_0$, it rejects for a small sample mean. With a continuous normal distribution, the relevant likelihood-ratio equalities have probability zero, so the optimal regions are unique up to null sets. A single nontrivial level-$\alpha$ rule cannot equal both regions. Thus the unrestricted two-sided alternative has no uniformly most powerful test. Restricting the comparison to unbiased or invariant tests changes the optimisation problem and can yield a useful optimum.{{cite:siegrist2022_lrt}} (§9.5, The Neyman–Pearson Lemma){{cite:siegrist2022_testing}} (§9.1, optimal tests)

## Check yourself
Distinguish a pointwise power calculation from a claim of uniform optimality.

### The upper normal test {#self-check-ex-inf-np-critical}
[A critical value from the lemma](../questions/ex-inf-np-critical.qmd): calculate the cutoff and power for $n=25$, $\sigma=2$, $\mu_0=10$ and $\mu_1=11$.

::: {.callout-tip collapse="true" title="Answer"}
The cutoff is $10.657941$ and power is $0.803765$. The likelihood-ratio ordering is increasing in the mean for every upper alternative, so the same cutoff is used throughout that alternative.
:::

### A two-sided competitor {#self-check-ex-inf-ump-two-sided}
[Why the two-sided test is not UMP](../questions/ex-inf-ump-two-sided.qmd): compare the one-sided and two-sided level-$0.05$ tests at a mean two standard errors above the null.

::: {.callout-tip collapse="true" title="Answer"}
The upper-tail rule has power $\Phi(2-1.644854)\approx0.638760$. The two-sided rule has power $1-\Phi(1.959964-2)+\Phi(-1.959964-2)\approx0.516005$. A lower-tail rule instead wins against lower alternatives, preventing one rule from winning on both sides.
:::
