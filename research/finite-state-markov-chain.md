# Finite-state Markov chain

Type: Concept/definition. Rank 176.

## Material checked

- **Checked:** Frozen baseline: 1,076 words, two figures, finite-state and homogeneous definitions, limiting-distribution theorem and three worked examples. Both figure instances and all worked examples remain.
- **Checked:** Levin and Peres, *Markov Chains and Mixing Times* (2nd ed.), author-posted full book, §§1.1, 1.3, 1.5 and 4.3. The finite-state transition matrix, row-vector convention, positive-power lemma, stationary construction and convergence proof were read directly.
- **Checked:** Dodge (2008), pp. 330–331, Markov biographical entry, used only for a cautious historical sentence.
- **Checked by code:** `checks/finite-state-markov-chain.py` recomputes the new two-state machine example, the retained six-state stepping-stone values and retained weather-chain probabilities.
- **Assumed:** All displayed matrices are time-homogeneous conditional transition laws. The convergence statement requires finite state space, irreducibility and aperiodicity.
- **Disputed:** The inherited informal definition omits that conditioning events must have positive probability; the new Definition states this. The inherited infinite-state figure is a counterexample to an overbroad reading of the finite-state convergence theorem, and is retained as such.

## Sources opened and used

1. Levin and Peres, *Markov Chains and Mixing Times*, 2nd ed. (2017), §§1.1, 1.3, 1.5, 4.3, full author-hosted book at `https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf`; pending bibliography key `levin_peres2017` exactly matches batch A.
2. Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 330–331, Markov entry; existing key `dodge2008`.

## Changes and checks

One collapsed proof covers Chapman–Kolmogorov, stationary existence and uniqueness, and convergence by a positive-power minorization. Two existing answered Markov question-bank pages are requested as hidden self-checks. Full gate results recorded in the commit run.
