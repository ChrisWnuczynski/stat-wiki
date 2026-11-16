# Multivariate normal distribution

Type: Distribution. Rank 39.

## Material checked

- Frozen baseline: 1,123 body words and three figures. The generated page contained two density/CDF plots, a correlation figure, two definition blocks, the affine-image result, a correlated-sum example, and ten question-bank links.
- Read the multivariate-normal definitions and conditional-normal derivations in `sources/stat2003/chapters/prob-05-transforms-and-limits.qmd` and `sources/stat3006/chapters/sl-01-multivariate-normal.qmd`, the two linked answered exercises, and the existing distribution record. The inherited definition cited several books and historical originals without located supporting passages.

## Sources opened and used

1. Korbinian Strimmer, [*Multivariate Statistics and Machine Learning*](https://strimmerlab.github.io/publications/lecture-notes/MATH38161/), University of Manchester online notes, 2025. Opened Chapter 1 §§1.1 and 1.3 for vector data, covariance, the multivariate normal density, ellipsoidal contours and entropy; Chapter 3 §3.1 and Example 3.9 for affine transformation, whitening and normal simulation. Existing bibliography key `strimmer2025_mva` links to the author's notes.
2. He Wang, [*Foundations of Probability and Statistical Theory*](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/), author-hosted online book, 2025. Opened Chapter 6 Extra, Theorems 24, 26 and 31, Example 32, and the surrounding multivariate-normal geometry for marginals, conditioning, affine images and characteristic functions. Existing key `wang2025_foundations` links to the author's site.
3. Stephen M. Stigler, [“Darwin, Galton and the Statistical Enlightenment”](https://academic.oup.com/jrsssa/article-abstract/173/3/469/7077679), *Journal of the Royal Statistical Society: Series A* **173** (2010), pp. 469–482. Opened the official publisher summary on p. 469 for the narrow statement that Galton's 1885 address introduced multivariate analysis. New key `stigler2010_galton_multivariate`. The article does not attribute the modern density to Galton.
4. Korbinian Strimmer, [*Probability and Distribution Refresher*](https://strimmerlab.github.io/publications/lecture-notes/probability-distribution-refresher/probability-distribution-refresher-a4.pdf), University of Manchester author-hosted notes, 1 February 2026. Opened Chapter 6 §6.4, pp. 69–72 for the Wishart construction as a sum of normal outer products. New key `strimmer2026_prob_refresher` replaces an unlocated Anderson citation in the shared Normal–Wishart relationship.

No new bibliography link points to an unauthorised copy.

## Changes and checks

- Added motivation, geometric intuition, the positive-definite versus singular distinction, affine and conditional laws, Mahalanobis distance, inference, simulation, a numerical worked example, a hidden “Your turn” answer, misconceptions, limits, connections and narrowly sourced history. The full collapsed proof covers density normalisation, affine closure, marginals and independence, the conditional formula, the distance distribution, entropy and contours.
- Replaced the unexamined definition citations in the shared probability chapter and added a located citation to the shared multivariate-normal chapter definition. The distribution record now gives the mode, entropy, moment-generating and characteristic functions, with a located affine theorem citation. The correlated-sum example remains. The shared Normal–Wishart relationship now has a located author-hosted source. The citation-preservation test records replacement of unexamined keys by the opened Strimmer, Wang and Stigler passages.
- Kept all three figure instances, both original definition blocks, the affine-image property and all ten question links. The removed affine-property proof-todo entry is covered by the reviewed full proof. Added two answered bank questions to the collapsed “Check yourself” section.
- `checks/multivariate-normal-distribution.py` checks every printed numerical value in the new examples against exact fractions, along with the proof, figures, question links and source keys.

## Verification

The generator completed 718 articles and 557 questions. The generated page has 3,996 body words versus 1,123 before, three figures versus three before, one collapsed proof, ten distinct question links, and two embedded self-checks with hidden answers. The numerical page check, 67 Python tests, offline verification of 428 bibliography entries, and overview link check pass. A full HTML render is unavailable because Quarto is not installed in this workspace; the generator uses the Pandoc shim for its conversion step.
