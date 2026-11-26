## Motivating example

A clinic measures the same binary health outcome twice for each patient. If the aim is the average risk among treated and untreated patients, the two observations from one person still belong together: shared circumstances can make their outcomes more alike than outcomes from different people. A marginal model states the mean risk at each covariate value and records enough within-person association for estimation and uncertainty calculations. It lets the treatment coefficient describe a population-average comparison rather than a hypothetical change within one particular person.{{cite:liang_zeger1986}} (§1, pp. 13–14, longitudinal motivation and marginal approach)

## Intuition

The mean curve answers a question across people: at a given age or treatment, what outcome is expected in the target population? A subject-specific model instead describes differences conditional on a person's latent traits or history. These can point in different directions if the mix of people changes with the covariate, as the maternal-age schematic above illustrates. Within-person dependence matters even when the desired coefficient is marginal, because repeated outcomes do not supply the same information as the same number of independent people.{{cite:liang_zeger1986}} (§1, pp. 13–14, population focus and repeated responses)

## Definition

Let $Y_j=(Y_{j1},\ldots,Y_{jm_j})^\top$ be the responses in cluster $j$, with mean vector $\mu_j(\beta)$. A common generalized linear marginal model specifies $g(\mu_{ji})=X_{ji}^\top\beta$ and $\operatorname{Var}(Y_{ji}\mid X_{ji})=\phi V(\mu_{ji})$. The link $g$ describes the population-average mean on a convenient scale; $V$ supplies the variance associated with each mean. A working correlation matrix $R_j(\alpha)$ then combines the marginal variances into $V_j=\phi A_j^{1/2}R_j(\alpha)A_j^{1/2}$, where $A_j$ has the variance-function values on its diagonal. The working matrix guides weighting and need not specify a full joint distribution.{{cite:liang_zeger1986}} (§§1, 3.1, pp. 14–16, marginal mean and working correlation)

The three ingredients in the definition above have different jobs. The mean model defines the coefficient's interpretation; the variance function scales each component; the within-cluster association describes how much information repeated observations contribute together. Clusters are usually assumed independent of one another even though observations within a cluster can be correlated. Calling the association *working* makes clear that its fitted form is a tool for estimation and may differ from the unknown true association. {{cite:liang_zeger1986}} (§§2–3, pp. 14–16, independent subjects and working matrix)

## Interpretation — Population average and individual path

For a logit link with binary outcomes, $\beta$ compares the log odds of the *marginal* success probabilities at two covariate values. It does not generally equal the log odds comparison for one person held at a fixed latent risk level. The same distinction applies to the maternal-age drawing: the blue curve compares the population at each age, while red paths trace people. The two slopes can differ because the populations being compared differ, and a working correlation choice does not by itself redefine the mean target.{{cite:liang_zeger1986}} (§1, pp. 13–14, marginal rather than conditional modelling)

The second figure below concerns two different responses from the same patient. Each response may have its own marginal mean and variance, while shared patients make the estimated slope pair correlated. Separate marginal intervals form a rectangle; a joint confidence region uses their covariance and has a different geometry. Its exact shape needs the *estimated* cross-response covariance, so a schematic ellipse should not be read as a reported fitted region. {{cite:liang_zeger1986}} (§3.1, pp. 15–16, covariance of estimating equations)

## Properties — Estimating the mean with clustered outcomes

Let $D_j=\partial\mu_j/\partial\beta^\top$. Generalized estimating equations solve

$$
U(\beta)=\sum_jD_j^\top V_j^{-1}\{Y_j-\mu_j(\beta)\}=0.
$$

If the mean is correct, the residual vector has conditional expectation zero at the true $\beta$, even when the working $V_j$ is not the true covariance. This gives the equation its central robustness property. It does **not** say every working matrix produces identical fitted coefficients or standard errors: different weights can yield different finite-sample solutions and efficiencies. The large-sample claim also needs enough independent clusters, well-behaved cluster sizes and leverage, and a defensible account of missing observations. {{cite:liang_zeger1986}} (§§2–3, pp. 14–16; §6, pp. 20–21, consistency and missingness)

The usual model-based covariance treats the working $V_j$ as correct. A cluster sandwich instead places empirical cluster score cross-products between two sensitivity matrices. In shorthand, $\widehat{\operatorname{Var}}(\widehat\beta)\approx B^{-1}MB^{-1}$, where $B=\sum_jD_j^\top V_j^{-1}D_j$ and $M=\sum_jU_jU_j^\top$ with $U_j=D_j^\top V_j^{-1}(Y_j-\mu_j)$. This uses cluster residual variation to allow misspecification of within-cluster covariance. It does not repair an incorrect mean, informative missingness, or a tiny number of independent clusters. {{cite:liang_zeger1986}} (§§2–3, pp. 14–16, covariance formula and conditions)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
At the true mean parameter $\beta_0$, suppose $\E(Y_j\mid X_j)=\mu_j(\beta_0)$. If $D_j$ and a nonsingular working $V_j$ are functions of the covariates and parameters, then $\E\{D_j^\top V_j^{-1}(Y_j-\mu_j(\beta_0))\mid X_j\}=D_j^\top V_j^{-1}\E\{Y_j-\mu_j(\beta_0)\mid X_j\}=0$. Summing over clusters gives an unbiased estimating equation regardless of whether $V_j$ equals the true covariance. This calculation explains the target; independent-cluster laws of large numbers and further regularity are needed to conclude consistency of its root.{{cite:liang_zeger1986}} (§3.1, pp. 15–16, estimating equation and consistency conditions)

For Bernoulli variables $A,B$ with means $0.2,0.8$, the joint success probability satisfies $P(A=1,B=1)\le\min(0.2,0.8)=0.2$. Thus $\operatorname{Cov}(A,B)\le0.2-(0.2)(0.8)=0.04$. Each variance is $0.2(0.8)=0.16$, so their standard-deviation product is $0.16$ and their correlation cannot exceed $0.04/0.16=0.25$. A mathematically positive-definite working correlation larger than that would not describe a genuine joint Bernoulli law with these particular margins. The elementary bound is why the association parameter must be interpreted with care. {{cite:liang_zeger1986}} (§1, pp. 13–14, marginal model without a specified joint law)
:::
:::

## Statistical use

Start with the scientific unit that can reasonably be treated as independent, such as a person, school or factory. Specify the marginal response mean and the covariates that answer the question, then choose a plausible working correlation—independence, exchangeable or a time-lag pattern—based on the measurements. Fit the estimating equations and report a cluster-based covariance estimate together with the number and sizes of clusters. Compare plausible mean specifications and investigate how missing visits arose. A robust standard error is a large-sample device, not an assurance that a correct-looking number can be extracted from only a few clusters.{{cite:liang_zeger1986}} (§§3–4, pp. 15–18, working structures; §6, pp. 20–21, missing data)

The warp-break analysis has two factories as its clusters. Its differing naive and sandwich columns are useful evidence that the covariance choice matters to the calculation, but two factories do not support the many-independent-clusters approximation behind an inferential claim. The burn-response ellipse likewise reminds us that two outcomes on one patient can move together even when each marginal regression is understandable on its own. {{cite:liang_zeger1986}} (§§2–3, pp. 14–16, independent-subject asymptotics)

If treatment affects who returns for a second visit, the observed visit mean can differ from the intended population mean; ordinary GEE with a misspecified working association has no automatic protection against such informative missingness. If one factory supplies almost all observations while only one other factory remains, the cluster sandwich has too few independent units for its large-sample rationale. And a binary pair with marginal probabilities $0.2$ and $0.8$ cannot have true correlation $0.6$: its maximum is $0.25$, as shown above. These are different failures of observation process, effective sample size and joint feasibility.{{cite:liang_zeger1986}} (§§3, 6, pp. 15–16, 20–21, missingness and independent clusters)
## Worked example

Suppose four untreated and four treated patients each have two binary visits. Untreated patient pairs are $(0,0),(0,0),(1,1),(0,0)$; treated pairs are $(1,1),(1,1),(0,0),(1,1)$. The observed marginal risks are $2/8=0.25$ and $6/8=0.75$, so the risk difference is $0.50$. Their odds are $1/3$ and $3$, giving a marginal odds ratio of $9$ and log odds contrast $\log9\approx2.1972$. These are comparisons of average visit risk across the two patient groups, not within-patient treatment changes.{{cite:liang_zeger1986}} (§1, pp. 13–14, population-averaged interpretation)

The repeated visits affect precision. The four per-person outcome means are $(0,0,1,0)$ untreated and $(1,1,0,1)$ treated. Within either group their sample variance is $0.25$, so a simple cluster-level standard error for the difference of group means is $\sqrt{0.25/4+0.25/4}\approx0.3536$. Pretending all eight visits in each group were independent Bernoulli observations gives $\sqrt{0.25(0.75)/8+0.75(0.25)/8}\approx0.2165$. The second calculation double-counts the information when paired visits agree perfectly. Neither number by itself licenses a confidence interval with only four independent patients per group. {{cite:liang_zeger1986}} (§§1–2, pp. 13–15, repeated-outcome dependence and independent clusters)

**Your turn.** Change one treated patient's pair from $(1,1)$ to $(1,0)$. What are the new treated marginal risk, risk difference and marginal odds ratio? Keep the untreated outcomes fixed.

::: {.callout-tip collapse="true" title="Answer"}
The treated group now has five events in eight visits, so its marginal risk is $5/8=0.625$. Against the unchanged untreated risk $2/8=0.25$, the risk difference is $0.625-0.25=0.375$. The treated odds are $5/3$ and the untreated odds are $1/3$, so their ratio is $5$. The altered visit belongs to one patient cluster; it has not created a new independent patient.
:::

## Common misconceptions

A population-average coefficient is not automatically the effect of changing one person's exposure; the two questions condition on different information. A working correlation supplies weights and can differ from the true association. A sandwich covariance is not a cure for a wrong mean: if a relevant mean covariate is omitted, residual reweighting cannot restore its interpretation. More visits are also not equivalent to more independent patients, because visit outcomes from one person can remain strongly associated.{{cite:liang_zeger1986}} (§§1–3, pp. 13–16, target, weighting and assumptions)

## Connections

[Generalised estimating equations](generalised-estimating-equations.qmd) supply the estimating rule for the mean parameters; [working correlation](working-correlation.qmd) specifies the chosen within-cluster weighting; and the [sandwich estimator](sandwich-estimator.qmd) estimates coefficient uncertainty from cluster scores. [Repeated measures](repeated-measures.qmd) describe one common data layout. [Marginal and conditional effects](marginal-and-conditional-effects.qmd) distinguish the population question from an individual-level one, while [two responses, one person](two-responses-one-person.qmd) extends the issue to different outcomes on the same unit.{{cite:liang_zeger1986}} (§§1–3, pp. 13–16)

## History

Liang and Zeger developed generalized estimating equations for longitudinal data in 1986. Their construction retained a marginal generalized linear mean while using a working correlation to account for repeated observations, avoiding the need to specify a full joint response distribution. The original paper already separated a correctly specified mean from a potentially imperfect working dependence model and gave independent-subject large-sample covariance results. That separation remains the reason marginal models are useful when scientific interest lies in population-average associations.{{cite:liang_zeger1986}} (Summary; §§1–3, pp. 13–16)
