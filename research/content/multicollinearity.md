## Lead context
Multicollinearity is the near-linear dependence of regression predictors on one another, and it inflates the variance of the least-squares slopes that try to separate those predictors.{{cite:dodge2008}} (p. 96, statistical collinearity){{cite:james_islr2013}} (§3.3.3, pp. 99–101, collinearity and coefficient uncertainty)

## Motivating example
Five units have inputs $x_1=(1,2,3,4,5)$ and $x_2=(2,4,5,8,11)$. The second list is almost twice the first: the straight copy would have been $(2,4,6,8,10)$. The third and fifth entries have been nudged, by $-1$ and $+1$. A response that moves with either list can be credited to $x_1$, to $x_2$, or to any mixture of the two. Least squares will pick one mixture. A small change in the data can pick a very different mixture, because the two columns carry almost the same information.{{cite:dodge2008}} (p. 362, a variable almost equal to a linear combination of the others){{cite:james_islr2013}} (§3.3.3, p. 100, discussion of coefficient sensitivity)

## Intuition
Exact collinearity means one predictor is a linear combination of the others. The projection $P_{\operatorname{col}(X)}y$ always exists, and the normal equations $X^\top Xb=X^\top y$ are always consistent. With exact rank deficiency, adding any nonzero vector in the kernel of $X$ to one coefficient solution gives another solution. There are infinitely many coefficient vectors, but their fitted values equal the same projection.{{cite:mit_1806_least_squares2022}} (Problem 2 and Solution 2, normal-equation consistency and uniqueness of the projection) Statistical collinearity, or multicollinearity, is the approximate version: one predictor is nearly that linear combination. A coefficient vector still exists, and its sampling variance is large, because the design has little variation in the direction that separates the predictors.{{cite:dodge2008}} (p. 96, mathematical and statistical collinearity)

The variance inflation factor makes that comparison numerical. For two centred predictors with correlation $r$, the variance of each multiple-regression slope is $1/(1-r^2)$ times the variance that slope would have in a simple regression on the same predictor. The factor depends on the correlation of the predictors, not on the response.{{cite:james_islr2013}} (§3.3.3, pp. 101–102, definition and formula for the variance inflation factor)

## Definition
In a regression with an intercept and two predictors, centre the predictors and write $S_{11}=\sum_i(x_{i1}-\bar x_1)^2$, and likewise $S_{22}$ and $S_{12}$. The correlation of the two predictors in the sample is $r=S_{12}/\sqrt{S_{11}S_{22}}$. The least-squares slopes solve

$$
\begin{pmatrix}S_{11}&S_{12}\\ S_{12}&S_{22}\end{pmatrix}
\begin{pmatrix}b_1\\ b_2\end{pmatrix}
=
\begin{pmatrix}S_{1y}\\ S_{2y}\end{pmatrix}.
$$

The determinant is $S_{11}S_{22}(1-r^2)$. It is zero when $|r|=1$, and the slopes are then not unique. When $|r|<1$ the variance of $b_1$, under uncorrelated errors of variance $\sigma^2$, is $\sigma^2/(S_{11}(1-r^2))$. The ratio of that variance to the simple-regression variance $\sigma^2/S_{11}$ is the variance inflation factor $1/(1-r^2)$.{{cite:dodge2008}} (p. 96, considerable variance of the estimators)

## Interpretation
A variance inflation factor of $1$ is an uncorrelated pair of predictors. A factor of $31.25$, as in the worked example, means the slope's sampling variance is $31.25$ times the simple-regression variance on the same $x_1$ column. The standard error is multiplied by $\sqrt{31.25}=5.590$. The point estimate can still be computed. The interval around it is wide because the data barely separate $x_1$ from $x_2$.{{cite:dodge2008}} (p. 362, strong correlation between explanatory variables){{cite:james_islr2013}} (§3.3.3, pp. 101–102, variance inflation and standard errors)

The multiple-regression slope is a partial slope: the change in fitted mean per unit of $x_1$ with $x_2$ held fixed. If the sample never holds $x_2$ fixed while $x_1$ moves, that partial slope is an extrapolation off the line the points actually occupy. A large inflation factor is a warning about that extrapolation.

## Properties
The inflation factor depends only on $r$. It is the same number for $b_1$ and for $b_2$ in the two-predictor model, because $1-r^2$ is symmetric. It does not depend on $\sigma^2$ or on $y$. Scaling a predictor changes $S_{11}$ and the simple-regression variance together, and the ratio is unchanged. Replacing $r$ by $-r$ leaves the factor unchanged: opposition inflates variances in the same way as agreement.

If $|r|=1$ the factor is infinite and the matrix is singular. That boundary is the distinction. Mathematical collinearity makes the least-squares estimator undefined as a unique vector. Statistical collinearity leaves it defined and makes it variable.{{cite:dodge2008}} (p. 96, impossible to define the estimators, or considerable variance)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Centre the predictors, so the intercept separates and the slope block is the $2\times 2$ matrix above. Its determinant is $S_{11}S_{22}-S_{12}^2=S_{11}S_{22}(1-r^2)$. The inverse has $S_{22}/\det$ in the $(1,1)$ position, hence

$$
\operatorname{Var}(b_1)=\sigma^2\frac{S_{22}}{S_{11}S_{22}(1-r^2)}=\frac{\sigma^2}{S_{11}(1-r^2)}
$$

when the errors are uncorrelated with variance $\sigma^2$. Dividing by the simple-regression variance $\sigma^2/S_{11}$ leaves $1/(1-r^2)$. The same algebra with the indices swapped gives the factor for $b_2$. When $r^2=1$ the determinant is zero and the normal equations do not have a unique solution.{{cite:dodge2008}} (p. 96, linear combination and approximate linear combination)
:::
:::

## Statistical use — When a wide interval is the design
Compute $r$, or the inflation factor, before reading a partial slope as a separate effect. If the scientific question is the joint movement of two predictors that always travel together, the partial slope is not the contrast the sample contains, and a wide interval is the honest summary. If the question really is the partial slope, the design has to move one predictor while the other stays put. Collecting more rows of the same nearly proportional pairs increases $S_{11}$ and does not by itself shrink $1/(1-r^2)$.{{cite:dodge2008}} (p. 362, regression problems with strongly correlated explanatory variables)

The factor $1/(1-r^2)$ is for two predictors and an intercept, with the variance formula that assumes uncorrelated equal-variance errors. Correlated errors change $\operatorname{Var}(b_1)$ by a matrix that this scalar does not capture. Three predictors can be jointly collinear with every pairwise correlation moderate; the two-predictor formula does not see that.{{cite:james_islr2013}} (§3.3.3, p. 101, multicollinearity beyond pairwise correlations) And an inflation factor describes the variance of the least-squares slopes. It does not say whether the mean is linear, whether a point is an outlier, or whether $x_1$ was assigned independently of $x_2$.{{cite:dodge2008}} (p. 96, the regression setting of the definition)

## Worked example
For $x_1=(1,2,3,4,5)$ and $x_2=(2,4,5,8,11)$, the means are $3$ and $6$, $S_{11}=10$, $S_{22}=50$ and $S_{12}=22$. Then

$$
r^2=\frac{22^2}{10\times 50}=\frac{484}{500}=0.968,\qquad r=\frac{22}{\sqrt{500}}\approx 0.9839,
$$

and the inflation factor is $1/0.032=31.25$. With responses $y=(1,2,1,3,4)$, the simple slope of $y$ on $x_1$ is $7/10=0.7$. The multiple-regression slopes are $b_1=-1.5$ and $b_2=1$. The partial slope on $x_1$ has the opposite sign from the simple slope, because $x_2$ has absorbed the shared rise and the residual contrast points the other way. The determinant of the slope matrix is $500-484=16$, so a unique solution exists. Replace $x_2$ by the exact copy $(2,4,6,8,10)$. Then $S_{12}=20$, $S_{22}=40$ and the determinant is $10\times 40-20^2=0$. No unique least-squares pair $(b_1,b_2)$ exists.{{cite:dodge2008}} (pp. 96, 362)

**Your turn.** If two centred predictors have correlation $0.6$, what is the variance inflation factor?

::: {.callout-tip collapse="true" title="Answer"}
$1/(1-0.36)=1/0.64=1.5625$. Each partial slope has sampling variance $1.5625$ times the simple-regression variance on the same column.
:::

## Common misconceptions
A large correlation of a predictor with the response is not multicollinearity. Multicollinearity is a relation among the predictors. A predictor can be weakly related to $y$ and still be almost a copy of another predictor.{{cite:dodge2008}} (p. 96, explanatory variables){{cite:james_islr2013}} (§3.3.3, p. 99, collinearity among predictors)

The partial slope is not the simple slope. In the example the simple slope is $0.7$ and the partial slope is $-1.5$. Quoting $0.7$ as the effect of $x_1$ after adjusting for $x_2$ uses the regression that did not adjust.{{cite:dodge2008}} (p. 362, regression)

A finite inflation factor is not a unique substantive decomposition. The fit with $b_1=-1.5$ and $b_2=1$ is the least-squares fit. A ridge penalty, or a decision to drop one predictor, is a different estimator. The singular copy of the design shows the boundary where even least squares stops returning one vector.{{cite:dodge2008}} (p. 96, the exact case)

## Connections
[Simple linear regression](simple-linear-regression.qmd) is the one-predictor case, where there is no second column to be collinear with and the inflation factor is $1$. The [least-squares line](least-squares-line.qmd) is that fit. Exact collinearity is the singular end of the same normal equations. A penalty that shrinks slopes, such as a ridge penalty, changes the estimator; it is not the least-squares solution whose variance the factor describes.{{cite:dodge2008}} (p. 96, least squares under collinearity)

## History
Mathematical collinearity is an exact linear combination, statistical collinearity is an approximate one, and multicollinearity is the name for the strong-correlation case in a regression. The exact case leaves least-squares estimators undefined as a unique solution. The approximate case leaves them defined and able to show considerable variance. A separate entry repeats the approximate definition: a variable almost equal to a linear combination of the others, sometimes met when explanatory variables are strongly correlated.{{cite:dodge2008}} (pp. 96, 362)
