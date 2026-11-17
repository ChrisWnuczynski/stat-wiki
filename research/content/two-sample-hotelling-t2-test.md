## Motivating example
Two treatments may differ in a combination of measurements even when neither coordinate alone supplies a decisive comparison. Hotelling's statistic measures the mean difference relative to its pooled covariance, taking account of the directions in which observations typically vary. The test asks about a population mean vector, rather than whether a classifier can predict treatment labels.{{cite:ackermann_strimmer2009_genesets}} (Appendix, “Hotelling's T²-test and related methods”)

## Definition — Centre the stated null difference
Let $d=\bar X_1-\bar X_2-\delta_0$ and $k=n_1n_2/(n_1+n_2)$. Under the common-covariance model, the covariance of the mean difference is $\Sigma/k$ and its estimate is $S/k$. Thus
$$T^2=k\,d^TS^{-1}d.$$
The formulas with no $\delta_0$ subtraction are the special case of testing equal means. The covariance estimate centres each group at its own sample mean, because covariance estimation does not impose the equality null.{{cite:ackermann_strimmer2009_genesets}} (Appendix, pooled-covariance statistic)

## Properties — Scaling, invariance and exact calibration
Put $N=n_1+n_2$ and $\nu=N-2$. The residual covariance has $\nu$ degrees of freedom. Independent Gaussian projection coordinates give $\nu S\sim W_p(\Sigma,\nu)$, independently of the normal mean difference. The resulting normal/Wishart ratio has
$$\frac{\nu-p+1}{\nu p}T^2\sim F_{p,\nu-p+1}$$
under the null. The dimension correction is therefore $N-p-1$, not $N-2$ in the denominator of the reference distribution.{{cite:ackermann_strimmer2009_genesets}} (Appendix, null F distribution){{cite:nist_hotelling2002}} (§6.5.4.3, one-sample normal/Wishart calibration)

For a nonsingular change of measurement coordinates $A$, the difference becomes $Ad$ and covariance becomes $ASA^T$. Its inverse is $A^{-T}S^{-1}A^{-1}$, so the quadratic form is unchanged. This proves invariance under changes of units and invertible linear combinations of the measured outcomes. Dropping a coordinate, unlike changing units, is not invertible and changes the hypothesis.

At $p=1$, the multiplier becomes one, the denominator degrees of freedom are $N-2$, and $T^2$ is exactly the squared pooled two-sample Student statistic. This scalar check is a useful way to detect a misplaced dimension or sample-size factor.{{cite:nist_hotelling2002}} (§6.5.4.3, Student-square template)

## Worked example — A bivariate mean difference
Suppose $n_1=10$, $n_2=12$, $\delta_0=0$, $\bar x_1-\bar x_2=(2,1)^T$, and
$$S=\begin{pmatrix}4&1\\1&9\end{pmatrix},\qquad S^{-1}=\frac1{35}\begin{pmatrix}9&-1\\-1&4\end{pmatrix}.$$
The quadratic form is $36/35\approx1.028571$, so $T^2=(120/22)(36/35)\approx5.610390$. With $p=2$ and $\nu=20$, the scaled statistic is $F=19T^2/40\approx2.664935$ on $(2,19)$ degrees of freedom. Its upper-tail probability is approximately $0.095462$, which exceeds $0.05$.

The corresponding $95\%$ cutoff for $T^2$ is approximately $7.414512$. The observed statistic falls below it, so the zero difference belongs to the matching confidence ellipsoid. This nonrejection allows substantial uncertainty in the difference; it does not establish that the treatment means coincide.{{cite:ackermann_strimmer2009_genesets}} (Appendix, quadratic statistic and F comparison)

**Your turn.** In one dimension, $n_1=n_2=5$, pooled variance $s_p^2=4$, and observed mean difference $2$. Compute $T^2$ and the corresponding pooled $t$. State the null degrees of freedom.

::: {.callout-tip collapse="true" title="Answer"}
Here $k=25/10=2.5$, so $T^2=2.5(2^2)/4=2.5$. The pooled $t$ is $2/\sqrt{4(1/5+1/5)}=\sqrt{2.5}\approx1.581139$. Its degrees of freedom are $8$, giving $T^2\sim F_{1,8}$ under the null.
:::

## Assumptions and limits — Covariance equality is substantive
The pooled finite-sample law needs common covariance, normality, within-group independence and independent groups. Equal group sizes do not make unequal covariances equal. In the univariate case with equal group sizes but unequal variances, a pooled denominator is a sum of differently scaled chi-squared variables, so it generally is not a single scaled chi-squared variable. The exact Student ratio therefore fails even though some large-sample variance calculations simplify.

For unequal covariance matrices, estimate the mean-difference covariance by $S_1/n_1+S_2/n_2$ and use an appropriate approximate multivariate Behrens–Fisher calibration. The modified Wishart moment approximation uses trace terms to describe the contributions of each sample and leads to the degrees-of-freedom expression above. This is an approximation, and its derivation is separate from the exact pooled result.{{cite:krishnamoorthy_yu2012}} (Appendix A, modified Wishart approximation; §1, pp. 141–142)

## Statistical use — Numerical stability and dimension
Solve $Sv=d$ and compute $k\,d^Tv$ instead of explicitly forming an inverse in numerical code. Check that the pooled matrix has sufficient rank: its rank is at most $N-2$, and exact calibration needs $N-p-1>0$. A regularised or pseudoinverse statistic may be useful in higher dimensions, but its reference law must be established for that procedure.{{cite:ackermann_strimmer2009_genesets}} (Appendix, dimension reduction and covariance regularisation)

When the pooled covariance is singular, the quadratic form in the mean difference is not defined through the usual inverse, and the F calibration used for a full-rank difference no longer applies.
