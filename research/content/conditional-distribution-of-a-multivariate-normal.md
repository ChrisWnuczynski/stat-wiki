## Motivating example
Suppose two calibrated measurements describe the same system, but only one is observed for a new case. A joint normal model gives more than a best linear prediction of the missing measurement: it gives its whole conditional distribution. The observed value moves the conditional centre, while the covariance describes the uncertainty left after using that observation. This is the basis of Gaussian prediction and a useful building block for imputation.{{cite:majumdar_majumdar2019}} (§1, block conditional distribution)

## Statement
Partition a jointly normal vector as $(X_A,X_B)$ with means $(\mu_A,\mu_B)$ and covariance blocks $\Sigma_{AA},\Sigma_{AB},\Sigma_{BA},\Sigma_{BB}$. If $\Sigma_{BB}$ is invertible, a version of the conditional law is normal with
$$m_A(b)=\mu_A+\Sigma_{AB}\Sigma_{BB}^{-1}(b-\mu_B),\qquad S_A=\Sigma_{AA}-\Sigma_{AB}\Sigma_{BB}^{-1}\Sigma_{BA}.$$
The formula conditions on the whole block $B$. The cross-covariance appears with its transpose in the opposite block because the joint covariance is symmetric. The conditional covariance can be singular even when the conditioning covariance is invertible.{{cite:majumdar_majumdar2019}} (§1, block partition formula; §3, Theorem 4)

## Proof
Put $C=\Sigma_{AB}\Sigma_{BB}^{-1}$ and define $Z=X_A-\mu_A-C(X_B-\mu_B)$. This is a linear transformation of a normal vector and hence jointly normal with $X_B$. Its cross-covariance is $\Sigma_{AB}-C\Sigma_{BB}=0$. For a joint normal law, block-diagonal covariance makes the characteristic function factor into the two marginal characteristic functions, giving independence. Its covariance is $\Sigma_{AA}-\Sigma_{AB}\Sigma_{BB}^{-1}\Sigma_{BA}$. Conditional on $X_B=b$, the identity $X_A=m_A(b)+Z$ therefore gives the claimed normal law. This argument also handles a degenerate residual covariance.{{cite:majumdar_majumdar2019}} (§3, linear transformation and independent decomposition)

## Key results — Conditioning removes a positive-semidefinite term
For any vector $a$, the reduction in variance is
$$a^\top(\Sigma_{AA}-S_A)a=(\Sigma_{BA}a)^\top\Sigma_{BB}^{-1}(\Sigma_{BA}a)\ge0.$$
Thus conditioning cannot increase covariance in the positive-semidefinite order for this family. The covariance does not depend on the observed value $b$. These features use joint normality: a generic joint distribution need not have a normal conditional law, a linear conditional mean or a constant conditional covariance.{{cite:goodfellow_bengio_courville2016}} (§3.9.3, multivariate Gaussian density and covariance)

Zero cross-covariance makes the two blocks independent for a joint normal law. For arbitrary distributions, zero covariance only excludes linear association and does not establish independence. That limitation matters when using Gaussian conditional formulas as an approximation.{{cite:goodfellow_bengio_courville2016}} (§§3.7–3.8, independence and covariance)

## Worked example
### A two-dimensional update
Let $\mu_A=1$, $\mu_B=2$, variances $\Sigma_{AA}=4$ and $\Sigma_{BB}=9$, and cross-covariance $3$. Given $X_B=5$, the conditional mean is $1+(3/9)(5-2)=2$ and conditional variance is $4-3^2/9=3$. Hence $X_A\mid X_B=5\sim N(2,3)$. If the observed value changes to $X_B=-1$, the conditional mean becomes zero while the variance stays three. Both conditional standard deviations are $\sqrt3$; the second parameter of $N(2,3)$ denotes variance here.{{cite:majumdar_majumdar2019}} (§1, conditional mean and covariance)

**Your turn.** In that example, what happens to the conditional law if the cross-covariance is zero instead?

::: {.callout-tip collapse="true" title="Answer"}
The conditional mean stays 1 and the conditional variance stays 4, regardless of the observed value of $X_B$. The blocks are independent.
:::

## Generalizations — Singular conditioning needs a support condition
With a singular conditioning covariance, a generalised inverse can describe a conditional law on the support of $X_B$. Values outside that support are not determined by the joint probability model, and different versions can disagree there. The nonsingular formula avoids this complication, while the independent-decomposition approach extends to the singular case with the relevant linear-algebra conditions.{{cite:majumdar_majumdar2019}} (§§1, 3, Theorem 4)


## Statistical use — Predict a block using its measured companions
The conditional mean supplies a point prediction for one vector block after another is observed. Its conditional covariance describes the uncertainty left after using those observations, rather than the marginal spread before conditioning. In the nonsingular Gaussian model this covariance does not depend on the observed numerical conditioning value. Predictions at different values therefore move the conditional mean while preserving the same conditional covariance. These conclusions use the joint Gaussian model as well as the block covariance calculation.{{cite:majumdar_majumdar2019}} (§1, conditional block formulas)

## Intuition
A joint normal model ties two blocks together by a covariance and by nothing more complicated than a linear rule. Once $X_B$ is observed, the conditional mean of $X_A$ moves away from $\mu_A$ by a matrix multiple of $b-\mu_B$. The multiple is the regression coefficient $\Sigma_{AB}\Sigma_{BB}^{-1}$. The conditional covariance subtracts the variance that this linear function of $X_B$ has explained. What remains does not depend on the numerical value $b$. Different observations shift the centre and share the residual spread. That constancy is a property of the Gaussian family. A generic joint distribution can have a conditional variance that widens in the tails and a conditional mean that curves.

In the worked numbers, $\Sigma_{AA}=4$, $\Sigma_{BB}=9$ and the cross-covariance is $3$. The correlation is $3/\sqrt{4\cdot 9}=1/2$. The fraction of variance removed by the regression is the squared correlation, so the conditional variance is $4(1-1/4)=3$, matching $4-3^2/9=3$. The conditional law given $X_B=5$ is $N(2,3)$, where the second parameter is the variance. The conditional standard deviation is $\sqrt 3$, not $3$. Given $X_B=11$ the same slope $3/9=1/3$ produces conditional mean $1+(1/3)(11-2)=4$, and the variance is still $3$.

## Related concepts — The residual is uncorrelated with the conditioner
Define $Z=X_A-\mu_A-\Sigma_{AB}\Sigma_{BB}^{-1}(X_B-\mu_B)$. Joint normality is preserved by this linear map, and the cross-covariance between $Z$ and $X_B$ is zero by construction of the coefficient. For a multivariate normal vector, a zero cross-covariance between two blocks implies independence, so $Z$ is independent of $X_B$. Conditioning on $X_B=b$ therefore leaves $Z$ with its unconditional law, which is normal with mean zero and covariance $S_A$. Adding back the fitted value $m_A(b)$ gives the conditional law of $X_A$.

The same algebra shows that conditioning cannot increase variance in the positive-semidefinite order. For every vector $a$,
$$a^\top(\Sigma_{AA}-S_A)a=(\Sigma_{BA}a)^\top\Sigma_{BB}^{-1}(\Sigma_{BA}a)\ge 0,$$
because $\Sigma_{BB}^{-1}$ is positive definite when $\Sigma_{BB}$ is invertible. Equality holds for a particular $a$ when $\Sigma_{BA}a=0$, that is, when that linear combination of $X_A$ is uncorrelated with $X_B$. Zero cross-covariance of the whole blocks makes $S_A=\Sigma_{AA}$ and makes the conditional mean ignore $b$. For non-Gaussian joints, zero covariance does not yield independence, and the conditional law need not be normal.{{cite:goodfellow_bengio_courville2016}} (§§3.7–3.8, independence and covariance)

## Common misconceptions
The formula conditions on the entire block $B$. Conditioning on one coordinate of a longer block is a different calculation, with a different residual covariance. Substituting a subvector into the full-block formula uses the wrong regression coefficient. The order of the variables inside each block has to match the order of the covariance blocks.

A singular $\Sigma_{BB}$ means some linear combination of the conditioning variables is constant. Values of $b$ off that hyperplane have probability zero under the joint model. A generalised inverse can describe a conditional law on the support. It does not assign a conditional distribution to an impossible $b$ in a way that the joint probability determines. The nonsingular numerical example, with $\Sigma_{BB}=9$, avoids that case. A reported conditional variance larger than the marginal variance $4$ would contradict the positive-semidefinite reduction and would signal an arithmetic error in the Schur complement.

The conditional mean is the population linear regression of $X_A$ on $X_B$. The residual covariance $S_A$ is the population mean squared error of that regression. Sample analogues replace $\Sigma$ by a sample covariance and inherit the same algebra when the sample covariance of the regressors is invertible. Gaussian graphical models factor a precision matrix rather than a covariance, and the zeros in that precision matrix are conditional independences given the remaining coordinates. Those zeros are not zeros of $\Sigma$. A zero conditional covariance in $S_A$ after conditioning on a block is the Schur complement statement above. It is the graphical-model statement when the block is the rest of the vector.{{cite:majumdar_majumdar2019}} (§1, block partition formula; §3, Theorem 4)
