## Motivating example
A factory wants the mean diameter of its parts, but the measurement variability is also unknown. Variance is a nuisance parameter for that mean question because it affects the sampling distribution without being the quantity of primary interest. It cannot simply be ignored: an interval based on a guessed variance has a different justification from one that estimates it. The same variance becomes a target parameter if the factory instead asks about manufacturing consistency. (The One Sample Model)

## Intuition — A role in the question, not a defect of the parameter
Write a model parameter as $(\psi,\lambda)$, with target $\psi$ and nuisance parameter $\lambda$. Profiling maximizes $L(\psi,\lambda)$ over $\lambda$ for each fixed $\psi$. Conditioning may remove nuisance dependence from a sampling distribution, while a pivot may cancel it from a statistic's distribution. Bayesian marginalization instead integrates over a specified prior or posterior distribution. Maximizing and integrating generally give different functions, and neither can be substituted for the other without changing the method.{{cite:dodge2008}} (pp. 334–335, normal maximum likelihood example)

## Properties — Profiling a normal likelihood
For iid $N(\mu,\sigma^2)$ observations, fix a candidate $\mu$ and let $R(\mu)=\sum_i(x_i-\mu)^2$. If $R(\mu)>0$, maximizing in $\sigma^2>0$ gives $\widehat\sigma^2(\mu)=R(\mu)/n$ by differentiating $-n\log(\sigma^2)/2-R(\mu)/(2\sigma^2)$. Substitution gives profile likelihood proportional to $R(\mu)^{-n/2}$. Since
$$R(\mu)=\sum_i(x_i-\overline x)^2+n(\overline x-\mu)^2,$$
the profile is maximized at $\overline x$ when the sample has positive scatter. If the observations are all identical, shrinking the variance at that common mean makes the unrestricted likelihood unbounded.{{cite:dodge2008}} (pp. 334–335, normal maximum likelihood example)

Under exact normal sampling, $Z=\sqrt n(\overline X-\mu)/\sigma$ is standard normal, $V=(n-1)s^2/\sigma^2$ is chi-squared with $n-1$ degrees of freedom, and they are independent. Thus $Z/\sqrt{V/(n-1)}=(\overline X-\mu)/(s/\sqrt n)$ has a $t_{n-1}$ distribution free of both unknown parameters. The pivot removes the nuisance from its distribution, while still using an estimate of its scale. (The One Sample Model, The Sample Variance; The $T$ Variable){{cite:dodge2008}} (pp. 77–78, normal-variance chi-squared statistic)

## Worked example — Profile and pivot for the same sample
For $x=(2,4,6)$, $\overline x=4$, centered scatter is eight and $s^2=4$. The profiled variance is $8/3$ at $\mu=4$ and $11/3$ at $\mu=5$. The profile likelihood ratio for five versus four is $(8/11)^{3/2}\approx0.620220$. A two-sided 95% $t$ interval uses $t_{2;0.975}\approx4.302653$ and standard error $2/\sqrt3$, giving $( -0.968275,8.968275)$. The wide interval reflects the uncertainty in estimating variability from three observations.

**Your turn.** For a normal sample of size $16$ with $\overline x=10$ and $s=4$, write the 95% interval using $t_{15;0.975}=2.131450$.

::: {.callout-tip collapse="true" title="Answer"}
The standard error is $4/4=1$, so the interval is $10\pm2.131450=(7.868550,12.131450)$.
:::

## Statistical use — Information after fitting nuisance coordinates
Partition a positive definite information matrix as
$$I=\begin{pmatrix}a&b^\top\\b&C\end{pmatrix}.$$
Solving $Iz=e_1$ gives the first inverse entry $(I^{-1})_{11}=1/(a-b^\top C^{-1}b)$. Since $C\succ0$, the subtracted quadratic form is nonnegative, so this entry is at least $1/a$, the bound with nuisance coordinates fixed. Equality holds when $b=0$. This is a bound comparison under regularity assumptions, rather than a universal statement that every realized interval must widen. In the normal mean–variance model, expected cross-information is zero, even though small-sample $t$ calibration still differs from a known-variance normal interval.{{cite:wuthrich_merz2022_glm}} (§5.1.4, Fisher information and nuisance dispersion) (The One Sample Model, The Sample Variance)

## Interpretation — The same sample, two removals of $\sigma$
For $x=(2,4,6)$ the sample mean is $4$ and the centered sum of squares is $8$. The profiled variance at a candidate mean $\mu$ is $R(\mu)/n$, so it equals $8/3$ at $\mu=4$ and $11/3$ at $\mu=5$. The profile likelihood ratio of those two candidate means is $(8/11)^{3/2}\approx0.620220$. Profiling has removed $\sigma^2$ by maximising it. The $t$ interval removes $\sigma$ by cancellation in the pivot. With $s=2$ and $n=3$, the standard error is $2/\sqrt3$, and $t_{2;0.975}\approx4.302653$ produces the interval $(-0.968275,8.968275)$. The profile ratio and the $t$ interval are functions of the same three numbers and answer different questions: one compares two point values of $\mu$ after maximising the nuisance variance, and the other is a set of $\mu$ values whose pivot stays inside a Student quantile. (The One Sample Model, The Sample Variance; The $T$ Variable)

A larger sample shows the same split with a sharper scale. For $n=16$, $\overline x=10$ and $s=4$, the standard error is $1$ and the $95\%$ Student interval with quantile $2.131450$ is $(7.868550,12.131450)$. A known-variance interval that used $\sigma=4$ would replace $2.131450$ by a normal quantile near $1.96$ and would be shorter. The difference is the price of estimating the nuisance scale from $15$ residual degrees of freedom. If the scientific question is the variance itself, $\sigma^2$ is the target and $\mu$ is the nuisance. The chi-squared pivot $(n-1)s^2/\sigma^2$ then removes $\mu$, and the $t$ pivot is the wrong tool. The name nuisance records the role in the question.{{cite:dodge2008}} (pp. 77–78, unknown-mean normal sample) (The One Sample Model)

## Connections — One information calculation
Partition
$$I=\begin{pmatrix}4&2\\2&4\end{pmatrix}.$$
Here $a=4$, $b=2$ and $C=4$. The Schur complement is $4-2^2/4=3$, so the inverse entry for the target is $1/3$. With the second parameter known, the bound read from $a$ alone is $1/4$. Estimating the nuisance parameter multiplies the asymptotic variance bound by $4/3$ in this numerical matrix. The cross-information $2$ is what creates the gap. A diagonal information matrix has $b=0$ and the two bounds agree. In the normal mean-and-variance model the expected cross-information is zero, so this particular inflation is absent from the asymptotic calculation, while the exact $t$ interval is still wider than the known-$\sigma$ interval because $s$ is random in finite samples. The information bound compares asymptotic variances. It does not replace the Student quantile.{{cite:wuthrich_merz2022_glm}} (§5.1.4, Fisher information and nuisance dispersion) (The One Sample Model, The Sample Variance)

## Common misconceptions
A parameter is a nuisance only relative to a target. In a study of mean diameter, the variance is a nuisance. In a study of consistency, the same variance is the target and the mean is the nuisance. Fitting a profile likelihood for the variance and calling the result a profile for the mean swaps the question. The three-observation profile above is a function of $\mu$. A profile for $\sigma^2$ would maximise over $\mu$ first, which for a normal sample returns $\overline x$ and leaves a function of the centered sum of squares.{{cite:dodge2008}} (pp. 334–335, normal maximum likelihood example)

Plugging $\widehat\sigma$ into a normal quantile produces an interval, and that interval is not the Student interval unless the quantile is the Student quantile. For the sixteen-observation example the normal multiplier $1.96$ would give $(8.04,11.96)$ if $\sigma$ were replaced by $s=4$. The Student interval is $(7.868550,12.131450)$. Both use $s$. They use different reference distributions. The plug-in normal interval is a large-sample approximation. The $t$ interval is exact under independent normal sampling. Wide intervals from $n=3$ are the procedure working with two degrees of freedom, not a failure of the pivot to remove $\sigma$. (The One Sample Model, The Sample Variance; The $T$ Variable){{cite:dodge2008}} (pp. 106–107, confidence-interval construction and interpretation)
