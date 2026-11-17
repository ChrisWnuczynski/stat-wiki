## Motivating example
In three independent trials, the first pair's product $X_1X_2$ estimates the probability of two successes without bias. It ignores the third trial. Conditioning on the total success count produces an estimator that uses the sample symmetrically and has smaller variance. The Lehmann–Scheffé theorem identifies when that improvement is the unique best unbiased estimator.{{cite:siegrist2022_sufficient_complete}} (§7.6, “Lehmann-Scheffé Theorem”)

## Definition — Two conditions on the reduction
A statistic $T$ is sufficient when the conditional law of the data given $T$ is free of the unknown parameter. It is complete when every integrable function $h(T)$ having expectation zero at every parameter value is itself zero almost surely at every parameter value. Both properties depend on the statistical family, including its parameter space.{{cite:siegrist2022_sufficient_complete}} (§7.6, “Sufficient Statistics” and “Complete Statistics”)

If $T$ is complete and sufficient and $\delta(T)$ is unbiased for $g(\theta)$ with finite variance, then $\delta(T)$ is the unique uniformly minimum-variance unbiased estimator of $g(\theta)$, up to almost-sure equality. The comparison is with unbiased estimators having finite variance, at every parameter value.{{cite:siegrist2022_sufficient_complete}} (§7.6, “Lehmann-Scheffé Theorem”)

## Properties — Why completeness supplies uniqueness
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $U$ be any competing unbiased estimator. Sufficiency makes $V(T)=E(U\mid T)$ a statistic independent of the unknown parameter in its definition. The tower property gives $E[V(T)]=g(\theta)$. Thus $E[V(T)-\delta(T)]=0$ throughout the model, and completeness gives $V(T)=\delta(T)$ almost surely. Finally,
$$
\operatorname{Var}(U)=\operatorname{Var}\{V(T)\}+E\{\operatorname{Var}(U\mid T)\}\ge\operatorname{Var}\{\delta(T)\}.
$$
Equality forces $U=V(T)$ almost surely. This proves both optimality and uniqueness among finite-variance unbiased estimators.{{cite:siegrist2022_sufficient_complete}} (§7.6, Rao–Blackwell and Lehmann–Scheffé theorems)
:::
:::

For binomial counts, allowing the success probability to range over an interval supplies completeness. Restricting the parameter to a few isolated values can remove that property. Completeness is therefore more than a fact about the numerical values a statistic can take.{{cite:dasgupta2011_exponential_family}} (§18.4, Ex. 18.16 and Thm. 18.8, pp. 511–512)

## Worked example
Let $X_1,X_2,X_3$ be independent Bernoulli$(p)$ variables and $T=X_1+X_2+X_3$. Conditional on $T=t$, all locations of the $t$ successes are equally likely. The chance that both the first and second positions succeed is
$$
E(X_1X_2\mid T=t)=\frac{t(t-1)}{3\cdot2}.
$$
Consequently $\delta(T)=T(T-1)/6$ is unbiased for $p^2$. At $T=2$ it equals $1/3$; at $T=3$ it equals $1$. Since $T$ is complete and sufficient for $0<p<1$, this is the unique UMVU estimator.{{cite:siegrist2022_sufficient_complete}} (§7.6, Bernoulli-distribution application){{cite:dasgupta2011_exponential_family}} (§18.4, Ex. 18.17, p. 512)

At $p=1/2$, $\operatorname{Var}(X_1X_2)=3/16$, whereas $\operatorname{Var}\{\delta(T)\}=5/48$. The latter is smaller by $1/12$. This calculation concerns repeated samples, not the precision of a particular observed value of $T$.

**Your turn.** Find $E\{T(T-1)\}$ and use it to verify unbiasedness without conditioning.

::: {.callout-tip collapse="true" title="Answer"}
There are six ordered pairs of distinct trials. Each pair succeeds with probability $p^2$, so $E\{T(T-1)\}=6p^2$ and $E\{T(T-1)/6\}=p^2$.
:::

## Check yourself

### A probability of two successes {#self-check-exr-completeness-binomial}

[Practice question](../questions/exr-completeness-binomial.qmd)

Evaluate the unbiased estimator of $p^2$ when three trials give $T=2$.

::: {.callout-tip collapse="true" title="Answer"}
The value is $T(T-1)/6=2/6=1/3$. Completeness makes it the only unbiased function of the full binomial count.
:::

### Conditioning an estimator {#self-check-ex-inf-rao-blackwell-variance}

[Practice question](../questions/ex-inf-rao-blackwell-variance.qmd)

Why does conditioning on a sufficient statistic give a statistic, preserve unbiasedness, and reduce variance?

::: {.callout-tip collapse="true" title="Answer"}
Sufficiency removes the unknown parameter from the conditional distribution. Iterated expectation preserves the target mean. Total variance subtracts the nonnegative expected conditional variance.
:::
