## Lead context
Concavity makes a finite score root sufficient for global optimality; it does not guarantee that a finite root exists.

## Motivating example
A logistic-regression optimiser reports a nearly zero score. Does this identify a local peak that might lose to a distant one? The Hessian answers that question for ordinary unpenalised Bernoulli logistic regression: the objective is concave throughout its finite coefficient space. Existence and identifiability must still be checked separately.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374){{cite:boyd_vandenberghe2004}} (§3.1.3, pp. 69–70)

## Statement
For fixed $X\in\mathbb R^{n\times p}$ and responses $y_i\in\{0,1\}$, let
$$
\ell(\beta)=\sum_i\{y_ix_i^\top\beta-\log(1+e^{x_i^\top\beta})\}.
$$
Every finite vector $\widehat\beta$ with $\nabla\ell(\widehat\beta)=0$ is a global maximiser over $\mathbb R^p$. If $X$ has full column rank, it is the unique maximiser. The statement is conditional on a finite stationary point; full rank alone does not ensure one exists.{{cite:boyd_vandenberghe2004}} (§3.1.3, pp. 69–70; §3.1.4, p. 71)

## Intuition — A tangent bounds the entire objective
For a differentiable concave function on a convex domain,
$$
\ell(\beta)\le\ell(\widehat\beta)+\nabla\ell(\widehat\beta)^\top(\beta-\widehat\beta).
$$
At a score root the tangent is horizontal, so it bounds all objective values by the value at that root. This is a global inequality, rather than a second-derivative check made only at the candidate.{{cite:boyd_vandenberghe2004}} (§3.1.3, p. 70)

## Proof
Write $p_i=\sigma(x_i^\top\beta)$, with $\sigma(\eta)=(1+e^{-\eta})^{-1}$. Differentiating gives $\sigma'=\sigma(1-\sigma)$ and hence
$$
\nabla\ell=X^\top(y-p),\qquad \nabla^2\ell=-X^\top WX,\qquad W=\operatorname{diag}(p_i(1-p_i)).
$$
Every finite predictor gives $0<p_i<1$. For every vector $v$,
$$
v^\top\nabla^2\ell\,v=-\sum_i p_i(1-p_i)(x_i^\top v)^2\le0.
$$
Therefore $\ell$ is concave. The tangent inequality proves global maximality at a finite stationary point. If $X$ has full column rank, $Xv\ne0$ for every $v\ne0$, making the quadratic form strictly negative. Strict concavity permits at most one maximiser.{{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374){{cite:boyd_vandenberghe2004}} (§§3.1.3–3.1.4, pp. 69–71)

## Key results — Rank and existence answer different questions
If $Xv=0$ for a nonzero $v$, then $X(\beta+tv)=X\beta$ for every $t$. The likelihood is constant on that line, so a finite maximiser cannot uniquely identify the coefficient vector. Its fitted linear predictor can nevertheless be identified.{{cite:boyd_vandenberghe2004}} (§A.5.1, nullspace)

For a concrete nonexistence example, take $(x,y)=(0,0),(1,1)$ with an intercept. Along $(\beta_0,\beta_1)=(-t,2t)$, both observed-label probabilities are $\sigma(t)$, so $\ell=2\log\sigma(t)$ increases toward zero as $t\to\infty$. Every finite value is negative. The design has full rank, but the supremum is approached only at diverging coefficients. The concavity theorem and this separated example are compatible: there is no finite score root in the example.{{cite:boyd_vandenberghe2004}} (§3.1.3, first-order optimality)

## Statistical use
A small score, a finite coefficient vector and adequate design rank address optimality and identifiability. They do not by themselves establish reliable Wald uncertainty: very weak curvature can make coefficient estimates unstable. Penalised likelihood changes the objective; convex penalties preserve concavity of the maximisation objective after subtraction, but nondifferentiable penalties need their appropriate optimality conditions.{{cite:boyd_vandenberghe2004}} (§3.2.1, sums and nonnegative weighted sums)

## Worked example
For an intercept-only sample $y=(0,0,1,1,1)$, the score is $3-5p$. Its root has $\widehat p=3/5$ and $\widehat\beta=\log(3/2)\approx0.405465$. The Hessian is $-5(3/5)(2/5)=-1.2$, and
$$
\ell(\widehat\beta)=3\log(3/5)+2\log(2/5)\approx-3.365058.
$$
The intercept column has rank one, so the stationary point is the unique global maximum. The negative curvature can also be verified directly from the one-variable log-likelihood.{{cite:boyd_vandenberghe2004}} (§3.1.3, pp. 69–70)

**Your turn.** For an intercept-only sample containing one zero and one one, find the root and its curvature.

::: {.callout-tip collapse="true" title="Answer"}
The score is $1-2p$, so $p=1/2$ and $\beta=0$. The Hessian is $-2(1/2)(1/2)=-1/2$. Full column rank makes this the unique finite maximiser.
:::
