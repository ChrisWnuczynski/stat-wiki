## Lead context
Quadratic discriminant analysis lets each class keep its own covariance, so the boundary between classes can bend.

## Motivating example
Two groups of measurements can share a centre-to-centre gap and still have different spreads. A rule that forces one common covariance cuts the space with a flat boundary. A rule that estimates a separate covariance for each class can put the wider class in charge of the tails, where its density dies away more slowly.{{cite:hastie_esl2009}} (§4.3, pp. 108–110)

## Intuition — What cancels, and what does not
Each class is modelled as multivariate normal. The Bayes rule picks the class with the largest product of prior probability and class density. With a shared covariance, the quadratic pieces $\mathbf{x}^\top\Sigma^{-1}\mathbf{x}$ are the same in every class and cancel in a comparison, leaving a flat boundary. Separate covariances leave the difference $\mathbf{x}^\top(\Sigma_j^{-1}-\Sigma_\ell^{-1})\mathbf{x}$ in place, and that difference is quadratic in $\mathbf{x}$.{{cite:hastie_esl2009}} (§4.3, eq. 4.9 and eq. 4.12, pp. 108–110)

## Definition — The quadratic score
For class $k$ with prior $\pi_k$, mean $\boldsymbol\mu_k$ and covariance $\Sigma_k$, the quadratic discriminant score is
$$
\delta_k(\mathbf{x})=-\frac12\log|\Sigma_k|-\frac12(\mathbf{x}-\boldsymbol\mu_k)^\top\Sigma_k^{-1}(\mathbf{x}-\boldsymbol\mu_k)+\log\pi_k.
$$
The plug-in rule replaces each unknown quantity by its class-wise estimate and predicts the class with the largest score. The boundary between two classes is the set where the two scores agree.{{cite:hastie_esl2009}} (§4.3, eq. 4.12, p. 109)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The normal density in class $k$ contributes the factor $(2\pi)^{-p/2}|\Sigma_k|^{-1/2}$ and the exponential of $-\frac12(\mathbf{x}-\boldsymbol\mu_k)^\top\Sigma_k^{-1}(\mathbf{x}-\boldsymbol\mu_k)$. In the comparison $\pi_k f_k(\mathbf{x})=\pi_\ell f_\ell(\mathbf{x})$ the common factor $(2\pi)^{-p/2}$ cancels. Taking logarithms leaves $\delta_k(\mathbf{x})=\delta_\ell(\mathbf{x})$. If $\Sigma_k=\Sigma_\ell=\Sigma$, the quadratic forms differ by a term linear in $\mathbf{x}$, because
$$
(\mathbf{x}-\boldsymbol\mu_k)^\top\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu_k)-(\mathbf{x}-\boldsymbol\mu_\ell)^\top\Sigma^{-1}(\mathbf{x}-\boldsymbol\mu_\ell)
$$
expands to a constant plus $2\mathbf{x}^\top\Sigma^{-1}(\boldsymbol\mu_\ell-\boldsymbol\mu_k)$. The boundary is then flat.{{cite:hastie_esl2009}} (§4.3, eq. 4.9–4.12)
:::
:::

## Worked example
Take two classes in one dimension, each with prior $1/2$. Class 1 is $N(0,1)$ and class 2 is $N(3,4)$. The scores agree at $x=1.418$ and at $x=-3.418$. Between those roots class 1 wins: at $x=0$ the scores are $-0.693$ and $-2.511$. Outside, the wider class wins. At $x=-4$, which is closer to $0$ than to $3$, the scores are $-8.693$ and $-7.511$, so class 2 is preferred. The extra variance, not the nearer mean, decides the far tail.

**Your turn.** Keep the same means, variances and equal priors. Evaluate both scores at $x=3$ and say which class is chosen.

::: {.callout-tip collapse="true" title="Answer"}
Class 1 has score $-\frac12(3)^2+\log\frac12=-5.193$. Class 2 has score $-\frac12\log 4+\log\frac12=-1.386$. Class 2 is chosen. The point sits on the class-2 mean, and the determinant penalty $-\frac12\log 4=-0.693$ is not large enough to overturn that.
:::

## Connections — Flat boundaries and extra parameters
[Linear discriminant analysis](linear-discriminant-analysis.qmd) is the shared-covariance case of the same normal model, and the [Bayes classifier](bayes-classifier.qmd) is the rule these scores estimate. A separate covariance for every class buys curved regions and spends more parameters: each new class brings its own $p(p+1)/2$ covariance entries. With a small class or a large $p$, that extra flexibility can follow noise in the training sample.{{cite:hastie_esl2009}} (§4.3, pp. 110–112)

## Check yourself

### Equal variances
Class 1 is $N(0,1)$, class 2 is $N(2,1)$, and the priors are equal. Is the decision boundary quadratic?

::: {.callout-tip collapse="true" title="Answer"}
No. The covariances agree, so the quadratic terms cancel. The boundary is the midpoint $x=1$, where the two normal log-densities with equal variance and equal prior are equal.
:::

### A one-dimensional parameter count
For $G=2$ classes and $p=1$ predictor, linear discriminant analysis estimates $4$ free parameters and quadratic discriminant analysis estimates $5$. Which extra parameter appears?

::: {.callout-tip collapse="true" title="Answer"}
Linear discriminant analysis uses two means, one shared variance and one free prior. Quadratic discriminant analysis replaces the shared variance by two class variances, which adds one parameter. The prior still contributes one free value because the two priors sum to $1$.
:::
