## Lead context
When a response falls in one of several unordered categories, each category is compared with one reference category on the log-odds scale, and those comparisons determine every probability.{{cite:r_nnet_multinom2026}} (Details, coefficients zero for the first class)

## Motivating example — Three answers, one reference
A survey records a reply as weak-willed, disease, or both, and those labels have no natural order. A single log-odds, as in a binary logit, cannot carry three probabilities. Choosing weak-willed as the reference leaves two comparisons: disease against weak-willed, and both against weak-willed. The comparison of disease with both is then the difference of those two, so it does not need a third free equation.{{cite:r_nnet_multinom2026}} (Details, a log-linear model with a zero coefficient vector for the first class)

## Intuition
Each free category gets a score. The reference score is set to zero, which removes the fact that adding the same constant to every score does not change the probabilities. Exponentiating the scores and dividing by their total, including the reference score of zero whose exponential is $1$, turns the scores into probabilities. A higher score means a larger share of that total. The share is not the score itself: the denominator moves when any score moves.{{cite:r_nnet_multinom2026}} (Details, baseline class)

## Definition
For categories $0,1,\ldots,K-1$ and a covariate row $\mathbf{x}$, the baseline-category logit model with reference $0$ is
\[
\log\frac{p_k}{p_0}=\eta_k=\beta_{0k}+\mathbf{x}^\top\boldsymbol{\beta}_k,\qquad k=1,\ldots,K-1.
\]
The reference linear predictor is $\eta_0=0$. Solving for the probabilities gives
\[
p_k=\frac{e^{\eta_k}}{\sum_{j=0}^{K-1}e^{\eta_j}},\qquad k=0,\ldots,K-1.
\]
The log-odds of category $k$ against category $m$ are $\eta_k-\eta_m$, with $\eta_0=0$. Software that fits this model by setting the coefficient vector of the first class to zero is using one choice of reference; any other class can be the reference if its score is the one set to zero.{{cite:r_nnet_multinom2026}} (Details, coefficients zero for the first class)

## Interpretation
The coefficient of a covariate in $\eta_k$ is a change in the log-odds of category $k$ against the reference, with the other covariates held fixed. It is not a change in $p_k$ by itself. If that coefficient is $0.5$, the odds against the reference are multiplied by $e^{0.5}\approx 1.6487$ when the covariate increases by one unit. The probability $p_k$ rises only to the extent that this category's share of the renormalised total rises, and a simultaneous change in another category's score can shrink that share again.{{cite:r_nnet_multinom2026}} (Details, log-linear model)

## Properties
The map from scores to probabilities is the softmax of $(\eta_0,\ldots,\eta_{K-1})$. It sends every real score vector to the probability simplex: each $p_k>0$ and the probabilities sum to $1$, as long as every exponential is finite. Adding a constant $c$ to every score multiplies every exponential by $e^c$ and cancels in the ratio, so the probabilities are unchanged. Setting $\eta_0=0$ picks one representative from that family of score vectors. There are $K-1$ free linear predictors, not $K$.{{cite:r_nnet_multinom2026}} (Details, one class has coefficient zero)

The odds ratio between two non-reference categories does not involve the reference level. If $\eta_2-\eta_1=0.5$, then $p_2/p_1=e^{0.5}\approx 1.6487$ whatever $\eta_0$ was, provided the same covariates are being compared. Changing the reference rewrites the coefficients and does not rewrite those pairwise odds.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Set $\eta_0=0$ and $\eta_k=\log(p_k/p_0)$ for $k\ge 1$. Then $p_k=p_0 e^{\eta_k}$. The probabilities sum to one, so $p_0\sum_{j=0}^{K-1}e^{\eta_j}=1$ and $p_0=1/\sum_j e^{\eta_j}$. Multiplying by $e^{\eta_k}$ gives the displayed formula. Each term is positive and the sum of the $p_k$ is one. If every score increases by $c$, the factor $e^c$ appears in every term of the numerator and the denominator and cancels. The log-odds $\log(p_k/p_m)=\eta_k-\eta_m$ follow by dividing the two formulas.{{cite:r_nnet_multinom2026}} (Details, baseline coefficients)
:::
:::

## Statistical use — Reporting a comparison against a named reference
Name the reference category in the same sentence as the coefficient. A coefficient in the disease equation is a comparison with weak-willed, not a comparison with both, until the two equations have been subtracted. With $K$ categories and $p$ covariates plus an intercept, the model has $(K-1)(p+1)$ free coefficients. A binary logit is the case $K=2$, with one equation. Fitting $K$ unrestricted score vectors without a zero constraint fits the same probabilities many times and does not give a unique coefficient vector.{{cite:r_nnet_multinom2026}} (Details, coefficients zero for the first class)

## Worked example
Suppose the reference score is $0$, the score for category $1$ is $0.5$ and the score for category $2$ is $1$. Then $e^{0.5}\approx 1.6487$, $e^{1}\approx 2.7183$, and the denominator is $1+1.6487+2.7183=5.3670$. The probabilities are
\[
p_0=\frac{1}{5.3670}\approx 0.1863,\qquad
p_1=\frac{1.6487}{5.3670}\approx 0.3072,\qquad
p_2=\frac{2.7183}{5.3670}\approx 0.5065.
\]
They sum to $1$. The odds of category $2$ against the reference are $e^{1}\approx 2.7183$. The odds of category $2$ against category $1$ are $e^{1-0.5}=e^{0.5}\approx 1.6487$, which is $0.5065/0.3072$. Adding $1$ to every score leaves these three probabilities unchanged, because every exponential would be multiplied by $e$.{{cite:r_nnet_multinom2026}} (Details, baseline class)

**Your turn.** Set the two free scores to $0$ and $\log 3$, with the reference score still $0$. Find the three probabilities.

::: {.callout-tip collapse="true" title="Answer"}
The exponentials are $1$, $1$ and $3$. The denominator is $5$. The probabilities are $1/5$, $1/5$ and $3/5$, that is $0.2$, $0.2$ and $0.6$.{{cite:r_nnet_multinom2026}} (Details, log-linear probabilities)
:::

## Common misconceptions
The coefficient is not a change in probability. In the worked example the score gap of $1$ produces odds $2.7183$ against the reference, while the probability of category $2$ is $0.5065$, not $2.7183$ and not $1$. A reader who adds the three scores, $0+0.5+1=1.5$, is not looking at a probability.{{cite:r_nnet_multinom2026}} (Details, the model is log-linear in the class indicators)

The categories are not ordered. A baseline logit does not say that category $2$ is twice category $1$ in any scale except the odds against the named reference. Putting the categories on a number line and fitting one slope is a different model, used when the order is real.

Changing which class is called zero changes the printed coefficients and does not change the fitted probabilities. Comparing two fits by their intercepts is meaningless until both fits use the same reference.{{cite:r_nnet_multinom2026}} (Details, which class has coefficient zero)

## Assumptions and limits — When the reference comparison is the wrong summary
The scores are linear in the covariates. A curved effect of age, forced into one coefficient per category, shifts every probability in a straight line on the log-odds scale and can miss a rise-and-fall. Empty categories in a covariate pattern make a sample odds ratio infinite; the probabilities in the formula stay in $(0,1)$ only while the linear predictors stay finite, and a fit that drives a score to $\pm\infty$ is pushing a probability to the boundary rather than reporting a stable odds ratio. The model also treats the categories as a single draw from one multinomial. If the labels were ordered, or if they were several binary responses, this baseline comparison is the wrong likelihood.{{cite:r_nnet_multinom2026}} (Details, counts for each of $K$ classes)

## Connections
A binary [logit link](logit-link.qmd) is this model with two categories. The [softmax](softmax-is-multinomial-logistic-regression.qmd) map is the passage from scores to probabilities written above. [Poisson regression](poisson-regression.qmd) is a different likelihood: counts on an unbounded integer, not a single category out of $K$. The software convention that the first class has coefficient zero is one baseline; the probabilities do not prefer that class.{{cite:r_nnet_multinom2026}} (Details, first class)

## Check yourself

1. If every score increases by $\log 2$, do the probabilities change?

::: {.callout-tip collapse="true" title="Answer"}
No. Every exponential is multiplied by $2$, and the factor cancels in the ratio. The reference score is no longer zero, which is why a fit sets one score back to zero without changing the probabilities.{{cite:r_nnet_multinom2026}} (Details, a zero coefficient vector removes that freedom)
:::

2. In the worked example, what is $p_2/p_1$?

::: {.callout-tip collapse="true" title="Answer"}
The exact probabilities satisfy $p_2/p_1=e^{0.5}\approx 1.6487$. It is the odds of category $2$ against category $1$, not against the reference. The four-decimal probabilities $0.5065$ and $0.3072$ are each rounded, so their ratio is not a second calculation of $e^{0.5}$.{{cite:r_nnet_multinom2026}} (Details, log-linear class comparisons)
:::

3. How many free linear predictors does a four-category model have?

::: {.callout-tip collapse="true" title="Answer"}
Three. One category is the reference and its score is fixed at zero. Four free score vectors would describe the same probabilities more than once.{{cite:r_nnet_multinom2026}} (Details, coefficients zero for the first class)
:::

## History
The parameterisation used by `multinom` fits a log-linear model and sets the coefficient vector of the first class to zero. That software choice is the baseline-category constraint: one class is the reference, and the remaining classes have free scores. The probabilities are the normalised exponentials of those scores. Any other class could have been the one with a zero coefficient vector; the fitted probabilities are what stay fixed when the reference changes.{{cite:r_nnet_multinom2026}} (Description and Details)
