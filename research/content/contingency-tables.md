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

**Your turn.** In the ESP survey table — the cross-classification of 458 respondents by artist status and strength of belief in extrasensory perception — find the proportion with strong belief among artists and among non-artists. Which denominator belongs to each?

::: {.callout-tip collapse="true" title="Answer"}
The conditional proportions are $67/114=0.5877$ and $129/344=0.3750$. Each denominator is its own row total. Dividing both counts by 458 would give joint proportions instead.
:::

## Statistical use — Association and sampling design
A multinomial table samples one population and records two attributes. Product-multinomial sampling fixes row sizes and compares response distributions across groups. Both can lead to the Pearson formula, but their sampling stories and interpretations differ. The ESP statistic is $15.9364$ with $p=0.000346$, calculated from unrounded expectations; rounding each contribution before summing loses precision. The table shows association, while a causal conclusion would require a design and assumptions beyond cross-classification.{{cite:openintro2019}} (§6.4, testing independence in two-way tables)

## Assumptions and limits
Expected counts near zero undermine the chi-squared approximation. A structural zero is an impossible combination of attributes, not simply an observed zero in a possible cell; such constraints alter the fitted model and degrees of freedom. Repeated observations on the same subject also require dependence to be represented. A table can be arithmetically correct while the independence model for its sampling units is wrong.{{cite:dodge2008}} (pp. 110–111, mathematical aspects and limitations)

## Lead context
A two-way contingency table records how many observations fall in each combination of two categorical variables. The row and column totals are the margins. Independence says that the conditional distribution of one variable is the same in every row. The fitted count in a cell is then the product of its row total, its column total, and the reciprocal of the grand total. The comparison of observed and fitted counts uses the same Pearson statistic as a goodness-of-fit comparison, with degrees of freedom determined by how many cell probabilities remain free after the margins are fitted.{{cite:dodge2008}} (p. 110, “Contingency Table”)

## Definition
For an $r\times c$ table the independence model has $(r-1)(c-1)$ degrees of freedom when no cell is fixed at probability zero and the margins are estimated from the table. A $2\times 3$ table therefore has two degrees of freedom, not five and not one. The expected count in row $i$ and column $j$ is $E_{ij}=R_iC_j/N$. Pearson's statistic is $\sum (O_{ij}-E_{ij})^2/E_{ij}$. Conditioning on both margins of a $2\times 2$ table yields a hypergeometric reference under independence. That exact comparison uses a different reference set from the chi-squared tail.{{cite:agresti1992_exact_survey}} (§§1.3–2.1, pp. 133–135){{cite:nist_contingency2002}} (§7.4.5, cell probabilities, expected frequencies and degrees of freedom)

## Interpretation
In the ESP survey table the grand total is $458$, the row totals are $114$ and $344$, and the fitted counts are about $48.79$, $55.76$, and $9.46$ in the first row. The statistic is about $15.94$ on two degrees of freedom, with an upper-tail probability near $0.000346$. The first-row admission rate is $67/114\approx 0.588$ and the second-row rate is $129/344=0.375$. Those two rates describe the rows. The constructed table with counts $20,30$ and $30,70$ has fitted counts about $16.667,33.333$ and $33.333,66.667$. Its statistic is $1.5$ on one degree of freedom, and the upper-tail probability is about $0.2207$.{{cite:openintro2019}} (§6.4, “The chi-square test for two-way tables”)

## Common misconceptions
A significant chi-squared statistic is evidence against independence under the sampling model. It is not a measure of how large the association is, and it grows with the sample size when the same population proportions are retained. The contributions $6.80$, $3.90$, and $1.26$ in the first row show where the ESP survey discrepancy is concentrated; they are not separate tests with their own reference distributions. A zero fitted count cannot be used in the denominator. If a row or column total is zero, that row or column contributes no observations and should be removed before the degrees of freedom are counted. Choosing which columns to merge after seeing the statistic changes the test that was planned.{{cite:dodge2008}} (pp. 110–111, mathematical aspects and limitations){{cite:openintro2019}} (§6.4, testing independence in two-way tables)

## Connections
The ESP survey table has grand total $458$ and row totals $114$ and $344$. Independence fits the cell counts by multiplying each row total by each column total and dividing by $458$. The first row of fitted counts is about $48.79$, $55.76$, and $9.46$. Pearson's statistic is about $15.94$ on two degrees of freedom, and the upper-tail probability is near $0.000346$. The row rates $67/114\approx 0.588$ and $129/344=0.375$ describe the two groups. They do not, by themselves, name a cause.

The constructed table $(20,30)$ and $(30,70)$ is smaller and has one degree of freedom. Its fitted counts are about $16.667$, $33.333$ and $33.333$, $66.667$. The statistic is $1.5$ and the upper-tail probability is about $0.2207$. A two-by-three table and a two-by-two table use the same Pearson formula and different degrees of freedom, $(r-1)(c-1)$. Contributions such as $6.80$, $3.90$, and $1.26$ show where a discrepancy is concentrated. They are pieces of one statistic, not separate tests. A zero row or column total removes that line before the degrees of freedom are counted, because it contributes no observations.{{cite:openintro2019}} (§6.4.1–6.4.2, two-way tables and expected counts)
