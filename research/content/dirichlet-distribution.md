## Motivating example
An election poll offers three response categories, and the quantity of interest is the vector of population proportions rather than one success probability. Those proportions must be nonnegative and add to one. A Dirichlet distribution describes uncertainty across that simplex and makes a multinomial update especially simple: each observed category count is added to the matching concentration parameter. Gelman and colleagues use exactly this construction for a three-response election poll.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

## Intuition
Write $\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_K)$ and $\alpha_0=\sum_k\alpha_k$. The ratios $\alpha_k/\alpha_0$ locate the mean probability vector, whereas the common total $\alpha_0$ controls how tightly draws gather around it. Raising every $\alpha_k$ by the same factor leaves the mean fixed but reduces variability. Because the components must sum to one, a larger draw for one category leaves less for the others. The simplex figures show that geometry: equal parameters keep the centre at $(1/3,1/3,1/3)$, while concentration values $0.1$, $1$ and $5$ change the spread from corner-heavy to centre-heavy.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

## Definition
For $K\ge2$ and every $\alpha_k>0$, $\boldsymbol P\sim\operatorname{Dirichlet}(\boldsymbol\alpha)$ has density on the interior of the probability simplex

$$
f(\boldsymbol p)=\frac{\Gamma(\alpha_0)}{\prod_{k=1}^{K}\Gamma(\alpha_k)}\prod_{k=1}^{K}p_k^{\alpha_k-1},
\qquad p_k>0,\quad\sum_{k=1}^{K}p_k=1.
$$

This is a density with respect to $(K-1)$-dimensional simplex coordinates, not a density over an unconstrained $K$-dimensional box. The closed simplex includes its faces; for positive parameters those faces have probability zero, even if a density tends to infinity near one. The normalizing factor is a multivariate beta integral. The density formula is evaluated on the interior of the simplex, where the stated support condition holds.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

## Properties
The coordinate mean is $\E(P_k)=\alpha_k/\alpha_0$, and its variance is $\alpha_k(\alpha_0-\alpha_k)/\{\alpha_0^2(\alpha_0+1)\}$. For distinct categories, $\operatorname{Cov}(P_j,P_k)=-\alpha_j\alpha_k/\{\alpha_0^2(\alpha_0+1)\}<0$. The negative covariance expresses the fixed-sum constraint; it is not an assumption that people choosing different categories are negatively associated. The second moments also give $\E(P_k^2)=\alpha_k(\alpha_k+1)/\{\alpha_0(\alpha_0+1)\}$ and $\E(P_jP_k)=\alpha_j\alpha_k/\{\alpha_0(\alpha_0+1)\}$.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

One component has a $\operatorname{Beta}(\alpha_j,\alpha_0-\alpha_j)$ marginal. More generally, grouping categories adds their concentration parameters: $P_1+P_2$ has beta shapes $\alpha_1+\alpha_2$ and $\alpha_0-\alpha_1-\alpha_2$. This is useful when the question concerns “positive response” across several survey subcategories. With $K=2$, the entire vector is $(P,1-P)$ and $P$ is beta. The proof in Properties uses independent gamma variables divided by their sum to establish the beta marginal; the same construction explains why grouping gamma components adds shapes.{{cite:gelman_bda2013}} (Ch. 3, §3.4)

When every $\alpha_k>1$, the joint density peaks inside the simplex at $p_k=(\alpha_k-1)/(\alpha_0-K)$. That *joint* mode need not equal the mean or the mode of a single beta marginal. If a concentration parameter is at or below one, this interior formula is inapplicable and the density can be flat or rise toward a face. The three-panel figure illustrates why a single phrase such as “centred on the mean” does not describe all parameter choices.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

## Related distributions
The [Beta distribution](beta-distribution.qmd) is the two-category case and the marginal law of any one component after the others are combined. Independent [Gamma distributions](gamma-distribution.qmd) with a common rate provide a sampling construction: divide each gamma draw by their sum. The [multinomial distribution](multinomial-distribution.qmd) counts categorical outcomes conditional on a fixed probability vector; a Dirichlet distribution places uncertainty on that vector. These relationships connect the density's algebra to simulation and inference.{{cite:gelman_bda2013}} (Ch. 3, §3.4)

## Statistical inference
If counts $\boldsymbol x=(x_1,\ldots,x_K)$ sum to $n$, the multinomial likelihood contributes $\prod_kp_k^{x_k}$. Multiplying by the Dirichlet prior gives posterior kernel $\prod_kp_k^{\alpha_k+x_k-1}$, so $\boldsymbol P\mid\boldsymbol x\sim\operatorname{Dirichlet}(\boldsymbol\alpha+\boldsymbol x)$. The posterior predictive probability of the next observation falling in category $k$ is $(\alpha_k+x_k)/(\alpha_0+n)$. This predictive average reflects uncertainty in the probability vector; the category probability itself remains uncertain after observing the counts.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

A three-category example starts with $\operatorname{Dirichlet}(2,3,5)$ and adds counts $(4,1,0)$, giving $\operatorname{Dirichlet}(6,4,5)$ and posterior mean $6/15=0.4$ for the first category, up from $2/10=0.2$. In the six-cell advertising table, $501$ observations update a uniform $\operatorname{Dirichlet}(1,1,1,1,1,1)$ prior to $(54,58,148,94,39,114)$. Its male-negative posterior mean $54/507\approx0.1065$ differs from its joint MAP component $53/501\approx0.1058$. These are distinct summaries of the same posterior; the MAP formula uses an interior mode, which holds for those updated cell parameters.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

## Worked example
Take a symmetric three-category prior $\boldsymbol P\sim\operatorname{Dirichlet}(1,1,1)$ and observe counts $(2,3,1)$. The posterior is $\operatorname{Dirichlet}(3,4,2)$, with total concentration $9$ and posterior mean $(1/3,4/9,2/9)$. The predictive chance of category two on the next draw is $4/9\approx0.444444$. Its marginal probability $P_2$ has $\operatorname{Beta}(4,5)$ distribution and variance $4\cdot5/(9^2\cdot10)=2/81\approx0.024691$. Meanwhile $\operatorname{Cov}(P_1,P_2)=-3\cdot4/(9^2\cdot10)=-2/135\approx-0.014815$. The negative covariance belongs to the uncertain probabilities: increasing one component of a probability vector forces some others down.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

**Your turn.** Start with $\operatorname{Dirichlet}(1,2,1)$ and observe counts $(3,0,1)$. Give the posterior, its mean vector, the predictive probability of category one or three on the next draw, and the beta marginal and variance of $P_1$.

::: {.callout-tip collapse="true" title="Answer"}
The posterior is $\operatorname{Dirichlet}(4,2,2)$ with total $8$, so its mean is $(4/8,2/8,2/8)=(0.5,0.25,0.25)$. Categories one or three together have predictive probability $(4+2)/8=0.75$. The marginal $P_1$ is $\operatorname{Beta}(4,4)$ and its variance is $4\cdot4/(8^2\cdot9)=1/36\approx0.027778$.
:::

## Common misconceptions
The $\alpha_k$ are positive concentration parameters, not probabilities that must sum to one; their *ratios* set the mean. The Dirichlet components are not independent, even when their gamma generators were independent before normalization. A uniform Dirichlet density on the simplex, obtained when all $\alpha_k=1$, does not make the marginal distribution of every coordinate uniform when $K>2$: the marginal is $\operatorname{Beta}(1,K-1)$. Finally, the joint mode formula applies only when every $\alpha_k>1$ and should not be substituted for the posterior mean.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

## Assumptions and limits — When a Dirichlet prior is too simple
A Dirichlet vector cannot express positive covariance between two distinct category probabilities because its covariance is always negative. For example, if two party preferences tend to rise together across regions at the expense of a third, a single Dirichlet prior cannot represent that joint uncertainty without additional structure. A concentration vector also fixes a particular mean direction; if yesterday's restaurant frequencies reflect a different population from today's, treating them as strong prior counts can distort the update. Finally, placing zero in an $\alpha_k$ does not give a proper Dirichlet member under this positive-parameter definition; special improper priors need separate posterior-propriety checks.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70, improper-prior discussion)

## Connections
Dirichlet–multinomial [conjugacy](dirichlet-multinomial-conjugacy.qmd) updates every category together. [Dirichlet moments](dirichlet-moments.qmd) quantify uncertainty and dependence, while the [interior mode](interior-dirichlet-mode.qmd) gives a different summary when all shapes exceed one. The simplex is the geometric reason the components cannot vary independently. The figures and advertising example show these relationships for three and six categories.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)

## History
The Dirichlet name recalls the multivariate beta integral that normalizes the density. Its modern statistical use as a prior for multinomial probabilities follows from the componentwise count update, as illustrated in Gelman and colleagues' categorical-data chapter. The older name identifies the distribution's analytic origin, while the conjugacy explains its role in Bayesian data analysis.{{cite:gelman_bda2013}} (Ch. 3, §3.4, pp. 69–70)
