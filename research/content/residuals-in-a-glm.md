## Motivating example
An observed count of $7$ is five above a fitted mean of $2$; an observed count of $55$ is five above a fitted mean of $50$. Raw residuals treat these departures as equal. A Poisson model does not, because its variance grows with its mean. Residual choice decides which aspect of the fitted distribution defines the scale of a discrepancy.{{cite:dunn_smyth1996}} (§2, “Pearson and Deviance Residuals”)

## Definition — Response, Pearson and deviance scales
The response residual $e_i=y_i-\hat\mu_i$ preserves the response's units. It compares the observation with its fitted mean, in the same observed-minus-fitted sense used in linear regression.{{cite:dodge2008}} (p. 457, “Residual”)

Write $\operatorname{Var}(Y_i)=\phi V(\mu_i)$. One Pearson convention divides by $\sqrt{V(\hat\mu_i)}$ and another divides by $\sqrt{\hat\phi V(\hat\mu_i)}$. The latter is dispersion-scaled. State the convention when comparing numbers from different software, especially for Gaussian, Gamma or overdispersed models. For ordinary Poisson and Bernoulli models $\phi=1$, so those conventions coincide.{{cite:dunn_smyth1996}} (§2, variance function and Pearson residual)

A unit deviance measures twice the log-likelihood loss from fitting the model mean rather than a saturated mean for one observation. Attaching the sign of $y_i-\hat\mu_i$ gives a deviance residual. Its square contributes to the unscaled deviance. Dispersion-scaled deviance residuals divide additionally by $\sqrt{\hat\phi}$. The likelihood comparison and the chosen scaling should both be explicit.{{cite:dunn_smyth1996}} (§2, unit deviance and signed residual)

## Properties — Deriving the Poisson formula
For a Poisson observation, terms independent of its mean cancel in the log-likelihood difference, giving
$$d(y,\mu)=2\{y\log(y/\mu)-(y-\mu)\},\qquad\mu>0.$$
At $y=0$, the continuous convention $y\log(y/\mu)=0$ gives $d=2\mu$. The deviance residual is therefore $-\sqrt{2\mu}$ at zero, while its Pearson residual is $-\sqrt\mu$.

For $y=\mu+\delta$ near its mean, expand $\log(1+\delta/\mu)$ to obtain
$$d(y,\mu)=\frac{\delta^2}{\mu}-\frac{\delta^3}{3\mu^2}+O(\delta^4/\mu^3).$$
To first order the signed square root is $\delta/\sqrt\mu$, the Pearson residual. The next term introduces asymmetry: equal-sized positive and negative count deviations need not have equal deviance magnitudes. This local relationship does not make either residual exactly normal for a small discrete mean.{{cite:dunn_smyth1996}} (§2, normality limits of Pearson and deviance residuals)

## Worked example — Equal raw deviations, different evidence
At $\mu=50$, observations $45$ and $55$ have Pearson residuals $-0.7071$ and $0.7071$. Their deviance residuals are approximately $-0.7194$ and $0.6958$. At $\mu=2$, observation $7$ has Pearson residual $3.5355$ and deviance residual $2.7457$. These formulas score departures from the model without assuming symmetry of the count distribution.

For one Bernoulli observation, the unit deviance is $-2\log p$ for a success and $-2\log(1-p)$ for a failure. At $p=0.7$, this gives signed residuals approximately $0.8446$ and $-1.5518$. A rare failure is a larger departure than an expected success. At $p=0.5$, the deviance magnitudes are both $\sqrt{2\log2}\approx1.1774$, whereas Pearson magnitudes are both one.

**Your turn.** A Poisson observation is zero and its fitted mean is $3$. Find its response, Pearson and deviance residuals under $\phi=1$.

::: {.callout-tip collapse="true" title="Answer"}
The response residual is $-3$. The Pearson residual is $-3/\sqrt3=-\sqrt3\approx-1.7321$. The deviance residual is $-\sqrt6\approx-2.4495$, using the zero-count convention in the unit deviance.
:::

## Statistical use — Understand the bands before interpreting a plot
For binary observations, raw residuals lie on the two curves $1-\hat p$ and $-\hat p$. Pearson and deviance transformations replace those with other two-curve patterns; they do not remove discreteness. Integer-valued counts likewise form response-specific bands. A pattern required by support is different from a trend signalling an omitted mean relationship.{{cite:dunn_smyth1996}} (§1, discrete-response residual curves)

Randomized quantile residuals address this by choosing $U_i$ uniformly between $F_i(y_i^-)$ and $F_i(y_i)$ and then applying the standard normal quantile. With known correct model parameters this randomisation fills the probability jumps and produces a uniform $U_i$, hence a normal transformed residual. For a discrete outcome $y$ with mass $p_y$, the conditional uniform density is $1/p_y$ on its CDF jump, and weighting by $P(Y=y)=p_y$ gives unconditional density one there. The jump intervals partition $(0,1)$, establishing the uniform law. Estimated parameters introduce additional sampling variation. Different randomisations also introduce visible variation in a particular diagnostic plot.{{cite:dunn_smyth1996}} (§3, “Randomized Quantile Residuals”)

## Assumptions and limits
Residuals calculated after fitting share parameter estimates, so they generally are dependent even when responses are independent. Leverage can reduce their variances and motivates further standardisation. Inspect residuals against fitted means, predictors and relevant time or group labels, with the model's support in mind. Deviance residuals are not automatically normal, equal-variance or universally preferable under skewness; a diagnostic must be assessed against the distribution and fitting procedure it uses.
