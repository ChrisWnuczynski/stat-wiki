## Lead context

A summary or a fit is robust when a small fraction of the data, moved a long way, does not move the answer very much. The median is the standard case. The arithmetic mean is not. Extreme changes to a small portion of the observations leave a robust method nearly where it was, and they pull a least-squares method with them.{{cite:nist_glossary2002}} (Glossary, "robust methods"){{cite:openintro2019}} (Ch. 2, §2.1.6)

## Motivating example

Five interest rates sit near 10%, and one loan is recorded at 26.3%. Replacing that one rate by 15%, or by 35%, leaves the median and the interquartile range where they were and shifts the mean and the standard deviation. In the published comparison the median stays at 9.93% and the interquartile range stays at 5.76 percentage points, while the mean moves from 11.57% to 11.34% or to 11.74% and the standard deviation moves from 5.05 to 4.61 or to 5.68. The two robust summaries describe the centre and the spread of the bulk of the loans. The mean describes a centre that has been pulled toward the extreme loan. Which description is wanted depends on the question. A typical loan is closer to the median. A total amount of money, added up across many loans, follows the mean.{{cite:openintro2019}} (Ch. 2, §2.1.6)

## Intuition

Squared error charges a residual of size 10 as 100, and a residual of size 1 as 1. A single wild point can therefore dominate the fit. Absolute error charges that residual as 10, in proportion to its size. Huber's loss uses the square while the residual is smaller than a chosen cutoff and then switches to a straight line, so ordinary points keep the efficiency of least squares and gross points lose their squared leverage. The population version of the same idea picks the conditional mean under squared error and the conditional median under absolute error. On a symmetric error law those two targets agree. On a long-tailed law, or in a sample with a misrecorded response, they do not.{{cite:hastie_esl2009}} (pp. 349–350, §10.6, squared error, absolute error, and Huber loss){{cite:dodge2008}} (p. 464, replacing the square by a function δ)

## Definition

A statistical method is robust when extreme changes to a small portion of the data do not change its answer strongly. An estimator of a regression coefficient, or of a location, is robust in the same sense when it is not sensitive to outliers or to small departures from the model that was written down. The arithmetic mean and other least-squares estimators are sensitive to outliers of that kind. The term for this resistance was introduced by Box in 1953, and the subject was recognised as a field by the middle of the 1960s. Laplace had already studied the distribution of the median in 1818, in the second supplement to the analytic theory of probability. Huber's 1964 paper on robust estimation of a location parameter separated the later M-estimators from ordinary least squares.{{cite:nist_glossary2002}} (Glossary, "robust methods"){{cite:dodge2008}} (pp. 463–464)

For a location $t$ and observations $y_1,\ldots,y_n$, least squares minimises $\sum_i(y_i-t)^2$ and returns the sample mean. Least absolute deviations minimises $\sum_i|y_i-t|$ and returns a sample median. An M-estimator replaces the square by a symmetric function $\delta$ with a unique minimum at zero, and minimises $\sum_i\delta(y_i-t)$. Huber's choice, for a positive cutoff $k$, is the square $x^2/2$ when $|x|\le k$ and the line $k|x|-k^2/2$ when $|x|>k$. The absolute-deviation estimator is the special case of a pure line, $\delta(x)=|x|$.{{cite:dodge2008}} (p. 464){{cite:hastie_esl2009}} (p. 349, §10.6, equation (10.23))

In regression the same replacement is made inside the loss $L(y,f(x))$. Squared error, absolute error, and Huber loss are three such choices. The fitted function changes with the loss. Huber's regression form is $(y-f(x))^2$ while $|y-f(x)|\le\delta$, and $2\delta|y-f(x)|-\delta^2$ otherwise.{{cite:hastie_esl2009}} (pp. 349–350, §10.6)

## Properties

Write the sum of squared deviations from a candidate location $t$ as the quadratic

$$
S(t)=\sum_{i=1}^{n}(y_i-t)^2=\sum_{i=1}^{n}y_i^2-2t\sum_{i=1}^{n}y_i+nt^2.
$$


Its derivative is $S'(t)=-2\sum_i y_i+2nt=2n(t-\bar y)$, which is zero only at the sample mean $\bar y$. The second derivative is $2n>0$, so that critical point is a minimum. The mean is the least-squares location because it is the unique minimiser of this quadratic.

On the five numbers $1,2,3,4,20$ the mean is $6$ and the median is $3$. Here $\sum y_i=30$ and $\sum y_i^2=430$, so

$$
S(t)=430-60t+5t^2,\qquad S'(t)=10(t-6).
$$


The derivative vanishes at $6$. Direct evaluation gives $S(6)=250$, $S(5)=255$ and $S(7)=255$. Moving one unit away from the mean raises the sum of squares by $5$, which is the comparison that illustrates the identity just proved. The same quadratic at the median is $S(3)=295$. The sum of absolute deviations is $28$ at the mean and $21$ at the median, so the median wins the $L_1$ criterion and the mean wins least squares. Moving $20$ still further moves the mean and leaves the median at $3$ until the extreme point crosses the middle of the ordered sample. That is the small-sample picture of robustness: the median's breakdown happens only when the extreme points become half the sample, while the mean moves as soon as one point moves.{{cite:openintro2019}} (Ch. 2, §2.1.6){{cite:nist_glossary2002}} (Glossary, "robust methods"){{cite:dodge2008}} (p. 464)

Under Gaussian errors, least squares is efficient, and a robust criterion is chosen to stay close to that efficiency while resisting the long tail. Huber loss is built for that compromise. Absolute loss resists gross outliers more strongly and gives up more efficiency when the errors really are Gaussian.{{cite:hastie_esl2009}} (p. 349, §10.6)

A median, an interquartile range, or an absolute-deviation fit is the summary to use when a few observations may be misrecorded and the target is the centre of the remaining mass. The mean and least squares are the summary to use when the squared loss really is the loss of interest, for example when the total of many units is the quantity to be reported, and when the extremes are genuine rather than mistakes. If a robust regression is fitted, the loss has to be named. A Huber fit with a large cutoff is least squares. A Huber fit with a small cutoff is close to absolute deviations.{{cite:hastie_esl2009}} (pp. 349–350, §10.6){{cite:dodge2008}} (p. 463, least squares is sensitive to outliers){{cite:openintro2019}} (Ch. 2, §2.1.6, mean versus median for a total)

## Worked example

The sample is $1,2,3,4,20$. The mean is $(1+2+3+4+20)/5=6$ and the median is $3$.

The squared-error sum is the quadratic $S(t)=430-60t+5t^2$. Then $S'(t)=10(t-6)$, so the critical point is $t=6$. Squared deviations from $6$ are $25,16,9,4,196$, which add to $250$. Squared deviations from the neighbours $5$ and $7$ add to $255$ and $255$. Squared deviations from the median $3$ are $4,1,0,1,289$, which add to $295$. The neighbour comparison illustrates the derivative calculation: the sum of squares is smaller at the mean than one unit away. Absolute deviations from $6$ are $5,4,3,2,14$, which add to $28$. Absolute deviations from $3$ are $2,1,0,1,17$, which add to $21$. The least-absolute location is $3$ because that sum is the smaller of the two absolute-deviation sums. Replacing $20$ by $200$ moves the mean to $(1+2+3+4+200)/5=42$ and leaves the median at $3$. One recording error of that size changes the mean by $36$ and the median by nothing.{{cite:dodge2008}} (p. 464, $L_1$ and least squares){{cite:openintro2019}} (Ch. 2, §2.1.6)

**Your turn.** For the sample $5,5,5,5,100$, compute the mean, the median, and the sum of absolute deviations from each.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $120/5=24$ and the median is $5$. Absolute deviations from $24$ are $19$ four times and $76$ once, totalling $152$. Absolute deviations from $5$ total $95$. The median has the smaller absolute-deviation sum.
:::

## Assumptions and limits

The guarantee is comparative: under contamination of a few points, the robust summary moves less than least squares. Equality with the population quantity of a model the data do not follow is a separate requirement, and robustness does not supply it. Huber's cutoff $k$ has to be chosen. Very large $k$ recovers least squares and its sensitivity. Very small $k$ recovers a fit close to absolute deviations and its loss of efficiency on clean Gaussian errors. A shift that moves every observation, such as a miscalibrated instrument, moves the median by the same amount as the mean. Robustness here is resistance to a small fraction of wild points. Outliers in the predictors, as opposed to the response, are a separate problem. A wild $x$ can lever a line even when the loss on $y$ is robust. Absolute deviations applied to a straight line still fit a straight line. They change the influence of the points, not the list of curves under consideration.{{cite:hastie_esl2009}} (p. 349, §10.6){{cite:dodge2008}} (pp. 463–464, the role of $k$, and outliers){{cite:nist_glossary2002}} (Glossary, "robust methods")

## Connections

An [outlier](outlier.qmd) is the kind of point robust methods are built to resist. [Least squares](least-squares.qmd) is the non-robust extreme of the same location and regression problem, and it is the procedure whose criterion $S(t)$ is minimised at the mean. [Mean squared error](mean-squared-error.qmd) is the risk that least squares minimises, and it is the wrong score if the loss of interest is absolute. The [bias of an estimator](bias-of-an-estimator.qmd) is a different defect: a median can be robust and still be biased for a mean. When the question is a total, the mean carries the information and the median throws the large values away. The interest-rate comparison and the loan-amount comparison in the same data set point in different directions for that reason.{{cite:hastie_esl2009}} (p. 349, §10.6){{cite:dodge2008}} (p. 463){{cite:openintro2019}} (Ch. 2, §2.1.6)
