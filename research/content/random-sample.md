## Lead context
The independence and common distribution let a sample average have a predictable sampling distribution, which is why random samples underlie many estimates and tests. Whether actual observations meet those assumptions depends on how they were selected and measured.{{cite:siegrist2022_random_samples}} (§6.1, “Random Samples” and “Difficulties”)

## Motivating example
Suppose a laboratory tests a fresh battery from the same production process on each of four independent trials. The four lifetimes can be modelled as a random sample if each trial has the same lifetime distribution. If four batteries from one batch share a batch effect, the iid assumption fails and a model with a batch effect is needed.{{cite:siegrist2022_random_samples}} (§6.1, “The Basic Statistical Model” and “Random Samples”)

## Definition
Write $X_1,\ldots,X_n$ for the random measurements before observation, $x_1,\ldots,x_n$ for their realised values, and $F$ for a common probability distribution. A random sample of size $n$ means that $X_1,\ldots,X_n$ are *independent and identically distributed* (iid) with law $F$. This is a joint probability model for the measurements. [Simple random sampling](simple-random-sample.qmd) instead describes a selection design in which every possible group of a given size has the same chance of selection.{{cite:siegrist2022_random_samples}} (§6.1, “Random Samples”){{cite:statistics_canada2003_survey}} (§6.2.2, pp. 93–94)

For measurable sets $A_1,\ldots,A_n$, independence and the common law give
$$
\Pr(X_1\in A_1,\ldots,X_n\in A_n)=\prod_{i=1}^n\Pr(X_i\in A_i)=\prod_{i=1}^n F(A_i).
$$
Here $A_i$ is a set of possible values for observation $i$, and $F(A_i)$ is its probability under the common law. If $F$ has a density or mass function $f$, the joint density or mass at realised values $x_1,\ldots,x_n$ is $\prod_{i=1}^n f(x_i)$. The product form is what makes the sample likelihood tractable.{{cite:siegrist2022_random_samples}} (§6.1, “Random Samples”){{cite:fisher1922}} (§2, pp. 312–313)

## Interpretation
The identical-distribution requirement makes the observations comparable under one law; independence describes their joint behaviour. Equal marginal distributions alone do not imply independence. For example, if $X_2=X_1$, then both variables have the same law but the second observation supplies no independent replication. Conversely, independent measurements with different means are not an iid random sample from a single $F$, although they can form a valid regression dataset under a model that allows those differences.{{cite:siegrist2022_random_samples}} (§6.1, “Random Samples”)

An iid model is a statement about repeated sampling before the values are known. Once $x_1,\ldots,x_n$ have been observed, the numbers are fixed; the sample mean $\bar x$ describes those numbers, while the random variable $\bar X$ describes how the same calculation would vary over repetitions. This distinction supports standard errors, confidence intervals and hypothesis tests.{{cite:siegrist2022_random_samples}} (§6.1, “Statistics” and “Descriptive and Inferential Statistics”){{cite:siegrist2022_normals}} (§6.8, “The One Sample Model”)

## Properties
For an iid sample with finite mean $\mu=\mathbb E X_i$ and finite variance $\sigma^2=\operatorname{Var}(X_i)$, the sample mean $\bar X=n^{-1}\sum_iX_i$ has mean $\mu$ and variance $\sigma^2/n$. The sample variance $s^2=(n-1)^{-1}\sum_i(X_i-\bar X)^2$, defined for $n\ge2$, has mean $\sigma^2$. Thus averaging reduces variance under independent replication, and dividing the squared deviations by $n-1$ removes the bias in variance estimation.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

When the common law is normal, $\bar X$ is exactly normal, $(n-1)s^2/\sigma^2$ has a chi-squared distribution with $n-1$ degrees of freedom, and $\bar X$ is independent of $s^2$. These stronger statements support exact normal-sample intervals and tests. The general moment identities above require finite variance; the exact distribution and independence results additionally require normality.{{cite:siegrist2022_normals}} (§6.8, “The One Sample Model,” “The Sample Mean,” “The Sample Variance”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Independence gives the joint probability product in the Definition. For the mean, linearity yields $\mathbb E\bar X=n^{-1}\sum_i\mu=\mu$. Independence makes the cross-covariances zero, so $\operatorname{Var}(\bar X)=n^{-2}\sum_i\sigma^2=\sigma^2/n$. The identity $\sum_i(X_i-\bar X)^2=\sum_i(X_i-\mu)^2-n(\bar X-\mu)^2$ gives expectation $n\sigma^2-n(\sigma^2/n)=(n-1)\sigma^2$, proving $\mathbb E s^2=\sigma^2$.{{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

For the normal statements, standardise $Z_i=(X_i-\mu)/\sigma$. An orthogonal change of coordinates whose first row is $(1/\sqrt n,\ldots,1/\sqrt n)$ gives independent standard-normal coordinates $W_1,\ldots,W_n$. Its first coordinate is $W_1=\sqrt n(\bar X-\mu)/\sigma$. The remaining coordinates span the deviations from $\bar X$, so $\sum_{j=2}^nW_j^2=\sum_i(X_i-\bar X)^2/\sigma^2=(n-1)s^2/\sigma^2$. The sum of $n-1$ independent squared standard normals is $\chi^2_{n-1}$ and is independent of $W_1$; hence it is independent of $\bar X$. Rescaling $W_1$ gives $\bar X\sim\operatorname N(\mu,\sigma^2/n)$.{{cite:siegrist2022_normals}} (§6.8, “The One Sample Model,” “The Sample Mean,” “The Sample Variance”)
:::
:::

## Statistical use
Check the units of sampling before treating measurements as independent replicates. If several observations come from one person, household, lake or manufacturing batch, their shared source may affect uncertainty. When observations have distinct covariates, a regression model can use independent responses with different conditional means. In either setting, the sampling model determines which likelihood and standard error are appropriate.{{cite:siegrist2022_random_samples}} (§6.1, “Difficulties” and “Random Samples”){{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–373)

For an iid sample, calculate a statistic such as $\bar X$ or $s^2$ from the observed values and use its sampling distribution under the proposed $F$ to quantify uncertainty. The sample mean's standard error is $\sigma/\sqrt n$ when $\sigma$ is known; in practice $s/\sqrt n$ is often used when it is unknown. Normal sampling yields the exact $t$ pivot for the mean, while large-sample approximations require their own conditions.{{cite:siegrist2022_normals}} (§6.8, “The One Sample Model,” “The Student Statistic”)

## Worked example
Let four independent Bernoulli observations have success probability $p=1/4$. One possible realised sample is $(x_1,x_2,x_3,x_4)=(1,0,1,0)$. Its observed mean is $\bar x=2/4=1/2$, and its sample variance is $s^2=\{2(1-1/2)^2+2(0-1/2)^2\}/3=1/3$. The probability of this *ordered* sequence is $(1/4)^2(3/4)^2=9/256$; the probability of any two successes in four trials is $\binom42(9/256)=27/128$. The sample mean differs from the population mean $p=1/4$ without contradicting the sampling model.{{cite:siegrist2022_random_samples}} (§6.1, “Random Samples”)

Before the four outcomes are seen, $\mathbb E\bar X=p=1/4$ and $\operatorname{Var}(\bar X)=p(1-p)/4=3/64$. The realised $\bar x=1/2$ is one draw from that sampling distribution. If the four recorded values were copies of the same Bernoulli outcome instead, their means would still be $1/4$ but $\operatorname{Var}(\bar X)$ would be $3/16$; the independent-sample variance formula would be wrong.{{cite:siegrist2022_random_samples}} (§6.1, “Random Samples”){{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”)

**Your turn.** Under the four independent Bernoulli$(1/4)$ draws in the example, what is the probability that all four outcomes are zero? What is $\mathbb E\bar X$?

::: {.callout-tip collapse="true" title="Answer"}
Each draw is zero with probability $3/4$. Independence gives $(3/4)^4=81/256$ for four zeros. The sample mean still has expectation $1/4$ over repeated samples.
:::

## Common misconceptions
The iid definition describes a joint law for measurements; simple random sampling describes an equal-probability selection design for distinct units. That survey design may make inclusion probabilities equal while measurements remain dependent through selection or shared circumstances. The properties of $\bar X$ and $s^2$ on this page rely on the iid model; apply design-specific or dependence-aware formulas when the data collection differs.{{cite:siegrist2022_random_samples}} (§6.1, “Random Samples” and “Difficulties”){{cite:statistics_canada2003_survey}} (§6.2.2, pp. 93–94)

## Connections
[Simple random sample](simple-random-sample.qmd) describes an equal-probability selection design for a fixed-size group; the iid definition here describes the resulting variables' joint law. The [sample mean and variance](moments-of-the-sample-mean-and-variance.qmd) use the iid assumption for their moment formulas. The [normal sample theorem](normal-sample-theorem.qmd) adds normality to obtain exact distributions and independence. A [likelihood function](likelihood-function.qmd) multiplies individual densities or masses under the iid model, while [paired samples](paired-samples.qmd) require treating each pair as one observation when measurements within pairs are dependent.{{cite:statistics_canada2003_survey}} (§6.2.2, pp. 93–94){{cite:siegrist2022_random_samples}} (§6.1, “Random Samples”){{cite:siegrist2022_normals}} (§6.8, “The One Sample Model”)

## History
In his 1922 paper on theoretical statistics, Ronald Fisher described inference from observations interpreted as a sample of a hypothetical population. He stressed that the relevant question is which population and set of conditions the sample represents. His treatment connected that sampling interpretation to statistics calculated from the observations and to likelihood-based estimation.{{cite:fisher1922}} (§§2–3, pp. 312–316)

Modern accounts distinguish the sampling rule from the probability model for measurements. Siegrist's random-sample chapter states the iid model explicitly and then derives separate behaviour for the sample mean, variance and normal-sample statistics. These results show how assumptions about replication become formulas used for estimation and testing.{{cite:siegrist2022_random_samples}} (§6.1, “Random Samples”){{cite:siegrist2022_sample_variance}} (§6.5, “The Standard Sample Variance”){{cite:siegrist2022_normals}} (§6.8, “The One Sample Model”)
