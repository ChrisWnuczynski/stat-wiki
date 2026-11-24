## Lead context
The Cauchy–Schwarz inequality says that the inner product of two vectors cannot exceed the product of their lengths, and the same bound limits the covariance of two random variables.

## Motivating example
Two examination marks for the same students can move together, but not more tightly than a straight line allows. If $X$ is the first mark and $Y$ the second, the correlation is the covariance divided by the product of the standard deviations. That quotient cannot fall outside $[-1,1]$. The obstruction is Cauchy–Schwarz applied to the centred marks: the squared covariance cannot exceed the product of the variances. A computed correlation of 1.2 is not a surprising data set. It is an arithmetic error.{{cite:durrett2019}} (p. 26, Cauchy–Schwarz as the case $p=q=2$ of Hölder)

## Intuition
For ordinary vectors, the inner product is a length times a length times the cosine of the angle between them, and a cosine is at most 1. The inequality $|x^\top y|\le\|x\|\,\|y\|$ is that fact without naming the cosine. For random variables the "vectors" are the variables themselves, the inner product is $\E(XY)$, and the length is $\sqrt{\E X^2}$. Equality holds when the two variables are proportional, the probabilistic version of pointing in the same direction. Centring the variables replaces $\E(XY)$ by the covariance and $\E X^2$ by the variance, which is why the correlation is the cosine of that angle.{{cite:durrett2019}} (p. 26, quadratic proof of Cauchy–Schwarz){{cite:dodge2008}} (p. 378, the absolute inner product is at most the product of the norms)

## Definition
Durrett records Cauchy–Schwarz as the case $p=q=2$ of Hölder's inequality: if $X$ and $Y$ are square-integrable, then
$$
\bigl(\E|XY|\bigr)^2\le\E(X^2)\,\E(Y^2).
$$
The displayed bound is the absolute-product form. The signed form $(\E XY)^2\le\E(X^2)\,\E(Y^2)$ holds too, but the two forms have different equality cases, set out in the Interpretation below. The vector form is: for vectors $x$ and $y$, $|x^\top y|\le\|x\|\,\|y\|$, where $\|x\|=\sqrt{x^\top x}$. Applied to the centred variables $X-\E X$ and $Y-\E Y$, the random-variable form becomes
$$
\bigl(\Cov(X,Y)\bigr)^2\le\Var(X)\Var(Y),
$$
whenever those variances are finite. If both variances are positive, dividing gives $|\rho(X,Y)|\le 1$.{{cite:durrett2019}} (p. 26, Remark after Hölder's inequality){{cite:dodge2008}} (p. 378, Cauchy–Schwarz inequality)

## Interpretation — What equality is saying
For the signed form, equality holds when one variable is a scalar multiple of the other, almost surely. For the absolute-product form displayed in the Definition, equality holds when $|X|$ and $|Y|$ are proportional almost surely, with no condition on how their signs are related. The distinction needs both second moments positive: if one variable is zero almost surely, both forms hold with equality trivially, but a zero variance does not define a correlation. For centred variables, proportionality means $Y-\E Y=c(X-\E X)$ almost surely, so the pair sits on a straight line. A correlation of exactly 1 is that line with positive slope. A correlation of exactly $-1$ is the line with negative slope. A correlation of 0 is not independence. It is the absence of a linear association. The variables $X$ uniform on $\{-1,0,1\}$ and $Y=X^2$ have covariance 0, because $XY=X^3=X$ and $\E X=0$, while $Y$ is a function of $X$. Cauchy–Schwarz is silent about that curved dependence. It only caps the linear one.{{cite:durrett2019}} (p. 26, the quadratic touches zero at one root when equality holds)

## Properties — The covariance bound and the vector norm
The vector $(12,15,16)$ has squared length $144+225+256=625$ and length $\sqrt{625}=25$. Its inner product with the unit vector $(0.48,0.60,0.64)$ is $12\times0.48+15\times0.60+16\times0.64=5.76+9+10.24=25$, which equals the product of the lengths $25\times1$. The two vectors are parallel: the second is the first divided by 25. A second vector that is not parallel falls strictly inside the bound. For $(12,15,16)$ and $(1,0,0)$ the inner product is 12 and the product of lengths is $25\times1=25$, and $12<25$.

For random variables with finite positive variances the same arithmetic gives $|\Cov(X,Y)|\le\sqrt{\Var(X)\Var(Y)}$. The sample correlation of a data set is the correlation of a discrete random variable that picks a row uniformly, so the same ceiling applies to the sample correlation. A sample correlation outside $[-1,1]$ does not need a statistical explanation.{{cite:dodge2008}} (p. 378, worked norm of $(12,15,16)$){{cite:durrett2019}} (p. 26, Cauchy–Schwarz)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For any real $\theta$,
$$
0\le\E(X+\theta Y)^2=\E X^2+2\theta\E(XY)+\theta^2\E Y^2,
$$
provided the second moments exist. The right-hand side is a quadratic $a\theta^2+b\theta+c$ with $a=\E Y^2$, $b=2\E(XY)$ and $c=\E X^2$. A quadratic that never goes negative has discriminant $b^2-4ac\le0$, so
$$
4\bigl(\E(XY)\bigr)^2-4\E(X^2)\E(Y^2)\le0.
$$
That is Cauchy–Schwarz. The same quadratic argument applied to $|X|$ and $|Y|$ instead of $X$ and $Y$ gives the displayed absolute-product form $(\E|XY|)^2\le\E(X^2)\,\E(Y^2)$, because $|X|^2=X^2$ and $|XY|=|X|\,|Y|$. If $\E Y^2=0$ then $Y=0$ almost surely and both sides are zero. If $\E Y^2>0$, equality holds when the quadratic touches zero, hence when $X+\theta Y=0$ almost surely for $\theta=-b/(2a)$, so $X$ is a multiple of $Y$.

Replace $X$ and $Y$ by $X-\E X$ and $Y-\E Y$. The cross term becomes the covariance and the squared lengths become the variances. If either variance is zero the covariance is zero as well, because a constant has covariance zero with every variable.{{cite:durrett2019}} (p. 26, discriminant of the quadratic)
:::
:::

## Statistical use — Where the bound is the result
The correlation is defined only when both variances are positive, and Cauchy–Schwarz is the reason the definition lands in $[-1,1]$. In a regression, the residual variance is $\Var(Y)(1-\rho^2)$ for a best linear predictor, which is non-negative precisely because $\rho^2\le1$. In the Cramér–Rao argument the covariance between an estimator and the score is bounded by the product of their standard deviations, and rearranging produces the lower bound on the variance of an unbiased estimator. Equality is the case in which the estimator is an affine function of the score. The inequality does not, by itself, say that any particular estimator attains the bound.{{cite:durrett2019}} (p. 26, equality when the variables are proportional)

If $\E X^2$ is infinite, the statement $(\E|XY|)^2\le\E(X^2)\E(Y^2)$ is not a numerical bound. Both sides may be infinite, and the proof's quadratic was not a real quadratic. A sample correlation uses the sample variances in the denominator. If every observed $x$ is the same number, that sample variance is 0 and the sample correlation is undefined, which matches the population fact that a constant has no correlation. Replacing a zero sample variance by a tiny number in order to print a correlation manufactures a quotient the inequality was never applied to. The right report is that the variable did not vary.

## Worked example
Let $X$ be the number of heads in one fair coin toss, so $\Pr(X=0)=\Pr(X=1)=1/2$, $\E X=1/2$ and $\E X^2=1/2$. Let $Y=X$. Then $\E(XY)=\E X^2=1/2$, and $\bigl(\E(XY)\bigr)^2=\E(X^2)\E(Y^2)=1/4$. Equality holds because $Y=1\cdot X$.

Let $Z$ be an independent copy of $X$. Then $\E(XZ)=\E X\E Z=1/4$, so $\bigl(\E(XZ)\bigr)^2=1/16$ while $\E(X^2)\E(Z^2)=1/4$. The ratio of the two sides is $1/4$. The centred versions have $\Var(X)=\E X^2-(\E X)^2=1/2-1/4=1/4$, and $\Cov(X,Z)=0$, so the correlation is 0. The bound is $|\Cov|\le1/4$, and 0 sits strictly inside it. Independence gave the zero covariance. The inequality did not need independence to be true.{{cite:durrett2019}} (p. 26, Cauchy–Schwarz)

**Your turn.** Take the vectors $x=(1,2)$ and $y=(2,1)$. Compute $|x^\top y|$, $\|x\|\,\|y\|$, and the same two numbers for $y=(2,4)$.

::: {.callout-tip collapse="true" title="Answer"}
The inner product $1\cdot2+2\cdot1=4$. Each vector has squared length $1+4=5$, so the product of lengths is 5, and $4<5$. For $y=(2,4)$ the inner product is $1\cdot2+2\cdot4=10$. The squared lengths are 5 and $4+16=20$, and $\sqrt{5}\times\sqrt{20}=\sqrt{100}=10$. Equality holds because $(2,4)=2(1,2)$.
:::

## Common misconceptions
Cauchy–Schwarz is not a statement that every correlation is near 1, and it is not a test. It is a ceiling. A correlation of 0.1 does not violate it. A correlation of 1.1 does, and the cure is to find the arithmetic mistake, not to collect more data. Equality does not mean the variables are independent. It means they are linearly dependent. And the bound uses second moments. A Cauchy distribution does not have a variance, so there is no correlation to which the centred form applies, even though the name Cauchy appears in both places. The distribution and the inequality are different objects.{{cite:durrett2019}} (p. 26, square-integrable variables){{cite:dodge2008}} (p. 378, the inequality for vectors with a Euclidean norm)

## Connections
The [correlation](correlation.qmd) is the centred form of the inequality, scaled to lie in $[-1,1]$. The [covariance](covariance.qmd) is the inner product of the centred variables. [Chebyshev's inequality](chebyshev-s-inequality.qmd) and [Markov's inequality](markov-s-inequality.qmd) bound tail probabilities rather than inner products. In a [linear regression](gaussian-linear-model.qmd) the residual variance stays non-negative because $\rho^2\le1$.{{cite:durrett2019}} (p. 26, Cauchy–Schwarz){{cite:dodge2008}} (p. 378, inner product and norms)

## Check yourself

### Signs and their sum {#self-check-ex-prob-sign-covariance}

Let $X$ be a fair coin coded $0$ and $1$, and let $Y=1-X$. Find $\Cov(X,Y)$ and say whether Cauchy–Schwarz is an equality.

[Exercise](../questions/ex-prob-sign-covariance.qmd)

::: {.callout-tip collapse="true" title="Answer"}
$\E X=\E Y=1/2$ and $XY=0$, so $\Cov(X,Y)=0-(1/2)(1/2)=-1/4$. Also $\Var(X)=\Var(Y)=1/4$, and $(-1/4)^2=(1/4)(1/4)$. Equality holds because $Y=1-X$, an affine function of $X$. The correlation is $-1$.
:::

### Information for a Poisson mean {#self-check-ex-inf-poisson-information}

The Cramér–Rao bound for an unbiased estimator of a Poisson mean uses Cauchy–Schwarz on the estimator and the score. For one Poisson observation the score for $\lambda$ is $X/\lambda-1$ and the Fisher information is $1/\lambda$. What lower bound does that give for the variance of an unbiased estimator of $\lambda$?

[Exercise](../questions/ex-inf-poisson-information.qmd)

::: {.callout-tip collapse="true" title="Answer"}
The bound is the reciprocal of the information, $1/(1/\lambda)=\lambda$. The sample mean of one observation is $X$ itself, and $\Var(X)=\lambda$, so the bound is attained. Attainment is the equality case of Cauchy–Schwarz: the unbiased estimator is an affine function of the score.
:::

## History
Durrett presents the inequality as the square case of Hölder's inequality and gives the one-line proof from a quadratic that must stay non-negative. The same relation holds for Euclidean vectors, under the name Cauchy–Schwarz, and the norm of the vector $(12,15,16)$ is 25. Hermann Schwarz's 1885 paper is the classical analysis source of the inequality. The probabilistic form used here is the one Durrett proves for square-integrable random variables.{{cite:durrett2019}} (p. 26, Remark){{cite:dodge2008}} (p. 378, Cauchy–Schwarz inequality and the length-25 example)
