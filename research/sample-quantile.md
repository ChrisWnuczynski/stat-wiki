# Sample quantile research notes

- **Checked:** Hyndman and Fan (1996), *Sample Quantiles in Statistical Packages*, original full five-page PDF linked from the author's page https://robjhyndman.com/papers/sample_quantiles.pdf ; read pp. 361–365, including definitions and comparisons. Author metadata and errata at https://fpp.robjhyndman.com/publications/quantiles/ . Pending key `hyndman_fan1996`.
- **Checked:** R Core `stats::quantile` documentation https://stat.ethz.ch/R-manual/R-devel/library/stats/html/quantile.html , Description, Details and Types 1–9, including default type 7 and type 1 empirical inverse. Pending key `r_stats_quantile`.
- **Checked:** Dodge (2008), authorized extraction, printed pp. 437, 439–440, quantile, quartile, and Q–Q plot entries. It describes another quartile interpolation convention and warns about very small samples.
- **Checked by code:** Type-1 versus type-7 worked values, patient example reported values, normal benchmark, Your turn, transformation counterexample, and proposed bank questions in `checks/sample-quantile.py`.
- **Assumed:** Observations have a meaningful numeric order; population interpretation additionally assumes a sample from a population.
- **Disputed:** “A fraction p is at or below the p-quantile” is only a rough gloss for finite samples, especially with interpolation and ties. The page distinguishes empirical inverse, median-of-halves and R type 7.
