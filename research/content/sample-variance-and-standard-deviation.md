## Lead context
The sample variance and the sample standard deviation measure how far a list of numbers lies from its own mean.

## Motivating example
The observations \(2,4,4,8\) have mean \(4.5\). The squared deviations are \(6.25\), \(0.25\), \(0.25\) and \(12.25\), and they sum to \(19\). Thus \(s^2=19/3\) and \(s=\sqrt{19/3}=2.5166\) to four decimals. Dividing the same sum of squares by \(n=4\) instead gives \(4.75\), which is smaller, because the divisor is larger.

## Intuition — Average the squared deviations, then restore the units
Each observation contributes a deviation from the sample mean. Those deviations sum to zero, so they are not \(n\) free pieces of information. Dividing the sum of squared deviations by \(n-1\) rather than by \(n\) is what makes the sample variance an unbiased estimator of a finite population variance.{{cite:siegrist2022_sample_variance}} (§6.5, The Standard Sample Variance) The standard deviation is the square root of that variance, so it is back in the units of the observations. The square root of an unbiased estimator is not itself unbiased.

## Definition — Divisor \(n-1\)
For observations \(x_1,\ldots,x_n\) with mean \(\overline x\),
\[
s^2=\frac{1}{n-1}\sum_{i=1}^n(x_i-\overline x)^2,
\qquad
s=\sqrt{s^2}.
\]
{{cite:siegrist2022_sample_variance}} (§6.5, The Sample Variance){{cite:dodge2008}} (pp. 506–507, Standard Deviation) An equivalent computational form is
\[
s^2=\frac{1}{n-1}\Bigl(\sum_{i=1}^n x_i^2-n\overline x^2\Bigr).
\]
{{cite:dodge2008}} (p. 507, Standard Deviation) Gosset’s 1908 formula divided by \(n\) instead.{{cite:dodge2008}} (p. 506, Standard Deviation) That divisor-\(n\) quantity is \(n-1\) times \(s^2\), divided by \(n\), and it estimates the variance of the empirical distribution that puts mass \(1/n\) on each observation.{{cite:siegrist2022_sample_variance}} (§6.5, The Sample Variance)

## Properties — Unbiasedness, and a biased square root
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let \(X_1,\ldots,X_n\) be independent with mean \(\mu\) and variance \(\sigma^2\), and write \(M=\overline X\). Then \(\sum_i(X_i-M)^2=\sum_i X_i^2-n M^2\). Taking expectations and using \(\mathbb{E} M=\mu\) and \(\operatorname{Var}(M)=\sigma^2/n\),
\[
\mathbb{E}\sum_i(X_i-M)^2
=n(\sigma^2+\mu^2)-n\bigl(\sigma^2/n+\mu^2\bigr)
=(n-1)\sigma^2.
\]
Hence \(\mathbb{E} S^2=\sigma^2\) when \(S^2\) divides by \(n-1\). The square-root function is concave, so Jensen’s inequality gives \(\mathbb{E} S\le\sigma\), with strict inequality when \(S\) is non-degenerate.{{cite:siegrist2022_sample_variance}} (§6.5, The Standard Sample Variance)
:::
:::

## Worked example — Four numbers

**Your turn.** Add a fifth observation equal to \(4\), so the list is \(2,4,4,8,4\). Give the mean and the sample variance.

::: {.callout-tip collapse="true" title="Answer"}
The total is \(22\) and the mean is \(4.4\). The sum of squared deviations is \(19.2\), and the sample variance divides by \(4\), so \(s^2=4.8\).
:::

## Connections — Population variance and standard errors
The [variance](variance.qmd) of a random variable is the population quantity \(\mathbb{E}(X-\mathbb{E} X)^2\) that \(S^2\) estimates.{{cite:dodge2008}} (p. 506, Standard Deviation) An [unbiased estimator](unbiased-estimator.qmd) is what the divisor \(n-1\) purchases for \(S^2\), not for \(S\). The [standard error](standard-error.qmd) of a mean is an estimated standard deviation of that mean, often \(s/\sqrt{n}\), and it is not another name for \(s\).

## Check yourself
### The same sum of squares
A sample of size \(6\) has \(\sum_i(x_i-\overline x)^2=10\). Give \(s^2\) and the divisor-\(n\) mean square.

::: {.callout-tip collapse="true" title="Answer"}
\(s^2=10/5=2\). The divisor-\(n\) mean square is \(10/6=5/3\). The unbiased sample variance is the larger of the two.
:::

### Why the deviations are short one
Why do the deviations \(x_i-\overline x\) have only \(n-1\) free values?

::: {.callout-tip collapse="true" title="Answer"}
They sum to zero. Any \(n-1\) of them determine the last one, so the sum of squares is an average over \(n-1\) degrees of freedom when the divisor in \(s^2\) is \(n-1\).
:::
