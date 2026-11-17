## Motivating example
A noisy instrument measures an unknown constant. Previous calibration suggests a central value and uncertainty about that constant, while a new series supplies observations with a known measurement variance. A normal prior for the constant and a normal sampling distribution give a model in which both sources of information can be combined analytically. The prior variance describes uncertainty about the constant; the measurement variance describes scatter of observations around it. They are different quantities.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

Such an update can also occur inside a hierarchical model. Conditional on the population mean and variance, a group's latent mean can have a normal prior and a normal conditional posterior. Marginalizing over unknown population parameters generally changes that simple normal form. Conditional conjugacy must therefore be distinguished from a claim about the entire marginal posterior.{{cite:gelman2006}} (§2.1, pp. 516–517)

## Definition — A prior for the mean, a likelihood for the measurements
Assume $X_i\mid\mu\stackrel{\mathrm{iid}}\sim N(\mu,\sigma^2)$ with a genuinely known $\sigma^2>0$, and independently specify the prior $\mu\sim N(m_0,v_0)$ with $v_0>0$. The prior is a distribution on an unknown parameter, while the conditional sampling law generates observations at a fixed parameter value. Their joint density is $p(\mu)\prod_i p(x_i\mid\mu)$. Bayes' rule then conditions this joint law on the observed measurements.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

The sample mean is sufficient for the likelihood's dependence on $\mu$: $\sum_i(x_i-\mu)^2=\sum_i(x_i-\overline x)^2+n(\overline x-\mu)^2$. The first term does not involve $\mu$, so two samples of the same size with the same mean yield the same posterior for $\mu$ under this known-variance model. Their different within-sample scatter would matter in an unknown-variance model.

## Properties — Posterior spread and predictive spread
Completing the square gives
$$v_n=(v_0^{-1}+n\sigma^{-2})^{-1},\qquad m_n=v_n(m_0/v_0+n\overline x/\sigma^2),$$
and $\mu\mid x\sim N(m_n,v_n)$. The posterior mean is a weighted average of the prior and sample means; the weights are proportional to their precisions $1/v_0$ and $n/\sigma^2$. The posterior variance is smaller than each positive input variance $v_0$ and $\sigma^2/n$. These are variances of competing information about the same mean.{{cite:gelman_bda2013}} (Ch. 2, §2.5, pp. 39–41){{cite:raiffa_schlaifer1961}} (Ch. 3, §3.3.4, pp. 64–65){{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

For a future observation conditionally independent of the data given $\mu$, integration gives $X_{\rm new}\mid x\sim N(m_n,\sigma^2+v_n)$. The added term is future observation noise. In contrast, the posterior variance of the latent mean is just $v_n$. A predictive interval and a credible interval for the mean therefore have different widths even though their centers agree.{{cite:gelman_bda2013}} (§2.5, p. 41, posterior predictive distribution){{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

## Worked example — Three observations and an uncertain calibration mean
Take prior $N(5,9)$, known observation variance four and measurements $(4,6,8)$. The sample mean is six. Prior precision is $1/9$, data precision is $3/4$, and total precision is $31/36$. Hence the posterior variance is $36/31=1.161290$ and its mean is $182/31=5.870968$. The sample pulls the mean upward from five toward six without reaching six. These are direct substitutions into the square-completion formulas.{{cite:goodfellow_bengio_courville2016}} (§5.6, eqs. 5.71–5.78, pp. 135–136)

The posterior standard deviation of the mean is $1.077632$. For a new measurement, the predictive variance is $4+36/31=160/31=5.161290$. Knowing the mean more precisely cannot remove the instrument's independent measurement noise. A central 95% credible interval for $\mu$ is approximately $(3.758848,7.983087)$, obtained from the normal quantiles of that posterior.

**Your turn.** Add an observation equal to six. Find the resulting posterior mean and variance.

::: {.callout-tip collapse="true" title="Answer"}
The four observations still average six. Total precision is $1/9+4/4=10/9$, so variance is $9/10$. The mean is $(5/9+6)/(10/9)=59/10=5.9$.
:::

## Assumptions and limits — Known variance is a substantive condition
Replacing $\sigma^2$ by an estimate and then applying the known-variance formulas treats that estimate as certain. It generally understates uncertainty compared with a model that integrates over variance. A hierarchical normal conditional distribution can still be useful computationally, but its interpretation is conditional on the other quantities used in the update.{{cite:gelman2006}} (§2.1, pp. 516–517)

Normal observation noise can also be inappropriate for outliers, dependent measurements or changing precision. The formula's analytic convenience does not establish its sampling assumptions. Under the stated model, however, one-step and sequential updating agree because likelihood multiplication is associative and each independent observation adds its precision and precision-weighted value.

Under this normal model the one-step update and the sequential update agree on the same posterior.
