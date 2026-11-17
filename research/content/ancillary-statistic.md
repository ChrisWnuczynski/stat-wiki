## Lead context
An ancillary statistic is a function of the sample whose distribution does not depend on the parameter.

## Motivating example
The observations \(3,5,7\) have mean \(5\) and centred values \(-2,0,2\). Adding \(4\) to every observation produces \(7,9,11\), with mean \(9\) and the same centred values \(-2,0,2\). The centred vector did not see the location shift. For any other shift the same cancellation occurs, which is why the distribution of the centred vector does not depend on \(\mu\).

## Intuition — Variation the parameter does not move
A sufficient statistic collects the part of the sample that moves with \(\theta\). An ancillary statistic collects a part whose probabilities can be written without \(\theta\). The formula still uses the data. What is free of \(\theta\) is the distribution. The property is tied to the named parameter. A statistic that ignores a normal mean, while the variance is treated as known, need not ignore the pair consisting of the mean and the variance.

## Definition — A distribution free of \(\theta\)
For a model \(\{P_\theta\}\), a statistic \(A=A(X)\) is ancillary for \(\theta\) when the law of \(A\) under \(P_\theta\) is the same for every \(\theta\). Equivalently, \(\mathbb{P}_\theta(A\in B)\) can be computed without knowing \(\theta\). If the model has a nuisance parameter, ancillarity for the interest parameter allows the nuisance parameter to remain in the distribution; ancillarity for the whole parameter does not.{{cite:dasgupta2007_basu}} (pp. 945–946, Basu's theorem)

## Properties — Centring removes a location
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let \(X_i=\mu+\varepsilon_i\) for \(i=1,\ldots,n\), with the \(\varepsilon_i\) independent of \(\mu\) and identically distributed, and write \(\overline X=n^{-1}\sum_i X_i\). Then
\[
X_i-\overline X=\varepsilon_i-\overline\varepsilon,
\]
because \(\mu\) is added to every observation and cancels in the difference. The centred vector is a function of \((\varepsilon_1,\ldots,\varepsilon_n)\) alone, so its distribution does not depend on \(\mu\). It is ancillary for \(\mu\) when \(\mu\) is the only unknown parameter. If a scale \(\sigma\) multiplies \(\varepsilon_i\), the centred vector is multiplied by \(\sigma\), so its distribution depends on \(\sigma\). It is then not ancillary for the pair \((\mu,\sigma)\).
:::
:::

{{cite:dasgupta2007_basu}} (pp. 945–946, Basu's theorem)

## Worked example — A shift that disappears

**Your turn.** Centre the sample \(1,1,4\). What is the centred vector, and what is the sum of its entries?

::: {.callout-tip collapse="true" title="Answer"}
The mean is \(2\), so the centred vector is \((-1,-1,2)\). The entries sum to \(0\). Every centred sample has that sum, because the deviations from a mean sum to zero. The vector is still random: only one linear constraint is fixed.
:::

## Connections — Sufficiency and Basu
A [sufficient statistic](sufficient-statistic.qmd) is the piece that carries \(\theta\). An ancillary statistic is a piece whose distribution does not. Whether that separation upgrades to independence is [Basu's theorem](basu-s-theorem.qmd). The centred vector in the proof is ancillary for a pure location parameter and, once a free scale is present, not ancillary for the pair.{{cite:dasgupta2007_basu}} (pp. 945–946, Basu's theorem)

