## Motivating example
A posterior density may be easy to evaluate up to a constant and hard to sample directly. A proposal mechanism supplies candidate states, and an acceptance rule corrects their relative frequencies. The invariance theorem establishes that one transition preserves the intended probability law. It separates the mathematical target of the transition from the further question of how quickly repeated transitions explore it.{{cite:hastings1970}} (§§2.1–2.2, pp. 98–100)

Rejection is part of that transition. When a proposed configuration is rejected, the next state repeats the current configuration and contributes again to an average. Removing such repetitions changes the stochastic process. In the physical sampling formulation, repeated configurations are explicitly counted when averages are calculated.{{cite:metropolis1953}} (§II, p. 1088)

## Statement
For a target density $\pi$ and proposal density $q(y\mid x)$, on pairs with $\pi(x)q(y\mid x)>0$ define
$$a(x,y)=\min\left\{1,\frac{\pi(y)q(x\mid y)}{\pi(x)q(y\mid x)}\right\}.$$
At a current state with positive target density, a candidate outside target support is rejected. Complete the accepted off-diagonal transitions with their rejection probability on the diagonal. The resulting Markov kernel satisfies detailed balance and hence leaves $\pi$ invariant. Null-target starting states require a compatible definition of the kernel but do not affect an invariance statement under $\pi$.{{cite:hastings1970}} (§2.2, eqs. 4–6, pp. 99–100)

## Proof
For distinct states with nonzero proposal flow,
$$\pi(x)q(y\mid x)a(x,y)=\min\{\pi(x)q(y\mid x),\pi(y)q(x\mid y)\}.$$
This expression is symmetric in $x$ and $y$, proving off-diagonal detailed balance. Diagonal mass pairs a state with itself and is automatically symmetric. Integrating the balance identity over starting states gives $\int\pi(dx)P(x,dy)=\pi(dy)\int P(y,dx)=\pi(dy)$, because a transition kernel has total mass one. The same argument covers zero reverse-proposal flow by assigning zero accepted forward flow.{{cite:hastings1970}} (§2.2, pp. 99–100)

Writing $\pi=f/Z$ cancels $Z$ in the acceptance ratio. Proposal factors cancel only for a symmetric proposal. These are separate cancellations: an unknown target normalizer can disappear even when the proposal ratio remains necessary.{{cite:hastings1970}} (§2.2, p. 100)

## Worked example — An asymmetric two-state proposal
Let target probabilities be $(0.8,0.2)$ on states $A,B$, and use proposal matrix $Q=\begin{pmatrix}0.1&0.9\\0.2&0.8\end{pmatrix}$. The acceptance probability from $A$ to $B$ is $1/18$, while the reverse acceptance probability is one. Thus the transition matrix is
$$P=\begin{pmatrix}0.95&0.05\\0.2&0.8\end{pmatrix}.$$
Its probability flows between the states agree: $0.8(0.05)=0.2(0.2)=0.04$. Multiplication gives $(0.8,0.2)P=(0.8,0.2)$, verifying invariance directly. This finite example instantiates the acceptance rule and its balance proof.{{cite:hastings1970}} (§2.2, eqs. 4–6)

If every proposal from $A$ to $B$ were accepted solely because $B$ can propose the reverse move, the target would be wrong. Acceptance must correct the magnitudes of proposal flow, not merely check that both directions are possible.

**Your turn.** Replace $Q$ by a proposal that always switches between the two states. Find the acceptance probability from $A$ to $B$ and the two off-diagonal transition probabilities.

::: {.callout-tip collapse="true" title="Answer"}
The proposal is symmetric. Acceptance from $A$ to $B$ is $0.2/0.8=1/4$, and from $B$ to $A$ is one. Therefore $P(A,B)=1/4$ and $P(B,A)=1$.
:::

## Key results — Deleting rejected iterations changes the weights
Let $A(x)=\int q(y\mid x)a(x,y)dy$ be the probability of accepting a candidate. Repeating proposals until acceptance changes the transition to $q(y\mid x)a(x,y)/A(x)$. Its pairwise flow is symmetric after weighting by $\pi(x)A(x)$, so its invariant density is proportional to that product when it can be normalized. State-dependent acceptance therefore alters frequencies if rejected iterations are omitted. The change follows directly by substituting the new transition into detailed balance.

In the two-state example, accepting a self-proposal counts as acceptance. Hence $A(A)=0.1+0.9/18=0.15$ and $A(B)=1$. The acceptance-only sequence has invariant weights proportional to $(0.12,0.2)$, namely $(3/8,5/8)$, rather than the target $(0.8,0.2)$. Keeping every attempted iteration preserves the intended residence times.{{cite:metropolis1953}} (§II, p. 1088)

## Common misconceptions — Stationarity does not establish convergence
An invariant distribution remains invariant if the chain starts from it. Convergence from a specified starting state needs further conditions, such as irreducibility and an appropriate aperiodicity condition. Even when convergence holds, strong dependence can make a finite average imprecise. The proposal affects efficiency while the acceptance correction establishes the target.{{cite:hastings1970}} (§2.1, pp. 98–99)

For example, an identity transition leaves every distribution invariant and never moves. It shows why a balance calculation alone cannot certify exploration. Conversely, rejections are compatible with correct sampling and must not be removed merely to make a sequence look more mobile.
