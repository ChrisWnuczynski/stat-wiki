## Lead context
Newton’s method replaces a score equation by its tangent line, then jumps to where that line crosses zero.

## Motivating example
Four independent Bernoulli trials produce one success. The logit of the success probability is a single coefficient $\beta$, and the maximum-likelihood equation $1-4p(\beta)=0$ has the closed root $p=1/4$. Starting from $\beta=0$ and using the slope of the score still walks toward that root in a few steps, which is the same idea a GLM uses when the root is not closed.{{cite:rstats_glm2026}} (`glm.fit`, iteratively reweighted least squares)

## Intuition — Follow the tangent of the score
Let $U(\beta)$ be a differentiable score, and let $H(\beta)$ be its derivative. The tangent at a current value $\beta^{(k)}$ is $U(\beta^{(k)})+H(\beta^{(k)})(\beta-\beta^{(k)})$. Setting the tangent to zero and solving gives
$$
\beta^{(k+1)}=\beta^{(k)}-H(\beta^{(k)})^{-1}U(\beta^{(k)}),
$$
provided $H(\beta^{(k)})$ is invertible. Each step uses only the value and the slope at the current point. For a log-likelihood, $U$ is the score and $H$ is the Hessian. Replacing $H$ by its expectation is Fisher scoring. For a binomial logit the observed Hessian equals that expectation, because it depends on the data only through the fitted probabilities.

R’s default GLM fitter, `glm.fit`, implements the weighted form of this iteration, called iteratively reweighted least squares.{{cite:rstats_glm2026}} (`glm.fit`, iteratively reweighted least squares)

## Definition — One step on a logistic intercept
For $y$ successes in $n$ independent Bernoulli trials and $\operatorname{logit}p=\beta$,
$$
U(\beta)=y-np(\beta),\qquad H(\beta)=-np(\beta)\bigl(1-p(\beta)\bigr),
$$
with $p(\beta)=e^{\beta}/(1+e^{\beta})$. The update is $\beta-U(\beta)/H(\beta)$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The log-likelihood is $\ell(\beta)=y\log p+(n-y)\log(1-p)$. Since $dp/d\beta=p(1-p)$,
$$
\frac{d\ell}{d\beta}=\Bigl(\frac{y}{p}-\frac{n-y}{1-p}\Bigr)p(1-p)=y-np.
$$
Differentiating again, $dU/d\beta=-n\,p(1-p)$. The chain rule uses only $p(\beta)$, so the Hessian does not contain $y$ except through that probability. The expected second derivative is therefore the same matrix.
:::
:::

A quadratic log-likelihood is finished in one step. If $\ell(\beta)=a+b\beta+c\beta^2$ with $c\neq 0$, then $U=b+2c\beta$ and $H=2c$, so
$$
\beta-U/H=\beta-(b+2c\beta)/(2c)=-b/(2c),
$$
the unique critical point, from every start.

## Worked example
Take $n=4$ and $y=1$, and start at $\beta^{(0)}=0$. Then $p=1/2$, $U=1-2=-1$, and $H=-1$. The first step is
$$
\beta^{(1)}=0-(-1)/(-1)=-1.
$$
At $\beta=-1$, $p=1/(1+e)\approx 0.268941$ and $U=1-4/(1+e)\approx -0.075766$. One further step reaches $\beta^{(2)}\approx -1.096339$. The exact root is $\log(1/3)\approx -1.098612$, where $p=1/4$. The iteration is already within $0.003$ of that root.

**Your turn.** From $\beta^{(2)}\approx -1.096339$, compute the success probability and the score $U=1-4p$, and say which way the next step moves.

::: {.callout-tip collapse="true" title="Answer"}
$p\approx 0.250426$ and $U\approx -0.001706$. The score is still negative, and $H=-np(1-p)$ is negative, so $-U/H$ is negative. The next value moves a little further down, toward $\log(1/3)$.
:::

## Connections — Closed roots and weighted least squares
When the score is linear, as it is for a normal [identity link](identity-link.qmd), one Newton step is the whole fit. A [Poisson](poisson-distribution.qmd) mean with the log link, or a binomial probability with the [logit link](logit-link.qmd), leaves a nonlinear score, and the same tangent update is repeated. [Maximum likelihood in a GLM](maximum-likelihood-in-a-glm.qmd) is that iteration applied to the GLM score. The algorithm can diverge when the likelihood has no finite maximizer, which is what [complete separation](complete-separation.qmd) does to a logistic fit.

## Check yourself

### Derivative of the logistic function {#self-check-ex-sl-10-1}

For $\sigma(\eta)=1/(1+e^{-\eta})$, show $\sigma'(\eta)=\sigma(\eta)(1-\sigma(\eta))$ and $\sigma(-\eta)=1-\sigma(\eta)$.

[Question-bank page](../questions/ex-sl-10-1.qmd)

::: {.callout-tip collapse="true" title="Answer"}
$\sigma'(\eta)=e^{-\eta}/(1+e^{-\eta})^2=\sigma(\eta)(1-\sigma(\eta))$. Also $\sigma(-\eta)=1/(1+e^{\eta})=e^{-\eta}/(1+e^{-\eta})=1-\sigma(\eta)$. The first identity is the weight in the logistic Hessian.
:::

### Complete separation {#self-check-ex-sl-10-5}

For $x=(1,2,3,4)$ and $y=(0,0,1,1)$, the path $\beta_1=s$, $\beta_0=-2.5s$ sends the logistic log-likelihood up to $0$ as $s\to\infty$. What does that say about a finite maximum?

[Question-bank page](../questions/ex-sl-10-5.qmd)

::: {.callout-tip collapse="true" title="Answer"}
No finite coefficient vector maximises the log-likelihood: along this path it increases toward $0$ and never attains $0$. Strict concavity does not by itself guarantee a finite root of the score. Newton’s method then has no finite stationary point to find.
:::
