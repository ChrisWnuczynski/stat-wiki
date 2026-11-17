## Motivating example
Two regression models may make errors in opposite directions on the same case. Their average can then be closer to the outcome than either model. Squared error admits an exact identity connecting the average prediction's error with the members' average error and their disagreement. No independence or normality assumption is needed for this pointwise algebra.{{cite:goodfellow_bengio_courville2016}} (§7.11, ensemble averaging)

## Statement
For predictions $f_1,\ldots,f_T$, let $\bar f=T^{-1}\sum_tf_t$. For any outcome $y$,
$$(\bar f-y)^2=\frac1T\sum_t(f_t-y)^2-\frac1T\sum_t(f_t-\bar f)^2.$$
The last term is the empirical second centred moment of the predictions, with divisor $T$. It differs from the unbiased sample-variance estimator with divisor $T-1$. Calling both simply “sample variance” can hide that factor. The identity is true for fixed numbers, whether or not the models were trained by the same procedure.{{cite:siegrist2022_sample_variance}} (§6.05, the two sample-variance conventions)

## Proof
Insert $f_t-y=(f_t-\bar f)+(\bar f-y)$ into each squared member error. The averaged cross term is $2(\bar f-y)T^{-1}\sum_t(f_t-\bar f)=0$. The remaining terms are the average squared deviation from $\bar f$ and $(\bar f-y)^2$. Rearranging gives the statement. Its subtraction term is non-negative, so the ensemble's squared error is at most the members' average squared error on the same case. This inequality compares with their average error; a particularly accurate member can still beat the ensemble.{{cite:siegrist2022_sample_variance}} (§6.05, centred sum-of-squares identity)

## Generalizations — Non-negative weights give a weighted identity
For weights $w_t\ge0$ summing to one and weighted prediction $f_w=\sum_tw_tf_t$, the same expansion gives
$$(f_w-y)^2=\sum_tw_t(f_t-y)^2-\sum_tw_t(f_t-f_w)^2.$$
The weights make the cross term vanish because $\sum_tw_t(f_t-f_w)=0$. If weights can be negative, the equality remains algebraically true when their sum is one, but the last expression need not be non-negative and the corresponding convex-averaging inequality can fail. This separates an equality from the assumption needed to read it as an improvement bound.

## Worked example
### Three models around one response
Let predictions be $1,4,7$ and outcome $y=5$. Their mean is $4.000$ and its squared error is $1.000$. Member squared errors are $16,1,4$, averaging $7.000$. Their squared deviations from the ensemble mean are $9,0,9$, averaging $6.000$. Thus the identity reads $1=7-6$. The model predicting four ties the ensemble here; averaging is not a guarantee of beating the best model on every case.

Use instead weights $(1/4,1/2,1/4)$. The weighted prediction is still $4.000$, the weighted member error is $5.500$, and the weighted disagreement is $4.500$. The equality becomes $1=5.5-4.5$. The change in weights changes the two terms on the right together, rather than supplying a free diversity gain.{{cite:goodfellow_bengio_courville2016}} (§7.11, averaging regression predictions)

**Your turn.** All three models predict six and the outcome is five. What are the ensemble error, average member error and disagreement term?

::: {.callout-tip collapse="true" title="Answer"}
The ensemble and every member have squared error $1.000$. Their disagreement term is $0.000$, so the identity reads $1=1-0$.
:::

## Statistical use — Pointwise disagreement and expected ensemble risk
For random member errors $e_t=f_t(X)-Y$, averaging also gives $E[(T^{-1}\sum_te_t)^2]=T^{-2}\sum_{s,t}E(e_se_t)$ when the second moments exist. Under a common zero error mean, common variance $v$ and common covariance $c$, this reduces to $v/T+(T-1)c/T$. The cross-covariances describe shared errors; adding more highly correlated models cannot remove them merely by increasing $T$.{{cite:goodfellow_bengio_courville2016}} (§7.11, eqs. 7.50–7.51)

For $v=4$, $c=1$ and $T=10$, the expected squared error is $1.300$. If the errors were uncorrelated with the same variance, it would be $0.400$. These are comparisons under explicitly specified joint error moments, rather than numerical predictions for every fitted ensemble. Bias can also contribute when the zero-mean assumption is dropped; the general cross-product formula remains the reliable starting point.{{cite:goodfellow_bengio_courville2016}} (§7.11, correlated and uncorrelated model errors)

## Common misconceptions — Diversity cannot be purchased independently of accuracy
Replacing a sensible model with an erratic one can increase disagreement and increase average member error by even more. The identity subtracts one changing quantity from another; it does not prescribe maximising disagreement alone. Assess the entire ensemble on held-out observations appropriate to the prediction target, and keep any weight selection separate from the data used to evaluate it. The choice of averaging scheme is part of the fitted prediction procedure.{{cite:goodfellow_bengio_courville2016}} (§7.11, ensemble construction)
