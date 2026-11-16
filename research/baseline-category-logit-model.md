# Baseline-category logit model

Type: Concept/definition. Rank 221. Tier: full.

## Material checked

- **Checked:** Baseline 712 words and no figures. The source definition with categories $0,\ldots,K-1$ and the addiction-survey coefficients stay on the generated page. The added example uses scores $0$, $0.5$ and $1$, not those survey coefficients.
- **Checked:** R `nnet::multinom` documentation, Details: a log-linear model is fitted with coefficients zero for the first class; the response may be a factor or a matrix of class counts.
- **Checked by code:** $e^{0.5}=1.64872127$, $e^{1}=2.71828183$, denominator $5.36700310$, probabilities $0.18632372$, $0.30719589$, $0.50648039$. Printed to four decimals as $1.6487$, $2.7183$, $5.3670$, $0.1863$, $0.3072$, $0.5065$, which sum to $1.0000$. The practice scores $0$ and $\log 3$ give probabilities $0.2$, $0.2$, $0.6$.
- **Assumed:** The linear predictors stay finite, so every probability is strictly between $0$ and $1$.
- **Disputed:** Nothing. Adding a constant to every score does not change the probabilities; the zero constraint chooses a representative and is not a substantive restriction on the probabilities.

## Sources opened and used

1. R Core Team, `multinom` in the nnet manual, `https://stat.ethz.ch/R-manual/R-devel/library/nnet/html/multinom.html`. New pending key `r_nnet_multinom2026`.

Agresti, McCullagh and Nelder, and Tutz were not opened. The probability map is derived from the log-odds definition. The manual is cited for the software baseline, which sets the first class's coefficients to zero.

## Skipped

The printed addiction coefficients in the source chapter were not refitted. The four-decimal probabilities are rounded from the exact exponentials; the check uses the exact values and the printed rounding.
