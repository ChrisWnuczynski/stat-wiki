## Lead context
Leave-one-out cross-validation scores each observation with a fit that did not use it, then averages those scores.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 241–243)

## Motivating example
A line fitted to three points looks accurate if one scores it on those same three points. Each point pulled the line toward itself, so the residuals are smaller than the errors the line would make on a new draw at the same $x$. Leaving one point out, refitting, and scoring only that point removes the pull of the point being scored. Doing this once for every point uses the whole sample without scoring a point on a fit that contained it.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.48, pp. 241–243)

## Intuition — Almost the same training set, every time
With $n$ observations the $i$th training set has size $n-1$. The fit being assessed is therefore close, in training size, to the fit one will eventually compute on all $n$ points. That is why the leave-one-out estimate has little bias from using a smaller training set, relative to five- or ten-fold cross-validation. The cost is dependence and computation. Two training sets of size $n-1$ share $n-2$ observations, so the $n$ held-out errors are not $n$ independent experiments. A binomial standard error that treats them as independent coin tosses overstates how much fresh information the average contains. The procedure also refits the model $n$ times, unless the fitting method has an algebraic shortcut.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–244)

## Definition
Let $\kappa(i)=i$ and let $\hat f^{-i}$ be the fit computed with observation $i$ removed. For a loss $L$, the leave-one-out estimate of prediction error is
$$
\mathrm{CV}=\frac1n\sum_{i=1}^{n} L\bigl(y_i,\hat f^{-i}(x_i)\bigr).
$$
This is $K$-fold cross-validation with $K=n$. It estimates the expected extra-sample error, the average loss on a new pair $(X,Y)$ drawn from the same joint distribution, not a posterior probability that the fitted function is correct. When a tuning constant is chosen by minimising this average, the minimised value is a score of the search as well as of the fit, and a separate outer assessment is required before that minimum is reported as a test error.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.48–7.49, pp. 241–243)

## Properties — Linear fits need only the full-sample residuals
If the fitted values from a linear method are $\hat y=Sy$ with $S$ not depending on $y$, the leave-one-out residual at $i$ equals the ordinary residual divided by $1-S_{ii}$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $\hat y^{-i}_i$ for the prediction at $x_i$ from the fit that excludes observation $i$. Consider a modified response vector $y^{\ast}$ that agrees with $y$ except at coordinate $i$, where $y^{\ast}_i=\hat y^{-i}_i$. Refitting on $y^{\ast}$ does not move the prediction at $i$, because that observation is now fit perfectly by a value the leave-one-out fit already predicted, so the $i$th fitted value on $y^{\ast}$ is still $\hat y^{-i}_i$. Linearity gives $\hat y^{\ast}-\hat y=S(y^{\ast}-y)$. The only nonzero entry of $y^{\ast}-y$ is $\hat y^{-i}_i-y_i$ in position $i$, and the $i$th coordinate of the display is
$$
\hat y^{-i}_i-\hat y_i=S_{ii}(\hat y^{-i}_i-y_i).
$$
Rearrangement yields $y_i-\hat y^{-i}_i=(y_i-\hat y_i)/(1-S_{ii})$, provided $S_{ii}\ne 1$. For ordinary least squares, $S$ is the hat matrix and $S_{ii}$ is the leverage of row $i$.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.51, p. 244)
:::
:::

Replacing each $S_{ii}$ by $\operatorname{tr}(S)/n$ produces generalised cross-validation, a cheaper approximation when the trace is easier to obtain than the separate diagonal entries. The approximation $1/(1-x)^{2}\approx 1+2x$ also shows why that trace penalty resembles an Akaike correction, but the exact leave-one-out identity uses the separate leverages.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.52, pp. 244–245)

## Statistical use — Score a fixed rule, or isolate the tuning
Use the average above when the fitting rule, including any preprocessing and any tuning constant, is already fixed. Standardising the predictors, choosing a penalty, or screening variables has to happen inside each leave-one-out fit. If those choices see the held-out response, the score is no longer the error of a rule applied to new data. Five- or ten-fold splits are often preferred when $n$ is large or the learning curve is still steep at size $n-1$, because they cost fewer refits and their training sets differ more. Leave-one-out remains the relevant check when an exact linear identity is available, or when the scientific comparison is specifically about training sets of size $n-1$.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1–7.10.2, pp. 242–246)

## Worked example
Fit a straight line by least squares to the three pairs $(x,y)=(1,1)$, $(2,2)$ and $(3,6)$. The design matrix with a column of ones has hat-matrix diagonal $(5/6,\ 1/3,\ 5/6)$, and the fitted line is $\hat y=-2+2.5x$. The fitted values are $0.5$, $3$ and $5.5$, so the ordinary residuals are $0.5$, $-1$ and $0.5$. Dividing by one minus the leverage gives the leave-one-out residuals
$$
\frac{0.5}{1-5/6}=3,\qquad \frac{-1}{1-1/3}=-1.5,\qquad \frac{0.5}{1-5/6}=3.
$$
The leave-one-out predictions are therefore $-2$, $3.5$ and $3$, and the mean squared leave-one-out error is $(9+2.25+9)/3=6.75$. Refitting on each pair of points reproduces the same three predictions, which is the identity rather than a second experiment. The mean squared residual of the full-sample fit is $(0.25+1+0.25)/3=0.5$, much smaller than $6.75$, because each point was allowed to influence the line that was then scored on it.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.51, p. 244)

**Your turn.** Suppose a fourth linear fit, not these data, has ordinary residual $0.4$ and leverage $0.2$ at one case. What is the leave-one-out residual at that case, and what goes wrong if the leverage equals $1$?

::: {.callout-tip collapse="true" title="Answer"}
The leave-one-out residual is $0.4/(1-0.2)=0.5$. If the leverage is $1$, the case lies in the column space in a way that forces a zero residual in every fit that includes it, and the division by $1-S_{ii}$ is undefined. The identity does not supply a leave-one-out score for that case.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.51, p. 244)
:::

## Common misconceptions
The $n$ leave-one-out errors are not independent Bernoulli trials, even when the loss is zero–one. Neighbouring training sets share almost every observation. A small leave-one-out average is not the error of a procedure that was allowed to pick the tuning constant with the smallest average: the minimum over several constants is an optimistic report of the search. Leave-one-out is not automatically more accurate than ten-fold cross-validation. It is nearly unbiased for the expected prediction error and can be highly variable, because the $n$ training sets are so similar.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–244)

The shortcut $e_i/(1-S_{ii})$ is for linear fitting methods, those with $\hat y=Sy$ and $S$ free of $y$. A tree, a nearest-neighbour rule, or a neural network refit does not inherit that one-line formula.

## Assumptions and limits — When the shortcut and the average both mislead
If standardisation, a variable screen, or a penalty is computed on all $n$ rows and only then a leave-one-out loop is run, the held-out row has already affected the fit. Hastie, Tibshirani and Friedman illustrate the scale of that mistake with a classification screen: predictors chosen using every label, followed by cross-validation, produced a very small cross-validated error in a problem whose true error was one half. The algebra of $S_{ii}$ cannot repair a matrix $S$ that was built with the held-out labels.{{cite:hastie_esl2009}} (Ch. 7, §7.10.2, pp. 245–246)

A second limit is leverage. A point with $S_{ii}$ near $1$ dominates the fit. Its ordinary residual is near $0$, and the leave-one-out residual inflates sharply. That inflation is the right warning that the point was not being predicted so much as being interpolated. Dropping the case and quoting only the ordinary residual hides it.

## Connections
[Cross-validation](cross-validation.qmd) is the $K$-fold procedure of which leave-one-out is the case $K=n$. [Nested cross-validation](nested-cross-validation.qmd) puts a search over tuning constants inside an outer split, so that the reported error is not the minimum that chose the constant. The [jackknife](jackknife.qmd) also drops one observation at a time, but it targets the bias and variance of an estimator rather than the prediction error of a fitted rule. For linear smoothers, generalised cross-validation replaces the separate leverages by their average, $\operatorname{tr}(S)/n$.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.51–7.52, pp. 244–245)

## Check yourself
### One leverage {#self-check-loo-leverage}

A least-squares fit has ordinary residual $-0.3$ and leverage $1/4$ at a case. Find the leave-one-out residual.

::: {.callout-tip collapse="true" title="Answer"}
Divide by $1-1/4=3/4$. The leave-one-out residual is $-0.3/(3/4)=-0.4$.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, eq. 7.51, p. 244)
:::

### Training residual against leave-one-out {#self-check-loo-compare}

In the three-point line, the mean squared ordinary residual is $0.5$ and the mean squared leave-one-out error is $6.75$. Why is the second number the one that estimates prediction error?

::: {.callout-tip collapse="true" title="Answer"}
Each ordinary residual scores a point on a line that used that point. Each leave-one-out residual scores the point on the line fitted to the other two. The average of those three squared residuals estimates the expected squared error of the fitting rule on a new case. The ordinary residual average estimates how well the line interpolates its own sample.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 241–244)
:::

### A shared training set {#self-check-loo-dependence}

Two leave-one-out training sets from a sample of size $20$ each omit a different row. How many training rows do they share, and why does that block a binomial standard error for the average of the $20$ errors?

::: {.callout-tip collapse="true" title="Answer"}
They share $18$ rows. The $20$ held-out errors are functions of heavily overlapping fits, so they are dependent. A binomial variance $p(1-p)/20$ would treat them as independent indicators and would overstate the precision of the average.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 242–244)
:::

## History
Stone’s cross-validatory assessment and the later synthesis in Hastie, Tibshirani and Friedman both treat the case $K=n$ as the extreme split: each fit drops a single case, the bias from the reduced training size is small, and the dependence among the fits is large. The linear-smoother identity that turns the full-sample residuals into leave-one-out residuals is recorded with that synthesis, together with the trace approximation that became generalised cross-validation.{{cite:hastie_esl2009}} (Ch. 7, §7.10.1, pp. 241–245)
