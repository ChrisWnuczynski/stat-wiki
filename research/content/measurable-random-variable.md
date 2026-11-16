## Motivating example
Suppose a random experiment produces an outcome $\omega$ in $(0,1)$, with ordinary interval events available for probability statements. Reading off $X(\omega)=\omega$ lets us ask whether the measurement is at most $0.4$: the corresponding outcomes form the event $(0,0.4]$. A numerical function is usable as a random variable precisely when every such question about its value pulls back to an event in the probability space. Without that condition, even a familiar-looking expression such as $P(X\leq0.4)$ need not be defined.{{cite:durrett2019}} (Ch. 1, §§1.2–1.3, pp. 10, 15–16)

## Intuition — Why inverse images matter
A probability measure assigns probabilities to sets of outcomes, not directly to numbers produced from those outcomes. The measurement $X$ bridges the two: a set of numerical values $B$ describes an outcome event $X^{-1}(B)=\{\omega:X(\omega)\in B\}$. Measurability asks that this event belong to the sample-space sigma-algebra whenever $B$ is a Borel set on the real line. The condition depends on the available events. A function can be measurable when every subset of a finite sample space is admitted, yet fail to be measurable on the same outcomes if the sigma-algebra records only coarse groups.{{cite:durrett2019}} (Ch. 1, §§1.2–1.3, pp. 10, 15–16)

## Definition
On a probability space $(\Omega,\mathcal F,P)$, a real-valued **measurable random variable** is a map $X:\Omega\to\mathbb R$ such that $X^{-1}(B)\in\mathcal F$ for every Borel set $B\subseteq\mathbb R$. Equivalently, it is enough to verify the threshold events $\{X\leq x\}\in\mathcal F$ for every real $x$, because these half-lines generate the Borel sigma-algebra. The resulting law is $P_X(B)=P\{X\in B\}$, and its cumulative distribution function is $F_X(x)=P(X\leq x)$. A random variable therefore gives a probability measure on the line even when the original outcomes are not numbers.{{cite:durrett2019}} (Ch. 1, §§1.2–1.3, pp. 10–11, 15–16)

The smallest sigma-algebra on $\Omega$ that makes $X$ measurable is $\sigma(X)=\{X^{-1}(B):B\text{ Borel}\}$. It contains exactly the events determined by observing $X$ alone. A statistic can be a random variable on the sample space because its threshold events are measurable; this is why its sampling distribution can be discussed.{{cite:durrett2019}} (Ch. 1, §1.3, pp. 15–16)

## Properties
An indicator $1_A$ is a random variable exactly when $A\in\mathcal F$: its event $\{1_A=1\}$ is $A$. If $X$ is measurable and $g:\mathbb R\to\mathbb R$ is Borel measurable, then $g(X)$ is measurable. In particular, continuous transformations, sums and products of real random variables remain random variables. A pointwise limit of measurable real-valued random variables is also measurable wherever it is defined as a finite value. These closure facts let complex statistical quantities be built from simpler observations without rechecking every possible value set.{{cite:durrett2019}} (Ch. 1, §1.3, pp. 15–17)

The distribution function $F_X$ is nondecreasing, right-continuous, tends to $0$ and $1$ at the two ends of the line, and has jump $P(X=x)$ at $x$. Right-continuity follows from using $\leq$ in its definition: when thresholds decrease to $x$, their events decrease to $\{X\leq x\}$. These properties are consequences of the probability law induced by $X$, rather than extra assumptions on the formula for $X$.{{cite:durrett2019}} (Ch. 1, §1.2, pp. 10–11)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $\mathcal C=\{B\subseteq\mathbb R:X^{-1}(B)\in\mathcal F\}$. Inverse images preserve complements and countable unions, so $\mathcal C$ is a sigma-algebra. If every $(-\infty,x]$ belongs to $\mathcal C$, then $\mathcal C$ contains the Borel sigma-algebra they generate. This proves the threshold criterion. For measurable $g$, $(g\circ X)^{-1}(B)=X^{-1}(g^{-1}(B))\in\mathcal F$, proving composition. Joint measurability of $(X,Y)$ follows because inverse images of Borel rectangles are intersections $\{X\in A\}\cap\{Y\in B\}$; applying composition to continuous addition and multiplication proves the sum and product claims. Countable infima and suprema are measurable by expressing their threshold events as countable unions or intersections; a finite pointwise limit equals the liminf and is therefore measurable.{{cite:durrett2019}} (Ch. 1, §1.3, pp. 15–17)

For the CDF, $x\leq y$ gives $\{X\leq x\}\subseteq\{X\leq y\}$, so $F_X$ is nondecreasing. If $x_n\downarrow x$, continuity of probability from above gives $F_X(x_n)\downarrow F_X(x)$. Thresholds tending to either end give the limiting values. Finally, $P(X=x)=P(X\leq x)-P(X<x)=F_X(x)-F_X(x-)$.{{cite:durrett2019}} (Ch. 1, §1.2, pp. 10–11)
:::
:::

## Statistical use
In data analysis, a measurement, a sample mean and a test statistic all need to be measurable before probabilities of their values have a formal meaning. Usually this is automatic because they are built from coordinate observations by continuous or simple piecewise operations. The distinction becomes visible when the event collection is coarse: a device that records only whether an outcome lies in a broad group cannot support a probability for a finer, unrecorded outcome distinction. The sigma-algebra $\sigma(X)$ also formalizes what observing $X$ reveals: two outcome events that $X$ cannot distinguish are not separately in its generated information.{{cite:durrett2019}} (Ch. 1, §§1.2–1.3, pp. 10, 15–17)

## Worked example
Let $\Omega=(0,1)$, let $\mathcal F$ be its Borel sets, and let $P$ be uniform length on these sets. With $X(\omega)=\omega$, the threshold event is $\{X\leq x\}=(0,x]$ for $0<x<1$, which is Borel. Thus $X$ is measurable. Its distribution function is $F_X(x)=0$ for $x\leq0$, $F_X(x)=x$ for $0<x<1$, and $F_X(x)=1$ for $x\geq1$. For example, $P(0.2<X\leq0.7)=0.7-0.2=0.5$. The subtraction works because the numerical interval pulls back to the outcome event $(0.2,0.7]$.{{cite:durrett2019}} (Ch. 1, §§1.2–1.3, pp. 10–11, 15–16)

**Your turn.** On that space set $Y(\omega)=1$ if $\omega>1/2$ and $Y(\omega)=0$ otherwise. Show that $Y$ is measurable, find $F_Y(0)$ and $F_Y(1)$, and compute $P(Y=1)$.

::: {.callout-tip collapse="true" title="Answer"}
The event $A=(1/2,1)$ is Borel, and $Y=1_A$ is measurable. Exactly half the uniform interval lies in $A$, so $P(Y=1)=1/2$. The event $\{Y\leq0\}$ is $(0,1/2]$, giving $F_Y(0)=1/2$; $\{Y\leq1\}=\Omega$, giving $F_Y(1)=1$. Its CDF is right-continuous at both jumps.{{cite:durrett2019}} (Ch. 1, §§1.2–1.3, pp. 10–11, 15)
:::

## Common misconceptions
Measurable does not mean continuous: the indicator in the exercise jumps at $1/2$ but is measurable. It does not mean every subset of $\Omega$ is an event; only the relevant inverse images must belong to $\mathcal F$. Nor is a distribution function an arbitrary nondecreasing graph: because it uses $P(X\leq x)$, it must also be right-continuous and have the correct end limits. Finally, two random variables can have the same distribution yet be defined on different outcome spaces; measurability describes the map relative to its own space, while the law describes its probabilities on the real line.{{cite:durrett2019}} (Ch. 1, §§1.2–1.3, pp. 10–11, 15–17)

## Assumptions and limits
On $\Omega=\{a,b,c,d\}$ with $\mathcal F=\{\varnothing,\{a,b\},\{c,d\},\Omega\}$, let $Z(a)=0$ and $Z(b)=Z(c)=Z(d)=1$. Then $\{Z\leq0\}=\{a\}\notin\mathcal F$, so $Z$ is not a random variable on this coarse space. On $(0,1)$ with Lebesgue probability, an indicator of a Vitali selector is a more subtle counterexample: the selected set is not Lebesgue measurable, so its probability cannot be assigned by the usual translation-invariant, countably additive measure. These examples expose a missing event, not a failure of ordinary algebra. The latter construction depends on the axiom of choice and is not encountered in routine measured data.{{cite:durrett2019}} (Ch. 1, §1.2, pp. 10–11; Appendix A.2, pp. 462–463)

## Connections
The [probability space](probability-space.qmd) supplies the events to which probabilities apply, and the [Borel sigma-algebra](generated-and-borel-sigma-algebras.qmd) supplies the value sets whose inverse images are checked. The [random-variable](random-variable.qmd) and [CDF](cumulative-distribution-function.qmd) articles develop the induced law. The answered [CDF right-continuity question](../questions/ex-sp-right-continuous.qmd) checks why the $\leq$ convention matters. Expectation is then an integral of a measurable function, built first from [simple variables](simple-variables-and-expectation.qmd).{{cite:durrett2019}} (Ch. 1, §§1.2–1.4, pp. 10–18)

## History
Kolmogorov's 1933 *Grundbegriffe der Wahrscheinlichkeitsrechnung* placed random quantities within an axiomatic probability framework; its third chapter treats random variables, followed by a chapter on expectation.{{cite:shafer_vovk2018_grundbegriffe}} (§5.1, p. 40) Modern presentations, such as Durrett's, emphasize the inverse-image condition and the probability law induced by a measurable map. The language explains why countable operations on events are built into probability theory: they support distributions and limits of random variables.{{cite:durrett2019}} (Ch. 1, §§1.2–1.3, pp. 10–17)
