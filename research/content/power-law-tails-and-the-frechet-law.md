## Motivating example
A maximum over many independent losses can grow far faster than a typical loss. Under an exact power-law upper tail, multiplying the sample size multiplies the scale of the maximum by a power of that increase. The Fréchet limit describes the remaining randomness after this scaling.{{cite:dasgupta2011_graduate_probability}} (§1.29.9, Thm. 1.101, p. 179)

## Definition — A positive heavy-tailed maximum
For the Pareto tail $P(X>x)=x^{-\alpha}$, $x\ge1$, and independent copies $X_1,\ldots,X_n$, let $M_n=\max_iX_i$. Its distribution is $P(M_n\le x)=F(x)^n$. Set $a_n=n^{1/\alpha}$. For every $z>0$ and sufficiently large $n$,
$$
P(M_n/a_n\le z)=\left(1-\frac{z^{-\alpha}}n\right)^n\longrightarrow \Phi_\alpha(z)=e^{-z^{-\alpha}}.
$$
The limiting CDF is zero for $z\le0$. This is a Fréchet law in a positive-scale parameterisation.{{cite:dasgupta2011_graduate_probability}} (§1.29.9, Thm. 1.101, pp. 178–179){{cite:siegrist2022_pareto}} (“Distribution Functions”, Pareto upper tail)

## Properties — A direct limit and a moment threshold
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Independence gives the $n$th power of the marginal CDF. Substitute $a_nz$ and take logarithms: $n\log(1-z^{-\alpha}/n)\to-z^{-\alpha}$. Exponentiating proves convergence at every positive $z$. At nonpositive $z$, both the finite-sample maximum probability and the limiting CDF are zero.{{cite:dasgupta2011_graduate_probability}} (§1.29.9, polynomial-tail extremes)
:::
:::

The upper tail of the limit satisfies $1-\Phi_\alpha(z)\sim z^{-\alpha}$. Hence its $r$th positive moment is finite exactly when $r<\alpha$. In particular the mean requires $\alpha>1$, while the variance requires $\alpha>2$. These thresholds follow by integrating $rz^{r-1}P(Z>z)$ over the positive half-line.{{cite:dasgupta2011_graduate_probability}} (Thm. 1.29, tail-integral moment formula){{cite:siegrist2022_pareto}} (“Moments”)

## Worked example
For $\alpha=2$ and $n=10000$, the scale is $a_n=100$. The limiting median is $(\log2)^{-1/2}$, so the approximate median maximum is $120.112241$. Solving the finite-sample CDF exactly gives
$$
\operatorname{median}(M_n)=\left(1-2^{-1/n}\right)^{-1/2}=120.114322.
$$
The approximation differs by about $0.002081$. A single observation has median $\sqrt2=1.414214$, showing the contrast between a typical observation and a sample maximum.{{cite:dasgupta2011_graduate_probability}} (§1.29.9, scaling of polynomial-tail extremes){{cite:siegrist2022_pareto}} (“Quantile Function”)

At $z=2$ and $n=100$, the exact scaled CDF is $(1-0.25/100)^{100}=0.778557$, while its limit is $e^{-0.25}=0.778801$. Increasing $n$ improves this particular approximation. General slowly varying tail factors require an appropriate quantile scale rather than an automatic use of $n^{1/\alpha}$.

**Your turn.** For $\alpha=2$, how does the maximum scale change when the sample size is multiplied by $4$?

::: {.callout-tip collapse="true" title="Answer"}
It is multiplied by $4^{1/2}=2$. This concerns the scale of the maximum, not the value of every realised maximum.
:::

## Check yourself

### A larger sample {#self-check-ex-sp-pareto-factor}

[Practice question](../questions/ex-sp-pareto-factor.qmd)

A Pareto upper tail has exponent $\alpha=2$. By what factor does the scale of the typical maximum change when the sample size is multiplied by $4$?

::: {.callout-tip collapse="true" title="Answer"}
The Fréchet scale for exponent $\alpha=2$ is $n^{1/2}$. Replacing $n$ by $4n$ multiplies the scale by $\sqrt{4}=2$.
:::

### An exponential comparison {#self-check-ex-sp-gumbel-scale}

[Practice question](../questions/ex-sp-gumbel-scale.qmd)

For independent $\mathrm{Exp}(2)$ variables, give $a_n$ and $b_n$ that produce the Gumbel limit.

::: {.callout-tip collapse="true" title="Answer"}
For an exponential rate $\lambda$ the centring $(\log n)/\lambda$ and the scale $1/\lambda$ produce the Gumbel limit. Here $\lambda=2$, so $b_n=(\log n)/2$ and $a_n=1/2$.
:::
