## Intuition — Compare the table with the product of its margins
Two categorical factors are independent, in the null hypothesis, when the probability of a cell is the product of its row probability and its column probability. The fitted count in that cell is then the row total times the column total, divided by the sample size. Pearson's statistic adds up, over cells, the squared gap between the observed count and that fitted count, each gap divided by the fitted count. Large values are the ones that count against independence.{{cite:dodge2008}} (pp. 79–80)

## Definition — Statistic, degrees of freedom, and a small-cell warning
For an $r\times c$ table with row totals $R_i$, column totals $C_j$ and sample size $n$, the fitted count under independence is $E_{ij}=R_i C_j/n$. The statistic is
$$
T=\sum_{i=1}^r\sum_{j=1}^c\frac{(O_{ij}-E_{ij})^2}{E_{ij}}.
$$
Dodge compares $T$ with the chi-squared table value on $(r-1)(c-1)$ degrees of freedom: a larger calculated value rejects independence at the chosen level. The same entry requires a random sample, one cell per individual, and warns that the approximation is unreliable when an estimated frequency is small, the stated threshold being less than $5$.{{cite:dodge2008}} (pp. 79–80)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
An $r\times c$ table has $rc$ cells and one constraint that the counts sum to $n$, leaving $rc-1$ free cells. The fitted independence model estimates $r-1$ free row probabilities and $c-1$ free column probabilities. The difference is
$$
rc-1-(r-1)-(c-1)=(r-1)(c-1).
$$
That count of free cells is the degrees of freedom in the chi-squared reference law. The limit law itself is not part of this arithmetic.{{cite:dodge2008}} (p. 80, degrees of freedom $(r-1)(c-1)$)
:::
:::

## Worked example — A $2\times 2$ trial
Thirty treated patients and thirty controls are classified by recovery. The counts are $18$ and $12$ in the treated row, and $10$ and $20$ in the control row. The column totals are $28$ and $32$, and $n=60$. The fitted count for treated recoveries is $30\times 28/60=14$. The four fitted counts are $14$, $16$, $14$ and $16$, all above $5$. The four contributions are
$$
\frac{4^2}{14},\quad \frac{4^2}{16},\quad \frac{4^2}{14},\quad \frac{4^2}{16},
$$
which sum to $30/7=4.286$ to three decimal places. There is $(2-1)(2-1)=1$ degree of freedom. The $0.95$ quantile of $\chi^2_1$ is $3.841$ to three decimal places, and $4.286>3.841$, so the comparison rejects independence at level $5\%$. The upper-tail probability past $30/7$ is $0.0384$ to four decimal places.{{cite:dodge2008}} (pp. 79–80)

**Your turn.** Keep the same margins and suppose the treated row had been $14$ and $16$. What is $T$?

::: {.callout-tip collapse="true" title="Answer"}
Every observed count equals its fitted count, so each contribution is $0$ and $T=0$. The table matches independence exactly. The degrees of freedom are still $1$.
:::

## Check yourself
### Degrees of freedom
How many degrees of freedom does a $3\times 4$ table have under this test?

::: {.callout-tip collapse="true" title="Answer"}
$(3-1)(4-1)=6$. The arithmetic is $12-1-(2+3)=6$.{{cite:dodge2008}} (p. 80)
:::

### A cell below the warning line
One fitted count is $3.2$ and the others exceed $5$. What does Dodge's condition say about the chi-squared approximation?

::: {.callout-tip collapse="true" title="Answer"}
The approximation is unreliable when an estimated frequency is small, and the stated threshold is less than $5$. A fitted count of $3.2$ falls under that warning. Combining categories is the remedy only when the combined categories still make sense.{{cite:dodge2008}} (p. 80)
:::

## Connections — The same statistic, several readings
The reference distribution is the [chi-squared distribution](chi-squared-distribution.qmd) on $(r-1)(c-1)$ degrees of freedom. Estimating the margins, rather than knowing the cell probabilities in advance, is what changes the degrees of freedom; that estimated-parameter case is [Pearson's test with estimated parameters](pearson-test-with-estimated-parameters.qmd). A $2\times 2$ table with a very small fitted count is the setting for [Fisher's exact test](fisher-s-exact-test.qmd), which uses the hypergeometric probabilities instead of the chi-squared tail.{{cite:dodge2008}} (pp. 79–80)
