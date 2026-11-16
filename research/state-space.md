# State space — rank 100

Type: Concept. Frozen baseline 285 body words, no figures. The source's definition, process notation, weather-history warning, infobox and related links remain generated. The new page builds from the distinction between time and state to a four-state Markov construction.

## Sources read

- **Checked:** David A. Levin and Yuval Peres, *Markov Chains and Mixing Times*, 2nd ed. (2017), author-hosted full PDF, §1.1 pp. 2–5 for the state space, Markov property, transition matrix and $\mu_t=\mu_0P^t$; Chapter 1 Notes p. 19 for Markov's 1906 work. Bibliography entry is pending from rank 98.
- **Checked:** W. K. Hastings, original 1970 *Biometrika* paper, §2.2 pp. 100–101, for extending a finite transition construction to continuous states; full author-hosted published scan read for rank 99.
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics* (2008), printed pp. 330–331, local authorized Markov entry for historical orientation. Its index has no dedicated state-space entry.
- **Checked by code:** The four-state transition matrix has nonnegative rows summing to one. Its pair-state transitions match the stipulated rain probabilities; two more rainy days have probabilities $0.24$ versus $0.64$ from the two rainy states, and the hidden exercise's two-day rain chance is $0.22$.
- **Assumed:** The weather rule is a hypothetical second-order process, with past pairs possible under its initial distribution. The queue and hidden-environment cases are conceptual counterexamples rather than estimates from observations.
- **Disputed:** None. The state need not have a numeric label or be the sample space of whole trajectories.

## Proof and bank

The collapsed proof verifies the Markov property of the augmented pair and the failure of the one-label state from different conditional probabilities. The selected answered bank questions are `c-12` for the Markov sufficiency criterion, `ex-sp-same-marginals` for how identical state-level marginals can hide different paths, and `ex-sp-increments-and-levels` for separating the time index from process values. None duplicates the four-state numerical example. No additional unproved theorem is claimed.
