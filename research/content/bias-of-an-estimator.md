## Lead context
The bias of an estimator is the gap between its average value and the parameter it is meant to estimate.

## Intuition — Average error is not the same thing as scatter
An estimator $T$ of a parameter $\theta$ is a random variable computed from the sample. Its bias is $b(\theta)=\mathbb{E}(T)-\theta$, whenever the expectation exists. Bias zero means the estimates are centred on $\theta$ on average. It does not mean a typical estimate is close: that closeness is the mean squared error, which splits into variance plus squared bias. A small bias can be the price of a large drop in variance.{{cite:dodge2008}} (p. 41, bias and precision)

## Definition — Expected value minus the target
If $\mathbb{E}(T)=\theta+b(\theta)$, then $b(\theta)$ is the bias of $T$. The estimator is unbiased when $b(\theta)=0$ for every $\theta$ under consideration, which is the same statement as $\mathbb{E}(T)=\theta$. Dodge traces the idea of an unbiased estimator to Gauss's work on least squares. Selection bias, exclusion bias and analytical bias are different uses of the word: they describe how a study can be distorted, not the expectation of a named estimator.{{cite:dodge2008}} (p. 41, definition and history)

## Properties — Mean squared error adds the square of the bias
When the variance is finite,
$$
\mathbb{E}(T-\theta)^2=\operatorname{Var}(T)+\{b(\theta)\}^2.
$$
For independent observations with mean $\mu$ and variance $\sigma^2$, the divisor-$n$ variance estimator $S_n^2=n^{-1}\sum_i(X_i-\overline X)^2$ has expectation $\sigma^2-\sigma^2/n$, so its bias for $\sigma^2$ is $-\sigma^2/n$.{{cite:dodge2008}} (p. 41, the variance calculation)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $T-\theta=(T-\mathbb{E} T)+b(\theta)$. The cross term has expectation zero, so the mean squared error is the variance plus $b(\theta)^2$.

For the variance estimator, expand $\sum_i(X_i-\overline X)^2=\sum_i(X_i-\mu)^2-n(\overline X-\mu)^2$. Taking expectations gives $n\sigma^2-\sigma^2=(n-1)\sigma^2$. Dividing by $n$ leaves $\mathbb{E}(S_n^2)=((n-1)/n)\sigma^2$, and the bias is $-\sigma^2/n$.{{cite:dodge2008}} (p. 41, mathematical aspects)
:::
:::

## Worked example
Let $n=5$ and $\sigma^2=4$. The bias of $S_n^2$ is $-4/5=-0.8$. The unbiased sample variance $s^2$, which divides by $n-1=4$, has bias $0$. Under normality, $(n-1)s^2/\sigma^2$ is chi-squared on $4$ degrees of freedom, so $\operatorname{Var}(s^2)=2\sigma^4/(n-1)=32/4=8$ and the mean squared error is $8$. The maximum-likelihood estimator $(4/5)s^2$ has variance $(4/5)^2\cdot 8=5.12$ and squared bias $0.64$, hence mean squared error $5.76$. The biased estimator is closer in mean square.{{cite:dodge2008}} (p. 41, bias of the divisor-$n$ variance)

**Your turn.** For $n=8$ and $\sigma^2=9$, find the bias of the divisor-$n$ variance estimator, and the normal-theory mean squared error of the unbiased $s^2$.

::: {.callout-tip collapse="true" title="Answer"}
The bias is $-9/8=-1.125$. The unbiased variance has variance $2(81)/7=162/7\approx 23.143$, and that is also its mean squared error because the bias is zero.{{cite:dodge2008}} (p. 41)
:::

## Connections
An [unbiased estimator](unbiased-estimator.qmd) is the special case $b(\theta)=0$. [Mean squared error](mean-squared-error.qmd) is the sum compared above. The square root of an unbiased variance estimator is not unbiased for the standard deviation, because the square root is curved. A study that systematically drops some units can be biased in Dodge's other sense even when every recorded estimator has bias zero.{{cite:dodge2008}} (p. 41, several types of bias)

## Check yourself — A scaled estimator
**1.** If $T$ is unbiased for $\theta$ and $c$ is a constant, what is the bias of $cT$ for $\theta$?

::: {.callout-tip collapse="true" title="Answer"}
$\mathbb{E}(cT)=c\theta$, so the bias is $c\theta-\theta=(c-1)\theta$. The choice $c=(n-1)/n$ is the step from $s^2$ to $S_n^2$ when both estimate $\sigma^2$, and it produces bias $-\sigma^2/n$.{{cite:dodge2008}} (p. 41)
:::

**2.** An estimator has variance $0.3$ and bias $0.1$. What is its mean squared error?

::: {.callout-tip collapse="true" title="Answer"}
The mean squared error is $0.3+0.1^2=0.31$. The squared bias is a tenth of the variance, so most of the error is scatter.{{cite:dodge2008}} (p. 41, bias is not precision)
:::
