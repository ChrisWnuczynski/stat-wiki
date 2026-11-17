## Motivating example
Two candidate models can predict the same average response while disagreeing about where that response lies. Suppose one predicts a mean near zero and the other a mean near four. Averaging their conditional noise variances alone ignores the distance between those means. The predictive-variance decomposition accounts for that additional spread by separating uncertainty within conditional distributions from variation between their means. It is a variance identity for mixtures, including posterior predictive mixtures.{{cite:downey2020_thinkbayes2}} (Chapter 7, “Mixture” and “General Mixtures”)

The same split appears when a future observation is drawn in two steps: first a parameter from its posterior, then a response from the sampling model at that parameter. A forecast that stops after the first step describes the parameter. A forecast that keeps both steps describes the new observation.{{cite:gelman_bda2013}} (Ch. 1, §1.3, eqs. 1.3–1.4; Ch. 3, §3.2)

## Statement

**Condition on the observed data throughout.**
For a future response $Y_*$ and parameter $\theta$, define $m(\theta,D)=E(Y_*\mid\theta,D)$ and $v(\theta,D)=\operatorname{Var}(Y_*\mid\theta,D)$. If $E(Y_*^2\mid D)<\infty$, then
$$\operatorname{Var}(Y_*\mid D)=E\{v(\theta,D)\mid D\}+\operatorname{Var}\{m(\theta,D)\mid D\}.$$
Conditional independence of $Y_*$ and $D$ given $\theta$ permits the shorter notation $m(\theta)$ and $v(\theta)$. The identity itself does not require that simplification: it remains true when the conditional mean and variance depend explicitly on the data. Both summands are nonnegative, and they refer to the same posterior distribution of $\theta$.{{cite:goodfellow_bengio_courville2016}} (§3.9, expectation, variance and covariance)

The first term averages the remaining variation of a response when the parameter is given. The second measures posterior variation in its conditional mean. These are mathematical definitions; the labels “noise” and “parameter uncertainty” are most useful when the model's conditioning structure makes that interpretation appropriate. Mixture components can also represent latent groups, model choices or unobserved environments.{{cite:downey2020_thinkbayes2}} (Chapter 7, “General Mixtures”)

## Intuition — Where a new observation can still move
Fix the observed data and imagine repeating the future draw. Sometimes the posterior selects a parameter whose conditional mean is high, and sometimes one whose conditional mean is low. That movement of the centre is the second term. Even after the centre is fixed, the sampling distribution still scatters observations around it. That scatter, averaged over the posterior, is the first term. Adding the two is the variance of the mixture.

A picture with two well-separated components makes the second term obvious: the mixture is wider than either component because probability sits in both places. A picture with one component makes the second term zero and leaves only the sampling variance. Real posteriors lie between those sketches. As the posterior of a location parameter concentrates, the between-mean term shrinks. The sampling term remains if a new observation still has its own noise.{{cite:gelman_bda2013}} (§2.5, p. 41, posterior predictive distribution)

## Proof
Set $\bar m=E(Y_*\mid D)=E\{m(\theta,D)\mid D\}$. Then
$$Y_*-\bar m=\{Y_*-m(\theta,D)\}+\{m(\theta,D)-\bar m\}.$$
Square this identity and take conditional expectation given $D$. Conditioning the cross term additionally on $\theta$ makes it zero, since $E\{Y_*-m(\theta,D)\mid\theta,D\}=0$. The first squared term averages the conditional variance and the second is the variance of the conditional mean. Finite second moments justify these expectations. The same calculation for vectors replaces squared deviations with outer products and gives the covariance-matrix version.

## Key results — Cancellation is a special case
The second term is always nonnegative, so the predictive variance is at least the posterior average of the conditional variance. An arbitrary plug-in variance $v(\widehat\theta,D)$ is not that average. It can sit above or below $E\{v(\theta,D)\mid D\}$, and therefore it need not sit below the full predictive variance.

One Bernoulli trial is a case in which two different shortcuts agree. If $Y_*\mid p$ is Bernoulli and $p$ has posterior mean $\mu$, then $Y_*$ is Bernoulli with success probability $\mu$, so its predictive variance is $\mu(1-\mu)$. The plug-in variance at $\mu$ equals that number. The decomposition still has two pieces: $E\{p(1-p)\mid D\}=\mu(1-\mu)-\operatorname{Var}(p\mid D)$ and $\operatorname{Var}(p\mid D)$. Their sum is $\mu(1-\mu)$. Using the plug-in variance happens to be correct for this one-trial law, while using only the average conditional variance would be too small by $\operatorname{Var}(p\mid D)$. A joint forecast of several trials that share one $p$ does not collapse in the same way, because the trials are dependent under the posterior predictive distribution.{{cite:gelman_bda2013}} (Ch. 1, §1.3, eqs. 1.3–1.4; Ch. 2, §2.1; Ch. 3, §3.2)

When the conditional variance does not depend on $\theta$, the first term equals that constant and the plug-in calculation that drops parameter uncertainty is short by exactly the second term. The normal mean with known observation variance is the standard example.

## Worked example
### Within-component and between-component spread
Let the posterior give probability $3/4$ to a conditional distribution with mean 0 and variance 1, and probability $1/4$ to one with mean 4 and variance 9. The predictive mean is $1$. The mean conditional variance is $(3/4)1+(1/4)9=3$. The variance of the conditional means is $(3/4)(0-1)^2+(1/4)(4-1)^2=3$. Hence the predictive variance is $6$, with equal contributions from the two sources.

A direct second-moment calculation agrees: $E(Y_*^2\mid D)=(3/4)(1+0^2)+(1/4)(9+4^2)=7$, and subtracting the squared predictive mean gives $7-1=6$. Choosing the most probable component alone gives variance 1, which discards both the second component's larger conditional variance and uncertainty about the mean.

### A beta posterior and one future trial
Suppose a success probability has posterior $\operatorname{Beta}(9,5)$. Its mean is $9/14$. The second moment is $E(p^2\mid D)=3/7$, so $\operatorname{Var}(p\mid D)=3/196$. The average Bernoulli variance is $E\{p(1-p)\mid D\}=3/14$. The plug-in variance at the posterior mean, and the predictive variance of one future Bernoulli trial, are both $45/196$. The gap $3/196$ is exactly the amount by which the average conditional variance lies below the full predictive variance. The equality of the plug-in and the full variance is the one-trial cancellation above; it is not a reason to drop $\operatorname{Var}(p\mid D)$ from a forecast of two trials that reuse the same $p$.

**Your turn.** Suppose both components in the two-point mixture have mean 2 but keep their probabilities and variances. What is the predictive variance?

::: {.callout-tip collapse="true" title="Answer"}
The between-mean contribution is zero. The predictive variance is the weighted mean conditional variance, 3.
:::

## Statistical use — Normal forecasts make the distinction transparent
If $Y_*\mid\mu,D\sim N(\mu,\sigma^2)$ with known $\sigma^2$ and $\mu\mid D\sim N(m_n,v_n)$, the predictive variance is $\sigma^2+v_n$. The predictive law is normal because it is the convolution of independent normal parameter uncertainty and observation noise. A coefficient posterior variance tends to shrink as information grows; the noise term remains even when the mean becomes accurately known.{{cite:gelman_bda2013}} (§2.5, p. 41, posterior predictive distribution)

For a numerical scale, take $\sigma^2=4$ and $v_n=1$. The variance of the latent mean is $1$, the predictive variance of a new measurement is $5$, and the predictive standard deviation is about $2.236068$. An interval for $\mu$ uses the smaller scale. An interval for the new measurement uses the larger one. Reporting the mean interval as a forecast of the next observation omits the observation noise.

For a new linear-regression input $x_*$, a Gaussian coefficient posterior with covariance $V$ contributes $x_*^TVx_*$ to predictive variance, while an independent observation error contributes its own variance. This gives a direct geometric interpretation of uncertainty about a fitted mean: changing $x_*$ changes the coefficient directions used in the forecast.{{cite:rasmussen_williams2006}} (§2.1, posterior predictive distribution)

## Generalizations — Vectors, groups and several future draws
For a random vector the same expansion uses outer products. The predictive covariance equals the posterior mean of the conditional covariance plus the covariance of the conditional mean vector. Each diagonal entry is an ordinary variance decomposition. Off-diagonal entries describe dependence created by a shared uncertain mean, even when the coordinates are conditionally uncorrelated given the parameter.

A hierarchical model adds a further layer. A new observation in an existing group is drawn given that group's effect, and the group's effect still has posterior uncertainty. A new group requires a draw of a new effect from the population distribution before the observation is drawn. Those two replication schemes have different conditional means and can have different predictive variances, even when they share a posterior for the population parameters. The identity applies to whichever conditional distribution the forecast actually uses.{{cite:gelman_bda2013}} (Ch. 1, §1.3, eqs. 1.3–1.4; Ch. 3, §3.2)

## Related concepts
The decomposition accounts for second moments. It does not determine quantiles. A two-point mixture with variance $6$ can be strongly skewed, and a normal interval built from its mean and variance need not have the probability the normal formula suggests. Posterior predictive draws, or an exact mixture calculation, produce probabilities for events such as $\{Y_*>5\}$ without that shape assumption.{{cite:downey2020_thinkbayes2}} (Chapter 7, “Mixture” and cumulative distributions)

A posterior interval for $\theta$ and a predictive interval for $Y_*$ answer different questions. The first covers the parameter under the posterior. The second covers an unobserved outcome and, when the decomposition applies, is inflated by both terms. Comparing their widths is meaningful only after the target of each interval has been named.

## Common misconceptions — Plug-in calculations need a qualification
The omitted between-mean term is nonnegative. However, an arbitrary plug-in variance $v(\widehat\theta,D)$ need not equal the mean conditional variance $E\{v(\theta,D)\mid D\}$. Therefore it is too strong to claim that every plug-in variance is necessarily smaller than the full predictive variance. With a constant conditional variance, dropping parameter uncertainty does give a downward error exactly equal to the between-mean term. With a varying conditional variance, both changes must be considered. The beta calculation shows a third pattern: for one Bernoulli trial the plug-in variance matches the full predictive variance, while the average conditional variance is the smaller number.{{cite:goodfellow_bengio_courville2016}} (§3.9, variance as a second-moment calculation)

The identity also concerns variance, rather than the shape of an interval. A mixture can be skewed or multimodal even when its mean and variance are easy to compute. A normal interval based only on those two moments need not have the requested predictive probability. Computing predictive quantiles from the mixture distribution avoids assuming a shape that the variance identity does not provide.{{cite:downey2020_thinkbayes2}} (Chapter 7, “Mixture” and cumulative distributions)

A finite predictive variance requires a finite second moment. A proper posterior predictive distribution can still have an infinite variance: a Student predictive law with two or fewer degrees of freedom is proper and has no finite variance. In that case the decomposition's hypothesis fails, and a variance comparison is the wrong summary. Quantiles of the predictive distribution remain available.{{cite:bernardo2005_reference}} (Example 23, equation 38, Student predictive distribution)
