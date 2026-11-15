# Unbiased estimator

Type: Concept/definition.

## Existing material read

- `articles/unbiased-estimator.qmd` before the edit: definition, sample mean and variance properties, least-squares property, three retained worked examples including the normal variance MSE comparison, five inline citations, and ten question links. Leading body: 768 words; no figures.
- `sources/stat2004/chapters/inf-02-estimation.qmd` around unbiasedness, bias–variance comparison, and the two variance estimators; the chapter's universal “no uniform winner” statement has the issue already recorded in `research/todo.md` and is not repeated here.
- `questions/ex-inf-poisson-mle.qmd`, `questions/ex-inf-poisson-umvu.qmd`, and `questions/ex-inf-shrunk-mean.qmd`.

## Sources opened and facts used

1. Fisher, [“On the Mathematical Foundations of Theoretical Statistics”](https://www.stats.org.uk/statistical-inference/Fisher1922.pdf), original 1922 paper opened earlier. Used only for the broad estimation and sampling-distribution framework, not credited with originating the present definition. Key `fisher1922`.
2. C. R. Rao, [“Information and the Accuracy Attainable in the Estimation of Statistical Parameters”](https://gwern.net/doc/statistics/1992-rao.pdf), a 1992 reprint of the 1945 paper. Read its introduction, explicit unbiasedness constraint, variance comparison, and warning that small bias may reduce error. Key `rao1945`.
3. David Blackwell, [“Conditional Expectation and Unbiased Sequential Estimation”](https://ds.dfci.harvard.edu/~gp/talks/Blackwell12.pdf), reproduced original 1947 text, especially its summary of expectation and variance under conditioning. Key `blackwell1947`.
4. NIST [“What are Variables Control Charts?”](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm), opened for the unbiased $n-1$ sample variance and biased sample standard deviation under normal sampling. The new article proves the sample-variance result and cites existing `casella_berger2002` and `wasserman2004`; no new bibliography entry was needed.
5. Existing source chapter citations to Casella and Berger (2002), Lehmann and Casella (1998), and Davison (2003), used for the definition, regression condition, and modern comparison of criteria. Full book texts were unavailable; equations are independently derived in the collapsed proof and checked by `checks/unbiased-estimator.py`.

## Verification and decisions

- Original definition, three examples and their calculations, all citations, and ten question links remain. No figures or examples were removed.
- The one collapsed proof covers sample-mean and sample-variance expectation, least-squares coefficient unbiasedness under explicit design and conditional-mean conditions, MSE decomposition, nonlinear-transformation bias, and Rao–Blackwell expectation and variance.
- The original claim that unbiased $s^2$ is preferred for exact pivots has a precise qualification: rescaling the MLE variance can form the same exact normal-model pivot, so this is a convenience rather than a unique justification.
- The history claims are limited to what the opened Fisher, Rao, and Blackwell papers actually studied; no unsupported origin for the word *unbiased* is asserted.
