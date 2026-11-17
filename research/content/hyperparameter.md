## Lead context
Learning it from related groups lets their estimates share information while carrying uncertainty about the population they came from.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.3, pp. 101–110)

## Motivating example
Suppose several clinics report proportions of patients with an outcome. Each clinic has its own unknown rate, but very small clinics provide little information about their own rate. A population distribution of clinic rates expresses their resemblance without forcing them to be identical. Its centre and spread are hyperparameters: the centre says where clinic rates tend to lie, and the spread says how much they vary. Data from all clinics inform those population quantities, which in turn inform each clinic. The rat-tumour example below uses this pattern for related animal studies.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.2, pp. 102–106)

## Intuition
There are two roles for a prior parameter. In a single Beta–Binomial analysis, $\alpha$ and $\beta$ may be chosen in advance and held fixed; they specify the prior for one success probability. In a hierarchy, study probabilities $\theta_j$ vary across studies, and the same $\alpha,\beta$ describe their population distribution. If these higher-level quantities are unknown, a full Bayesian analysis gives them a hyperprior and updates them with all studies. The term *hyperparameter* names a role in the model, not a guarantee that the quantity is random or known.{{cite:gelman_bda2013}} (Ch. 2, §2.4, pp. 34–35; Ch. 5, §§5.1–5.3, pp. 101–109)

## Definition
Write $\theta_j$ for group $j$'s parameter and $\phi$ for a parameter governing its population distribution. A common hierarchical model factors as $p(\phi)\prod_{j=1}^Jp(\theta_j\mid\phi)p(y_j\mid\theta_j)$ when groups are conditionally independent given their parameters. Here $\phi$ is a hyperparameter and $p(\phi)$ a hyperprior. A Beta population of rates has $\phi=(\alpha,\beta)$ with $\theta_j\mid\alpha,\beta\sim\operatorname{Beta}(\alpha,\beta)$. Its mean is $\alpha/(\alpha+\beta)$ and its total concentration $\alpha+\beta$ controls spread at a fixed mean. The model should state whether $\phi$ is fixed, estimated and plugged in, or assigned a posterior distribution.{{cite:gelman_bda2013}} (Ch. 2, §2.4, pp. 34–35; Ch. 5, §§5.1–5.3, pp. 104–109)

## Properties
With binomial observations $Y_j\mid\theta_j\sim\operatorname{Bin}(n_j,\theta_j)$, fixing $\alpha,\beta$ gives $\theta_j\mid\alpha,\beta,y_j\sim\operatorname{Beta}(\alpha+y_j,\beta+n_j-y_j)$. Its posterior mean is $(\alpha+y_j)/(\alpha+\beta+n_j)$: a weighted average of the population mean and the observed proportion $y_j/n_j$. The weight on the population mean is $(\alpha+\beta)/(\alpha+\beta+n_j)$, so a smaller group is pulled farther toward the population centre when the hyperparameters are held fixed. The q-23 example below computes this for two groups with the same observed proportion but different sizes.{{cite:gelman_bda2013}} (Ch. 2, §2.4, pp. 34–35; Ch. 5, §§5.1–5.3, pp. 102–109)

For a full Bayesian analysis, the relevant group posterior is $p(\theta_j\mid\mathbf y)=\int p(\theta_j\mid\phi,\mathbf y)p(\phi\mid\mathbf y)\,d\phi$. This averages the conditional Beta update over plausible hyperparameter values. It is generally different from inserting one fitted $\widehat\phi$ into that update. Integrating out each $\theta_j$ first gives the hyperposterior proportional to $p(\phi)\prod_jp(y_j\mid\phi)$, the principle behind the displayed marginal-hyperposterior property. A prior normalising factor may depend on $\phi$ and therefore cannot be discarded from this product.{{cite:gelman_bda2013}} (Ch. 5, §5.3, pp. 108–110)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For fixed positive $\alpha,\beta$, the Beta moment formulas give mean $m=\alpha/(\alpha+\beta)$ and variance $m(1-m)/(\alpha+\beta+1)$. At fixed $m$, increasing $\alpha+\beta$ therefore decreases the population variance. Multiply the binomial likelihood kernel $\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}$ by the Beta density kernel $\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}$. The powers combine to the Beta kernel with parameters $\alpha+y_j,\beta+n_j-y_j$. Taking its mean gives $(\alpha+y_j)/(\alpha+\beta+n_j)$. Expanding
$$
\frac{\alpha+\beta}{\alpha+\beta+n_j}\frac{\alpha}{\alpha+\beta}
+\frac{n_j}{\alpha+\beta+n_j}\frac{y_j}{n_j}
$$
recovers that mean, and the two weights sum to one. This is conditional shrinkage at a stated $\alpha,\beta$.{{cite:gelman_bda2013}} (Ch. 2, §2.4, pp. 34–35; Ch. 5, §5.3, pp. 108–109)

For the hyperposterior, integrate the joint density over each group rate. Its factor becomes $p(y_j\mid\alpha,\beta)=\binom{n_j}{y_j}B(\alpha+y_j,\beta+n_j-y_j)/B(\alpha,\beta)$. Multiplying these factors by $p(\alpha,\beta)$ gives the property formula. The binomial coefficient is constant as $\alpha,\beta$ vary, but $B(\alpha,\beta)^{-1}$ is not. Finally, the law of total probability yields the marginal integral for $\theta_j$; the law of total variance separates average conditional uncertainty from variation of the conditional mean as $\phi$ changes. A fixed plug-in value does not perform this averaging.{{cite:gelman_bda2013}} (Ch. 5, §5.3, pp. 108–110)
:::
:::

## Statistical use — Choosing a hyperparameter
Hyperparameters are useful when related groups have uneven sample sizes. A shared population distribution can stabilise small-group estimates while allowing large groups to be driven mainly by their own data. Before fitting, specify what makes groups comparable, select a sensible distribution for their parameters, and check how conclusions change under plausible hyperpriors. With few groups, the hyperposterior can be broad and sensitive to its prior, especially for a between-group scale. A computational method must explore that hyperposterior rather than report the conditional update at a single convenient value.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.3, 5.7, pp. 102–110, 128–132)

## Worked example
Take two hypothetical clinics with success counts $1$ of $4$ and $16$ of $40$. For illustration, hold the shared Beta hyperparameters at $\alpha=2,\beta=3$, giving a population mean $2/5=0.4$. The first clinic's conditional posterior is $\operatorname{Beta}(3,6)$ with mean $3/9=1/3$, between its observed $1/4$ and the population mean. The second has $\operatorname{Beta}(18,27)$ and mean $18/45=0.4$, equal to both its observed proportion and the population mean. The first clinic puts weight $5/9$ on the population mean; the second puts only $5/45=1/9$ on it. These are conditional results for the chosen hyperparameters. To make them full hierarchical results, the clinics would also inform $p(\alpha,\beta\mid\mathbf y)$, and each reported clinic posterior would average over that distribution.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.3, pp. 102–110)

**Your turn.** For a Beta population with fixed $\alpha=1,\beta=4$, one group has $2$ successes in $5$ trials. Find the prior mean, its conditional posterior mean, and the two weights in the weighted-average formula.{{cite:gelman_bda2013}} (Ch. 2, §2.4, pp. 34–35)

::: {.callout-tip collapse="true" title="Answer"}
The prior mean is $1/5=0.2$. The conditional posterior is $\operatorname{Beta}(3,7)$, with mean $3/10=0.3$. The population and data weights are both $5/10=1/2$, so $(1/2)(0.2)+(1/2)(2/5)=0.3$. Fixing $\alpha,\beta$ here is an explicit condition of the calculation; uncertainty in them would require another averaging step.
:::

## Common misconceptions
A hyperparameter is not necessarily known: in full Bayes it can have a posterior. Assigning it a hyperprior does not mean every group has the same parameter; the group parameters still vary under their shared population law. Conditional independence of groups given $\phi$ does not make their marginal posteriors independent after $\phi$ is integrated out. Nor is a plug-in estimate of $\phi$ automatically a full Bayesian analysis: it leaves out the uncertainty over plausible population distributions.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.3, pp. 101–110)

## Assumptions and limits — Exchangeability and prior sensitivity
The hierarchy can fail when groups are not meaningfully exchangeable. Gelman and colleagues note that historical animal studies conducted in one laboratory may not describe a current study in another, or that a time trend may invalidate a common population law. A Beta population also confines group rates to a particular shape family; a strongly bimodal set of groups may need a richer model. With only a handful of groups, a vague prior for a between-group scale can leave a very long posterior tail, as their three-school example shows. These are concrete model checks, not reasons to treat a fitted hyperparameter as certain.{{cite:gelman_bda2013}} (Ch. 5, §§5.1, 5.7, pp. 103–104, 128–132)

## Connections
A [hierarchical Bayesian model](hierarchical-bayesian-model.qmd) sets the levels in which hyperparameters appear. The [marginal hyperposterior](marginal-hyperposterior.qmd) updates them after lower-level parameters are integrated out. [Beta–Binomial conjugacy](beta-binomial-conjugacy.qmd) provides the conditional update, while [partial pooling](complete-pooling-no-pooling-and-partial-pooling.qmd) describes the resulting sharing of information. [Empirical Bayes](empirical-bayes.qmd) instead inserts estimated hyperparameters into lower-level calculations.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.3, pp. 101–110)

## History
The historical note in Gelman and colleagues' treatment identifies Good's 1965 work as an early thorough account of hierarchical Bayesian modelling and describes later normal and binomial developments. Their rat-study example builds on work by Tarone and by Dempster and colleagues in the early 1980s. The modern distinction between fixing population parameters and assigning them a full posterior is central to that account.{{cite:gelman_bda2013}} (Ch. 5, §5.8, pp. 132–133)
