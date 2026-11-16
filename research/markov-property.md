# Markov property

Type: Concept/definition. Rank 179.

## Material checked

- **Checked:** Frozen baseline: 902 body words, one figure, conditional Markov definition, transition-matrix and Chapman–Kolmogorov statements, six-stone example and one question link. All remain.
- **Checked:** Levin and Peres, full author-hosted 2017 book, §1.1 pp. 2–4 for the positive-probability-history definition, transition rows and path law; §1.3 pp. 7–8 for distinct irreducibility and aperiodicity conditions. The pending bibliography entry was already staged with rank 176.
- **Checked:** Dodge (2008), printed pp. 330–331, Markov entry for cautious historical context.
- **Checked by code:** Two-state weather paths, initial mixture and second-order counterexample probabilities; retained six-stone transition calculations in `checks/markov-property.py`.
- **Assumed:** The weather example uses a constant transition law, while Markov property by itself allows a time-dependent law. Only positive-probability conditioning histories are used.
- **Disputed:** “No memory” can be misread as independence of consecutive states. The new Intuition explains the conditional statement and the state-augmentation counterexample.

## Sources opened and used

1. Levin and Peres, *Markov Chains and Mixing Times*, 2nd ed. (2017), §§1.1, 1.3, author-hosted full text `https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf`; pending key `levin_peres2017` staged in rank 176.
2. Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 330–331, Markov entry; existing key `dodge2008`.

## Changes and checks

One collapsed proof covers the path-product and matrix-composition identities and pair-state augmentation. Two existing answered bank questions are requested as hidden self-checks. Full gate results recorded in commit run.
