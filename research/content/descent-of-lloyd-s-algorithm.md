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
