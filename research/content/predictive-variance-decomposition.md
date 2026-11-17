## Motivating example
Two candidate models can predict the same average response while disagreeing about where that response lies. Suppose one predicts a mean near zero and the other a mean near four. Averaging their conditional noise variances alone ignores the distance between those means. The predictive-variance decomposition accounts for that additional spread by separating uncertainty within conditional distributions from variation between their means. It is a variance identity for mixtures, including posterior predictive mixtures.{{cite:downey2020_thinkbayes2}} (Chapter 7, “Mixture” and “General Mixtures”)

## Statement

**Condition on the observed data throughout.**
For a future response $Y_*$ and parameter $\theta$, define $m(\theta,D)=E(Y_*\mid\theta,D)$ and $v(\theta,D)=\operatorname{Var}(Y_*\mid\theta,D)$. If $E(Y_*^2\mid D)<\infty$, then
$$\operatorname{Var}(Y_*\mid D)=E\{v(\theta,D)\mid D\}+\operatorname{Var}\{m(\theta,D)\mid D\}.$$
Conditional independence of $Y_*$ and $D$ given $\theta$ permits the shorter notation $m(\theta)$ and $v(\theta)$. The identity itself does not require that simplification: it remains true when the conditional mean and variance depend explicitly on the data. Both summands are nonnegative, and they refer to the same posterior distribution of $\theta$.{{cite:goodfellow_bengio_courville2016}} (§3.9, expectation, variance and covariance)

The first term averages the remaining variation of a response when the parameter is given. The second measures posterior variation in its conditional mean. These are mathematical definitions; the labels “noise” and “parameter uncertainty” are most useful when the model's conditioning structure makes that interpretation appropriate. Mixture components can also represent latent groups, model choices or unobserved environments.{{cite:downey2020_thinkbayes2}} (Chapter 7, “General Mixtures”)

## Proof
Set $\bar m=E(Y_*\mid D)=E\{m(\theta,D)\mid D\}$. Then
$$Y_*-\bar m=\{Y_*-m(\theta,D)\}+\{m(\theta,D)-\bar m\}.$$
Square this identity and take conditional expectation given $D$. Conditioning the cross term additionally on $\theta$ makes it zero, since $E\{Y_*-m(\theta,D)\mid\theta,D\}=0$. The first squared term averages the conditional variance and the second is the variance of the conditional mean. Finite second moments justify these expectations. The same calculation for vectors replaces squared deviations with outer products and gives the covariance-matrix version.

## Worked example
### Within-component and between-component spread
Let the posterior give probability $3/4$ to a conditional distribution with mean 0 and variance 1, and probability $1/4$ to one with mean 4 and variance 9. The predictive mean is $1$. The mean conditional variance is $(3/4)1+(1/4)9=3$. The variance of the conditional means is $(3/4)(0-1)^2+(1/4)(4-1)^2=3$. Hence the predictive variance is $6$, with equal contributions from the two sources.

A direct second-moment calculation agrees: $E(Y_*^2\mid D)=(3/4)(1+0^2)+(1/4)(9+4^2)=7$, and subtracting the squared predictive mean gives $7-1=6$. Choosing the most probable component alone gives variance 1, which discards both the second component's larger conditional variance and uncertainty about the mean.

**Your turn.** Suppose both components have mean 2 but keep their probabilities and variances. What is the predictive variance?

::: {.callout-tip collapse="true" title="Answer"}
The between-mean contribution is zero. The predictive variance is the weighted mean conditional variance, 3.
:::

## Statistical use — Normal forecasts make the distinction transparent
If $Y_*\mid\mu,D\sim N(\mu,\sigma^2)$ with known $\sigma^2$ and $\mu\mid D\sim N(m_n,v_n)$, the predictive variance is $\sigma^2+v_n$. The predictive law is normal because it is the convolution of independent normal parameter uncertainty and observation noise. A coefficient posterior variance tends to shrink as information grows; the noise term remains even when the mean becomes accurately known.{{cite:gelman_bda2013}} (§2.5, p. 41, posterior predictive distribution)

For a new linear-regression input $x_*$, a Gaussian coefficient posterior with covariance $V$ contributes $x_*^TVx_*$ to predictive variance, while an independent observation error contributes its own variance. This gives a direct geometric interpretation of uncertainty about a fitted mean: changing $x_*$ changes the coefficient directions used in the forecast.{{cite:rasmussen_williams2006}} (§2.1, posterior predictive distribution)

## Common misconceptions — Plug-in calculations need a qualification
The omitted between-mean term is nonnegative. However, an arbitrary plug-in variance $v(\widehat\theta,D)$ need not equal the mean conditional variance $E\{v(\theta,D)\mid D\}$. Therefore it is too strong to claim that every plug-in variance is necessarily smaller than the full predictive variance. With a constant conditional variance, dropping parameter uncertainty does give a downward error exactly equal to the between-mean term. With a varying conditional variance, both changes must be considered.{{cite:goodfellow_bengio_courville2016}} (§3.9, variance as a second-moment calculation)

The identity also concerns variance, rather than the shape of an interval. A mixture can be skewed or multimodal even when its mean and variance are easy to compute. A normal interval based only on those two moments need not have the requested predictive probability. Computing predictive quantiles from the mixture distribution avoids assuming a shape that the variance identity does not provide.{{cite:downey2020_thinkbayes2}} (Chapter 7, “Mixture” and cumulative distributions)
