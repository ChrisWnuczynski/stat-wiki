## Lead context

It is a test of the equality of the means of two or more independent groups that does not assume the groups share a common population variance; it is also called Welch's one-way test. It is the multi-group counterpart of Welch's two-sample t procedure: where the classic one-way analysis of variance pools every group's observations into a single error mean square, Welch's procedure weights each group mean by the precision with which it is estimated, and then corrects both the statistic and its reference degrees of freedom for the uncertainty in the separate variance estimates. The procedure was published by Welch in 1951 as an alternative approach to the comparison of several mean values {{cite:welch1951}} (pp. 330–336).

Let the groups be indexed by $j = 1, \ldots, k$. In group $j$ there are $n_j \ge 2$ independent observations with population mean $\mu_j$ and population variance $\sigma_j^2$, sample mean $\bar Y_j$ and sample variance $s_j^2$, computed with divisor $n_j - 1$. Write $N = \sum_{j=1}^{k} n_j$ for the total sample size. The null hypothesis is

$$H_0: \mu_1 = \mu_2 = \cdots = \mu_k,$$

against the alternative that at least two of the $\mu_j$ differ. No condition $\sigma_1^2 = \cdots = \sigma_k^2$ is imposed. The test is an omnibus test: rejection establishes that the means are not all equal, and nothing more specific. Which pairs differ is a separate question, answered by a follow-up procedure such as Games–Howell, described below. Like its two-sample counterpart, the test is approximate: its statistic does not have an exact $F$ distribution in finite samples, and the sense in which the $F$ reference is an approximation is stated precisely in the section on the statistic.

## Intuition — The assumption that the classic test spends, and what its failure costs

The classic one-way analysis of variance writes each observation as a group mean plus an error, estimates one common error variance from the pooled within-group sum of squares, and refers the ratio of the between-group mean square to that pooled estimate to an $F$ distribution on $(k - 1, N - k)$ degrees of freedom {{cite:nist_anova2002}} (§7.4.3.1). The pooling is not a computational convenience. It is the step that makes the reference distribution exact under normal sampling: if every $\sigma_j^2$ equals a common $\sigma^2$, the pooled mean square estimates that $\sigma^2$ whichever group it is computed from, and the numerator and denominator of the $F$ ratio are independent scaled chi-squared variables. If the $\sigma_j^2$ differ, the pooled mean square estimates a sample-size-weighted average of unequal quantities, and neither the size nor the power of the classic test is the value its $F$ table reports.

The damage depends on how the unequal variances are paired with the unequal sample sizes, and this interaction, not heterogeneity alone, is the central practical fact. When the larger groups have the larger variances, the pooled denominator is inflated by precisely the groups that dominate the numerator's weighting, and the classic test becomes conservative: it rejects less often than its nominal level, under the null and under alternatives alike. When the smaller groups have the larger variances, the pooled denominator understates the variability of the comparisons that carry the between-group sum of squares, and the classic test becomes liberal: it rejects more often than its nominal level when $H_0$ is true, so a nominally $5\%$ test may have a materially larger actual type I error rate. With equal sample sizes the two effects largely cancel and the classic test is comparatively robust to heterogeneity; with unequal $n_j$ they do not. Tomarken and Serlin's comparison of analysis-of-variance alternatives under variance heterogeneity documents this pattern across noncentrality structures {{cite:tomarken_serlin1986}} (pp. 90–99), and the quantitative review by Lix, Keselman and Keselman reaches the same conclusion across the published simulation record: the classic $F$ test's error rates are trustworthy under heterogeneity chiefly when group sizes are equal or nearly so {{cite:lix_keselman_keselman1996}} (pp. 579–619). The two-sample literature makes the identical point for $k = 2$: pooling is the step that fails first, and it fails in a direction determined by the pairing of sample size with variance {{cite:delacre2017_welch}} (pp. 95–96).

A preliminary test of equal variances does not repair this. Testing $H_0: \sigma_1^2 = \cdots = \sigma_k^2$ first, for example with Levene's test, and choosing the classic or the Welch procedure according to the outcome, makes the final procedure a two-stage procedure whose error rates are those of neither stage: the preliminary test has low power exactly in the small samples where the choice matters, and conditioning the main test on its outcome distorts the main test's calibration. The defensible practice is to select the procedure from the design and the plausibility of a common variance before examining the test outcomes, or to use the Welch procedure by default when a common variance is not part of the scientific model.

## Definition — Precision weights and a weighted grand mean

For group $j$, the variance of the sample mean $\bar Y_j$ is $\sigma_j^2 / n_j$, estimated by $s_j^2 / n_j$. Welch's weight for group $j$ is the reciprocal of that estimated variance,

$$w_j = \frac{n_j}{s_j^2}, \qquad W = \sum_{j=1}^{k} w_j,$$

where $W$ is the total weight {{cite:welch1951}} (pp. 330–336). A group receives a large weight when its mean is estimated precisely, either because $n_j$ is large or because $s_j^2$ is small. These are the weights that a weighted least-squares estimate of a common mean would use if the $\sigma_j^2$ were known, with the population variances replaced by their sample estimates; that substitution is the source of every approximation that follows.

The weighted grand mean is

$$\bar Y_w = \frac{\sum_{j=1}^{k} w_j \bar Y_j}{W}.$$

It is not the ordinary grand mean $\bar Y = \sum_j n_j \bar Y_j / N$, and the difference matters. The ordinary grand mean weights groups by sample size alone, so a large but imprecise group moves it substantially; the weighted grand mean weights by precision, so the centre against which the group means are compared is the best available estimate of the common mean under $H_0$, given the separate variances. The weighted between-group sum of squares is

$$Q = \sum_{j=1}^{k} w_j (\bar Y_j - \bar Y_w)^2.$$

If the variances were known and $H_0$ were true, $Q$, with population weights in place of the $w_j$, would have a chi-squared distribution on $k - 1$ degrees of freedom. With estimated weights it does not, and the statistic below is the correction of $Q$ that Welch constructed for that reason {{cite:welch1951}} (pp. 330–336).

## Properties — The Welch statistic, its correction term and its degrees of freedom

Define the correction quantity

$$A = \sum_{j=1}^{k} \frac{(1 - w_j / W)^2}{n_j - 1}.$$

At fixed group size, each summand decreases as group $j$'s share of the total weight grows: for $n_j = 5$ it is $(1 - 0.1)^2 / 4 = 0.2025$ at a weight share of $0.1$, but only $(1 - 0.9)^2 / 4 = 0.0025$ at a share of $0.9$. A small group carrying a low weight can therefore contribute substantially to $A$ — close to $1/(n_j - 1)$ when its share is negligible — while a group that dominates the total weight contributes almost nothing through its own summand; a summand is small when the share is large or the group is based on many observations. Welch's statistic is

$$F_W = \frac{Q / (k - 1)}{1 + \dfrac{2(k - 2)}{k^2 - 1} A},$$

referred to an $F$ distribution on numerator degrees of freedom

$$\nu_1 = k - 1$$

and denominator degrees of freedom

$$\nu_2 = \frac{k^2 - 1}{3A}$$

{{cite:welch1951}} (pp. 330–336). Three features of this construction require exact statement.

**What is exact and what is approximate.** The definitions of $w_j$, $\bar Y_w$, $Q$ and $A$ are exact arithmetic functions of the sample summaries. Nothing distributional is exact thereafter. The reference statement $F_W \approx F_{\nu_1, \nu_2}$ under $H_0$ is an approximation obtained by matching moments of the distribution of $Q$, in the manner of the Welch–Satterthwaite approximation for a linear combination of variance estimates {{cite:satterthwaite1946}} (pp. 110–114). The denominator degrees of freedom $\nu_2$ are estimated from the same data as the statistic, are generally not an integer, and are not a count of observations. The correction factor in the denominator of $F_W$ is part of the same moment-matching: it inflates the statistic's denominator so that the first two moments of the corrected statistic agree more closely with those of the reference $F$. A $p$-value from this procedure is therefore an approximate $p$-value even when every group is exactly normally distributed. It is not an exact test at any sample size, and reporting it as though it were exact misstates what was computed.

**The case $k = 2$.** When $k = 2$, the factor $2(k - 2)$ is zero, so the correction factor is $1$, and $F_W$ reduces to $Q$. In that case $Q$ is exactly the square of Welch's two-sample $t$ statistic, and $\nu_2 = 1 / A$ is exactly the Welch–Satterthwaite degrees of freedom of that $t$ statistic. Welch's ANOVA is therefore a genuine generalisation of the two-sample procedure, not merely an analogue of it: the 1947 two-sample approximation {{cite:welch1947}} (pp. 28–35) is the $k = 2$ special case of the 1951 construction. The two-sample interval built on that $t$ statistic is treated in the article on the [Welch interval](welch-interval.qmd). Standard software exposes the same relationship: in R, `oneway.test` with `var.equal = FALSE` applies Welch's 1951 approximate method, described there as generalising the two-sample Welch test to arbitrarily many samples {{cite:rstats_oneway2026}} (Arguments, `var.equal`).

**Behaviour when the variances are equal.** If the $s_j^2$ are all similar, the weights are approximately proportional to the $n_j$, and $\bar Y_w$ is close to the ordinary grand mean. Similarity of the variances does not by itself make $A$ small: with equal weights and a common group size $n$, $A = (k - 1)^2 / (k (n - 1))$, so three groups of size two with exactly equal sample variances still give $A = 4/3$ and $\nu_2 = 2$. It is large group sizes, for fixed $k$, that make $A$ small, the correction factor close to $1$ and $\nu_2$ large; in that regime the Welch statistic gives a result close to the classic $F$ on the same data, though not identical to it, because the reference degrees of freedom still differ. The cost of using Welch's procedure when the classic assumptions happen to hold is a small loss of power; the cost of using the classic procedure when they fail can be a type I error rate far from the nominal level. That asymmetry is the argument for Welch's procedure as a default in the two-sample case {{cite:delacre2017_welch}} (pp. 95–96), and it carries over to $k$ groups.

### A distinct alternative — the Brown–Forsythe statistic

Welch's statistic is not the only heteroscedastic alternative to the classic $F$, and it should not be conflated with the statistic proposed by Brown and Forsythe in the same problem. Brown and Forsythe examined the small-sample behaviour of several statistics for testing the equality of means and proposed a statistic, conventionally denoted $F^*$, that retains the classic unweighted between-group sum of squares in the numerator and instead replaces the pooled denominator by a weighted combination of the separate group variances, with Satterthwaite-type degrees of freedom {{cite:brown_forsythe1974_means}} (pp. 129–132). The architectural difference is genuine: Welch reweights the numerator around a precision-weighted centre and corrects the result, whereas Brown and Forsythe leave the classic numerator intact and repair only the denominator. The two statistics can therefore disagree on the same data, and a report must name which was computed.

A further naming hazard is specific to this pair of authors. Brown and Forsythe also published, in 1974, robust tests for the equality of *variances*, in which the median-centred form of Levene's test originates {{cite:brown_forsythe1974_variances}} (pp. 364–367). That Brown–Forsythe test answers a question about spread, is treated in the article on [Levene's test](levene-s-test.qmd), and is not an alternative test of equal means. Citing "Brown–Forsythe (1974)" without the journal or the subject leaves the reference ambiguous between two different papers solving two different problems.

## Worked example — Three groups, unequal sizes and unequal variances

Three independent groups are

- Group 1: $8, 9, 10, 11, 12$, so $n_1 = 5$;
- Group 2: $13, 15, 17, 15$, so $n_2 = 4$;
- Group 3: $10, 14, 18, 22, 26, 14, 18, 22$, so $n_3 = 8$.

The total sample size is $N = 17$. The group means are $\bar Y_1 = 10$, $\bar Y_2 = 15$ and $\bar Y_3 = 18$. The within-group sums of squares are $10$, $8$ and $192$, so the sample variances are

$$s_1^2 = \frac{10}{4} = 2.5, \qquad s_2^2 = \frac{8}{3} \approx 2.6667, \qquad s_3^2 = \frac{192}{7} \approx 27.4286.$$

Group 3 is both the largest group and by far the most variable: its variance is roughly eleven times that of group 1. This is the pairing — larger group, larger variance — under which the classic test is expected to be conservative.

The weights are

$$w_1 = \frac{5}{2.5} = 2, \qquad w_2 = \frac{4}{8/3} = 1.5, \qquad w_3 = \frac{8}{192/7} \approx 0.2917,$$

with total weight $W \approx 3.7917$. Group 3, despite contributing $8$ of the $17$ observations, receives only $w_3 / w_1 = 0.2917 / 2 = 7/48 \approx 0.1458$ of the weight of group 1 — slightly more than one seventh ($1/7 \approx 0.1429$), but still a small fraction of it — because its mean is estimated imprecisely. The weighted grand mean is

$$\bar Y_w = \frac{2(10) + 1.5(15) + 0.2917(18)}{3.7917} \approx 12.5934,$$

well below the ordinary grand mean $\bar Y \approx 14.9412$, which group 3's size pulls upward. The weighted between-group sum of squares is

$$Q = 2(10 - 12.5934)^2 + 1.5(15 - 12.5934)^2 + 0.2917(18 - 12.5934)^2 \approx 30.6648.$$

The correction quantity is

$$A = \frac{(1 - 2/3.7917)^2}{4} + \frac{(1 - 1.5/3.7917)^2}{3} + \frac{(1 - 0.2917/3.7917)^2}{7} \approx 0.2993,$$

so the correction factor is $1 + \frac{2(3 - 2)}{3^2 - 1}(0.2993) \approx 1.0748$ and

$$F_W = \frac{30.6648 / 2}{1.0748} \approx 14.2650,$$

on $\nu_1 = 2$ and $\nu_2 = \dfrac{8}{3(0.2993)} \approx 8.9094$ degrees of freedom. The upper-tail probability of an $F_{2, \, 8.9094}$ distribution at $14.2650$ is $p \approx 0.0017$. At the $5\%$ level, and at the $1\%$ level, $H_0$ is rejected: the three means are not all equal.

For contrast, the classic analysis of the same $17$ observations gives a between-group sum of squares of $196.9412$ on $2$ degrees of freedom, a within-group sum of squares of $210$ on $14$ degrees of freedom, mean squares $98.4706$ and $15$, and $F \approx 6.5647$ on $(2, 14)$ degrees of freedom, with $p \approx 0.0097$. The classic test also rejects at $5\%$, but its $p$-value is nearly six times the Welch $p$-value, and the discrepancy is in the direction the pairing predicts: the large, highly variable third group inflates the pooled error mean square to $15$, although two of the three groups have variances near $2.5$, and the pooled denominator thereby understates how precisely groups 1 and 2 locate their means. Neither $p$-value should be read to more precision than the approximations support; the comparison, not the third decimal place, is the point.

**Your turn.** Three new groups are

- Group A: $5, 7, 9, 7$;
- Group B: $9, 10, 11, 12, 13$;
- Group C: $12, 16, 20, 24, 16, 20$.

Compute the group means and sample variances, the weights, the weighted grand mean, $Q$, $A$, $F_W$, both degrees of freedom and the approximate $p$-value. Do you reject $H_0$ at the $5\%$ level?

::: {.callout-tip collapse="true" title="Answer"}
The sample sizes are $n_A = 4$, $n_B = 5$ and $n_C = 6$. The means are $7$, $11$ and $18$, and the sample variances are $8/3 \approx 2.6667$, $2.5$ and $17.6$. The weights are $w_A = 1.5$, $w_B = 2$ and $w_C \approx 0.3409$, with $W \approx 3.8409$ and weighted grand mean $\bar Y_w \approx 10.0592$. Then $Q \approx 37.3047$ and $A \approx 0.3473$, the correction factor is approximately $1.0868$, and $F_W \approx 17.1622$ on $\nu_1 = 2$ and $\nu_2 \approx 7.6779$ degrees of freedom, giving $p \approx 0.0015$. Reject $H_0$ at the $5\%$ level. Note that the classic $F$ on these data is approximately $17.7132$ on $(2, 12)$ degrees of freedom: here it is slightly larger than the Welch statistic, because the Welch correction factor and the reduced denominator degrees of freedom, not the weighting alone, determine the outcome. Welch's procedure is not a device for obtaining a larger statistic.
:::

## Statistical use

### Follow-up comparisons — the Games–Howell procedure

Rejection of $H_0$ leaves open which pairs of means differ. Applying ordinary pairwise $t$ tests, or Tukey's procedure, after a Welch omnibus test reintroduces the assumption the omnibus test was chosen to avoid, because both pool the variances. The Games–Howell procedure, studied by Games and Howell in 1976 for pairwise comparisons with unequal sample sizes and unequal variances {{cite:games_howell1976}} (pp. 113–125), pools nothing. For groups $i$ and $j$, write $v_i = s_i^2 / n_i$ and $v_j = s_j^2 / n_j$ for the estimated variances of the two sample means. The pair's standard error is $\sqrt{v_i + v_j}$, its degrees of freedom are the pair-specific Welch–Satterthwaite value

$$\nu_{ij} = \frac{(v_i + v_j)^2}{v_i^2 / (n_i - 1) + v_j^2 / (n_j - 1)},$$

and its statistic is referred not to a $t$ distribution but to the studentised range distribution for $k$ groups on $\nu_{ij}$ degrees of freedom, which is what charges the procedure for examining all pairs rather than one pre-specified pair {{cite:games_howell1976}} (pp. 113–125). Each pair therefore has its own degrees of freedom. In the worked example above, the three pair-specific values are $\nu_{12} \approx 6.4615$, $\nu_{13} \approx 8.8608$ and $\nu_{23} \approx 9.1773$, all well below the $14$ error degrees of freedom a pooled procedure would have used for every pair. The corresponding simultaneous confidence intervals have the form of a mean difference plus or minus a studentised-range critical value, for $k$ groups and that pair's $\nu_{ij}$, multiplied by $\sqrt{(v_i + v_j)/2}$. Because the calibration is itself approximate — a studentised range referred to estimated, pair-specific degrees of freedom — Games–Howell intervals and tests should be reported with their degrees of freedom, and their familywise error control should be described as approximate.

Two limits deserve emphasis. First, Games–Howell is a follow-up to a mean comparison: it inherits the normality sensitivity of the underlying mean estimates, and with very small groups its pair-specific degrees of freedom can be so low that no comparison has useful power. Second, performing Games–Howell comparisons only after a significant omnibus result, and performing them unconditionally, are different procedures with different error properties; which was done should be stated.

**When to use it.** Welch's ANOVA is the appropriate omnibus test of equal means for $k$ independent groups when a common population variance is not assumed — because the design gives no reason to expect one, because the groups are known to differ in spread, or because group sizes are unequal and even moderate heterogeneity would then distort the classic test. Tomarken and Serlin's simulations support the Welch statistic, among the alternatives they compared, as retaining its nominal error rates under heterogeneity combined with unequal group sizes {{cite:tomarken_serlin1986}} (pp. 90–99), and the review by Lix, Keselman and Keselman recommends heteroscedastic procedures over the classic $F$ in the same circumstances {{cite:lix_keselman_keselman1996}} (pp. 579–619).

**Reporting.** A complete report states $k$, the $n_j$, the group means and standard deviations, $F_W$, both degrees of freedom including the non-integer $\nu_2$, and the approximate $p$-value, and names the procedure as Welch's. Reporting only "$F(2, 8.91) = 14.27$, $p = .002$" without naming the procedure invites a reader to assume the classic test with an inexplicably fractional degrees of freedom. Software defaults differ and must be checked: in R, `oneway.test` defaults to `var.equal = FALSE` and hence to Welch's procedure, while `aov` computes the classic test {{cite:rstats_oneway2026}} (Arguments, `var.equal`).

## Assumptions and limits

**What it still assumes.** Removing the equal-variance assumption removes one assumption, not all of them. The observations must be independent within and between groups. The $F$ approximation is derived under normal sampling in each group, and although the moment-matching gives the procedure some tolerance of non-normality, strongly skewed distributions with small $n_j$ degrade both the Welch and the classic calibrations; the weights themselves are ratios involving $s_j^2$, a statistic whose own sampling variability is large under skewness and heavy tails. Each $n_j$ must be at least $2$, and a group whose sample variance is zero — all observations identical — receives an infinite weight and breaks the construction; such a group is a data problem, not a limiting case of the test. Where normality itself is untenable and the question can be reframed in terms of distributions or ranks rather than means, a rank procedure such as the [Kruskal–Wallis test](kruskal-wallis-test.qmd) answers a different, weaker null hypothesis and should be chosen for that reason, not as a drop-in replacement reporting on means.

**What it does not supply.** The test gives no estimate of any difference and no confidence interval for one; the weighted grand mean $\bar Y_w$ is a computational centre under $H_0$, not an estimate of a population quantity of independent interest, and it changes if the group variances change even when the group means do not. Effect sizes and pairwise intervals must come from the follow-up procedure. Nor does a non-significant result establish that the means are equal: with small denominator degrees of freedom — $\nu_2 \approx 8.91$ in the worked example, against the classic $14$ — the test may have little power against differences of practical size.

## Common misconceptions

**"Welch's ANOVA is the classic ANOVA with a different degrees-of-freedom adjustment."** It is not. The weights change the centre, the numerator and the statistic itself, before any degrees-of-freedom question arises. Two analyses that differ only in their reference degrees of freedom would report the same $F$; the worked example reports $14.2650$ and $6.5647$ on the same data.

**"A Levene test should be run first to decide between the classic and Welch tests."** Levene's test examines the equal-variance hypothesis {{cite:nist_levene2002}} (§1.3.5.10), but using its outcome as a switch creates a two-stage procedure calibrated as neither of its stages. Failure to reject equal variances, in particular, is not evidence that pooling is safe; it is frequently only evidence that the groups are small.

**"Welch's ANOVA assumes the variances are unequal."** It does not. It permits them to be unequal. If they are in fact equal, the procedure remains valid and loses little; the assumption it drops is an assumption, not a requirement in the opposite direction.

**"The Brown–Forsythe test and Welch's ANOVA are two names for one statistic."** They are not, as the section above shows: they differ in whether the numerator is reweighted, and "Brown–Forsythe" additionally names a test of variances that is a different procedure again {{cite:brown_forsythe1974_means}} (pp. 129–132).

**"A significant Welch result identifies the groups that differ."** It does not. It is an omnibus result over all $k$ means. Pairwise claims require a follow-up procedure with its own multiplicity calibration, such as Games–Howell.

## History

The two-sample problem came first. Welch's 1947 paper in *Biometrika* addressed the generalisation of Student's problem when several different population variances are involved, giving the approximate degrees of freedom now attached to the two-sample Welch $t$ statistic {{cite:welch1947}} (pp. 28–35); Satterthwaite had published the underlying moment-matching approximation for estimates of variance components in 1946 {{cite:satterthwaite1946}} (pp. 110–114). Welch's 1951 paper, "On the comparison of several mean values: an alternative approach", in the same journal, extended the construction from two means to $k$ means, producing the weighted statistic, correction term and denominator degrees of freedom used in this article {{cite:welch1951}} (p. 330). The paper's title is itself the statement of intent: the classic analysis of variance was not repaired but replaced, for this problem, by a statistic built from the separate variances from the outset.

The procedure was slow to become a default. Textbooks continued to present the classic test as the primary method and Welch's statistic, if at all, as a remedy to be applied after heterogeneity had been demonstrated, which inverted the logic of the two-stage problem described above. The simulation literature of the 1970s and 1980s supplied the evidence that changed the recommendation: Brown and Forsythe's 1974 small-sample study compared statistics for the equality of several means under heterogeneity {{cite:brown_forsythe1974_means}} (pp. 129–132), Games and Howell provided the matching pairwise procedure in 1976 {{cite:games_howell1976}} (pp. 113–125), and Tomarken and Serlin's 1986 comparison under specific noncentrality structures documented the classic test's failure modes when unequal variances met unequal sample sizes {{cite:tomarken_serlin1986}} (pp. 90–99). Lix, Keselman and Keselman's 1996 quantitative review consolidated that record and recommended heteroscedastic alternatives to the classic $F$ {{cite:lix_keselman_keselman1996}} (pp. 579–619). In current software the procedure is no longer an exotic option: R's `oneway.test` applies it by default {{cite:rstats_oneway2026}} (Arguments, `var.equal`).

## Connections

- [One-way analysis of variance](one-way-analysis-of-variance.qmd): the classic test of the same null hypothesis, whose pooled error mean square and exact $F$ reference under a common variance are the point of departure for everything in this article.
- [Welch interval](welch-interval.qmd): the two-sample Welch procedure for a difference of means. Welch's ANOVA with $k = 2$ reproduces its $t$ statistic squared and its Welch–Satterthwaite degrees of freedom exactly.
- [Levene's test](levene-s-test.qmd): a test of the equal-variance hypothesis itself, formed by an analysis of variance on absolute deviations. It examines the assumption Welch's ANOVA declines to make; it is not a preliminary switch for choosing between the two mean tests.
- [Kruskal–Wallis test](kruskal-wallis-test.qmd): a rank test for the one-way layout. It tests whether the groups' distributions coincide, not whether their means are equal, and is the alternative when a statement about means is not defensible.
- [F distribution](f-distribution.qmd): the reference distribution for the Welch statistic, used here as a moment-matched approximation with an estimated, generally non-integer denominator degrees of freedom, rather than as the exact law it is for the classic statistic under its assumptions.
- [Two-sample t test](two-sample-t-test.qmd): the pooled two-sample test, whose equal-variance assumption is the $k = 2$ case of the assumption examined in this article.

## Check yourself

1. Using only groups 1 and 2 of the worked example — means $10$ and $15$, sample variances $2.5$ and $8/3$, sizes $5$ and $4$ — compute Welch's two-sample $t$ statistic, and confirm that its square and its Welch–Satterthwaite degrees of freedom agree with what the $k = 2$ case of the formulas in this article gives.

::: {.callout-tip collapse="true" title="Answer"}
The estimated variance of the difference is $2.5/5 + (8/3)/4 = 0.5 + 0.6667 = 1.1667$, so $t = (10 - 15)/\sqrt{1.1667} \approx -4.6291$ and $t^2 \approx 21.4286$. For $k = 2$ the correction factor is $1$ because $2(k - 2) = 0$, and the weighted between-group sum of squares $Q$ equals $21.4286$, so $F_W = t^2$. The degrees of freedom are $\nu_2 = 1/A \approx 6.4615$, and the Welch–Satterthwaite formula $(v_1 + v_2)^2 / (v_1^2/4 + v_2^2/3)$, with $v_1 = 0.5$ and $v_2 = 0.6667$, also gives approximately $6.4615$. The two constructions coincide, as they must.
:::

2. A study has two configurations of three groups, each with the same three population variances. In configuration X the largest variance occurs in the largest group; in configuration Y the largest variance occurs in the smallest group. For which configuration is the classic $F$ test liberal, and why?

::: {.callout-tip collapse="true" title="Answer"}
Configuration Y. The classic denominator is a pooled variance dominated by the large groups. In configuration Y those large groups have the small variances, so the pooled denominator understates the variability of the group means — in particular of the small, highly variable group, whose mean is in fact imprecisely estimated but is weighted in the between-group sum of squares by its sample size alone. The $F$ ratio is therefore systematically too large under the null hypothesis, and the test rejects more often than its nominal level. In configuration X the same mechanism runs in reverse and the test is conservative.
:::

3. Three groups have weights $w_1 = 1$, $w_2 = 2$, $w_3 = 3$ and sample sizes $n_1 = n_2 = n_3 = 6$. Compute $A$, the correction factor, and $\nu_2$.

::: {.callout-tip collapse="true" title="Answer"}
The total weight is $W = 6$. Then $A = (5/6)^2/5 + (4/6)^2/5 + (3/6)^2/5 = 0.1389 + 0.0889 + 0.0500 \approx 0.2778$. The correction factor is $1 + \frac{2(1)}{8}(0.2778) \approx 1.0694$, and $\nu_2 = 8 / (3 \times 0.2778) = 9.6$. Note that $\nu_2 = 9.6$ is far below the classic denominator degrees of freedom $N - k = 15$ for these sample sizes: estimating three separate variances, one of them from a group supplying half the total weight, costs substantial reference degrees of freedom.
:::
