## Lead context
A summary or a fit is robust when a small fraction of the data, moved a long way, does not move the answer very much. The median is the textbook case. The arithmetic mean is not.{{cite:nist_glossary2002}} (Glossary, "robust methods"){{cite:openintro2019}} (Ch. 2, §2.1.6)

## Motivating example
Five interest rates sit near $10\%$, and one loan is recorded at $26.3\%$. Replacing that one rate by $15\%$, or by $35\%$, leaves the median and the interquartile range where they were and shifts the mean and the standard deviation. The two robust summaries describe the centre and the spread of the bulk of the loans. The mean describes a centre that has been pulled toward the extreme loan. Which description is wanted depends on the question. A typical loan is closer to the median. A total amount of money, added up across many loans, follows the mean.{{cite:openintro2019}} (Ch. 2, §2.1.6, the interest-rate scenarios and the loan-amount comparison)

## Intuition
Squared error charges a residual of size $10$ as $100$, and a residual of size $1$ as $1$. A single wild point can therefore dominate the fit. Absolute error charges that residual as $10$, in proportion to its size. Huber's loss uses the square while the residual is smaller than a chosen cutoff and then switches to a straight line, so ordinary points keep the efficiency of least squares and gross points lose their squared leverage. The population version of the same idea picks the conditional mean under squared error and the conditional median under absolute error. On a symmetric error law those two targets agree. On a long-tailed law, or in a sample with a misrecorded response, they do not.{{cite:hastie_esl2009}} (pp. 349–350, §10.6, squared error, absolute error, and Huber loss){{cite:dodge2008}} (p. 464, replacing the square by a function $\delta$)

## Definition
A statistical method is robust when extreme changes to a small portion of the data do not change its answer strongly. An estimator of a regression coefficient, or of a location, is robust in the same sense when it is not sensitive to outliers or to small departures from the model that was written down.{{cite:nist_glossary2002}} (Glossary, "robust methods"){{cite:dodge2008}} (p. 463, robust estimation)

For a location $t$ and observations $y_1,\ldots,y_n$, least squares minimises $\sum_i(y_i-t)^2$ and returns the sample mean. Least absolute deviations minimises $\sum_i|y_i-t|$ and returns a sample median. An M-estimator replaces the square by a symmetric function $\delta$ with a unique minimum at zero, and minimises $\sum_i\delta(y_i-t)$. Huber's choice, for a positive cutoff $k$, is the square $x^2/2$ when $|x|\le k$ and the line $k|x|-k^2/2$ when $|x|>k$. The absolute-deviation estimator is the special case of a pure line.{{cite:dodge2008}} (p. 464){{cite:hastie_esl2009}} (p. 349, §10.6, equation (10.23))

In regression the same replacement is made inside the loss $L(y,f(x))$. Squared error, absolute error, and Huber loss are three such choices. The fitted function changes with the loss.{{cite:hastie_esl2009}} (pp. 349–350, §10.6)

## Properties
On the five numbers $1,2,3,4,20$ the mean is $6$ and the median is $3$. The sum of absolute deviations is $28$ at the mean and $21$ at the median, so the median wins the $L_1$ criterion. The sum of squared deviations is $250$ at the mean and $295$ at the median, so the mean wins the least-squares criterion. Moving $20$ still further moves the mean and leaves the median at $3$ until the extreme point crosses the middle of the ordered sample. That is the small-sample picture of robustness: the median's breakdown happens only when the extreme points become half the sample, while the mean moves as soon as one point moves.{{cite:openintro2019}} (Ch. 2, §2.1.6){{cite:nist_glossary2002}} (Glossary, "robust methods")

Under Gaussian errors, least squares is efficient, and a robust criterion is chosen to stay close to that efficiency while resisting the long tail. Huber loss is built for that compromise. Absolute loss resists gross outliers more strongly and gives up more efficiency when the errors really are Gaussian.{{cite:hastie_esl2009}} (p. 349, §10.6)

## Statistical use — Choosing a summary that matches the tail
Use a median, an interquartile range, or an absolute-deviation fit when a few observations may be misrecorded and the target is the centre of the remaining mass. Use the mean and least squares when the squared loss really is the loss of interest, for example when the total of many units is the quantity to be reported, and when the extremes are genuine rather than mistakes. If a robust regression is fitted, say which loss was minimised. A Huber fit with a large cutoff is least squares. A Huber fit with a small cutoff is close to absolute deviations.{{cite:hastie_esl2009}} (pp. 349–350, §10.6){{cite:dodge2008}} (p. 463, least squares is sensitive to outliers){{cite:openintro2019}} (Ch. 2, §2.1.6, mean versus median for a total)

## Worked example
The sample is $1,2,3,4,20$. The mean is $(1+2+3+4+20)/5=6$ and the median is $3$.

Absolute deviations from $6$ are $5,4,3,2,14$, which add to $28$. Absolute deviations from $3$ are $2,1,0,1,17$, which add to $21$. Squared deviations from $6$ are $25,16,9,4,196$, which add to $250$. Squared deviations from $3$ are $4,1,0,1,289$, which add to $295$.

The least-squares location is $6$ because $250<295$. The least-absolute location is $3$ because $21<28$. Replacing $20$ by $200$ moves the mean to $(1+2+3+4+200)/5=42$ and leaves the median at $3$. One recording error of that size changes the mean by $36$ and the median by nothing.{{cite:dodge2008}} (p. 464, $L_1$ and least squares){{cite:openintro2019}} (Ch. 2, §2.1.6)

**Your turn.** For the sample $5,5,5,5,100$, compute the mean, the median, and the sum of absolute deviations from each.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $120/5=24$ and the median is $5$. Absolute deviations from $24$ are $19$ four times and $76$ once, totalling $152$. Absolute deviations from $5$ total $95$. The median has the smaller absolute-deviation sum.
:::

## Common misconceptions
Robust does not mean unchanged by every kind of data error. A shift that moves every observation, such as a miscalibrated instrument, moves the median by the same amount as the mean. Robustness here is resistance to a small fraction of wild points, not resistance to a systematic shift of the whole sample.{{cite:nist_glossary2002}} (Glossary, "robust methods"){{cite:dodge2008}} (p. 463, outliers and small departures)

The median is not always the better scientific summary. When the question is a total, the mean carries the information and the median throws the large values away. The interest-rate comparison and the loan-amount comparison in the same data set point in different directions for that reason.{{cite:openintro2019}} (Ch. 2, §2.1.6)

A robust loss does not repair a mean function that was the wrong shape. Absolute deviations applied to a straight line still fit a straight line. They change the influence of the points, not the list of curves under consideration.{{cite:hastie_esl2009}} (p. 349, §10.6, the population targets of squared and absolute loss)

## Assumptions and limits — What is being protected
The guarantee is comparative: under contamination of a few points, the robust summary moves less than least squares. It is not a claim that the robust summary equals the population quantity of a model the data do not follow. Huber's cutoff $k$ has to be chosen. Very large $k$ recovers least squares and its sensitivity. Very small $k$ recovers a fit close to absolute deviations and its loss of efficiency on clean Gaussian errors. Outliers in the predictors, as opposed to the response, are a separate problem. A wild $x$ can lever a line even when the loss on $y$ is robust.{{cite:hastie_esl2009}} (p. 349, §10.6){{cite:dodge2008}} (p. 464, the role of $k$)

## Connections
An [outlier](outlier.qmd) is the kind of point robust methods are built to resist. [Least squares](least-squares.qmd) is the non-robust extreme of the same location and regression problem. [Mean squared error](mean-squared-error.qmd) is the risk that least squares minimises, and it is the wrong score if the loss of interest is absolute. The [bias of an estimator](bias-of-an-estimator.qmd) is a different defect: a median can be robust and still be biased for a mean.{{cite:hastie_esl2009}} (p. 349, §10.6){{cite:dodge2008}} (p. 463)

## History
Laplace, in 1818, studied the median in the second supplement to the analytic theory of probability. The word robust, for this resistance to departures from a model, was introduced by Box in 1953 and was in wide use as the name of a field by the middle of the 1960s. Huber's 1964 paper on robust estimation of a location parameter, and the M-estimators built from it, separated the field from ordinary least squares. The Huber loss used in regression is that construction.{{cite:dodge2008}} (pp. 463–464){{cite:hastie_esl2009}} (p. 349, §10.6, Huber, 1964)
