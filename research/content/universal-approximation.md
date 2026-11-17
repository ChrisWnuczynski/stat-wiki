## Motivating example
A straight line cannot fit every curved response on an interval, even if its coefficients are estimated perfectly. Adding nonlinear hidden units changes the available function class. An approximation theorem asks whether this class can get arbitrarily close to a target throughout a domain, before asking how weights could be learned from a finite noisy sample. Keeping those questions separate makes the theorem useful without confusing representation with statistical performance.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 194–195)

## Definition — The error and the quantifiers
For a continuous target $f$ on the compact cube, uniform error is
$$\|F-f\|_\infty=\sup_{x\in[0,1]^p}|F(x)-f(x)|.$$
The assertion is: for every such $f$ and every $\varepsilon>0$, there exist a finite width and real weights giving error below $\varepsilon$. The width and weights may depend on both $f$ and $\varepsilon$. This is density of a union of finite-width model classes, rather than exact representation by one fixed network size.{{cite:cybenko1989}} (thm. 2, pp. 307–308)

A continuous sigmoidal function tends to zero at negative infinity and one at positive infinity. The logistic function is an example. A linear output combination is essential because its coefficients can be negative and its output can exceed the range of the activation. A single final logistic output always lies between zero and one and therefore cannot uniformly approximate an unrestricted real-valued target such as the constant $2$.{{cite:cybenko1989}} (§1, p. 303; thm. 2, pp. 307–308)

## Properties — Continuity sets a boundary
Finite networks with continuous activations produce continuous functions. A uniform limit of continuous functions is continuous: choose one approximating function within $\varepsilon/3$ of the limit, use its continuity near a point, then add the three errors. Thus a discontinuous step function on an interval cannot be uniformly approximated to arbitrarily small error by continuous networks. In fact a jump from zero to one forces uniform error at least $1/2$ for every continuous approximation.

Approximation in probability or in an integral norm is weaker than uniform approximation. A steep sigmoid can make a narrow transition zone whose probability is small, even while its largest pointwise error near a jump stays substantial. A theorem for measurable functions must therefore specify its mode of approximation.{{cite:cybenko1989}} (thm. 3, pp. 309–310, approximation outside a small set)

## Worked example — A constructive curved approximation
For a concrete construction use the rectified linear unit $r(t)=\max(0,t)$. Linear interpolation of $f(x)=x^2$ at knots $0,1/4,1/2,3/4,1$ gives
$$F(x)=\tfrac14x+\tfrac12r(x-\tfrac14)+\tfrac12r(x-\tfrac12)+\tfrac12r(x-\tfrac34),\qquad0\le x\le1.$$
On this domain the first term is also $\tfrac14r(x)$, so all four summands can be hidden-unit outputs. The initial slope is $1/4$ and each hinge raises the slope by $1/2$, giving successive slopes $1/4,3/4,5/4,7/4$. On a knot interval $[a,b]$, the interpolation line minus $x^2$ is $(x-a)(b-x)$. Its maximum is $(b-a)^2/4$, reached at the midpoint. Here every interval has length $1/4$, so the exact uniform error is $1/64=0.015625$.

This is a fully specified network and an error certificate for one target. It illustrates the distinction between a constructive approximation and a general existence theorem. The ReLU construction uses a different activation from the sigmoidal theorem, while both belong to broader families of approximation results.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 194–196, activation classes and depth)

**Your turn.** Interpolate $x^2$ with equally spaced knots $0,1/2,1$. Find the interpolation value at $x=1/4$ and the maximum error. How many equal subintervals suffice to make this interpolation error at most $0.01$?

::: {.callout-tip collapse="true" title="Answer"}
The first segment joins $(0,0)$ to $(1/2,1/4)$ and has value $1/8$ at $1/4$. The target is $1/16$, so the error is $1/16=0.0625$, also the maximum over both intervals. With $m$ equal subintervals, the maximum is $1/(4m^2)$. The condition $1/(4m^2)\le0.01$ gives $m\ge5$.
:::

## Statistical use — Three different errors
Approximation error measures the best attainable fit within an architecture. Optimisation error measures failure to find suitable weights in that class. Statistical error measures the effect of observing finitely many noisy training cases rather than the population relationship. Increasing width can reduce the first while complicating the other two. A training algorithm and validation design address issues that an existence theorem leaves open.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 194–195)

Depth can encode repeated composition efficiently. Universality of one hidden layer does not give an efficient width bound for every target, and it gives no fixed sample size that learns every continuous function. The cube contains infinitely many functions with arbitrarily fine variation. A useful learning guarantee needs further restrictions on target complexity, sampling and noise.

## Assumptions and limits
The general sigmoidal density theorem uses a separation argument for function spaces and measures. The explicit interpolation calculation establishes its own error bound without establishing that general theorem. The distinction matters when extending the target domain, removing compactness, changing the activation or demanding derivative approximation: each extension needs a suitable theorem with its own hypotheses.
