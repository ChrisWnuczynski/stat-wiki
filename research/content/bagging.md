## Motivating example

A deep regression tree can choose a different first split after a small change in the training data. Predictions at a particular input can then vary substantially across fitted trees. Bagging averages predictions after repeatedly perturbing the data by sampling with replacement. This targets sensitivity of the fitted rule to the particular training sample.{{cite:breiman1996_bagging}} (§1)

## Definition — Bootstrap aggregation

From $n$ observed cases, draw $n$ cases independently with replacement to form each bootstrap sample. Fit the same learning procedure separately to each sample. For a numeric response, average the predictions; for class labels, specify a voting or probability-averaging rule. Bagging changes training rows. Random forests add random feature selection, and boosting changes the subsequent fitting problem in response to the ensemble so far. These mechanisms create different ensembles.{{cite:dietterich2000_ensembles}} (§2.2, Bagging)

## Properties — Two sources of variation

Condition on the observed training data $D$. If independently generated bootstrap fits have predictions $F_1(x),\ldots,F_B(x)$ with conditional mean $m_D$ and variance $v_D$, then
$$
E(\bar F_B\mid D)=m_D,\qquad
\operatorname{Var}(\bar F_B\mid D)=v_D/B.
$$
That reduction concerns Monte Carlo variation from generating a finite ensemble. Across new training datasets, the infinite-ensemble prediction $m_D$ still varies. By total variance,
$$
\operatorname{Var}(\bar F_B)=\operatorname{Var}(m_D)+E(v_D)/B.
$$
Adding trees removes the second contribution, not the sampling variation of $m_D$. The bootstrap approximation to ideal repeated-sample aggregation can also change bias, so bias preservation is not a general guarantee of bagging.{{cite:breiman1996_bagging}} (§4)

Under the different unconditional simplification that each member has variance $\sigma^2$ and pairwise correlation $\rho$, expansion of the variance of the sum gives
$$
\operatorname{Var}(\bar F_B)=\sigma^2\left[\rho+\frac{1-\rho}{B}\right].
$$
This identity explains why copying a fitted predictor adds no information and why diversity among predictions matters. Classification error is a nonlinear function of the votes; a variance identity alone is not a universal theorem that voting improves classification.{{cite:dietterich2000_ensembles}} (§1, pp. 1–3)

## Worked example

Suppose member predictions each have variance nine and pairwise correlation $0.2$. With twenty-five members, the average has variance $9[0.2+0.8/25]=2.088$. With one hundred members, it is $1.872$. Its limiting variance is $1.8$, so the second increase in ensemble size has a smaller benefit.

For a bootstrap sample from ten cases, a particular case is omitted with probability $(9/10)^{10}\approx0.348678$. The expected number of distinct included cases is $10[1-(9/10)^{10}]\approx6.51322$. Repeated draws can therefore produce ten rows with fewer than ten distinct observed cases. The resampling construction is the one used for bootstrap aggregation.{{cite:breiman1996_bagging}} (§1)

**Your turn.** In the variance calculation, set $\rho=1$ while keeping member variance nine. What does averaging achieve?

::: {.callout-tip collapse="true" title="Answer"}
The variance stays nine for every ensemble size. With perfectly correlated equal-variance predictions, the covariance terms exactly offset the apparent gain from averaging individual variances.
:::

## Statistical use — Out-of-bag assessment

For a particular training case, predictions can be formed from only those bootstrap models whose samples omitted that case. This out-of-bag prediction uses the case as an assessment point for those models. Reusing the same assessment repeatedly to choose tuning settings can make the selected error optimistic; independent assessment still has a role after extensive model selection.{{cite:breiman2001_rf}} (§3.1, p. 11)
