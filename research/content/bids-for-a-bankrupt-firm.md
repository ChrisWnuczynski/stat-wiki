## Motivating example
A legal-defence indicator has coefficient $0.2679$. For two otherwise identical firms the fitted mean number of bids is multiplied by $e^{0.2679}=1.307$.

## Intuition — A count that is too regular
The response is the number of takeover bids received by a firm. A Poisson log-linear mean can still describe how that count moves with the firm's size and with the actions taken around the bid. The fitted counts are tighter than a Poisson law with the same mean: when the fit said about seven bids, the firms mostly produced six, seven or eight. The displayed fit is a log-linear mean with an extra dispersion parameter above the Poisson boundary.

## Definition — Reading a log-linear coefficient
The fitted mean for a firm with covariate row $x$ is $\mu=\exp(x^\top\beta)$. {{cite:mccullagh1992_glm_intro}} (p. 544, link and linear predictor) If two rows differ only in a $0/1$ indicator whose coefficient is $\beta_j$, their means differ by the factor $e^{\beta_j}$. {{cite:mccullagh1992_glm_intro}} (p. 544, link and linear predictor) A quadratic term in size, $\beta_s s+\beta_{s^2}s^2$ with $\beta_{s^2}<0$, rises and then falls. Its turning point on the size axis is $s=-\beta_s/(2\beta_{s^2})$.

## Worked example — Legal defence, and the bend in size
The displayed legal-defence coefficient is $0.2679$, with standard error $0.1228$. The mean ratio for two otherwise identical firms is
$$
e^{0.2679}=1.307
$$
to three decimal places, which is $1.31$ to two decimal places. {{cite:mccullagh1992_glm_intro}} (p. 544, link and linear predictor) The ratio of the coefficient to its standard error is $0.2679/0.1228=2.182$, which rounds to the table's $2.18$.

The size coefficients are $0.1793$ and $-0.0076$. The log-mean in size, holding the other covariates at the reference coded as zero, turns at
$$
s=\frac{0.1793}{2\times 0.0076}=11.80
$$
billions, to two decimal places. Relative to size $0$, the mean at that turning point is multiplied by $e^{1.0575}=2.879$ to three decimal places.

**Your turn.** The white-knight coefficient in the same table is $0.4813$. Find the mean ratio $e^{0.4813}$ to three decimal places.

::: {.callout-tip collapse="true" title="Answer"}
$e^{0.4813}=1.618$ to three decimal places. A firm that invites a white knight, with the other covariates unchanged, has a fitted mean $1.618$ times the mean of a firm that does not.
:::

## Connections — Counts, logs, and a tighter variance
The mean equation is a [log link](log-link.qmd) inside a [generalised linear model](generalised-linear-model.qmd). The Poisson boundary is the [Poisson distribution](poisson-distribution.qmd), whose variance equals its mean. The fitted dispersion sits above that boundary, which is why a Poisson or negative-binomial variance cannot represent these counts. The coefficient table is one fitted mean, not a second copy of the raw bids.
