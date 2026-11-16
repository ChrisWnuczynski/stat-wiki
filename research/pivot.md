# Pivot

Type: Concept/definition. Rank 60.

## Material checked

- **Checked:** Frozen baseline 618 body words and no figures. The inherited page has four named pivot properties, two answered question examples, an infobox and three question links. All are retained.
- **Checked:** Siegrist §8.1 gives the pivot definition, coverage by inversion, transformations, and different tail choices. His §6.08 proves one- and two-sample normal-sample Student laws and the variance-ratio F law. Geyer's University of Minnesota §4.4.2 explicitly distinguishes exact, asymptotic and approximate pivots, and notes that the pivot function contains the target parameter. Fox Ch. 6 §6.1.3 was already read and logged in `research/confidence-interval.md` for the slope t property. Neyman's 1937 original was read and logged there for confidence construction. Student's 1908 original was read for the t reference law.
- **Checked by code:** SciPy recomputed the $t_{15}$ and $t_8$ quantiles, both worked interval endpoints, the normal-coverage and $t^2$/$F$ bank-question values. `checks/pivot.py` verifies every printed numeric result in the added prose and checks generated practice.
- **Assumed:** Exact Student results require independent normal observations; pooled two-sample t also assumes a common variance. The slope result assumes fixed nonconstant predictors and independent normal errors.
- **Disputed:** The inherited lead called a pivot a statistic, which is false for the usual mean t pivot. The generator lead now describes it as a data-and-parameter quantity. The shared source paragraph also had the inaccurate claim that the pivot “must not depend on unknown parameters”; it now correctly refers to the pivot's distribution. These source changes affect the pivot article and confidence-interval chapter.

## Sources opened and used

1. Kyle Siegrist, [*Introduction to Set Estimation*](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/08:_Set_Estimation/8.01:_Introduction_to_Set_Estimation), §8.1 “Pivot Variables” (2022), new key `siegrist2022_set_estimation`.
2. Kyle Siegrist, [*Special Properties of Normal Samples*](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.08:_Special_Properties_of_Normal_Samples), §6.08 (2022), existing key `siegrist2022_normals`.
3. Charles J. Geyer, [*Stat 5421 Lecture Notes*](https://www.stat.umn.edu/geyer/f22/5421/notes/ch9.html), §4.4.2 (2023), new key `geyer2023_pivots`.
4. Jerzy Neyman, [*Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability*](https://wwwusers.ts.infn.it/~milotti/Didattica/StatisticaAvanzata/Neyman_1937.pdf), *Philosophical Transactions A* **236** (1937), pp. 346–350. Previously read and logged in `research/confidence-interval.md`, existing key `neyman1937`.
5. John Fox, [*Applied Regression Analysis and Generalized Linear Models*](https://www.sagepub.com/shop/buy-a-book/applied-regression-analysis-and-generalized-linear-models-3-237254), Ch. 6 §6.1.3, pp. 111–112. Previously read and logged in `research/confidence-interval.md`, existing key `fox2016_regression`.
6. Student, [*The Probable Error of a Mean*](https://doi.org/10.2307/2331554), *Biometrika* **6** (1908), pp. 1–4; existing key `student1908`.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

The generated body has 2,455 words and no figures. Added motivating and worked examples, exact interval inversion, one collapsed proof of inherited pivot laws, hidden-answer practice, distinct wrong readings and concrete model failures, plus two answered bank questions on normal coverage and $t^2$/$F$. Verification: the generator built 718 articles and 557 questions; all 67 Python tests pass; offline bibliography verification covers 447 entries; `git diff --check` passes. The dependent coverage article and parent confidence-interval chapter rebuild and pass link checks. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator uses the system Pandoc shim.
