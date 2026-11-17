## Lead context
A clique is a complete set of vertices that cannot be enlarged without dropping an edge.{{cite:evans2025_graphical}} (§4.3)

## Motivating example
On the six-vertex graph with edges $12$, $13$, $23$, $24$, $34$, $45$, $46$ and $56$, the cliques are $\{1,2,3\}$, $\{2,3,4\}$ and $\{4,5,6\}$. Vertex $4$ lies in two of them. The edge $\{2,4\}$ is complete but sits inside $\{2,3,4\}$, so it is not itself a clique.

## Intuition — Complete, and not extendable
A subset of vertices is complete when every two distinct members are adjacent. It is a clique when it is complete and maximal: no further vertex is adjacent to all of its members. A single edge is a clique when its endpoints have no common neighbour. A triangle is a clique when no fourth vertex is joined to all three. An edge inside that triangle is complete and not maximal, so it is not a clique. A single vertex is complete in every graph, and it is a clique only when it has no neighbour.{{cite:evans2025_graphical}} (§4.3)

## Definition
Let $G=(V,E)$ be an undirected graph without loops. A set $C\subseteq V$ is complete if every pair of distinct vertices in $C$ is an edge. It is a clique if it is complete and no set properly containing $C$ is complete.{{cite:evans2025_graphical}} (§4.3) Equivalently, no vertex outside $C$ is a neighbour of every vertex in $C$.

## Properties — The three sets, and no others
The claim about that six-vertex graph is an enumeration, not a modelling assumption.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The triples $\{1,2,3\}$, $\{2,3,4\}$ and $\{4,5,6\}$ are complete: each of the three edges in the first triple is present, likewise $23$, $24$ and $34$ in the second, and $45$, $46$ and $56$ in the third. None of them extends. Vertex $4$ is not joined to $1$, so it cannot join $\{1,2,3\}$. Vertex $1$ is not joined to $4$, so it cannot join $\{2,3,4\}$. Vertices $5$ and $6$ are not joined to $2$ or $3$. Vertex $1$ is not joined to $5$ or $6$, and vertex $2$ is not joined to $5$ or $6$, so nothing outside $\{4,5,6\}$ completes that triple.

Any other triple misses an edge. For instance $\{1,2,4\}$ lacks $14$, and $\{2,4,5\}$ lacks $25$. A set of four vertices would contain one of these incomplete triples. A complete pair that is not inside one of the three triples does not exist on the edge list, and every complete pair that does exist is contained in one of the three triples, so those pairs are not maximal. The clique list is therefore exactly the three triples.
:::
:::

## Worked example
Consider a smaller graph on vertices $\{1,2,3,4\}$ with edges $12$, $23$, $31$ and $34$. The triangle $\{1,2,3\}$ is complete. Vertex $4$ is joined to $3$ only, so it is not joined to $1$ or to $2$, and the triangle does not extend. The edge $\{3,4\}$ is complete, and no third vertex is joined to both $3$ and $4$, so $\{3,4\}$ is a second clique. The cliques are $\{1,2,3\}$ and $\{3,4\}$.

**Your turn.** Add the edge $14$ to that graph, and no other edge. Is $\{3,4\}$ still a clique? Is $\{1,3,4\}$ a clique?

::: {.callout-tip collapse="true" title="Answer"}
Vertex $1$ is now joined to both $3$ and $4$, so $\{3,4\}$ extends and is no longer a clique. The set $\{1,3,4\}$ has all three edges, and vertex $2$ is not joined to $4$, so $\{1,3,4\}$ is a clique. The triangle $\{1,2,3\}$ is still complete and does not extend, because $4$ is not joined to $2$. The edge $\{1,2\}$ sits inside that triangle, so it is not a clique. The cliques are $\{1,2,3\}$ and $\{1,3,4\}$.
:::

## Connections
Evans defines a density to factorise according to the graph when it is a product of potentials, one for each clique. That product is a statement about the joint distribution. The word clique itself remains a description of the graph.{{cite:evans2025_graphical}} (§4.3, eq. 4.1) The [precision matrix](precision-matrix.qmd) of a normal vector encodes the pairwise part of the same idea: a zero off-diagonal entry is a missing edge and a zero [partial correlation](partial-correlation.qmd). The six-vertex graph above has triangular cliques, so an edge potential can be absorbed into the potential of the triangle that contains it.

