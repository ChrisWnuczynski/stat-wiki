## Lead context
It compares parameter values using the data that were actually observed and the sampling model chosen for them. The method supplies a rule for many different models, including count, lifetime, and regression data; its answer is meaningful only with the model, parameter space, and data-recording process stated.{{cite:fisher1922,nist_handbook_mle2002}}

## Motivating example
The ten spark plugs in the original definition yielded two defects. A defect rate of one fifth gives the observed count a greater probability than rates of three tenths or two fifths under the binomial model. Maximisation makes this comparison systematic. If the same ten outcomes were instead observed with dependence between plugs, the binomial likelihood would no longer represent their joint sampling law.{{cite:fisher1922,casella_berger2002}}

## Intuition
A probability model fixes a parameter and varies possible samples; a likelihood fixes the sample and varies possible parameters. Maximum likelihood chooses the parameter whose model density or mass is highest at that sample. Only relative heights within the *same* observation model have this meaning. A likelihood is not automatically a probability distribution over parameter values, and a maximiser need not be unbiased, unique, finite, or even attained.{{cite:fisher1922,nist_handbook_mle2002}}

## Definition
Let $x=(x_1,\ldots,x_n)$ be the observed data, $\theta\in\Theta$ an allowed parameter value, and $f_\theta(x)$ their *joint* probability mass or density. The likelihood is $L_x(\theta)=f_\theta(x)$, and an MLE is any $\widehat\theta\in\operatorname{argmax}_{\theta\in\Theta}L_x(\theta)$, if that set is nonempty. For independent observations with common mass or density $f(x_i;\theta)$, the joint expression reduces to the product already displayed above. Dependence calls for its actual joint law. Multiple maximisers make the estimate set-valued until a rule for choosing one is specified.{{cite:fisher1922,casella_berger2002}}

If $L_x(\theta)>0$, maximising its logarithm gives the same maximisers. The score equation $\partial\ell/\partial\theta=0$, where $\ell=\log L_x$, identifies interior stationary points when differentiability holds; it does not certify a global maximum or find a boundary solution. The binomial, uniform-endpoint, and degenerate-normal cases on this page show three different behaviours.{{cite:fisher1922,nist_handbook_mle2002}}

## Properties
Multiplying the likelihood by a positive factor depending on the observed data but not on $\theta$ leaves its maximisers unchanged. This is why binomial coefficients and normal constants can be dropped *for an optimisation within one model*. The absolute likelihood height still depends on the chosen mass or density and must not be treated as a posterior probability.{{cite:fisher1922}}

The binomial example has $\widehat p=x/n$ for $0\le x\le n$ when the parameter space includes $0$ and $1$. If the parameter space is strictly $0<p<1$ and the observed count is $0$ or $n$, only a boundary supremum exists. Similarly, the normal variance estimate dividing by $n$ is a finite MLE only when the sample has nonzero spread; with all observations equal and unrestricted positive variance, the normal likelihood grows without bound as the variance approaches zero. These are parameter-space facts, not exceptions to the definition.{{cite:casella_berger2002,nist_handbook_mle2002}}

The [invariance property](invariance-of-maximum-likelihood.qmd) applies to a target $g(\theta)$ even when $g$ is not one-to-one: maximise $L_x$ over each set of parameter values mapping to the same target, then compare those profile heights. If $\widehat\theta$ globally maximises $L_x$, its image $g(\widehat\theta)$ maximises that profile. A nonlinear image need not preserve unbiasedness, so invariance is an optimisation claim, not an expectation claim.{{cite:fisher1922,fisher1925_est}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For independent observations, the joint law factors as $\prod_i f(x_i;\theta)$ by the definition of independence. The logarithm is strictly increasing on positive values, so it preserves likelihood order and turns that product into a sum. If $c(x)>0$ does not depend on $\theta$, then $c(x)L_x(\theta_1)\ge c(x)L_x(\theta_2)$ exactly when $L_x(\theta_1)\ge L_x(\theta_2)$, proving the constant-factor claim.{{cite:fisher1922}}

For a binomial count $x$, ignoring its parameter-independent coefficient gives $L(p)=p^x(1-p)^{n-x}$ on $[0,1]$. When $0<x<n$, $\ell'(p)=x/p-(n-x)/(1-p)$ vanishes at $p=x/n$, and $\ell''(p)=-x/p^2-(n-x)/(1-p)^2<0$. At $x=0$ the likelihood decreases and is largest at $p=0$; at $x=n$ it increases and is largest at $p=1$. Excluding the endpoints excludes those two maximisers.{{cite:casella_berger2002}}

For the normal example, let $A=\sum_i(x_i-\overline x)^2$. For each positive variance $v$, $\sum_i(x_i-\mu)^2=A+n(\mu-\overline x)^2$ is smallest at $\mu=\overline x$. The profile log likelihood is $-A/(2v)-(n/2)\log v$ plus a constant. If $A>0$, its derivative $(A-nv)/(2v^2)$ changes from positive to negative at $v=A/n$, and the profile tends downward at both ends; this is the global maximum. If $A=0$, the profile increases without bound as $v\downarrow0$. For the uniform endpoint with observed $M=\max_i x_i>0$, the closed-endpoint density convention makes $L(\theta)=\theta^{-n}$ for $\theta\ge M$, and zero below $M$; it decreases on the allowed positive branch, so $M$ is its maximiser. An open-endpoint density version excludes $M$ and has only a supremum there.{{cite:casella_berger2002}}

Finally, define $L_g(\nu)=\sup_{\theta:g(\theta)=\nu}L_x(\theta)$ over attainable target values. If $\widehat\theta$ is a global maximiser, then $L_g(g(\widehat\theta))=L_x(\widehat\theta)\ge L_g(\nu)$ for every attainable $\nu$. This proves invariance without requiring $g$ to be one-to-one.{{cite:fisher1922,fisher1925_est}}
:::
:::

## Statistical use
Write down how each observation was generated and what was recorded, including any censoring or truncation, before maximising. Specify the parameter domain and inspect boundaries and convergence diagnostics. When reporting a fitted value, add an uncertainty measure and a model check; maximising the likelihood of the observed data alone does not establish that the model describes new data well. The source chapter's small-sample variance example also shows why an MLE should not be labelled unbiased by default.{{cite:nist_handbook_mle2002,casella_berger2002}}

## Worked example
Suppose three independent lifetimes are exponential with a common rate $\lambda>0$. Two failures are observed at times $2$ and $4$, while a third item is still running when observation ends at time $5$. The first two records contribute densities $\lambda e^{-2\lambda}$ and $\lambda e^{-4\lambda}$; the censored record contributes survival probability $e^{-5\lambda}$. Thus $L(\lambda)=\lambda^2e^{-11\lambda}$ and $\ell(\lambda)=2\log\lambda-11\lambda$. Its derivative vanishes at $\widehat\lambda=2/11\approx0.1818$ per unit time, and the second derivative is negative. Counting the censored item as a failure would incorrectly give $3/11$.{{cite:nist_handbook_mle2002}}

**Your turn.** Three failures occur at times $1$, $2$, and $4$, and a fourth lifetime is right-censored at $5$ under the same model. What is the maximum-likelihood rate?

::: {.callout-tip collapse="true" title="Answer"}
There are three failure factors and total observed time $1+2+4+5=12$, so $L(\lambda)=\lambda^3e^{-12\lambda}$. The score is $3/\lambda-12$, giving $\widehat\lambda=3/12=0.25$ per unit time. The log likelihood is strictly concave for positive $\lambda$, so this stationary point is the maximum.
:::

## Common misconceptions
The MLE is a rule, while the numerical maximiser from one sample is its estimate. A higher likelihood at one parameter does not assign that parameter a posterior probability. A zero score need not mark a global maximum; the normal degenerate and uniform boundary examples show why checking the domain matters. Invariance under a parameter transformation does not imply that the transformed estimate is unbiased. A model can fit its training observations well and still be inaccurate for new observations.{{cite:fisher1922,nist_handbook_mle2002}}

## Assumptions and limits
The product likelihood assumes independence and a correctly specified individual mass or density. The exact normal and binomial formulas assume their stated sampling laws. MLE consistency and approximate normality require further regularity and identifiability conditions and should not be inferred from the maximisation definition alone. With parameter-dependent support, pointwise density conventions can alter whether a supremum is attained at a boundary, as the uniform example makes explicit.{{cite:casella_berger2002,nist_handbook_mle2002}}

## Connections
The [likelihood function](likelihood-function.qmd) is the objective being maximised; its target is an [estimator](estimator.qmd) before data collection and an estimate after observation. [Method of moments](method-of-moments.qmd) instead equates sample and model moments and can yield a different rule, as with the uniform endpoint. [Invariance of maximum likelihood](invariance-of-maximum-likelihood.qmd) describes how the maximiser changes when its target is transformed. [Mean squared error](mean-squared-error.qmd) evaluates an estimator across repeated samples and can favour a different rule.{{cite:fisher1922,casella_berger2002}}

## Check yourself
[Normal maximum likelihood estimates](../questions/ex-inf-normal-mle.qmd) asks for two parameters and a maximum check. [An exponential rate](../questions/ex-inf-exponential-mle.qmd) uses the rate parametrisation and invariance for a median. [A Poisson mean](../questions/ex-inf-poisson-mle.qmd) compares maximisation with unbiasedness and consistency.

## History
In 1912 Ronald Fisher sought an objective way to fit a theoretical frequency curve to observations. He proposed choosing parameter values that maximise the product of the model densities at the observed data, or equivalently the sum of their logarithms. This addressed the choice among competing curve-fitting criteria, not a claim that the selected model must be true.{{cite:fisher1912_curve}}

Fisher's 1922 paper set out likelihood separately from probability and developed maximum likelihood as a general estimation method. It treated the sample as fixed during comparison of parameter values and discussed the information and sampling behaviour of estimators. His 1925 work extended the theory of statistical estimation.{{cite:fisher1922,fisher1925_est}}

Modern practice uses likelihood maximisation for models whose data include incomplete observations such as right-censored lifetimes as well as fully observed samples. The NIST treatment describes that computation and the need to assess small-sample behaviour and numerical optimisation, while contemporary inference texts compare MLEs with other estimators by their repeated-sampling properties.{{cite:nist_handbook_mle2002,casella_berger2002}}
