## Motivating example
Four tumour-bearing rats among fourteen controls give a raw proportion $4/14\approx0.2857$. This study is small enough that its estimate can change sharply with one outcome. Seventy historical control groups provide information about how rates vary between studies, but complete pooling would assume every group has exactly the same rate. A beta-binomial hierarchy provides an intermediate model in which each group can differ while contributing to a common population description.{{cite:gelman_bda2013}} (§5.1, pp. 102–103, tab. 5.1)

## Definition — Separate animal sampling from study variation
Given its study rate $\theta_j$, the count $Y_j$ is binomial with size $n_j$. Across studies, rates are drawn from $\operatorname{Beta}(\alpha,\beta)$. Put $m=\alpha/(\alpha+\beta)$ and $\kappa=\alpha+\beta$. Then the between-study mean is $m$ and variance is $m(1-m)/(\kappa+1)$. A large concentration $\kappa$ means study rates are tightly grouped around $m$; it does not mean each observed study fraction has low binomial sampling variation.{{cite:gelman_bda2013}} (§5.1, pp. 102–103)

Conditional independence of animals given a shared rate is different from marginal independence. Integrating over a random rate induces positive association between two Bernoulli outcomes in the same group: their covariance is $\operatorname{Var}(\theta_j)$. Outcomes from different studies are conditionally independent given fixed hyperparameters in this model.

## Properties — Derive conjugacy and shrinkage
Multiplying the binomial likelihood by the beta density gives kernel
$$\theta_j^{\alpha+y_j-1}(1-\theta_j)^{\beta+n_j-y_j-1}.$$
The conditional posterior is therefore $\operatorname{Beta}(\alpha+y_j,\beta+n_j-y_j)$. Its mean can be expressed as
$$\E(\theta_j\mid y_j,\alpha,\beta)=\frac{n_j}{n_j+\kappa}\frac{y_j}{n_j}+\frac\kappa{n_j+\kappa}m.$$
For fixed hyperparameters, smaller groups receive more weight on the population mean. This is an exact algebraic weighting identity, not a guarantee that the population mean is scientifically appropriate for every group.

Integrating the likelihood instead gives the marginal count mass
$$\mathbb{P}(Y_j=y_j\mid\alpha,\beta)={n_j\choose y_j}\frac{B(\alpha+y_j,\beta+n_j-y_j)}{B(\alpha,\beta)}.$$
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

## Interpretation — Three averages and one update
The historical table supports three different averages, and they answer three questions. The pooled fraction $263/1725\approx0.152464$ weights each animal equally. The unweighted mean of the seventy study fractions, about $0.136007$, weights each study equally. The beta mean $\hat\alpha/(\hat\alpha+\hat\beta)=2.3048/16.3846\approx0.140792$ is the mean of the fitted study-rate distribution. The gap between $0.152464$ and $0.136007$ is the gap between animal weighting and study weighting. The fitted beta mean sits near the study-weighted figure because the marginal likelihood sees each study as one draw of a rate, with a binomial sample around that rate. Substituting the pooled animal fraction for $m$ in the shrinkage formula uses a different estimand.{{cite:gelman_bda2013}} (§5.1, p. 102, tab. 5.1)

The concentration $\hat\kappa=\hat\alpha+\hat\beta\approx16.3846$ is a statement about study-to-study variation of the rates. The fitted beta mean is $2.3048/16.3846\approx0.1407$. The beta variance at that mean is about $0.1407\times0.8593/17.3846\approx0.00695$, and the corresponding standard deviation is about $0.0834$. The sample standard deviation of the seventy observed fractions is $0.103492$, larger than $0.0834$, because each observed fraction also contains binomial noise. Equating those two standard deviations would treat sampling error as extra heterogeneity. The marginal likelihood separates them by using the group sizes. A study of size $14$ with rate $0.14$ has binomial variance $0.14\times0.86/14\approx0.0086$ on the fraction scale, the same order as the fitted between-study variance. Both pieces belong in a description of why $4/14$ moved.{{cite:gelman_bda2013}} (§5.1, pp. 102–103)

Given the fitted hyperparameters, the current study’s posterior mean is
$$\frac{14}{14+16.3846}\cdot\frac{4}{14}+\frac{16.3846}{14+16.3846}\cdot\frac{2.3048}{16.3846}=0.20750.$$
The weight on the raw fraction $4/14$ is $14/30.3846\approx0.4608$, and the weight on the historical mean is about $0.5392$. A study with $n_j=100$ and the same raw fraction would put weight $100/(100+16.3846)\approx0.8592$ on $4/14$ and would shrink only to about $0.2653$. The hierarchy does not pull every study to $0.14$. It pulls small studies harder because a small binomial sample is weak evidence against the historical mean. The posterior $\operatorname{Beta}(6.3048,24.0798)$ is the update that conditions on $(\hat\alpha,\hat\beta)$. A full hierarchical posterior would also spread those two hyperparameters. The reported mean $0.20750$ does not include that second layer of uncertainty.{{cite:gelman_bda2013}} (§5.3, beta-binomial hierarchical posterior)

## Common misconceptions
The raw proportion $4/14\approx0.2857$ is the maximum-likelihood estimate for a single binomial probability. It is the right answer to "what fraction did this control group show?" It is a noisy answer to "what rate does a new control group of this type have?" One more tumour would move $4/14$ to $5/14\approx0.3571$. The beta update moves a less extreme amount because it treats the historical studies as information about the rate, not as fourteen extra animals with the same rate. Complete pooling would append the current animals to the $1725$ historical animals and estimate $(263+4)/(1725+14)=267/1739\approx0.1535$, which almost ignores the current group. The hierarchy sits between $0.2857$ and $0.1535$. Quoting only the raw fraction and quoting only the pooled fraction are the two endpoints of that path.{{cite:gelman_bda2013}} (§5.1, pp. 102–103, tab. 5.1)

A posterior mean is not a posterior probability that the rate exceeds a threshold, and it is not a prediction for the next animal until the beta-binomial predictive probability is computed. Under $\operatorname{Beta}(6.3048,24.0798)$ the mean is $0.20750$. The probability that the next control animal in a new study is affected, after integrating a fresh rate, depends on whether the new study is a new draw from the beta population or a further animal from the current study. For a further animal in the current study the predictive probability equals the current posterior mean. For a new study it equals the population mean $m$, if the hyperparameters are treated as known. Mixing those two predictions reports the wrong experiment. The historical endpoint is endometrial stromal polyps in female F344 controls. A mean fitted to that table is a statement about that endpoint and those controls.{{cite:gelman_bda2013}} (§5.1, p. 102, description of the rat experiment)
