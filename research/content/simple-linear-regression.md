## Lead context
One measured input is used to describe the mean of a numerical response by a straight line, with the line chosen to make the squared vertical errors as small as possible.{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line least squares)

## Motivating example
Five seedlings are grown under 2, 4, 6, 8 and 10 hours of light a day, and their growth is 3, 4, 8, 9 and 11 millimetres. A straight summary is wanted: how many extra millimetres go with one extra hour, in these five pots. The hours were set by the grower, so they are treated as fixed numbers. The growth is the response. A line fitted by least squares answers that slope question inside this sample; it does not by itself say that more light caused the extra growth.{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line model){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, linear in the parameters)

## Intuition
Each candidate line produces a vertical gap between the observed growth and the height of the line at that hour. Squaring those gaps stops positive and negative gaps from cancelling, and it charges a large gap more than a small one. The least-squares line is the line whose squared gaps add to the smallest total. For a straight line the minimiser has a closed form, because the sum of squares is a quadratic function of the intercept and the slope and the critical point is a minimum.{{cite:nist_ls_straight2002}} (§4.4.3.1, criterion $Q$){{cite:dodge2008}} (p. 305, partial derivatives)

The fitted line is a description of the sample. The regression line in the model is the unknown mean, $\mathbb E(Y_i)=\beta_0+\beta_1 x_i$. The two lines meet only by accident. Replacing the unknown mean by the fitted line is estimation, and the size of the gaps that remain is what estimates the noise.{{cite:nist_ls_straight2002}} (§4.4.3.1, estimates versus parameters)

## Definition
With fixed inputs $x_1,\ldots,x_n$, not all equal, and responses $y_1,\ldots,y_n$, the least-squares intercept and slope minimise

$$
Q(b_0,b_1)=\sum_{i=1}^n\bigl(y_i-b_0-b_1 x_i\bigr)^2.
$$

The minimiser is

$$
\hat\beta_1=\frac{\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)}{\sum_{i=1}^n(x_i-\bar x)^2},\qquad
\hat\beta_0=\bar y-\hat\beta_1\bar x.
$$

The same critical-point equations are the normal equations $\sum_i(y_i-\hat\beta_0-\hat\beta_1 x_i)=0$ and $\sum_i x_i(y_i-\hat\beta_0-\hat\beta_1 x_i)=0$.{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line estimators){{cite:dodge2008}} (p. 305, normal equations)

The sampling model writes the responses as random variables $Y_i=\beta_0+\beta_1 x_i+\varepsilon_i$. Least squares estimates $\beta_0$ and $\beta_1$ whether or not the errors are normal. Normality is an extra assumption used when the slope is compared with a $t$ reference law. The residual standard deviation uses the minimised $Q$ and the count of mean parameters. For a straight line that count is $p=2$, so

$$
\hat\sigma=\sqrt{\frac{Q}{n-2}}.
$$

{{cite:nist_ls_straight2002}} (§4.4.3.1, residual standard deviation){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, statistically linear)

## Interpretation
The slope $\hat\beta_1$ is the change in fitted height per unit change in $x$, inside the observed range of $x$. The intercept $\hat\beta_0$ is the fitted height at $x=0$. If $x=0$ is far from the hours that were used, that intercept is an extrapolation, and a shift of the slope moves it. The intercept estimator depends on the slope estimator whenever $\bar x\neq 0$, so a bad slope and a bad intercept travel together. Centring $x$ at $\bar x$ makes the intercept the fitted height at the average input, and that centred intercept is not moved by an error in the slope through the product $\hat\beta_1\bar x$.{{cite:nist_ls_straight2002}} (§4.4.3.1, dependence of the two estimators)

The line always passes through $(\bar x,\bar y)$. In the seedling numbers, $\bar x=6$ and $\bar y=7$, and the fitted height at 6 hours is 7 millimetres. That identity is the first normal equation divided by $n$. It is not a statement that the mean response equals the sample mean of $y$ at every $x$.{{cite:dodge2008}} (p. 305, first normal equation){{cite:nist_ls_straight2002}} (§4.4.3.1, intercept formula)

## Properties
Under the mean model $\mathbb E(Y_i)=\beta_0+\beta_1 x_i$ with fixed $x_i$ not all equal, $\hat\beta_1$ and $\hat\beta_0$ are unbiased for $\beta_1$ and $\beta_0$. The proof uses only that mean. If the errors are also uncorrelated and each has variance $\sigma^2$, then $\operatorname{Var}(\hat\beta_1)=\sigma^2/S_{xx}$ with $S_{xx}=\sum_i(x_i-\bar x)^2$. A larger spread of the inputs makes the slope estimator less variable. If every $x_i$ is the same, $S_{xx}=0$ and the slope formula does not define a line.{{cite:nist_ls_straight2002}} (§4.4.3.1, denominator of the slope)

Replacing $\sigma^2$ by $\hat\sigma^2=Q/(n-2)$ gives the estimated standard error $\hat\sigma/\sqrt{S_{xx}}$. That estimate is a scale for the slope. It is not, by itself, a probability statement: a $t_{n-2}$ reference law needs normal, independent, equal-variance errors as well as the mean model.{{cite:nist_ls_straight2002}} (§4.4.3.1, residual standard deviation)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Differentiate $Q$. The derivatives are $-2\sum_i(y_i-b_0-b_1 x_i)$ and $-2\sum_i x_i(y_i-b_0-b_1 x_i)$. Setting both to zero is the pair of normal equations. The first equation says the residuals sum to zero, hence $\hat\beta_0=\bar y-\hat\beta_1\bar x$, and the fitted line passes through $(\bar x,\bar y)$. Substitute that intercept into the second equation. The cross term with $\bar y$ drops because $\sum_i(x_i-\bar x)=0$, and the slope formula follows.{{cite:dodge2008}} (p. 305, normal equations){{cite:nist_ls_straight2002}} (§4.4.3.1, partial derivatives)

For the mean, write $\hat\beta_1=\sum_i(x_i-\bar x)Y_i/S_{xx}$. Then

$$
\mathbb E(\hat\beta_1)=\sum_i(x_i-\bar x)(\beta_0+\beta_1 x_i)/S_{xx}=\beta_1,
$$

again because the centred inputs sum to zero. The intercept identity then gives $\mathbb E(\hat\beta_0)=\beta_0$. If the $Y_i$ are uncorrelated with variance $\sigma^2$, the variance of the linear combination is $\sigma^2\sum_i(x_i-\bar x)^2/S_{xx}^2=\sigma^2/S_{xx}$.{{cite:nist_ls_straight2002}} (§4.4.3.1, slope estimator)
:::
:::

## Statistical use — Reading a slope inside the observed hours
Quote $\hat\beta_1$ as a change in mean response per unit $x$ for $x$ values inside the range that was observed, and attach $\hat\sigma/\sqrt{S_{xx}}$ as its estimated standard error under equal, uncorrelated error variances. A prediction for a new $Y$ at a new $x$ is wider than a confidence interval for the mean $\beta_0+\beta_1 x$, because the new draw adds one error variance on top of the uncertainty in the fitted line. Outside the observed range the same algebra still prints a number, and that number is an extrapolation whose miss can grow quickly if the mean bends.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, extrapolation and outliers){{cite:nist_ls_straight2002}} (§4.4.3.1, residual standard deviation)

## Worked example
For the five seedlings, $\bar x=6$, $\bar y=7$, $S_{xx}=40$ and $S_{xy}=42$. The slope is $42/40=1.05$ millimetres per hour, and the intercept is $7-1.05\times 6=0.70$. The fitted heights are $2.8$, $4.9$, $7.0$, $9.1$ and $11.2$. The residuals are $0.2$, $-0.9$, $1.0$, $-0.1$ and $-0.2$, and

$$
Q=0.2^2+(-0.9)^2+1^2+(-0.1)^2+(-0.2)^2=1.90.
$$

With $n-2=3$, $\hat\sigma=\sqrt{1.90/3}=\sqrt{19/30}\approx 0.7958$. The estimated standard error of the slope is $\sqrt{(19/30)/40}=\sqrt{19/1200}\approx 0.1258$. At $7$ hours, between the observed inputs, the fitted mean is $0.70+1.05\times 7=8.05$ millimetres.{{cite:nist_ls_straight2002}} (§4.4.3.1, estimators and residual standard deviation)

Replace the last growth $11$ by $20$, as if one pot had been mis-recorded. Then $S_{xy}=78$, the slope becomes $78/40=1.95$, and the intercept becomes $8.8-1.95\times 6=-2.90$. One point moved the slope from $1.05$ to $1.95$. Squared error did what the criterion asks: it chased the large gap.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, sensitivity to outliers)

**Your turn.** For the points $(0,1)$, $(1,3)$ and $(2,2)$, find the least-squares slope and intercept, and the fitted height at the mean of $x$.

::: {.callout-tip collapse="true" title="Answer"}
Here $\bar x=1$, $\bar y=2$, $S_{xx}=2$ and $S_{xy}=1$, so the slope is $1/2=0.5$ and the intercept is $2-0.5\times 1=1.5$. The fitted height at $x=1$ is $2$, the mean of $y$. The residual sum of squares is $1.5$.
:::

## Common misconceptions
The slope is not a causal effect of changing the input. The hours of light were assigned in the seedling story, and even then unmeasured differences among pots can sit in the errors. In an observational series the same algebra produces a slope and does not produce an intervention.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, the fitted line as a description)

Least squares minimises vertical squared gaps, not absolute gaps and not horizontal gaps. Predicting $x$ from $y$ swaps the roles and produces a different line. A model such as $\beta_0+\beta_0\beta_1 x$ is a straight line in $x$ and is not linear in the parameters, so the closed form above does not apply.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, a product of parameters)

The intercept at $x=0$ is not a meaningful growth when the experiment never used zero hours. And a high correlation in the sample is not a licence to extend the line past the largest $x$.{{cite:nist_ls_straight2002}} (§4.4.3.1, intercept depends on the slope){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, extrapolation)

## Assumptions and limits — When the squared-error line misleads
If the inputs are identical, $S_{xx}=0$ and no slope is defined. If the mean response bends, a line can still be the best line and still be a poor description: over a long range a straight line becomes extreme at both ends, because a statistically linear function has no horizontal asymptote. One outlier, as in the change from $11$ to $20$, can move $\hat\beta_1$ from $1.05$ to $1.95$ because the criterion squares that gap. Correlated errors, such as measurements taken in time order on the same plant, leave $\hat\beta_1$ unbiased for a straight mean and make $\sigma^2/S_{xx}$ the wrong variance, because that variance used uncorrelated errors.{{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, long ranges and outliers){{cite:nist_ls_straight2002}} (§4.4.3.1, slope formula)

## Connections
The [least-squares line](least-squares-line.qmd) is this fitted line. A [pivot](pivot.qmd) for the slope appears once normal independent errors supply a $t_{n-2}$ reference law for $(\hat\beta_1-\beta_1)/(\hat\sigma/\sqrt{S_{xx}})$. [Multicollinearity](multicollinearity.qmd) is the matching failure when several inputs are nearly linear combinations of one another, so that the analogue of $S_{xx}$ is nearly singular. [Poisson regression](poisson-regression.qmd) keeps a regression mean and drops both the identity link and the constant variance.{{cite:nist_ls_straight2002}} (§4.4.3.1, straight-line estimators)

## History
The least-squares criterion minimises the sum of squared residuals between observed and fitted values. Legendre introduced the method in 1805. Independent development in the late eighteenth and early nineteenth centuries by Gauss, Legendre, and possibly Adrain. Those two accounts agree that the published early nineteenth-century method is least squares; they do not agree on a single inventor.{{cite:dodge2008}} (p. 304, least-squares method){{cite:nist_linear_least_squares_pmd2002}} (§4.1.4.1, Gauss, Legendre and Adrain)
