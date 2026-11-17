## Motivating example

An experiment compares five corn varieties, but the scientific question may be whether one parent variety differs from the average of four mutants. Testing every pair of varieties would bury that question among many comparisons. A contrast writes the intended comparison directly as a weighted difference of treatment means, then gives it an estimate and uncertainty.{{cite:nist_contrasts2002}} (§7.4.3.6, Definition and Estimation of Contrasts){{cite:dodge2008}} (p. 113, Domains and Limitations)

## Intuition

To compare two groups, subtract one mean from the other. To compare one group against the average of several, give the focal group weight $1$ and divide weight $-1$ among the others. The weights must sum to zero so that adding the same constant to every group mean leaves the comparison unchanged. This feature distinguishes a contrast from a general weighted sum of means, such as an overall average, which changes when every group shifts. The choice of weights translates a substantive question into an estimable quantity.{{cite:nist_contrasts2002}} (§7.4.3.6, Definition of contrasts and Estimation of Linear Combinations)

## Definition

For treatment means $\mu_1,\ldots,\mu_k$, a contrast is $C=\sum_{j=1}^k c_j\mu_j$ with fixed coefficients satisfying $\sum_{j=1}^k c_j=0$. The difference $\mu_1-\mu_2$ is a contrast; the mean $(\mu_1+\mu_2)/2$ is not. Multiplying every coefficient by the same nonzero constant changes the numerical scale of the contrast but not the hypothesis $C=0$. For meaningful units and interpretation, state both the coefficient vector and which direction a positive value represents.{{cite:nist_contrasts2002}} (§7.4.3.6, Definition of contrasts)

In a one-way model with independent observations, group $j$ has mean $\mu_j$, size $n_j$ and common within-group variance $\sigma^2$. The natural estimate is $\widehat C=\sum_j c_j\overline Y_{\cdot j}$. It is unbiased and has variance $\sigma^2\sum_j c_j^2/n_j$. Thus a group with fewer observations contributes more uncertainty for the same coefficient magnitude. With normal independent errors and a pooled mean square error $\mathrm{MSE}$, the estimated standard error replaces $\sigma^2$ by $\mathrm{MSE}$. {{cite:nist_contrasts2002}} (§7.4.3.6, Estimation of contrasts and Confidence Interval for a Contrast)

## Interpretation — A comparison on its own scale

For $C=(\mu_1+\mu_2)/2-\mu_3$, a positive estimate says that the average of groups 1 and 2 exceeds group 3. It does not say that *each* of the first two groups exceeds group 3. A confidence interval for $C$ carries the same units as the response, unlike its t statistic. The interval addresses the chosen weighted difference; a new choice of weights asks a new question and may require a different simultaneous-inference plan.{{cite:nist_contrasts2002}} (§7.4.3.6, Example 2 and Confidence Interval for a Contrast)

## Properties — Estimation, testing, and orthogonality

Under $H_0:C=0$ in the normal equal-variance one-way model, the standardized estimate $T=\widehat C/\sqrt{\mathrm{MSE}\sum_j c_j^2/n_j}$ has a $t_{N-k}$ distribution, where $N=\sum_j n_j$. Its square is $F_{1,N-k}$, equivalently $F=\mathrm{SS}_C/\mathrm{MSE}$ with $\mathrm{SS}_C=\widehat C^2/(\sum_j c_j^2/n_j)$. This supplies a test for a fixed contrast and a confidence interval using the same standard error. The $F$ ratio is nonnegative and has one numerator degree of freedom because the contrast asks one scalar question.{{cite:nist_contrasts2002}} (§7.4.3.6, Confidence Interval for a Contrast)

Two estimated contrasts with coefficient vectors $c$ and $d$ have covariance $\sigma^2\sum_j c_jd_j/n_j$. They are orthogonal, hence independent under the normal model, when this weighted sum is zero. If all $n_j$ are equal, this reduces to the familiar zero dot product $\sum_j c_jd_j=0$. With unequal sizes, using the unweighted dot product alone can falsely suggest independence. Orthogonal contrasts can separate distinct treatment comparisons, but independence does not mean their scientific meanings are interchangeable. {{cite:nist_contrasts2002}} (§7.4.3.6, orthogonal contrasts and estimator variance)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Linearity gives $E(\widehat C)=\sum_jc_jE(\overline Y_{\cdot j})=C$. Independent groups have $\operatorname{Var}(\overline Y_{\cdot j})=\sigma^2/n_j$, so variance and covariance of weighted sums give $\operatorname{Var}(\widehat C)=\sigma^2\sum_j c_j^2/n_j$ and $\operatorname{Cov}(\widehat C,\widehat D)=\sigma^2\sum_j c_jd_j/n_j$. If all treatment means rise by $a$, the contrast rises by $a\sum_jc_j=0$, proving its common-shift invariance.

For normal independent errors, the group means are jointly normal and independent of the pooled within-group sum of squares. Under $C=0$, dividing $\widehat C/\{\sigma\sqrt{\sum c_j^2/n_j}\}$ by the independent square root of $\mathrm{MSE}/\sigma^2$ gives $t_{N-k}$; squaring gives $F_{1,N-k}$. The argument assumes the coefficients are fixed independently of the responses used in the test. {{cite:nist_contrasts2002}} (§7.4.3.6, group-mean variance and contrast interval)
:::
:::

## Statistical use — Plan the question and the family

Choose coefficients from the experimental question, keeping the unit and direction legible. For a parent versus the average of four mutants, use $(-1/4,-1/4,1,-1/4,-1/4)$ if the parent is group 3 and a positive value means the parent yields more. Choosing only the largest-looking contrast after inspecting the same data changes the selection procedure: an unadjusted single-test p-value or interval no longer covers that search. Scheffé's method supplies simultaneous intervals over all contrasts; Tukey's method is tailored to pairwise comparisons. The method should match the set of comparisons the analysis will make.{{cite:nist_scheffe2002}} (§7.4.7.2, Scheffé's method and Comparison with Tukey's Method){{cite:dodge2008}} (p. 113, History)

For the five-variety corn data, the planned parent-versus-mutants estimate using the mutant-minus-parent direction is $(48.93+55.07+48.30+51.93)/4-59.80=-8.7425$, printed as $-8.74$. With three plots per variety, $\sum c_j^2/n_j=(4/16+1)/3=0.4167$; using $\mathrm{MSE}=10.57$ gives $F\approx17.4$ on $(1,10)$ degrees of freedom and $p\approx0.002$. The negative sign says variety 3 yielded more than the mutant average. The question-page comparison of variety 2 against the average of varieties 1 and 4 remains a different contrast of the same data. {{cite:nist_contrasts2002}} (§7.4.3.6, contrast test construction)

If one fertilizer has much larger response variance, pooling a common $\mathrm{MSE}$ may misstate the contrast standard error. If plots in the same field block are correlated, treating all observations as independent also misstates it. If the analyst tests every contrast suggested by the observed means and reports only the most extreme unadjusted p-value, the nominal single-comparison error rate no longer describes the selection. A planned contrast, a covariance model suited to the design, and an appropriate multiple-comparison procedure address different parts of these failures.{{cite:nist_contrasts2002}} (§7.4.3.6, one-way ANOVA model and MSE){{cite:nist_scheffe2002}} (§7.4.7.2, all-contrast coverage)
## Worked example

Suppose three fertilizer groups each have $n_j=4$ plots, with mean yields $12$, $15$ and $18$ kilograms, and a pooled $\mathrm{MSE}=9$ square kilograms. Compare the third fertilizer with the average of the first two using $c=(-1/2,-1/2,1)$. The estimate is $\widehat C=18-(12+15)/2=4.5$ kilograms. The variance multiplier is $\sum c_j^2/n_j=(1/4+1/4+1)/4=0.375$, giving standard error $\sqrt{9(0.375)}\approx1.8371$. The t statistic is $4.5/1.8371\approx2.4495$ on $N-k=9$ degrees of freedom. Its square is $F=6$ on $(1,9)$ degrees of freedom. The estimate describes a yield advantage of $4.5$ kilograms for the third group over the average of the first two; uncertainty about that advantage still matters.{{cite:nist_contrasts2002}} (§7.4.3.6, Estimation of contrasts and Confidence Interval)

**Your turn.** With the same three means and group sizes, compare fertilizer 2 with fertilizer 1. Give the coefficient vector, estimated difference, variance multiplier, standard error using the same MSE, and t statistic.

::: {.callout-tip collapse="true" title="Answer"}
Use $c=(-1,1,0)$, whose coefficients sum to zero. The estimate is $15-12=3$ kilograms. The variance multiplier is $(1+1)/4=0.5$, so the standard error is $\sqrt{9(0.5)}=\sqrt{4.5}\approx2.1213$ kilograms. The t statistic is $3/2.1213\approx1.4142$ on $9$ degrees of freedom. This pairwise comparison differs from the third-versus-average question in both estimate and precision.
:::

## Common misconceptions

Coefficients that merely add to one form an average, not necessarily a contrast; a contrast's coefficients add to zero. The sign of a contrast depends on which group receives positive weight, while a two-sided test of zero is unchanged by reversing all signs. Orthogonality of raw coefficient vectors implies independent normal contrast estimates only when group sizes are equal or the appropriate weighted condition holds. Finally, a fixed contrast remains mathematically defined after seeing data, but inference that ignores the search used to select it can overstate evidence.{{cite:nist_contrasts2002}} (§7.4.3.6, definition and orthogonality){{cite:nist_scheffe2002}} (§7.4.7.2, simultaneous intervals)

## Connections

[One-way analysis of variance](one-way-analysis-of-variance.qmd) asks whether the means differ somewhere; a contrast names a particular difference. [ANOVA F distribution](anova-f-distribution.qmd) calibrates the squared t statistic under the stated model. [Tukey intervals](tukey-intervals.qmd) focus on pairwise comparisons, while [multiple comparisons](multiple-comparisons.qmd) address a family of questions. [Main effects](main-effect.qmd) and [sum-to-zero constraints](sum-to-zero-and-contrast-constraints.qmd) also use weighted comparisons of means, though model coding and a scientific contrast have different roles.{{cite:nist_contrasts2002}} (§7.4.3.6){{cite:nist_scheffe2002}} (§7.4.7.2)

## History

Contrasts grew with analysis of variance as a way to express comparisons among treatment means, including more than pairwise differences. Dodge's encyclopedia links the subject to Tukey's and Scheffé's work on simultaneous comparisons in the mid-twentieth century. The modern distinction remains useful: NIST presents a single contrast with its own t interval, then Scheffé intervals that cover an entire family of possible contrasts.{{cite:dodge2008}} (p. 113, History){{cite:nist_contrasts2002}} (§7.4.3.6, Confidence Interval for a Contrast){{cite:nist_scheffe2002}} (§7.4.7.2, simultaneous confidence interval)
