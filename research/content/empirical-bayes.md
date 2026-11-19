## Motivating example

When many related means are estimated, a prior centre and spread can determine how much each noisy estimate is pulled towards the others. Empirical Bayes estimates features of that prior from the ensemble of observations, then uses the fitted prior to estimate the individual parameters. Normal means provide a concrete setting in which this borrowing of information can be calculated explicitly.{{cite:efron_morris1975}} (§1, pp.311–312)

## Definition — Marginal fitting followed by conditional inference

Suppose $X_i\mid\theta_i\sim N(\theta_i,s_i^2)$ and $\theta_i\mid m,\tau^2\sim N(m,\tau^2)$. Integrating out $\theta_i$ gives $X_i\mid m,\tau^2\sim N(m,s_i^2+\tau^2)$. Marginal maximum likelihood is one way to estimate $(m,\tau^2)$; other empirical-Bayes procedures estimate the mixing distribution more generally. The normal-means shrinkage calculation uses information across coordinates to estimate prior-scale features.{{cite:efron_morris1975}} (§1, p.312, Eqs.1.8–1.9)

With the hyperparameters fixed, completion of the square gives
$$E(\theta_i\mid X_i)=m+B_i(X_i-m),\quad
 B_i=\frac{\tau^2}{\tau^2+s_i^2},\qquad
 V_i=\frac{\tau^2s_i^2}{\tau^2+s_i^2}.$$
Small sampling variance gives a weight near one; a narrow prior gives stronger shrinkage. The precision-addition argument is the same Gaussian conjugacy calculation used for a fixed normal prior.{{cite:deisenroth_faisal_ong2020}} (§6.6.1, pp.208–210, Table6.2)

## Worked example — A fitted spread

Take four independent observations $(-1,1,3,5)$, each with sampling variance one, and a common $N(m,\tau^2)$ prior. The marginal normal likelihood is maximised at $\widehat m=2$ and total variance $\sum_i(X_i-2)^2/4=5$. Thus $\widehat\tau^2=4$, the fitted shrinkage weight is $4/5$, and the four estimates are
$$(-0.4,\ 1.2,\ 2.8,\ 4.4).$$
The fitted conditional variance is $4/5$ for every coordinate. More generally the variance estimate is truncated at the boundary: $\widehat\tau^2=\max\{0,n^{-1}\sum_i(X_i-\bar X)^2-1\}$. This particular marginal-likelihood rule is distinct from the unbiased precision-estimation rule that leads to the James–Stein expression.{{cite:efron_morris1975}} (§1, p.312, Eqs.1.8–1.9)

**Your turn.** A fitted prior has mean two and variance four. An observation is five with sampling variance four. What are its conditional posterior mean and variance?

::: {.callout-tip collapse="true" title="Answer"}
The weight is $4/(4+4)=1/2$. The posterior mean is $2+(5-2)/2=3.5$ and its variance is $4\cdot4/(4+4)=2$.
:::

## Properties — Conditional uncertainty and hyperparameter uncertainty

Substituting fitted hyperparameters produces a conditional posterior. A hierarchical analysis instead assigns the hyperparameters a prior and integrates their posterior uncertainty. Marginal likelihood itself is an integral over model parameters; replacing an uncertain parameter by one fitted value and integrating over it are different operations.{{cite:deisenroth_faisal_ong2020}} (§8.6.2, pp.285–286, Eq.8.44)

The law of total variance separates the consequences:
$$\operatorname{Var}(\theta\mid X)=
 E\{\operatorname{Var}(\theta\mid X,\eta)\mid X\}
 +\operatorname{Var}\{E(\theta\mid X,\eta)\mid X\}.$$
For an equal mixture of $N(5,1)$ and $N(9,1)$, the mean is seven and the variance is $1+4=5$. Reporting only a within-component variance of one omits the between-component contribution. This calculation illustrates uncertainty propagation; it does not impose a universal ordering between every fitted interval and every hierarchical interval.{{cite:deisenroth_faisal_ong2020}} (§6.5.3, pp.202–203, Thm.6.12)

## Statistical use — Unequal information across groups

For a group sample mean, $s_i^2=\sigma^2/n_i$. With prior centre $70$, prior variance $25$, and observation variance $100$, a group of size $100$ and mean $75$ has weight $25/26$ and posterior mean $74.80769$. A group of size two and mean $95$ has weight $1/3$ and posterior mean $78.33333$. The posterior gap is $3.52564$, compared with the observed gap of twenty. Larger groups receive less shrinkage because their sample means contain more information.{{cite:efron_morris1975}} (§1, p.312, Eq.1.8)
