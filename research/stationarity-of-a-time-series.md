# Stationarity of a time series — research record

## Sources opened

- Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed., full author-hosted online textbook, Ch. 9 §9.1 at `https://otexts.com/fpp3/arima.html#stationarity-and-differencing`; read stationarity, plots/ACF and differencing sections.
- Meinshausen, *Time Series Analysis* ETH Zurich course notes (2022), full university-hosted text, §§1.1–1.6, especially §1.3 pp. 5–6 definitions/examples and §1.4 p. 7 covariance properties.
- Mikusheva and Schrimpf, MIT OpenCourseWare *Introduction to VARs: Wold Decomposition Theorem*, corrected 2012 lecture 10, full official MIT-hosted PDF at `https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/c513d2c0f8b1949efacd64e27df0fe07_MIT14_384F13_lec10.pdf`; opened the stated weak-stationarity representation and scalar proof. Added as support for the preserved Wold box after removing unread original-source citations.
- Dodge (2008), authorized local "Time Series" entry, printed p. 536, including history of trend/seasonal decomposition and Persons's 1919 proposal.
- Generated baseline page, 662 words, zero figures; Wold box, strict/weak definitions, variogram equation, and question links preserved.

## Claim ledger

- **Checked:** Strict stationarity holds for all finite-dimensional laws under shifts; weak stationarity requires finite variance, constant mean and lag-only covariance (Meinshausen §1.3). Strict with finite second moments implies weak; for Gaussian processes weak implies strict (same source).
- **Checked:** Trend and fixed seasonal pattern violate stationarity, while aperiodic cycles can coexist with it; differencing may remove changing level (Hyndman–Athanasopoulos Ch. 9 §9.1).
- **Checked:** White noise and a two-sided MA(1) are weakly stationary; a random walk has variance increasing with time (Meinshausen §1.3 pp. 6–7).
- **Checked by code:** New MA(1) numeric values, variogram identity, random-walk variance and changing-law counterexample are verified in `checks/stationarity-of-a-time-series.py`.
- **Checked:** $|\gamma(h)|\le\gamma(0)$ and positive semidefiniteness follow from Cauchy–Schwarz and variance of a linear combination (Meinshausen §1.4).
- **Assumed:** Synthetic MA(1) innovations are independent with specified moments and extend over all integer times; the daily-sales examples are illustrative.
- **Disputed/limited:** A flat-looking plot or quick ACF decay does not prove stationarity; finite observations are compatible with multiple mechanisms. A strict-stationary Cauchy series lacks finite variance, so strict implies weak only with finite second moments.
- **Proof debt:** The page embeds Wold decomposition from the course source. Its reviewed proof is already logged in `proofs-todo.json` under `wold-decomposition`; the new collapsed proof handles elementary covariance and strict/weak relationships but does not claim to prove Wold's decomposition.
