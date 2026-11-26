## Lead context
A CDF describes discrete, continuous, and mixed laws within the same framework for interval probabilities, quantiles, and tail risks. The value *at* a jump includes the probability mass at that point.{{cite:billingsley1995}} (§14, pp. 188–189)

## Motivating example — At most four on a die, and a smooth rise
The probability that a fair die shows at most four is four sixths. Asking the same question for every threshold gives its whole CDF: it stays flat between die faces and jumps by one sixth at each face. By contrast, the CDF of a continuously distributed measurement can rise smoothly. Both are answers to the same threshold question, with the same definition.{{cite:billingsley1995}} (§14, pp. 188–189)

## Intuition — Accumulating probability from left to right
Think of a CDF as probability accumulated while a threshold moves from left to right. It starts near zero, never falls, and approaches one. A vertical jump records an atom, or positive probability at an exact value. A smooth rise records probability spread over an interval. A flat stretch says that interval has no probability under the model. The CDF is therefore a more general description than a probability mass function or density alone.{{cite:billingsley1995}} (§14, pp. 188–189)

## Definition — $F(x)=\mathbb{P}(X\le x)$
For a real-valued [random variable](random-variable.qmd) $X$, its **cumulative distribution function** is

$$
F_X(x)=\mathbb P(X\le x),\qquad x\in\mathbb R.
$$

In the CDF definition, $x$ is a fixed real threshold, $\mathbb P$ is the probability measure, and the event $\{X\le x\}$ includes equality. The subscript may be dropped when only one variable is under discussion. The law of $X$ assigns probabilities to Borel sets on the real line; the CDF records its values on the half-lines $(-\infty,x]$. Those values determine the entire law, because half-lines determine interval probabilities and generate the Borel sets.{{cite:kolmogorov1933_slln}} (Ch. III, §2){{cite:billingsley1995}} (§14, pp. 188–189)

For $a<b$, the half-open interval probability is $\mathbb P(a<X\le b)=F_X(b)-F_X(a)$. Define the left limit $F_X(a-)=\lim_{y\uparrow a}F_X(y)=\mathbb P(X<a)$. Then the point mass at $a$ is $\mathbb P(X=a)=F_X(a)-F_X(a-)$, and $\mathbb P(a\le X\le b)=F_X(b)-F_X(a-)$. These endpoint distinctions vanish at values without an atom, but they matter for discrete and mixed laws.{{cite:billingsley1995}} (§14, pp. 188–189)

## Properties — Monotonicity, right-continuity, and the quantile inverse
Every CDF is nondecreasing and right-continuous, with limits zero as $x\to-\infty$ and one as $x\to+\infty$. Conversely, any real function with those four properties is the CDF of some probability distribution. Right-continuity is part of the present $\le$ convention: at a jump, the value of the function is its height *after* including the atom. It concerns endpoint values at jumps.{{cite:billingsley1995}} (§14, pp. 188–189)

For a discrete distribution with values $x_i$ and masses $p_i=\mathbb P(X=x_i)$, $F_X(x)=\sum_{x_i\le x}p_i$; each jump has height $p_i$. For an absolutely continuous distribution with density $f_X$, $F_X(x)=\int_{-\infty}^{x}f_X(t)\,\mathrm dt$, and $F_X'(x)=f_X(x)$ almost everywhere. A continuous CDF need not have a density, so differentiating an arbitrary continuous CDF is not a universal recipe for its law.{{cite:billingsley1995}} (§14, pp. 188–189){{cite:durrett2019}} (§1.2, pp. 10–13)

For $0<u<1$, define the generalized inverse or quantile by $Q(u)=\inf\{x:F_X(x)\ge u\}$. The infimum is the first threshold at which the accumulated probability reaches $u$. If $U$ is uniform on $(0,1)$, then $Q(U)$ has CDF $F_X$, including when $F_X$ jumps or has flat intervals. This construction is the [inverse-transform method](inverse-transform-method.qmd).{{cite:billingsley1995}} (§14, pp. 188–189)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $a<b$, then $\{X\le a\}\subseteq\{X\le b\}$, so monotonicity of probability makes $F_X(a)\le F_X(b)$. The events $\{X\le x_n\}$ decrease to $\{X\le x\}$ when $x_n\downarrow x$; continuity of a finite probability measure from above gives $F_X(x_n)\downarrow F_X(x)$. This is right-continuity. The events $\{X\le n\}$ increase to the whole sample space as $n\to\infty$, and $\{X\le -n\}$ decrease to the empty set; continuity of probability gives the two limits.{{cite:billingsley1995}} (§14, pp. 188–189)

The disjoint identity $\{X\le b\}=\{X\le a\}\sqcup\{a<X\le b\}$ proves the half-open interval formula. As $y\uparrow a$, the events $\{X\le y\}$ increase to $\{X<a\}$, which proves the left-limit identity. Subtracting that event from $\{X\le a\}$ gives the jump probability, and subtracting it from $\{X\le b\}$ gives the closed-interval formula. The discrete sum is the union of the atoms at or below $x$. For a density, integrating over $(-\infty,x]$ gives the displayed integral and the fundamental theorem of calculus yields its derivative where applicable.{{cite:billingsley1995}} (§14, pp. 188–189)

To prove the inverse-transform claim, right-continuity and monotonicity imply $\{x:F_X(x)\ge u\}=[Q(u),\infty)$ for $0<u<1$. Hence $Q(u)\le x$ exactly when $u\le F_X(x)$. For uniform $U$, $\mathbb P\{Q(U)\le x\}=\mathbb P\{U\le F_X(x)\}=F_X(x)$. This also proves the converse CDF characterization: on a uniform probability space, the generalized inverse of any nondecreasing right-continuous function with the two stated limits is a random variable with that CDF. Its half-open interval probabilities are the differences of $F$, so the function fixes the law on all Borel sets.{{cite:billingsley1995}} (§14, pp. 188–189)

For the maximum of independent variables, $\{\max(X_1,\ldots,X_n)\le m\}=\bigcap_{i=1}^{n}\{X_i\le m\}$. Independence of the $X_i$ makes the event probability the product $\prod_iF_i(m)$; the event identity itself does not require independence.{{cite:durrett2019}} (§2.1){{cite:billingsley1995}} (§14, p. 190)
:::
:::

## Interpretation — Staircases, smooth rises, and the inverse-transform reading
The distribution-function comparison shows a fair die's staircase CDF alongside an exponential law's smooth CDF. The jump at a die face is the probability of that face, while a vertical difference between two thresholds on the smooth curve is the probability of falling between them. Inverse-transform sampling reverses this reading: a uniform height on the probability axis selects the first threshold at which the CDF reaches that height. At a jump, an interval of uniform heights selects the same outcome, producing an atom.{{cite:billingsley1995}} (§14, pp. 188–189)

## Statistical use — The empirical CDF, tails, and quantiles
For observations $X_1,\ldots,X_n$, the [empirical distribution function](../notes/ur-02-probability-and-simulation.qmd#s-an-empirical-distribution-and-a-kernel-density) is $F_n(x)=n^{-1}\sum_{i=1}^{n}\mathbf1\{X_i\le x\}$, where $\mathbf1$ is one when its condition holds and zero otherwise. It estimates the population CDF without first choosing a parametric density. For observed values $1,1,2,4,7$, it gives $F_5(2)=3/5$; the jump at $1$ is $2/5$. A comparison of $F_n$ with a fitted CDF can reveal where a model puts too much or too little probability.{{cite:billingsley1995}} (§20, pp. 268–269)

In risk reporting, $F_X(c)$ is the probability of a result at or below threshold $c$, while $1-F_X(c)$ is the probability of exceeding it. For a one-sided threshold decision, name the direction and whether equality counts. Quantiles invert the question: for a target probability $u$, find a threshold $Q(u)$ whose cumulative probability reaches at least $u$. In simulation, apply that generalized inverse to uniform draws; a strictly increasing ordinary inverse is unnecessary.{{cite:billingsley1995}} (§14, pp. 188–189)

## Worked example — An atom at zero and a uniform remainder
Suppose $X=0$ with probability $1/4$; otherwise draw uniformly from $(0,1)$. Its CDF is $0$ for $x<0$, $1/4+3x/4$ for $0\le x<1$, and $1$ for $x\ge1$. The jump at zero is $F_X(0)-F_X(0-)=1/4$. The probability of $0<X\le1/2$ is $F_X(1/2)-F_X(0)=5/8-1/4=3/8$; including zero instead gives $F_X(1/2)=5/8$. The median under the generalized-inverse convention solves $1/4+3x/4=1/2$, giving $Q(1/2)=1/3$. This one example requires both an atom and a density to describe the full law, while one CDF covers both.{{cite:billingsley1995}} (§14, pp. 188–189)

**Your turn.** For this same law, find $\mathbb P(X=0)$ and $Q(1/8)$ from the CDF alone.

::: {.callout-tip collapse="true" title="Answer"}
The jump at zero gives $\mathbb P(X=0)=F_X(0)-F_X(0-)=1/4$. Since the CDF first reaches $1/8$ at zero, $Q(1/8)=0$; solving $F_X(x)=1/8$ as if the CDF were everywhere continuous would miss the atom.
:::

## Common misconceptions — A CDF is a probability; a density need not be
A CDF is a probability, so its values lie between zero and one; a density can exceed one because its *integral* over a region is a probability. A CDF includes the mass at its threshold, whereas $F_X(x-)$ excludes it. Not every CDF has a density, and not every continuous CDF is differentiable or absolutely continuous. An ordinary inverse may fail at jumps and flat stretches, which is why the quantile uses an infimum. Finally, a function that has the correct limiting values but is not right-continuous is not a CDF under the $\le$ convention.{{cite:billingsley1995}} (§14, pp. 188–189){{cite:durrett2019}} (§1.2, pp. 10–13)

## Assumptions and limits — One dimension, and independence for a product of CDFs
The four CDF properties apply to any real-valued random variable, without assuming a density or finite moments. The empirical CDF treats the observed sample values as equally weighted; its suitability for inference depends on how the sample was collected. Inverse-transform sampling needs uniform input and the chosen generalized-inverse convention. The maximum's product formula requires independence, even though its underlying event equality does not. The formulas here concern a one-dimensional law; a multivariate CDF needs a joint event and does not follow from the separate marginal CDFs alone.{{cite:billingsley1995}} (§§12, 14, 20){{cite:durrett2019}} (§2.1){{cite:billingsley1995}} (§14, p. 190)

## Connections — Mass functions, densities, quantiles, and the empirical CDF
The [probability mass function](discrete-distribution.qmd) supplies a staircase CDF by summing point masses. A [density](continuous-distribution.qmd) supplies an absolutely continuous CDF by integration. A quantile reverses the threshold question using a generalized inverse, and the [inverse-transform method](inverse-transform-method.qmd) uses that inverse for simulation. The [empirical distribution function](../notes/ur-02-probability-and-simulation.qmd#s-an-empirical-distribution-and-a-kernel-density) replaces a population probability with the observed fraction at or below each threshold. For two variables, a [joint distribution](joint-distribution-and-density.qmd) is needed to calculate probabilities involving both; their marginal CDFs alone are insufficient.{{cite:billingsley1995}} (§§12, 14, 20)

## History — Kolmogorov's strict inequality and the modern $\le$ convention
Kolmogorov's 1933 *Grundbegriffe der Wahrscheinlichkeitsrechnung* defined a distribution function in its chapter on random variables and explained how its values determine probabilities of intervals and, for a Borel probability field, the whole law. His displayed convention was $P(X<x)$, with *strict* inequality; accordingly the function in that treatment is left-continuous and its interval formula uses $[a,b)$. This article uses the modern $P(X\le x)$ convention, so it is right-continuous and uses $(a,b]$. The distinction changes values at atoms but describes the same underlying probability law.{{cite:kolmogorov1933_slln}} (Ch. III, §2){{cite:billingsley1995}} (§14, pp. 188–189)

Billingsley's later treatment states the present right-continuous convention, identifies the jump with its point mass, and proves that any function satisfying monotonicity, right-continuity, and the two endpoint limits is a distribution function. It also constructs the law by applying the generalized inverse to a uniform variable. These results explain why one CDF can specify discrete, continuous, and mixed examples without selecting a density in advance.{{cite:billingsley1995}} (§14, pp. 188–189)
