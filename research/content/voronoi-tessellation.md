## Lead context
A Voronoi tessellation cuts space into the regions of points closest to each of a fixed set of centres.

## Motivating example
A map of clinics assigns every address to the nearest clinic. The boundary between two clinics is not an arbitrary curve. It is the set of addresses that are equally far from both, and it is a straight cut perpendicular to the line joining them. With three or more clinics those cuts stop where a third clinic becomes nearer, and the map is a tessellation by convex cells.{{cite:hastie_esl2009}} (§14.3.6, p. 510)

## Intuition — Nearest centre, then the mean of what landed there
Given centres $\mathbf{m}_1,\ldots,\mathbf{m}_K$, the cell of centre $k$ is every point $\mathbf{x}$ whose Euclidean nearest centre is $\mathbf{m}_k$. $K$-means alternates two steps that talk to these cells. Given the centres, each observation is assigned to the cell it falls in. Given the assignment, each centre moves to the mean of the observations in its cell. The boundaries drawn by the first step are the Voronoi tessellation of the current centres. The same cells, for a probability distribution rather than a finite sample, are the regions that define principal points: each principal point is the mean of the distribution inside its own cell.{{cite:hastie_esl2009}} (§14.3.6, p. 510; §14.5.3, p. 542)

## Definition — The cell and the two-centre boundary
The Voronoi cell of centre $\mathbf{m}_k$ is
$$
V_k=\{\mathbf{x}:\|\mathbf{x}-\mathbf{m}_k\|\le\|\mathbf{x}-\mathbf{m}_j\|\text{ for every }j\}.
$$
Ties, where two or more centres are equally near, form the boundary and have area zero under a continuous distribution. For two centres $\mathbf{a}$ and $\mathbf{b}$ the boundary is the hyperplane of points equidistant from both.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The inequality $\|\mathbf{x}-\mathbf{a}\|^2\le\|\mathbf{x}-\mathbf{b}\|^2$ expands to
$$
\|\mathbf{x}\|^2-2\mathbf{x}^\top\mathbf{a}+\|\mathbf{a}\|^2\le\|\mathbf{x}\|^2-2\mathbf{x}^\top\mathbf{b}+\|\mathbf{b}\|^2,
$$
so $2\mathbf{x}^\top(\mathbf{b}-\mathbf{a})\le\|\mathbf{b}\|^2-\|\mathbf{a}\|^2$. This is linear in $\mathbf{x}$. The midpoint $(\mathbf{a}+\mathbf{b})/2$ satisfies it with equality, and the coefficient of $\mathbf{x}$ is parallel to $\mathbf{b}-\mathbf{a}$, so the boundary is the hyperplane through the midpoint orthogonal to the segment joining the centres.
:::
:::

## Worked example
Let $\mathbf{a}=(0,0)$ and $\mathbf{b}=(6,2)$. Squaring both distances gives the boundary $3x+y=10$. The midpoint $(3,1)$ lies on it: $9+1=10$. The query $(2,1)$ has distances $\sqrt{5}=2.236$ and $\sqrt{17}=4.123$, so it belongs to the cell of $\mathbf{a}$. It also lies on the $\mathbf{a}$ side of the line, because $3\cdot 2+1=7<10$, while $\mathbf{b}$ itself gives $3\cdot 6+2=20>10$.

**Your turn.** Which cell contains $(4,0)$? Compute both distances.

::: {.callout-tip collapse="true" title="Answer"}
The distance to $\mathbf{a}$ is $4$ and the distance to $\mathbf{b}$ is $\sqrt{(4-6)^2+(0-2)^2}=\sqrt{8}=2.828$. The point belongs to the cell of $\mathbf{b}$. The line test agrees: $3\cdot 4+0=12>10$.
:::

## Connections — Clustering, prototypes, and convex cells
[Lloyd's $k$-means algorithm](lloyd-s-k-means-algorithm.qmd) redraws this tessellation at every assignment step, {{cite:hastie_esl2009}} (§14.3.6, p. 510) and the [$k$-means criterion](k-means-criterion.qmd) is the sum of squared distances to the centre of the cell. A cell is an intersection of half-spaces, one for each other centre, so it is convex. A third centre does not bend the pairwise boundary. It only shortens the piece of that boundary that remains active.
