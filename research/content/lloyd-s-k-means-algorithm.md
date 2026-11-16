## Lead context
Lloyd’s algorithm alternates between giving each point the nearest centre and replacing each centre by the mean of its points.

## Motivating example
Five points in a plane can be split into two groups in many ways. Trying every split is possible. Twenty-five points into five groups is not a calculation one does by hand: the number of unlabelled partitions grows as a Stirling number of the second kind. Lloyd’s iteration replaces that search by two cheap updates.

## Intuition — Each step is easy, and the pair is not
With the centres held fixed, each point should join the centre closest to it in squared Euclidean distance. With the labels held fixed, the centre of a cluster should be the coordinate-wise mean, because that mean minimises the sum of squared distances inside the cluster. Doing both at once is a hard combinatorial problem. Doing one and then the other cannot raise that sum, but it can stop at a split that a different start would have beaten.

## Definition — Assignment and the mean update
Choose centres $m_1,\ldots,m_K$. Repeat until the labels stop changing:

1. Set $C(i)=\arg\min_k\|x_i-m_k\|^2$, keeping the current label if a point is equally close to two centres.
2. Replace $m_k$ by the mean of the points with $C(i)=k$.

An empty cluster has no mean, so this description assumes every cluster stays nonempty.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a fixed label set with $N_k\ge 1$ points, 
$$
\sum_{C(i)=k}\|x_i-m\|^2=\sum_{C(i)=k}\|x_i-\bar x_k\|^2+N_k\|\bar x_k-m\|^2.
$$
The second term is zero only at $m=\bar x_k$, so the mean update does not increase the sum of squares. With centres fixed, giving a point a farther centre cannot decrease its own term, so the assignment step does not increase the sum either.
:::
:::

## Worked example
Take the points $0,1,10$ and centres $0$ and $10$. Squared distances send $0$ and $1$ to the first centre and $10$ to the second. The updated centres are $0.5$ and $10$. The within-cluster sum of squares is
$$
(0-0.5)^2+(1-0.5)^2+(10-10)^2=0.5.
$$
The next assignment is unchanged, so the algorithm stops. The partition $\{0,1\}$ and $\{10\}$ is a fixed point of these two steps. Another start can stop at a different partition.

**Your turn.** Start from centres $0$ and $10$ on the points $0,8,10$. Give the centres after the first mean update and the within-cluster sum of squares at that pair of centres.

::: {.callout-tip collapse="true" title="Answer"}
The point $8$ is closer to $10$ than to $0$, so the clusters are $\{0\}$ and $\{8,10\}$. The new centres are $0$ and $9$, and the sum of squares is $(8-9)^2+(10-9)^2=2$.
:::

## Connections — Local minima and other moves
The [within-cluster sum of squares](k-means-criterion.qmd) is the objective these two steps do not increase. A [Hartigan–Wong step](hartigan-wong-algorithm.qmd) can move one point and recompute two means together, which Lloyd’s separate updates do not try. The number of partitions is why the iteration is used at all: $S(4,2)=7$, while $S(10,3)=9330$.

## Check yourself

### Pairs and means {#self-check-ex-sl-04-1}

For a set of $N$ points with mean $\bar x$, why is $\sum_i\sum_l\|x_i-x_l\|^2=2N\sum_i\|x_i-\bar x\|^2$?

[Question-bank page](../questions/ex-sl-04-1.qmd)

::: {.callout-tip collapse="true" title="Answer"}
Expand $\|x_i-x_l\|^2=\|x_i-\bar x\|^2+\|x_l-\bar x\|^2-2(x_i-\bar x)^{\mathsf T}(x_l-\bar x)$. The cross term sums to zero because the deviations from the mean sum to zero. Each squared deviation is then counted $2N$ times.
:::

### Counting partitions {#self-check-ex-sl-04-2}

How many ways are there to split $\{1,2,3,4\}$ into two nonempty unlabelled clusters, and what is $S(10,3)$?

[Question-bank page](../questions/ex-sl-04-2.qmd)

::: {.callout-tip collapse="true" title="Answer"}
There are seven splits: four of type $1\mid 3$ and three of type $2\mid 2$. The Stirling number $S(10,3)$ equals $9330$.
:::
