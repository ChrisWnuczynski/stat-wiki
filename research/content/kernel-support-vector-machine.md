## Motivating example
Opposite corners of a square have the same label in XOR. A straight line in the input plane cannot separate the two diagonals, but their coordinate product distinguishes them immediately. A kernel support vector machine lets a linear separator use nonlinear features through inner products, so the algorithm can find a curved boundary without constructing every feature coordinate. The choice of kernel determines which geometry the margin uses.{{cite:goodfellow_bengio_courville2016}} (§§5.7.2, 6.1)

## Intuition — A linear separator in another geometry
A valid kernel is a function $K(x,z)=\langle\phi(x),\phi(z)\rangle$ for some feature map into an inner-product space. Its finite Gram matrices are symmetric positive semidefinite, since $a^\top K a=\|\sum_i a_i\phi(x_i)\|^2\ge0$. A nonlinear input boundary can therefore arise from a hyperplane $\langle w,\phi(x)\rangle+b=0$. The model is linear in the feature representation, while its predictions need not be linear in $x$.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, Support Vector Machines)

For $x\in\mathbb R^2$, the quadratic kernel has the explicit representation
$$\phi(x)=(1,\sqrt2x_1,\sqrt2x_1x_2,\sqrt2x_2,x_1^2,x_2^2)^\top,$$
because multiplying two such feature vectors gives $(1+x^\top z)^2$. This ordering makes the cross-product coordinate in the XOR calculation precise. Higher-degree polynomial expansions can become large, and Gaussian kernels correspond to infinite-dimensional representations, yet each prediction can still be computed using kernel values.{{cite:zhang_d2l2023}} (§11.2, similarity kernels, for Gaussian distance weighting){{cite:goodfellow_bengio_courville2016}} (§5.7.2, kernel trick)

## Properties — The penalty and the support vectors
The soft-margin primal minimizes
$$\frac12\|w\|^2+C\sum_i\xi_i,\qquad y_i(\langle w,\phi(x_i)\rangle+b)\ge1-\xi_i,\quad\xi_i\ge0.$$
Its dual uses the Gram matrix and bounds each multiplier by $C$. Large $C$ makes violations costly relative to feature-space norm; small $C$ allows more violations. The numerical meaning of $C$ depends on whether the loss is summed or averaged, and on kernel scaling. A kernel's bandwidth and $C$ should be tuned together with validation data.{{cite:holmes_huber2019_msmb}} (§12.6, regularization and cross-validation){{cite:goodfellow_bengio_courville2016}} (§5.7.2)

::: {.callout-note collapse="true" title="Proof of the finite kernel representation"}
::: {.proof}
Introduce multipliers $\alpha_i\ge0$ for the margin constraints and $\gamma_i\ge0$ for $\xi_i\ge0$. Stationarity in $w,b,\xi$ gives $w=\sum_i\alpha_i y_i\phi(x_i)$, $\sum_i\alpha_i y_i=0$, and $C-\alpha_i-\gamma_i=0$. Substituting the first identity into the Lagrangian yields the dual quadratic form and the bounds $0\le\alpha_i\le C$. Complementary slackness gives $y_k f(x_k)=1$ when $0<\alpha_k<C$, which proves the intercept formula. If no multiplier is strictly between its bounds, that particular formula has no eligible index; the KKT inequalities must instead determine an admissible intercept. The argument requires a positive semidefinite kernel for the convex norm interpretation.
:::
:::

## Worked example — Changing the margin penalty for XOR
The square's Gram matrix is $8I+\mathbf1\mathbf1^\top$, with eigenvalues $12,8,8,8$. Because the labels sum to zero, the rank-one term vanishes on the labelled multiplier vector. The hard-margin optimum $\alpha_i=1/8$ is thus unique. With a soft-margin bound $C\ge1/8$, it stays feasible and is still optimal. For $0<C<1/8$, symmetry and strict concavity give $\alpha_i=C$ and one admissible intercept is $b=0$. The decision function becomes $f(x)=-8Cx_1x_2$, and every training margin is $8C<1$. This illustrates that a correct training label need not have margin at least one in a soft-margin fit.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, margin and kernel classifier)

**Your turn.** Use $C=1/16$ for the four XOR points. What are their functional margins, and what is $f(0.5,-0.5)$?

::: {.callout-tip collapse="true" title="Answer"}
The decision function is $f(x)=-x_1x_2/2$. Each training margin is $1/2$, and $f(0.5,-0.5)=1/8>0$, predicting the positive class.
:::

## Statistical use — Scoring new observations
Prediction needs only training points with nonzero multipliers, the support vectors. Sparse multipliers can make scoring faster, although an SVM can have many support vectors. Input standardization must use training estimates before distances are computed. A decision score is a signed margin, not a posterior class probability; probability calibration requires an additional fitted relationship and an appropriate validation procedure.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, computational costs){{cite:holmes_huber2019_msmb}} (§12.5, probabilities and objective functions)
