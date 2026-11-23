## Lead context
Resampling draws further samples from the observed sample and refits a statistic on each draw. The original sample is used more than once. The refits are used to estimate the bias or the standard deviation of a parameter estimate, or to form an interval, when a formula for that estimate is missing or doubtful. The draws are not new observations from the population. They are new combinations of the observations already in hand.{{cite:dodge2008}} (p. 456){{cite:james_islr2013}} (p. 175, Ch. 5)

## Motivating example
A sample of three numbers, $1$, $2$, and $3$, is all the data available. The sample mean is $2$. A standard-error formula for the mean exists, and for this tiny sample it can be checked by listing every resample. The same listing also shows the bias of a variance formula that divides by $n$ rather than by $n-1$. The point of the listing is the method: recompute the statistic on samples drawn from the sample, and read the spread or the bias off those recomputations. For a regression coefficient whose standard error the software does not print, the same method is often the practical one.{{cite:james_islr2013}} (pp. 175, 187, §5.2){{cite:dodge2008}} (p. 456)

## Definition
While a sample is being used to estimate a parameter of the population it came from, the same sample can be sampled again. That second sampling is resampling. Bootstrap, jackknife, and cross-validation are three techniques that do it. They are especially used when the exact distribution of the data is unknown, or when the data come from a design that is hard to model.{{cite:dodge2008}} (p. 456)

The bootstrap draws samples of size $n$ with replacement from the $n$ observations, recomputes the statistic on each draw, and uses the spread of those recomputations as a measure of uncertainty. The draws come from the empirical distribution of the sample itself; a fitted-model resample would instead simulate new data from an estimated model.{{cite:shalizi2025_truth_regression}} (Ch. 24, §24.4, p. 392) For the sample $1, 2, 3$ there are $3^3=27$ such ordered draws. Conditional on the observed sample, each is equally likely, because each position in the draw is filled independently and uniformly from the three observed values; that equiprobability is a property of the resampling mechanism itself and does not require the empirical distribution to equal the unknown population distribution. The jackknife recomputes the statistic $n$ times, each time deleting one observation. Dodge writes the jackknife bias of an estimate $\hat\theta$ as

$$
B(\hat\theta)=(J-1)\bigl(\hat\theta_{(\cdot)}-\hat\theta\bigr),
$$


where $J=n$ when each deleted block is a single observation and $\hat\theta_{(\cdot)}$ is the average of the leave-one-out estimates. The leading $1/n$ term in the bias is removed by subtracting $B$. Cross-validation holds observations out of the fit and scores the fit on the held-out observations. It estimates prediction error. It does not estimate the sampling variance of a coefficient.{{cite:dodge2008}} (pp. 272, 456){{cite:james_islr2013}} (pp. 176, 187, §5.1 and §5.2)

## Interpretation
The bootstrap spread of a statistic is the variability of that statistic across resamples of this sample. It is a description of the sample's empirical distribution. If the sample is a reasonable picture of the population, the description is a usable stand-in for the sampling variability one would see in new samples from the population. If the sample misses a region of the population, every resample misses it too: resampling cannot recover support that the sample never had. What that missing support does to the uncertainty estimate has no guaranteed direction. Dodge's warning is sharp: when the sample does not represent the population, the procedures risk absolutely false inferences.{{cite:dodge2008}} (pp. 456–457)

A jackknife bias of zero does not mean the statistic is a good estimator. The sample mean has jackknife bias zero, because every leave-one-out mean averages back to the full mean, and the mean can still have a large variance. The correction is aimed at bias of order $1/n$. It is not a variance estimate.{{cite:dodge2008}} (p. 272)

Training error and test error are a different pair. The training error is the error of a fitted rule on the observations used to fit it. The test error is the error on a new observation. Cross-validation estimates the second by resampling the role of "new." A bootstrap standard error of a coefficient estimates how much the coefficient would move if the sample were drawn again. When the coefficient comes from a regression fit, that redraw can resample whole cases or resample the fit's residuals; the two schemes preserve different structure.{{cite:shalizi2025_truth_regression}} (Ch. 24, §24.5.3, p. 396 and §24.5.4, pp. 398–399) Quoting one of those numbers as the other answers the wrong question.{{cite:james_islr2013}} (pp. 175–176, Ch. 5)

## Worked example
The sample is $1, 2, 3$. The sample mean is $2$, and the divide-by-$n$ variance is

$$
\hat\theta=\frac{(1-2)^2+(2-2)^2+(3-2)^2}{3}=\frac{2}{3}.
$$


There are $27$ bootstrap samples of size $3$. The mean of their means is $2$. The variance of one draw under the empirical distribution is $2/3$, so the variance of the bootstrap mean is $(2/3)/3=2/9\approx 0.2222$.

The leave-one-out divide-by-$n$ variances are $0.25$ on $\{2,3\}$, $1$ on $\{1,3\}$, and $0.25$ on $\{1,2\}$. Their average is $\hat\theta_{(\cdot)}=0.5$. The jackknife bias is

$$
B=(3-1)\bigl(0.5-\tfrac{2}{3}\bigr)=-\tfrac{1}{3}.
$$


The corrected value is $\hat\theta-B=1$, which is also $3\hat\theta-2\hat\theta_{(\cdot)}$. The jackknife has changed $2/3$ into $1$ by recomputing the statistic three times.{{cite:dodge2008}} (pp. 272, 457)

**Your turn.** The sample is $4$ and $9$. List the four equally likely bootstrap samples of size $2$, their means, and the average of those means.

::: {.callout-tip collapse="true" title="Answer"}
The samples are $(4,4)$, $(4,9)$, $(9,4)$, and $(9,9)$. Their means are $4$, $6.5$, $6.5$, and $9$. The average of the four means is $6.5$, the mean of the original sample.
:::

## Connections
The [bootstrap](bootstrap.qmd) is the with-replacement half of the method, and the [jackknife](jackknife.qmd) is the leave-one-out half used for bias. [Cross-validation](cross-validation.qmd) is the hold-out half used for prediction error. A [standard error](standard-error.qmd) computed from a formula is the closed-form cousin of the bootstrap spread, available when the statistic is simple enough that the formula exists. The bootstrap remains useful for a [linear regression](simple-linear-regression.qmd) coefficient precisely when one wants a check on that formula, and it is the default when the learning method does not supply a formula at all.{{cite:james_islr2013}} (p. 187, §5.2){{cite:dodge2008}} (p. 457)

## History
The jackknife was introduced in the 1950s as a way to reduce the bias of an estimate. Through the 1960s and 1970s, resampling was used in sampling theory to estimate a variance. The bootstrap was introduced by Efron in the late 1970s and then developed across fields. The three names now sit together because each one recomputes a statistic on data drawn from the observed sample, and each one fails, in the same way, when that sample is not a picture of the population the next sample would come from.{{cite:dodge2008}} (pp. 456–457){{cite:james_islr2013}} (p. 187, §5.2)
