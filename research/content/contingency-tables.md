## Motivating example
A survey records both occupation and degree of belief. Raw counts alone can mislead when one occupation group is three times as large as another. A contingency table keeps the joint counts and their margins together so that comparisons can use within-group proportions. It is a cross-classification of categorical attributes; its layout does not itself imply independence.{{cite:dodge2008}} (p. 110, “Contingency Table”)

## Intuition
A row proportion estimates a conditional distribution, such as belief given occupation. A column proportion reverses the conditioning. Neither equals the joint proportion unless it is multiplied by the corresponding marginal proportion. This distinction separates a large group from a group with a large conditional rate. A table's counts must refer to observational units classified once into mutually exclusive cells.{{cite:openintro2019}} (§6.4.1–6.4.2, two-way tables and expected counts)

## Properties — Deriving the fitted counts
Under multinomial sampling and independence, $p_{ij}=a_ib_j$. Ignoring constants, the log-likelihood is
$$\ell(a,b)=\sum_i R_i\log a_i+\sum_j C_j\log b_j.$$
Maximizing each term subject to a unit sum gives $\widehat a_i=R_i/n$, $\widehat b_j=C_j/n$, and $E_{ij}=R_iC_j/n$. Summing over a row or column shows that the fitted table has exactly the observed margins. The unrestricted table has $rc-1$ free probabilities; independence has $(r-1)+(c-1)$, leaving $(r-1)(c-1)$ residual directions. The resulting Pearson test uses a large-sample chi-squared reference.{{cite:nist_contingency2002}} (§7.4.5, cell probabilities, expected frequencies and degrees of freedom)

## Worked example — Rates before significance
In a constructed table, twenty of fifty people in group A and thirty of one hundred in group B report an outcome. The rates are $0.4$ and $0.3$, although the raw outcome count is larger in B. The observed table is $(20,30)$ in the first row and $(30,70)$ in the second. The fitted independence table is $(16.667,33.333)$ and $(33.333,66.667)$, giving $T=1.5$ on one degree of freedom and approximate $p=0.2207$. The ten percentage-point estimate remains informative even though the test does not reject at 5%.{{cite:openintro2019}} (§6.4, “The chi-square test for two-way tables”)

**Your turn.** In the ESP table below, find the proportion with strong belief among artists and among non-artists. Which denominator belongs to each?

::: {.callout-tip collapse="true" title="Answer"}
The conditional proportions are $67/114=0.5877$ and $129/344=0.3750$. Each denominator is its own row total. Dividing both counts by 458 would give joint proportions instead.
:::

## Statistical use — Association and sampling design
A multinomial table samples one population and records two attributes. Product-multinomial sampling fixes row sizes and compares response distributions across groups. Both can lead to the Pearson formula, but their sampling stories and interpretations differ. The ESP statistic is $15.9364$ with $p=0.000346$, calculated from unrounded expectations; rounding each contribution before summing loses precision. The table shows association, while a causal conclusion would require a design and assumptions beyond cross-classification.{{cite:openintro2019}} (§6.4, testing independence in two-way tables)

## Assumptions and limits
Expected counts near zero undermine the chi-squared approximation. A structural zero is an impossible combination of attributes, not simply an observed zero in a possible cell; such constraints alter the fitted model and degrees of freedom. Repeated observations on the same subject also require dependence to be represented. A table can be arithmetically correct while the independence model for its sampling units is wrong.{{cite:dodge2008}} (pp. 110–111, mathematical aspects and limitations)
