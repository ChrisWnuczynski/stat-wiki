## Motivating example
Suppose an instrument measures deviations from a reference value that is known independently. The spread of those deviations is uncertain. A few observations can update a distribution for the variance without also estimating the reference mean. Normal sampling and an inverse-gamma prior make this known-mean variance update exact. Treating an estimated mean as though it were known would change the statistical experiment.{{cite:gelman2006}} (§3.1, pp. 518–519)

Inverse-gamma conditional updates also occur within hierarchical models, where the current values of other parameters determine a sum of squared residuals. A convenient full conditional does not establish that the marginal variance posterior has the same family. Nor does conjugacy alone establish that a small-shape prior is weakly informative.{{cite:gelman2006}} (§§2.1, 3.1, pp. 516–518)

## Statement
Use the shape–scale convention $p(v)=b_0^{a_0}v^{-a_0-1}e^{-b_0/v}/\Gamma(a_0)$ on $v>0$, with $a_0,b_0>0$. For $n$ independent $N(\mu,v)$ observations with known $\mu$, let $Q_\mu=\sum_i(x_i-\mu)^2$. Then
$$v\mid x\sim\operatorname{InvGamma}(a_n,b_n),\quad a_n=a_0+n/2,\quad b_n=b_0+Q_\mu/2.$$
Equivalently, precision $1/v$ has a gamma posterior with shape $a_n$ and rate $b_n$. Stating the density kernel fixes which rate or scale convention is intended.{{cite:gelman2006}} (§3.1, pp. 518–519)

The name normal–inverse-gamma often describes a joint prior for an unknown mean and variance. The calculation here conditions on a known mean. In a joint model, integrating an unknown mean changes the residual sum of squares and contributes a prior–sample discrepancy term. The two calculations should be distinguished by their assumptions rather than only by a family name.{{cite:gelman2006}} (§2.1, conditional versus marginal conjugacy)

## Proof
The normal likelihood in $v$ is proportional to $v^{-n/2}\exp\{-Q_\mu/(2v)\}$. Multiplying by the inverse-gamma kernel gives $v^{-(a_0+n/2)-1}\exp\{-(b_0+Q_\mu/2)/v\}$. Its shape and scale are positive, so it normalizes to the stated inverse-gamma posterior. With $w=1/v$, the Jacobian is $w^{-2}$, giving $p(w\mid x)\propto w^{a_n-1}e^{-b_nw}$. Thus the precision law is gamma in shape–rate form.{{cite:gelman2006}} (§3.1, pp. 518–519)

For any $r<a_n$, a reciprocal substitution in the gamma integral gives $E(v^r\mid x)=b_n^r\Gamma(a_n-r)/\Gamma(a_n)$. The gamma normalization also gives each finite moment explicitly.{{cite:ng_tian_tang2011_dirichlet}} (§1.2.1, eqs. 1.2–1.3) In particular, the mean is $b_n/(a_n-1)$ for $a_n>1$ and variance is $b_n^2/\{(a_n-1)^2(a_n-2)\}$ for $a_n>2$. Differentiating the log density yields its mode $b_n/(a_n+1)$. A proper posterior can therefore lack a finite mean or variance.

## Key results — Centering at a known value uses all departures
The identity $Q_\mu=\sum_i(x_i-\overline x)^2+n(\overline x-\mu)^2$ separates within-sample scatter from displacement of the sample mean. Both contribute evidence about a variance around a known mean. Centering only at $\overline x$ discards the second term. In a small sample concentrated far from its known reference, that discarded term may dominate the likelihood's information about spread.{{cite:gelman2006}} (§3.1, pp. 518–519)

The update is additive over independent batches: each observation adds one-half to shape and half its squared departure to scale. This sufficiency also makes analytical calculations useful for checking a numerical sampler. The implementation should be checked under the same variance or precision parameterization used in its density.

## Worked example — Three deviations from ten
Let $\mu=10$, observe $(8,10,12)$ and take prior $\operatorname{InvGamma}(2,3)$. The squared-deviation sum is eight, so $a_n=7/2$ and $b_n=7$. The posterior mean variance is $7/(5/2)=2.8$, its mode is $7/(9/2)=14/9=1.555556$, and its variance is $392/75=5.226667$. An equal-tailed 90% credible interval for $v$ is approximately $(0.995227,6.459501)$, calculated from the inverse-gamma quantiles. The mean and mode differ because they summarize a skewed positive distribution.{{cite:gelman2006}} (§3.1, pp. 518–519)

**Your turn.** Add one further measurement equal to the known mean ten. What changes in the posterior shape, scale and mean?

::: {.callout-tip collapse="true" title="Answer"}
The shape rises to four, the scale stays seven because the new squared departure is zero, and the posterior mean becomes $7/(4-1)=7/3$.
:::

## Common misconceptions — Small hyperparameters are not automatic ignorance
A small inverse-gamma shape and scale can have a strong effect near zero and can produce problematic behavior in hierarchical variance inference. The numerical size of a hyperparameter does not measure the information of the induced prior on a standard deviation, a logarithm or a variance ratio. Prior predictive checks and sensitivity analysis should use the substantive measurement scale.{{cite:gelman2006}} (§§4.3, 5.1, pp. 521–525)

A credible interval for $v$ is not an interval for a future observation. A standard-deviation interval is obtained by taking square roots of variance interval endpoints, since square root is monotone. A posterior mode does not obey the same transformation rule because density maximizers depend on Jacobians.
