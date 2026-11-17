## Motivating example

A screening programme may care about making any false declaration, or about the fraction of its declarations that are false. These are different error summaries. A guarantee on the first also bounds the second, but a small expected false fraction can coexist with a high probability of at least one false declaration.{{cite:benjamini_hochberg1995}} (§2.1, p.291)

## Statement

Let $V$ count rejected true null hypotheses and $R$ count all rejections in a fixed family. Define $Q=V/R$ when $R>0$ and $Q=0$ when $R=0$. Then
$$\operatorname{FDR}=E(Q)\le P(V\ge1)=\operatorname{FWER}.$$
Thus any procedure controlling FWER at $\alpha$ also controls FDR at $\alpha$ at the same parameter configuration. Strong FWER control supplies this bound for every configuration of true and false nulls. Weak control under the complete null supplies only a complete-null statement.{{cite:benjamini_hochberg1995}} (§2.1, p.291)

## Proof

If $V=0$, then $Q=0$. If $V\ge1$, $V\le R$ gives $Q\le1$. Therefore $0\le Q\le\mathbf1\{V\ge1\}$ pointwise. Taking expectations proves the inequality. It needs neither independent tests nor a particular distribution of their statistics. Under the complete null, every rejection is false, hence $V=R$ and $Q=\mathbf1\{R>0\}$; the two error rates are then equal.{{cite:benjamini_hochberg1995}} (§2.1, p.291)

## Intuition — A probability versus a fraction

FWER regards every outcome with at least one false rejection as an error event, regardless of the number of true discoveries accompanying it. FDR additionally scales false rejections by the realised number of discoveries. The convention at $R=0$ is part of the definition: it makes a procedure that never rejects have FDR zero, rather than an undefined ratio.{{cite:benjamini_hochberg1995}} (§2.1, p.291)

## Worked example

Suppose a procedure always rejects fifty hypotheses and exactly one of those rejected nulls is true. Its FWER is one but its FDR is $1/50=0.02$. This proves that the converse implication fails. In another experiment, suppose it rejects twenty hypotheses with one false rejection with probability $0.1$, and rejects nothing otherwise. Then FWER is $0.1$ and FDR is $0.1/20=0.005$. These are expectations over the procedure's outcomes, not a guarantee about the false fraction in each realised rejection set.{{cite:benjamini_hochberg1995}} (§2.1, p.291)

**Your turn.** Under a complete null, a procedure rejects at least one hypothesis with probability $0.05$. Find both error rates.

::: {.callout-tip collapse="true" title="Answer"}
Every rejection is false, so the false-discovery proportion is one whenever any rejection occurs and zero otherwise. Both FWER and FDR equal $0.05$.
:::

## Statistical use — A union-bound guarantee

For $m$ tests with valid null p-values, Bonferroni rejects when $p_i\le\alpha/m$. If $I_0$ is the set of true nulls,
$$P(V\ge1)\le\sum_{i\in I_0}P(p_i\le\alpha/m)
\le |I_0|\alpha/m\le\alpha.$$
The first step is the union bound, which follows from adding event indicators; no independence is required. With one hundred tests at $\alpha=0.05$, the cutoff is $0.0005$. The theorem then also gives FDR control.{{cite:grinstead_snell1997}} (§1.2, pp.20–23)

## Related concepts — The direction of the guarantee

An FDR-controlling method can allow more rejections than a method that controls the probability of any false rejection. Benjamini–Hochberg chooses a single step-up cutoff from ordered p-values; its independence theorem is a separate result from the elementary inequality proved here. Applying the FDR–FWER inequality requires that both rates refer to the same family and the same procedure.{{cite:benjamini_hochberg1995}} (§3.1, p.293, Thm.1)
