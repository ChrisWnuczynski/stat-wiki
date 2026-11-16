# Probability measure

Type: Concept/definition. Rank 178.

## Material checked

- **Checked:** Frozen baseline: 388 body words, one figure, three axioms, five probability properties, finite equal-outcome formula. The figure and the full original Properties section are preserved.
- **Checked:** Durrett, *Probability: Theory and Examples* (5th ed.), full author-hosted text, Ch. 1 §1.1 pp. 1–3 (probability space, sigma-algebra, measure, basic results, discrete construction) and §1.2 (induced distributions and non-density examples).
- **Checked:** Dodge (2008) printed p. 282 records Kolmogorov's 1933 monograph. History is confined to that checked fact.
- **Checked by code:** The six loaded-die weights and all worked and practice event probabilities are exact `Fraction` sums in `checks/probability-measure.py`.
- **Assumed:** The six face weights define the measure on the full power set. The counterexamples to additivity are deliberately inconsistent proposed assignments, not probabilistic models.
- **Disputed:** Informally saying the measure assigns probabilities to “the events” is correct only after the event sigma-algebra is specified; the new Definition makes the domain explicit. Equal likelihood is a special finite case, not an axiom.

## Sources opened and used

1. Durrett, *Probability: Theory and Examples*, 5th ed. (2019), Ch. 1 §§1.1–1.2, full author-posted PDF `https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf`; existing key `durrett2019`.
2. Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 282, Kolmogorov entry; existing key `dodge2008`.

## Changes and checks

One collapsed proof covers the inherited probability identities plus continuity from above and below. Two existing answered bank questions are requested as hidden self-checks. Full gate results recorded in commit run.
