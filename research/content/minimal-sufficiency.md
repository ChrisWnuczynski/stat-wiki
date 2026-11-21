## Lead context
A minimal sufficient statistic is the coarsest summary of the sample that still preserves every likelihood comparison the parameter can make.{{cite:dasgupta2011_exponential_family}} (§18.4.1, pp. 512–514)

## Motivating example
Three Poisson counts, $2$, $0$, and $5$, have the same sum as $1$, $3$, and $3$. For every rate $\lambda$ the likelihood ratio of these two samples is the constant $36/240=0.15$. A third sample, $4$, $0$, $0$, has sum $4$ rather than $7$, and its likelihood ratio against the first sample is $0.1\lambda^3$, which changes with $\lambda$. The sum separates the samples that the likelihood can separate, and it lumps together the samples that the likelihood cannot. That is minimal sufficiency for this model.

## Intuition
The whole sample is sufficient, because conditioning on every observation leaves nothing random. Sufficiency alone is not compression. A statistic $T$ is minimal sufficient when every other sufficient statistic can be coarsened down to $T$ without losing sufficiency. For a family whose support does not depend on the parameter, the likelihood-ratio test of that idea is practical: $p(\mathbf{x}\mid\theta)/p(\mathbf{y}\mid\theta)$ is free of $\theta$ for all $\theta$ exactly when $T(\mathbf{x})=T(\mathbf{y})$.{{cite:dasgupta2011_exponential_family}} (§18.4.1, pp. 512–514)

## Definition
The ratio criterion is the one already displayed for a dominated family with $\theta$-free support. Two samples are assigned the same value of a minimal sufficient statistic when their likelihood ratio does not depend on $\theta$. Any sufficient statistic is a function of the data that preserves those distinctions, and the minimal one preserves no further distinctions.{{cite:dasgupta2011_exponential_family}} (§18.4.1, pp. 512–514)

For iid $\mathrm{N}(\mu,1)$ observations the ratio of densities is
$$
\exp\Bigl(-\frac{\sum x_i^2-\sum y_i^2}{2}+\mu\bigl(\sum x_i-\sum y_i\bigr)\Bigr).
$$
The quadratic term does not involve $\mu$. The linear term is free of $\mu$ for every $\mu$ precisely when the sums agree. The sum, or the sample mean, is minimal sufficient for $\mu$.

## Interpretation — Same sum, different lists
For the Poisson samples $\mathbf{x}=(2,0,5)$ and $\mathbf{y}=(1,3,3)$,
$$
\frac{L(\mathbf{x}\mid\lambda)}{L(\mathbf{y}\mid\lambda)}=\frac{1!\,3!\,3!}{2!\,0!\,5!}=\frac{36}{240}=0.15
$$
for every $\lambda>0$. The factorials do not depend on $\lambda$, and the powers of $\lambda$ cancel because both sums equal $7$. Against $\mathbf{z}=(4,0,0)$,
$$
\frac{L(\mathbf{x}\mid\lambda)}{L(\mathbf{z}\mid\lambda)}=0.1\lambda^3,
$$
which is a different function at $\lambda=1$ and at $\lambda=2$: the values are $0.1$ and $0.8$. The sum is $7$ for $\mathbf{x}$ and $4$ for $\mathbf{z}$, so a minimal sufficient statistic must give them different values.

## Properties
A complete sufficient statistic is minimal sufficient. The converse is false.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose $T$ is sufficient and $S$ is minimal sufficient. Then $S=g(T)$ for some function $g$, by the definition of minimal sufficiency. In particular $S$ is a function of every sufficient statistic, which is the property just used.

For the Poisson ratio, the joint mass is $e^{-n\lambda}\lambda^{\sum x_i}/\prod x_i!$. Dividing two such masses, the exponential factors cancel and $\lambda^{\sum x_i-\sum y_i}$ is constant in $\lambda>0$ if and only if the exponents agree. The factorial ratio is then a positive constant. Thus the sum is constant on the pairs the ratio cannot separate, and it changes when the ratio depends on $\lambda$.

For the normal calculation, fix $\sigma=1$ and the samples $(1,3)$ and $(0,4)$. Both sums equal $4$, and
$$
\frac{L(1,3\mid\mu)}{L(0,4\mid\mu)}=\exp\bigl(-(10-16)/2\bigr)=\exp(3),
$$
which does not depend on $\mu$. Replacing $(0,4)$ by $(0,3)$ leaves a factor $\exp(\mu)$, which does.
:::
:::

## Statistical use — What may be thrown away
Once a minimal sufficient statistic is in hand, the rest of the sample is useless for inference about $\theta$ inside the model. For a normal mean with known variance, the individual deviations from the mean do not appear in the likelihood ratio. They remain useful for checking the normal model, which is a question outside the parametric family. Minimal sufficiency is a reduction for $\theta$, not a licence to discard diagnostics.

For a Poisson rate, the sum is the statistic the likelihood sees. The order of the counts is not. Two samples with the same sum and the same $n$ produce proportional likelihoods, so they produce the same maximum-likelihood estimate $n^{-1}\sum X_i$ and the same likelihood-ratio tests of a hypothesised rate.

## Worked example
Take the three Poisson samples above, with $n=3$.

The pair $\mathbf{x}=(2,0,5)$ and $\mathbf{y}=(1,3,3)$ has likelihood ratio $0.15$ at every $\lambda$. At $\lambda=1$ and at $\lambda=2$ that number does not move. The pair $\mathbf{x}$ and $\mathbf{z}=(4,0,0)$ has ratio $0.1\lambda^3$, equal to $0.1$ at $\lambda=1$ and $0.8$ at $\lambda=2$. The minimal sufficient statistic $\sum X_i$ equals $7$ for the first two samples and $4$ for the third.

For a uniform shift, let the observations be $0.2$, $0.9$, and $1.1$ from $\mathrm{Uniform}(\theta,\theta+1)$. The likelihood is positive only when $\theta\le 0.2$ and $\theta\ge 1.1-1$, that is when $\theta\in[0.1,0.2]$. The interval is a function of the minimum and the maximum. The range $1.1-0.2=0.9$ does not name the interval by itself: the sample $0.3$, $0.5$, $1.2$ has the same range and the different interval $[0.2,0.3]$.

**Your turn.** For $\mathrm{N}(\mu,1)$ data, compute the likelihood ratio of $(1,3)$ against $(2,2)$, and say whether the ratio depends on $\mu$.

::: {.callout-tip collapse="true" title="Answer"}
Both samples sum to $4$. The sums of squares are $1+9=10$ and $4+4=8$, so the ratio is $\exp(-(10-8)/2)=\exp(-1)$, about $0.3679$, with no $\mu$ left in the exponent. The two samples share the minimal sufficient statistic.
:::

## Common misconceptions
Minimal sufficiency is not the same as using a one-dimensional statistic. For $\mathrm{Uniform}(\theta,\theta+1)$ the pair $(\min,\max)$ is minimal sufficient and the range, which is one-dimensional, is ancillary. Compressing to the range loses the location of the window.

The whole sample is sufficient. Calling it minimal confuses "nothing was thrown away" with "nothing further can be thrown away". A sufficient statistic that still splits two samples with proportional likelihoods is not minimal.

A complete sufficient statistic is minimal. The converse fails for the uniform shift model: $(\min,\max)$ is minimal sufficient, and the range is an ancillary function of it, so the statistic is not complete.

## Assumptions and limits — When the ratio test does not apply
The ratio criterion used here assumes a dominated family whose support does not depend on $\theta$. A uniform law on $[0,\theta]$ has a support that moves with $\theta$. The density ratio is then not the right instrument, and the sample maximum carries the parameter in the support constraint rather than in a $\theta$-free ratio of the kind above.

If two parameter values give mutually singular distributions, a statistic can be sufficient for a trivial reason and still fail to be a useful reduction. The ratio criterion is a tool inside one dominated family, not a theorem about every statistical model.

Dependence across observations can make the sum insufficient. The Poisson argument factored because the joint mass was a product. A model with a common random effect does not factor in the same way, and the sum of the counts need not be minimal sufficient for the rate.

## Connections
A [sufficient statistic](sufficient-statistic.qmd) keeps the likelihood comparisons. Minimal sufficiency is the coarsest such reduction. A [complete statistic](complete-statistic.qmd) has no nonzero function of mean zero, and completeness implies minimal sufficiency. An ancillary statistic, such as the range in the uniform shift model, has a distribution free of $\theta$. The [likelihood function](likelihood-function.qmd) is the object the ratio criterion reads.

## History
The ratio criterion is the practical test of minimal sufficiency for dominated families whose support does not move with the parameter. The normal calculation shows why the sample sum is enough for a normal mean when the variance is known, and the uniform shift model shows why a minimal sufficient statistic need not be complete. Those two calculations are the ones carried out above.
