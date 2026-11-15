# Conditional independence

Type: Concept/definition.

## Existing material read

- `articles/conditional-independence.qmd` before the edit: the general definition, the discrete and density product formulas, the four listed properties, the five density identities, and the separating-set sentence. Citations present: Lauritzen 1996 in the body, and Besag 1974 in the reference list. Twenty-six linked questions. No figures. Leading body: 505 words under the `PROGRESS.md` count.
- `sources/stat3006/chapters/sl-19-graphical-models.qmd`, the conditional-independence section.

## Sources opened and facts used

1. A. P. Dawid, [“Conditional Independence in Statistical Theory” (1979)](https://people.csail.mit.edu/tdanford/discovering-causal-graphs-papers/dawid-79.pdf), *Journal of the Royal Statistical Society B* 41(1), 1–31. The file is a scanned copy; the text was read from the extraction. Read §3.1–3.2 (definition, symmetry as Theorem 3.1, sufficiency) and §4 (Lemmas 4.1–4.3: the joint-variable form, reduction for a function of \(X\), and contraction). The running heads place the definition on journal p. 2, Theorem 3.1 on p. 3, and the lemmas on p. 4. The scan also records the marginalisation paradox for improper distributions. New key `dawid1979`, DOI `10.1111/j.2517-6161.1979.tb01052.x`.
2. Lauritzen 1996 remains the citation already attached to the density identities and the global Markov sentence. That book was not opened. No new formula was attributed to it beyond the separation sentence already printed on the page.

## Verification and decisions

- Added a formula-free lead, the two-experiment motivation, the discrete definition aligned with the existing product formula, symmetry and the reduction and contraction properties, one collapsed proof, a fully numerical example in which the variables are conditionally independent and marginally dependent, and a history limited to the opened paper plus the separation sentence already on the page.
- The proof covers symmetry, reduction, contraction, and the two density cancellations already displayed. It is stated for positive discrete probabilities and for densities where the relevant marginals are positive.
- `checks/conditional-independence.py` checks the joint probabilities, the marginal product \(1/4\), the joint success probability \(5/16\), the conditional probability \(5/8\), and the within-slice conditional probability \(1/4\).
- The original definition, four bullets, five density identities, separating-set sentence, citation keys, and twenty-six question links remain.

## Correction pass

- Recast the page type as a concept/definition. Corrected the correlation wording to distinguish marginal from conditional correlation and supplied a counterexample for the converse.
- The added prose now cites only Dawid §§3–4, the opened source. Removed new graphical-model and Lauritzen claims that this research did not substantiate; the pre-existing chapter excerpt still has Lauritzen citations and needs a separate source audit. Rephrased reader-facing prose and checked printed numerical values.
