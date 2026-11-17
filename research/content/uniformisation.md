## Motivating example
A continuous-time chain has different exit rates in different states, while a Poisson clock has a single constant event rate. Uniformisation reconciles them by ringing a common clock sufficiently fast and allowing some rings to leave the state unchanged. It is both a construction of the process and a numerically stable way to compute its transition probabilities using nonnegative terms.{{cite:siegrist2022_ctmc_transition}} (§15.16, “Uniform Transition Semigroups”)

## Definition
For a finite generator $Q$, let $\nu_i=-q_{ii}$ and choose $\gamma>0$ with $\gamma\ge\max_i\nu_i$. The matrix $R=I+Q/\gamma$ is stochastic. At each independent rate-$\gamma$ Poisson-clock event, move according to $R$. A diagonal move is a virtual event and is not counted as an actual jump to a different state. Conditional on $n$ clock events, the state evolves according to $R^n$.{{cite:durrett2019}} (§3.7, Poisson counts and independent increments)

## Properties — Derive the mixture and its generator
Since $I$ commutes with $R$, ordinary power-series multiplication gives
$$e^{tQ}=e^{\gamma t(R-I)}=e^{-\gamma t}\sum_{n=0}^{\infty}\frac{(\gamma t)^n}{n!}R^n.$$
In finite dimensions both series converge absolutely, justifying their rearrangement. The coefficients are Poisson probabilities, so every term is nonnegative and the sum has row sums one. Conversely, the clock construction has short-time transition matrix
$$(1-\gamma h)I+\gamma hR+o(h)=I+hQ+o(h),$$
which identifies its generator as $Q$. This proves the finite-state construction rather than treating the Poisson weights as a formal analogy.{{cite:siegrist2022_ctmc_transition}} (§15.16, matrix-exponential representation)

In state $i$, a ring produces a real departure with probability $\nu_i/\gamma$. Thinning a Poisson clock gives real departures at rate $\nu_i$. Conditional on a departure, its destination probability is $R_{ij}/(1-R_{ii})=q_{ij}/\nu_i$. Hence both the holding-time law and the embedded jump probabilities match the generator. An absorbing state has $\nu_i=0$ and all its clock events are virtual.{{cite:durrett2019}} (§3.7.2, pp. 178–179, thinning)

## Worked example — A two-state chain with a faster clock
Take
$$Q=\begin{pmatrix}-2&2\\3&-3\end{pmatrix},\qquad\gamma=5,\qquad R=\begin{pmatrix}0.6&0.4\\0.6&0.4\end{pmatrix}.$$
Each row of $R$ is the stationary distribution. Direct multiplication gives $R^2=R$, so $R^n=R$ for every $n\ge1$. The Poisson mixture collapses to
$$P(t)=e^{-5t}I+(1-e^{-5t})R.$$
At $t=1$, starting in state zero, the probability of state one is $0.4(1-e^{-5})\approx0.397305$. Choosing $\gamma=3$ gives a different stochastic matrix, $\left(\begin{smallmatrix}1/3&2/3\\1&0\end{smallmatrix}\right)$, and a different distribution of virtual rings, but exactly the same $P(t)$. The generator identity $Q=\gamma(R-I)$ is unchanged.{{cite:siegrist2022_ctmc_transition}} (§15.16, “The Two-State Chain”)

At equilibrium, the real-jump rate is $0.6(2)+0.4(3)=2.4$ per unit time. The rate-$5$ construction therefore has average virtual-event rate $5-2.4=2.6$ at equilibrium. This describes computational events, not additional physical transitions of the process.

**Your turn.** A generator has exit rates $1,4,2$. Can $\gamma=3$ be used? If $\gamma=5$, what is the diagonal entry of $R$ in the state with exit rate $4$?

::: {.callout-tip collapse="true" title="Answer"}
The choice $3$ is invalid because the state of exit rate $4$ would have diagonal entry $1-4/3<0$. With $\gamma=5$, that diagonal is $1-4/5=0.2$, the probability of a virtual ring in that state.
:::

## Statistical use — A certified truncation error
Approximating the mixture by terms $0\le n\le M$ leaves a nonnegative error in each entry bounded by
$$P\{N>M\},\qquad N\sim\operatorname{Poisson}(\gamma t),$$
because every entry of every $R^n$ is at most one. Each truncated row sums exactly to $P(N\le M)$. Thus the missing row mass is a computable error certificate. With $\gamma t=5$ and $M=20$, the bound is approximately $8.1093\times10^{-8}$.{{cite:durrett2019}} (§3.7, Poisson probability mass function)

Choosing a needlessly large $\gamma$ increases the expected number of clock events, $\gamma t$, and usually the number of powers needed. Choosing a smaller value than the largest exit rate destroys stochasticity. For a finite chain, the largest exit rate is a natural starting choice; another value may be convenient when it simplifies the powers, as $\gamma=5$ does in the worked example.

## Assumptions and limits
Finite-state chains always have bounded exit rates. An infinite chain with unbounded exit rates has no single finite dominating clock of this form. Questions of explosion and infinite-dimensional operator convergence then need additional arguments. Even in finite dimensions, for very large $\gamma t$ direct factorial arithmetic can overflow or underflow; evaluating Poisson weights recursively or around their mode is a numerical issue separate from the exact mixture identity.
