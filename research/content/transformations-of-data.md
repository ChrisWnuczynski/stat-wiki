## Motivating example
Incomes $10,20,40,80$ are equally spaced in their successive ratios, even though their differences are $10,20,40$. Their natural logarithms are equally spaced by $\log2$. A logarithmic scale therefore expresses multiplicative structure as additive structure. This can make a relationship easier to model and describe, provided the scientific meaning of the transformed response is made explicit.{{cite:dodge2008}} (p. 318, “Logarithmic Transformation”)

## Definition
A transformation replaces a variable $x$ by a function $g(x)$. A strictly increasing transformation preserves ranks; a strictly decreasing transformation reverses them. A one-to-one transformation can be inverted on its domain, whereas a many-to-one transformation, such as squaring over all real numbers, loses information about the sign. Logarithms and reciprocals require particular care about zero and negative values.{{cite:dodge2008}} (p. 540, “Transformation”)

Affine transformations change units and origin. Nonlinear transformations change relative distances: for example, a change from $1$ to $2$ and one from $100$ to $101$ are equal on an additive scale but very different on a logarithmic scale. A transformed analysis should therefore be motivated by relationships and variability rather than by the wish to produce a more attractive plot.

## Properties — Which summaries commute with a transformation?
For an odd sample size and the usual middle-order-statistic median, every strictly monotone transformation maps the sample median to the transformed sample median. Ordering proves this directly: the middle rank stays the middle rank even when the order is reversed. For an even sample size, the convention that averages the two middle values breaks this identity under nonlinear transformations.

For example, the two observations $1$ and $9$ have median $5$. Their logarithms have median $(\log1+\log9)/2=\log3$, whereas the logarithm of their median is $\log5$. The transformed median is a geometric rather than arithmetic midpoint in this example. Likewise $\operatorname{mean}(g(x_i))$ need not equal $g(\bar x)$.{{cite:openintro2019}} (§2.1, median and transforming data)

The mismatch is especially important for prediction. If $\log Y=\eta+\varepsilon$ with $\varepsilon\sim N(0,\sigma^2)$, then the conditional median of $Y$ is $e^\eta$ but its mean is $e^{\eta+\sigma^2/2}$. To derive the mean, complete the square in the normal density when integrating $e^\varepsilon$; the resulting normal density integrates to one and leaves the factor $e^{\sigma^2/2}$. Simply exponentiating a fitted log mean therefore targets a median under this model.{{cite:nist_handbook2002}} (§1.3.6.6.9, lognormal distribution)

## Worked example — A multiplicative response model
Take $\log Y=1+0.2x+\varepsilon$, with normal error standard deviation $0.5$. At $x=0$, the conditional median is $e\approx2.7183$ and mean is $e^{1.125}\approx3.0802$. Increasing $x$ by one multiplies both by $e^{0.2}\approx1.2214$, a rise of about $22.14\%$. The approximate percentage change $100\beta=20\%$ is less accurate here than the exact expression $100(e^\beta-1)$.

At $x=1$, a central conditional $95\%$ prediction interval, with the model parameters treated as known and $z=1.96$, is
$$[e^{1.2-1.96(0.5)},e^{1.2+1.96(0.5)}]\approx[1.2461,8.8463].$$
Monotonicity preserves the interval's probability when its endpoints are exponentiated. The unequal distances from the median on the raw scale reflect multiplicative variation; symmetry on the log scale becomes asymmetry on the raw scale.{{cite:nist_handbook2002}} (§1.3.6.6.9, lognormal quantiles)

**Your turn.** A log-linear model has coefficient $\beta=\log(1.5)$. What multiplier corresponds to a two-unit increase in its predictor? For raw observations $1,4,16$, compare the log of the median with the median of the logs.

::: {.callout-tip collapse="true" title="Answer"}
A two-unit increase gives multiplier $e^{2\beta}=1.5^2=2.25$. The median of the observations is $4$, so its logarithm is $\log4$. There are three observations and the logarithm is strictly increasing, so the median of the logs is also $\log4$.
:::

## Statistical use — Diagnostics on the fitted scale
A transformation can reduce skewness, make an association closer to linear, or stabilise a variance. These are distinct goals. A normal-looking marginal response does not ensure normal regression residuals, and a linear mean does not ensure constant residual variance. Check the model on its fitted scale, then explain predictions on the scientifically useful scale.{{cite:openintro2019}} (§2.1, transforming data; §9.3, “Checking model conditions using graphs”)

The creatinine Q–Q plots compare raw measurements with reciprocals. Because the reciprocal is decreasing on positive values, it reverses their ordering and compresses large measurements. Values rounded on the raw scale remain discrete after transformation; a transformed Q–Q plot can therefore show steps even when its overall shape is close to linear. Changes in numerical skewness describe those particular recorded values and do not by themselves establish a normal model.

## Assumptions and limits
Adding a constant before taking logarithms changes ratios and the meaning of the model. The constant should have a defensible measurement interpretation. For zeros arising from censoring, a censoring model may be preferable to an arbitrary offset. The square root of a count and a Poisson GLM are also different approaches: one changes the response, while the other models a count distribution directly. A transformation can improve a model without making every assumption true.
