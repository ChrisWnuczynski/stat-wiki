## Motivating example
A fitted statistic may have no convenient standard-error formula. Recompute it after removing each observation in turn and examine how much it changes. These leave-one-out fits supply the ingredients of the jackknife. They can estimate sampling variability and, for suitably smooth statistics, diagnose a leading finite-sample bias. The bias estimate and standard-error estimate are different summaries of the same recomputations.{{cite:efron1981}} (§5, pp. 592–593)

The observations are the sampling units. If an experiment samples independent clusters rather than independent individuals, deleting one individual does not reproduce the experiment's variation. The deletion scheme must match that sampling structure; ordinary delete-one formulas are written for an independent identically distributed sample.

## Definition — Delete-one values, their average and pseudovalues
For a statistic $\widehat\theta=T(x_1,\ldots,x_n)$, let $\widehat\theta_{(-i)}$ be its value with observation $i$ removed. Put $\overline\theta_{(-)}=n^{-1}\sum_i\widehat\theta_{(-i)}$. The estimated bias is
$$\widehat B_J=(n-1)(\overline\theta_{(-)}-\widehat\theta),$$
and the bias-corrected estimate is $\widehat\theta_J=n\widehat\theta-(n-1)\overline\theta_{(-)}$. The pseudovalue $q_i=n\widehat\theta-(n-1)\widehat\theta_{(-i)}$ has average $\widehat\theta_J$. These definitions fix the sign of the bias correction: subtract the estimated bias from the full-sample statistic.{{cite:dodge2008}} (pp. 272–273)

The jackknife standard error is
$$\widehat{\operatorname{se}}_J=\left\{\frac{n-1}{n}\sum_i(\widehat\theta_{(-i)}-\overline\theta_{(-)})^2\right\}^{1/2}.$$
Equivalently, its square is the sample variance of the pseudovalues divided by $n$. The factor $(n-1)/n$ is essential: the leave-one-out statistics are highly dependent because most of their observations overlap. Treating them as independent repetitions and using their ordinary standard error would be incorrect.{{cite:efron1981}} (§5, eq. 5.1, pp. 592–593)

## Properties — Why a leading bias term cancels
Suppose $E(T_n)=\theta+a/n+b/n^2+O(n^{-3})$, and each deletion has the same expectation as the statistic from $n-1$ independent observations. Then
$$E(\widehat\theta_J)=nE(T_n)-(n-1)E(T_{n-1})=\theta+O(n^{-2}).$$
The $a$ terms cancel exactly. This argument requires a compatible expansion and deletion procedure. It does not say that every statistic becomes exactly unbiased. A nonsmooth functional, such as an extreme order statistic, may behave poorly under ordinary delete-one resampling.{{cite:dodge2008}} (p. 272){{cite:efron1981}} (§5, pp. 592–593)

For the sample mean, $\overline x_{(-i)}=(n\overline x-x_i)/(n-1)$, so the average deletion mean equals $\overline x$, the bias correction is zero and the pseudovalues equal the observations themselves. The jackknife standard error therefore reduces to $s/\sqrt n$, with $s^2$ using denominator $n-1$. This exact special case is a useful check of any implementation.

## Worked example — A nonlinear statistic
Take $x=(1,2,6)$ and estimate the square of the population mean using $T(x)=\overline x^2$. The full estimate is nine. The three deletion estimates are $16$, $12.25$ and $2.25$, with average $61/6$. The jackknife bias estimate is $2(61/6-9)=7/3$, so the corrected estimate is $20/3$. Squaring a sample mean introduces upward bias through its sampling variance; this calculation removes that contribution using the delete-one values.{{cite:dodge2008}} (p. 272, bias-cancellation calculation)

The pseudovalues are $-5$, $2.5$ and $22.5$. A pseudovalue can be negative even though the statistic is a square. These constructed quantities summarize local influence and are not observations from the population. Their sample variance divided by three is $2425/36$, so the jackknife standard error is $\sqrt{2425}/6=8.20738$. A large uncertainty estimate is plausible here: changing one of only three observations has a substantial effect.{{cite:efron1981}} (§5, eq. 5.1)

**Your turn.** Apply the delete-one jackknife to the sample mean of the same three observations. Give the bias estimate and standard error.

::: {.callout-tip collapse="true" title="Answer"}
The deletion means are $4$, $3.5$ and $1.5$, averaging three. The bias estimate is zero. The standard error squared is $7/3$, so the standard error is $\sqrt{7/3}=1.52753$.
:::

## Assumptions and limits — A deletion sensitivity is not a complete interval
The jackknife uses changes under small perturbations of the empirical distribution. It is most natural for statistics that respond smoothly to those changes. The same observations also determine all deletion fits, so their spread is an estimate of sampling variation rather than an independent experimental replication. Bias correction can increase variability, and neither operation automatically provides an accurate small-sample confidence interval.{{cite:efron1981}} (§§5–6, pp. 592–594)

A t multiplier applied to pseudovalues is an approximation requiring further justification, not an exact consequence of the definitions. For clustered, dependent or weighted data, the sampling design may require deleting groups and modifying the scaling. A report should state the deletion unit and distinguish the full estimate, bias estimate, corrected estimate and estimated standard error.
