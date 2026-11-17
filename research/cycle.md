# Cycle

Generator input: [research prose](content/cycle.md). Numerical verification: [Python check](../checks/cycle.py).

## Sources read

- `hyndman_athanasopoulos2021` (§2.3, Time series patterns)
- `dodge2008` (p. 536, Time Series)
- `hyndman_athanasopoulos2021` (§3.2, Time series components)
- `hyndman_athanasopoulos2021` (§9.1, Stationarity and differencing)
- `hyndman_athanasopoulos2021` (§3.2, Seasonally adjusted data)

## Calculations

Applied lag-12 and lag-24 differences to the two-frequency series, checked the filter magnitude and common period, and recomputed the linked AR(1) covariance and forecast-loss examples.

## Validation

Final build, all fifteen page checks, offline citation validation and full unit suite are recorded in the batch report. Shared corrections are staged outside tracked inputs for orchestrator integration.
