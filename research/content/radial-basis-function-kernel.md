## Motivating example
Two observations can be similar because they are close in the recorded feature space, even when a straight-line boundary cannot separate their classes. A Gaussian radial basis function kernel turns distance into similarity without requiring the analyst to construct every nonlinear feature explicitly. It is useful in support vector machines and Gaussian processes, but its scale parameter is meaningful only relative to the scale of the inputs.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, kernel machines, pp. 138–142)

## Definition — Distance determines similarity
For $x,x'\in\mathbb R^p$ and length scale $\ell>0$, define
$$k_\ell(x,x')=\exp\left[-\frac{\|x-x'\|^2}{2\ell^2}\right].$$
The alternative parameterisation is $k_\gamma(x,x')=e^{-\gamma\|x-x'\|^2}$ with $\gamma=1/(2\ell^2)>0$. Equal inputs have similarity one. Increasing distance decreases similarity, while increasing $\ell$ makes similarity decline more slowly. The kernel is stationary because it depends only on the difference, and isotropic because it depends on that difference only through its Euclidean norm.{{cite:rasmussen_williams2006}} (§4.2.1, equation 4.9, pp. 82–83)

A finite Gram matrix has entries $K_{ij}=k_\ell(x_i,x_j)$. Its positive semidefiniteness is the property needed to use it as an inner-product matrix or a covariance matrix. Positivity of individual entries alone would not establish that property. A valid kernel must give a nonnegative quadratic form for every finite set of inputs and every real coefficient vector.{{cite:rasmussen_williams2006}} (§4.1, positive semidefinite covariance functions, pp. 79–81)

## Properties — An infinite collection of polynomial features
Expanding the squared distance gives
$$k_\ell(x,x')=e^{-\|x\|^2/(2\ell^2)}e^{-\|x'\|^2/(2\ell^2)}e^{x^Tx'/\ell^2}.$$
For a multi-index $\alpha=(\alpha_1,\ldots,\alpha_p)$ of nonnegative integers, define
$$\phi_\alpha(x)=e^{-\|x\|^2/(2\ell^2)}\frac{x^\alpha}{\ell^{|\alpha|}\sqrt{\alpha!}}.$$
The product of exponential power series gives $k_\ell(x,x')=\sum_\alpha\phi_\alpha(x)\phi_\alpha(x')$. Also $\sum_\alpha\phi_\alpha(x)^2=k_\ell(x,x)=1$. Hence the feature vector is square-summable and every finite Gram quadratic form equals a sum of squares, proving positive semidefiniteness. Polynomial features of every degree appear, which explains why the feature representation is not restricted to a fixed finite polynomial degree.{{cite:rasmussen_williams2006}} (§4.2.1, squared-exponential covariance and feature-space construction, pp. 83–84)

For distinct fixed inputs, $\gamma\to\infty$ drives off-diagonal Gram entries to zero, giving the identity matrix in the limit. As $\gamma\downarrow0$, all entries tend to one. These limits describe the similarity matrix, rather than guaranteeing a particular test error: the fitted procedure also depends on labels, regularisation and training size.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, Gaussian kernels and support vector machines)

## Worked example — Three points on a line
Take inputs $0,1,2$ and length scale $\ell=1$. Similarities at separations 1 and 2 are $e^{-1/2}=0.606531$ and $e^{-2}=0.135335$. Thus
$$K=\begin{pmatrix}1&0.606531&0.135335\\0.606531&1&0.606531\\0.135335&0.606531&1\end{pmatrix}.$$
For coefficients $c=(1,-1,0)$, the quadratic form is $c^TKc=2(1-e^{-1/2})=0.786939$. Doubling the length scale changes the similarity of points separated by one to $e^{-1/8}=0.882497$, showing that the larger scale treats them as more similar.

**Your turn.** With length scale one, at what distance does similarity equal $e^{-2}$?

::: {.callout-tip collapse="true" title="Answer"}
Solve exp(−r²/2)=exp(−2). The nonnegative distance is r=2.
:::

## Statistical use — Input scaling and kernel width interact
Multiplying every input by a positive constant $a$ while keeping $\ell$ fixed is equivalent to dividing the length scale by $a$ on the previous coordinates. To preserve every similarity, multiply $\ell$ by the same constant instead. With coordinate-specific scales, a product kernel can use separate length scales, replacing squared distance by $\sum_j(x_j-x_j')^2/\ell_j^2$. This states a different metric on feature space.{{cite:rasmussen_williams2006}} (§4.2.1, characteristic length scale; §5.1, automatic relevance determination)

Scaling parameters and kernel parameters should be fitted inside the training portion of an assessment procedure. In a classification model, kernel width and the regularisation cost act jointly: a highly local feature map with a strong penalty can behave differently from the same map with a weak penalty. The similarity formula alone does not select either setting or turn a decision score into a calibrated posterior probability.{{cite:goodfellow_bengio_courville2016}} (§§5.3 and 5.7.2, hyperparameters and kernel classification)

## Common misconceptions — Infinite features do not eliminate finite computation
A kernel method can evaluate a finite Gram matrix directly while representing an infinite-dimensional feature map implicitly. Its numerical cost depends on the number of observations and the fitting algorithm. The existence of that feature map says nothing by itself about independence of observations, model calibration or whether the measurement units define a useful notion of distance.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, kernel trick)

## Interpretation — Length scale and the gamma convention name one width
The identity $\gamma=1/(2\ell^2)$ converts the two standard parameterisations. Length scale $\ell=2$ is $\gamma=1/8=0.125$. At unit distance the similarity is $e^{-1/8}=0.882497$ under that wider kernel, compared with $e^{-1/2}=0.606531$ when $\ell=1$. The distance at which the $\ell=1$ kernel equals $e^{-2}$ solves $r^2/(2\ell^2)=2$. With $\ell=1$ the nonnegative solution is $r=2$, the separation already used for the corner of the three-point Gram matrix. These conversions are exact. They do not choose a width for a particular training set.{{cite:rasmussen_williams2006}} (§4.2.1, equation 4.9, pp. 82–83)

As $\gamma$ grows, distinct fixed inputs become orthogonal in the Gram matrix. For the inputs $0,1,2$, every off-diagonal entry tends to zero and the diagonal stays one, so the limit is $I_3$. The quadratic form $c^TKc$ for $c=(1,-1,0)$ tends to $2$. At $\ell=1$ that form is $0.786939$, already below $2$ because the neighbouring inputs remain similar. The opposite limit, $\gamma\downarrow0$, sends every entry to one. A coefficient vector that sums to zero then has quadratic form tending to zero, which is a reminder that a very wide kernel sees those three inputs as almost the same point.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, Gaussian kernels and support vector machines)

### Statistical use — Positive semidefiniteness is a property of every finite set
The feature expansion shows $c^TKc=\sum_\alpha(c^\top\phi_\alpha)^2\ge0$ for every real $c$ and every finite input list. Symmetry of $K$ is immediate from $\|x-x'\|=\|x'-x\|$. Positive entries are a weaker property: a matrix of positive numbers can still have a negative eigenvalue. The three-point matrix in the example has smallest eigenvalue safely positive, since the displayed quadratic form on a contrast is positive and the diagonal dominance is visible, but the general guarantee is the sum-of-squares representation rather than a check of one matrix. A kernel that fails on some configuration of inputs cannot be used as a covariance function on all of $\mathbb R^p$.{{cite:rasmussen_williams2006}} (§4.1, positive semidefinite covariance functions, pp. 79–81){{cite:rasmussen_williams2006}} (§4.2.1, squared-exponential covariance and feature-space construction, pp. 83–84)

## Connections
Changing the units of an input is a change of $\ell$ unless the length scale is transformed with the input. That is the same bookkeeping required when [scaling](scaling.qmd) a variable before a variance-based method. In a classifier the kernel supplies similarities, and a probability model such as [softmax](softmax-is-multinomial-logistic-regression.qmd) is a further choice about how scores become class probabilities. The kernel formula does not make that second choice.{{cite:rasmussen_williams2006}} (§4.2.1, characteristic length scale; §5.1, automatic relevance determination)
