## Lead context
Multiple testing is the problem of looking at many hypotheses at once, when a level that is modest for one test becomes liberal for the whole list.

## Motivating example
A single test at level $0.05$ has a $5\%$ chance of a false rejection when its null hypothesis is true. Twenty independent tests, each at that level, have a much larger chance that at least one true null is rejected. The probability is $1-0.95^{20}=0.6415$. A list of "discoveries" from those tests is not twenty copies of a $5\%$ procedure. The errors accumulate.{{cite:hastie_esl2009}} (§18.7, p. 686)

## Intuition — Family-wise error or a share of the discoveries
The family-wise error rate is the probability of at least one false rejection in the family. Bonferroni keeps it at most $\alpha$ by testing each hypothesis at $\alpha/m$. That guarantee is strict, and with a large $m$ it demands very small $p$-values, so many real differences are missed. The false discovery rate is the expected proportion of false rejections among the rejections. It agrees with the family-wise error rate when every null is true, and it is smaller when some nulls are false, because the denominator then counts true discoveries as well as false ones. Controlling the proportion, rather than the chance of any mistake, leaves more power when many of the alternatives are real.{{cite:benjamini_hochberg1995}} (pp. 291–293, §2){{cite:hastie_esl2009}} (§18.7.1, pp. 687–688)

## Definition — Bonferroni and Benjamini–Hochberg
For $m$ tests and family-wise level $\alpha$, Bonferroni rejects hypothesis $j$ when its $p$-value satisfies $p_j\le \alpha/m$. For independent test statistics, the Benjamini–Hochberg procedure at level $q^\ast$ orders the $p$-values $p_{(1)}\le\cdots\le p_{(m)}$ and rejects every hypothesis whose $p$-value is at most $p_{(k)}$, where $k$ is the largest index with
$$
p_{(k)}\le q^\ast\, k/m.
$$
If no such $k$ exists, nothing is rejected. When the test statistics of the true nulls are independent, the procedure controls the false discovery rate at a level no larger than $q^\ast$.{{cite:benjamini_hochberg1995}} (p. 293, §3.1, Theorem 1){{cite:hastie_esl2009}} (§18.7.1, Algorithm 18.2)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $A_j$ be a false rejection of a true null by an uncorrected level-$\alpha$ test, so $\Pr(A_j)\le\alpha$. Bonferroni instead uses level $\alpha/m$. The probability of at least one false rejection is at most $\sum_j \Pr(A_j)\le m\cdot(\alpha/m)=\alpha$, by the union bound. This does not assume independence. The proof that the ordered-threshold procedure controls the false discovery rate is longer and is not given here.{{cite:benjamini_hochberg1995}} (p. 293, Theorem 1){{cite:hastie_esl2009}} (§18.7, p. 686)
:::
:::

## Worked example
Four ordered $p$-values are $0.004$, $0.018$, $0.040$ and $0.200$, and $q^\ast=0.10$. The thresholds $q^\ast k/4$ are $0.025$, $0.050$, $0.075$ and $0.100$. Then $0.004\le 0.025$, $0.018\le 0.050$, $0.040\le 0.075$, and $0.200\not\le 0.100$. The largest admissible index is $k=3$, so the three smallest $p$-values are rejected and $0.200$ is not. Bonferroni at family-wise level $0.10$ uses the single threshold $0.10/4=0.025$, and rejects only $0.004$. The ordered rule rejects two further hypotheses because their place in the list, not a common threshold, sets the bar.

**Your turn.** Five independent true nulls are each tested at level $0.05$. Find the exact family-wise error rate.

::: {.callout-tip collapse="true" title="Answer"}
The probability that one true null is not rejected is $0.95$, so the probability that all five escape rejection is $0.95^5=0.77378$. The family-wise error rate is $1-0.77378=0.22622$.
:::

## Connections — One comparison and a long list
A [Bonferroni correction](bonferroni-correction.qmd) is the union-bound threshold. The [false discovery rate](false-discovery-rate.qmd) is the proportion Benjamini and Hochberg control, and [Benjamini–Hochberg](benjamini-hochberg.qmd) is the ordered procedure. [Multiple comparisons](multiple-comparisons.qmd) in an analysis of variance is the same accumulation of error, specialised to contrasts among means. Dependence among the tests makes $1-(1-\alpha)^m$ the wrong family-wise formula. Positive dependence tends to make that probability smaller, because the false rejections overlap.{{cite:hastie_esl2009}} (§18.7, p. 686)
