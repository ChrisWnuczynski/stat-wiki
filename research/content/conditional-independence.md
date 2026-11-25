## Lead context
Two variables can share information only because both respond to a third. Once that third variable is known, neither of the first two carries extra information about the other. The same pair can still be dependent when the third variable is hidden.{{cite:dawid1979}} (§§3–4)

## Motivating example
A fair coin selects one of two experiments. In the first, two answers are independent draws with success probability $1/4$. In the second, the success probability is $3/4$, and the draws are again independent. Knowing which experiment was used makes one answer irrelevant to the other. Not knowing the experiment makes the answers move together, because a pair of successes is more plausible when the high-probability experiment was selected. The arithmetic is in the worked example.{{cite:dawid1979}} (§§3–4)

## Intuition
Conditional independence is independence inside each slice of the conditioning variable. The slice can change with the conditioning value. What must not change, inside a slice, is the relevance of one variable to the other. Marginal correlation looks at the slices piled on top of one another, so a shared slice label can create dependence that disappears as soon as the label is known. The opposite can also happen: variables that are independent overall can be dependent inside a slice. The two statements answer different questions.{{cite:dawid1979}} (§§3–4)

## Definition
Let $X$, $Y$ and $Z$ be random variables. Write $X\perp Y\mid Z$ when, for every value $z$ with positive probability in the discrete case, the conditional distribution of $(X,Y)$ given $Z=z$ is a product distribution. Equivalently, for every $x$ and every pair $(y,z)$ with $\mathbb P(Y=y,Z=z)>0$,

$$
\mathbb P(X=x\mid Y=y,Z=z)=\mathbb P(X=x\mid Z=z).
$$


Knowing $Y$ does not change the conditional distribution of $X$ once $Z$ is known. For general conditional probabilities, the probability of a set of $X$-values given $Y$ and $Z$ has a version that depends on $Z$ alone. For a joint density the product form $f(x,y,z)=f(x\mid z)\,f(y,z)$ expresses the same condition where the relevant marginal densities are positive.{{cite:dawid1979}} (§§3–4)

## Interpretation
The symbol $X\perp Y\mid Z$ is a statement about conditional distributions, not about a single correlation. Zero *marginal* correlation is neither necessary nor sufficient for conditional independence, and conditional independence does not imply marginal independence. When conditional second moments exist, conditional independence does give zero conditional covariance. In the coin example the conditional correlation is zero in each experiment, while the marginal probability of two successes is $5/16$ rather than the product $1/4$.{{cite:dawid1979}} (§§3–4)

The factorisation $f(x,y,z)=g(x,z)\,h(y,z)$, with nonnegative factors that define a proper joint density, separates the $x$-dependent and $y$-dependent parts once $z$ is fixed. Normalising each slice shows why neither variable then adds information about the other.{{cite:dawid1979}} (§§3–4)

## Properties
Conditional independence is symmetric: $X\perp Y\mid Z$ if and only if $Y\perp X\mid Z$, when a joint distribution exists. If $U=h(X)$ and $X\perp Y\mid Z$, then $U\perp Y\mid Z$, and also $X\perp Y\mid (Z,U)$. If in addition $X\perp W\mid (Y,Z)$, then $X\perp (W,Y)\mid Z$. These are the symmetry, reduction, and contraction properties.{{cite:dawid1979}} (§§3–4)

A further equivalent form is $(X,Z)\perp (Y,Z)\mid Z$. Adding $Z$ to both sides does not create new information, because $Z$ is already known.{{cite:dawid1979}} (§§3–4)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Assume discrete variables and conditioning values with positive probability. If $\mathbb P(X=x,Y=y\mid Z=z)=\mathbb P(X=x\mid Z=z)\mathbb P(Y=y\mid Z=z)$, the right-hand side is symmetric in $X$ and $Y$, so $Y\perp X\mid Z$. Dividing by $\mathbb P(Y=y\mid Z=z)$ gives $\mathbb P(X=x\mid Y=y,Z=z)=\mathbb P(X=x\mid Z=z)$. The same division with the roles reversed gives the other conditional probability.{{cite:dawid1979}} (§§3–4)

If also $X\perp W\mid (Y,Z)$, then

$$
\mathbb P(X=x\mid W=w,Y=y,Z=z)=\mathbb P(X=x\mid Y=y,Z=z)=\mathbb P(X=x\mid Z=z).
$$


The conditional distribution of $X$ given $(W,Y,Z)$ depends only on $Z$, which is $X\perp (W,Y)\mid Z$.{{cite:dawid1979}} (§§3–4)

When second moments exist, the conditional product law gives $\mathbb E(XY\mid Z)=\mathbb E(X\mid Z)\mathbb E(Y\mid Z)$, so the conditional covariance is zero. This says nothing about the marginal covariance, because averaging over $Z$ can make both conditional means move together. Conversely, take independent fair Bernoulli variables $X$ and $Y$, and let $Z=\mathbf1_{\{X=Y\}}$. Their marginal covariance is zero. Given $Z=1$, however, $\mathbb P(X=1,Y=1\mid Z=1)=1/2$, while $\mathbb P(X=1\mid Z=1)\mathbb P(Y=1\mid Z=1)=1/4$. Thus zero marginal correlation does not imply conditional independence.{{cite:dawid1979}} (§3)

For a joint density, $f(x\mid y,z)=f(x,y,z)/f(y,z)$ where $f(y,z)>0$. Substituting $f(x,y,z)=f(x\mid z)f(y,z)$ cancels $f(y,z)$ and leaves $f(x\mid z)$. Multiplying the resulting equality by $f(z\mid y)$ gives $f(x,z\mid y)=f(x\mid z)f(z\mid y)$.{{cite:dawid1979}} (§§3–4)

Let $U=h(X)$. Summing the product formula over the $x$ with $h(x)=u$ yields

$$
\mathbb P(U=u,Y=y\mid Z=z)=\mathbb P(U=u\mid Z=z)\mathbb P(Y=y\mid Z=z),
$$


which is $U\perp Y\mid Z$. For the refined conditioning, the event $\{U=u\}$ restricts $X$ to $h^{-1}(u)$. On that event,

$$
\mathbb P(Y=y\mid X=x,Z=z,U=u)=\mathbb P(Y=y\mid X=x,Z=z)=\mathbb P(Y=y\mid Z=z),
$$


using $X\perp Y\mid Z$. Summing over $x$ conditional on $(Z,U)$ also gives $P(Y\mid Z,U)=P(Y\mid Z)$.{{cite:dawid1979}} (§§3–4) Therefore the two conditional laws agree, so $P(Y\mid X,Z,U)=P(Y\mid Z,U)$, i.e. $X\perp Y\mid(Z,U)$.
:::
:::

## Statistical use
A statistic $T(X)$ is sufficient for a parameter when the conditional distribution of the data $X$ given $T(X)$ does not depend on that parameter. The parameter is fixed in this sampling-model statement. An ancillary statistic instead has a marginal distribution that does not depend on the parameter. These are different ways in which a statistic can remove dependence on an unknown value.{{cite:dawid1979}} (§§3–4)


## Worked example
Let $Z$ be $0$ or $1$ with probability $1/2$ each. Given $Z=0$, let $X$ and $Y$ be independent with success probability $1/4$. Given $Z=1$, let them be independent with success probability $3/4$. Then

$$
\mathbb P(X=1\mid Y=1,Z=0)=\frac14=\mathbb P(X=1\mid Z=0),
$$


and the same equality holds at $Z=1$ with probability $3/4$. So $X\perp Y\mid Z$.

The marginal probability of two successes is

$$
\mathbb P(X=1,Y=1)=\tfrac12\cdot\tfrac14\cdot\tfrac14+\tfrac12\cdot\tfrac34\cdot\tfrac34=\tfrac{5}{16}.
$$


Also $\mathbb P(X=1)=\mathbb P(Y=1)=1/2$, so the product is $1/4$, not $5/16$. The pair is conditionally independent and marginally dependent. The difference is $1/16$.{{cite:dawid1979}} (§§3–4)

**Your turn.** For the same distribution, find $\mathbb P(X=1\mid Y=1)$.

::: {.callout-tip collapse="true" title="Answer"}
$\mathbb P(Y=1)=1/2$ and $\mathbb P(X=1,Y=1)=5/16$, so $\mathbb P(X=1\mid Y=1)=(5/16)/(1/2)=5/8$. This is not $\mathbb P(X=1)=1/2$. Knowing $Y$ still helps until $Z$ is known.
:::

## Common misconceptions
Conditional independence is not marginal independence, and it is not a correlation of zero. Symmetry needs a joint distribution: a sampling statement such as “the conditional distribution of the data given a parameter does not depend on a second parameter” need not reverse if that parameter has no probability distribution. A function of $X$ cannot restore a dependence that $X$ itself does not have, given $Z$. Finally, knowing $Z$ and also a function of $X$ does not let $Y$ re-enter the conditional distribution of $X$; the contraction and reduction properties say the opposite.{{cite:dawid1979}} (§§3–4)

## Assumptions and limits
The probability calculations assume a joint distribution and conditioning events of positive probability. Density formulas are versions, valid where the relevant marginal densities are positive. Dawid's analysis of a marginalisation paradox shows why improper distributions can break equivalences that hold for proper joint laws.{{cite:dawid1979}} (§§3–4)

## Connections
[Independent random variables](independent-random-variables.qmd) are the case with no conditioning variable. A [conditional distribution](conditional-distribution.qmd) is the law that factors given $Z$. [Conditional probability](conditional-probability.qmd) supplies the positive-mass quotient in the discrete definition.{{cite:dawid1979}} (§§3–4)

## History
Dawid's 1979 paper treats conditional independence as a relation $X\perp Y\mid Z$ with several equivalent expressions. One says that the conditional distribution of $X$ given $Y$ and $Z$ is determined by $Z$ alone. Symmetry then follows as a theorem for a proper joint law. His reduction and contraction results describe how the relation behaves when variables are combined or replaced by functions.{{cite:dawid1979}} (§§3–4)

The paper also uses conditional independence to describe sufficiency. Given a sufficient statistic, the conditional law of the data does not depend on the parameter. This connects the probability relation to a concrete question in inference: whether a statistic contains all the information about the unknown parameter that the sampling model supplies.{{cite:dawid1979}} (§§3–4)
