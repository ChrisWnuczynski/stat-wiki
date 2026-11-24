## Lead context
Multiple testing is the problem of looking at many hypotheses at once, when a level that is modest for one test becomes liberal for the whole list.

## Motivating example
A single test at level $0.05$ has a $5\%$ chance of a false rejection when its null hypothesis is true. Twenty independent tests, each at that level, have a much larger chance that at least one true null is rejected. The probability is $1-0.95^{20}=0.6415$. A list of "discoveries" from those tests is not twenty copies of a $5\%$ procedure. The errors accumulate.{{cite:hastie_esl2009}} (§18.7, p. 686)

## Intuition — Family-wise error or a share of the discoveries
The family-wise error rate is the probability of at least one false rejection in the family. Bonferroni keeps it at most $\alpha$ by testing each hypothesis at $\alpha/m$. That guarantee is strict, and with a large $m$ it demands very small $p$-values, so many real differences are missed. The false discovery rate is the expected proportion of false rejections among the rejections. It agrees with the family-wise error rate when every null is true, and it is smaller when some nulls are false, because the denominator then counts true discoveries as well as false ones. Controlling the proportion, rather than the chance of any mistake, leaves more power when many of the alternatives are real.{{cite:benjamini_hochberg1995}} (pp. 291–293, §2){{cite:hastie_esl2009}} (§18.7.1, pp. 687–688)

## Definition — Bonferroni and Benjamini–Hochberg
For $m$ tests and family-wise level $\alpha$, Bonferroni rejects hypothesis $j$ when its $p$-value satisfies $p_j\le \alpha/m$. The Benjamini–Hochberg procedure at level $q^\ast$ orders the $p$-values $p_{(1)}\le\cdots\le p_{(m)}$ and rejects every hypothesis whose $p$-value is at most $p_{(k)}$, where $k$ is the largest index with
$$
p_{(k)}\le q^\ast\, k/m.
$$
If no such $k$ exists, nothing is rejected.{{cite:hastie_esl2009}} (§18.7.1, Algorithm 18.2) Let $m_0$ be the number of true null hypotheses. Theorem 1 states that independent test statistics yield control of the false discovery rate at $q^\ast$ for any configuration of the false nulls. The lemma used to prove it takes the true-null $p$-values to be independent, holds for every fixed tuple of false-null $p$-values, and bounds the conditional false discovery rate by $(m_0/m)q^\ast$. Integrating the conditional bound gives a false discovery rate no larger than $(m_0/m)q^\ast$, and therefore no larger than $q^\ast$. The remark after the proof allows the false-null statistics to be dependent among themselves. What the argument requires is that each true-null $p$-value is independent of all the other $p$-values. Mutual independence among the true-null $p$-values still leaves a false-null $p$-value free to depend on them, and the conditional bound need not survive that dependence.{{cite:benjamini_hochberg1995}} (p. 293, §3.1, Theorem 1, the lemma used in its proof, and the following remark)

The role of the missing independence is visible in a family of four $p$-values at level $q^\ast=0.04$. The ordered thresholds are $0.01$, $0.02$, $0.03$ and $0.04$. Let $P_1,P_2,P_3$ be independent and uniform on $(0,1)$, each the $p$-value of a true null, and let $P_4$ be the $p$-value of a false null. Set $P_4=0$ when one of $P_1,P_2,P_3$ lies in $(0.01,0.02]$ and the other two exceed $0.04$, and set $P_4=1$ otherwise. For each $i\in\{1,2,3\}$, write $F_i$ for the event that $P_i\le 0.01$ while the other two true-null $p$-values exceed $0.04$. On $F_i$ one has $P_4=1$. The smallest $p$-value is $P_i$, which meets the threshold $0.01$, and every remaining $p$-value exceeds $0.04$, so the comparisons at ranks $2$, $3$ and $4$ fail. The procedure rejects only hypothesis $i$, and the proportion of false rejections among the rejections is $1$. Write $A_i$ for the event that $P_i\in(0.01,0.02]$ while the other two true-null $p$-values exceed $0.04$. On $A_i$ one has $P_4=0$. The ordered values begin with $0$ and $P_i$, and these are at most the thresholds $0.01$ and $0.02$, while the other two exceed $0.04$. The procedure rejects the false null and true null $i$, and the proportion of false rejections among the rejections is $1/2$.

A uniform coordinate falls in an interval of length $0.01$ with probability $0.01$, and it exceeds $0.04$ with probability $0.96$. Thus $\Pr(F_i)=\Pr(A_i)=0.01\times 0.96\times 0.96=0.009216$. The six events are disjoint, because each requires two true-null $p$-values to exceed $0.04$. The false discovery rate is the expectation of the proportion just used, so these events alone give the lower bound
$$
3\times 0.009216 + 3\times\frac{1}{2}\times 0.009216 = 0.041472.
$$
The nominal level was $0.04$. The variables $P_1,P_2,P_3$ remain independent of one another. The excess over $0.04$ is produced by the dependence of $P_4$ on $(P_1,P_2,P_3)$, which means that no true-null $p$-value is independent of all the other $p$-values.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $A_j$ be a false rejection of a true null by an uncorrected level-$\alpha$ test, so $\Pr(A_j)\le\alpha$. Bonferroni instead uses level $\alpha/m$. The probability of at least one false rejection is at most $\sum_j \Pr(A_j)\le m\cdot(\alpha/m)=\alpha$, by the union bound. This does not assume independence. The proof that the ordered-threshold procedure controls the false discovery rate conditions on the false-null $p$-values and is not given here.{{cite:benjamini_hochberg1995}} (p. 293, Theorem 1){{cite:hastie_esl2009}} (§18.7, p. 686)
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
