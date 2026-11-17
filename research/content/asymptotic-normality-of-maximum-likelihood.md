## Lead context
A regular consistent likelihood maximiser is locally controlled by the sum of individual scores and the information matrix. Both the probability limit and the normal limit are needed to justify a Wald standard error.{{cite:self_liang1987}} (§1, assumptions and thm. 1, pp. 605–606)

## Motivating example
With $70$ successes in $200$ independent Bernoulli trials, the fitted probability is $0.35$. A normal approximation gives a standard error near $0.034$, but this approximation rests on an interior parameter and a regular likelihood. It cannot be transferred unchanged to an endpoint estimated by a sample maximum.{{cite:dodge2008}} (pp. 334–335, likelihood maximisation)

## Properties — Score, curvature and the local rate
For scalar $\theta$, write $S_n=\ell_n'$ and $i(\theta_0)=E_{\theta_0}[(\partial_\theta\log f(X;\theta_0))^2]>0$. At a consistent interior score root, Taylor expansion gives
$$
0=S_n(\theta_0)+(\widehat\theta-\theta_0)S_n'(\theta_0)
 +\tfrac12(\widehat\theta-\theta_0)^2S_n''(\theta^*).
$$
The remainder uses the second derivative of the score, which is the third derivative of log likelihood. An integrable uniform bound on individual third derivatives makes $n^{-1}S_n''(\theta^*)=O_p(1)$. Consistency makes its product with $\widehat\theta-\theta_0$ negligible. If the information identities, score central limit theorem and curvature law of large numbers hold, dividing the expansion gives
$$
\sqrt n(\widehat\theta-\theta_0)
=\frac{S_n(\theta_0)/\sqrt n}{-S_n'(\theta_0)/n+o_p(1)}
\Rightarrow N(0,i(\theta_0)^{-1}).
$$
Smoothness, finite positive information and an appropriate neighbourhood are substantive assumptions. A likelihood can have multiple local maxima, and consistency must identify the relevant maximising sequence.{{cite:self_liang1987}} (§1, assumptions and thm. 1; §2, thm. 2, pp. 605–607)

## Worked example
For Bernoulli probability $p$, the score is $(K-np)/\{p(1-p)\}$ and per-observation information is $i(p)=1/\{p(1-p)\}$. At $\widehat p=70/200=0.35$,
$$
\widehat{SE}=\sqrt{0.35(0.65)/200}=0.03373.
$$
Using $z_{0.975}=1.95996$ gives a Wald interval $[0.28390,0.41610]$. The curvature estimate is $200/\{0.35(0.65)\}=879.12088$. These formulas describe an approximation to the estimator's sampling law, rather than an exact parameter-free distribution for the binomial count.{{cite:dodge2008}} (pp. 44–45, binomial model; pp. 334–335, likelihood equations)

The Poisson Newton example has $n=7$ and sum $11$, so its exact maximum is $11/7=1.57143$. Five Newton steps from $1$ using the observed information reach $1.5714285714$. The closed-form maximiser supplies a numerical check on the iterative calculation.

**Your turn.** For $n=100$ and $K=50$, compute the information-based standard error and the approximate $95\%$ Wald interval.

::: {.callout-tip collapse="true" title="Answer"}
The standard error is $\sqrt{0.5(0.5)/100}=0.05$. The interval is approximately $[0.40200,0.59800]$.
:::

## Assumptions and limits
Efficiency comparisons need a regular local class of estimators. Pointwise consistency and a normal limit alone do not rule out superefficiency. For normal location with known unit variance, define $T_n=0$ when $|\bar X|\le n^{-1/4}$ and $T_n=\bar X$ otherwise. At mean zero it equals zero with probability tending to one; at each fixed nonzero mean it eventually behaves like $\bar X$. Its behaviour along local means of order $n^{-1/2}$ is irregular. This example explains why the class in an information-bound optimality statement matters.

A one-step score improvement from a root-$n$ consistent preliminary estimate shares the likelihood limit only with suitable local derivative and information convergence. Boundaries, singular information and parameter-dependent support require separate limits; cone projections can replace Gaussian laws at boundaries.{{cite:self_liang1987}} (§§1–2, pp. 605–607)
