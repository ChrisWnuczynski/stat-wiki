# Inverse-Gamma distribution

Type: Distribution. Rank 38.

## Material checked

- The frozen baseline has 2,235 body words and two figure instances. The generated page contained the density and moments in its infobox, the mode result, three linked propositions, two worked questions and their hidden answers, a mean–mode calculation, and 19 distinct question links.
- Read the inverse-Gamma and normal-variance portions of `sources/book/chapters/bayes-03-normal-models.qmd`; the regression prior and marginal variance derivations in `sources/book/chapters/bayes-09-linear-regression.qmd`; both worked questions in `sources/prep/chapters/ian.qmd` and `ian-answers.qmd`; and the existing Normal distribution and Full conditional distribution articles and research notes. The local McCullagh–Nelder PDF is unavailable and is not relevant to this distribution page.

## Sources opened and used

1. Howard Raiffa and Robert Schlaifer, [*Applied Statistical Decision Theory*](https://www.wiley.com/en-us/applied-statistical-decision-theory-p-9780471383499), 1961. Opened the scanned book at Chapter 11 §11.1.3, pp. 290–291 for gamma precision and the normal variance update, and Chapter 13 §13.5, pp. 342–344 for normal regression with unknown precision and marginal versus conditional laws. Existing key `raiffa_schlaifer1961`.
2. Stan Development Team, [*Stan Functions Reference*, “Positive Continuous Distributions”](https://mc-stan.org/docs/functions-reference/positive_continuous_distributions.html#inverse-gamma-distribution), current online edition. Opened “Gamma distribution,” “Inverse gamma Distribution,” and “Scaled inverse chi-square distribution” for parameter conventions and densities. Existing key `stan_functions2026`.
3. SciPy community, [*SciPy Manual*, `scipy.stats.invgamma`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.invgamma.html). Opened Notes and Examples for the shape/scale software convention, scaled inverse-chi-squared equivalence, and random generation. New key `scipy_invgamma2026`.
4. Andrew Gelman, [“Prior distributions for variance parameters in hierarchical models”](https://sites.stat.columbia.edu/gelman/bayescomputation/Gelman2006.pdf), *Bayesian Analysis* **1** (2006), pp. 515–534. Opened §§3.1, 4.3, and 5.1, pp. 519–524 for conditional conjugacy, the inverse-Gamma$(\epsilon,\epsilon)$ sensitivity problem, and the eight-schools example. Existing key `gelman2006`.
5. Newcastle University [MAS2901 question bank, Question 83](https://matthewalexanderfisher.github.io/NCL-MAS2901/content/appendix/question-bank.html?chapter=4&coverage=upto). Opened the known-mean normal inverse-Gamma exercise and its worked posterior derivation as an independent cross-check. The page does not cite this because the original Raiffa–Schlaifer book supplies the claim.

The prior [Normal distribution research report](normal-distribution.md) records an earlier opening of Gelman et al., *Bayesian Data Analysis*, Ch. 2 §§2.5–2.6. Direct reopening of its 55 MB author PDF failed with the web reader's size cap and HTTP 403 in this workspace. The new inverse-Gamma text instead cites the opened sources above.

## Changes and checks

- Added motivation, reciprocal-precision intuition, explicit shape/scale convention, moment existence and scaling properties, posterior inference, generation, a numerical example with hidden challenge answer, misconceptions, limits, connections, and sourced history. Every new factual paragraph names a source location.
- One collapsed Proof box covers density normalisation, all stated moments, mode, scale transformation, known-mean conjugacy, joint normal–inverse-Gamma regression conjugacy, and the marginal variance posterior under a full-rank regression design. The older one-result mode proof is incorporated in this box. The proof-todo generator now recognises a reviewed full Properties proof across linked distribution results; the three inverse-Gamma property todo items are removed. Its same logic removes the previously proved Normal distribution property entries. No new proofs-todo item is needed.
- Corrected the inverse-Gamma second parameter from “rate” to “scale” in the normal-model chapter, related preparation question and answer, and regression chapter. The reciprocal gamma parameter remains a rate. The shared chapter edits were checked on their dependent normal-variance, regression, and question pages after regeneration. Replaced unsupported or unlocated citations attached to the inverse-Gamma page with located Raiffa–Schlaifer, Stan, and Gelman passages. The reciprocal-gamma relationship uses an opened Stan passage.
- The distribution template gained optional researched section slots and suppresses a short built-in mode Proof box when the page supplies a full reviewed Properties proof. Other researched distributions keep their content and preservation counts. The reciprocal relationship citation can now be overridden from this distribution's input record without editing the shared relationship file.
- Preserved both plots, all infobox formulas and values, the original two worked questions with hidden answers, the mean–mode calculation, all three property links, and all 19 question links. No factual example, figure, or question was removed; the duplicate mode derivation was consolidated into the full proof.
- `checks/inverse-gamma-distribution.py` asserts every printed numerical value in the new and original examples against exact fractions, the original plots and question links, and the single Proof box.

## Verification

Generated article: 5,567 body words versus 2,235 before, two figures versus two before, one collapsed Proof box, and 19 distinct question-bank links. The “Check yourself” section embeds two bank questions with hidden answers. All page checks, 67 Python tests, offline verification of 426 bibliography entries, and link checks pass. The full HTML render was unavailable because Quarto is not installed in this workspace; the generator used the Pandoc shim for its conversion step.
