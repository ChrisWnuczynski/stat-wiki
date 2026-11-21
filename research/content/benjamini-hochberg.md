## Lead context
Benjamini–Hochberg is a step-up rule that rejects an initial run of ordered p-values so that the expected share of false discoveries stays at or below a chosen level.

## Motivating example
Take $m=5$, $q^*=0.05$ and ordered $p$-values $0.001$, $0.012$, $0.020$, $0.039$, $0.30$. The thresholds $(i/5)0.05$ are $0.01$, $0.02$, $0.03$, $0.04$ and $0.05$. Then $0.039\le 0.04$, while $0.30>0.05$, so $k=4$. The strict form in Algorithm 18.2 also stops at $4$, because $0.039<0.04$. A single cutoff $q^*/m=0.01$ rejects only the first $p$-value.

## Intuition — A line that gets more lenient
A family-wise rule spends its whole error budget on the event that any true null is rejected. The false-discovery rate instead looks at the proportion of rejected hypotheses that are true nulls, and takes the expectation of that proportion. Ordering the $p$-values and drawing a line of slope $q^*/m$ spends that budget gradually: the smallest $p$-value is held to a strict cutoff, and later ones are allowed a higher threshold. The procedure then rejects every hypothesis up to the last one that meets its own threshold, including an earlier $p$-value that sat above the line at its own rank.{{cite:hastie_esl2009}} (Ch. 18, §18.7.1, pp. 687–688)

## Definition — The largest rank under the line
Let $P_{(1)}\le\cdots\le P_{(m)}$ be the ordered $p$-values and let $q^*\in(0,1)$. Reject $H_{(1)},\ldots,H_{(k)}$ when $k$ is the largest index with $P_{(k)}\le (k/m)q^*$, and reject nothing if no such index exists. Hastie, Tibshirani and Friedman write the same step-up search with a strict inequality, $P_{(j)}<\alpha j/M$.{{cite:hastie_esl2009}} (p. 688, Algorithm 18.2, Eq. 18.44) When no ordered $p$-value equals its threshold, the closed and strict cutoffs reject the same set. They call the controlled quantity

$$
\mathrm{FDR}=\mathbb{E}(V/R),
$$

with $V$ the number of false rejections and $R$ the number of rejections, and they record the bound $\mathrm{FDR}\le (M_0/M)\alpha\le\alpha$ under independence.{{cite:hastie_esl2009}} (p. 687, Eq. 18.43 and Eq. 18.45)

## Worked example — Five ordered $p$-values

**Your turn.** Use the same five $p$-values and set $q^*=0.02$. List the five thresholds and give $k$.

::: {.callout-tip collapse="true" title="Answer"}
The thresholds are $0.004$, $0.008$, $0.012$, $0.016$ and $0.020$. Only $0.001\le 0.004$. The next $p$-value, $0.012$, exceeds $0.008$, and none of the later ones meet their own thresholds, so $k=1$.
:::

## Connections — Family-wise error and a plug-in estimate
The [family-wise error rate](family-wise-error-rate.qmd) is $\mathbb{P}(V\ge 1)$, which is at least the false-discovery rate, so a procedure that controls the former controls the latter.{{cite:hastie_esl2009}} (p. 687) A [Bonferroni correction](bonferroni-correction.qmd) is the single cutoff $q^*/m$ used in the example. The [false discovery rate](false-discovery-rate.qmd) is the expectation being controlled, not the false-discovery proportion in one realised list. Hastie, Tibshirani and Friedman also describe a permutation plug-in, $\widehat{\mathrm{FDR}}=\widehat{\mathbb{E}}(V)/R_{\mathrm{obs}}$, and say that it matches Benjamini–Hochberg when the $p$-values come from those permutations.{{cite:hastie_esl2009}} (p. 689, Algorithm 18.3)
