## Lead context
A structure function says which patterns of working components make the whole system work.

## Motivating example
Five bulbs in a single string go dark when any one bulb fails. Five bulbs in parallel stay lit until the last bulb fails. The components can be identical. The system is not, because the rule that turns component states into a system state is different. That rule is the structure function. Once the component states are random, the probability the system works is the reliability.

## Intuition — Binary states, monotone systems
Label component $i$ by $x_i=1$ if it works and $x_i=0$ if it has failed. The structure $\varphi(x_1,\ldots,x_n)$ equals $1$ when the system works. A monotone system has the property that repairing a failed component cannot itself cause the system to fail: if $\mathbf{x}\le\mathbf{y}$ coordinatewise, then $\varphi(\mathbf{x})\le\varphi(\mathbf{y})$. A series system works only when every component works, so $\varphi(\mathbf{x})=\prod_i x_i$. A parallel system works when at least one component works, so $\varphi(\mathbf{x})=1-\prod_i(1-x_i)$.

## Definition — Two-out-of-three
A $k$-out-of-$n$ system works when at least $k$ components work. Two-out-of-three therefore has
$$
\varphi(x_1,x_2,x_3)=1\quad\text{when }x_1+x_2+x_3\ge 2,
$$
and $\varphi=0$ otherwise. The multilinear form that agrees with this rule on binary inputs is
$$
\varphi(\mathbf{x})=x_1x_2+x_1x_3+x_2x_3-2x_1x_2x_3.
$$
If the component states $X_i$ are independent with $\Pr(X_i=1)=p$, the reliability is the binomial upper tail
$$
r(p)=\Pr(\varphi(\mathbf{X})=1)=3p^2(1-p)+p^3.
$$
{{cite:pishro_nik2014}} (§5.1, independent random variables)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
On a binary vector the sum of the three pairwise products counts the number of working pairs, and the triple product is $1$ only when all three work. If two components work, exactly one pair is working and the triple product is $0$, so $\varphi=1$. If all three work, each pair contributes $1$ and the triple product subtracts $2$, leaving $3-2=1$. If fewer than two work, every product is $0$. Thus the polynomial matches the threshold rule.

Under independent components with common success probability $p$, the system works if exactly two components work or if all three work. There are three ways to choose the failed component, each with probability $p^2(1-p)$, and one way for all three to work, with probability $p^3$. Adding these disjoint probabilities gives $r(p)$. Independence is what lets the joint probability of a named pattern factor into $p$ and $1-p$.{{cite:pishro_nik2014}} (§5.1, independent random variables)
:::
:::

## Worked example
At $p=0.9$,
$$
r(0.9)=3(0.81)(0.1)+(0.9)^3=0.243+0.729=0.972.
$$
The state $(1,1,0)$ has $\varphi=1$, and $(1,0,0)$ has $\varphi=0$. A series system of the same three components would have reliability $0.9^3=0.729$, which is smaller because it refuses every state with a single failure.

**Your turn.** Compute $r(0.8)$ for the same two-out-of-three system.

::: {.callout-tip collapse="true" title="Answer"}
$$
r(0.8)=3(0.64)(0.2)+(0.8)^3=0.384+0.512=0.896.
$$
Lowering each component reliability from $0.9$ to $0.8$ drops the system reliability from $0.972$ to $0.896$.
:::

## Connections — Paths, cuts, and lifetimes
The [reliability function](reliability-function.qmd) is $r(\mathbf{p})=\Pr(\varphi(\mathbf{X})=1)$ once the component states are random. For independent components it is the multilinear structure polynomial with each $x_i$ replaced by $p_i$. {{cite:pishro_nik2014}} (§5.1, independent random variables) A minimal path is a set of components that is sufficient for $\varphi=1$ and has no smaller subset that is sufficient. A series arrangement is the special case of $n$-out-of-$n$, and a parallel arrangement is $1$-out-of-$n$. Replacing a static state by a lifetime turns the same structure into a system lifetime: a series lifetime is the first component failure.

## Check yourself

### A series of two
Write $\varphi$ for two components in series, and the reliability when they work independently with probabilities $0.9$ and $0.8$.

::: {.callout-tip collapse="true" title="Answer"}
$\varphi(x_1,x_2)=x_1x_2$. Independence gives $r=0.9\times 0.8=0.72$.
:::

### One failed component in parallel
Three components stand in parallel and the state is $(0,1,0)$. Does the system work?

::: {.callout-tip collapse="true" title="Answer"}
Yes. A parallel structure works when at least one component works, and here $\varphi=1-(1-0)(1-1)(1-0)=1$. The two failures do not matter.
:::
