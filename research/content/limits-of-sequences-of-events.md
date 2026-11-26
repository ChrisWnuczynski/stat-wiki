## Motivating example
An alarm may sound occasionally forever without eventually sounding every day. These are different long-run events. Limsup describes infinitely many occurrences; liminf describes eventual uninterrupted occurrence. The distinction is especially useful for convergence, where a sequence succeeds if each fixed error tolerance is violated only finitely often.{{cite:durrett2019}} (§2.3, pp. 67–68)

## Intuition — Read the quantifiers in order
For a fixed outcome $\omega$, membership in $\bigcap_m\bigcup_{n\ge m}A_n$ means: for every starting index $m$, there is some later $n$ with $\omega\in A_n$. No tail can eliminate all occurrences. Membership in $\bigcup_m\bigcap_{n\ge m}A_n$ instead means: there is one starting index after which every $A_n$ contains $\omega$. The first permits arbitrarily long gaps; the second permits only finitely many failures.{{cite:durrett2019}} (§2.3, definitions of limsup and liminf)

The events remain measurable because a sigma-algebra is closed under countable unions and intersections. The underlying set operations are deterministic; no independence assumption belongs in their definitions. Independence becomes relevant only when turning a sequence of event probabilities into a probability for a long-run occurrence.{{cite:tao2011_measure}} (§1.4, sigma-algebras and measurable spaces)

## Properties — Indicators and complements
For every outcome,
$$\mathbf1_{\liminf A_n}=\liminf_n\mathbf1_{A_n},\qquad
\mathbf1_{\limsup A_n}=\limsup_n\mathbf1_{A_n}.$$
The first limit is one precisely when the indicators are eventually always one; the second is one precisely when ones occur arbitrarily late. Hence $\liminf A_n\subseteq\limsup A_n$. De Morgan's laws also give $(\limsup A_n)^c=\liminf A_n^c$ and $(\liminf A_n)^c=\limsup A_n^c$. If the two sets agree, their common value is the set limit.{{cite:durrett2019}} (§2.3, pp. 67–68){{cite:tao2011_measure}} (§1.4, countable set operations)

Set convergence is exactly pointwise convergence of indicators. If the common limiting event is $A$, bounded convergence then gives $\mathbb{P}(A_n)\to \mathbb{P}(A)$. The converse fails: probabilities can converge while event membership keeps alternating. Even when no set limit exists,
$$\mathbb{P}(\liminf A_n)\le\liminf \mathbb{P}(A_n)\le\limsup \mathbb{P}(A_n)\le \mathbb{P}(\limsup A_n).$$
To prove the first inequality, let $B_m=\bigcap_{n\ge m}A_n$. Then $B_m\uparrow\liminf A_n$ and $\mathbb{P}(B_m)\le\inf_{n\ge m}\mathbb{P}(A_n)$. Pass to the limit by continuity from below. Apply that result to the complements for the last inequality.{{cite:durrett2019}} (§2.3, ex. 2.3.1){{cite:tao2011_measure}} (§1.4, ex. 1.4.24, dominated convergence for sets)

## Worked example — Alternation and shrinking neighborhoods
Let the sample space be $\{a,b,c\}$ with probabilities $(1/2,1/3,1/6)$. Alternate $A_{2k-1}=\{a,b\}$ and $A_{2k}=\{b,c\}$. The point $b$ occurs always; $a$ and $c$ occur infinitely often but each is absent infinitely often. Thus $\liminf A_n=\{b\}$ with probability $1/3$, while $\limsup A_n=\{a,b,c\}$ with probability one. The individual probabilities alternate between $5/6$ and $1/2$. The inequalities above become $1/3\le1/2\le5/6\le1$.

For a different example, use a uniform point on $[0,1]$ and $A_n=(0,1/n)$. These sets decrease and their intersection is empty: every positive point eventually exceeds $1/n$, and zero belongs to none of the sets. Both event limits are empty even though every $A_n$ has positive probability.{{cite:tao2011_measure}} (§1.2, ex. 1.2.11, downward monotone convergence)

**Your turn.** Alternate $A_{2k-1}=\{1,2\}$ and $A_{2k}=\{2,3\}$ on $\{1,2,3,4\}$. Find both limits.

::: {.callout-tip collapse="true" title="Answer"}
The liminf is $\{2\}$ and the limsup is $\{1,2,3\}$. Outcome 4 never occurs, while outcomes 1 and 3 keep returning without becoming permanent.
:::

## Connections — Convergence through deviation events
For random variables $X_n$, almost-sure convergence to $X$ means
$$\mathbb{P}\left(\bigcup_{k\ge1}\limsup_n\{|X_n-X|>1/k\}\right)=0.$$
Indeed, outside this countable union every rational tolerance $1/k$ is violated only finitely often, which is equivalent to convergence. If the probabilities of each such deviation sequence are summable, the first Borel–Cantelli lemma supplies the zero probabilities. Its proof is the tail union bound $\mathbb{P}(\bigcup_{n\ge m}A_n)\le\sum_{n\ge m}\mathbb{P}(A_n)\to0$; independence is unnecessary for this direction.{{cite:durrett2019}} (§2.3, thm. 2.3.1)

## Statistical use — Monotone sequences are a special case
If $A_n\subseteq A_{n+1}$, membership can change only from absent to present. A point in the union eventually enters and then stays, so both limits equal $\bigcup_n A_n$. If $A_{n+1}\subseteq A_n$, membership can change only from present to absent, and both limits equal $\bigcap_n A_n$. Continuity of probability then gives the corresponding limits of $\mathbb{P}(A_n)$. For increasing sets, write their union as the disjoint union of the first set and successive differences and apply countable additivity. Decreasing continuity follows by taking complements, since the total probability is finite. This elementary argument explains why tail unions and intersections are so useful: each forms a monotone sequence even when the individual events oscillate.{{cite:tao2011_measure}} (§1.4, countably additive measures; §1.2, ex. 1.2.11)

Neither event limit is the same as “at least one event occurs.” An event can happen once and belong to the union without belonging to the limsup. The liminf is stricter still, requiring a final stretch with no further absences. Reading these quantifiers before calculating probabilities prevents a finite occurrence from being mistaken for long-run behavior.{{cite:durrett2019}} (§2.3, limsup and liminf definitions)

## Common misconceptions
Equal probabilities do not force the sets to settle. On a fair coin, let $A_n$ be heads on odd $n$ and tails on even $n$. Every set has probability $1/2$, so the numerical sequence $\mathbb{P}(A_n)$ converges. The liminf is empty, because neither outcome belongs to every set from some index onward, and the limsup is the whole two-point space, because each outcome returns infinitely often. There is no set limit. The probability inequalities still hold: $\mathbb{P}(\liminf A_n)=0$ and $\mathbb{P}(\limsup A_n)=1$, with $0\le1/2\le1/2\le1$. Convergence of $\mathbb{P}(A_n)$ is a statement about numbers. Convergence of $A_n$ is a statement about which outcomes remain.{{cite:durrett2019}} (§2.3, pp. 67–68){{cite:tao2011_measure}} (§1.4, ex. 1.4.24, dominated convergence for sets)

The complement swaps the two limits. The complement of “$A_n$ occurs infinitely often” is “from some index onward, $A_n$ does not occur,” which is $\liminf A_n^c$. In the coin alternation, $A_n$ occurs infinitely often for both outcomes, so the complement is empty, matching $\liminf A_n^c=\emptyset$. In the shrinking neighborhoods $A_n=(0,1/n)$, each fixed positive point eventually leaves, so the limsup is empty and almost every outcome fails to occur infinitely often. A point that occurs only at $n=1$ is in the union and not in the limsup. Counting “ever” and counting “infinitely often” are different unions.{{cite:durrett2019}} (§2.3, definitions of limsup and liminf){{cite:tao2011_measure}} (§1.2, ex. 1.2.11, downward monotone convergence)

## Assumptions and limits — Almost-sure statements are limsup statements
A sample average converges almost surely to $\mu$ when, for every tolerance $1/k$, the event $\{|\overline X_n-\mu|>1/k\}$ occurs for only finitely many $n$, except on a set of probability zero. That sentence is a countable union of limsup events. The first Borel–Cantelli lemma turns summable probabilities into such a null limsup, and its proof is the tail union bound. Independence is not required for that direction. Dependence can still make the bound true while a second-moment calculation gives a sharper rate, or it can make the events so overlapping that the bound is loose. The lemma supplies a sufficient condition for a null limsup. It does not say that a divergent sum of probabilities forces the limsup to have probability one. That converse uses an independence or quasi-independence hypothesis of its own.{{cite:durrett2019}} (§2.3, thm. 2.3.1)

Indicator limits also explain monotone continuity without a separate axiom. If $A_n$ increases to $A$, then $\mathbf1_{A_n}$ increases to $\mathbf1_A$, both set limits equal $A$, and bounded convergence gives $\mathbb{P}(A_n)\to \mathbb{P}(A)$. The same conclusion follows from writing $A$ as the disjoint union of $A_1$ and the successive differences $A_{n+1}\setminus A_n$ and applying countable additivity. Decreasing sets pass to the complement, where the probabilities remain bounded by one. The alternating three-point example is the case the monotone argument does not cover: the indicators oscillate, the set limit fails, and the probabilities oscillate between $5/6$ and $1/2$. Monotone continuity is the special case in which the quantifiers collapse to a single eventual transition.{{cite:tao2011_measure}} (§1.4, countably additive measures; §1.2, ex. 1.2.11){{cite:durrett2019}} (§2.3, ex. 2.3.1)
