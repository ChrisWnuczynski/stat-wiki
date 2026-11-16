# Posterior point summaries

Type: Definition/concept. Rank 53.

## Material checked

- Frozen baseline: 711 body words, zero figures. Read the generated definition, inherited posterior-draw property and its two worked question answers. Seven further question links remain. The source is `sources/book/chapters/bayes-01-foundations.qmd` around the point-summary definition.
- **Checked:** Gelman et al., *Bayesian Data Analysis*, Ch. 2 §2.3 pp. 32–34 distinguishes posterior mean, median, mode, quantiles and intervals for a skewed posterior. Hoff, *Bayes estimators*, pp. 8–10 proves squared-error choice of the mean and identifies medians under absolute loss; p. 11 gives the Beta–Binomial update.
- **Checked by code:** for $\operatorname{Beta}(3,9)$, mean 0.25, median 0.2357855, mode 0.2 and variance 27/1872; for $\operatorname{Beta}(4,8)$, mean 1/3, median 0.3238045 and mode 0.3. The median is recomputed by numerical inversion of an integer-shape Beta CDF in `checks/posterior-point-summaries.py`.
- **Checked history:** BDA Ch. 2 §2.10 p. 56 identifies Bayes's 1763 inverse-probability problem and later development. Hoff's notes state their decision-theoretic basis in Lehmann and Casella (1998), Ch. 4. The page does not credit Bayes with the modern loss-function terminology.
- **Assumed:** worked binomial trials are conditionally independent given their success probability with a uniform prior.
- **Disputed:** an unqualified “MAP is the most probable value” is misleading for a continuous parameter because a point has probability zero and density modes depend on parameterisation. The article states MAP as a density maximum on a specified scale and demonstrates that dependence.

## Sources opened and used

1. Gelman et al., [*Bayesian Data Analysis*, 3rd ed.](https://sites.stat.columbia.edu/gelman/book/BDA3.pdf), Ch. 2 §§2.3 and 2.10, pp. 32–34, 56. Read the author-hosted noncommercial edition. Existing key `gelman_bda2013`.
2. Peter D. Hoff, [*Bayes estimators*](https://www2.stat.duke.edu/~pdh10/Teaching/581/LectureNotes/Static/bayes.pdf), Duke University (2013), pp. 8–11. Opened the author-hosted notes; checked posterior-risk minimisation, loss functions and the Beta update. Existing key `hoff2013_bayes_estimators`.
3. The inherited posterior-draw property cites Geyer (1992) and Wang (2025). Those works were opened for the earlier Posterior mean pass, as recorded in `research/posterior-mean.md`; their supported citations and formulas are retained.

## Changes and checks

- Add a specific contrast among mean, median and mode, one collapsed proof of loss choices and transformation behavior, worked and practice Beta calculations, concrete failure cases, and two answered bank questions. Preserve the existing definition, property, worked questions, infobox and seven question links.
- The generated page grows from 711 to 3,490 body words and retains zero figures. No shared source text was edited, so no dependent article changed. The one collapsed proof covers squared and absolute loss, affine means, monotone medians, noninvariance of MAP under log odds, the Beta update and the heavy-tail moment boundary. The inherited posterior-draw result has its existing entry under `posterior-summaries-from-draws` in `proofs-todo.json`; there is no new unproved claim on this page.
- Verification: `checks/posterior-point-summaries.py` passes the displayed Beta numbers, loss comparison, MAP transformation, hidden practice and inherited draw indices; the generator builds 718 articles and 557 questions; all 67 Python tests pass; offline verification covers 441 bibliography entries; and `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator used the system Pandoc shim.
