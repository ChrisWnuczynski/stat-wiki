## Motivating example
Four tumour-bearing rats among fourteen controls give a raw proportion $4/14\approx0.2857$. This study is small enough that its estimate can change sharply with one outcome. Seventy historical control groups provide information about how rates vary between studies, but complete pooling would assume every group has exactly the same rate. A beta-binomial hierarchy provides an intermediate model in which each group can differ while contributing to a common population description.{{cite:gelman_bda2013}} (§5.1, pp. 102–103, tab. 5.1)

## Definition — Separate animal sampling from study variation
Given its study rate $\theta_j$, the count $Y_j$ is binomial with size $n_j$. Across studies, rates are drawn from $\operatorname{Beta}(\alpha,\beta)$. Put $m=\alpha/(\alpha+\beta)$ and $\kappa=\alpha+\beta$. Then the between-study mean is $m$ and variance is $m(1-m)/(\kappa+1)$. A large concentration $\kappa$ means study rates are tightly grouped around $m$; it does not mean each observed study fraction has low binomial sampling variation.{{cite:gelman_bda2013}} (§5.1, pp. 102–103)

Conditional independence of animals given a shared rate is different from marginal independence. Integrating over a random rate induces positive association between two Bernoulli outcomes in the same group: their covariance is $\operatorname{Var}(\theta_j)$. Outcomes from different studies are conditionally independent given fixed hyperparameters in this model.{{cite:siegrist2022_beta_bernoulli}} (section “Outcome Variables”, pair covariance)

## Properties — Derive conjugacy and shrinkage
Multiplying the binomial likelihood by the beta density gives kernel
$$\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1}.$$
The conditional posterior is therefore $\operatorname{Beta}(\alpha+y_j,\beta+n_j-y_j)$. Its mean can be expressed as
$$E(\theta_j\mid y_j,\alpha,\beta)=\frac{n_j}{n_j+\kappa}\frac{y_j}{n_j}+\frac\kappa{n_j+\kappa}m.$$
For fixed hyperparameters, smaller groups receive more weight on the population mean. This is an exact algebraic weighting identity, not a guarantee that the population mean is scientifically appropriate for every group.{{cite:siegrist2022_beta_bernoulli}} (section “Outcome Variables”, posterior beta law)

Integrating the likelihood instead gives the marginal count mass
$$P(Y_j=y_j\mid\alpha,\beta)={n_j\choose y_j}\frac{B(\alpha+y_j,\beta+n_j-y_j)}{B(\alpha,\beta)}.$$
The product across independent studies is the marginal likelihood for the hyperparameters. Maximising it is an empirical-Bayes procedure. A full Bayesian analysis places a hyperprior on $(\alpha,\beta)$ and averages conditional posteriors over their posterior uncertainty.{{cite:gelman_bda2013}} (§5.3, beta-binomial hierarchical posterior)

## Worked example — Historical fitting and the current study
Transcribing the seventy fractions in the historical-control table gives $263$ affected animals among $1725$ controls. The unweighted mean of the seventy fractions is approximately $0.136007$, and their sample standard deviation is $0.103492$. The pooled animal fraction is approximately $0.152464$. These averages differ because studies have different sizes. Neither should be substituted silently for the other.{{cite:gelman_bda2013}} (§5.1, p. 102, tab. 5.1)

Maximising the beta-binomial marginal likelihood over positive hyperparameters for these historical groups gives approximately $\hat\alpha=2.3048$ and $\hat\beta=14.0798$. Conditioning on those fitted values, the current $4/14$ study has posterior approximately $\operatorname{Beta}(6.3048,24.0798)$ and mean $0.20750$. This calculation uses the historical groups to estimate population variation, then uses the current group once for its own update. It conditions on a fitted hyperparameter pair and does not include uncertainty from estimating that pair.

For a transparent comparison, a deliberately specified prior $\operatorname{Beta}(2,8)$ would instead give posterior $\operatorname{Beta}(6,18)$ and mean $0.25$. Here the shrinkage expression is $(14/24)(4/14)+(10/24)(0.2)=0.25$. This is a chosen-prior illustration, distinct from the marginal-likelihood fit.

**Your turn.** Use the specified $\operatorname{Beta}(2,8)$ prior for a study with one affected rat among ten. Find its posterior mean and its weights on the raw fraction and prior mean.

::: {.callout-tip collapse="true" title="Answer"}
The posterior is $\operatorname{Beta}(3,17)$ and its mean is $3/20=0.15$. The raw fraction is $0.1$ and prior mean $0.2$; both weights are $10/(10+10)=1/2$, giving $0.15$.
:::

## Assumptions and limits
Exchangeability across studies is a scientific assumption. Changes in animal strain, observation window, laboratory practices or tumour definition can make some historical groups less comparable to a current group. The endpoint in the cited example is endometrial stromal polyps in female F344 controls; a model for that endpoint should not silently become a model for arbitrary cancers.{{cite:gelman_bda2013}} (§5.1, p. 102, description of the rat experiment)

The variability of observed fractions combines heterogeneity of the true rates with binomial sampling error. Matching their sample variance directly to a beta variance ignores that second component. The beta-binomial marginal likelihood incorporates the group sizes and sampling variation explicitly. Finally, a posterior rate estimate describes risk under the chosen control-study population model; a comparison of drug treatments needs a model for treatment assignment and treatment outcomes as well.
