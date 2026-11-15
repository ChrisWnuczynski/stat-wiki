# Expectation

Type: Concept/definition.

## Existing material read

- `articles/expectation.qmd` before the edit: discrete and continuous definitions, expectation-of-a-function and tower-property statements, a discrete grouping proof, three worked examples, 29 linked questions, and no figures. Leading body: 698 words under the `PROGRESS.md` counting method.
- `sources/stat2003/chapters/prob-02-random-variables.qmd`, “Expectation and variance,” including the centre-of-mass interpretation, the function-of-a-variable theorem and its grouping proof, and linearity without independence. Compared with the generated notes page.
- `questions/ex-prob-double-six-wait.qmd` and `questions/ex-sp-spike.qmd`, including their hidden answers.

## Sources opened and facts used

1. Christiaan Huygens, [*De ratiociniis in ludo aleae*](https://math.dartmouth.edu/~doyle/docs/huygens/huygens.pdf), 1657; read the 1714 English translation, preface and Propositions I–III. These passages derive fair values of chances in games by averaging equally likely winnings and by weighting unequal numbers of chances. Used for the first history paragraph. Citation key `huygens1657`.
2. Charles M. Grinstead and J. Laurie Snell, [*Introduction to Probability*](https://math.dartmouth.edu/~prob/prob/prob.pdf), 2nd revised edition, AMS, 1997; read the freely available revised PDF, chapter 6 §6.1, especially Definition 6.1, Theorem 6.2 on linearity, and Example 6.3 on the St Petersburg game. Used for the definition, interpretation, linearity, examples, and limits. Citation key `grinstead_snell1997`.
3. Rick Durrett, [*Probability: Theory and Examples*](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf), 5th edition, 2019; read §4.1.2, especially the defining property of conditional expectation and Theorem 4.1.13 on the tower property. Used for the proof and modern definition. Citation key `durrett2019`.
4. [Wikipedia: Expected value](https://en.wikipedia.org/wiki/Expected_value), opened for cross-check only, not cited.

## Verification and decisions

- The new collapsed proof covers both copied properties: the function-of-a-variable rule in continuous as well as discrete form, and the unconditional and nested tower properties. It also proves the added linearity and indicator statements. The original discrete grouping proof remains in the body.
- The cost, die, St Petersburg, double-six, and spike calculations were checked in `checks/expectation.py` using exact rational arithmetic.
- The source chapter and existing three worked examples, definitions, citations, and question links remain. No figure or substantive text was removed. No new bibliography entry was needed because all three sources have existing keys.

## Correction pass

- Replaced unopened Bernoulli, Grimmett–Stirzaker, and Doob citations in the relevant source definitions with Grinstead–Snell chapter 6 §6.1 and Durrett §4.1.2, both read during this pass. Added locations to researched citations.
- Cited the motivating and worked examples and their hidden answer, removed a second History paragraph that repeated definitions, and checked values printed in the three inherited examples.
