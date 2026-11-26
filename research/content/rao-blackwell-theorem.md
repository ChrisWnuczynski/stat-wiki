## Motivating example
Eight independent binary observations all measure the same success probability. The first observation alone is unbiased, yet it ignores seven measurements. Conditioning that observation on the total number of successes recovers the sample proportion. Rao–Blackwell improvement formalises this removal of sampling noise while preserving unbiasedness.{{cite:siegrist2022_sufficient_complete}} (§ “Properties of Sufficient Statistics”, Rao–Blackwell theorem)

## Properties — The variance removed by conditioning
Write $W=\E_\theta(U\mid T)$, where $U$ has finite second moment and $T$ is sufficient. Sufficiency makes a common version of this conditional expectation a statistic: its defining conditional distribution does not require the unknown parameter. The tower property gives $\E_\theta W=\E_\theta U$.{{cite:siegrist2022_sufficient_complete}} (§ “Properties of Sufficient Statistics”, Rao–Blackwell theorem)

The improvement has an exact size. Put $R=U-W$. Since $\E(R\mid T)=0$, every square-integrable function of $T$ is orthogonal to $R$; in particular $\E\{R(W-\E U)\}=0$. Expanding the square therefore gives
$$
\operatorname{Var}_\theta U=\operatorname{Var}_\theta W+\E_\theta(R^2).
$$
Thus equality holds precisely when $U=W$ almost surely under the parameter value being considered. This is an orthogonal-projection argument in the space of square-integrable random variables.{{cite:durrett2019}} (§4.1, Thm. 4.1.15, p. 213)

The same expansion around an arbitrary target $g(\theta)$ proves
$$
\E_\theta\{U-g(\theta)\}^2=\E_\theta\{W-g(\theta)\}^2+\E_\theta(R^2).
$$
Consequently conditioning also improves squared-error risk for a biased estimator, provided the conditional expectation is computable as a parameter-free statistic. Unbiasedness identifies the usual variance comparison; it is not required for this squared-error identity.{{cite:durrett2019}} (§4.1, Thms. 4.1.13–4.1.15, pp. 212–213)

## Worked example — From one trial to eight
Let $X_i$ be independent Bernoulli variables with probability $p$, $U=X_1$, and $S=\sum_{i=1}^8X_i$. Conditional on $S=s$, exchangeability makes each coordinate equally likely to be one, so $\E(X_1\mid S=s)=s/8$. The improved estimator is $S/8$. At $p=0.3$, the variance falls from $0.21$ to $0.02625$, a factor of eight. For $S=3$ the estimate is $0.375$. The conditional-distribution calculation uses the Bernoulli model, rather than merely a convenient correlation between $S$ and $U$.{{cite:siegrist2022_sufficient_complete}} (§ “Sufficient Statistics”, Bernoulli trials)

**Your turn.** For four Bernoulli trials, improve $X_1X_2$ as an estimator of $p^2$. What is its value when the total is three?

::: {.callout-tip collapse="true" title="Answer"}
Conditional on $S=s$, there are $s(s-1)$ ordered successful pairs among $4\cdot3$ possible ordered pairs. The estimator is $S(S-1)/12$, which equals $1/2$ at $S=3$.
:::

## Connections — Sufficiency and uniqueness
A sufficient statistic permits the improvement, but does not by itself establish a uniformly minimum-variance estimator. Completeness supplies the additional uniqueness argument: two unbiased functions of a complete sufficient statistic differ by a function with expectation zero at every parameter, hence agree almost surely. An arbitrary residual after conditioning need not be ancillary; zero conditional mean is the property used in the variance proof.{{cite:siegrist2022_sufficient_complete}} (§ “Complete Statistics”)

## Check yourself

### A conditional count probability {#self-check-ex-inf-poisson-umvu}

[Practice question](../questions/ex-inf-poisson-umvu.qmd)

For four Poisson observations with total five, estimate $P(X_1=1)$ without bias.

::: {.callout-tip collapse="true" title="Answer"}
Conditionally $X_1\mid S=5$ is binomial with parameters $5,1/4$. Its probability at one is $5(1/4)(3/4)^4=405/1024=0.395508$. The plug-in estimate is $(5/4)e^{-5/4}=0.358131$.
:::

### An unbiased quadratic {#self-check-exr-completeness-binomial}

[Practice question](../questions/exr-completeness-binomial.qmd)

For three Bernoulli trials, find the unbiased function of their total estimating $p^2$.

::: {.callout-tip collapse="true" title="Answer"}
$\E\{T(T-1)\}=3\cdot2p^2$, so the estimator is $T(T-1)/6$. At $T=2$ it equals $1/3$. Completeness makes this unbiased function unique.
:::
