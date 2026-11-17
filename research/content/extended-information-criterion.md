## Lead context
The extended Bayesian information criterion penalises both parameter dimension and the multiplicity of candidate models. The graphical-model version counts possible edges as well as fitted edges.{{cite:foygel_drton2010}} (§1, eq. 1)

## Motivating example
Adding three edges increases a fitted log likelihood by $10$. That improvement always helps fit, but it must pay a penalty for searching a larger model space. Ordinary BIC and an extended criterion can therefore select different graphs from the same list of candidates.{{cite:chen_chen2008_ebic}} (§2, extended-criterion formula)

## Properties — A graph-selection score is not a fitting penalty
For a fixed graph, the Gaussian concentration matrix must be positive definite and have zeros at missing edges. The score uses the maximum likelihood over that constrained model, not the objective value used to generate a candidate through an $\ell_1$ penalty. A penalised path supplies candidate edge sets; an unpenalised constrained refit supplies the likelihood term required in this version of EBIC.{{cite:foygel_drton2010}} (§2.1, eq. 2; §3, simulations)

In the general model-space construction, assigning smaller prior probability to each member of a large class contributes an extra $2\gamma\log\tau$ penalty, where $\tau$ counts models of comparable size. The graphical form uses $4\gamma|E|\log p$ to account for the scale of searching edges among $p$ vertices. This is a multiplicity charge, not an estimate of prediction error.{{cite:chen_chen2008_ebic}} (§2, model prior and extended criterion){{cite:foygel_drton2010}} (§1, eq. 1)

## Worked example
Let $n=120$, $p=8$. Compare graphs with $7$ and $10$ edges and maximised log likelihoods $-300$ and $-290$. For any $\gamma$, subtracting the smaller graph's criterion from the larger graph's gives
$$
\Delta=-20+3\log120+12\gamma\log8.
$$
At $\gamma=0$, $\Delta=-5.63752$, so ordinary BIC chooses the ten-edge graph. At $\gamma=0.5$, $\Delta=6.83913$, so EBIC chooses the seven-edge graph. The crossover is $\gamma=0.22592$; at this value the scores tie. These likelihoods define an illustrative comparison, rather than the outcome of the simulated chain sample.

An eight-vertex chain has $7$ edges, while there are $\binom82=28$ possible unordered edges. A Gaussian AR(1) covariance with entries $0.6^{|j-k|}$ has tridiagonal inverse, so its conditional-independence graph is that chain. The population zero pattern gives a target against which a selection method can be evaluated; a finite sample need not recover every edge.{{cite:foygel_drton2010}} (§2.1, Gaussian concentration graph; §2.2, consistency assumptions)

**Your turn.** With $n=100$, $p=10$ and $\gamma=1/2$, how much must the maximised log likelihood improve to justify one extra edge?

::: {.callout-tip collapse="true" title="Answer"}
The extra penalty is $\log100+2\log10=4\log10$. Since likelihood enters as $-2\ell$, the improvement must exceed $2\log10=4.60517$.
:::

## Assumptions and limits
The consistency result for the graphical criterion imposes restrictions on graph size, signal strength, dimension growth and the candidate class, including decomposability in the stated theorem. It does not guarantee exact graph recovery for every graphical-lasso path or finite sample. A candidate list that omits the relevant graph cannot select it, whatever the score. Singular data can also make the constrained likelihood fail to attain a finite maximum.{{cite:foygel_drton2010}} (§2.2, main theorem)

## Intuition
A criterion for choosing a graph has to charge two different luxuries. The first is the number of edges actually fitted, because each edge spends a parameter. The second is the number of graphs that could have been tried. Ordinary BIC charges the first. The extended criterion adds a charge that grows with the size of the search. A gain of $10$ in the maximised log likelihood always improves the likelihood term. Whether it pays for one more edge depends on the sample size, the number of vertices, and the multiplicity parameter $\gamma$.{{cite:chen_chen2008_ebic}} (§2, extended-criterion formula)

## Definition
For a candidate graph with edge set $E$, the graphical EBIC uses the maximised Gaussian log likelihood $\ell_E$ of the covariance under the constraint that the concentration matrix is zero on the missing edges. One form of the comparison is
$$
\mathrm{EBIC}_\gamma(E)=-2\ell_E+|E|\log n+4\gamma|E|\log p.
$$
The middle term is the usual BIC charge for $|E|$ free concentration parameters in this edge-counting convention. The last term is the extended charge. At $\gamma=0$ the extended charge disappears. The likelihood in $\ell_E$ is the unpenalised constrained maximum. Substituting the penalised graphical-lasso objective would mix the selection penalty into the goodness-of-fit term and would no longer be the criterion stated here.{{cite:foygel_drton2010}} (§1, eq. 1){{cite:foygel_drton2010}} (§2.1, eq. 2; §3, simulations)

## Statistical use
Compare two nested candidates by the difference of their scores. In the worked numbers, moving from $7$ edges to $10$ edges with $n=120$ and $p=8$ changes the criterion by $-20+3\log 120+12\gamma\log 8$. The likelihood improvement is worth $20$ on the $-2\ell$ scale. The BIC piece costs $3\log 120\approx 14.36$, so at $\gamma=0$ the larger graph still wins by about $5.64$. The extended piece at $\gamma=1/2$ costs another $6\log 8\approx 12.48$ and reverses the choice. The scores tie at $\gamma\approx 0.226$. For a single extra edge at $n=100$, $p=10$ and $\gamma=1/2$, the same arithmetic asks the maximised log likelihood to improve by more than $2\log 10\approx 4.605$. That hurdle is the sum of a $\log n$ piece and a $2\gamma\log p$ piece, converted from the $-2\ell$ scale back to the log-likelihood scale.{{cite:chen_chen2008_ebic}} (§2, model prior and extended criterion)

## Common misconceptions
The extended term is not an estimate of prediction error, and it is not the $\ell_1$ penalty used to draw a graphical-lasso path. If $p$ grows while $n$ and the fitted edge count stay fixed, and if $\gamma>0$, the term $4\gamma|E|\log p$ increases. The criterion becomes stricter because there are more possible edges to have searched, not because the fitted graph has more parameters. A candidate list that never includes the relevant graph cannot be rescued by a smaller score. Consistency theorems also restrict the class of graphs, the signal strength, and the growth of $p$ with $n$. A finite sample, a singular covariance, or a nondecomposable graph outside those conditions can make the formal guarantee inapplicable even though the score can still be computed.{{cite:foygel_drton2010}} (§2.2, main theorem){{cite:foygel_drton2010}} (§2.1, Gaussian concentration graph; §2.2, consistency assumptions)

## History
The extended criterion adds a charge that grows with the number of candidate graphs, not only with the number of edges that were fitted. In the numerical comparison, $n=120$ and $p=8$, and the move from seven edges to ten edges changes the score by $-20+3\log 120+12\gamma\log 8$. At $\gamma=0$ that change is about $-5.64$, so the larger graph is preferred. At $\gamma=1/2$ the extra charge $6\log 8$ is about $12.48$ and the smaller graph is preferred. The two scores meet near $\gamma=0.226$.

A single extra edge has a simpler hurdle. With $n=100$, $p=10$ and $\gamma=1/2$, the maximised log likelihood must improve by more than $2\log 10$, about $4.605$, before the larger graph wins. The binomial count of possible edges among eight vertices is $\binom{8}{2}=28$. A penalty built from that count is a statement about the search space. Substituting a penalised fitting objective for the maximised likelihood would charge the edges twice, once inside the fit and again in the criterion.{{cite:chen_chen2008_ebic}} (§2, model prior and extended criterion)
