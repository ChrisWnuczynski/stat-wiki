## Motivating example
A mean computed from a few observations is variable, and a variance computed after fitting that mean loses one degree of freedom. The expectation identities quantify both effects without assuming a normal population. They also explain why dividing by the sample size and dividing by one less than the sample size answer different estimation questions.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

## Statement
For an iid sample of size $n\ge2$ with mean $\mu$ and finite variance $\sigma^2$, define $\overline X=n^{-1}\sum_iX_i$ and $S^2=(n-1)^{-1}\sum_i(X_i-\overline X)^2$. Then
$$
E(\overline X)=\mu,\qquad \operatorname{Var}(\overline X)=\frac{\sigma^2}{n},\qquad E(S^2)=\sigma^2.
$$
Finite variance is sufficient for these statements. Normality is required for stronger distributional claims such as independence of the sample mean and sample variance in a normal sample.{{cite:grinstead_snell1997}} (§6.2, Thm. 6.9, p. 260; §6.3, Thms. 6.14–6.16, p. 272){{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

## Proof
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Linearity gives the mean identity. Independence makes the variance of $\sum X_i$ equal to $n\sigma^2$, and scaling by $1/n$ gives $\sigma^2/n$. Finally,
$$
\sum_i(X_i-\overline X)^2=\sum_i(X_i-\mu)^2-n(\overline X-\mu)^2.
$$
Taking expectations subtracts $\sigma^2$ from $n\sigma^2$, leaving $(n-1)\sigma^2$. Divide by $n-1$.{{cite:siegrist2022_sample_variance}} (§6.5, proof of unbiasedness)
:::
:::

## Key results — Bias and extra moments
The estimator using divisor $n$ is $V_n=((n-1)/n)S^2$, so its expectation is $((n-1)/n)\sigma^2$. The correction removes bias in estimating the variance; it does not make the sample standard deviation unbiased. A nonlinear square root does not preserve expectation.{{cite:siegrist2022_sample_variance}} (§6.5, sample standard deviation)

[]{#property-variance-of-sample-variance}

If the population fourth central moment $\mu_4$ is finite, the variance of the unbiased sample variance is
$$
\operatorname{Var}(S^2)=\frac1n\left(\mu_4-\frac{n-3}{n-1}\sigma^4\right).
$$
Thus $S^2$ can be unbiased while itself having infinite variance. The second-moment and fourth-moment assumptions do different work.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”, variance formula)

## Common misconceptions
Unbiasedness is a statement about the average over repeated samples, not about the sample in hand. $\E(S^2)=\sigma^2$ does not make any one computed $S^2$ close to $\sigma^2$: in the discrete example worked in this article, $\operatorname{Var}(S^2)=3/8$ at $n=2$ against a mean of $1/2$, so individual values scatter widely around the parameter they estimate. The same caution applies to $\overline X$: $\E(\overline X)=\mu$ locates the centre of its sampling distribution, while $\operatorname{Var}(\overline X)=\sigma^2/n$ measures how far a single sample mean typically falls from that centre.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

## Worked example
Let $X$ take $-1,0,1$ with probabilities $1/4,1/2,1/4$. Then $\mu=0$, $\sigma^2=1/2$, and $\mu_4=1/2$. With $n=2$, direct enumeration of the nine possible ordered sample pairs gives
$$
E(\overline X)=0,\quad\operatorname{Var}(\overline X)=1/4,\quad E(S^2)=1/2,\quad\operatorname{Var}(S^2)=3/8.
$$
The biased divisor-two variance has expectation $1/4$. This discrete population confirms that the unbiasedness calculation does not require a continuous or normal model.{{cite:siegrist2022_sample_variance}} (§6.5, sample-variance moment identities)

**Your turn.** At sample size $4$, what are $\operatorname{Var}(\overline X)$ and $E(V_4)$ for this population?

::: {.callout-tip collapse="true" title="Answer"}
They are $(1/2)/4=1/8$ and $(3/4)(1/2)=3/8$, respectively.
:::

## Related concepts
These moments are the inputs on which the normal-sample laws rest. The [sample variance and standard deviation](sample-variance-and-standard-deviation.qmd) are the statistics whose expectations are computed here. In the i.i.d. setting of this article, the identities $\E(\overline X)=\mu$, $\operatorname{Var}(\overline X)=\sigma^2/n$ and $\E(S^2)=\sigma^2$ require only a finite second moment; a finite $\operatorname{Var}(S^2)$ requires more, namely a finite fourth central moment $\mu_4$, as the variance formula above shows. The distributional statements add a sampling assumption: for an i.i.d. normal sample, the scaled variance $(n-1)S^2/\sigma^2$ follows the [chi-squared distribution](chi-squared-distribution.qmd) exactly, and the joint behaviour of $\overline X$ and the scatter is the [sampling law of the normal mean and scatter](sampling-law-of-the-normal-mean-and-scatter.qmd).{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)
