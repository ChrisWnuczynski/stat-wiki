## Lead context
Independent random variables carry no information about one another: the probability of any combination is the product of the separate probabilities.

## Motivating example
Two rolls of one fair die are independent. The face on the first roll does not change the chance of a six on the second, and the probability of two sixes is $(1/6)\times(1/6)$.{{cite:grinstead_snell1997}} (§4.1, ex. 4.14, pp. 144–145) A different experiment looks similar and is not independent. A die is drawn at random from a box that contains a biased die, and then rolled twice. The first roll says something about which die was drawn, so it changes the probability of the second roll.

## Intuition — The joint distribution factors
Independence is a property of the joint distribution, not of the individual marginals. Random variables $X$ and $Y$ are independent when any event determined by $Y$ leaves the probability of every event determined by $X$ unchanged.{{cite:durrett2019}} (§2.1, pp. 43–44) Discrete random variables $X$ and $Y$ are independent when $\Pr(X=x,Y=y)=\Pr(X=x)\Pr(Y=y)$ at every pair $(x,y)$. Knowing $Y=y$ (with $\Pr(Y=y)>0$) then leaves the conditional distribution of $X$ equal to its marginal. Continuous variables with a joint density are independent when that density is the product of the marginal densities, and an infinite sequence is independent when every finite subcollection is.{{cite:pishro_nik2014}} (§5.1, independent random variables)

## Definition — Borel events, joint distribution functions, and product laws
For general real-valued random variables $X_1,\ldots,X_n$ on a common probability space — whether discrete, continuous, or mixed — independence means that for all Borel sets $B_1,\ldots,B_n\subseteq\mathbb{R}$,
$$
\Pr(X_1\in B_1,\ldots,X_n\in B_n)=\prod_{k=1}^n \Pr(X_k\in B_k),
$$
equivalently that the generated $\sigma$-fields $\sigma(X_1),\ldots,\sigma(X_n)$ are independent; an arbitrary family of random variables is independent when every finite subcollection is.{{cite:durrett2019}} (§2.1, thm. 2.1.1, pp. 43–44) Because half-lines $(-\infty,x_k]$ form a $\pi$-system generating the Borel sets, $X_1,\ldots,X_n$ are independent if and only if their joint cumulative distribution function factors at every point $(x_1,\ldots,x_n)\in\mathbb{R}^n$,
$$
F_{X_1,\ldots,X_n}(x_1,\ldots,x_n)=\Pr(X_1\le x_1,\ldots,X_n\le x_n)=\prod_{k=1}^n F_{X_k}(x_k),
$$
so testing half-lines suffices to establish Borel independence.{{cite:durrett2019}} (§2.1.1, thm. 2.1.8, p. 47)

In measure-theoretic terms, if each $X_k$ has marginal law $\mu_k$, independence is equivalent to $(X_1,\ldots,X_n)$ having the product distribution $\mu_1\times\cdots\times\mu_n$ on $\mathbb{R}^n$.{{cite:durrett2019}} (§2.1.2, thm. 2.1.11, p. 48) On countable supports, taking singleton Borel sets $B_k=\{x_k\}$ reduces this condition to the point-mass factorisation across all tuples $(x_1,\ldots,x_n)$.{{cite:grinstead_snell1997}} (§4.1, def. 4.4, p. 143) When $(X_1,\ldots,X_n)$ has a joint density, Borel independence holds if and only if a version of the joint density factors into marginal densities (or into nonnegative measurable coordinate factors $g_1(x_1)\cdots g_n(x_n)$).{{cite:durrett2019}} (§2.1, exs. 2.1.1–2.1.2, p. 54)

## Properties — Integrable expectations and measurable transformations
Borel-measurable functions applied to disjoint blocks of independent random variables remain independent; in particular, if $X$ and $Y$ are independent and $g,h:\mathbb{R}\to\mathbb{R}$ are Borel measurable, then $g(X)$ and $h(Y)$ are independent.{{cite:durrett2019}} (§2.1.1, thm. 2.1.10, p. 47) If $X$ and $Y$ are independent and integrable, meaning $\E[|X|]<\infty$ and $\E[|Y|]<\infty$ (or if $X\ge 0$ and $Y\ge 0$), then $XY$ is integrable with $\E[|XY|]=\E[|X|]\E[|Y|]<\infty$ and
$$
\E[XY]=\E[X]\E[Y],
$$
extending to $\E[g(X)h(Y)]=\E[g(X)]\E[h(Y)]$ whenever $\E[|g(X)|]<\infty$ and $\E[|h(Y)|]<\infty$.{{cite:durrett2019}} (§2.1.2, thm. 2.1.12, p. 48) By induction, $\E\bigl[\prod_{k=1}^n X_k\bigr]=\prod_{k=1}^n \E[X_k]$ whenever $X_1,\ldots,X_n$ are independent with $\E[|X_k|]<\infty$ for each $k$, while the converse fails even for $n=2$: uncorrelated variables with $\E[XY]=\E[X]\E[Y]$ need not be independent.{{cite:durrett2019}} (§2.1.2, thm. 2.1.13 and ex. 2.1.14, p. 49)

For general distributions with $\E[|X|],\E[|Y|]<\infty$, the expectation identity integrates $xy$ against the product measure $\mu_X\times\mu_Y$ via Fubini's theorem.{{cite:durrett2019}} (§2.1.2, thm. 2.1.12, p. 48) When $X$ and $Y$ are discrete with finite support, the argument reduces to factoring a finite double sum, which is the finite-support case proved next.{{cite:grinstead_snell1997}} (§6.1, thm. 6.4, pp. 233–234)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For independent discrete variables with finite support,
$$
\E[XY]=\sum_{x,y} xy\,\Pr(X=x,Y=y)=\sum_{x,y} xy\,\Pr(X=x)\Pr(Y=y).
$$
Because the support is finite, the double sum separates into $\bigl(\sum_x x\Pr(X=x)\bigr)\bigl(\sum_y y\Pr(Y=y)\bigr)=\E[X]\E[Y]$.{{cite:pishro_nik2014}} (§5.1, independent random variables)
:::
:::

## Worked example
Let $X$ and $Y$ be independent Bernoulli variables with $\Pr(X=1)=0.4$ and $\Pr(Y=1)=0.5$. Then $\E[X]=0.4$, $\E[Y]=0.5$ and $\E[XY]=\Pr(X=Y=1)=0.4\times 0.5=0.2$, which equals the product of the means. A different joint distribution on $\{0,1\}^2$,
$$
\begin{align*}
\Pr(0,0)&=0.2,&\Pr(0,1)&=0.3,\\
\Pr(1,0)&=0.1,&\Pr(1,1)&=0.4,
\end{align*}
$$
has $\E[X]=0.5$, $\E[Y]=0.7$ and $\E[XY]=0.4$. The product of the means is $0.35$, not $0.4$, so $X$ and $Y$ are not independent. The marginals alone cannot show this. The joint probability $\Pr(X=1,Y=1)=0.4$ disagrees with $0.5\times 0.7=0.35$.

**Your turn.** In the independent Bernoulli pair, find $\Pr(X=0,Y=1)$.

::: {.callout-tip collapse="true" title="Answer"}
$\Pr(X=0)=0.6$ and $\Pr(Y=1)=0.5$, so the joint probability is $0.6\times 0.5=0.3$.
:::

## Common misconceptions — Pairwise independence is weaker than mutual independence
Checking independence two variables at a time does not establish mutual independence for three or more variables. Let $U$ and $V$ be independent fair bits in $\{0,1\}$ with $\Pr(U=0)=\Pr(U=1)=1/2$ and $\Pr(V=0)=\Pr(V=1)=1/2$, and define $W=U\oplus V$ (exclusive-or, addition modulo $2$). The triple $(U,V,W)$ takes only the four equally likely values $(0,0,0)$, $(0,1,1)$, $(1,0,1)$, and $(1,1,0)$, each with probability $1/4$, so $W$ is also a fair bit with $\Pr(W=0)=\Pr(W=1)=1/2$. Every pair — $(U,V)$, $(U,W)$, and $(V,W)$ — assigns probability $1/4=(1/2)(1/2)$ to each of its four outcomes in $\{0,1\}^2$, so $U,V,W$ are pairwise independent. Yet the triple is not mutually independent: $\Pr(U=V=W=0)=1/4$ rather than $(1/2)^3=1/8$, because $U$ and $V$ determine $W$ completely.{{cite:durrett2019}} (§2.1, ex. 2.1.4, p. 45)

## Connections — Events, conditional independence, and sums
[Independent events](independent-events.qmd) correspond to independent indicator random variables, and [conditional independence](conditional-independence.qmd) applies the same factorisation inside a conditional distribution, so variables can be dependent on the margin and independent given a third variable. Independence is what lets a [convolution](convolution.qmd) obtain the law of a sum from the marginals, and what makes pairwise covariances vanish so the variance of a finite sum of square-integrable variables equals the sum of the variances.{{cite:durrett2019}} (§2.1, thm. 2.1.3, p. 44; §2.1.3, thms. 2.1.15–2.1.16, pp. 49–50)
