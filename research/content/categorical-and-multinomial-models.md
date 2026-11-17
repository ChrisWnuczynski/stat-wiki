## Motivating example — Labels and count vectors answer different questions
An observer can record each customer's chosen category, or record only the total in each category. A categorical model describes one label. A multinomial model describes the count vector from a fixed number of independent labels with common category probabilities. Aggregating discards order, so a combinatorial factor is needed when calculating the probability of a count vector.{{cite:dodge2008}} (p. 363)

## Definition — Count the sequences behind a table
Let $Y_1,\ldots,Y_n$ be independent with $\Pr(Y_i=k)=p_k$ for $k=1,\ldots,K$, and $\sum_kp_k=1$. Then $X_k=\sum_i\mathbf1\{Y_i=k\}$ has joint probability
$$\Pr(X=x)=\frac{n!}{\prod_kx_k!}\prod_kp_k^{x_k},\qquad x_k\ge0,\quad\sum_kx_k=n.$$
Every sequence having those counts has the same product probability, and there are $n!/\prod_kx_k!$ such sequences. For likelihood comparisons as a function of $p$, this factor is constant, but it remains essential to the probability of the observed counts.{{cite:dodge2008}} (pp. 363–364)

## Properties — A fixed total creates negative covariance
Writing each count as a sum of category indicators gives $E(X_k)=np_k$ and $\operatorname{Var}(X_k)=np_k(1-p_k)$. For distinct categories, the two indicators for one trial cannot both equal one, so their covariance is $-p_jp_k$. Independence between different trials then gives $\operatorname{Cov}(X_j,X_k)=-np_jp_k$. Each marginal count is binomial, but the count vector has dependent coordinates because its components sum to the nonrandom total $n$.{{cite:durrett2019}} (§3.10, p. 201, multinomial vector)

For a Dirichlet prior with positive parameters $\alpha_k$, multiplication by the multinomial likelihood changes each exponent from $\alpha_k-1$ to $\alpha_k+x_k-1$. Hence posterior parameters are $\alpha_k+x_k$, and the predictive probability of the next category is $(\alpha_k+x_k)/(\sum_j\alpha_j+n)$. The prior sample-size interpretation of the total concentration should be used with the chosen parameter convention stated explicitly.{{cite:downey2020_thinkbayes2}} (Ch. 18, “The Dirichlet Distribution”)

## Worked example — Three categories and four observations
Let $p=(1/2,1/3,1/6)$ and $n=4$. For $x=(2,1,1)$, there are $4!/(2!1!1!)=12$ corresponding ordered sequences, giving count probability $12(1/2)^2(1/3)(1/6)=1/6$. The first two counts have covariance $-4(1/2)(1/3)=-2/3$. Their expected values are $2$ and $4/3$, respectively; a noninteger expectation is compatible with integer observations. These are direct consequences of the indicator representation.{{cite:dodge2008}} (pp. 363–364)

With a $\operatorname{Dirichlet}(1,1,1)$ prior and those counts, the posterior is $\operatorname{Dirichlet}(3,2,2)$. Its predictive probabilities are $(3/7,2/7,2/7)$. Positive concentration parameters give positive predictive probability to a category even when its observed count is zero; the size of this smoothing depends on the stated prior.{{cite:downey2020_thinkbayes2}} (Ch. 18, Dirichlet updating)

**Your turn.** Under that same prior, observe a fifth label in category three. What is its posterior predictive probability for a sixth label?

::: {.callout-tip collapse="true" title="Answer"}
The posterior parameters become $(3,2,3)$, so the probability for category three is $3/8$.
:::

## Assumptions and limits — Independence and a common probability vector
A fixed multinomial model is inappropriate when category probabilities vary between observations or outcomes cluster beyond what the model allows. Conditional multinomial sampling with a random common probability vector can represent extra variation, but it changes the marginal model. Sampling without replacement from a finite population instead leads to a multivariate hypergeometric count law. Counts alone do not reveal which sampling mechanism produced them.{{cite:grinstead_snell1997}} (§3.2, sampling without replacement; §5.1, important distributions)
