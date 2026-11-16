# Stationary distribution — rank 98

Type: Concept/definition. Frozen baseline 667 body words, no figures. The source definition, weather-chain calculation, doubly stochastic property, two-state calculation, infobox, laboratory link and seven question links remain generated from their original inputs.

## Sources read

- **Checked:** David A. Levin and Yuval Peres, *Markov Chains and Mixing Times*, 2nd ed. (2017), author-hosted full text at https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf. Read §1.3 Example 1.8, §1.5 pp. 9–13 (eqs. 1.14–1.15, Example 1.12, Proposition 1.14, Corollary 1.17, Proposition 1.19), §1.6 pp. 13–14 (Proposition 1.20 and Examples 1.21–1.22), §1.7 on closed classes, §3.1 on sampling and §4.3 on convergence, plus Chapter 1 Notes p. 19 for the 1906 history.
- **Checked:** Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), printed pp. 330–331, “Markov, Andrei Andreevich,” from the authorized local source. It supports only the history of Markov's work and mathematical setting, not the stationary-distribution theorem.
- **Checked by code:** The worked transition matrix is stochastic, the vector $(0.2,0.4,0.4)$ is stationary, the two-step law from state zero is $(0.375,0.375,0.25)$, and the Your turn vector is $(1/3,2/3)$. `checks/stationary-distribution.py` covers these and the retained source examples.
- **Assumed:** The worked machine transition rule is a hypothetical finite-state model; no empirical fit is claimed. Its self-loops and connected graph give aperiodicity and irreducibility.
- **Disputed:** None. The inherited sentence “long-run fraction of time” is valid in the finite irreducible setting but must not be confused with stepwise convergence for periodic chains; the new text distinguishes them.

## Proof status and integration

One collapsed proof establishes propagation of a stationary start, uniform stationarity for doubly stochastic matrices, graph-degree stationarity, detailed balance sufficiency and a no-stationary-law infinite counterexample. The more extensive existence/uniqueness, return-time, convergence and closed-class results are recorded in pending proofs. The pending bibliography entry adds the author-hosted textbook. Three existing answered questions are selected for the bank: deterministic cycle, path graph and closed classes; none duplicates the numeric worked example.
