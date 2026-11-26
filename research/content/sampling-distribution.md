## Lead context
A statistic changes from sample to sample. The sampling distribution is the distribution of those changes, before any particular sample is drawn. {{cite:dodge2008}} (p. 471) {{cite:nist_glossary2002}} (Glossary, “sampling distribution”)

## Motivating example
A population of three workshops has daily outputs 1, 2, and 3 tonnes. Samples of size 2, drawn without replacement, are the pairs (1, 2), (1, 3), and (2, 3). Their means are 1.5, 2, and 2.5. Those three numbers, equally likely, are the sampling distribution of the sample mean. The population mean is 2, and the mean of the three sample means is also 2. {{cite:dodge2008}} (p. 471) {{cite:dodge2008}} (p. 412)

## Intuition
The population is fixed. The sample is random. A statistic is a function of the sample, so it is a random variable. Its distribution is what repeated sampling would produce. A standard error is the standard deviation of that distribution, not the standard deviation of the one sample in hand. {{cite:nist_glossary2002}} (Glossary, “standard error”) {{cite:dodge2008}} (p. 472)

## Definition
A sampling distribution is the distribution of a statistic $T(X_1,\ldots,X_n)$, where $T$ is a function of the sample. {{cite:dodge2008}} (p. 471) In the same words, it is the distribution of a summary quantity calculated from sample data. {{cite:nist_glossary2002}} (Glossary, “sampling distribution”) {{cite:nist_glossary2002}} (Glossary, “statistic”)

For a finite population of size $N$, the number of samples of size $n$ drawn without replacement is the number of combinations $\binom{N}{n}$, when every such sample is equally likely. {{cite:dodge2008}} (p. 471)

## Properties
The mean of the sampling distribution of the sample mean equals the population mean. The standard deviation of that sampling distribution is the standard error of the mean. For sampling without replacement from a finite population it is smaller than $\sigma/\sqrt{n}$ by the factor $\sqrt{(N-n)/(N-1)}$. {{cite:dodge2008}} (p. 472)

In the three-workshop example the population variance of 1, 2, 3 about the mean 2 is $((1-2)^2+(0)^2+(1)^2)/3 = 2/3$. The three sample means 1.5, 2, 2.5 have variance about 2 equal to $(0.25+0+0.25)/3 = 1/6$. {{cite:dodge2008}} (p. 471)

## Statistical use
A confidence interval is a range in which the true population value is estimated to lie. When the sampling distribution of a statistic is approximately normal, an interval of about two standard errors on either side of the estimate is a usual approximate 95 percent interval. {{cite:abs_glossary2023}} (Glossary, “Confidence interval”) {{cite:nist_glossary2002}} (Glossary, “standard error”)

## Worked example
Population values 1, 2, 3. Equally likely samples of size 2 have means 1.5, 2, and 2.5. The sampling distribution of $\bar X$ therefore puts probability $1/3$ on each of those three numbers. Its expectation is $(1.5+2+2.5)/3 = 2$, the population mean. {{cite:dodge2008}} (p. 471) {{cite:dodge2008}} (p. 412)

**Your turn.** Samples of size 1 from the same population are just the single values 1, 2, and 3, each with probability $1/3$. What is the expectation of that sampling distribution?

::: {.callout-tip collapse="true" title="Answer"}
The expectation is $(1+2+3)/3 = 2$, the same population mean.
:::

## Common misconceptions
The histogram of one sample is not the sampling distribution. The histogram describes the observations. The sampling distribution describes a statistic computed from those observations, across samples. {{cite:nist_glossary2002}} (Glossary, “sampling distribution”) {{cite:abs_glossary2023}} (Glossary, “Statistic”)

A standard error is not a standard deviation of the raw data. It is the spread of the statistic. {{cite:nist_glossary2002}} (Glossary, “standard error”) {{cite:dodge2008}} (p. 472)

## Assumptions and limits
The shape of the sampling distribution depends on the population, the sample size, and the way the sample is drawn. Replacing without-replacement draws by with-replacement draws changes the standard error. A formula derived for one design is the wrong description of another. {{cite:dodge2008}} (p. 472) {{cite:nist_glossary2002}} (Glossary, “sample”)

## Connections
The [statistic](statistic.qmd) is the random quantity. The [parameter](parameter.qmd) is the population feature that statistic is often aimed at. A [confidence interval](confidence-interval.qmd) is a procedure whose coverage is a probability in the sampling distribution. The [standard error](standard-error.qmd) is that distribution's standard deviation. {{cite:dodge2008}} (p. 412) {{cite:nist_glossary2002}} (Glossary, “standard error”)

For a normal population, some sampling distributions are known in closed form: the sample mean is exactly normal, the scaled sample variance follows the [chi-squared distribution](chi-squared-distribution.qmd), the standardised mean with an estimated scale follows the [Student t distribution](student-t-distribution.qmd), and a ratio of two scaled variances follows the [F distribution](f-distribution.qmd); the joint statement for the mean and the scatter is the [sampling law of the normal mean and scatter](sampling-law-of-the-normal-mean-and-scatter.qmd). When no closed form is available, the [central limit theorem](central-limit-theorem.qmd) supplies the large-sample approximation instead.{{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”)

## History
Once a sample was accepted as evidence about a population, the next question was how the summary itself varies. The sampling distribution is that question made precise: not the distribution of the units, but the distribution of the function of the sample. {{cite:dodge2008}} (p. 471) {{cite:dodge2008}} (p. 518)
