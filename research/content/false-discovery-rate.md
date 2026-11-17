## Lead context
The false discovery rate is the expected share of true nulls among the hypotheses a procedure declares significant.

## Motivating example
Four sorted $p$-values are $0.001$, $0.04$, $0.06$ and $0.8$. At level $0.1$ the Benjamini–Hochberg comparisons are $0.025$, $0.05$, $0.075$ and $0.1$. The comparison $0.8\le 0.1$ does not hold.

## Intuition — A proportion of the list, not a probability of any mistake
Family-wise control asks for a small probability of even one false rejection. That demand grows stricter as the list of tests grows. The false discovery rate asks a different question: among the hypotheses actually declared significant, what fraction are null, on average? A long list may contain many false rejections and still have a small proportion of them, so control of the rate is a weaker demand than control of the family-wise error, and it leaves more power for the non-null hypotheses.{{cite:hastie_esl2009}} (p. 687)

## Definition — The ratio, with an empty list counted as zero
Let \(V\) be the number of true nulls that are rejected and \(R\) the number of rejections. The false discovery proportion is \(V/R\) when \(R>0\), and \(0\) when \(R=0\). The false discovery rate is the expectation of that proportion. Hastie, Tibshirani and Friedman write the same target as \(\mathrm{E}(V/R)\) for the genes called significant. The empty-list convention matters when a procedure often rejects nothing, because conditioning on \(R>0\) drops the factor \(\mathrm{P}(R>0)\).{{cite:hastie_esl2009}} (p. 687, eq. 18.43)

## Properties — Family-wise control is the stronger demand
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let \(Q=V/R\) when \(R>0\) and \(Q=0\) when \(R=0\). If \(V=0\), then \(Q=0\). If \(V\ge 1\), then \(Q=V/R\le 1\). So \(Q\le 1_{\{V\ge 1\}}\) and \(\mathrm{E}(Q)\le\mathrm{P}(V\ge 1)\). When every null is true, \(V=R\), so \(Q\) is \(0\) or \(1\) and the two sides agree.{{cite:hastie_esl2009}} (p. 687)
:::
:::

Under independence, the Benjamini–Hochberg procedure at level \(\alpha\) satisfies \(\mathrm{FDR}\le (M_0/M)\alpha\le\alpha\), where \(M_0\) is the number of true nulls and \(M\) is the number of tests. The argument is not the short comparison above.{{cite:hastie_esl2009}} (p. 687, eq. 18.45)

## Worked example — Four ordered \(p\)-values at level \(0.1\)
Four \(p\)-values, already sorted, are \(0.001\), \(0.04\), \(0.06\) and \(0.8\). The Benjamini–Hochberg threshold at level \(0.1\) compares \(p_{(j)}\) with \(0.1\cdot j/4\):
\[
0.025,\quad 0.05,\quad 0.075,\quad 0.1.
\]
Then \(0.001\le 0.025\), \(0.04\le 0.05\) and \(0.06\le 0.075\), while \(0.8\le 0.1\) does not hold. The largest passing index is \(3\), so those three hypotheses are rejected and the last is kept.{{cite:hastie_esl2009}} (p. 688, Algorithm 18.2)

**Your turn.** Replace the level by \(0.05\), and use the same four sorted \(p\)-values. Which hypotheses are rejected?

::: {.callout-tip collapse="true" title="Answer"}
The thresholds are \(0.0125\), \(0.025\), \(0.0375\) and \(0.05\). Only \(0.001<0.0125\). The later comparisons \(0.04<0.025\), \(0.06<0.0375\) and \(0.8<0.05\) all fail. The largest passing index is \(1\), so only the first hypothesis is rejected.
:::

## Connections — Bonferroni, the step-up line, and power
A [Bonferroni correction](bonferroni-correction.qmd) aims at the [family-wise error rate](family-wise-error-rate.qmd). The comparison \(Q\le 1_{\{V\ge 1\}}\) is why that control also controls the false discovery rate, while the converse fails as soon as some nulls are false. The [Benjamini–Hochberg](benjamini-hochberg.qmd) rule is the step-up comparison used in the worked example. The bound \(\mathrm{FDR}\le\alpha\) quoted from the independent case is a guarantee on the expectation, not a guarantee that every realised list has false-discovery proportion at most \(\alpha\).{{cite:hastie_esl2009}} (p. 687, eq. 18.45)

## Check yourself
Sorted \(p\)-values \(0.01\) and \(0.04\), with \(M=2\) and level \(0.05\). How many hypotheses are rejected?

::: {.callout-tip collapse="true" title="Answer"}
The thresholds are \(0.025\) and \(0.05\). Then \(0.01<0.025\) and \(0.04<0.05\), so both are rejected.
:::

In that two-test rejection, could the realised false-discovery proportion still be \(1\)?

::: {.callout-tip collapse="true" title="Answer"}
Yes. If both nulls are true, then \(V=R=2\) and the proportion is \(1\). Control of the expected proportion does not cap the proportion on a single list.
:::
