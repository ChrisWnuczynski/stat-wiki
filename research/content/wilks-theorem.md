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
