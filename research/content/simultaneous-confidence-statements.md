## Motivating example
A study compares two treatments on several correlated measurements. Reporting a separate interval for each coordinate does not automatically cover all coordinates together, and it does not protect a contrast selected after looking at the measurements. A simultaneous statement starts from a confidence region for the whole mean difference, then derives bounds that hold for every linear direction whenever that one region covers.{{cite:ackermann_strimmer2009_genesets}} (Appendix, “Hotelling's T²-test and related methods”, mean-difference statistic)

## Definition — Begin with an ellipsoid
Let $\hat\delta=\bar X_1-\bar X_2$ and $C=(1/n_1+1/n_2)S$, where $S$ is a positive-definite pooled covariance matrix under the independent common-covariance normal model. Inverting the Hotelling test gives a region
$$\mathcal E=\{\delta:(\hat\delta-\delta)^TC^{-1}(\hat\delta-\delta)\le c\},$$
where $c$ is the appropriate $T^2$ cutoff. Here use quantile notation explicitly: $c=\frac{(N-2)p}{N-p-1}F_{p,N-p-1;1-\alpha}$ for $N=n_1+n_2$. The upper-tail notation in the formulas above denotes the same cutoff.{{cite:ackermann_strimmer2009_genesets}} (Appendix, Hotelling F calibration)

Under the stated sampling assumptions, the random region has coverage $1-\alpha$ for the fixed vector $\delta$. Coverage concerns repeated samples, not a posterior probability distribution over points of the realised ellipsoid. The distinction is the same as for an ordinary mean interval.{{cite:nist_handbook2002}} (§1.3.5.2, confidence coefficient)

## Properties — Optimise a contrast over the ellipsoid
For a fixed vector $a$, write $h=\delta-\hat\delta$ and $z=C^{-1/2}h$. Then $\delta\in\mathcal E$ means $\|z\|^2\le c$, while
$$a^Th=(C^{1/2}a)^Tz.$$
Cauchy–Schwarz gives $|a^Th|\le\sqrt{c\,a^TCa}$. Equality is attained, for nonzero $a$, by $z$ proportional to $C^{1/2}a$, with sign chosen to maximise or minimise the contrast. Consequently the exact range of $a^T\delta$ over the ellipsoid is
$$a^T\hat\delta\pm\sqrt{c\,a^TCa}.$$
This is an optimisation statement about a set, independent of the sampling proof that calibrated the set. The Hotelling covariance-weighted construction supplies the ellipsoid used in that argument.{{cite:nist_hotelling2002}} (§6.5.4.3, quadratic-form region)

If the true vector belongs to the ellipsoid, these intervals cover every $a^T\delta$ simultaneously, including directions chosen after seeing the data. Conversely, if the vector lies outside, choose $a=C^{-1}(\delta-\hat\delta)$; its contrast violates the bound. Thus the all-directions event is exactly the ellipsoid event. Coordinate intervals alone form a bounding box and are a weaker simultaneous requirement.

## Worked example — Coordinates and a sum
Suppose $n_1=n_2=10$, $p=2$, $\hat\delta=(2,1)^T$ and $S=\left(\begin{smallmatrix}4&1\\1&9\end{smallmatrix}\right)$. At $95\%$ confidence, $c\approx7.605594$. Since $C=0.2S$, the coordinate half-widths are approximately $2.466673$ and $3.700009$. The intervals are therefore $2\pm2.466673$ and $1\pm3.700009$.

For the sum, choose $a=(1,1)^T$. The estimated sum is $3$ and its variance factor is $a^TCa=0.2(4+2+9)=3$. Its half-width is $\sqrt{3c}\approx4.776692$. Adding coordinate half-widths would give a wider bound, because it discards the ellipsoid's covariance geometry. The direct contrast interval is the tight projection of that ellipsoid.{{cite:ackermann_strimmer2009_genesets}} (Appendix, pooled covariance and mean difference)

**Your turn.** An ellipsoid uses $C=\operatorname{diag}(1,4)$ and $c=9$, with centre $(0,0)$. Find the simultaneous half-width for the second coordinate and for the sum of both coordinates.

::: {.callout-tip collapse="true" title="Answer"}
The second coordinate has half-width $\sqrt{9(4)}=6$. The sum has variance factor $1+4=5$, giving half-width $\sqrt{45}=3\sqrt5\approx6.708204$.
:::

## Statistical use — State the family of comparisons
Bonferroni intervals are another construction: for a prespecified finite list of $m$ contrasts, build each interval with failure probability at most $\alpha/m$. The union bound makes the probability of any miss at most $\alpha$, regardless of dependence between the intervals. This protects that finite list, whereas the Hotelling projection protects every direction. The more suitable construction depends on which family the scientific question actually requires.{{cite:nist_bonferroni2002}} (§7.4.7.3, family coverage bound)

## Assumptions and limits
Exact pooled Hotelling coverage needs independent multivariate normal groups, common positive-definite covariance and $N-p-1>0$. A coordinate's units enter its interval through $C$, so changing units also changes the numerical representation of a contrast. Replacing $S$ by another covariance estimate may be sensible, but it changes the calibration problem. Simultaneity protects the specified linear comparisons; it does not correct selection of the outcomes, model or sampling design through an unrelated process.

A collection of intervals has a coverage probability for the whole collection, and that probability is smaller than the coverage of one prechosen coordinate when the coordinates can miss separately.
