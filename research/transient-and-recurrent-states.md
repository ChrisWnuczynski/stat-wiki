# Transient and recurrent states

Rank 196. Type: Concept. Frozen baseline: 477 body words, zero figures. The original return-time, visit-count, absorbing-state and stationary-mass statements and all question links are retained.

## Checked

- **Checked in full source:** Dodge (2008), printed pp. 330–331, “Markov, Andrei Andreevich”, describes his work on dependent processes and its Kazan University appearances. Both complete extracted pages `/workspace/statwiki-sources/dodge2008/pages/pdf-0330.txt` and `pdf-0331.txt` were read. This supports history only, not recurrence proofs.
- **Checked in the repository source chapter:** `sources/stat3004/chapters/sp-05-classes-and-reversibility.qmd`, §§“Communication and closed classes” and “Recurrence and period”, for definitions and finite-state structure.
- **Checked by proof:** One collapsed box proves geometric visit counts, positive recurrence in finite closed irreducible classes, and transient behaviour of finite states outside closed classes. The inherited stationary-mass/mean-return identity and class-wide recurrence-type theorem remain logged as proof debt.
- **Checked by code:** `checks/transient-and-recurrent-states.py` verifies transition row sums and return/visit calculations in the original two-state example, new three-state example and pending two-state question.
- **Assumed:** Time-homogeneous Markov transitions and a countable state space; finiteness is explicitly used for the closed-class recurrence theorem. The new three-state example's B and C transitions are deterministic.
- **Disputed:** A large one-step self-loop probability does not make a state recurrent. The article separates total visits (including time zero) from the original $N_i$ of later visits. An infinite-state chain need not inherit the finite closed-class conclusion.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 330–331, Markov biography; existing `dodge2008` key.
- The repository stochastic-processes course chapter was read for the existing definitions. Its inherited Norris, Feller and Grimmett–Stirzaker citations remain in the original block; new claims are proved rather than attributed to unread texts.

## Changes

Added motivation, explicit return-time definition, finite-class proof, numerical three-state example with hidden answer, misconceptions, distinct failure cases, connections and sourced history. An existing closed-class bank question and a new answered return-time question await shared integration. No figure was present.
