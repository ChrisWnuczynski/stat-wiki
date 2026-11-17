## Motivating example — A nearest-centre allocation can still improve
A partition can assign every point to its closest current centroid and still allow a profitable single-point transfer once the affected centroids are recomputed. The objective compares the complete partition after a move, rather than distances to centres that are artificially held fixed. This distinction explains why a Hartigan transfer can leave a partition at which a Lloyd reassignment-and-recentring cycle has stopped.{{cite:hartigan_wong1979}} (pp. 100–101, Description and Purpose; Method)

## Definition — Optimise a partition by transfers
For fixed $K$, the algorithm seeks a partition of a finite dataset into nonempty clusters that reduces the within-cluster sum of squared Euclidean distances to their respective means. It is a partitional clustering procedure: the output is a collection of disjoint groups, rather than a hierarchy of nested groups. Choice of distance and scaling determines which observations count as close.{{cite:dodge2008}} (pp. 83–84, Cluster Analysis)

The Hartigan–Wong implementation organises transfers through an optimal-transfer stage and a quick-transfer stage. The optimal-transfer stage searches destination clusters using their current size-adjusted addition costs. The quick-transfer stage revisits a likely alternative destination for each point. A live set records clusters whose centres have changed, avoiding distance calculations whose conclusions cannot yet have changed. The algorithm targets a local optimum under point transfers, rather than comparing every possible partition.{{cite:hartigan_wong1979}} (pp. 100–101, Method, steps 1–7)

## Properties — Derive the size adjustment before choosing a move
For a cluster $C$ of size $n$ with mean $m$, write $W(C)=\sum_{i\in C}\|x_i-m\|^2$. The identity $W(C)=\sum_{i\in C}\|x_i\|^2-n\|m\|^2$ gives, for a member $x$ and $n>1$,
$$W(C)-W(C\setminus\{x\})=\frac{n}{n-1}\|x-m\|^2.$$
For a destination cluster $D$ of size $r$ and mean $u$,
$$W(D\cup\{x\})-W(D)=\frac{r}{r+1}\|x-u\|^2.$$
Subtract the removal saving from the addition cost to obtain the change in the total criterion. A strictly negative difference is an improving transfer. A singleton source cluster cannot be emptied while maintaining $K$ nonempty clusters.{{cite:hartigan_wong1979}} (p. 101, OPTRA and QTRAN size-adjusted distances)

The factors matter even for equally distant points. Removing a point allows its source centroid to move, amplifying the saving relative to its squared distance from the old mean. Adding the point allows the destination mean to move toward it, reducing the addition cost. The geometry of centroids and the sizes of both clusters therefore enter the comparison. Treating every transfer as a difference of unadjusted distances would implement a different procedure.

## Worked example — Escape the horizontal partition
Consider $(0,0),(0,1),(10,0),(10,1)$ and two clusters defined by the second coordinate. Their centres are $(5,0)$ and $(5,1)$ and the total within sum of squares is $100$. Every point is closer to its assigned centre: the squared distances are $25$ versus $26$. Nevertheless, moving $(10,0)$ into the upper cluster saves $2(25)=50$ from the lower cluster and adds $(2/3)(26)=52/3$ to the upper cluster. The total change is $-98/3$, leaving criterion $202/3\approx67.333333$.

The lower cluster is then the singleton $(0,0)$, while the upper mean is $(20/3,2/3)$. Moving $(0,1)$ from the upper cluster to the singleton cluster next reaches the vertical partition. The two vertical clusters each have within sum of squares $1/2$, so the total is one. The first transfer could not be discovered by simply asking whether the point was closer to the destination's old centroid.

**Your turn.** Before the first transfer, what is the removal saving for $(10,0)$ and the addition cost at the upper cluster?

::: {.callout-tip collapse="true" title="Answer"}
The removal saving is $2/(2-1)\times25=50$. The addition cost is $2/(2+1)\times26=52/3$. Their difference favours the transfer.
:::

## Assumptions and limits — A local criterion needs a data geometry
Every strict transfer decreases the objective. There are finitely many assignments of a finite dataset to $K$ labelled nonempty clusters, so an exact-arithmetic procedure accepting only strict decreases cannot continue indefinitely. A terminal partition need not be globally optimal; a simultaneous move of several points may improve it even if no single transfer does. Numerical implementations additionally need tolerances and iteration limits, so a software convergence code has to be inspected rather than inferred from the mathematical argument.{{cite:hartigan_wong1979}} (pp. 100–102, purpose, stopping steps and IFAULT)

Squared Euclidean distance gives variables with large numerical scales more influence. Standardisation changes that influence and therefore changes the fitted partition; it is not a neutral formatting operation. A cluster interpretation also presupposes that the selected variables and distance express a meaningful similarity. Several initialisations can reveal sensitivity to starting centres, but agreement across a finite set of starts does not certify the global optimum.{{cite:dodge2008}} (pp. 83–84, distance and structural assumptions in cluster analysis)
