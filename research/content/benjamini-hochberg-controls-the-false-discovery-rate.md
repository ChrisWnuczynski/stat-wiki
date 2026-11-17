## Motivating example — Control the expected fraction of false discoveries
When many hypotheses are screened, a researcher may be willing to tolerate some false calls while controlling their expected proportion in the rejected list. That criterion differs from controlling the probability of making even one false call. The latter is the family-wise error rate targeted by methods such as Bonferroni. The criterion should follow the scientific decision before a multiple-testing procedure is chosen.{{cite:nist_bonferroni2002}} (§7.4.7.3); {{cite:blanchard_roquain2009}} (§2.2, Definition 1)

## Statement
Order $m$ p-values as $p_{(1)}\le\cdots\le p_{(m)}$. For $0<q<1$, the linear step-up procedure takes $R=\max\{r:p_{(r)}\le qr/m\}$, or $R=0$ if the set is empty, and rejects the first $R$ hypotheses. If all p-values are mutually independent and every true-null p-value is super-uniform, then
$$E\left\{\frac{V}{R\vee1}\right\}\le\frac{m_0}{m}q.$$
For exactly uniform null p-values, the expectation equals $(m_0/m)q$. The number $m_0$ is the unknown count of true null hypotheses and $V$ counts their rejections.{{cite:blanchard_roquain2009}} (§2.3, Definition 4 and Theorem 6)

## Proof
Fix a true null index $i$, and let $R_i^0$ be the rejection count when its p-value is replaced by zero. It depends only on the other p-values and is at least one. The step-up rule implies that $i$ is rejected precisely when $p_i\le qR_i^0/m$; on that event the rejection count equals $R_i^0$. Lowering an already rejected p-value cannot change feasibility at any larger step, since it was already below all those larger thresholds. Conversely, raising zero to a value below the $R_i^0$ threshold preserves that feasible step and cannot create a larger one.

Conditional on the other p-values, independence and super-uniformity give
$$E\left\{\frac{\mathbf1\{i\text{ rejected}\}}{R\vee1}\Bigm|p_{-i}\right\}=\frac{\Pr(p_i\le qR_i^0/m)}{R_i^0}\le\frac qm.$$
Summing this inequality over the $m_0$ true nulls proves the result. Exactly uniform null p-values turn each inequality into equality. The argument uses the joint independence assumption when conditioning on the other p-values.{{cite:blanchard_roquain2009}} (§2.3, Theorem 6; §6, independent-p-value arguments)

## Worked example — A step-up crossing can follow a failed step
For five p-values $(0.004,0.018,0.021,0.06,0.4)$ and $q=0.05$, the thresholds are $(0.01,0.02,0.03,0.04,0.05)$. The largest crossing is at rank three, so the first three hypotheses are rejected. This procedure uses the largest crossing; it is not a rule that stops at the first p-value exceeding its threshold. The observed false-discovery proportion cannot be calculated from these p-values alone because the true null statuses are unknown.{{cite:blanchard_roquain2009}} (§2.3, Definition 4)

For a separate numerical illustration, if $m=1000$, $m_0=900$ and $q=0.05$, the theorem's FDR bound is $0.045$. The bound concerns the expectation over repeated data. A realised list can have a larger false-discovery proportion.{{cite:blanchard_roquain2009}} (§2.3, Theorem 6)

**Your turn.** Under the global null, where every hypothesis is true, what does the false-discovery proportion equal when at least one hypothesis is rejected?

::: {.callout-tip collapse="true" title="Answer"}
Every rejection is false, so the proportion is one. Consequently, under the global null the FDR equals the probability of making at least one rejection.
:::

## Generalizations — Dependence requires the matching guarantee
Positive regression dependence permits an extension of the linear step-up guarantee. Under arbitrary dependence, dividing the nominal level by the harmonic sum $H_m=\sum_{r=1}^m1/r$ gives a sufficient conservative modification. These are different assumptions and procedures; marginal p-value validity by itself does not establish the independent-p-value result. Replacing $m_0$ by an estimate can improve power but also changes the procedure, and needs its own calibration argument.{{cite:blanchard_roquain2009}} (§§1.1, 2.3, Theorems 6–7)


## Statistical use — Define the testing family before applying the rule
The number of tests and their null hypotheses determine the family to which the FDR statement applies. The guarantee concerns that collection under its probability assumptions; it does not identify which particular rejected hypotheses are false. Reporting the threshold, the number rejected and the construction of the p-values lets a reader distinguish the data calculation from its error-control justification. The unknown number of true nulls explains why the bound contains a quantity unavailable from the rejected list alone.{{cite:blanchard_roquain2009}} (§§2.2–2.3)
