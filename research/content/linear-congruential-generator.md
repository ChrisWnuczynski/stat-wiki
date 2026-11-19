## Motivating example
A simulation must be repeatable when a bug is investigated. A linear congruential generator supplies a deterministic sequence controlled by a seed. The useful question is how its arithmetic affects repetition and dependence, rather than whether a particular list of decimals looks irregular.{{cite:hull_dobell1962}} (§3, pp. 232–233)

## Definition — A map on a finite residue set
Choose a positive integer modulus $m$, an integer multiplier $a$, an increment represented by $0\le c<m$, and a seed $x_0\in\{0,\ldots,m-1\}$. The recurrence is
$$
x_{j+1}=(ax_j+c)\bmod m,\qquad u_j=x_j/m.
$$
The state belongs to $\{0,\ldots,m-1\}$ and the scaled output belongs to $[0,1)$. At most $m$ distinct states can appear before a repeat. After a state repeats, the subsequent states repeat because the update is deterministic.{{cite:hull_dobell1962}} (§3, pp. 232–233)

The mixed generator has $c\ne0$; the multiplicative generator has $c=0$. A zero seed is then absorbing. The distinction affects achievable periods and the arithmetic conditions used to choose parameters.{{cite:hull_dobell1962}} (§3, Theorems 1–2, pp. 233–236)

## Properties — Period is only one diagnostic

[]{#property-full-period}
For a mixed generator to have full period $m$, the increment must be relatively prime to $m$, every prime factor of $m$ must divide $a-1$, and $4$ must divide $a-1$ when it divides $m$. These are the Hull–Dobell conditions. They concern visiting all residues; they do not establish independence of successive outputs.{{cite:hull_dobell1962}} (§3, Theorem 1, p. 233)

The pairs $(u_j,u_{j+1})$ are constrained by the recurrence. A complete traversal of the marginal state set can therefore coexist with a poor multidimensional pattern. For the multiplicative case, write $x_{j+1}=ax_j-mk_j$ for an integer $k_j$. Dividing by $m$ gives $u_{j+1}-au_j=-k_j$, so successive pairs lie on parallel lines. The same relation between the first two coordinates constrains longer tuples to parallel hyperplanes. A long cycle therefore does not remove geometric structure.{{cite:marsaglia1968_planes}} (Thm. 1 and proof, pp. 25–27) Statistical checks of generated sequences address a different issue from full-period arithmetic.{{cite:hull_dobell1962}} (§4, statistical considerations)

## Worked example
Take $m=16$, $a=5$, $c=1$, and $x_0=0$. Iterating gives
$$
0,1,6,15,12,13,2,11,8,9,14,7,4,5,10,3,0.
$$
Every residue appears once before returning to the seed, giving period $16$. The increment is relatively prime to $16$ and $a-1=4$ is divisible by both $2$ and $4$. By contrast, taking $a=3$ with the same increment and modulus gives $0,1,4,13,8,9,12,5,0$, of period $8$.{{cite:hull_dobell1962}} (§3, Theorem 1, p. 233)

For the full-period example, the average of the scaled outputs over one cycle is $7.5/16=0.46875$. The midpoint transformation $(x_j+1/2)/16$ has cycle average $1/2$ and excludes both endpoints. Neither transformation makes the deterministic outputs independent.

**Your turn.** Starting with $x_0=0$, compute the first three updates of the full-period generator and scale them by $16$.

::: {.callout-tip collapse="true" title="Answer"}
The updated states are $1,6,15$, so the scaled values are $0.0625,0.375,0.9375$.
:::

## History
Computer generation distinguishes random numbers from pseudorandom sequences, whose marginal frequencies and successive dependence require separate scrutiny.{{cite:dodge2008}} (p. 446)
