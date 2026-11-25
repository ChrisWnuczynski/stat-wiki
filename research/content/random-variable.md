## Lead context
A random variable is a fixed function of the underlying outcome; its distribution describes the probabilities of its values. A realised value is one number obtained after the experiment. Distinguishing the function, its law, and its observed value makes probability statements and statistical procedures precise.{{cite:kolmogorov1933_slln}} (Ch. III, §2){{cite:billingsley1995}} (§20, pp. 256–257)

## Motivating example — Two tosses, one number of heads
For two coin tosses, the complete outcomes are HH, HT, TH, and TT. The number of heads maps them to $2,1,1,0$, respectively. The event “exactly one head” is therefore the preimage $\{\mathrm{HT},\mathrm{TH}\}$ of the numerical value $1$. This is how a question about numbers becomes an event that can be assigned a probability.{{cite:kolmogorov1933_slln}} (Ch. III, §2){{cite:billingsley1995}} (§§13–14, pp. 182–183, 188–189)

## Intuition — The rule is fixed; the outcome is random
The word “random” describes which outcome is selected, not a rule that changes after the experiment. Before tossing a coin, the number of heads is a random variable; after the tosses, its observed value is an ordinary number. Different rules can be applied to the same outcomes, and their resulting variables can be dependent even when each one's separate distribution is known. Conversely, variables on different experiments can have the same distribution.{{cite:billingsley1995}} (§§13–14, pp. 182–183, 188–189)

## Definition — A measurable map from outcomes to numbers
Let $(\Omega,\mathcal F,\mathbb P)$ be a probability space: $\Omega$ is the set of possible outcomes, $\mathcal F$ the measurable events, and $\mathbb P$ their probability measure. A real-valued **random variable** is a function $X:\Omega\to\mathbb R$ for which

$$
\{\omega\in\Omega:X(\omega)\le x\}\in\mathcal F
\quad\text{for every }x\in\mathbb R.
$$

The condition is *measurability*: every numerical threshold question is an event. Because half-lines of this form generate the Borel sets, the preimage $\{\omega:X(\omega)\in B\}$ is measurable for every Borel set $B\subseteq\mathbb R$. A realised value is written $x=X(\omega)$; the capital $X$ denotes the function before the outcome is observed. On a finite sample space with every subset declared an event, every real-valued function on $\Omega$ is automatically a random variable.{{cite:kolmogorov1933_slln}} (Ch. III, §2){{cite:billingsley1995}} (§§13–14, pp. 182–183, 188–189)

The *law* of $X$ is the probability measure $\mathbb P_X(B)=\mathbb P(X\in B)$ on Borel sets $B$. Its [cumulative distribution function](cumulative-distribution-function.qmd) is $F_X(x)=\mathbb P(X\le x)$. The law tells us everything about one-variable probability questions involving $X$, but it does not record how $X$ is paired with another variable on the same experiment. A discrete law puts probability one on a countable set of values; an absolutely continuous law has a density. Other laws can combine these types or have neither a density nor a point mass description alone.{{cite:billingsley1995}} (§§12–14){{cite:durrett2019}} (§1.2, pp. 10–14)

## Properties — Transformations, expectation, and the CDF
If $g:\mathbb R\to\mathbb R$ is a Borel-measurable function, then $Y=g(X)$ is also a random variable. This includes indicators such as $\mathbf1\{X>c\}$, where $c$ is a fixed threshold, and transformations such as $X^2$. The law of $Y$ follows from preimages: $\mathbb P(Y\in B)=\mathbb P(X\in g^{-1}(B))$. Thus a transformation changes the distribution according to which input values it groups together.{{cite:billingsley1995}} (§§13–14, pp. 182–183, 188–189)

For a measurable $g$ with $\mathbb E|g(X)|<\infty$, the [expectation of a function](expectation-of-a-function.qmd) is $\mathbb E g(X)=\int g(x)\,\mathbb P_X(\mathrm dx)$. When $X$ is discrete with masses $p_i$ at $x_i$, this is $\sum_i g(x_i)p_i$; when it has density $f_X$, it is $\int g(x)f_X(x)\,\mathrm dx$. These are two calculations of the same expectation, determined by the law rather than by the particular sample space used to construct $X$. {{cite:billingsley1995}} (§20){{cite:durrett2019}} (Ch. 1, §1.6)

The CDF $F_X$ is nondecreasing and right-continuous, approaches zero and one at the two ends of the line, and gives $\mathbb P(a<X\le b)=F_X(b)-F_X(a)$ for $a<b$. Every function satisfying these properties is the CDF of a law on the real line; the [CDF article](cumulative-distribution-function.qmd) spells out the endpoint convention and its converse construction. The distinction between a point mass and a density is visible in the CDF's jumps and continuous rises.{{cite:billingsley1995}} (§14, pp. 188–189)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For any Borel set $B$, the event $\{g(X)\in B\}$ equals $\{X\in g^{-1}(B)\}$. Measurability of $g$ makes $g^{-1}(B)$ Borel, and measurability of $X$ makes the latter set an event. This proves that $g(X)$ is a random variable and gives its transformation law. In particular, the inverse image of $\{1\}$ under $\mathbf1\{X>c\}$ is $\{X>c\}$.{{cite:billingsley1995}} (§§13–14, pp. 182–183, 188–189)

For an indicator $g=\mathbf1_B$, $\mathbb E g(X)=\mathbb P(X\in B)=\int g(x)\,\mathbb P_X(\mathrm dx)$ by definition of the law. Linearity proves the identity for nonnegative simple functions. Approximate any nonnegative measurable $g$ from below by simple functions and use monotone convergence; split an integrable signed $g$ into positive and negative parts. If the law places masses $p_i$ at $x_i$, the integral becomes $\sum_i g(x_i)p_i$; if it has density $f_X$, the definition of a density makes it $\int g(x)f_X(x)\,\mathrm dx$. Absolute integrability ensures neither side is an undefined difference of infinities.{{cite:durrett2019}} (Ch. 1, §1.6)

The events $\{X\le a\}\subseteq\{X\le b\}$ for $a<b$ give CDF monotonicity, and the disjoint union $\{X\le b\}=\{X\le a\}\sqcup\{a<X\le b\}$ gives the interval formula. Continuity of probability from above as thresholds decrease to $x$ gives right-continuity; thresholds tending to $\pm\infty$ give the limits. Conversely, for such an $F$, put $Q(u)=\inf\{x:F(x)\ge u\}$ and take $U$ uniform on $(0,1)$. Monotonicity and right-continuity give $\{Q(U)\le x\}=\{U\le F(x)\}$, so $Q(U)$ has CDF $F$. This establishes the converse construction.{{cite:billingsley1995}} (§14, pp. 188–189)
:::
:::

## Statistical use — A sample, a statistic, and an indicator
In a sample, write $X_1,\ldots,X_n$ for the random measurements before observing them and $x_1,\ldots,x_n$ for their realised values. A [statistic](statistic.qmd), such as $\bar X=n^{-1}\sum_i X_i$, is itself a random variable because it is a measurable function of the sample. Its *sampling distribution* describes how it would vary if the experiment were repeated under the model. After data are observed, $\bar x$ is one realised number, not a distribution.{{cite:billingsley1995}} (§20){{cite:nist_glossary2002}} (entries “statistic” and “sampling distribution”)

An indicator $\mathbf1_A$ of an event $A$ is a random variable taking values zero and one; its expectation equals $\mathbb P(A)$. This lets a binary outcome be analysed using the same machinery as counts or continuous measurements. For independent replicate trials, a sum of indicators counts occurrences of $A$. Its sample proportion has expectation $\mathbb P(A)$ and can be compared with a proposed event probability.{{cite:durrett2019}} (Ch. 1, §1.6)

## Worked example — The sum of two dice, and an indicator of a large sum
Roll two fair dice independently and let $X$ be their sum. The outcome is an ordered pair $(i,j)\in\{1,\ldots,6\}^2$, and $X(i,j)=i+j$. There are $36$ equally likely pairs. Six have sum $7$, so $\mathbb P(X=7)=6/36=1/6$; the sums $2,3,4$ have $1,2,3$ pairs, so $F_X(4)=\mathbb P(X\le4)=6/36=1/6$. By symmetry or by adding the two die expectations, $\mathbb E X=7$. If $Y=\mathbf1\{X\ge10\}$, then sums $10,11,12$ have $3,2,1$ pairs, and $\mathbb P(Y=1)=6/36=1/6$. The same experiment supports both the count $X$ and the binary variable $Y$.{{cite:durrett2019}} (Ch. 1, §§1.1, 1.6)

**Your turn.** What is $\mathbb P(X\ge11)$ in this experiment, and which ordered dice outcomes make the event true?

::: {.callout-tip collapse="true" title="Answer"}
The event consists of $(5,6)$, $(6,5)$, and $(6,6)$. It has three of the 36 equally likely ordered outcomes, so $\mathbb P(X\ge11)=3/36=1/12$.
:::

## Common misconceptions — A variable, a law, and a realised value are not the same
A random variable is a function on outcomes; its distribution is the probability law of its values, and an observed value is one number. Two variables can have the same marginal law yet be dependent or independent under different joint constructions. A continuous CDF need not have a density; the density formula describes an absolutely continuous law. A density's value is not the probability of an exact point. Measurability matters on infinite spaces: a numerical rule is a random variable only when its relevant inverse images are events.{{cite:billingsley1995}} (§§12–14){{cite:durrett2019}} (§1.2, pp. 10–14)

## Assumptions and limits — The sample space, integrability, and the dice model
The definition uses a chosen sample space, sigma-algebra, and probability measure. It applies to dependent variables, discrete or mixed laws, and variables without a finite expectation. The expectation formula with signed $g$ requires $\mathbb E|g(X)|<\infty$. A real-valued variable is one-dimensional; a [random vector](mean-vector-and-covariance-matrix.qmd) has several coordinates and a joint law that cannot generally be recovered from the coordinate marginals alone. The dice calculation uses the extra model assumptions that the dice are fair and independent.{{cite:billingsley1995}} (§§14, 20)

## Connections — Events, laws, statistics, and joint distributions
An [event](event.qmd) is a measurable set of outcomes, while a random variable maps outcomes to numerical values; $\{X\le x\}$ connects them. A [CDF](cumulative-distribution-function.qmd) and the law describe one-variable probabilities without specifying the underlying sample space. A [statistic](statistic.qmd) is a random variable computed from a sample, and an [estimator](estimator.qmd) is a statistic used for an unknown parameter. A [joint distribution](joint-distribution-and-density.qmd) records how multiple variables are paired, including their dependence; two separate CDFs do not.{{cite:billingsley1995}} (§20){{cite:nist_glossary2002}} (entries “statistic” and “sampling distribution”)

## History — Kolmogorov's 1933 threshold definition
In *Grundbegriffe der Wahrscheinlichkeitsrechnung* (1933), Andrey Kolmogorov defined a real random variable as a numerical function on elementary outcomes whose threshold preimages belong to the event collection. His threshold convention used $X<a$, which leads to a left-continuous distribution function. The measure-based formulation covers both discrete and non-discrete variables.{{cite:kolmogorov1933_slln}} (Ch. III, §2)

Modern measure-theoretic treatments express the condition through inverse images of Borel sets and use $X\le x$ for a right-continuous CDF. Billingsley shows that the two ways of testing measurability are equivalent because threshold half-lines generate the Borel sigma-algebra. He also defines a variable's law as the probability it induces on the real line, clarifying why distinct outcome spaces can produce the same distribution. The difference between strict and non-strict thresholds changes endpoint notation, not which functions count as measurable random variables.{{cite:billingsley1995}} (§§13–14, pp. 182–183, 188–189)
