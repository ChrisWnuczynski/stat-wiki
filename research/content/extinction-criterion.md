## Lead context
The mean offspring count locates the survival threshold, while the full offspring distribution determines the probability of extinction above it.

## Statement
Let $Z_0=1$ and let each individual independently have an offspring count $\xi$ with probabilities $p_k$ and finite mean $m$. If $p_0>0$, extinction occurs with probability one for $m\le1$, and with probability strictly below one for $m>1$. If $p_0=0$, every individual has at least one child and extinction is impossible. In particular, the deterministic law $\xi=1$ has no extinction even though its mean is one.{{cite:durrett2019}} (§4.3.4, Thm. 4.3.10–4.3.12, pp. 231–233)

## Motivating example
A newly introduced lineage may have a growing expected population and still disappear. A family tree with either no children or two children makes the distinction visible: a large family later cannot rescue a lineage that has already reached zero. The event of survival concerns the entire sequence of generations rather than its average size at one time.{{cite:grinstead_snell1997}} (§10.2, branching processes)

## Intuition — Iterating the family tree
Write $f(s)=\sum_{k\ge0}p_ks^k$ and $q_n=\Pr(Z_n=0)$. Independence of descendant families yields
$$
q_0=0,\qquad q_{n+1}=f(q_n).
$$
Since zero is absorbing, the events $\{Z_n=0\}$ increase with $n$. Their probabilities tend to the eventual extinction probability $q$. Continuity of the generating function gives $q=f(q)$. If $r\in[0,1]$ is any fixed point, induction gives $q_n\le r$, so $q$ is the smallest fixed point.{{cite:grinstead_snell1997}} (§10.2, fixed-point recursion)

The derivative $f'(1-)=m$ compares the generating function with the diagonal near one. A supercritical slope places $f(s)$ below $s$ just to the left of one, while $f(0)=p_0>0$ places it above the diagonal at zero. A smaller intersection then determines extinction.{{cite:durrett2019}} (§4.3.4, Thm. 4.3.12, pp. 232–233)

## Key results — The boundary at one offspring on average
For $m<1$, $\mathbb E Z_n=m^n$ and $\Pr(Z_n>0)\le m^n$, proving certain extinction. At $m=1$, the expectation remains one for every generation, so the expectation bound alone gives no decay. Convexity of $f$ supplies the critical conclusion. Multiple independent ancestors give extinction probability $q^r$ when $Z_0=r$.{{cite:durrett2019}} (§4.3.4, Thm. 4.3.10–4.3.12 and Ex. 4.3.12, pp. 231–234)

## Proof
The recursion above proves the smallest-fixed-point representation. For $p_0>0$ and $m\le1$, convexity gives $f(s)\ge f(1)+f'(1-)(s-1)\ge s$ on $[0,1]$. The inequality is strict for $s<1$: if the offspring law has positive probability of two or more children, the generating function is strictly convex on $(0,1)$; if it is supported on $\{0,1\}$, then $f(s)-s=p_0(1-s)>0$. Thus the smallest fixed point is one. For $m>1$, $f(s)<s$ sufficiently close to one, and $f(0)>0$, so an intersection exists below one. Convexity makes that intersection unique below one. This proves the criterion.{{cite:grinstead_snell1997}} (§10.2, generating-function argument){{cite:durrett2019}} (§4.3.4, Thm. 4.3.12)

## Worked example
Take $p_0=1/4$ and $p_2=3/4$. Then $m=3/2$ and
$$
f(s)-s=\frac{(s-1)(3s-1)}4.
$$
The smaller root is $q=1/3$, giving survival probability $2/3$. Extinction by generation one has probability $1/4$, and by generation two it has probability $f(1/4)=19/64$. These increase towards $1/3$. Three independent ancestors all die out with probability $(1/3)^3=1/27$.

**Your turn.** Change the probabilities to $p_0=3/4$, $p_2=1/4$. Find the mean and the root that is a probability of extinction.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $1/2$. The equation $s=3/4+s^2/4$ has roots $1$ and $3$. The only root in $[0,1]$ is $1$, so extinction is certain.
:::
