# Discrete distribution

Type: Concept/definition. Rank 48.

## Material checked

- Frozen baseline: 435 body words, two figure instances. Generated page contains a die/CDF figure, a three-family mass-function figure, and answered examples for the sum and minimum of two dice. Read `sources/stat2003/chapters/prob-02-random-variables.qmd` and the generated page before editing.
- **Checked:** A discrete law concentrates probability one on a finite or countable support; the mass function is nonnegative and sums to one; interval and event probabilities sum the relevant masses. Durrett, Ch. 1 §1.2, p. 13; Grinstead–Snell, Ch. 1 §1.2, pp. 19–21.
- **Checked:** Grinstead–Snell, Ch. 1 §1.2, pp. 25–27, distinguishes equally likely elementary dice outcomes from the nonuniform law of their sum. Durrett, Ch. 1 §1.2, pp. 13–14, gives point mass and countably infinite examples.
- **Checked by exact arithmetic:** the new three-inspection and two-trial calculations, plus the inherited dice sums and minimum expectation, in `checks/discrete-distribution.py`.
- **Assumed for examples:** independence of the inspection or trial outcomes and the stated common probabilities. These are modelling assumptions, not properties of every discrete distribution.
- **Disputed:** none. The absent Dodge directory prevents a checked claim about the term's historical origin, so no such attribution is made.

## Sources opened and used

1. Charles M. Grinstead and J. Laurie Snell, [*Introduction to Probability*](https://math.dartmouth.edu/~prob/prob/prob.pdf), Ch. 1 §1.2, pp. 19–21, 25–27, and Ch. 6 §6.1. Opened the author-approved Dartmouth copy through the web reader. It is explicitly freely redistributable in its front matter.
2. Rick Durrett, [*Probability: Theory and Examples*, 5th ed.](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf), Ch. 1 §1.2, pp. 13–14. Opened the author's Duke PDF through the web reader. These passages distinguish discrete, absolutely continuous and singular laws.
3. The repository's own probability chapter named above was read for its original definition, figures, notation and examples.

## Changes and checks

- Added narrative on support, mass functions, the staircase CDF, infinite support, transformations, comparison with densities, statistical uses and concrete failure cases. One collapsed proof covers the stated identities. Added a separate numerical worked example and a hidden practice answer.
- Kept both inherited figures and both answered dice examples. Selected `ex-prob-wait-pmf` and `ex-prob-joint-table` for the generated question-bank section.
- Replaced the inherited uninspected Billingsley reference in the source definition with the two opened, located sources.

## Verification

The generator completed 718 articles and 557 question pages using the temporary Pandoc shim; Quarto itself is unavailable in this workspace, so no full HTML render was run. The generated article has 2,330 body words versus 435 before and retains both figure instances. The source-definition change also appears in the Random variable article and probability chapter; the dependent article remains above its 872-word, one-figure baseline. The page arithmetic check, 67 Python tests, offline verification of 437 bibliography entries, and `git diff --check` pass. Build-only citation timestamps in tracked lab and overview files were restored.
