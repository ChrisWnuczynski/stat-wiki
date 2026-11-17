## Lead context
The distinction separates a computable summary from the purpose assigned to that summary. An estimator is the rule before sampling; an estimate is its realised value.{{cite:dodge2008}} (pp. 185–186)

## Motivating example
Four independent coin tosses give $(1,0,1,1)$, with $1$ denoting a head. The number of heads is $3$, the sample proportion is $3/4$, and the sample variance with divisor $3$ is $1/4$. All three are statistics. Calling $3/4$ an estimate of the probability of a head adds an inferential purpose to a summary that can already be computed.{{cite:dodge2008}} (p. 517)

## Properties — Parameter-free formula, parameter-dependent law
For Bernoulli observations with success probability $p$, $K=\sum_iX_i$ has the binomial law. Thus $K$ is a statistic although $P_p(K=k)$ depends on $p$. Requiring its law to be free of $p$ would impose the much stronger property of ancillarity. The parameter-free requirement concerns evaluation of the function, not its distribution.{{cite:dodge2008}} (pp. 44–45, 517)

An estimator need not be accurate, unbiased or unique. Under squared-error loss, its quality is measured by
$$
E_p[(T-p)^2]=\operatorname{Var}_p(T)+\{E_p(T)-p\}^2.
$$
To derive this decomposition, insert $T-p=(T-E_pT)+(E_pT-p)$, expand the square, and use $E_p(T-E_pT)=0$. The cross-term vanishes. Bias and variability are different contributions to the same risk.{{cite:goodfellow_bengio_courville2016}} (§5.4.2, eqs. 5.20–5.21; §5.4.4)

## Worked example
Compare $\widehat p=K/4$ with $\widetilde p=(K+1)/6$. On the observed sample their estimates are $3/4$ and $2/3$. Since $E_pK=4p$ and $\operatorname{Var}_pK=4p(1-p)$,
$$
E_p\widehat p=p,\quad \operatorname{Var}_p\widehat p=\frac{p(1-p)}4,
\qquad E_p\widetilde p-p=\frac{1-2p}{6},\quad
\operatorname{Var}_p\widetilde p=\frac{p(1-p)}9.
$$
At $p=1/2$ both biases vanish, but their risks are $1/16$ and $1/36$. At $p=0$ the sample proportion has risk zero whereas the second rule always reports $1/6$ and has risk $1/36$. A comparison at one parameter value cannot establish uniform superiority. Point estimation treats an estimator as a function of the random data and evaluates its behaviour across repeated samples.{{cite:goodfellow_bengio_courville2016}} (§5.4.1, eqs. 5.18–5.19)

**Your turn.** If the four tosses are $(0,0,1,0)$, evaluate both estimators. Is $\sum_i(X_i-p)^2$ a statistic when $p$ is unknown?

::: {.callout-tip collapse="true" title="Answer"}
$K=1$, so the estimates are $1/4$ and $1/3$. The final expression contains the unknown $p$ and cannot be evaluated from the sample alone, so it is not a statistic.
:::

## Assumptions and limits
The formulas for expectations and variances above use independent Bernoulli sampling. The distinction between statistic and estimator does not need that particular model: a fixed design, a known constant or auxiliary randomisation with a specified law can be included in an estimation procedure. An expression containing the unknown quantity it purports to estimate still requires a different, observable rule.{{cite:dodge2008}} (pp. 185, 517)
