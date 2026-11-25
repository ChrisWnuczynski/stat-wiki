## Motivating example
A squared-distance clustering problem has two coupled choices: which cluster each observation belongs to, and where each cluster centre lies. Lloyd's algorithm alternates between them. It assigns each observation to a closest centre and then replaces every nonempty cluster's centre by its arithmetic mean. Each operation solves one part of the problem while holding the other part fixed.{{cite:lloyd1982}} (§§IV–VI, pp. 130–132)

## Statement
For observations $x_1,\ldots,x_n\in\mathbb R^d$, assignments $z_i\in\{1,\ldots,K\}$ and centres $\mu_1,\ldots,\mu_K$, define $J(z,\mu)=\sum_i\|x_i-\mu_{z_i}\|^2$. A nearest-centre assignment step cannot increase $J$. Replacing the centre of each nonempty assigned group by its mean also cannot increase $J$. The statement assumes squared Euclidean distance and a centre update that minimises the objective for the chosen assignments. Different distances generally require a different centre update.{{cite:lloyd1982}} (§IV, best quanta; §V, best partition)

## Proof
For fixed centres, replacing $z_i$ by any nearest-centre index changes its contribution to $\min_k\|x_i-\mu_k\|^2$, no larger than its earlier contribution. Summing proves descent for assignment. For a nonempty cluster $C$ with mean $\bar x_C$, expand
$$\sum_{i\in C}\|x_i-\mu\|^2=\sum_{i\in C}\|x_i-\bar x_C\|^2+|C|\|\mu-\bar x_C\|^2.$$
The cross-term vanishes because the centred observations sum to zero. The second term is nonnegative and is minimised at the mean, proving descent for the centre update. The identity is the finite-sample form of a squared-error projection.{{cite:lloyd1982}} (§IV); {{cite:nist_ls_straight2002}} (§4.4.3.1, squared-error minimisation)

## Key results — Descent need not locate the global optimum
The objective values form a nonincreasing sequence bounded below by zero, so those values converge. This alone does not prove convergence to a unique centre configuration or to a global minimum. Ties can move assignments without changing the objective, and different initial centres can lead to different stationary configurations. A deterministic tie convention and an explicit policy for empty clusters make the algorithm well specified.{{cite:lloyd1982}} (§VI, necessary conditions and multiple stationary points)

## Worked example
### Watch both parts decrease the sum
For one-dimensional observations $(0,2,8,10)$, start with centres $(0,8)$ and assign to nearest centres. The groups are $(0,2)$ and $(8,10)$, giving objective $0+4+0+4=8$. Updating their centres to $(1,9)$ reduces the objective to $1+1+1+1=4$. Reassignment leaves those groups unchanged, so this run has reached a fixed assignment. The fall from eight to four is exactly the sum of cluster-size-weighted squared movements of the centres: $2(1-0)^2+2(9-8)^2=4$.{{cite:lloyd1982}} (§§IV–VI)

**Your turn.** Keep the first group $(0,2)$ fixed, but put its centre at $3$. What is its squared-distance objective, and how much does returning to its mean reduce it?

::: {.callout-tip collapse="true" title="Answer"}
Its objective is $(0-3)^2+(2-3)^2=10$. The mean is 1, where the objective is 2, so the reduction is 8.
:::

## Common misconceptions — Stop because the numerical criterion is satisfied
A small objective decrease is a stopping criterion, rather than proof of scientific cluster structure. The chosen number of clusters, feature scaling and distance can dominate the resulting partition. Scaling one feature changes the relative squared distances and can therefore change both assignments and centres. Repeated starts help investigate optimisation sensitivity, while substantive interpretation still needs the measurement context.{{cite:lloyd1982}} (§VI, local and absolute minima)


## Statistical use — Monitor the objective through complete iterations
Record the objective after assignment and again after the centre update. Each recorded value should be no larger than the preceding value when both operations follow the stated squared-distance rule. An increase is a reason to inspect distance calculations, missing observations, empty-cluster handling and centre updates. Comparing several initialisations can reveal different achieved objectives for the same data and cluster count. Such comparisons assess the optimisation calculation while leaving the choice of cluster count and measurement scale as additional modelling decisions.{{cite:goodfellow_bengio_courville2016}} (§5.8.2, k-means clustering)

## Intuition
Lloyd's algorithm never tries to solve the joint problem in one step. With the centres held fixed, each observation should be given to a nearest centre, because its contribution to $J$ is then as small as that menu of centres allows. With the labels held fixed, each centre should move to the mean of its group, because the sum of squared Euclidean distances to a set of points is minimised at their average. The worked run starts at centres $(0,8)$ on the points $(0,2,8,10)$. Assignment produces groups $(0,2)$ and $(8,10)$ and cost $8$. The means $(1,9)$ cut the cost to $4$. A further assignment does not move anyone. The decrease $8-4=4$ equals $2(1-0)^2+2(9-8)^2$, the size-weighted squared movement of the two centres.

The mean is the only centre with that guarantee for squared Euclidean distance. For the two points $0$ and $2$ the mean is $1$, and the within-group cost is $(0-1)^2+(2-1)^2=2$. Placing the centre at $3$ instead costs $(0-3)^2+(2-3)^2=10$. For the three points $0,0,3$ the mean is $1$ and the cost is $(0-1)^2+(0-1)^2+(3-1)^2=6$. A median minimises the sum of absolute deviations, not the sum of squares. Using a median as the centre update in a squared-distance algorithm gives up the descent proof.

## Related concepts — The objective converges, and the partition need not be unique
Each accepted step produces a value of $J$ no larger than the previous value, and $J$ cannot fall below zero. A nonincreasing sequence that is bounded below converges to some limit. The limit is a number. It need not be the global minimum of $J$ over all partitions into $K$ groups, and the sequence of centres need not converge to a single configuration if ties allow several assignments with the same cost. Different initial centres on the same points can stop at different costs. The algorithm is a descent method for a nonconvex objective. Descent explains the monotone trace. It does not explain which basin the start fell into.{{cite:lloyd1982}} (§VI, necessary conditions and multiple stationary points)

Empty clusters are a specification detail the descent identity does not settle. If a centre loses every point, there is no mean to compute. A rule that leaves the centre where it was, or that reseeds it at a distant point, has to be stated before two implementations can be compared. A tie on the assignment boundary, an observation equally distant from two centres, can be given to either index without changing $J$. The next centre update can still differ. A deterministic tie break makes the map from centres to the next centres a function.

### Cluster count, scaling and initialisation
A small final value of $J$ is sometimes read as evidence that the data contain $K$ well separated groups. The singleton partition has $J=0$ for any data set in which each point may have its own centre. The raw minimum over $K$ is therefore a poor selector of $K$. Lloyd's algorithm, run at a fixed $K$, finds a stationary partition for that $K$. The choice of $K$ is an input. Scaling a coordinate multiplies the squared gaps on that coordinate and can change both the assignments and the means. Standardising before clustering is a modelling choice. It is not implied by the descent theorem, and skipping it is also a modelling choice.

Stopping when the drop in $J$ falls below a tolerance ends the computation. It does not certify a global optimum, and it does not certify that a nearby start would have produced the same partition. Several random starts, with the attained costs recorded, are a probe of that sensitivity. The lowest cost among them is the best cost found, not a proof that no better partition exists.{{cite:lloyd1982}} (§VI, local and absolute minima)

## Generalizations — The same cancellation as a one-way decomposition
The centre-update identity is the one-dimensional form of a least-squares projection onto the constant vector inside each cluster. The cross term vanishes because residuals from a mean sum to zero, the same cancellation that splits a one-way sum of squares into within-group and between-group parts. The assignment step is what makes the design, the cluster labels, depend on the current fit. Alternating between a label update and a weighted mean is also the structure of a hard-assignment EM algorithm for a mixture of spherical Gaussians, in the limit where the component variances tend to zero and the responsibilities become $0$ or $1$. The monotone decrease of $J$ is the clustering form of that likelihood increase. A soft assignment with positive responsibilities optimises a different objective.
