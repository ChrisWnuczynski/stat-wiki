## Motivating example

Two fits to the same two-component mixture can describe the same density while reporting their component means in opposite orders. Averaging the first reported means then combines different physical clusters. Label switching is a symmetry of the model that must be respected when defining a summary.{{cite:stephens2000}} (§§1–2, pp. 795–797)

## Definition — Permuting an entire component

For $f(x)=\sum_{j=1}^K\pi_j f_j(x;\theta_j)$, a permutation must move each weight together with its component parameter. For any permutation $\sigma$,
$$
\sum_j\pi_{\sigma(j)}f_j(x;\theta_{\sigma(j)})
=\sum_j\pi_j f_j(x;\theta_j),
$$
when the components belong to the same parametric family and $f_j$ denotes that common family evaluated at its parameter. Thus the sampling density has no preferred numbering. Positive-weight distinct components in an identifiable finite-mixture family can be recovered only up to their order; coincident components or zero weights can introduce further ambiguities.{{cite:green2019_finite_mixtures}} (Ch. 1, §1.3.1, pp. 13–14)

## Interpretation — What a posterior average is averaging

If the prior is also permutation invariant, the posterior shares the likelihood symmetry. Label-specific posterior means can then collapse distinct groups into similar summaries. A chain that stays near one labelling can instead conceal the symmetry: stable traces of component-specific means alone do not establish that all relevant posterior regions were explored.{{cite:stephens2000}} (§§2–3, pp. 796–800)

Useful targets include the predictive density, sorted means where that ordering has a scientific interpretation, and co-clustering probabilities $P(Z_i=Z_j\mid x)$. The last event survives every joint permutation of the allocations. Parameter ordering changes the representation; it does not create information separating two genuinely overlapping populations.{{cite:green2019_finite_mixtures}} (Ch. 1, §1.3.1, pp. 13–14){{cite:stephens2000}} (§§3–4, pp. 798–803)

## Worked example

Consider two equivalent parameter vectors for unit-variance normal mixtures:
$$
A:\ (\pi_1,\mu_1,\pi_2,\mu_2)=(0.3,-2,0.7,2),
\qquad B:\ (0.7,2,0.3,-2).
$$
For either vector, the density at zero is $\phi(2)\approx0.053991$ and the mixture mean is $0.3(-2)+0.7(2)=0.8$. Averaging the raw coordinates of $A$ and $B$ instead gives weights $(0.5,0.5)$ and means $(0,0)$. That averaged parameter vector gives density $\phi(0)\approx0.398942$ at zero and mean zero. Averaging equivalent density functions and evaluating the density at averaged parameters are different operations. Matching the lower mean to the lower mean before averaging returns vector $A$. This example illustrates the label-specific averaging problem.{{cite:stephens2000}} (§2.2, pp. 796–798)

**Your turn.** If allocation vectors $(1,1,2)$ and $(2,2,1)$ occur in two draws, which pairs are co-clustered?

::: {.callout-tip collapse="true" title="Answer"}
Observations one and two are together in both draws; each is separate from observation three. The three pairwise co-clustering indicators are $(1,0,0)$ in either labelling.
:::

## Connections — Matching components across fits

Relabelling procedures choose permutations to make a stated loss or comparison meaningful. Sorting one-dimensional means is a simple choice; multidimensional components have no single natural order. A relabelling rule should therefore follow the target of the analysis. Prediction can often avoid labelling altogether, whereas statements about a named component need a scientific or mathematical matching rule.{{cite:stephens2000}} (§§3–4, pp. 798–803)

