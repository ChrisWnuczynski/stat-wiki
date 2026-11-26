## Motivating example
Two regression models may make errors in opposite directions on the same case. Their average can then be closer to the outcome than either model. Squared error admits an exact identity connecting the average prediction's error with the members' average error and their disagreement. No independence or normality assumption is needed for this pointwise algebra.{{cite:goodfellow_bengio_courville2016}} (§7.11, ensemble averaging)

## Statement
For predictions $f_1,\ldots,f_T$, let $\bar f=T^{-1}\sum_tf_t$. For any outcome $y$,
$$(\bar f-y)^2=\frac1T\sum_t(f_t-y)^2-\frac1T\sum_t(f_t-\bar f)^2.$$
The last term is the empirical second centred moment of the predictions, with divisor $T$. It differs from the unbiased sample-variance estimator with divisor $T-1$. Calling both simply “sample variance” can hide that factor. The identity is true for fixed numbers, whether or not the models were trained by the same procedure.

## Proof
Insert $f_t-y=(f_t-\bar f)+(\bar f-y)$ into each squared member error. The averaged cross term is $2(\bar f-y)T^{-1}\sum_t(f_t-\bar f)=0$. The remaining terms are the average squared deviation from $\bar f$ and $(\bar f-y)^2$. Rearranging gives the statement. Its subtraction term is non-negative, so the ensemble's squared error is at most the members' average squared error on the same case. This inequality compares with their average error; a particularly accurate member can still beat the ensemble.

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
For random member errors $e_t=f_t(X)-Y$, averaging also gives $\E[(T^{-1}\sum_te_t)^2]=T^{-2}\sum_{s,t}\E(e_se_t)$ when the second moments exist. Under a common zero error mean, common variance $v$ and common covariance $c$, this reduces to $v/T+(T-1)c/T$. The cross-covariances describe shared errors; adding more highly correlated models cannot remove them merely by increasing $T$.{{cite:goodfellow_bengio_courville2016}} (§7.11, eqs. 7.50–7.51)

For $v=4$, $c=1$ and $T=10$, the expected squared error is $1.300$. If the errors were uncorrelated with the same variance, it would be $0.400$. These are comparisons under explicitly specified joint error moments, rather than numerical predictions for every fitted ensemble. Bias can also contribute when the zero-mean assumption is dropped; the general cross-product formula remains the reliable starting point.{{cite:goodfellow_bengio_courville2016}} (§7.11, correlated and uncorrelated model errors)

## Common misconceptions — Diversity cannot be purchased independently of accuracy
Replacing a careful model with an erratic one can raise disagreement and raise the average member error by more than the disagreement rose. The identity subtracts the disagreement term from the average member error. Maximising disagreement alone is a different objective from minimising ensemble squared error. The ensemble is scored on observations that were not used to choose its weights, and the averaging rule is part of the fitted procedure.{{cite:goodfellow_bengio_courville2016}} (§7.11, ensemble construction)

## Intuition — The cross term vanishes because the residuals from the average sum to zero
Write each member error as the sum of the ensemble error and the member's deviation from the ensemble. Squaring and averaging, the cross term is twice the ensemble error times the average deviation from the ensemble. That average deviation is zero by the definition of an arithmetic mean, so the cross term drops. What remains is the identity
$$
(\bar f-y)^2=\frac1T\sum_t(f_t-y)^2-\frac1T\sum_t(f_t-\bar f)^2.
$$
The second term uses the divisor $T$. For the predictions $1,4,7$ it equals $6.000$, while the unbiased sample variance of those three numbers, with divisor $T-1=2$, equals $9.000$. Both summaries describe the same spread. They answer different normalisations, and the ensemble identity is the one with divisor $T$.

Four constant predictions $2,2,2,6$ of an outcome $3$ have ensemble mean $3.000$ and ensemble squared error $0$. The member squared errors average $3.000$ and the disagreement term averages $3.000$, so the identity reads $0=3-3$. The ensemble lands on the outcome because the members straddle it. A single member that predicted $3$ would also have had squared error $0$; the identity compares the ensemble with the average member, and the best member can still match the ensemble on a given case.

## Key results — Weights have to stay non-negative for the inequality
If the weights are non-negative and sum to one, the weighted disagreement $\sum_t w_t(f_t-f_w)^2$ is non-negative, and the weighted ensemble squared error is at most the weighted average of the member squared errors. The worked weights $(1/4,1/2,1/4)$ give weighted member error $5.500$, weighted disagreement $4.500$ and ensemble squared error $1.000$. Weights that sum to one and take a negative value keep the algebraic identity and can make the disagreement expression negative, so the inequality can fail. The sign restriction is what turns an equality into a guarantee that averaging helps relative to the weighted members.

For random errors with common variance $v$, common covariance $c$ and mean zero, the expected squared error of the equal-weight ensemble is $v/T+(T-1)c/T$. With $v=4$, $c=1$ and $T=10$ this equals $1.300$. Uncorrelated errors with the same variance would give $4/10=0.400$. The gap $0.900$ is the contribution of the shared covariance, and adding further copies of a model that makes the same errors does not drive that term to zero.{{cite:goodfellow_bengio_courville2016}} (§7.11, eqs. 7.50–7.51)

## Related concepts
The divisor distinction is the same distinction as in the two conventions for a sample variance. The ensemble formula is an algebraic identity for a list of numbers, in force whether or not those numbers are a random sample. The risk formula $v/T+(T-1)c/T$ adds a probability model for the member errors. Reporting which of the two statements is in use keeps a pointwise decomposition separate from an expectation over a joint error distribution.{{cite:goodfellow_bengio_courville2016}} (§7.11, correlated and uncorrelated model errors)
