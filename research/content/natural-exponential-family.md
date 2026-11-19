## Motivating example
Poisson counts and Bernoulli outcomes look different, but their likelihoods share a useful structure. Once the data enter the exponent through a sufficient statistic, a log normaliser supplies its moments by differentiation. Natural exponential families make this structure explicit.{{cite:dasgupta2011_exponential_family}} (§§18.1–18.2, pp. 498–506)

## Definition — Tilting a base measure
A one-dimensional natural exponential family has density or mass function
$$
f_\eta(x)=h(x)\exp\{\eta x-A(\eta)\},\qquad
A(\eta)=\log\int e^{\eta x}h(x)\,d\nu(x).
$$
The natural parameter space consists of the values for which the integral is finite. A general exponential family replaces $x$ by a statistic $T(x)$, possibly vector-valued. Thus a family may become natural after treating its sufficient statistic as the observation; the phrase should identify which variable is being tilted.{{cite:dasgupta2011_exponential_family}} (§18.2, canonical representation)

For a Poisson variable, $h(x)=1/x!$, $\eta=\log\lambda$, and $A(\eta)=e^\eta$. For a Bernoulli variable, $h(x)=1$ on $\{0,1\}$ and $A(\eta)=\log(1+e^\eta)$, so its natural parameter is the log odds. The support and base measure are part of the family, not terms that can be dropped when changing models.{{cite:dasgupta2011_exponential_family}} (§§18.1–18.2, Poisson and binomial examples)

## Properties — Moments from normalisation
At an interior parameter value where differentiation is valid,
$$
A'(\eta)=E_\eta(X),\qquad A''(\eta)=\operatorname{Var}_\eta(X).
$$
Differentiate $\int f_\eta(x)d\nu(x)=1$ to obtain $E(X-A')=0$. Differentiating again yields $E\{(X-A')^2-A''\}=0$. Thus the second derivative is nonnegative and $A$ is convex. For a nondegenerate family it is strictly positive, making the mean increase with the natural parameter.{{cite:dasgupta2011_exponential_family}} (§18.2.2, Thm. 18.3){{cite:nelder_wedderburn1972}} (§1.1, eqs. 3–6, p. 371)

For $n$ independent observations the log likelihood is $\eta\sum_i x_i-nA(\eta)$ plus a data-only term. The score is $\sum_i x_i-nA'(\eta)$ and its derivative is $-nA''(\eta)$. A finite stationary point therefore matches the model mean to the sample mean and maximises this concave log likelihood. The mean can lie at a boundary where no finite stationary point exists.{{cite:nelder_wedderburn1972}} (§§1.1, 2.2, pp. 371, 374)

## Worked example
For counts $0,1,5$, the total is $6$, the sample size is $3$, and the sample mean is $2$. The Poisson score $6-3e^\eta$ vanishes at $\widehat\eta=\log2=0.693147$, giving $\widehat\lambda=2$. The observed negative second derivative there is $3e^{\widehat\eta}=6$, equal to the expected information.{{cite:dasgupta2011_exponential_family}} (§18.2.2, moment identities)

If all three counts are zero, the likelihood increases as $\eta\to-\infty$ and $\lambda\downarrow0$. A maximum exists at $\lambda=0$ when that boundary is included, but there is no finite natural parameter corresponding to it.

**Your turn.** A Bernoulli sample has $4$ successes in $10$ trials. Find its fitted mean and natural parameter.

::: {.callout-tip collapse="true" title="Answer"}
The fitted mean is $0.4$, with natural parameter $\log(0.4/0.6)=\log(2/3)=-0.405465$.
:::
