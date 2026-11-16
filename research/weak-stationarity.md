# Weak stationarity

Rank 197. Type: Concept. Frozen baseline: 206 body words, zero figures. The original strict-versus-weak comparison, lag covariance definition, citations and question links remain.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 536, “Time Series”, reports Persons's 1919 decomposition into trend, cyclical, seasonal and irregular components. The complete extracted page `/workspace/statwiki-sources/dodge2008/pages/pdf-0534.txt` was read. It supplies historical context for removing systematic components, not the stationary covariance theorem.
- **Checked in the repository source chapter:** `sources/book/chapters/12-time-series.qmd`, lines 19–57, defines strict/weak stationarity, the lag covariance and the AR(1)/random-walk contrast.
- **Checked by proof:** One collapsed box establishes strict-with-finite-variance implies weak, covariance symmetry and bounds, difference variance, stationary AR(1) autocovariance and a weak-not-strict construction. `checks/weak-stationarity.py` recomputes all printed AR and alternating-distribution numbers plus pending bank arithmetic.
- **Assumed:** The worked AR(1) is initialized in its stationary regime with independent mean-zero innovations; $|\phi|<1$ is required. A stationary process here has finite second moments by definition.
- **Disputed:** A process can have constant marginal mean and variance yet fail the lag-covariance requirement. Weak stationarity alone does not imply strict stationarity outside suitable families such as Gaussian. An AR coefficient inside the unit circle does not make an arbitrary deterministic start stationary at its first time point.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 536, “Time Series”; existing `dodge2008` key for history.
- The repository's time-series book chapter was read for the mathematical baseline. Its inherited Khinchin, Wold and Brockwell–Davis citations remain; new mathematical claims are proved or computed rather than attributed to unread full publications.

## Changes

Added motivation, precise moment conditions, AR(1) proof and numerical example with hidden answer, an explicit weak-not-strict construction, distinct misconceptions, concrete failures, connections and history. Three answered bank checks, one already available, await integration. No figure was present.
