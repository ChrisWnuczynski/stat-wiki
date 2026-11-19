## Lead context
Scaling puts a likelihood improvement in units of the model's dispersion; its reference distribution still needs justification.

## Motivating example
Adding predictors usually improves a fitted likelihood. A raw improvement of ten units means different things when the response variance is one or one hundred. A dispersion scale makes the comparison interpretable, but estimating that scale does not turn every deviance difference into an exact F statistic.{{cite:nelder_wedderburn1972}} (§§2.3–2.4, pp. 375–376)

## Definition — Specify the dispersion convention
For independent exponential-dispersion observations with a common fixed $\phi$, compare a fitted mean model with a saturated model, which fits each observation's mean separately. Define the unscaled deviance by
$$
D=2\phi\{\ell_{\mathrm{sat}}(\phi)-\ell_{\mathrm{fit}}(\phi)\}.
$$
Then $D/\phi$ is the scaled deviance, a twice-log-likelihood difference at that same dispersion. Some authors use “deviance” for the scaled quantity; the definition and scale must therefore accompany numerical comparisons. For a homoscedastic Gaussian model $D$ is the residual sum of squares, while for an ordinary Poisson model $\phi=1$.{{cite:nelder_wedderburn1972}} (§2.3, p. 375)

For nested mean models $M_0\subset M_1$ of fitted ranks $p_0<p_1$, the saturated term cancels:
$$
T=\frac{D_0-D_1}{\phi}=2\{\ell_1(\phi)-\ell_0(\phi)\}.
$$
The difference is nonnegative when the fits maximise over the stated nested spaces. Different dispersions or a fitted nuisance parameter changing the likelihood comparison require additional care.{{cite:nelder_wedderburn1972}} (§2.4, p. 376)

## Interpretation — A nested comparison differs from goodness of fit
[]{#property-regular-deviance-calibration}
For regular identifiable nested models with the true parameter in the interior, fixed dimension and adequate information growth, a likelihood-ratio difference has an asymptotic chi-square reference with $p_1-p_0$ degrees of freedom. Boundary parameters, unidentified components and poorly supported cells can invalidate that reference. The distributional assertion is an approximation outside special models.{{cite:nelder_wedderburn1972}} (§2.4, p. 376)

A residual deviance compares the fitted model with a saturated model whose dimension may grow with sample size. It does not follow from the fixed-dimensional nested-model argument that $D/\phi$ always resembles $\chi^2_{n-p}$. For example, individual Poisson counts with small means can have deviance behaviour incompatible with that calibration even as the number of observations increases.{{cite:wuthrich_merz2022_glm}} (§5.3.1, pp. 143–144, Ex. 5.17)

## Properties — Why the F ratio has two divisors
For a Gaussian linear model with independent equal-variance errors, nested fixed design spaces and $n>p_1$, the null gives independent quantities
$$
(D_0-D_1)/\phi\sim\chi^2_{p_1-p_0},\qquad D_1/\phi\sim\chi^2_{n-p_1}.
$$
An orthonormal basis splits the normal error vector into the extra fitted directions and residual directions; independent standard normal coordinates give these sums of squares. Their normalised ratio is therefore exactly
$$
F=\frac{(D_0-D_1)/(p_1-p_0)}{D_1/(n-p_1)}\sim F_{p_1-p_0,n-p_1}.
$$
The deviance difference itself has no F distribution. Replacing dispersion by an estimate in another GLM may motivate an approximate F comparison, but the Gaussian orthogonal-coordinate proof is what gives this exact result.{{cite:nelder_wedderburn1972}} (§2.4, p. 376)

For a variance function $V(\mu)$ and unit observation weights, the Pearson estimate $\widehat\phi_P=(n-p)^{-1}\sum_i(y_i-\widehat\mu_i)^2/V(\widehat\mu_i)$ estimates scale from standardised residuals. A deviance-based estimate $D/(n-p)$ is a distinct choice whose reliability depends on the model and asymptotic regime.{{cite:wuthrich_merz2022_glm}} (§5.3.1, pp. 143–144, eq. 5.30)

## Worked example
For $x=(0,1,2,3)$ and $y=(1,2,2,5)$, the fitted line is $\widehat y=0.7+1.2x$. The intercept-only residual sum of squares is $D_0=9$, and the line's is $D_1=1.8$. There is one additional coefficient and two residual degrees of freedom, so
$$
\widehat\phi=1.8/2=0.9,\qquad F=\frac{9-1.8}{0.9}=8.
$$
Under a Gaussian constant-variance model with zero slope, the exact reference is $F_{1,2}$ and the upper-tail probability is approximately $0.105573$. The large reduction in residual sum of squares comes with only two degrees of freedom for estimating variance. If $\phi$ were known to equal one instead, the statistic would be $7.2$ with an exact $\chi^2_1$ reference. These are different inferential settings.{{cite:nelder_wedderburn1972}} (§§2.3–2.4, pp. 375–376)

**Your turn.** Multiply all response values by ten. What happens to the estimated dispersion and F statistic?

::: {.callout-tip collapse="true" title="Answer"}
Both residual sums of squares and the variance estimate multiply by $100$, giving estimated dispersion $90$. The numerator and denominator of F have the same factor, so F stays $8$.
:::
