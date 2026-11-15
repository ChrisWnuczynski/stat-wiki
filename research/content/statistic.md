## Lead context
Statistics turn a collection of observations into quantities that can be compared with a probability model. A sample mean, a range, and a test score are all statistics, but they answer different questions about the same data.

## Motivating example
A factory weighs four packages and records 1, 3, 5, and 7 units above its target. The average excess, four units, is a statistic: anyone with the four readings can calculate it. If the factory's true long-run mean excess is unknown, subtracting that unknown mean from the sample average produces a useful theoretical random quantity, but it is not a statistic one can compute from those readings alone.

## Intuition
Before sampling, a statistic is a random variable because a new sample would usually give a different value. After sampling, its realised value is a fixed number. Its *sampling distribution* describes the values it would take across hypothetical repetitions of the same sampling procedure. A statistic's formula cannot contain an unknown population parameter, although its sampling distribution often does.{{cite:fisher1922,nist_glossary2002}}

## Definition
Write $X_1,\ldots,X_n$ for the random observations before collection, and $x_1,\ldots,x_n$ for their realised values. A statistic is $T=t(X_1,\ldots,X_n)$ for a specified function $t$ that uses only the sample and known constants; its observed value is $t(x_1,\ldots,x_n)$. The function may return a vector, such as a pair of sample summaries, rather than just one number. The [sample mean](summary-statistics.qmd) $\overline X=n^{-1}\sum_iX_i$ and, for $n\geq2$, the [sample variance](sample-variance-and-standard-deviation.qmd) $s^2=(n-1)^{-1}\sum_i(X_i-\overline X)^2$ are statistics. The population mean $\mu$ and variance $\sigma^2$ describe the sampling model and are not calculated from the particular sample.{{cite:fisher1922,nist_glossary2002}}

## Properties
The moments result above assumes independent, identically distributed observations with finite variance $\sigma^2$ and common mean $\mu$. It says the sample mean is centred on $\mu$, its variance falls as the sample size grows, and $s^2$ has expectation $\sigma^2$. These are sampling-distribution facts, rather than facts about one observed mean or variance.{{cite:siegrist2022_normals}}

The normal sample theorem adds three exact distributional conclusions when the observations are normal. The sample mean is then normal, the scaled residual sum of squares is chi-squared, and the mean and sample variance are independent. That independence is special: it need not hold for a nonnormal population even though the preceding moment identities still hold.{{cite:siegrist2022_normals}}

Proof idea: centre the observations at their population mean for the moment calculation. For a normal sample, rotate the vector of standardised observations so one coordinate represents the sample mean and the other coordinates represent residuals.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For independent, identically distributed $X_i$ with mean $\mu$ and variance $\sigma^2$, linearity gives $\mathbb E\overline X=\mu$, and independence gives $\operatorname{Var}(\overline X)=n^{-2}\sum_i\operatorname{Var}(X_i)=\sigma^2/n$. The identity $\sum_i(X_i-\overline X)^2=\sum_i(X_i-\mu)^2-n(\overline X-\mu)^2$ follows by expansion and $\sum_i(X_i-\overline X)=0$. Its expectation is $n\sigma^2-n(\sigma^2/n)=(n-1)\sigma^2$, so $\mathbb E s^2=\sigma^2$. None of these steps needs normality.{{cite:siegrist2022_normals}}

Now suppose the observations are also normal and $\sigma>0$. The variables $Z_i=(X_i-\mu)/\sigma$ are independent standard normals. Apply an orthogonal rotation whose first row is $(1/\sqrt n,\ldots,1/\sqrt n)$. The rotated vector still has independent standard-normal coordinates. Its first coordinate is $\sqrt n(\overline X-\mu)/\sigma$, proving the stated normal law for $\overline X$. By preservation of squared length, the sum of squares of the remaining $n-1$ coordinates is $\sum_i(X_i-\overline X)^2/\sigma^2=(n-1)s^2/\sigma^2$, proving its $\chi^2_{n-1}$ law. Those coordinates are independent of the first, so $s^2$ and $\overline X$ are independent. This proves all three parts of the theorem as stated above.{{cite:siegrist2022_normals}}
:::
:::

## Statistical use
An [estimator](estimator.qmd) is a statistic used to guess a population parameter; the sample mean is an estimator of $\mu$ in the model above. A test statistic reduces data to a value that can be compared with a reference distribution. For example, when a null hypothesis fixes a known value $\mu_0$, the quantity $(\overline X-\mu_0)/(s/\sqrt n)$ is computable from the sample and is a statistic. Under the normal model and that null hypothesis it has a $t_{n-1}$ distribution, because the proof above supplies an independent standard-normal numerator and scaled chi-squared denominator. Replacing $\mu_0$ by an *unknown* $\mu$ gives a pivot useful in theory but not a statistic that can be evaluated from the data alone.{{cite:siegrist2022_normals}}

## Worked example
For readings $1,3,5,7$, the observed sample mean is $\overline x=(1+3+5+7)/4=4$, and the range is $7-1=6$. The squared deviations from the sample mean are $9,1,1,9$, giving $s^2=20/(4-1)=20/3\approx6.67$. All three values are statistics computed from this sample. If the population mean $\mu$ is unknown, $\overline x-\mu$ cannot be evaluated, although the random variable $\overline X-\mu$ has a sampling distribution under a specified model.

**Your turn.** A new sample is $2,4,6$. Find its mean, sample variance, and range. If a null hypothesis specifies $\mu_0=4$, is $(\overline X-\mu_0)/(s/\sqrt3)$ a statistic, and what is its observed value?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $4$, the sample variance is $[(-2)^2+0^2+2^2]/(3-1)=4$, and the range is $6-2=4$. Because $\mu_0$ is specified, the expression is a statistic; its observed numerator is zero, so its value is $0$.
:::

## Common misconceptions
“Statistic” does not mean only a sample mean or an estimate. The maximum, range, sample variance, and a test score all qualify if their formulas use only observed data and known constants. A statistic also need not have a parameter-free sampling distribution: the sample mean's distribution generally changes with the unknown population mean. Conversely, a formula involving an unknown parameter is not a statistic merely because its distribution happens to be known; the existing $t$ pivot example makes that distinction.{{cite:fisher1922,siegrist2022_normals}}

## Assumptions and limits
The definition of a statistic does not assume normality, independence, or a large sample. Those assumptions enter when deriving a particular sampling distribution or interpreting the result. Reducing a dataset to one statistic can lose information about the model parameter; a [sufficient statistic](sufficient-statistic.qmd) is a special statistic that retains all parameter information in a specified model. The same numerical summary may be sufficient in one model and insufficient in another, so the claim must always name the model.{{cite:fisher1922}}

## Connections
Every [estimator](estimator.qmd) is a statistic used for a particular inferential goal, while a statistic such as the sample range need not be an estimator of the parameter under discussion. A sampling distribution describes the statistic before data are observed. A [pivot](pivot.qmd) may include an unknown parameter but has a known distribution; the existing normal-sample example shows why that differs from the definition here. [Sufficiency](sufficient-statistic.qmd) asks whether a statistic preserves all information about a model parameter.{{cite:fisher1922,siegrist2022_normals}}

## Check yourself
Try [deciding which formulas are statistics](../questions/ex-inf-which-are-statistics.qmd), then [deriving the sample-variance expectation](../questions/ex-inf-expected-sample-variance.qmd). The first tests whether a formula is computable; the second tests a property of a computable summary under repeated sampling.

::: {.callout-tip collapse="true" title="Answers"}
In the first problem, $\overline X$, the sample range, and $\sum_iX_i^2$ are statistics. The formulas containing the unknown $\mu$ are not, even though one has a parameter-free $t$ distribution. In the second, expanding around $\mu$ gives $\sum_i(X_i-\overline X)^2=\sum_i(X_i-\mu)^2-n(\overline X-\mu)^2$; expectations are $n\sigma^2$ and $\sigma^2$ respectively, so $\mathbb E s^2=\sigma^2$.{{cite:siegrist2022_normals}}
:::

## History
In his 1922 paper on the mathematical foundations of theoretical statistics, Ronald Fisher described reducing a sample to statistics and then judging those statistics by their sampling behaviour. He distinguished problems of estimating population parameters from problems of deriving the distributions of functions of observations. The problem was how to extract information from a sample without confusing an observed summary with an unknown feature of the population.{{cite:fisher1922}}

Fisher also formulated sufficiency as a test of whether a statistic retained all the sample's information about a parameter. Modern practice uses statistics both for estimation and for testing: a data summary is interpreted through its sampling distribution, and its standard error describes repeated-sample variation. These roles appear in the NIST statistical glossary and in current treatments of normal-sample inference.{{cite:fisher1922,nist_glossary2002,siegrist2022_normals}}
