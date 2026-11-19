## Lead context
The equations describe how a transition matrix changes when a small interval is appended to the start or end of an observation period.

## Motivating example
A machine alternates between working and repair. Its failure and repair rates determine more than its long-run availability: they determine the chance that it is under repair one hour after starting in working order. The forward and backward equations convert these rates into probabilities at each elapsed time.{{cite:siegrist2022_ctmc_transition}} (§15.16, “The Two-State Chain”)

## Definition — Two derivatives of one semigroup
For a finite time-homogeneous chain, the generator $Q$ has nonnegative off-diagonal entries and zero row sums. The transition matrix $P(t)$ obeys $P(s+t)=P(s)P(t)$ and $P(0)=I$. Writing $P(h)=I+hQ+o(h)$ gives
$$
P'(t)=P(t)Q,\qquad P'(t)=QP(t).
$$
The first equation is forward and the second backward. A probability row vector evolves by $\pi'(t)=\pi(t)Q$. A column vector of expected future rewards evolves by the backward equation. The matrix side matters even though $P(t)$ itself commutes with $Q$.{{cite:siegrist2022_ctmc_transition}} (§15.16, “The Transition Semigroup” and “Uniform Transition Semigroups”)

## Properties — A finite-state proof
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $h>0$, subtract $P(t)$ from $P(t+h)=P(t)P(h)$ and divide by $h$. The limit is $P(t)Q$. Using $P(t+h)=P(h)P(t)$ gives $QP(t)$. Finiteness permits the limits to pass through the matrix products. The matrix exponential solves both initial-value problems: termwise differentiation of its convergent series gives $Qe^{tQ}=e^{tQ}Q$.{{cite:siegrist2022_ctmc_transition}} (§15.16, “Uniform Transition Semigroups”)
:::
:::

On infinite state spaces, rates can be unbounded and explosion can occur. Forward differentiation requires conditions controlling the infinite sums. A finite-state argument should therefore not be extended merely by replacing finite matrix multiplication with an unrestricted series.{{cite:siegrist2022_ctmc_transition}} (§15.16, discussion of bounded generators)

The matrix equations also yield $P_t=e^{tQ}$ by the convergent matrix power series; each power commutes with $Q$.{{cite:durrett2012_essentials}} (§4.2, eqs. 4.7–4.10, pp. 123–125)

## Worked example
Use rates $\alpha=2$ from working state $0$ to repair state $1$, and $\beta=3$ in the reverse direction. Then
$$
Q=\begin{pmatrix}-2&2\\3&-3\end{pmatrix},\qquad
p_{01}(t)=\frac25(1-e^{-5t}).
$$
At time $1$, $p_{01}(1)=0.397305$ to six decimal places. Its derivative at zero is $2$, the failure rate. The limiting repair probability is $2/5$ and the working probability is $3/5$. The full transition matrix at time $1$ has rows approximately $(0.602695,0.397305)$ and $(0.595957,0.404043)$.{{cite:siegrist2022_ctmc_transition}} (§15.16, “The Two-State Chain”)

**Your turn.** With both rates equal to $1$, what is the chance of being in state $1$ at time $1$ starting in state $0$?

::: {.callout-tip collapse="true" title="Answer"}
It is $(1-e^{-2})/2=0.432332$, with limiting probability $1/2$.
:::

## History
Kolmogorov's work on probability and stochastic processes developed alongside his measure-theoretic foundations. He became a professor in 1931 and published his probability monograph in 1933.{{cite:dodge2008}} (p. 282)
