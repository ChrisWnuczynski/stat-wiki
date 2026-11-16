# Poisson regression

Type: Concept. Rank 228. Tier: full.

## Material checked

- **Checked:** Baseline 592 words and no figures. The source note on the log link, offsets and overdispersion stays. The added wards use counts $4$ and $9$ over $2$ and $3$ years.
- **Checked:** R `glm` manual: `offset` argument; Poisson and binomial dispersion fixed at one; prior weights are not the usual Poisson exposure.
- **Checked by code:** rates $2$ and $3$, $\log 2\approx 0.6931$, $\log(1.5)\approx 0.4055$, pooled rate $2.6$, means $5.2$ and $7.8$, Pearson $6/13\approx 0.4615$, no-offset Pearson $25/13\approx 1.9231$, $6.5/3\approx 2.1667$, count ratio $2.25$.
- **Assumed:** Independent Poisson counts. A dispersion factor free of $\beta$ drops out of the score; that algebra is in the limits section as a consequence of the score, not as a fitted quasi-Poisson model.
- **Disputed:** Nothing.

## Sources opened and used

1. R `glm` manual. Existing key `rstats_glm2026`.

## Skipped

McCullagh and Nelder was not opened.
