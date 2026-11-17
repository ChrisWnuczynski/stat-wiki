## Lead context
The likelihood-ratio statistic measures the loss of fit caused by imposing the null restrictions. Its chi-squared reference law is an interior, regular-model limit.{{cite:dodge2008}} (pp. 310–311)

## Motivating example
In $100$ Bernoulli trials, $60$ successes favour a fitted proportion $0.6$ over the null $0.5$. The improvement in maximised log likelihood can be compared with one effective squared Gaussian coordinate, because the null imposes one smooth restriction. The approximation depends on the model geometry, rather than merely on a nonnegative statistic.

## Properties — Quadratic likelihood geometry
In a regular $d$-parameter model, local log likelihood has the quadratic form $h^\top Z-\tfrac12h^\top I h+o_p(1)$, where $Z\Rightarrow N_d(0,I)$ and $I\succ0$. Maximising over all local directions completes the square. Maximising under a smooth null restricts directions to its tangent subspace. Whitening by $I^{1/2}$ turns twice the difference of these maxima into the squared length of a standard Gaussian projection onto the orthogonal complement of that subspace. With $r$ independent restrictions that complement has dimension $r$, giving $\chi_r^2$.{{cite:self_liang1987}} (§3, thm. 3 and Case 4, pp. 607–608)

This geometric calculation derives the limit once the local quadratic expansion and asymptotic maximiser localisation are justified. Identifiability, nonsingular information, adequate smoothness and an interior truth ensure those ingredients in regular models. Boundary constraints replace subspaces by cones and alter the projection law.{{cite:self_liang1987}} (§1, pp. 605–606; §3, thm. 3)

## Worked example
The binomial log likelihood difference gives
$$
D=2\{60\log(0.6/0.5)+40\log(0.4/0.5)\}=4.02710.
$$
The $\chi_1^2$ upper tail is $0.04477$. Pearson's statistic for the same two counts is $4$, with tail $0.04550$. Their numerical closeness reflects the shared quadratic approximation; the statistics are not algebraically equal. The likelihood ratio compares the unrestricted and restricted maximum likelihood values.{{cite:dodge2008}} (pp. 310–311)

For a normal sample with unknown variance and null mean $\mu_0$, a separate exact calculation gives $D=n\log\{1+t^2/(n-1)\}$. It is monotone in $t^2$, whose exact null law is $F_{1,n-1}$. Thus an exact $F$ or $t$ calibration can be translated into an exact likelihood-ratio rejection region, although $D$ itself is not an $F$ variable.

**Your turn.** If a regular unrestricted model has dimension $7$ and its smooth null has dimension $4$, what is the limiting reference law? Would a boundary truth preserve that conclusion automatically?

::: {.callout-tip collapse="true" title="Answer"}
There are $3$ restrictions, giving $\chi_3^2$ under the regular interior assumptions. A boundary truth changes the tangent geometry and requires a separate derivation.
:::

## Assumptions and limits
For $Z\sim N(0,1)$, a single nonnegative mean constrained to be zero under the null produces $D=(\max(Z,0))^2$, a half point mass at zero and half $\chi_1^2$. Its positive-tail $5\%$ cutoff is therefore the upper $10\%$ chi-squared cutoff, $2.70554$. That mixture is a particular boundary case. Other nuisance-boundary configurations are more complicated and need not even be chi-squared mixtures.{{cite:self_liang1987}} (§3, Cases 5 and 8, pp. 608–609)

## Intuition
Twice the gain in log likelihood is a comparison of two maxima. In a regular model the log likelihood is locally a downward paraboloid. The unrestricted maximum climbs to the top of that paraboloid. The null maximum is allowed to climb only inside a flat subspace. The difference in height is the squared distance from the unrestricted peak to that subspace. After the information matrix has whitened the coordinates, that distance has a chi-squared limit, with one degree of freedom for each independent restriction. The picture fails when the true parameter sits on a boundary, because the allowed set is then a cone rather than a subspace.{{cite:self_liang1987}} (§3, thm. 3 and Case 4, pp. 607–608)

## Definition
Let $\ell(\theta)$ be the log likelihood and let $\widehat\theta$ maximize it over an open parameter set of dimension $d$. Let $\widehat\theta_0$ maximize it over a smooth null of dimension $d-r$, with the true value interior to both sets. Wilks' statistic is
$$
D=2\{\ell(\widehat\theta)-\ell(\widehat\theta_0)\}.
$$
Under the regularity conditions that give a quadratic expansion, a nonsingular information matrix, and a consistent interior maximizer, $D$ converges in distribution to $\chi^2_r$. For the binomial illustration, $d=1$, $r=1$, and $D=4.02710$. Pearson's statistic equals $4$. The two numbers are close because both are approximations to the same squared normal coordinate; they are not algebraically identical.{{cite:dodge2008}} (pp. 310–311)

## Statistical use
The degrees of freedom are the number of independent restrictions, not the number of nuisance parameters. Testing one coefficient in a model that also contains many unrestricted nuisance coefficients still has a one-degree chi-squared limit when that coefficient is an interior point of a regular model. A null of dimension $4$ inside a regular model of dimension $7$ leaves three restrictions and a $\chi^2_3$ limit. The same count does not apply automatically if the null forces a variance to zero or a probability onto the edge of the parameter space. In the normal-mean problem with unknown variance, $D=n\log\{1+t^2/(n-1)\}$ is a strictly increasing function of $t^2$. An exact $t$ or $F$ rejection region can therefore be rewritten as a region for $D$, but the null distribution of $D$ itself is not the $F$ distribution. For $n=10$ and $t=2$, $D=10\log(1+4/9)\approx 3.677$, while the two-sided $t_9$ tail probability is about $0.077$. The chi-squared approximation on one degree of freedom gives about $0.055$. The exact test uses the monotone transformation, not the chi-squared tail.{{cite:self_liang1987}} (§1, pp. 605–606; §3, thm. 3)

## Common misconceptions
A large maximised likelihood does not by itself supply the reference distribution. The reference distribution comes from the difference of two maxima under the null. A likelihood-ratio statistic that is monotone in an exact $F$ statistic need not have an $F$ law; monotonicity transfers rejection events, not densities. Boundary truth is a second, separate mistake. If a mean is known to be nonnegative and the null sets it to zero, the limit of $D$ puts probability one half at zero and spreads the remaining probability as $\chi^2_1$. The upper $5\%$ point of that mixture is the ordinary upper $10\%$ point of $\chi^2_1$, about $2.706$, not the usual $3.841$. Using the interior critical value makes the test conservative for that particular boundary problem, and other boundary geometries are not the same mixture.{{cite:self_liang1987}} (§3, Cases 5 and 8, pp. 608–609)

## History
The chi-squared limit is a large-sample description of a regular interior comparison. One smooth restriction produces one degree of freedom whether or not the model contains other free parameters, because those parameters are estimated on both sides of the comparison. Three independent restrictions produce three degrees of freedom. The binomial illustration with deviance $4.02710$ is close to a chi-squared tail of $0.04477$, and Pearson's statistic of $4$ has tail $0.04550$. Closeness of those two tails is the quadratic approximation at work. It is not an identity between the two statistics.

A boundary changes the geometry. When a normal mean is constrained to be nonnegative and the null sets it to zero, the limiting law of the likelihood-ratio statistic places probability one half at zero and spreads the rest as chi-squared on one degree of freedom. The upper $5\%$ point of that mixture is about $2.706$. The ordinary interior $5\%$ point, about $3.841$, is a higher threshold. For the small normal sample with $n=10$ and $t=2$, the exact likelihood-ratio statistic is about $3.677$. Its two-sided Student tail is about $0.077$ and the chi-squared tail is about $0.055$. The exact comparison follows the monotone transformation of the $t$ statistic. The chi-squared tail is the large-sample stand-in.{{cite:self_liang1987}} (§3, Cases 5 and 8, pp. 608–609)
