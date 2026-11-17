## Lead context
Delete-one estimates measure how a statistic changes when each observation is omitted; their spread also supports a bias correction.

## Motivating example
A statistic may have no convenient standard-error formula, yet be easy to recompute after deleting one observation. The jackknife turns those recomputations into a sensitivity calculation. It is particularly natural for smooth functions of empirical averages, where deletion approximates a derivative with respect to observation weights.{{cite:efron1979}} (§5, pp. 12–14)

## Definition — Deletions, pseudovalues and two estimates
For $n\ge2$, let $\widehat\theta$ use all observations and $\widehat\theta_{(i)}$ omit observation $i$. Define $\overline\theta_{(-)}=n^{-1}\sum_i\widehat\theta_{(i)}$. The usual delete-one estimates are
$$
\widehat b_J=(n-1)(\overline\theta_{(-)}-\widehat\theta),\qquad
\widehat V_J=\frac{n-1}{n}\sum_i(\widehat\theta_{(i)}-\overline\theta_{(-)})^2.
$$
The estimated standard error is $\sqrt{\widehat V_J}$, while the bias-corrected estimate is $\widehat\theta_J=\widehat\theta-\widehat b_J$. These are different uses of the same deletions.{{cite:dodge2008}} (pp. 271–272){{cite:efron1979}} (§5, pp. 13–14)

The pseudovalue for observation $i$ is $P_i=n\widehat\theta-(n-1)\widehat\theta_{(i)}$. Its average equals $\widehat\theta_J$, and
$$
\widehat V_J=\frac1{n(n-1)}\sum_i(P_i-\overline P)^2.
$$
The pseudovalues are generally dependent; writing the formula as a variance of their average does not make them independent observations.{{cite:dodge2008}} (pp. 271–272)

## Properties — What the expansion must control
Suppose an iid-sample statistic has the regular expectation expansion
$$
E(\widehat\theta_n)=\theta+\frac an+\frac b{n^2}+O(n^{-3}).
$$
Each deletion has the distribution of the statistic at sample size $n-1$. Thus
$$
E(\widehat\theta_J)=nE(\widehat\theta_n)-(n-1)E(\widehat\theta_{n-1})=\theta+O(n^{-2}).
$$
The constant $a$ cancels exactly. The displayed remainder control matters: a bare $o(n^{-1})$ remainder, multiplied by $n$ in this difference, does not itself establish second-order bias. Nor does removing leading bias necessarily reduce mean squared error, since variance may increase.{{cite:dodge2008}} (pp. 271–272){{cite:efron1979}} (§5, pp. 12–14)

## Assumptions and limits — Deletion is a local perturbation
For a statistic that is smooth in empirical observation weights, deleting a point approximates a directional derivative. The jackknife variance therefore parallels a first-order Taylor approximation to resampling variation. Statistics with abrupt responses to deletions, including sample quantiles in some settings, need separate analysis; a successful formula for a sample mean does not establish validity for every statistic.{{cite:efron1979}} (§1, p. 1; §5, pp. 12–14)

Dependence among observations also changes the resampling unit. Deleting one correlated measurement while treating all others as independent does not automatically estimate the variability of an independent-cluster estimator. The deletion scheme and the estimator's sampling model must agree.{{cite:dodge2008}} (pp. 271–272, grouped jackknife)

## Worked example
For data $(1,2,4,5)$, let $\widehat\theta=\bar x^2=9$. The four deleted means are $11/3,10/3,8/3,7/3$, so the deleted squared means average $167/18$. The estimated bias is
$$
3\left(\frac{167}{18}-9\right)=\frac56,
$$
and the corrected estimate is $49/6\approx8.166667$. In this example the correction has a direct interpretation. If the data are iid with finite variance, $E(\bar X^2)=\mu^2+\sigma^2/n$, and the unbiased sample variance estimates $\sigma^2$. Algebra gives $\widehat\theta_J=\bar x^2-s^2/n$. Here $s^2=10/3$, recovering the same correction.{{cite:dodge2008}} (pp. 271–272)

For the sample mean itself, the deleted estimates average $\bar x$ and the jackknife bias estimate is zero. Substitution into the variance formula gives $s^2/n=5/6$, hence standard error $\sqrt{5/6}\approx0.912871$. The nonlinear statistic and the mean respond differently to deletion despite using the same observations.{{cite:efron1979}} (§5, pp. 13–14)

**Your turn.** Translate every observation by $10$. Does the jackknife bias estimate for the squared mean change?

::: {.callout-tip collapse="true" title="Answer"}
The sample variance is unchanged, so the estimated bias remains $s^2/n=5/6$. The squared mean becomes $13^2=169$, and its corrected value is $169-5/6=1009/6\approx168.166667$.
:::

