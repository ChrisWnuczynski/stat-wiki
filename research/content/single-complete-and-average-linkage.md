## Lead context
Single, complete, and average linkage are three ways to turn distances between points into a distance between clusters while clusters are being merged.

## Motivating example
Four clinics sit on a line at positions $0$, $1$, $10$, and $12$. The closest pair is the first two clinics, one unit apart, and the next pair is the last two, two units apart. The question is how far the pair $\{0,1\}$ is from the pair $\{10,12\}$. Single linkage answers $9$, the gap between $1$ and $10$. Complete linkage answers $12$, the gap between $0$ and $12$. Average linkage answers $10.5$, the mean of the four cross gaps. The same points, and three different merges.{{cite:hastie_esl2009}} (§14.3, eqs. 14.41–14.43, pp. 523–524)

## Intuition
Agglomerative clustering starts with each observation as its own cluster and repeatedly merges the two closest clusters. "Closest" is undefined until a distance between groups is chosen. Single linkage uses the nearest pair of points, one from each group. Complete linkage uses the furthest pair. Average linkage uses the mean of every cross pair. If the clusters are tight and well separated, the three answers nearly agree. If points form a chain, they do not.{{cite:hastie_esl2009}} (§14.3, pp. 523–525)

## Definition
For groups $G$ and $H$ and pairwise dissimilarities $d_{ii'}$,
$$
d_{\mathrm{SL}}(G,H)=\min_{i\in G,\,i'\in H}d_{ii'},
$$
$$
d_{\mathrm{CL}}(G,H)=\max_{i\in G,\,i'\in H}d_{ii'},
$$
$$
d_{\mathrm{GA}}(G,H)=\frac{1}{N_G N_H}\sum_{i\in G}\sum_{i'\in H}d_{ii'}.
$$
Here $N_G$ and $N_H$ are the sizes of the groups. Dodge describes the same two extremes for Euclidean distance: single linkage takes the closest elements, and complete linkage takes the furthest.{{cite:dodge2008}} (p. 84){{cite:hastie_esl2009}} (§14.3, eqs. 14.41–14.43, p. 523)

## Interpretation — Order, scale, and chaining
Single and complete linkage depend only on the order of the dissimilarities. A strictly increasing transformation of every $d_{ii'}$ does not change which pair is nearest or furthest, so it does not change the merge sequence. Average linkage uses the numerical values. The same transformation can change which groups it merges.{{cite:hastie_esl2009}} (§14.3, p. 525)

Single linkage can chain. Points at $0$, $1$, $2$, and $10$ are merged by single linkage into $\{0,1,2\}$ before that cloud is joined to $10$, because each consecutive gap is $1$. The diameter of $\{0,1,2\}$ is $2$, and it keeps growing along the chain. Complete linkage resists that: the distance from $\{0,1\}$ to $2$ is the furthest gap, which is $2$, and the distance from $\{0,1,2\}$ to $10$ is $10$.{{cite:hastie_esl2009}} (§14.3, pp. 524–525)

## Properties
The three distances on the clinic pairs are exact, and the monotone-invariance claim is immediate from the formulas.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Label the clinics $A,B,C,D$ at $0,1,10,12$. Then $d(A,B)=1$, $d(C,D)=2$, and the four cross distances are $d(A,C)=10$, $d(A,D)=12$, $d(B,C)=9$, $d(B,D)=11$. The minimum is $9$, the maximum is $12$, and the average is $(10+12+9+11)/4=10.5$.

For the chain $0,1,2,10$, the cross distances from $\{0,1\}$ to $\{2\}$ are $2$ and $1$. Single linkage returns $1$, complete linkage returns $2$, and average linkage returns $1.5$. The cross distances from $\{0,1,2\}$ to $\{10\}$ are $10$, $9$, and $8$. Single linkage returns $8$, complete linkage returns $10$, and average linkage returns $9$.

If $h$ is strictly increasing, $\min h(d_{ii'})=h(\min d_{ii'})$ and $\max h(d_{ii'})=h(\max d_{ii'})$. The identity fails for an average: $h(10.5)$ need not equal the average of the transformed cross distances.{{cite:hastie_esl2009}} (§14.3, eqs. 14.41–14.43)
:::
:::

## Statistical use — Reading a dendrogram
Each merge has a height equal to the group distance at which it happened. A dendrogram draws those heights. For the clinics, single linkage joins $\{0,1\}$ at height $1$, $\{10,12\}$ at height $2$, and the two pairs at height $9$. Complete linkage uses heights $1$, $2$, and $12$. Average linkage uses $1$, $2$, and $10.5$. Cutting the dendrogram at a height between $2$ and $9$ yields the same two clusters under all three rules. Cutting between $9$ and $12$ still splits them under complete linkage and has already joined them under the other two.{{cite:hastie_esl2009}} (§14.3, pp. 520–524){{cite:dodge2008}} (p. 157)

## Worked example
Positions $0$, $1$, $10$, and $12$, with absolute distance.

Closest pair: $0$ and $1$, distance $1$, under every rule. Next: $10$ and $12$, distance $2$. The four cross distances are $10$, $12$, $9$, and $11$.

Single linkage then merges the pairs at $9$. Complete linkage merges them at $12$. Average linkage merges them at $10.5$. The within-pair distances never re-enter that last comparison.

**Your turn.** Points at $0$, $1$, and $4$. After merging $0$ and $1$, find the single, complete, and average distances from that pair to $4$.

::: {.callout-tip collapse="true" title="Answer"}
The cross distances are $4$ and $3$. Single linkage returns $3$, complete linkage returns $4$, and average linkage returns $3.5$.
:::

## Common misconceptions
Single linkage is not "the clusters are compact". It only requires one short bridge. A chain of close steps can produce a cluster whose farthest members are far apart.

Complete linkage is not "every member is close to the cluster centre". It requires every cross pair to be no farther than the recorded height. A point can still sit closer to another cluster's centre than to some member of its own cluster.

Average linkage is not invariant to a monotone rescaling of the distances. Converting kilometres to a squared distance changes the average and can change the merge, while single and complete linkage keep the same sequence.

## Assumptions and limits — When the three rules disagree
The formulas assume a dissimilarity for every pair of observations. A missing distance removes terms from the minimum, the maximum, and the average, and the three rules then answer different questions about the remaining pairs.

If the dissimilarities are not distances, the triangle inequality can fail. Single linkage will still chain along small values. The geometric picture of a chain in the line is then only an analogy.

Average linkage's population reading, as an estimate of $\iint d(x,x')\,p_G(x)p_H(x')\,\mathrm{d}x\,\mathrm{d}x'$, asks for the groups to be samples from two densities. A hand-picked set of four clinics is not such a sample. The number $10.5$ is then a summary of those four gaps, not an estimate of a population integral.{{cite:hastie_esl2009}} (§14.3, pp. 525–526)

## Connections
[Hierarchical clustering](hierarchical-clustering.qmd) is the sequence of merges these distances drive. A [dendrogram](dendrogram.qmd) records the heights. [Single linkage](single-linkage.qmd) is the minimum rule on its own. The same three choices appear whenever an algorithm must replace a set of pairwise numbers by one number for a pair of groups.

## Check yourself
### Four gaps
The cross distances between $\{0,1\}$ and $\{10,12\}$ are $10$, $12$, $9$, and $11$. What are the single, complete, and average linkages?

::: {.callout-tip collapse="true" title="Answer"}
The minimum is $9$, the maximum is $12$, and the average is $10.5$.{{cite:hastie_esl2009}} (§14.3, eqs. 14.41–14.43)
:::

### A chain of three
After merging positions $0$ and $1$, the distances to $2$ are $2$ and $1$. What does each rule return?

::: {.callout-tip collapse="true" title="Answer"}
Single linkage returns $1$, complete linkage returns $2$, and average linkage returns $1.5$.
:::

### A rescaling
Replace every distance $d$ by $d^2$. Do single linkage and average linkage still merge $\{0,1\}$ with $\{10,12\}$ at heights that are the squares of $9$ and $10.5$?

::: {.callout-tip collapse="true" title="Answer"}
Single linkage uses the smallest squared gap, $9^2=81$, which is the square of the old height. Average linkage averages $100$, $144$, $81$, and $121$, which equals $111.5$, not $10.5^2=110.25$. The average does not commute with squaring.{{cite:hastie_esl2009}} (§14.3, p. 525)
:::

## History
Dodge's account of cluster analysis defines single linkage as the Euclidean distance between the closest members of two classes and complete linkage as the distance between the furthest members, inside an agglomerative algorithm that rebuilds the distance table after each merge.{{cite:dodge2008}} (p. 84) Hastie, Tibshirani and Friedman add group-average linkage, the size-weighted mean of all cross dissimilarities, and they record that single and complete linkage depend only on the order of those dissimilarities.{{cite:hastie_esl2009}} (§14.3, pp. 523–525)
