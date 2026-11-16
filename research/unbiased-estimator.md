# Unbiased estimator

Type: Concept/definition.

## Existing material read

- `articles/unbiased-estimator.qmd` before the edit: definition, sample mean and variance properties, least-squares property, three retained worked examples including the normal variance MSE comparison, five inline citations, and ten question links. Leading body: 768 words; no figures.
- `sources/stat2004/chapters/inf-02-estimation.qmd` around unbiasedness, bias–variance comparison, and the two variance estimators; the chapter's universal “no uniform winner” statement has the issue already recorded in `research/todo.md` and is not repeated here.
- `questions/ex-inf-poisson-mle.qmd`, `questions/ex-inf-poisson-umvu.qmd`, and `questions/ex-inf-shrunk-mean.qmd`.

## Sources opened and facts used

1. Fisher, [“On the Mathematical Foundations of Theoretical Statistics”](https://www.stats.org.uk/statistical-inference/Fisher1922.pdf), original 1922 paper opened earlier. Used only for the broad estimation and sampling-distribution framework, not credited with originating the present definition. Key `fisher1922`.
2. C. R. Rao, [“Information and the Accuracy Attainable in the Estimation of Statistical Parameters”](https://doi.org/10.1007/978-1-4612-0919-5_16), a 1992 reprint of the 1945 paper. Read its introduction, explicit unbiasedness constraint, variance comparison, and warning that small bias may reduce error. Key `rao1945`.
3. David Blackwell, [“Conditional Expectation and Unbiased Sequential Estimation”](https://ds.dfci.harvard.edu/~gp/talks/Blackwell12.pdf), reproduced original 1947 text, especially its summary of expectation and variance under conditioning. Key `blackwell1947`.
4. Kyle Siegrist, [*Probability, Mathematical Statistics, and Stochastic Processes*, §6.5](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.05:_The_Sample_Variance), opened for the general $n-1$ sample-variance proof and standard-deviation bias. New key `siegrist2022_sample_variance`.
5. He Wang, [*Foundations of Probability and Statistical Theory*, Chapter 13](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/chapters/chapter-13-point-estimation2.html), §§15–17, opened for unbiasedness, MSE, bias–variance, sample-mean moments, and normal variance comparison. Key `wang2025_foundations`.
6. John Fox, [*Applied Regression Analysis and Generalized Linear Models*](https://www.sagepub.com/shop/buy-a-book/applied-regression-analysis-and-generalized-linear-models-3-237254), third edition, Ch. 6 §6.1.2, p. 109. Opened the fixed-design least-squares unbiasedness statement and assumptions. New key `fox2016_regression`.

Casella and Berger (2002), Lehmann and Casella (1998), Wasserman (2004), Davison (2003), and Cramér (1946) were cited in the first draft or inherited blocks without their texts being opened. The correction replaces those citations in the generated Unbiased estimator article with located sources.

## Verification and decisions

- The definition, three examples and their calculations, and ten question links remain. No figures or examples were removed.
- The one collapsed proof covers sample-mean and sample-variance expectation, least-squares coefficient unbiasedness under explicit design and conditional-mean conditions, MSE decomposition, nonlinear-transformation bias, and Rao–Blackwell expectation and variance.
- The normal-model discussion explains how rescaling the MLE variance yields the same exact pivot as unbiased $s^2$.
- The history uses the opened Fisher, Rao, and Blackwell papers to describe the development of estimation criteria.
