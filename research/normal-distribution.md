# Normal distribution

Type: Distribution.

## Material checked

- The generated article began with 3,035 body words, four figure instances, two infobox plots, the shared density comparison, the IQ example, posterior calculations and their worked answers, and fourteen distinct practice-question links.
- `distributions.json`, `distribution_relationships.json`, the normal definition in `sources/stat2003/chapters/prob-02-random-variables.qmd`, the normal-sample theorem in `sources/stat2004/chapters/inf-01-statistical-inference.qmd`, and normal conjugacy in `sources/book/chapters/bayes-03-normal-models.qmd`.

## Sources opened and used

1. Kyle Siegrist, [“The Normal Distribution,” §5.6](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/05:_Special_Distributions/5.06:_The_Normal_Distribution). Read the standard and general normal sections, including the density, CDF, moments, MGF, affine and independent-sum properties. Key `siegrist2022_normal_distribution`, added to the bibliography.
2. Siegrist, [“The Binomial Distribution,” §11.2](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/11:_Bernoulli_Trials/11.02:_The_Binomial_Distribution), “The Normal Approximation”; and [“The Lognormal Distribution,” §5.12](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/05:_Special_Distributions/5.12:_The_Lognormal_Distribution), “Definition.” Keys `siegrist2022_binomial_distribution` and `siegrist2022_lognormal_distribution`, both added.
3. Siegrist, [“Special Properties of Normal Samples,” §6.08](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.08:_Special_Properties_of_Normal_Samples). Read its normal-mean, sample-variance and independence proofs during the confidence-interval pass. Key `siegrist2022_normals`.
4. Andrew Gelman et al., [*Bayesian Data Analysis*, third edition](https://sites.stat.columbia.edu/gelman/book/BDA3.pdf), Chapter 2 §§2.5–2.6, pp. 39–43, and Chapter 3 §3.5, pp. 70–72. Read normal-mean, inverse-gamma, and multivariate-normal passages. Key `gelman_bda2013`.
5. Howard Raiffa and Robert Schlaifer, [*Applied Statistical Decision Theory*](https://gwern.net/doc/statistics/decision/1961-raiffa-appliedstatisticaldecisiontheory.pdf), Chapter 3 §3.3.4, pp. 64–65, and Chapter 11 §11.1.3, pp. 290–291. Read the normal-prior precision update and gamma prior on normal precision. Key `raiffa_schlaifer1961`.
6. Peter Hoff, [“Bayes Estimators”](https://www2.stat.duke.edu/~pdh10/Teaching/581/LectureNotes/Static/bayes.pdf), §1, pp. 1–2, for the normal-mean weighted shrinkage calculation. Key `hoff2013_bayes_estimators`.
7. George Box and Mervin Muller, [“A Note on the Generation of Random Normal Deviates”](https://www.scispace.com/pdf/a-note-on-the-generation-of-random-normal-deviates-1xek1iybaa.pdf), *Annals of Mathematical Statistics* **29** (1958), pp. 610–611. Read the scanned article's transformation and stated computational motivation. Key `box_muller1958`.

The de Moivre and Gauss original passages were inaccessible. Their historical attribution is omitted and recorded in `research/todo.md`; the History section uses the opened Box–Muller paper and modern normal-model account. The inherited Feller, Forbes, Casella–Berger, Anderson, Box–Tiao, and Gelfand–Smith citations attached to this page's claims were replaced or removed after checking which opened texts actually supported the claims.

## Changes and checks

- Added precise notation, distinctions between a normal observation and a normal approximation for an average, interpretation of the density and its spread, and one collapsed proof covering moments, transforms, entropy, Fisher information, the normal-sample theorem, conjugacy, and Box–Muller sampling. The prior affine proof is incorporated in that box.
- Corrected the relationship to the lognormal family in both directions, with matching parameters; replaced unsupported relationship and historical citations with located citations. The normal-sample theorem now defines its sample variance on first use and requires at least two observations.
- The distribution template now reads `research/content/<slug>.md` because it previously had no page-specific research slot. It also omits an empty built-in proof when the researched page supplies the single collapsed proof.
- `checks/normal-distribution.py` recomputes printed standard-normal probabilities and checks that the generated article cites only sources opened for this pass. The comparison figure, infobox plots and values, copied definitions, worked answers, and question links remain.
- The generated page has 4,538 body words, four figure instances, one Proof box, and fourteen distinct practice-question links. The build produced 718 articles and 557 question pages; 67 Python tests, the printed-value script, and offline verification of 408 bibliography records pass.
