## Motivating example

A laboratory tests several genes for association with a disease and plans to report every gene that passes a significance cutoff. Even if each test has a small false-positive chance, searching many genes makes at least one false claim likely. The family-wise error rate measures that chance for the *whole stated set* of tests, so it is useful when one false claim would undermine the report.{{cite:benjamini_hochberg1995}} (pp. 289–291, Introduction and §2)

## Intuition

Imagine every null hypothesis in the family is true. A single test at level $0.05$ makes a false rejection with probability at most $0.05$. Running ten independent such tests gives ten opportunities for one mistake; the chance of at least one is $1-(1-0.05)^{10}\approx0.4013$. If each cutoff is reduced to $0.005$, the independent-case chance becomes $1-(1-0.005)^{10}\approx0.0489$. The family-wise rate concerns that union of mistakes, not the average false-positive rate of one test. For dependent tests the exact expression changes, but the concern survives.{{cite:benjamini_hochberg1995}} (pp. 289–291, multiplicity and FWER){{cite:nist_bonferroni2002}} (§7.4.7.3, Bonferroni general inequality)

## Definition

Choose a family of $m$ null hypotheses and a rule for rejecting them. Let $V$ be the number of *true* null hypotheses that the rule rejects. The family-wise error rate is $\mathrm{FWER}=\Pr(V\ge1)$ under the data-generating configuration. It is a property of a procedure under a model, not the probability that at least one reported finding is false after the data have been observed. The family must be described in terms of the questions being jointly answered; quietly redefining it after looking at the p-values defeats the intended error guarantee.{{cite:benjamini_hochberg1995}} (§§1–2, pp. 289–291, table of errors)

*Weak* control bounds FWER when all null hypotheses in the family are true. *Strong* control bounds it for every combination of true and false nulls. A method advertised as strong allows genuine effects to be present without losing its bound on false rejections. The distinction matters because real studies often include a mixture of null and non-null effects. {{cite:benjamini_hochberg1995}} (§1, pp. 289–290, strong control)

## Properties — Why Bonferroni works

Suppose each true-null p-value is valid, so $\Pr(p_i\le t)\le t$ for each threshold $t$. Reject a hypothesis only when its p-value is at most $\alpha/m$. For the set $I_0$ of true nulls, the chance of any false rejection is at most $\sum_{i\in I_0}\Pr(p_i\le\alpha/m)\le |I_0|\alpha/m\le\alpha$. The argument is a union bound, so it requires no independence among tests. It may be conservative, particularly if the tests are highly dependent or few nulls are true.{{cite:benjamini_hochberg1995}} (§2, p. 291, Bonferroni threshold){{cite:nist_bonferroni2002}} (§7.4.7.3, general inequality)

The same idea yields simultaneous confidence statements. If each of $g$ intervals misses its own target with chance at most $\alpha/g$, the chance that *any* interval misses is at most $\alpha$. Thus all intervals cover together with probability at least $1-\alpha$. This is the confidence-interval counterpart of family-wise error control. Tukey's studentized-range intervals exploit the joint distribution of pairwise mean differences for a more tailored family of comparisons. {{cite:nist_bonferroni2002}} (§7.4.7.3, simultaneous intervals){{cite:nist_scheffe2002}} (§7.4.7.2, comparison with Tukey)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $E_i$ for falsely rejecting true null $i$. Then $\{V\ge1\}=\bigcup_{i\in I_0}E_i$. The elementary union inequality gives $\Pr(\bigcup_{i\in I_0}E_i)\le\sum_{i\in I_0}\Pr(E_i)$. Each valid p-value tested at $\alpha/m$ has $\Pr(E_i)\le\alpha/m$, hence $\mathrm{FWER}\le |I_0|\alpha/m\le\alpha$. Replacing $E_i$ by the event that interval $i$ misses its target proves simultaneous coverage at least $1-\alpha$.

For independent true-null tests with exact uniform p-values, no rejection at threshold $t$ has probability $(1-t)^m$. Taking its complement gives $1-(1-t)^m$. This exact expression needs independence; the union bound does not. {{cite:benjamini_hochberg1995}} (§2, p. 291){{cite:nist_bonferroni2002}} (§7.4.7.3, general inequality)
:::
:::

## Interpretation — What the guarantee says

If a procedure controls FWER at $0.05$ under its assumptions, then across repeated studies of the same design and data-generating configuration, no more than $5\%$ of studies will make even one false rejection in the stated family. It does not say that every reported rejection has a $5\%$ chance of being false, nor that $5\%$ of rejections are false. Those are different quantities. The false discovery rate, $E\{V/\max(R,1)\}$ for $R$ total rejections, averages the *proportion* of false discoveries; when every null is true, that proportion is one whenever anything is rejected, so FDR and FWER coincide in that special configuration.{{cite:benjamini_hochberg1995}} (§2, pp. 291–292, FWER and FDR)

## Statistical use — Define the family before looking

Family-wise control is compelling when a single mistaken declaration has high cost, such as choosing one treatment based on any apparently superior comparison. A family may be a prespecified set of treatment comparisons, endpoints or features, provided it matches the conclusions to be reported. If the analysis scans all genes but reports only the smallest p-value, calling that selected gene a family of one hides the search. Conversely, unrelated questions need not always be placed in one enormous family; the scientific reporting plan determines the relevant joint claim.{{cite:benjamini_hochberg1995}} (§1, pp. 289–290, when FWER is desirable){{cite:nist_bonferroni2002}} (§7.4.7.3, finite set of contrasts)

The power cost is real but depends on the problem. For $m=5000$ tests and $\alpha=0.05$, Bonferroni's cutoff is $0.05/5000=10^{-5}$, demanding very strong evidence from any one test. Strong effects can still pass; weaker effects may be missed. FDR control may suit a discovery screen where some false leads can be followed up, while FWER control may suit a set of confirmatory claims. The two error targets answer different questions. {{cite:benjamini_hochberg1995}} (§§1, 3.2, pp. 289–290, 294–295, power and example)

If individual p-values are invalid under their nulls, the Bonferroni proof fails at its first probability bound. If a study tests hundreds of outcomes but declares only the most promising five to be its "family" after seeing them, the claimed cutoff ignores the selection. If outcomes or hypotheses are revised repeatedly without accounting for those searches, a nominal family-wise guarantee may not describe the full analysis. Correlation among tests alone does not break Bonferroni control; it changes its conservatism and the exact error rate.{{cite:benjamini_hochberg1995}} (§1, pp. 289–290, selection and multiplicity){{cite:nist_bonferroni2002}} (§7.4.7.3, general inequality)
## Worked example

Four prespecified hypotheses produce p-values $0.004$, $0.015$, $0.030$ and $0.20$. To control FWER at $\alpha=0.05$ by Bonferroni, compare each with $0.05/4=0.0125$. Only $0.004$ passes. Treating each test separately at $0.05$ would report the first three, but its family-wise error guarantee would not be $0.05$. If all four nulls were true and their exact p-values independent, the actual FWER of the Bonferroni rule would be $1-(1-0.0125)^4\approx0.0491$, slightly below the bound. This exact number is illustrative; the $0.05$ guarantee also holds when the tests are dependent.{{cite:benjamini_hochberg1995}} (§2, p. 291){{cite:nist_bonferroni2002}} (§7.4.7.3, Bonferroni inequality)

**Your turn.** Five planned comparisons have p-values $0.002$, $0.009$, $0.014$, $0.070$ and $0.30$. Which pass a Bonferroni family-wise cutoff of $0.05$? If all five nulls are true and tests independent, what is the chance of at least one rejection when each is instead tested at unadjusted level $0.05$?

::: {.callout-tip collapse="true" title="Answer"}
Bonferroni uses $0.05/5=0.01$, so $0.002$ and $0.009$ pass; $0.014$ does not. With five independent exact null p-values tested at $0.05$, the family-wise chance is $1-(0.95)^5\approx0.2262$. The observed number of small p-values is not itself that probability; the latter describes repeated use of the rule under the all-null model.
:::

## Common misconceptions

FWER is not a per-test Type I error rate; it counts whether *any* true null was rejected in the family. It is not the expected false fraction among discoveries, which is FDR. Bonferroni control does not require independent tests, although the convenient formula $1-(1-t)^m$ does. A stringent cutoff is not proof that every rejection is true, and a nonsignificant result is not proof of no effect. These distinctions separate the error criterion, its calculation, and the interpretation of a particular study.{{cite:benjamini_hochberg1995}} (§§1–2, pp. 289–292){{cite:nist_bonferroni2002}} (§7.4.7.3, general inequality)

## Connections

[Multiple testing](multiple-testing.qmd) frames the family. The [Bonferroni correction](bonferroni-correction.qmd) is a general union-bound procedure, while [Tukey intervals](tukey-intervals.qmd) address pairwise means. [False discovery rate](false-discovery-rate.qmd) and [Benjamini–Hochberg](benjamini-hochberg.qmd) use a different error target; [family-wise control implies false-discovery control](family-wise-control-implies-false-discovery-control.qmd) relates the two criteria.{{cite:benjamini_hochberg1995}} (§§1–3, pp. 289–294)

## History

Bonferroni published dependence inequalities in 1936, according to Dodge's biographical entry; one supplies the elementary bound now used for simultaneous tests and intervals. By 1995, Benjamini and Hochberg described family-wise control as the classical approach to multiple comparisons and proposed false discovery rate control for settings where counting the proportion of false leads better matched the scientific aim. The choice of error criterion reflects what a false claim costs in the particular study.{{cite:dodge2008}} (pp. 50–51, Bonferroni entry){{cite:benjamini_hochberg1995}} (§1, pp. 289–290)
