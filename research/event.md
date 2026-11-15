# Event

Type: Concept/definition.

## Existing material read

- `articles/event.qmd` before the edit: event-as-subset definition, five probability properties with a direct argument, a four-engine aircraft worked example, three inline citations, and twelve linked questions. Leading body: 460 words; no figures.
- `sources/stat2003/chapters/prob-01-experiments.qmd`, especially the sample-space, event, probability-measure, and component-system sections; `sources/stat3004/chapters/sp-09-probability-spaces.qmd` for measurable events and countable additivity.
- `questions/ex-prob-two-dice-faces.qmd`, `questions/ex-prob-channel-zero.qmd`, and `questions/ex-prob-unit-square-max.qmd`, including their worked answers.

## Sources opened and facts used

1. Andrey Kolmogorov, [*Foundations of the Theory of Probability*, English translation of the 1933 book](https://www.stat.yale.edu/~pollard/Courses/600.spring2018/Handouts/Foundations1933.pdf), Chapter I §1–2. Read the events-as-subsets axioms, the finite construction, and the two-coin example. Existing bibliography key `kolmogorov1933_slln` identifies the 1933 original; the opened copy is the 1956 English edition.
2. Rick Durrett, [*Probability: Theory and Examples*, 5th ed.](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf), Chapter 1 §1.1, pp. 1–3, and Chapter 2 §2.1. Read the probability-space definition, Theorem 1.1.1 and its proof of monotonicity and subadditivity, Example 1.1.2 on finite spaces, and the treatment of independent variables. Existing key `durrett2019`.
3. MIT 18.05, [*Probability: Terminology and Examples* (Spring 2022)](https://openlearninglibrary.mit.edu/asset-v1%3AMITx%2B18.05r_10%2B2022_Summer%2Btype%40asset%2Bblock/pdf_mit18_05_s22_class2-prep.pdf), §3. Checked complement, disjoint sum, and inclusion–exclusion against its statement and explanation.

## Verification and decisions

- The hand-specified lead now says “an event,” rather than “the event.”
- The article distinguishes a member of a sigma-algebra from an arbitrary subset of an uncountable space. It keeps the elementary finite-space wording as a special case.
- One collapsed Proof box establishes complement and monotonicity, finite inclusion–exclusion, both De Morgan identities, and the countable union bound. It uses only the probability axioms stated in the new Definition.
- The fair-die worked example and challenge were checked with exact fractions; `checks/event.py` also enumerates all sixteen four-engine states and verifies the original probability $0.9801$.
- The aircraft example, definition, property argument, and twelve question links remain. No figure or example was removed. The researched “Check yourself” link list was removed because the question links appear in the generated list.
- Citations to unopened Feller, Billingsley, and Grimmett–Stirzaker were replaced in the researched prose, extracted definition and properties, and article reference mapping with located Kolmogorov and Durrett citations. The research history disclaimer was removed.
