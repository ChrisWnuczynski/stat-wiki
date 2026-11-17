## Motivating example
Suppose independent measurements successively inform an unknown mean. Re-evaluating a posterior integral after every observation would be cumbersome. A normal likelihood with known variance and a normal prior instead requires only two running quantities: precision and precision-weighted mean. The normal family is closed under this update. That closure, rather than a general claim that Bayesian posteriors are normal, is the conjugacy result.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

Closure can hold conditionally inside a more complicated model while failing after other unknowns are integrated out. For example, a group's normal conditional update can be embedded in a hierarchy whose marginal posterior is a mixture of normals. Keeping track of what is conditioned on prevents that distinction from being lost.{{cite:gelman2006}} (§2.1, pp. 516–517)

## Statement
For independent observations $X_i\mid\mu\sim N(\mu,\sigma^2)$ with known positive $\sigma^2$ and prior $N(m_0,v_0)$, define $P_0=1/v_0$ and $h_0=m_0/v_0$. The update is
$$P_n=P_0+n/\sigma^2,\qquad h_n=h_0+\sum_ix_i/\sigma^2,$$
so the posterior is $N(h_n/P_n,1/P_n)$. The data contribution is the precision of the sample mean, $n/\sigma^2$, rather than the precision of one observation. This form also makes a sequential implementation explicit.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

When observations have different known variances $s_i^2$, the same argument replaces $n/\sigma^2$ by $\sum_i1/s_i^2$ and $\sum_ix_i/\sigma^2$ by $\sum_ix_i/s_i^2$. The observations still need conditional independence in this simple calculation. Correlated noise requires its covariance matrix in the quadratic likelihood.

## Proof
Multiply the normal likelihood and prior kernels. Their log product, up to terms independent of $\mu$, is
$$-\frac12\left[\left(\frac1{v_0}+\frac n{\sigma^2}\right)\mu^2-2\left(\frac{m_0}{v_0}+\frac{\sum_ix_i}{\sigma^2}\right)\mu\right].$$
Since $P_n>0$, completing the square writes it as $-P_n(\mu-h_n/P_n)^2/2$ plus a constant. Its integral is finite and equals a positive multiple of $\sqrt{2\pi/P_n}$, so normalization produces the claimed normal density. The same calculation with individual variances proves the heterogeneous-precision extension.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

## Key results — Equivalent information and order invariance
Write $n_0=\sigma^2/v_0$. Then the posterior mean is $(n_0m_0+n\overline x)/(n_0+n)$ and its variance is $\sigma^2/(n_0+n)$. The quantity $n_0$ is prior precision expressed in units of one observation's precision. It can be noninteger and is not a count of measurements secretly present in the dataset. Changing the observation variance changes this equivalent count even if the same prior is used.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

Updating in batches gives the same answer because both $P$ and $h$ receive additive increments. A posterior from one batch becomes the next batch's prior. This equivalence presumes that the batches use the same latent mean and the specified independent sampling model. Reusing the same observations as though they were a new batch would double-count their likelihood contribution.

## Worked example — Update together and sequentially
Let $\mu\sim N(0,4)$, let the known observation variance be four, and observe $8$ and $12$. The prior precision is $1/4$. The two observations add $1/2$ to precision and five to the precision-weighted mean. Thus $P_2=3/4$, $h_2=5$, the posterior mean is $20/3=6.666667$ and variance is $4/3=1.333333$. A central 95% credible interval is $(4.403495,8.929838)$. The interval uses posterior normal quantiles.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

Sequentially, observing eight first gives precision $1/2$, weighted mean two and hence posterior $N(4,2)$. Observing twelve adds $1/4$ to precision and three to weighted mean. The result is again $N(20/3,4/3)$. Here the prior equivalent sample size is one: its mean zero receives the same precision weight as each individual observation.

**Your turn.** Starting from that final posterior, observe one additional value of ten with the same known variance. Find the new posterior.

::: {.callout-tip collapse="true" title="Answer"}
Precision rises from $3/4$ to one, and the precision-weighted mean rises from five to $15/2$. The posterior is $N(7.5,1)$.
:::

## Common misconceptions — A diffuse prior and an unknown variance differ
For a fixed nonempty sample, taking $v_0\to\infty$ makes the posterior mean approach $\overline x$ and variance approach $\sigma^2/n$. The limiting prior density is improper, so the calculation describes a posterior limit, not a proper normal distribution with infinite variance. Proper priors and their improper limits require separate treatment.{{cite:gelman2006}} (§2.2, p. 517)

Estimating $\sigma^2$ is another operation entirely. If it is unknown, replacing it with a point estimate does not integrate over its uncertainty. Conditional normal updates may be part of that larger model, but the marginal mean posterior often has heavier tails.{{cite:gelman2006}} (§2.1, pp. 516–517)
