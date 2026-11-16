# Generalised estimating equations — research notes (rank 206)

## Sources read

- Checked: Liang and Zeger (1986), complete original *Biometrika* paper hosted by University of Sydney teaching site, https://www.maths.usyd.edu.au/u/jchan/GLM/Liang%26Zeger1986GEE.pdf, opened 2026-11-16. Section 1 pp. 13–14 explains marginal rather than conditional aims; §2 pp. 14–15 gives independence equation; §3.1 pp. 15–16 gives working covariance, GEE equation 6, asymptotic result and sandwich. §5 pp. 19–20 discusses efficiency; §6 limitations.
- Checked: original chapter sources/book/chapters/09-marginal-models.qmd and generated baseline article, preserving the source equation, citations and four linked exercises. The chapter's warp-breaks example has only two factories, so the robust standard error there is illustrative, not a reliable large-cluster estimate.
- Checked with code: Bernoulli intercept-only GEE example with 30 independent two-response clusters; working-independence and cluster-sandwich standard errors.
- Assumed: clusters independent, finite moments and regular smooth mean model; no informative loss of repeated measurements, for the cited consistency result. Example's thirty clusters are a teaching calculation, not evidence of good finite-sample coverage.
- Disputed: changing working correlation does not preserve finite-sample coefficient estimates exactly; the theorem concerns consistency for the same marginal target under conditions. Sandwich standard errors are not robust to an incorrect mean model or dependence between clusters.
- Dodge: source present; index has no dedicated GEE entry.

## Preservation

Baseline: 250 words, zero figures, four question links. Its definition and original source citations remain.
