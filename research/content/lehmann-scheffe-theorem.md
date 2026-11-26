## Motivating example
In three independent trials, the first pair's product $X_1X_2$ estimates the probability of two successes without bias. It ignores the third trial. Conditioning on the total success count produces an estimator that uses the sample symmetrically and has smaller variance. The Lehmann–Scheffé theorem identifies when that improvement is the unique best unbiased estimator.{{cite:siegrist2022_sufficient_complete}} (§7.6, “Lehmann-Scheffé Theorem”)

## Definition — Two conditions on the reduction
A statistic $T$ is sufficient when the conditional law of the data given $T$ is free of the unknown parameter. It is complete when every integrable function $h(T)$ having expectation zero at every parameter value is itself zero almost surely at every parameter value. Both properties depend on the statistical family, including its parameter space.{{cite:siegrist2022_sufficient_complete}} (§7.6, “Sufficient Statistics” and “Complete Statistics”)

If $T$ is complete and sufficient and $\delta(T)$ is unbiased for $g(\theta)$ with finite variance, then $\delta(T)$ is the unique uniformly minimum-variance unbiased estimator of $g(\theta)$, up to almost-sure equality. The comparison is with unbiased estimators having finite variance, at every parameter value.{{cite:siegrist2022_sufficient_complete}} (§7.6, “Lehmann-Scheffé Theorem”)

## Properties — Why completeness supplies uniqueness
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $U$ be any competing unbiased estimator. Sufficiency makes $V(T)=\E(U\mid T)$ a statistic independent of the unknown parameter in its definition. The tower property gives $\E[V(T)]=g(\theta)$. Thus $\E[V(T)-\delta(T)]=0$ throughout the model, and completeness gives $V(T)=\delta(T)$ almost surely. Finally,
$$
\operatorname{Var}(U)=\operatorname{Var}\{V(T)\}+\E\{\operatorname{Var}(U\mid T)\}\ge\operatorname{Var}\{\delta(T)\}.
$$
Equality forces $U=V(T)$ almost surely. This proves both optimality and uniqueness among finite-variance unbiased estimators.{{cite:siegrist2022_sufficient_complete}} (§7.6, Rao–Blackwell and Lehmann–Scheffé theorems)
:::
:::

A complete sufficient statistic also gives a minimal sufficient reduction in the usual standard Borel setting with common parameter-free conditional distributions. Here minimality is understood up to null sets. The conditional-expectation argument uses bounded functions, so it does not require moments of $T$ itself.{{cite:siegrist2022_sufficient_complete}} (§7.6, sufficient, complete and minimal sufficient statistics)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $U$ be any sufficient statistic and $f(T)$ any bounded measurable function. Put $g(U)=\E_\theta[f(T)\mid U]$ and $h(T)=\E_\theta[g(U)\mid T]$. Sufficiency supplies versions of both functions independent of $\theta$. Iterated expectation gives $\E_\theta[h(T)-f(T)]=0$ for every parameter value. Completeness forces $h(T)=f(T)$ almost surely. Conditional Jensen's inequality now gives
$$
\E_\theta[f(T)^2]=\E_\theta[h(T)^2]\le \E_\theta[g(U)^2]\le \E_\theta[f(T)^2].
$$
Equality in the last conditional-variance inequality forces $f(T)=g(U)$ almost surely. Apply this to indicators from a countable generating class of the statistic's standard Borel value space. Every such indicator is a function of $U$, so $T$ is measurable with respect to $U$, up to null sets. This is minimal sufficiency. The same total-variance identity underlies the Rao–Blackwell proof.{{cite:siegrist2022_sufficient_complete}} (§7.6, Rao–Blackwell theorem and its conditional-variance proof)
:::
:::

For binomial counts, allowing the success probability to range over an interval supplies completeness. Restricting the parameter to a few isolated values can remove that property. Completeness is therefore more than a fact about the numerical values a statistic can take.{{cite:dasgupta2011_exponential_family}} (§18.4, Ex. 18.16 and Thm. 18.8, pp. 511–512)

## Worked example
Let $X_1,X_2,X_3$ be independent Bernoulli$(p)$ variables and $T=X_1+X_2+X_3$. Conditional on $T=t$, all locations of the $t$ successes are equally likely. The chance that both the first and second positions succeed is
$$
\E(X_1X_2\mid T=t)=\frac{t(t-1)}{3\cdot2}.
$$
Consequently $\delta(T)=T(T-1)/6$ is unbiased for $p^2$. At $T=2$ it equals $1/3$; at $T=3$ it equals $1$. Since $T$ is complete and sufficient for $0<p<1$, this is the unique UMVU estimator.{{cite:siegrist2022_sufficient_complete}} (§7.6, Bernoulli-distribution application){{cite:dasgupta2011_exponential_family}} (§18.4, Ex. 18.17, p. 512)

At $p=1/2$, $\operatorname{Var}(X_1X_2)=3/16$, whereas $\operatorname{Var}\{\delta(T)\}=5/48$. The latter is smaller by $1/12$. This calculation concerns repeated samples, not the precision of a particular observed value of $T$.

**Your turn.** Find $\E\{T(T-1)\}$ and use it to verify unbiasedness without conditioning.

::: {.callout-tip collapse="true" title="Answer"}
There are six ordered pairs of distinct trials. Each pair succeeds with probability $p^2$, so $\E\{T(T-1)\}=6p^2$ and $\E\{T(T-1)/6\}=p^2$.
:::

## Check yourself

### A probability of two successes {#self-check-exr-completeness-binomial}

[Practice question](../questions/exr-completeness-binomial.qmd)

In three independent Bernoulli trials let T be the success count. Show that h(T)=T(T-1)/6 is unbiased for p², and evaluate it at T=2. Why is this function unique among unbiased functions of T when p ranges over (0,1)?

::: {.callout-tip collapse="true" title="Answer"}
There are six ordered pairs of distinct trials. Each pair succeeds with probability p², so E[T(T-1)/6]=p². At T=2 the estimate is 2/6=1/3. If another function of T were unbiased for p², its difference from h would have expectation zero for every p. The binomial count is complete on (0,1), so the difference is zero almost surely.
:::

### Conditioning an estimator {#self-check-ex-inf-rao-blackwell-variance}

[Practice question](../questions/ex-inf-rao-blackwell-variance.qmd)

Let $U$ be unbiased for $\theta$ and let $T$ be sufficient. In one sentence each, say why $W(T)=\mathbb{E}(U\mid T)$ is a statistic, why it is unbiased, and why $\operatorname{Var} W\le\operatorname{Var} U$.

::: {.callout-tip collapse="true" title="Answer"}
$W(T)$ is a statistic because sufficiency makes the conditional distribution of the sample given $T$ free of $\theta$, so the conditional expectation does not depend on $\theta$. It is unbiased because $\mathbb{E}\{W(T)\}=\mathbb{E}(U)=\theta$ by the tower property. Its variance is smaller because $\operatorname{Var}(U)=\operatorname{Var}\{W(T)\}+\mathbb{E}\{\operatorname{Var}(U\mid T)\}$ and the second term is nonnegative.
:::
