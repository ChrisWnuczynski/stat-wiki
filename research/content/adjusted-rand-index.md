## Motivating example
Six items are split as $\{1,2,3\}$ against $\{4,5,6\}$, and again as $\{1,2,4\}$ against $\{3,5,6\}$. The labels do not have to match. Agreement is counted on the pairs.{{cite:hubert_arabie1985}} (pp. 193–218)

## Intuition — Pairs, not labels
Two partitions of the same items can use different label names for the same groups. Agreement is therefore counted on pairs. A pair that sits together in both partitions, or apart in both, is a pair the partitions treat the same way. The adjusted index subtracts the number of together-pairs expected from the two sets of group sizes alone.{{cite:hubert_arabie1985}} (pp. 193–218) Identical partitions then score one, as the proof below checks.

## Definition — Chance-corrected pair counts
Let $n_{ij}$ be the number of items in group $i$ of the first partition and group $j$ of the second, with row sums $a_i$ and column sums $b_j$. Write $C(m,2)=m(m-1)/2$ and $C(n,2)$ for the number of pairs. The number of pairs placed together in both partitions is $I=\sum_{ij}C(n_{ij},2)$.{{cite:hubert_arabie1985}} (pp. 193–218) Under a random table with these margins, the hypergeometric falling factorial gives
$$
\mathbb E(I)=\frac{\bigl(\sum_i C(a_i,2)\bigr)\bigl(\sum_j C(b_j,2)\bigr)}{C(n,2)}.
$$
The ceiling used in the correction is $\bigl(\sum_i C(a_i,2)+\sum_j C(b_j,2)\bigr)/2$. The adjusted index is $(I-\mathbb E(I))$ divided by that ceiling minus $\mathbb E(I)$. The unadjusted Rand index, by contrast, is the proportion of all pairs that are together in both or apart in both.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
With both margins fixed, the count $n_{ij}$ satisfies $\mathbb E\bigl[n_{ij}(n_{ij}-1)\bigr]=a_i(a_i-1)\,b_j(b_j-1)/\bigl(n(n-1)\bigr)$. Divide by two:
$$
\mathbb E\bigl[C(n_{ij},2)\bigr]=C(a_i,2)\,C(b_j,2)/C(n,2).
$$
Summing over cells factors into the product of the two pair totals over $C(n,2)$. If the partitions are identical, the table is diagonal, $I=\sum_i C(a_i,2)$, and the column pair total equals the row pair total, so the ceiling equals $I$. The numerator and the denominator of the adjusted index are then equal, and the index equals $1$.
:::
:::

## Worked example — Six items, two against two
Label the items $1,\ldots,6$. Let the first partition be $\{1,2,3\}$ and $\{4,5,6\}$, and the second $\{1,2,4\}$ and $\{3,5,6\}$. The $2\times 2$ counts are
$$
\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$
Each margin is $(3,3)$, so each partition contains $C(3,2)+C(3,2)=6$ together-pairs, and $C(6,2)=15$. The together-in-both count is $C(2,2)+C(2,2)=2$. Pairs apart in both number $15-6-6+2=5$, so $7$ of $15$ pairs agree and the Rand index is $7/15=0.4667$ to four decimal places. The chance expectation is $6\cdot 6/15=2.4$. The ceiling is $6$. The adjusted index is
$$
\frac{2-2.4}{6-2.4}=-\frac{0.4}{3.6}=-\frac19\approx -0.111.
$$
The negative value means the partitions agree on fewer together-pairs than the margins alone would suggest.

**Your turn.** Keep the same margins and suppose the table is diagonal, $\begin{pmatrix}3&0\\0&3\end{pmatrix}$. Find $I$ and the adjusted index.

::: {.callout-tip collapse="true" title="Answer"}
$I=C(3,2)+C(3,2)=6$. The expectation is still $2.4$ and the ceiling is still $6$, so the index is $(6-2.4)/(6-2.4)=1$.
:::

## Connections — Agreement without matching names
The index is a comparison of two partitions, such as a clustering from [Lloyd's $k$-means algorithm](lloyd-s-k-means-algorithm.qmd) and a set of known labels. It does not require cluster $1$ to be class $1$. A [decision tree](decision-tree.qmd) also partitions the sample, but it does so with labelled leaves rather than with an agreement score between two groupings. The unadjusted count of agreeing pairs is the Rand index; the adjustment is what recentres the score.

## Check yourself
### One pair
How many pairs do $3$ items make, and how many do $6$ items make?

::: {.callout-tip collapse="true" title="Answer"}
$C(3,2)=3$ and $C(6,2)=15$. The worked example uses both of those counts.
:::

### A zero in the denominator
If every group in both partitions has size $1$, what is $I$, and why does the adjusted ratio become undefined?

::: {.callout-tip collapse="true" title="Answer"}
No pair is together in either partition, so $I=0$ and both pair totals are $0$. The expectation and the ceiling are $0$, and the correction divides by zero. There are no together-pairs whose chance agreement one could subtract.
:::
