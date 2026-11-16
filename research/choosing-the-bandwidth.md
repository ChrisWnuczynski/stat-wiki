# Choosing the bandwidth — research record

## Sources opened

- Wasserman, *Non-parametric Density Estimation*, full author-hosted CMU lecture 26, §§1–2, at `https://www.stat.cmu.edu/~larry/=stat705/Lecture26.pdf`, read kernel estimator, bias/variance derivation, IMSE and dimensional scaling.
- Hansen and Larsson, *Computational Statistics with R*, full author-hosted Ch. 2 §§2.1, 2.2, 2.4 at `https://cswr.nrhstat.org/density.html`, read bandwidth effects, plug-in reference, and leave-one-out likelihood/least-squares cross-validation.
- Silverman, *Density Estimation for Statistics and Data Analysis* (1986), full historical discussion §2.11 reproduced by Caltech/IPAC NED at `https://ned.ipac.caltech.edu/level5/March02/Silverman/Silver2_11.html`; opened for Rosenblatt/Parzen history, not numerical rule.
- R `stats` full official bandwidth-selector documentation, `https://stat.ethz.ch/R-manual/R-devel/RHOME/library/stats/html/bandwidth.html`, read implementation details for `bw.nrd0`, `bw.ucv`, `bw.SJ`.
- Dodge authorized local index and full text searched. No relevant bandwidth/kernel-density entry found. Baseline 427 words, zero figures, all original MISE/matrix discussion and three linked questions retained.

## Claim ledger

- **Checked:** A scalar bandwidth changes smoothing; small $h$ gives high variance, large $h$ high bias, under smoothness conditions (Wasserman §§1–2; Hansen–Larsson Ch. 2 §2.2).
- **Checked:** Univariate smooth-kernel approximate MISE has form $Ah^4+B/(nh)$, optimized at $(B/(4An))^{1/5}$ (Wasserman §2, pp. 2–3). This is asymptotic and assumes sufficient derivatives; it is not a universal finite-sample formula.
- **Checked:** Leave-one-out log-likelihood evaluates each observation against a density fit without that observation, while unbiased CV targets squared-error risk (Hansen–Larsson Ch. 2 §2.4).
- **Checked:** In the course's multivariate convention $H$ is a covariance-bandwidth matrix and univariate $H=h^2$; the equivalent scale-matrix convention in Wasserman's lecture uses $H=hI$. The article keeps the course convention explicit.
- **Checked by code:** Gaussian leave-one-out densities/log scores for $x=(0,1,2)$, $h=0.5,1,2$ and scaled Your turn are recomputed in `checks/choosing-the-bandwidth.py`.
- **Checked:** Silverman §2.11 identifies Rosenblatt 1956 as early published kernel-density work; the modern R docs distinguish normal-reference, CV and Sheather–Jones software selectors.
- **Assumed:** Synthetic three-point sample is illustrative; its selected bandwidth is only the best of three candidates under one CV criterion, not a population-optimal bandwidth.
- **Assumed:** The author-hosted Wasserman lecture PDF has no visible publication date; its search index dates it to approximately 2020. The bibliography year is provisional, while the lecture text and locators were read directly.
- **Disputed/limited:** Cross-validation may be unstable for very small samples or unsuitable near support boundaries. A density after dimension reduction targets a projected distribution, not the full joint law.
