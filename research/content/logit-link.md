## Lead context
It lets a linear predictor describe a probability while keeping fitted values between zero and one. Its coefficients describe changes in odds, so the baseline probability is needed to turn a coefficient into a probability change.{{cite:berkson1944,cox1958_logistic}}

## Motivating example
Suppose a treatment doubles the odds of recovery. If the untreated recovery probability is one fifth, its odds are one to four; doubling them gives one to two, or a treated probability of one third. The logit makes the multiplication of odds an addition of $\log 2$ to a linear predictor. The probability rises by about 13 percentage points, not by a factor of two.{{cite:cox1958_logistic,agresti2002}}

## Intuition
A binary response can be zero or one, but its *mean* is a probability. Taking the logarithm of its odds gives a scale without probability boundaries: probabilities close to zero map to large negative numbers, one half maps to zero, and probabilities close to one map to large positive numbers. The inverse transformation bends a straight predictor into an S-shaped probability curve. Applying the logit directly to a realised zero or one would be undefined; the link is applied to the modelled mean.{{cite:berkson1944,nelder_wedderburn1972}}

## Definition
For a Bernoulli response $Y$ coded as $1$ for success and $0$ for failure, write $p=\mathbb P(Y=1\mid\mathbf x)$ for the success probability at observed covariate vector $\mathbf x$. The *logit link* is $g(p)=\log\{p/(1-p)\}$ for $0<p<1$. Here $1-p$ is the failure probability, $p/(1-p)$ is the odds of success, and $\log$ is the natural logarithm. A logistic regression sets $g(p)=\eta=\mathbf x^\top\boldsymbol\beta$, where $\eta$ is the linear predictor and $\boldsymbol\beta$ is its coefficient vector. The inverse link is $p=\operatorname{expit}(\eta)=1/(1+e^{-\eta})$. The previously displayed bold $\boldsymbol X$ represents a model covariate vector; lower-case $\mathbf x$ denotes its observed value.{{cite:berkson1944,cox1958_logistic,nelder_wedderburn1972}}

Probabilities exactly zero and one have infinite limiting logits and are outside the link's domain. A finite predictor always gives a probability strictly between them. This does not prevent a sample from containing only zeros or only ones, nor does it mean that a finite maximum-likelihood coefficient always exists.{{cite:berkson1944,cox1958_logistic}}

## Properties
The logit is strictly increasing from negative infinity to positive infinity, with $g(1/2)=0$ and $g(1-p)=-g(p)$. Its inverse is strictly increasing, and its derivative at $\eta$ is $p(1-p)$, largest when $p=1/2$. Hence a fixed increase in the predictor changes the probability most sharply near one half, and less sharply near either boundary.{{cite:berkson1944,nelder_wedderburn1972}}

The link is *canonical* for a Bernoulli or binomial response because the coefficient of the observed success count in the exponential-family log likelihood is the logit of the success probability. This is an algebraic property of the distribution, not a requirement to use this link. A [probit link](probit-link.qmd) is another valid choice for the same Bernoulli response.{{cite:nelder_wedderburn1972,agresti2002}}

If one covariate increases by one unit while the others stay fixed, its coefficient $\beta_j$ adds to the log odds and multiplies the odds by $e^{\beta_j}$. For an increase of $d$ units, the multiplier is $e^{d\beta_j}$. This is a *conditional* comparison at fixed values of the other covariates, assuming the predictor contains no interaction that also changes. The corresponding change in probability depends on the starting value of $p$.{{cite:cox1958_logistic,agresti2002}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $0<p<1$, differentiation gives $g'(p)=1/p+1/(1-p)=1/[p(1-p)]>0$. Its limits as $p$ approaches zero and one are negative and positive infinity. Substitution gives $g(1/2)=0$ and $g(1-p)=-g(p)$. Solving $e^\eta=p/(1-p)$ gives $p=e^\eta/(1+e^\eta)$; differentiation yields $dp/d\eta=p(1-p)$. Since $p(1-p)=1/4-(p-1/2)^2$, this derivative is largest at one half.{{cite:berkson1944}}

For one Bernoulli observation $y\in\{0,1\}$, the log likelihood is $y\log p+(1-y)\log(1-p)=y\log\{p/(1-p)\}+\log(1-p)$. The coefficient of $y$ is $g(p)$, the natural parameter. For a binomial count of $m$ trials, the log likelihood is $y g(p)+m\log(1-p)+\log\binom m y$; the last term depends on $y$ but not on $p$. Thus the logit is canonical. If the predictor changes from $\eta$ to $\eta+d\beta_j$, the odds change from $e^\eta$ to $e^\eta e^{d\beta_j}$, proving the stated multiplier.{{cite:nelder_wedderburn1972,cox1958_logistic}}

Finally, consider the complete-separation claim in the retained interpretation. For one scalar covariate $x_i$, suppose both response classes occur and every observed success has $x_i>c$ while every failure has $x_i<c$. In an unpenalised logistic regression with intercept $-tc$ and slope $t$, letting $t\to\infty$ sends every success probability toward one and every failure probability toward zero. Each log-likelihood contribution approaches zero from below, so the total approaches its supremum of zero. At finite $t$, every probability lies strictly between zero and one and the log likelihood remains below zero. No finite coefficient vector attains that supremum along this separating direction.{{cite:cox1958_logistic}}
:::
:::

## Statistical use
For a fitted logistic model, report the response coding, the covariates held fixed, an odds ratio with an uncertainty interval, and predicted probabilities at useful covariate values. The ratio alone cannot tell a reader the absolute probability change. When data perfectly separate the classes, an ordinary unpenalised maximum-likelihood fit may drive coefficients outward instead of returning finite estimates; inspect fitted values and convergence diagnostics. A different link, a penalty, or a different data design changes the analysis and needs its own justification.{{cite:agresti2002,cox1958_logistic}}

## Worked example
Take the fitted linear predictor $\eta=\log(1/3)+x\log 3$, where $x=0$ denotes the reference group and $x=1$ the comparison group. At $x=0$, the odds are $1/3$ and the predicted probability is $1/4=0.25$. At $x=1$, the odds are $1$ and the predicted probability is $1/2=0.50$. The coefficient $\log 3$ gives an odds ratio of $3$, a risk ratio of $2$, and a probability difference of $0.25$. These are three different comparisons of the same two model predictions.{{cite:agresti2002}}

**Your turn.** Keep the odds ratio at $3$ but start from a reference probability of $0.10$. What is the comparison probability, risk ratio, and probability difference?

::: {.callout-tip collapse="true" title="Answer"}
The starting odds are $1/9$; multiplying by $3$ gives odds $1/3$ and probability $1/4=0.25$. The risk ratio is $0.25/0.10=2.5$ and the probability difference is $0.25-0.10=0.15$. The odds ratio stayed $3$, but the other two summaries changed.
:::

## Common misconceptions
A logit coefficient is a difference in *log odds*, not a fixed difference in probability. Exponentiating it produces an odds ratio, which usually differs from a risk ratio. A fitted Bernoulli model transforms its *mean*, not each zero or one response. “Canonical” describes its exponential-family form; it does not assert that a logit is scientifically preferable for every binary-outcome problem. Finally, an unpenalised fit can have finite probabilities for every finite coefficient vector while lacking a finite maximum-likelihood estimate under complete separation.{{cite:berkson1944,cox1958_logistic,nelder_wedderburn1972}}

## Assumptions and limits
The logit transformation itself assumes only a probability strictly between zero and one. Interpreting $e^{\beta_j}$ as one common odds multiplier across covariate settings additionally assumes the stated additive predictor has no interaction involving that covariate. A Bernoulli GLM's usual likelihood treats responses as conditionally independent; repeated observations on a subject require a model for dependence or an appropriate estimating method. A conditional odds ratio from a fitted model does not by itself establish a causal treatment effect.{{cite:cox1958_logistic,agresti2002}}

## Connections
The [odds](odds.qmd) turn a probability into a success-to-failure ratio; the [odds ratio](odds-ratio.qmd) compares that ratio across two groups. [Binary logistic regression](binary-logistic-regression.qmd) combines the logit with a Bernoulli likelihood and a linear predictor. The [probit link](probit-link.qmd) uses a standard-normal quantile instead and does not give coefficients a direct odds-ratio interpretation. The [complementary log-log link](complementary-log-log-link.qmd) is asymmetric around probability one half. All are link choices for a binary mean; changing the link does not change the observed zero-or-one response.{{cite:bliss1935,berkson1944,nelder_wedderburn1972}}

## Check yourself
[Logit, probit and odds](../questions/c-20.qmd) asks for the three definitions. [Odds ratios](../questions/ex-sl-10-2.qmd) uses a ten-year coefficient change and fitted probabilities; check why its odds ratio and probability ratio differ. For model comparison, [changing from a logit to a probit link](../questions/q-38.qmd) keeps the Bernoulli response but refits the coefficients.

## History
Joseph Berkson applied the logistic function to bioassay data in 1944. The problem was to describe how the fraction of subjects showing an all-or-none response changed with dose. He compared a logistic curve with the integrated normal curve then used for this purpose and worked with a linear scale of logits for fitting. The paper explicitly used the term *logit*.{{cite:berkson1944}}

David Cox's 1958 analysis considered sequences of binary outcomes whose success chances depended on explanatory variables. His regression treatment developed the logistic law for those varying chances, making the link useful beyond one dose-response curve. This is the setting behind the coefficient and odds-ratio interpretation used here.{{cite:cox1958_logistic}}

Nelder and Wedderburn's 1972 generalised-linear-model framework placed binomial regression beside normal, Poisson, and gamma models under a common likelihood and link-function structure. In that framework the logit is the binomial canonical link because it is the binomial natural parameter. Later categorical-data treatments retain both this algebraic result and the practical need to report probabilities alongside odds ratios.{{cite:nelder_wedderburn1972,agresti2002}}
