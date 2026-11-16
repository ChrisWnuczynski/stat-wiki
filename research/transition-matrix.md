# Transition matrix: research notes

## Sources opened

- **Checked:** Levin & Peres, *Markov Chains and Mixing Times*, 2nd ed., author-hosted edition, §1.1 (read earlier in this batch for the Markov-chain page). A transition matrix has entries $P(x,y)$, row distributions, $n$-step entries of $P^n$, and the row-vector convention $\mu_n=\mu_0P^n$. The author page at `https://pages.uoregon.edu/dlevin/MARKOV/` confirms the freely offered second edition. The PDF fetch timed out on this revisit, so this page uses the previously read full section and checks the formulas independently.
- **Checked:** inherited `sources/stat3004/chapters/sp-04-discrete-markov.qmd`, “Transition rules” and “Rain after two days.” Preserve its weather example (two-step probabilities $0.30$ and $0.45$), three-state reachability illustration, and row-orientation note. The new worked example uses a different directed cycle.
- **Checked:** inherited `sources/book/chapters/bayes-04-mcmc.qmd`, “Markov chains and equilibrium,” for the contrasting convention that uses columns indexing the current state. Distinguish the convention explicitly rather than treating one orientation as universal.
- **Checked for history:** Dodge, *The Concise Encyclopedia of Statistics*, “Markov, Andrei Andreevich,” pp. 330–331. It traces Markov's work on dependent sequences; it does not supply the matrix-power proof.

## Mathematical checks

- **Checked:** The row-stochastic directed-cycle-with-hold matrix $P=((1/2,1/2,0),(0,1/2,1/2),(1/2,0,1/2))$ has $P^2=((1/4,1/2,1/4),(1/4,1/4,1/2),(1/2,1/4,1/4))$ and $P^3=((1/4,3/8,3/8),(3/8,1/4,3/8),(3/8,3/8,1/4))$. From state A, $\Pr(X_2=C)=1/4$ through B. From C, $\Pr(X_2=B)=1/4$ through A. Uniform $(1/3,1/3,1/3)$ is stationary since columns also sum to one.
- **Checked:** If the first-step rule is a swap matrix $S=((0,1),(1,0))$ and the second-step rule is the identity $I$, the two-step rule is $SI=S$, whereas $S^2=I$. A single matrix power requires time homogeneity.
- **Checked:** For the deterministic two-state swap, $\pi=(1/2,1/2)$ is stationary but the distribution from a fixed state alternates. Stationarity does not by itself imply convergence.

## Scope decisions

- **Assumed:** States A, B, C are hypothetical process modes, not empirical observations.
- **Disputed:** “Rows and columns both sum to one” is not a general property of transition matrices; only rows must under this convention. The worked example happens to be doubly stochastic.
- **Disputed:** “$P^n$ converges because $P$ is a transition matrix” is false for periodic or reducible chains.
