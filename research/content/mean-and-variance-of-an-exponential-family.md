## Motivating example — One derivative can replace several integrations
A normal, a Poisson and a binomial distribution have different probability formulas, yet their means and variances can be recovered by differentiating their log-normalising functions. This is useful in likelihood fitting because it relates distributional moments to score equations and curvature. The derivative rule needs a common support and justified interchange of differentiation with integration or summation; it is not a consequence of the notation alone.{{cite:nelder_wedderburn1972}} (§1.1, p. 371)

## Key results — Fix the sign and scale conventions
Write a one-parameter exponential dispersion family as
$$f(y;\eta,\phi)=\exp\!\left\{\frac{y\eta-A(\eta)}{a(\phi)}+d(y,\phi)\right\},\qquad a(\phi)>0,$$
with $\phi$ fixed during differentiation. On an open natural-parameter domain where the derivatives may pass through the normalising integral,
$$\mathbb EY=A'(\eta),\qquad \operatorname{Var}(Y)=a(\phi)A''(\eta).$$
With the alternative numerator $y\eta+c(\eta)$, set $c=-A$ to obtain the negative signs in the corresponding formulas. Mixing those two conventions would turn a nonnegative variance into a negative number.{{cite:nelder_wedderburn1972}} (§1.1, p. 371, eqs. 1–6)

## Proof
Because the density integrates to one, its derivative integrates to zero. Its score is $(y-A'(\eta))/a(\phi)$. Therefore $0=\int\partial_\eta f=(\mathbb EY-A'(\eta))/a(\phi)$, proving the mean identity. Differentiate the centred identity $\int(y-A'(\eta))f\,dy=0$ once more. The product rule gives
$$0=-A''(\eta)+\frac1{a(\phi)}\mathbb E[(Y-A'(\eta))^2].$$
Using the first identity converts the expectation into a variance and proves the second. For a mass function, replace each integral with a sum. The support being independent of $\eta$ prevents boundary terms from being omitted.{{cite:nelder_wedderburn1972}} (§1.1, p. 371)

## Generalizations — The gradient and Hessian describe sufficient statistics
For a vector family $f_\theta(x)=h(x)\exp\{\theta^\top T(x)-A(\theta)\}$, the same differentiation gives $\nabla A(\theta)=\mathbb E_\theta T(X)$ and $\nabla^2A(\theta)=\operatorname{Cov}_\theta(T(X))$. The Hessian is positive semidefinite because $v^\top\nabla^2A v=\operatorname{Var}(v^\top T)\ge0$. A nonzero direction with zero variance corresponds to a linear relation among the sufficient statistics. A minimal regular representation excludes such constant directions, making the Hessian positive definite and the cumulant strictly convex.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1)

If the scalar exponent instead contains $b(\theta)a(y)+c(\theta)$, the statistics and parameter must be distinguished. Differentiating gives $b'(\theta)\mathbb E[a(Y)]+c'(\theta)=0$. Unless $a(y)=y$ and $b(\theta)=\theta$, this is not directly the simple formula for $\mathbb EY$. Reparameterisation can recover a natural parameter, but the chain rule must be carried through rather than discarding $b'$.

## Statistical use — Curvature also measures information
For a single observation in the displayed dispersion family, the score variance is $\operatorname{Var}(Y)/a(\phi)^2=A''(\eta)/a(\phi)$. Under the same regularity conditions this equals the expected negative second derivative of the log-likelihood, giving the Fisher information for the natural parameter. For independent observations, information contributions add. The relation explains why the variance function enters iterative weighted fitting for generalised linear models.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1, pp. 371–373)

## Worked example — Three checks of the derivative rule
For a Bernoulli response, $A(\eta)=\log(1+e^\eta)$ and $a=1$. At $\eta=\log4$, the success probability is $4/5$, the mean is $4/5$, and the variance is $4/25$. For a binomial count of five independent such trials, the cumulant is five times larger, giving mean four and variance $4/5$.

For a Gamma variable with fixed shape three and natural parameter $\eta<0$, take $A(\eta)=-3\log(-\eta)$ and absorb the remaining density factors into $h$. Then $A'=-3/\eta$ and $A''=3/\eta^2$. At $\eta=-1/2$, the mean is six and the variance is twelve. The natural parameter is negative even though the mean is positive; it is the negative rate, not the mean itself.{{cite:nelder_wedderburn1972}} (§§3.2–3.4, pp. 377–381)

**Your turn.** For a Poisson family with $A(\eta)=e^\eta$, what are the mean and variance at $\eta=\log3$?

::: {.callout-tip collapse="true" title="Answer"}
Both derivatives are $e^\eta$, so both the mean and variance equal three.
:::

## Common misconceptions — A moment-generating function is a different transform
The first two derivatives of a moment-generating function at zero give $\mathbb EY$ and $\mathbb EY^2$. Its second derivative therefore needs a squared-mean subtraction to become a variance. A cumulant-generating function is the logarithm of that transform and has the variance as its second derivative at zero. The log partition function is related to the cumulant-generating function by shifting the natural parameter, which is why it has the same cumulant structure.{{cite:wainwright_jordan2008}} (§3.5.1, prop. 3.1)
