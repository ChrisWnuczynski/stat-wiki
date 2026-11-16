# Confidence interval

Type: Concept/definition.

## Material read before editing

- `articles/confidence-interval.qmd`: original coverage definition; four pivot statements; one coverage figure; four worked examples; interval laboratory link; 21 practice questions. The article had 976 body words by the progress-table method and one figure.
- `sources/stat2004/chapters/inf-03-confidence-intervals.qmd`: coverage definition, one- and two-sample pivots, variance-ratio pivot, the tablet and household examples, and the source interval explanation.
- `sources/stat2004/chapters/inf-06-regression.qmd`: fixed-design slope pivot and its normal-error derivation.

## Sources opened and facts used

1. Jerzy Neyman, [“Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability”](https://wwwusers.ts.infn.it/~milotti/Didattica/StatisticaAvanzata/Neyman_1937.pdf), *Philosophical Transactions of the Royal Society A* **236** (1937), pp. 333–380. Read pp. 333–334 and 346–350 for the practical problem, fixed parameter, random limits, and confidence construction; pp. 370–375 for precision and one-sided limits; pp. 378–379 for the summary. Key `neyman1937`.
2. NIST/SEMATECH, [“Confidence Limits for the Mean,” §1.3.5.2](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm). Read its coverage interpretation, one-sample $t$ interval, width factors, test connection, and numerical example. Key `nist_mean_limits2002`.
3. Kyle Siegrist, [“Special Properties of Normal Samples,” §6.08](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.08:_Special_Properties_of_Normal_Samples). Read “The One Sample Model” and “The Two Sample Model,” including the $t$, pooled two-sample $t$, and sample-variance $F$ distributions and their independence arguments. Key `siegrist2022_normals`.
4. John Fox, [*Applied Regression Analysis and Generalized Linear Models*, Chapter 6 §6.1.3](https://www.sagepub.com/shop/buy-a-book/applied-regression-analysis-and-generalized-linear-models-3-237254), pp. 111–112. Read the slope standard error, $t_{n-2}$ interval, and test relation; the preceding §6.1.2 was opened during the Unbiased estimator pass. Key `fox2016_regression`.
5. Student, [“The Probable Error of a Mean”](https://en.wikisource.org/wiki/The_Probable_Error_of_a_Mean), *Biometrika* **6** (1908), pp. 1–25; the introduction and pp. 1–4 were opened during the Standard error pass. Key `student1908`.
6. NIST/SEMATECH, [“Confidence interval approach,” §7.2.3.1](https://www.itl.nist.gov/div898/handbook/prc/section2/prc231.htm), for the normal-sample standard-deviation interval. The chapter's worked tablet example was checked against the displayed chi-squared quantiles. This page is recorded for verification; no new bibliography key was needed.

The Casella–Berger, Davison, Fisher 1925, and Snedecor citations attached to inherited pivot statements were replaced with the opened sources above. The unopened books were not cited in the new prose.

## Changes and checks

- Added a plain-language introduction, coverage interpretation, precise symbol definitions, distinctions between exact and conservative coverage, practical assumptions, relationships, a numerical repetition example, and two historical paragraphs grounded in Neyman.
- One collapsed Proof box proves the exact one-sample, pooled two-sample, $F$ variance-ratio, and regression-slope pivot claims as stated, then derives their confidence or test interpretation.
- The original definition, all four pivot statements, the `inf-coverage.png` figure, four worked examples and answers, laboratory link, and 21 question links remain.
- `checks/confidence-interval.py` recomputes the new repetition example and numerical results printed in the inherited examples and answer.
- Corrected the household standard error from $178/\sqrt{51}=24.93$ to $24.92$ and stated the normal-sampling assumption precisely. The page now has 2,292 body words, one figure, one Proof box, 22 distinct question links, and 41 inline citation uses. The original question-link and figure counts do not fall. Four dependent pivot pages received located citations in the shared source and explanation data so the site-wide three-citation test still passes.
- Build: 718 articles and 557 question pages. `checks/confidence-interval.py`, 67 Python tests, and offline verification of 405 bibliography records pass. The proof todo entries for the four standalone pivot articles remain for their ranked depth passes; the confidence-interval page proves those same results in one collapsed box.
