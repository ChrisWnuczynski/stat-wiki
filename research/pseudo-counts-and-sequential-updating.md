# Pseudo-counts and sequential updating

Type: Concept/method. Rank 174.

## Material checked

- **Checked:** Frozen baseline: 376 body words, zero figures, two pseudo-count formulas, Beta(5,5) warning, sequential-coherence proposition and four original question links. The new source retains all.
- **Checked:** Diaconis and Ylvisaker (1979), full paper, §1 pp. 269–270. It displays the Beta density, Beta-Binomial posterior shape additions and linear posterior expectation, and distinguishes conjugate closure from linearity. This supports the sequential update and weighted-mean interpretation.
- **Checked:** Dodge (2008) p. 40 gives Beta density, mean and the uniform Beta(1,1) case; p. 32 dates Bayes's posthumous essay and Price's role. The printed pages were read via the indexed extracted text.
- **Checked by code:** Two-batch shape additions, posterior mean and mode, all displayed decimal approximations and exact fractions in `checks/pseudo-counts-and-sequential-updating.py`.
- **Assumed:** Trials are conditionally independent with one stable success probability. Pseudo-counts are a summary-specific analogy, not necessarily physical prior observations.
- **Disputed:** A claim that pseudo-counts have a unique count would conflate posterior mean and mode. The two formulas already on the page show different conventions; the new proof explains their origin. Gelman's full author-hosted BDA PDF was identified but exceeded the web reader's file size limit, so no new claim relies on it.

## Sources opened and used

1. Diaconis and Ylvisaker, “Conjugate Priors for Exponential Families,” *Annals of Statistics* **7** (1979), §1 pp. 269–270, full paper in a Columbia course archive at `https://www.cs.columbia.edu/~blei/fogm/2020F/readings/DiaconisYlvisaker1979.pdf`; existing key `diaconis_ylvisaker1979`.
2. Dodge, *The Concise Encyclopedia of Statistics* (2008), Beta Distribution p. 40 and Bayes p. 32; existing key `dodge2008`.

## Changes and checks

One collapsed proof covers conjugate update, batch-order invariance, weighted posterior mean and interior mode. Pending shared checks select two already answered, substantively related question-bank items. Full gate results recorded in the commit run.
