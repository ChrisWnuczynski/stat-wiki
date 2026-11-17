## Lead context
One sample is often all the data there are, and a second independent sample is not coming. Resampling draws further samples from the sample already in hand, refits the same statistic or the same model on each draw, and reads the scatter of those refits as information about the original fit.{{cite:james_islr2013}} (p. 175, Ch. 5){{cite:dodge2008}} (p. 456, sampling inside the initial sample)

## Motivating example
The slope of a least-squares line has a formula for its standard error when the errors are uncorrelated and the variance is constant. A median, a ratio of two coefficients, or a curve chosen by looking at several degrees does not hand over such a formula. Drawing many new samples from the observations that were actually collected, and recomputing the statistic each time, produces a list of values whose spread stands in for the sampling variability that a second real sample would have shown.{{cite:james_islr2013}} (p. 175, Ch. 5, variability of a linear regression fit; p. 187, §5.2)

## Intuition
The empirical distribution of the sample is a stand-in for the population distribution. Sampling from it, with replacement, is the bootstrap: each draw has the same size as the original sample, and the same observation can appear more than once. Leaving out one observation at a time, and recomputing the statistic on what remains, is the jackknife. Holding out a block of observations, fitting on the rest, and scoring the block, is cross-validation. All three reuse the sample. They differ in what they are trying to see: the jackknife was introduced to estimate bias, resampling was used to estimate variance, and cross-validation estimates the error of a prediction on observations the fit did not see.{{cite:dodge2008}} (pp. 456–457){{cite:james_islr2013}} (pp. 175–176, Ch. 5)

## Definition
Resampling methods calculate a statistic repeatedly on samples drawn from the observed sample. In the bootstrap, each resample is drawn with replacement and has the original sample size. For a sample of $n$ distinct values the number of possible resamples is $n^n$, and each is equally likely if the draw is uniform. The bootstrap distribution of a statistic $T$ is the distribution of $T$ across those resamples. Its mean and variance estimate the mean and variance of $T$ under the empirical distribution.{{cite:james_islr2013}} (p. 187, §5.2){{cite:dodge2008}} (p. 457, see bootstrap)

The jackknife of a statistic $\hat\theta$ computed on a sample of size $J$ uses the $J$ leave-one-out values $\hat\theta_{(i)}$. Their average is $\hat\theta_{(\cdot)}$. The jackknife estimate of bias is
\[
B=(J-1)\bigl(\hat\theta_{(\cdot)}-\hat\theta\bigr),
\]
and $\hat\theta-B$ is the bias-corrected value, equal to $J\hat\theta-(J-1)\hat\theta_{(\cdot)}$.{{cite:dodge2008}} (pp. 272 and 457, jackknife bias)

Cross-validation holds out part of the sample, fits on the complement, and records the prediction error on the held-out part. The training error, computed on the same observations that were fitted, can be much smaller than the test error on new observations. The held-out error is a resampling estimate of that test error.{{cite:james_islr2013}} (pp. 175–176, Ch. 5)

## Properties
For the sample mean, every bootstrap resample is an average of draws from the observed values, and the mean of those averages equals the sample mean. If one draw from the empirical distribution has variance $v$, an average of $n$ independent draws has variance $v/n$. The jackknife bias of the sample mean is zero, because each leave-one-out mean averages to the sample mean.

For the divide-by-$n$ variance the jackknife need not be zero. The correction $n\hat\theta-(n-1)\hat\theta_{(\cdot)}$ is the general bias-corrected value from the formula above. On the three-point sample in the worked example it changes $2/3$ into $1$.{{cite:dodge2008}} (p. 272, bias formula)

Cross-validation and the bootstrap answer different questions even though both redraw the sample. A cross-validation average estimates prediction error. A bootstrap spread estimates the sampling variability of a statistic that was computed on the whole sample. Using one in place of the other mixes those targets.{{cite:james_islr2013}} (p. 175, Ch. 5, model assessment versus the accuracy of an estimate)

## Statistical use — Reading a list of refits
Use the bootstrap when the statistic is an awkward function of the sample and a standard-error formula is missing or doubtful, and report the spread of the recomputed statistic across the resamples. Use the jackknife when the leading question is bias of a smooth statistic and $n$ refits are enough. Use [cross-validation](cross-validation.qmd) when the leading question is how a fitted predictor performs on observations it did not train on. In every case the original sample has to be a reasonable picture of the population the next sample would come from. A sample that misses an entire region of that population produces resamples with the same hole.{{cite:james_islr2013}} (pp. 175–176, Ch. 5){{cite:dodge2008}} (p. 457, false inferences if the sample does not represent the population)

## Worked example
The sample is $1,2,3$. The sample mean is $2$, and the divide-by-$n$ variance is
\[
\hat\theta=\frac{(1-2)^2+(2-2)^2+(3-2)^2}{3}=\frac{2}{3}.
\]
There are $3^3=27$ bootstrap samples of size $3$. The mean of their means is $2$. The variance of one draw under the empirical distribution is $2/3$, so the variance of the bootstrap mean is $(2/3)/3=2/9\approx 0.2222$.

The leave-one-out divide-by-$n$ variances are $0.25$ on $\{2,3\}$, $1$ on $\{1,3\}$, and $0.25$ on $\{1,2\}$. Their average is $\hat\theta_{(\cdot)}=0.5$. The jackknife bias is
\[
B=(3-1)\bigl(0.5-\tfrac{2}{3}\bigr)=-\tfrac{1}{3}.
\]
The corrected value is $\hat\theta-B=1$, which is also $3\hat\theta-2\hat\theta_{(\cdot)}$. The jackknife has changed $2/3$ into $1$ by recomputing the statistic three times.{{cite:dodge2008}} (pp. 272 and 457)

**Your turn.** The sample is $4$ and $9$. List the four equally likely bootstrap samples of size $2$, their means, and the average of those means.

::: {.callout-tip collapse="true" title="Answer"}
The samples are $(4,4)$, $(4,9)$, $(9,4)$ and $(9,9)$. Their means are $4$, $6.5$, $6.5$ and $9$. The average of the four means is $6.5$, the mean of the original sample.
:::

## Common misconceptions
Resampling does not create new information about a population the original sample never represented. Twenty-seven bootstrap means from $1,2,3$ describe the sample $1,2,3$. They do not discover that a fourth, unobserved, population value exists.{{cite:dodge2008}} (p. 457)

The bootstrap spread of a coefficient is not a cross-validation estimate of prediction error. One refits the statistic on resamples of the whole sample. The other scores observations that were held out of the fit.{{cite:james_islr2013}} (p. 175, Ch. 5)

A jackknife bias of zero does not mean the statistic is a good estimator. The sample mean has jackknife bias zero and can still have a large variance. The correction above changed $2/3$ into $1$ only because the defect was bias of a particular variance formula.{{cite:dodge2008}} (p. 272)

## Assumptions and limits — The sample has to stand for the population
Bootstrap variances treat the empirical distribution as the truth. Dependence, a sample selected by the size of the response, or a population with much heavier tails than the sample, all break that substitution. The jackknife bias formula is a linear approximation in the leave-one-out values. It is reliable for smooth statistics such as a variance, and it is a poor tool for a statistic that jumps when one point is removed, such as a sample maximum. Cross-validation estimates test error for the fitting procedure that was actually repeated on the training folds. It does not estimate the error of a procedure that was chosen after seeing the held-out scores.{{cite:james_islr2013}} (pp. 175–176, Ch. 5, training error versus test error){{cite:dodge2008}} (p. 457)

## Connections
The [bootstrap](bootstrap.qmd) and the [jackknife](jackknife.qmd) are the two resampling plans named for a whole-sample statistic. [Leave-one-out cross-validation](leave-one-out-cross-validation.qmd) uses the same leave-one-out subsets as the jackknife and scores prediction error rather than bias. A [sampling distribution](sampling-distribution.qmd) is what these calculations are trying to approximate when a fresh sample cannot be drawn. [Mean squared error](mean-squared-error.qmd) is one target a bias estimate and a variance estimate can be combined to describe.{{cite:dodge2008}} (p. 457, bootstrap, jackknife, and Monte Carlo){{cite:james_islr2013}} (p. 175, Ch. 5)

## History
The jackknife was introduced in the 1950s as a way to reduce the bias of an estimate. Through the 1960s and 1970s, resampling was used to estimate variances. The bootstrap was introduced by Efron in the late 1970s and then developed across many fields. Cross-validation, as used now, estimates prediction error by holding data out of the fit, precisely because the training error on the fitted observations can be much smaller than the error on new observations.{{cite:dodge2008}} (p. 457){{cite:james_islr2013}} (pp. 175–176, Ch. 5)
