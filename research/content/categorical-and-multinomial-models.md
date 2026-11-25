## Motivating example
An observer can record each customer's chosen category, or record only the total in each category. A categorical model describes one label. A multinomial model describes the count vector from a fixed number of independent labels with common category probabilities. Aggregating discards order, so a combinatorial factor is needed when calculating the probability of a count vector.{{cite:dodge2008}} (p. 363)

## Definition — Count the sequences behind a table
Let $Y_1,\ldots,Y_n$ be independent with $\Pr(Y_i=k)=p_k$ for $k=1,\ldots,K$, and $\sum_kp_k=1$. Then $X_k=\sum_i\mathbf1\{Y_i=k\}$ has joint probability
$$\Pr(X=x)=\frac{n!}{\prod_kx_k!}\prod_kp_k^{x_k},\qquad x_k\ge0,\quad\sum_kx_k=n.$$
Every sequence having those counts has the same product probability, and there are $n!/\prod_kx_k!$ such sequences. For likelihood comparisons as a function of $p$, this factor is constant, but it remains essential to the probability of the observed counts.{{cite:dodge2008}} (pp. 363–364)

## Properties — A fixed total creates negative covariance
Writing each count as a sum of category indicators gives $\E(X_k)=np_k$ and $\operatorname{Var}(X_k)=np_k(1-p_k)$. For distinct categories, the two indicators for one trial cannot both equal one, so their covariance is $-p_jp_k$. Independence between different trials then gives $\operatorname{Cov}(X_j,X_k)=-np_jp_k$, which is strictly negative when $n>0$ and $p_jp_k>0$; if one of the two probabilities is zero, that count is constant at $0$ and the covariance is $0$. Each marginal count is binomial, but the count vector has dependent coordinates because its components sum to the nonrandom total $n$.{{cite:durrett2019}} (§3.10, p. 201, multinomial vector)

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

## Intuition
A categorical draw is one label. A multinomial vector counts how many of $n$ independent labels fell in each category. The probability of one specific sequence with counts $x$ is $\prod_k p_k^{x_k}$. Every sequence with those counts has that same probability, and there are $n!/\prod_k x_k!$ such sequences. Multiplying by the combinatorial factor converts a sequence probability into a count probability. For the probabilities $p=(1/2,1/3,1/6)$ and counts $(2,1,1)$ in four draws, the factor is $4!/(2!1!1!)=12$ and the count probability is $12\cdot(1/2)^2\cdot(1/3)\cdot(1/6)=1/6$. Likelihood comparisons in $p$ can ignore the factor because it does not depend on $p$. Probability calculations for the table cannot ignore it.

The counts are dependent even though the labels are independent. One more label in category $1$ is one fewer label for the other categories, because the total is fixed at $n$. The covariance $\operatorname{Cov}(X_j,X_k)=-np_j p_k$ for $j\neq k$ is the numerical form of that constraint. With $n=4$ and the probability vector $p=(1/2,1/3,1/6)$ of the worked example, $\operatorname{Cov}(X_1,X_2)=-4\cdot(1/2)\cdot(1/3)=-2/3$. The margins are still binomial: $\E(X_1)=2$ and $\E(X_2)=4/3$. An expectation need not be an integer that the count can attain.

### Properties — Predictive probabilities after a Dirichlet update
A Dirichlet prior with parameters $\alpha_k$ has density proportional to $\prod_k p_k^{\alpha_k-1}$ on the simplex. Multiplying by the multinomial likelihood adds $x_k$ to the $k$th parameter. After counts $(2,1,1)$ and a $\operatorname{Dirichlet}(1,1,1)$ prior, the posterior is $\operatorname{Dirichlet}(3,2,2)$ and the probability that the next label falls in category $1$ is $3/7$. A further label in category $3$ moves the parameters to $(3,2,3)$, and the probability for category $3$ on a sixth label is $3/8$.

Zero counts do not force a zero predictive probability while the prior parameters stay positive. Counts $(3,0,0)$ with the same prior give posterior $\operatorname{Dirichlet}(4,1,1)$. The probability of category $2$ on the next draw is $1/6$. The size of that smoothing is the prior parameter, not a property of the multinomial coefficient. A prior $\operatorname{Dirichlet}(0.1,0.1,0.1)$ would smooth less. The update rule is the same. The numerical probability is not.

The fixed-total constraint also determines a missing cell. Six labels in four categories, with three of the counts equal to $1$, $2$, and $0$, leave $6-3=3$ for the remaining category. The model does not need a probability vector to enforce that arithmetic. It needs the probability vector to say how likely that table was.

## Common misconceptions
Independent binomial margins are sometimes multiplied together and called a multinomial likelihood. Independent binomials do not force the counts to sum to a common $n$, and their covariance is zero. The multinomial covariance is $-np_jp_k$, strictly negative when $n>0$ and $p_jp_k>0$. A product of binomial likelihoods answers a different sampling story, one in which each category count comes from its own set of trials. Contingency tables add a further distinction. A single multinomial sample over the cells of a table is not the same design as independent multinomial samples in each row, and neither is the same as sampling without replacement from a finite population. The likelihood factor and the covariance formula have to match the design that was actually used.{{cite:durrett2019}} (§3.10, p. 201, multinomial vector)

A noninteger expected count is not a defect in the calculation. $E(X_2)=4/3$ in the worked example. The count $X_2$ itself is an integer on every outcome. The expectation averages those integers. Rounding $4/3$ to $1$ before computing a variance or a covariance replaces the model by a different summary.

## Connections
The binomial distribution is the multinomial model with two categories. The Poisson model for independent counts, conditioned on their sum, returns a multinomial distribution. That conditioning is why a set of independent Poisson means, once the total is fixed, acquires the multinomial covariances $-np_jp_k$. Dirichlet–multinomial conjugacy is the Bayesian update of the Properties section: it stays inside the Dirichlet family when one fixed probability vector is shared by all $n$ labels. When the shared probability is instead random, drawn once and then used for every label, each marginal count is overdispersed relative to the binomial variance at the mean probability $\bar p_k=\E(P_k)$, namely $n\bar p_k(1-\bar p_k)$: the extra marginal variance is $n(n-1)\operatorname{Var}(P_k)$. That excess is strictly positive only when $n>1$ and $\operatorname{Var}(P_k)>0$; it is zero for a single label ($n=1$), and zero when $P_k$ is degenerate, which is the fixed-probability multinomial case itself. The counts still sum to $n$. A goodness-of-fit comparison that assumes the multinomial variance will read that extra variation as a lack of fit; the [Dirichlet–multinomial](dirichlet-multinomial-conjugacy.qmd) model exists to separate the two sources of variation.
