## Motivating example
A joint table puts mass $0.2$ and $0.3$ on $Y=1$ and $Y=2$ when $X=0$, and mass $0.4$ and $0.1$ when $X=1$. Each row sums to $0.5$. The mean of $Y$ can be computed inside each row and then averaged across the rows.

## Intuition — Average in stages
The conditional expectation $\mathbb E(Y\mid X)$ is a random variable: it is the mean of $Y$ once $X$ is known, and it still varies with $X$. Averaging that random mean, over the distribution of $X$, returns the ordinary mean of $Y$. The same idea nests. If one conditions first on a larger collection of variables and then on a smaller one, the smaller conditioning is what remains.{{cite:durrett2019}} (eq. 4.1.5 and Thm. 4.1.13, p. 211)

## Statement
**The smaller sigma-field wins.** Let $Y$ be integrable. For a sub-sigma-algebra $\mathcal G$,
$$
\mathbb E\bigl(\mathbb E(Y\mid\mathcal G)\bigr)=\mathbb E(Y).
$$
If $\mathcal F_1\subset\mathcal F_2$, then $\mathbb E\bigl(\mathbb E(Y\mid\mathcal F_1)\mid\mathcal F_2\bigr)=\mathbb E(Y\mid\mathcal F_1)$ and $\mathbb E\bigl(\mathbb E(Y\mid\mathcal F_2)\mid\mathcal F_1\bigr)=\mathbb E(Y\mid\mathcal F_1)$. In the second identity the smaller sigma-field is the one that survives. Taking $\mathcal F_1=\sigma(X)$ and $\mathcal F_2=\sigma(X,Z)$ is the nested form $\mathbb E\bigl(\mathbb E(Y\mid X,Z)\mid X\bigr)=\mathbb E(Y\mid X)$.{{cite:durrett2019}} (eq. 4.1.5 and Thm. 4.1.13, p. 211)

## Proof
The defining integral property says that for every event $A\in\mathcal G$,
$$
\int_A \mathbb E(Y\mid\mathcal G)\,d\mathrm P=\int_A Y\,d\mathrm P,
$$
when $Y$ is integrable. The whole sample space belongs to $\mathcal G$, so the integrals of $\mathbb E(Y\mid\mathcal G)$ and of $Y$ agree, which is $\mathbb E\bigl(\mathbb E(Y\mid\mathcal G)\bigr)=\mathbb E(Y)$.{{cite:durrett2019}} (eq. 4.1.5, p. 211)

Now let $\mathcal F_1\subset\mathcal F_2$. The random variable $\mathbb E(Y\mid\mathcal F_1)$ is already $\mathcal F_2$-measurable, because $\mathcal F_1\subset\mathcal F_2$. If a random variable is measurable with respect to $\mathcal F$, its conditional expectation given $\mathcal F$ is the variable itself. That is $\mathbb E\bigl(\mathbb E(Y\mid\mathcal F_1)\mid\mathcal F_2\bigr)=\mathbb E(Y\mid\mathcal F_1)$.{{cite:durrett2019}} (Ex. 4.1.3, p. 207) For the other order, both $\mathbb E\bigl(\mathbb E(Y\mid\mathcal F_2)\mid\mathcal F_1\bigr)$ and $\mathbb E(Y\mid\mathcal F_1)$ are $\mathcal F_1$-measurable. On any $A\in\mathcal F_1\subset\mathcal F_2$ the integral of $\mathbb E(Y\mid\mathcal F_2)$ equals the integral of $Y$, which equals the integral of $\mathbb E(Y\mid\mathcal F_1)$. The two sides have the same integrals over $\mathcal F_1$, so they are equal.{{cite:durrett2019}} (Thm. 4.1.13, p. 211)

## Worked example — A four-cell table
Let the joint probabilities be

| | $Y=1$ | $Y=2$ |
|---|---:|---:|
| $X=0$ | $0.2$ | $0.3$ |
| $X=1$ | $0.4$ | $0.1$ |

Each row sums to $0.5$. Then
$$
\mathbb E(Y\mid X=0)=\frac{0.2\cdot 1+0.3\cdot 2}{0.5}=1.6,
\qquad
\mathbb E(Y\mid X=1)=\frac{0.4\cdot 1+0.1\cdot 2}{0.5}=1.2.
$$
Averaging over $X$ gives $1.6\cdot 0.5+1.2\cdot 0.5=1.4$. Directly, $\mathbb E(Y)=1\cdot(0.2+0.4)+2\cdot(0.3+0.1)=1.4$. The same arithmetic with $Y^2$, whose values are $1$ and $4$, gives $\mathbb E(Y^2\mid X=0)=2.8$, $\mathbb E(Y^2\mid X=1)=1.6$, and both the tower average and the direct mean equal $2.2$.{{cite:durrett2019}} (eq. 4.1.5, p. 211)

**Your turn.** For this table, compute $\mathbb E(Y^2)$ directly from the four cells and confirm it equals $2.2$.

::: {.callout-tip collapse="true" title="Answer"}
$\mathbb E(Y^2)=1\cdot(0.2+0.4)+4\cdot(0.3+0.1)=0.6+1.6=2.2$. The conditional route is $2.8\cdot 0.5+1.6\cdot 0.5=2.2$.
:::

### A function of $X$
Suppose $Y=X$ on this same marginal of $X$, so $\mathbb P(X=0)=\mathbb P(X=1)=0.5$. What is $\mathbb E(Y\mid X=0)$, and what does the tower say about $\mathbb E(Y)$?

::: {.callout-tip collapse="true" title="Answer"}
Given $X=0$, $Y$ is the constant $0$, so the conditional expectation is $0$. Likewise $\mathbb E(Y\mid X=1)=1$. The tower returns $\mathbb E(Y)=0\cdot 0.5+1\cdot 0.5=0.5$, which is also the marginal mean of $X$.
:::

### Independence
Suppose instead that $X$ is still fair and $Y$ is independent of $X$, with $\mathbb P(Y=1)=0.6$ and $\mathbb P(Y=2)=0.4$. Find $\mathbb E(Y\mid X=0)$ and the tower average.

::: {.callout-tip collapse="true" title="Answer"}
Independence makes the conditional mean the unconditional mean: $\mathbb E(Y)=1\cdot 0.6+2\cdot 0.4=1.4$, at both $X=0$ and $X=1$. Averaging a constant $1.4$ still gives $1.4$.
:::

## Related concepts — Means computed in layers
The identity is the first half of the calculation that splits a random sum into a mean number of terms times a mean term. [Conditional expectation](conditional-expectation.qmd) is the inner object; [expectation](expectation.qmd) is what the outer average returns. [Conditional probability](conditional-probability.qmd) is the same layering for events rather than for an integrable random variable.{{cite:durrett2019}} (eq. 4.1.5, p. 211)
