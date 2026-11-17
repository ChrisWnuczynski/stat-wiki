## Motivating example
A nonnegative matrix of spectral intensities may contain several recurring component patterns. A low-rank factorization can represent each observed spectrum as a weighted combination of those patterns. Requiring both the patterns and their weights to be nonnegative gives an additive representation: one component cannot cancel another with a negative coefficient. This constraint makes the approximation different from an unconstrained low-rank singular-value decomposition.{{cite:lee_seung2001_algorithms}} (§§1–2)

Linear factor models more broadly reconstruct observations from a lower-dimensional code. The constraints and distributional assumptions decide the interpretation of that code. Nonnegativity alone does not turn a component into a chemically identifiable constituent or establish a probabilistic model for the measurements.{{cite:goodfellow_bengio_courville2016}} (Ch. 13, eqs. 13.1–13.2)

## Definition — Constrain the factors, then choose a loss
For a matrix $V\in\mathbb R_+^{m\times n}$ and selected rank $r$, choose $W\in\mathbb R_+^{m\times r}$ and $H\in\mathbb R_+^{r\times n}$ to approximate $V\approx WH$. One objective is $\tfrac12\lVert V-WH\rVert_F^2$. Another is the generalized Kullback–Leibler divergence $\sum_{ij}\{V_{ij}\log(V_{ij}/(WH)_{ij})-V_{ij}+(WH)_{ij}\}$. Zero entries require the convention $0\log(0/z)=0$ and appropriate handling when the fitted entry is zero. Choosing a loss expresses which reconstruction discrepancies matter.{{cite:lee_seung2001_algorithms}} (§3, eqs. 2–3)

The divergence is not generally symmetric. When both matrices are normalized probability arrays it reduces to the usual KL divergence, but normalization is an additional condition. For count-like observations, a Poisson log likelihood leads to this divergence up to terms depending only on the observations. Squared error instead corresponds to a constant-variance Gaussian noise criterion when such a probabilistic interpretation is appropriate.{{cite:lee_seung2001_algorithms}} (§3)

## Properties — Separate convexity does not give a joint convex problem
With $W$ fixed, squared error is convex in $H$; with $H$ fixed it is convex in $W$. The joint objective contains their products and is generally nonconvex. Alternating between the factors can reduce the objective without finding its global minimum. A low reconstruction error also does not identify unique factors.{{cite:lee_seung2001_algorithms}} (§§3–4)

For any positive diagonal $D$, $(WD)(D^{-1}H)=WH$. Permuting corresponding factor columns and coefficient rows preserves the product too. These transformations prove scale and permutation nonidentifiability directly. Additional normalizations can fix a scale convention, but they do not in general establish uniqueness beyond these simple transformations.

### Multiplicative descent {#multiplicative-descent}
For strictly positive starting factors, the squared-error multiplicative updates are
$$H\leftarrow H\odot\frac{W^\top V}{W^\top WH},\qquad W\leftarrow W\odot\frac{VH^\top}{WHH^\top},$$
where products and quotients outside matrix products are entrywise. Apply the updates sequentially, using the new $H$ in the second step. The auxiliary-function argument establishes a nonincreasing squared-error objective. A zero entry can remain locked at zero, so initialization and denominator handling matter. Objective descent by itself is weaker than a guarantee of a globally optimal or unique factorization.{{cite:lee_seung2001_algorithms}} (§4, thm. 1; §5)

## Worked example — One alternating update
Let $V=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $r=1$, $W=(1,1)^\top$ and $H=(1,1)$. The starting squared-error objective with its one-half factor is seven. Updating $H$ gives $(2,3)$ and reduces the objective to two. The next update gives $W=(8/13,18/13)^\top$. The reconstructed matrix is
$$WH=\frac1{13}\begin{pmatrix}16&24\\36&54\end{pmatrix},$$
and the objective becomes $1/13=0.0769231$. Every entry stays nonnegative. The update has improved the reconstruction substantially, while the input data matrix has rank two and cannot be exactly reproduced at rank one. These calculations instantiate the stated update rule.{{cite:lee_seung2001_algorithms}} (§4, thm. 1)

The same reconstructed matrix arises after doubling $W$ and halving $H$. The two pairs of factors differ numerically but express the same additive approximation. Comparing factor estimates between runs therefore needs a scale convention and a correspondence between components.

**Your turn.** Suppose $V=\begin{pmatrix}1&2\\2&4\end{pmatrix}$. Give an exact nonnegative rank-one factorization and its squared-error objective.

::: {.callout-tip collapse="true" title="Answer"}
Take $W=(1,2)^\top$ and $H=(1,2)$. Their product is exactly $V$, so the objective is zero.
:::

## Connections — Reconstruction, sparsity and validation
Nonnegative factors often produce localized additive representations, but nonnegativity is not the same constraint as sparsity. A factor can be positive in every coordinate. Sparse coding explicitly introduces a preference for small numbers of active coefficients, for example through an absolute-value penalty. These are different ways to control a low-dimensional representation.{{cite:goodfellow_bengio_courville2016}} (§13.4, eq. 13.18)

The selected rank, preprocessing and reconstruction loss all influence the components. Centering a nonnegative matrix by subtracting column means usually introduces negative entries and changes the feasibility of this model. A sensible analysis checks reconstruction on relevant held-out entries or observations and examines stability across initializations. An interpretable component should be supported by the scientific measurement process as well as by a numerical factorization.

Nonnegativity of both factors keeps each reconstruction inside the cone generated by the chosen columns. Dropping that sign restriction changes the problem into an ordinary low-rank factorisation.
