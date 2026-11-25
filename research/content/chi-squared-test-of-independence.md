## Motivating example
Thirty treated patients and thirty controls are split by recovery into counts $18$, $12$, $10$ and $20$. The product of the margins puts $14$ in the treated-recovery cell. The test asks how far the table sits from that product.

## Intuition — Compare the table with the product of its margins
Two categorical factors are independent, in the null hypothesis, when the probability of a cell is the product of its row probability and its column probability. The fitted count in that cell is then the row total times the column total, divided by the sample size. Pearson's statistic adds up, over cells, the squared gap between the observed count and that fitted count, each gap divided by the fitted count. Large values are the ones that count against independence.{{cite:dodge2008}} (pp. 79–80)

## Definition — Statistic, degrees of freedom, and a small-cell warning
For an $r\times c$ table with row totals $R_i$, column totals $C_j$ and sample size $n$, the fitted count under independence is $E_{ij}=R_i C_j/n$. The statistic is
$$
T=\sum_{i=1}^r\sum_{j=1}^c\frac{(O_{ij}-E_{ij})^2}{E_{ij}}.
$$
$T$ is compared with the chi-squared table value on $(r-1)(c-1)$ degrees of freedom: a larger calculated value rejects independence at the chosen level. The approximation uses a random sample with one cell per individual, and it is unreliable when an estimated frequency is small, the stated threshold being less than $5$.{{cite:dodge2008}} (pp. 79–80)

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

**R note.** With `m <- matrix(c(18, 12, 10, 20), nrow = 2, byrow = TRUE)`, `chisq.test(m, correct = FALSE)` reproduces the uncorrected Pearson statistic $30/7$ and $p\approx 0.0384$. For a $2\times 2$ table, R's default `chisq.test(m)` applies Yates's continuity correction, giving $3.28125$ and $p\approx 0.0701$. Thus the default does not reject independence at the unadjusted $5\%$ level, explaining why it differs from the calculation above.

**Your turn.** Keep the same margins and suppose the treated row had been $14$ and $16$. What is $T$?

::: {.callout-tip collapse="true" title="Answer"}
Every observed count equals its fitted count, so each contribution is $0$ and $T=0$. The table matches independence exactly. The degrees of freedom are still $1$.
:::

## Connections — The same statistic, several readings
The reference distribution is the [chi-squared distribution](chi-squared-distribution.qmd) on $(r-1)(c-1)$ degrees of freedom. Estimating the margins, rather than knowing the cell probabilities in advance, is what changes the degrees of freedom; that estimated-parameter case is [Pearson's test with estimated parameters](pearson-test-with-estimated-parameters.qmd). A $2\times 2$ table with a very small fitted count is the setting for [Fisher's exact test](fisher-s-exact-test.qmd), which uses the hypergeometric probabilities instead of the chi-squared tail.{{cite:dodge2008}} (pp. 79–80)
