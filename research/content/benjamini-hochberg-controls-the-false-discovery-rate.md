## Motivating example
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

## Worked example
### A step-up crossing can follow a failed step
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

## Intuition
Family-wise control asks for a small probability of any false rejection. Bonferroni spends the error budget evenly: with $m$ tests and budget $\alpha$, each p-value is compared with $\alpha/m$. That rule does not look at how the p-values are arranged, and it becomes severe as $m$ grows. False-discovery-rate control asks for something weaker and often more relevant to a screen. Among the hypotheses that were rejected, the expected fraction that are true nulls should be at most a chosen $q$, up to the factor $m_0/m$ that accounts for how many nulls are true.

The linear step-up rule reads the ordered p-values against the line $qr/m$. It does not stop at the first failure. In the worked list $(0.004,0.018,0.021,0.06,0.4)$ with $q=0.05$ and $m=5$, the thresholds are $0.01,0.02,0.03,0.04,0.05$. The second p-value $0.018$ is below $0.02$, the third $0.021$ is below $0.03$, and the fourth $0.06$ is above $0.04$. The largest index that still meets its line is $3$, so the first three hypotheses are rejected even though a reader who stopped at the first exceedance would have to look carefully at the order. The rule uses the largest crossing.

## Key results — The realised proportion is not the FDR
If $V$ true nulls are among $R$ rejections, the false-discovery proportion is $V/(R\vee 1)$. The maximum with one sets the ratio to zero when nothing is rejected. There are then no discoveries and no false discoveries. For $R=8$ and $V=2$ the realised proportion is $2/8=0.25$. The FDR is the expectation of that proportion, not the proportion in one realised list. A list with proportion $0.25$ is compatible with a procedure whose FDR bound is $0.045$. The bound in the theorem, for $m=1000$, $m_0=900$ and $q=0.05$, is $(900/1000)\cdot 0.05=0.045$. Under exact uniformity and independence the bound is sharp: the expectation equals $(m_0/m)q$ rather than merely sitting below it.

Under the global null every hypothesis is true, so $V=R$ whenever $R\ge 1$ and the proportion equals one on that event. The FDR then equals the probability of at least one rejection. Family-wise error and false-discovery rate agree in that special case. They separate as soon as some nulls are false and a large $R$ can dilute a nonzero $V$.

## Common misconceptions
The procedure does not estimate $V$ for the list in hand. The p-values determine $R$. The identities of the false nulls are unknown, which is why a significant call is not labelled true or false by the theorem. An estimate of $m_0$ can be plugged into a modified threshold. That modification is a different procedure and needs its own proof. Replacing $m_0$ by $m$ in the guarantee is valid and conservative, because $m_0/m\le 1$. It is not the same act as estimating $m_0$ from the data and then claiming the sharper bound without checking the estimation.

Dependence among p-values removes the equality case of the independent proof. Positive regression dependence on a subset is one condition under which the linear step-up rule still controls FDR at level $q$. Arbitrary dependence is handled by a smaller threshold, dividing $q$ by the harmonic sum $H_m=\sum_{r=1}^m 1/r$. For $m=5$, $H_5=1+1/2+1/3+1/4+1/5=137/60\approx 2.283333$, so the adjusted level is $q/H_5$. For $m=1000$ the harmonic sum is about $7.485$ and the adjustment is more severe. Using the independent-p-value theorem under arbitrary dependence is not justified by the marginal validity of each separate p-value.{{cite:blanchard_roquain2009}} (§§1.1, 2.3, Theorems 6–7)

## Related concepts
A single-test p-value is a false-discovery-rate procedure with $m=1$: the threshold is $q$, and $V/(R\vee 1)$ is either zero or one. Bonferroni and Holm control a different functional, the probability of $V\ge 1$. A study that screens thousands of hypotheses and can tolerate a controlled fraction of false leads is in the false-discovery setting. A study that will act on a single rejected claim as if it were confirmed is closer to the family-wise setting. The mathematics does not choose the study. It converts the chosen functional into a threshold for the ordered p-values, under the dependence assumption the user is willing to assert.
