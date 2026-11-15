## Lead context
Two variables can share information only because both respond to a third. Once that third variable is known, neither of the first two carries extra information about the other. The same pair can still be dependent when the third variable is hidden.{{cite:dawid1979}}

## Motivating example
A fair coin selects one of two experiments. In the first, two answers are independent draws with success probability \(1/4\). In the second, the success probability is \(3/4\), and the draws are again independent. Knowing which experiment was used makes one answer irrelevant to the other. Not knowing the experiment makes the answers move together, because a pair of successes is more plausible when the high-probability experiment was selected. The arithmetic is in the worked example.{{cite:dawid1979}}

## Intuition
Conditional independence is independence inside each slice of the conditioning variable. The slice can change with the conditioning value. What must not change, inside a slice, is the relevance of one variable to the other. Marginal correlation looks at the slices piled on top of one another, so a shared slice label can create dependence that disappears as soon as the label is known. The opposite can also happen: variables that are independent overall can be dependent inside a slice. The two statements answer different questions.{{cite:dawid1979}}

## Definition
Let \(X\), \(Y\) and \(Z\) be random variables. Write \(X\perp Y\mid Z\) when, for every value \(z\) with positive probability in the discrete case, the conditional distribution of \((X,Y)\) given \(Z=z\) is a product distribution. Equivalently, for positive conditional probabilities,
\[
\mathbb P(X=x\mid Y=y,Z=z)=\mathbb P(X=x\mid Z=z).
\]
Knowing \(Y\) does not change the conditional distribution of \(X\) once \(Z\) is known. The existing page records the same idea for a general conditional probability: the conditional probability of a set of \(X\)-values, given \(Y\) and \(Z\), has a version that depends on \(Z\) alone. For a joint density the product form \(f(x,y,z)=f(x\mid z)\,f(y,z)\) is the same statement where the marginal density of \(Z\) is positive.{{cite:dawid1979,lauritzen1996}}

## Interpretation
The symbol \(X\perp Y\mid Z\) is a statement about conditional distributions, not about a single correlation. A correlation of zero is neither necessary nor sufficient for conditional independence, and conditional independence does not imply marginal independence. In the coin example the conditional correlation is zero in each experiment, while the marginal probability of two successes is \(5/16\) rather than the product \(1/4\).{{cite:dawid1979}}

The factorisation \(f(x,y,z)=g(x,z)\,h(y,z)\) says that every term which involves both \(X\) and \(Y\) also involves \(Z\). That is the form used to read conditional independence from a joint density, and it is the form a graph encodes when a separating set blocks the paths between two groups of variables.{{cite:lauritzen1996,dawid1979}}

## Properties
Conditional independence is symmetric: \(X\perp Y\mid Z\) if and only if \(Y\perp X\mid Z\), when a joint distribution exists. If \(U=h(X)\) and \(X\perp Y\mid Z\), then \(U\perp Y\mid Z\), and also \(X\perp Y\mid (Z,U)\). If in addition \(X\perp W\mid (Y,Z)\), then \(X\perp (W,Y)\mid Z\). These are the symmetry, reduction, and contraction properties. They are the discrete content of the four bullets already listed on this page.{{cite:dawid1979}}

A further equivalent form is \((X,Z)\perp (Y,Z)\mid Z\). Adding \(Z\) to both sides does not create new information, because \(Z\) is already known.{{cite:dawid1979}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Assume discrete variables and conditioning values with positive probability. If \(\mathbb P(X=x,Y=y\mid Z=z)=\mathbb P(X=x\mid Z=z)\mathbb P(Y=y\mid Z=z)\), the right-hand side is symmetric in \(X\) and \(Y\), so \(Y\perp X\mid Z\). Dividing by \(\mathbb P(Y=y\mid Z=z)\) gives \(\mathbb P(X=x\mid Y=y,Z=z)=\mathbb P(X=x\mid Z=z)\). The same division with the roles reversed gives the other conditional probability.{{cite:dawid1979}}

Let \(U=h(X)\). Summing the product formula over the \(x\) with \(h(x)=u\) yields
\[
\mathbb P(U=u,Y=y\mid Z=z)=\mathbb P(U=u\mid Z=z)\mathbb P(Y=y\mid Z=z),
\]
which is \(U\perp Y\mid Z\). For the refined conditioning, the event \(\{U=u\}\) restricts \(X\) to \(h^{-1}(u)\). On that event,
\[
\mathbb P(Y=y\mid X=x,Z=z,U=u)=\mathbb P(Y=y\mid X=x,Z=z)=\mathbb P(Y=y\mid Z=z),
\]
using \(X\perp Y\mid Z\). The right-hand side does not depend on \(x\) or \(u\), so \(Y\)'s conditional distribution given \((Z,U)\) is a function of \(Z\) alone.{{cite:dawid1979}}

If also \(X\perp W\mid (Y,Z)\), then
\[
\mathbb P(X=x\mid W=w,Y=y,Z=z)=\mathbb P(X=x\mid Y=y,Z=z)=\mathbb P(X=x\mid Z=z).
\]
The conditional distribution of \(X\) given \((W,Y,Z)\) depends only on \(Z\), which is \(X\perp (W,Y)\mid Z\).{{cite:dawid1979}}

For the density identities already displayed, \(f(x\mid y,z)=f(x,y,z)/f(y,z)\) where \(f(y,z)>0\). Substituting \(f(x,y,z)=f(x\mid z)f(y,z)\) cancels \(f(y,z)\) and leaves \(f(x\mid z)\). Multiplying the resulting equality by \(f(z\mid y)\) gives \(f(x,z\mid y)=f(x\mid z)f(z\mid y)\).{{cite:lauritzen1996}}
:::
:::

## Statistical use
A sufficient statistic is a conditional-independence statement: given the statistic, the data carry no further information about the parameter. An ancillary statistic is the companion statement that its sampling distribution does not depend on the parameter. Both readings need a joint distribution only when one wants to reverse the conditioning; a sampling model by itself supports the direction in which the data are random and the parameter is fixed.{{cite:dawid1979}}

In a graphical model, conditional independence is what a separating set claims. If \(C\) separates \(A\) from \(B\) and the distribution has the global Markov property, then \(X_A\perp X_B\mid X_C\). That is the separation sentence already on this page. A zero in a precision matrix is a further, Gaussian, reading of the same relation and is left to the page devoted to that reading.{{cite:lauritzen1996}}

## Worked example
Let \(Z\) be \(0\) or \(1\) with probability \(1/2\) each. Given \(Z=0\), let \(X\) and \(Y\) be independent with success probability \(1/4\). Given \(Z=1\), let them be independent with success probability \(3/4\). Then
\[
\mathbb P(X=1\mid Y=1,Z=0)=\frac14=\mathbb P(X=1\mid Z=0),
\]
and the same equality holds at \(Z=1\) with probability \(3/4\). So \(X\perp Y\mid Z\).

The marginal probability of two successes is
\[
\mathbb P(X=1,Y=1)=\tfrac12\cdot\tfrac14\cdot\tfrac14+\tfrac12\cdot\tfrac34\cdot\tfrac34=\tfrac{5}{16}.
\]
Also \(\mathbb P(X=1)=\mathbb P(Y=1)=1/2\), so the product is \(1/4\), not \(5/16\). The pair is conditionally independent and marginally dependent. The difference is \(1/16\).{{cite:dawid1979}}

**Your turn.** For the same distribution, find \(\mathbb P(X=1\mid Y=1)\).

::: {.callout-tip collapse="true" title="Answer"}
\(\mathbb P(Y=1)=1/2\) and \(\mathbb P(X=1,Y=1)=5/16\), so \(\mathbb P(X=1\mid Y=1)=(5/16)/(1/2)=5/8\). This is not \(\mathbb P(X=1)=1/2\). Knowing \(Y\) still helps until \(Z\) is known.
:::

## Common misconceptions
Conditional independence is not marginal independence, and it is not a correlation of zero. Symmetry needs a joint distribution: a sampling statement such as “the conditional distribution of the data given a parameter does not depend on a second parameter” need not reverse if that parameter has no probability distribution. A function of \(X\) cannot restore a dependence that \(X\) itself does not have, given \(Z\). Finally, knowing \(Z\) and also a function of \(X\) does not let \(Y\) re-enter the conditional distribution of \(X\); the contraction and reduction properties say the opposite.{{cite:dawid1979}}

## Assumptions and limits
The probability calculations assume a joint distribution and conditioning events of positive probability. Density formulas are versions, valid where the relevant marginal densities are positive. Improper distributions can separate two formally equivalent conditional-independence statements; the opened paper records that marginalisation paradox and then restricts attention to proper distributions. The graph separation claim needs the global Markov property for that distribution.{{cite:dawid1979,lauritzen1996}}

## Connections
[Independent random variables](independent-random-variables.qmd) are the case with no conditioning variable. A [conditional distribution](conditional-distribution.qmd) is the object that factors. [Conditional probability](conditional-probability.qmd) is the discrete quotient used in the definition. A [separating set](separating-set.qmd) is the graph form of the same claim, and a [zero precision entry](a-zero-precision-entry-is-conditional-independence.qmd) is the Gaussian form. The [precision matrix](precision-matrix.qmd) holds those entries.{{cite:dawid1979,lauritzen1996}}

## Check yourself
[Conditional versus marginal dependence](../questions/c-36.qmd) asks for the distinction in the worked example. [Conditional independence from a partitioned covariance](../questions/ex-sl-19-4.qmd) asks for the Gaussian version. [Precision to graph](../questions/ex-sl-19-2.qmd) reads zeros as separations.

## History
Dawid's 1979 paper treats conditional independence as a relation \(X\perp Y\mid Z\) with several equivalent expressions. One of them says that the conditional distribution of \(X\) given \(Y\) and \(Z\) is determined by \(Z\) alone. Symmetry is then a theorem, not a part of that one-sided reading, and it uses a joint distribution. The same paper records the reduction property for a function of \(X\) and the contraction property that combines two conditional independences into one. Those lemmas are the four bullets already stated on this page. The paper also warns that improper distributions can make two of the formal expressions come apart.{{cite:dawid1979}}

The factorisation through a separating set is the graphical reading. Lauritzen's development, already cited for the density identities and the global Markov property, uses the product \(g(x,z)h(y,z)\) as the density form that extends from three variables to a graph. The numerical example on this page is the three-variable case of that product: the conditional success probability depends on the experiment and not on the other answer, while the marginal joint probability does not factor.{{cite:lauritzen1996,dawid1979}}
