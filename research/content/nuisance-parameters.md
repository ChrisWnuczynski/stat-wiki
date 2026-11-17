## Motivating example
A factory wants the mean diameter of its parts, but the measurement variability is also unknown. Variance is a nuisance parameter for that mean question because it affects the sampling distribution without being the quantity of primary interest. It cannot simply be ignored: an interval based on a guessed variance has a different justification from one that estimates it. The same variance becomes a target parameter if the factory instead asks about manufacturing consistency.{{cite:siegrist2022_normals}} (The One Sample Model)

## Intuition — A role in the question, not a defect of the parameter
Write a model parameter as $(\psi,\lambda)$, with target $\psi$ and nuisance parameter $\lambda$. Profiling maximizes $L(\psi,\lambda)$ over $\lambda$ for each fixed $\psi$. Conditioning may remove nuisance dependence from a sampling distribution, while a pivot may cancel it from a statistic's distribution. Bayesian marginalization instead integrates over a specified prior or posterior distribution. Maximizing and integrating generally give different functions, and neither can be substituted for the other without changing the method.{{cite:siegrist_mle2022}} (Extending the Method and the Invariance Property){{cite:openintro2019}} (§7.1, one-sample means)

## Properties — Profiling a normal likelihood
For iid $N(\mu,\sigma^2)$ observations, fix a candidate $\mu$ and let $R(\mu)=\sum_i(x_i-\mu)^2$. If $R(\mu)>0$, maximizing in $\sigma^2>0$ gives $\widehat\sigma^2(\mu)=R(\mu)/n$ by differentiating $-n\log(\sigma^2)/2-R(\mu)/(2\sigma^2)$. Substitution gives profile likelihood proportional to $R(\mu)^{-n/2}$. Since
$$R(\mu)=\sum_i(x_i-\overline x)^2+n(\overline x-\mu)^2,$$
the profile is maximized at $\overline x$ when the sample has positive scatter. If the observations are all identical, shrinking the variance at that common mean makes the unrestricted likelihood unbounded.{{cite:siegrist_mle2022}} (The Normal Distribution){{cite:dodge2008}} (pp. 334–335, normal maximum likelihood example)

Under exact normal sampling, $Z=\sqrt n(\overline X-\mu)/\sigma$ is standard normal, $V=(n-1)s^2/\sigma^2$ is chi-squared with $n-1$ degrees of freedom, and they are independent. Thus $Z/\sqrt{V/(n-1)}=(\overline X-\mu)/(s/\sqrt n)$ has a $t_{n-1}$ distribution free of both unknown parameters. The pivot removes the nuisance from its distribution, while still using an estimate of its scale.{{cite:siegrist2022_normals}} (The One Sample Model, The Sample Variance; The $T$ Variable){{cite:openintro2019}} (§7.1, t distribution)

## Worked example — Profile and pivot for the same sample
For $x=(2,4,6)$, $\overline x=4$, centered scatter is eight and $s^2=4$. The profiled variance is $8/3$ at $\mu=4$ and $11/3$ at $\mu=5$. The profile likelihood ratio for five versus four is $(8/11)^{3/2}\approx0.620220$. A two-sided 95% $t$ interval uses $t_{2;0.975}\approx4.302653$ and standard error $2/\sqrt3$, giving $( -0.968275,8.968275)$. The wide interval reflects the uncertainty in estimating variability from three observations.

**Your turn.** For a normal sample of size $16$ with $\overline x=10$ and $s=4$, write the 95% interval using $t_{15;0.975}=2.131450$.

::: {.callout-tip collapse="true" title="Answer"}
The standard error is $4/4=1$, so the interval is $10\pm2.131450=(7.868550,12.131450)$.
:::

## Statistical use — Information after fitting nuisance coordinates
Partition a positive definite information matrix as
$$I=\begin{pmatrix}a&b^\top\\b&C\end{pmatrix}.$$
Solving $Iz=e_1$ gives the first inverse entry $(I^{-1})_{11}=1/(a-b^\top C^{-1}b)$. Since $C\succ0$, the subtracted quadratic form is nonnegative, so this entry is at least $1/a$, the bound with nuisance coordinates fixed. Equality holds when $b=0$. This is a bound comparison under regularity assumptions, rather than a universal statement that every realized interval must widen. In the normal mean–variance model, expected cross-information is zero, even though small-sample $t$ calibration still differs from a known-variance normal interval.{{cite:wuthrich_merz2022_glm}} (§5.1.4, Fisher information and nuisance dispersion){{cite:siegrist2022_normals}} (The One Sample Model, The Sample Variance)
