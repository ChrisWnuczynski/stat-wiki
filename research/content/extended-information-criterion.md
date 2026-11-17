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
