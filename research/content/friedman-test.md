## Lead context
It ranks the treatments inside each block and asks whether the rank totals could have arisen if, within every block, every ordering were equally likely. The usual reference distribution is chi-squared. For a small table the exact probability is the proportion of within-block permutations that produce a statistic at least as large, and that proportion need not equal the chi-squared tail.

## Motivating example
Six judges score three products. The scores are a convenience; only the order inside each judge is used. Five judges put the products in the same order. The fifth does not. An additive block analysis of these six judges and three products uses the interaction mean square as its error, on $(6-1)(3-1) = 10$ degrees of freedom, and it assumes normal errors and additivity. Ranking within judges uses only the within-block orderings. On these six judges the statistic is $7$, the exact probability under random ranking is $25/864$, and the chi-squared approximation on $2$ degrees of freedom is $0.0302$. Both reject at $5\%$. Changing the sixth judge’s order drops the statistic to $4$ and the chi-squared test no longer rejects.

## Definition — Ranks within blocks
Arrange the observations as $X_{ij}$, with blocks $i = 1, \ldots, b$ and treatments $j = 1, \ldots, k$, and with one observation in each cell. Inside block $i$, replace the $k$ values by their ranks $R(X_{ij})$, using rank $1$ for the smallest. Tied values inside a block share the average of the ranks they occupy. The treatment rank total is
$$
R_j = \sum_{i=1}^{b} R(X_{ij}).
$$
If every ordering inside a block is equally likely and the blocks are independent, each $R_j$ estimates the same mean rank $b(k+1)/2$. The Friedman statistic without ties is
$$
T_1 = \frac{12}{bk(k+1)} \sum_{j=1}^{k} \Bigl(R_j - \frac{b(k+1)}{2}\Bigr)^2 = \frac{12}{bk(k+1)} \sum_{j=1}^{k} R_j^2 - 3b(k+1).
$$
The second form uses only the rank totals. Large $T_1$ is evidence that the treatments do not have the same effect inside the blocks. Friedman writes $n$ for the number of rows, which are the blocks, and $p$ for the number of columns, which are the treatments. Those are $b$ and $k$ here, and his integer formula in the column rank totals is $T_1$.{{cite:friedman1937}} (pp. 676, 678–679); {{cite:nist_friedman2023}} (the rank totals and $T_1$)

When ties occur, the null variance of the ranks is no longer that of a random permutation of $1, \ldots, k$. The untied statistic divides $\sum_j \bigl(R_j - b(k+1)/2\bigr)^2$ by $bk(k+1)/12$. The tie-corrected statistic replaces that denominator by $(A_1 - C_1)/(k-1)$,
$$
T_1 = \frac{\sum_{j=1}^{k} \bigl(R_j - b(k+1)/2\bigr)^2}{(A_1 - C_1)/(k-1)},
$$
where $A_1$ is the sum of the squares of every within-block rank and $C_1 = bk(k+1)^2/4$. With no ties, $A_1 - C_1 = bk(k+1)(k-1)/12$, so $(A_1 - C_1)/(k-1)$ returns to $bk(k+1)/12$ and the two formulae agree.{{cite:nist_friedman2023}} (the tie correction)

Friedman showed that if the number of rows and the number of columns are not too small, $T_1$ is approximately chi-squared on $k-1$ degrees of freedom when the ranking is random. A second function of the same rank totals,
$$
T_2 = \frac{(b-1)\, T_1}{b(k-1) - T_1},
$$
is the two-way analysis-of-variance $F$ statistic computed on the ranks, and it is referred to $F$ on $(k-1,\, (b-1)(k-1))$ degrees of freedom. The chi-squared approximation to $T_1$ can be poor; $T_2$ is the approximation preferred when the table is small. The two are monotone functions of each other, so they order samples in the same way. They do not have the same $p$-value. So long as the number of rows and the number of columns are not too small, Friedman’s $\chi_r^2$, which is $T_1$, tends to a chi-squared law on $p-1$ degrees of freedom.{{cite:friedman1937}} (pp. 678–679); {{cite:nist_friedman2023}} ($T_2$ and the two critical regions)

## Properties — Two treatments, ties, and the exact permutation count
For $k = 2$ there are no ties only if, in every block, one treatment is strictly above the other. Let $S$ be the number of blocks in which treatment $1$ receives rank $2$. Then $R_1 = b + S$ and $R_2 = 3b - R_1$, because each block contributes ranks adding to $3$ and there are $b$ blocks. The null mean of each rank total is $3b/2$. Substitution into the untied formula gives
$$
T_1 = \frac{4}{b}\Bigl(S - \frac{b}{2}\Bigr)^2.
$$
The sign test on the same $b$ blocks has null mean $b/2$ and null variance $b/4$ for the count $S$. The square of its standardised value is $4(S - b/2)^2/b$, the same number as $T_1$. So, with no ties, the Friedman statistic is exactly the squared normal approximation to the sign test, not a new ranking. The signed-rank test is the different procedure that would also use the sizes of the within-block differences. With two treatments, Friedman’s ranking was already identified with the binomial sign count in 1945.{{cite:wilcoxon1945}} (p. 81); {{cite:nist_friedman2023}} ($k = 2$)

The exact null for an untied table does not need the chi-squared curve. Under independent blocks and no treatment differences, the $k!$ orderings inside a block are equally likely. There are $(k!)^b$ rank tables. The exact $p$-value is the proportion of those tables whose $T_1$ is at least as large as observed. For $k = 3$ and $b = 6$ that collection has $6^6 = 46656$ tables, small enough to count. The chi-squared probability is the approximation to this count. Which of the two is being reported should be said explicitly. `friedman.test` reports the chi-squared form.{{cite:nist_friedman2023}} (assumptions); {{cite:r_friedman_test2026}} (Value)

The additive analysis of one observation per cell fits a block effect and a treatment effect and uses the interaction mean square as the error. That residual has $(b-1)(k-1)$ degrees of freedom, $10$ for six blocks and three treatments, which is the denominator degrees of freedom of $T_2$. The $F$ comparison assumes normal errors and additivity, because the interaction mean square is being used as the error variance. Friedman’s procedure does not form that residual. It ranks within blocks, and the null is that every ordering inside a block is equally likely. The procedure is the one used for an unreplicated complete block design when that normality assumption is not granted.{{cite:nist_friedman2023}} ($T_2$); {{cite:r_friedman_test2026}} (Details); {{cite:friedman1937}} (p. 675)

## Worked example — Six judges and three products
The scores, with products $A$, $B$ and $C$ in that order, are
$$
\begin{align*}
&(5, 8, 6),\; (4, 7, 5),\; (6, 9, 7),\\
&(3, 6, 4),\; (7, 5, 8),\; (4, 8, 6).
\end{align*}
$$
Higher is better. Ranking within each judge, the smallest score in the row receiving rank $1$, gives the ranks
$$
\begin{align*}
&(1, 3, 2),\; (1, 3, 2),\; (1, 3, 2),\\
&(1, 3, 2),\; (2, 1, 3),\; (1, 3, 2).
\end{align*}
$$
No row contains a tie. The rank totals are $R_A = 7$, $R_B = 16$ and $R_C = 13$. They add to $6 \times (1+2+3) = 36$, as they must. The null mean of each total is $6 \times 4/2 = 12$. Then
$$
T_1 = \frac{1}{6}\bigl[(7-12)^2 + (16-12)^2 + (13-12)^2\bigr] = \frac{25+16+1}{6} = 7.
$$
The integer form gives the same value: $12/(6 \cdot 3 \cdot 4) \times (7^2+16^2+13^2) - 3 \cdot 6 \cdot 4 = 474/6 - 72 = 7$.

The chi-squared approximation on $k-1 = 2$ degrees of freedom assigns probability $0.0302$ to the region $T_1 \ge 7$. The upper $5\%$ point of that chi-squared law is $5.991$, so the approximate test rejects. The exact count is available here because $6^6 = 46656$ is finite. Of those tables, $1350$ have a statistic of $7$ or more, and $1350/46656 = 25/864 \approx 0.0289$. The approximation and the exact probability are close, and they agree on rejection at $5\%$. They are not the same number. The $F$ form is $T_2 = (6-1) \cdot 7 / (6 \cdot 2 - 7) = 7$ on $(2, 10)$ degrees of freedom, with upper-tail probability $0.0126$. Reporting “$p = 0.030$” without saying which reference produced it mixes $T_1$ with $T_2$. `friedman.test` on the score matrix, rows as blocks and columns as products, returns Friedman’s chi-squared equal to $7$ on $2$ degrees of freedom, the $T_1$ probability $0.0302$.{{cite:r_friedman_test2026}} (Value); {{cite:nist_friedman2023}} ($T_1$ and $T_2$)

The assumptions used for the exact count are that the six judges are independent and that, if the products were equivalent, each judge’s three ranks would be a random permutation. The scores are only the device that produced the ranks. Any strictly increasing transformation of a judge’s three scores would have left that judge’s ranks, and therefore $T_1$, unchanged.

Change the sixth judge’s scores from $(4, 8, 6)$ to $(5, 4, 6)$. That row’s ranks change from $(1, 3, 2)$ to $(2, 1, 3)$. The rank totals become $8$, $14$ and $14$, and
$$
T_1 = \frac{(-4)^2 + 2^2 + 2^2}{6} = \frac{24}{6} = 4.
$$
Now $4 < 5.991$, so the chi-squared test at $5\%$ does not reject. One judge’s order was enough to move the statistic across the approximate critical value. The exact probability for $T_1 \ge 4$ is a larger fraction of the $46656$ tables than $25/864$; the point of the change is the statistic a reader can recompute by hand, which falls from $7$ to $4$.

If the global test rejects, the rank totals can be compared in pairs. Treatments $i$ and $j$ are declared different when
$$
|R_j - R_i| > t_{1-\alpha/2,\, (b-1)(k-1)} \sqrt{\frac{2\bigl(b A_1 - \sum_j R_j^2\bigr)}{(b-1)(k-1)}},
$$
with $A_1$ the sum of all squared within-block ranks. Here there are no ties, so $A_1 = 6(1+4+9) = 84$, and $b A_1 - \sum R_j^2 = 504 - 474 = 30$. The $0.975$ quantile of $t$ on $10$ degrees of freedom is $2.228$, and the threshold is $2.228 \times \sqrt{6} \approx 5.46$. The absolute gaps are $|16-7| = 9$, $|13-7| = 6$ and $|16-13| = 3$. At $\alpha = 0.05$ this rule separates $A$ from $B$ and $A$ from $C$, and it does not separate $B$ from $C$. The rule is a follow-up to a rejected global test, not a set of three fresh $5\%$ tests with a guaranteed family-wise error.{{cite:nist_friedman2023}} (multiple comparisons)

**Your turn.** Four blocks and three treatments have rank totals $5$, $8$ and $11$. Compute $T_1$, and say whether the chi-squared $5\%$ test on $2$ degrees of freedom rejects. The critical value is $5.991$.

::: {.callout-tip collapse="true" title="Answer"}
The null mean of each total is $4 \times 2 = 8$. The deviations are $-3$, $0$ and $3$, and the sum of squares is $9+0+9 = 18$. Then $T_1 = 12/(4 \cdot 3 \cdot 4) \times 18 = 4.5$. Since $4.5 < 5.991$, the approximate $5\%$ test does not reject.
:::

## Statistical use — Blocks, the statistic to quote, and the R function
The design is a complete block design with one observation on each treatment in each block: judges, patients, or batches, with every treatment appearing once inside each. Blocks are there so that a systematic difference between judges is removed before the treatments are compared. Ranking within the block is what removes it.{{cite:dodge2008}} (p. 447)

Quote $T_1$ together with its reference. For a table as small as six blocks and three treatments, the exact permutation probability $25/864$ and the chi-squared probability $0.0302$ can both be given; if only one is given, it has to be the one that was computed. `friedman.test` takes a matrix with blocks in rows and treatments in columns, or a formula `y ~ treatment | block`. It drops a block that contains a missing value. The printed statistic is Friedman’s chi-squared, the $T_1$ family, and the printed degrees of freedom are those of the chi-squared approximation. It does not print $T_2$ and it does not print the exact permutation count.{{cite:r_friedman_test2026}} (Usage, Details and Value)

The data only need to be rankable. A judge who can order three products but cannot score them has already supplied the ranks the test uses. A procedure that used the numerical gaps inside a judge would be assuming more than an order.{{cite:nist_friedman2023}} (assumptions); {{cite:friedman1937}} (p. 675)

## Assumptions and limits — What the chi-squared tail is approximating
The exact $25/864$ uses independent blocks and, inside each block, a uniform random ordering under the null. If the judges confer, or if several judges score the same session, the $46656$ tables are no longer equally likely and the count is not the null probability. The chi-squared statement has a further limit of its own: it is an approximation for tables that are not too small, and Friedman’s derivation presents it as a tendency of the statistic, not as an identity. On this example the approximation is off by about $0.0013$ in the tail probability. That is small beside $0.05$. It is large enough that “the $p$-value is $0.0302$” should not be rewritten as “exactly $1350$ of the $46656$ tables”.{{cite:friedman1937}} (pp. 676, 679)

The pairwise threshold above is a further approximation, a $t$ quantile times an estimated standard error of a difference of rank totals. It is not the exact permutation test of that pair. Separating $A$ from $B$ at a gap of $9$, against a threshold of $5.46$, is stable to a small change in the quantile. A gap sitting on the threshold would not be.

## History — Ranks instead of a normal residual, 1937
Milton Friedman set out the method of ranks in 1937 for tables with two or more criteria of classification, precisely so that the analysis would not inherit the normality assumption of the analysis of variance. Each row is ranked, and a statistic $\chi_r^2$ is formed from the column mean ranks. When the rows and columns are not too few, that statistic is referred to the chi-squared distribution on one fewer degrees of freedom than the number of columns. The integer formula in the rank totals is the expression used in the worked example. In that formula $n$ is the number of rows and $p$ is the number of columns, which are $b$ and $k$ on this page. The paper’s point is the null: if the column factor has no effect, the ranks in a row are a random ranking, and no distribution is assumed for the original measurements.{{cite:friedman1937}} (pp. 675–676, 678–679)

The same reduction, for two columns, is the sign test. The $F$ form on the ranks, the tie correction, and the pairwise comparison of rank totals are the later computational account of the same ranking.{{cite:wilcoxon1945}} (p. 81); {{cite:nist_friedman2023}} (ties, $T_2$, and $k = 2$)

## Connections — Blocks, the sign test, and ranks without blocks
[Blocks in analysis of variance](blocks-in-analysis-of-variance.qmd) are the groups inside which the treatments are ranked. [Two-factor analysis of variance](two-factor-analysis-of-variance.qmd) is the normal-theory analysis of the same rectangular table. With one observation per cell the additive form uses the interaction mean square as its error, on $(b-1)(k-1)$ degrees of freedom, and it assumes normal errors and additivity. Friedman uses only the within-block orderings. [Repeated measures](repeated-measures.qmd) are the case in which the block is a person and the treatments are occasions or conditions on that person. The [sign test](sign-test.qmd) is the Friedman statistic when $k = 2$ and there are no ties. The [Kruskal–Wallis test](kruskal-wallis-test.qmd) is the rank comparison for samples that are not arranged in blocks.

## Check yourself
**1.** Every judge assigns ranks $(1, 3, 2)$ to products $A$, $B$ and $C$. There are six judges. What are the rank totals and $T_1$?

::: {.callout-tip collapse="true" title="Answer"}
The totals are $6$, $18$ and $12$. They deviate from $12$ by $-6$, $6$ and $0$. The sum of squares is $36+36+0 = 72$, and $T_1 = 72/6 = 12$.
:::

**2.** Two treatments are compared in six blocks, and treatment $1$ is ranked higher in every block. What is $T_1$?

::: {.callout-tip collapse="true" title="Answer"}
Here $b = 6$ and $S = 6$, so $T_1 = 4(6 - 3)^2/6 = 6$. The sign count is six positives out of six, and the square of its standardised null value is the same $6$.
:::

**3.** Inside one block the two better products tie, and the third is strictly worse. Which ranks are assigned?

::: {.callout-tip collapse="true" title="Answer"}
The worst product receives rank $1$. The two tied products share the average of ranks $2$ and $3$, which is $2.5$. The within-block ranks are $1$, $2.5$ and $2.5$, in the appropriate order.
:::
