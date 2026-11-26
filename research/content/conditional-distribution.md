## Lead context
It describes what remains uncertain about one variable when a value of another variable is known. The joint law determines these conditional laws; averaging them with the distribution of the known variable recovers the unconditional law. This is the basis of prediction and calculations that condition first and average later.{{cite:billingsley1995}} (§33, Ex. 33.5){{cite:durrett2019}} (Thm. 4.1.13)

## Motivating example
If a shop's daily takings depend on how many customers arrive, a distribution for spending conditional on a particular customer count answers a narrower question than the unconditional distribution of takings. The unconditional calculation must average over the possible counts. The day-of-takings example below does exactly this, separating uncertainty in spending per customer from uncertainty in the number of customers.{{cite:durrett2019}} (Thm. 4.1.13)

## Intuition
Conditioning changes which outcomes are still considered possible or how they are weighted. For discrete $X$, “given $X=x$” restricts attention to the positive-probability event $\{X=x\}$. For continuous $X$, that event typically has probability zero, so ordinary division by its probability cannot define the answer. When a joint density exists, a conditional density is a vertical slice of that density divided by the marginal density of $X$, at values where the marginal density is positive and finite. More generally, conditional laws form a measurable probability kernel. Changing that kernel only on a fixed set of conditioning values with marginal measure zero leaves the joint law unchanged, provided the modified kernel remains measurable. This does not permit arbitrary simultaneous changes at every zero-probability singleton: an uncountable union of marginal-null singletons need not have marginal measure zero.{{cite:kolmogorov1933_slln}} (Ch. V, §3){{cite:billingsley1995}} (§33, Ex. 33.5)

## Definition
Let $X$ and $Y$ be random variables with joint law $\mathbb P_{X,Y}$ and marginal law $\mathbb P_X$. A **conditional distribution** of $Y$ given $X$ assigns to each $x$ a probability law $K(x,\cdot)$ such that for Borel sets $A$ and $B$,

$$
\mathbb P(X\in A,Y\in B)=\int_A K(x,B)\,\mathbb P_X(\mathrm dx).
$$

Here $A$ specifies possible values of $X$, $B$ possible values of $Y$, and $K(x,B)$ is the conditional probability assigned to $Y\in B$ when $X=x$. The map $x\mapsto K(x,B)$ must be measurable. This identity explains what “given $X=x$” means even when $\mathbb P(X=x)=0$: conditional laws are determined by the joint law up to changes on $\mathbb P_X$-null sets. The conditional expectation of integrable $Y$ is the function $m(X)$ with $m(x)=\int y\,K(x,\mathrm dy)$ wherever the integral is defined.{{cite:kolmogorov1933_slln}} (Ch. V, §3){{cite:billingsley1995}} (§33, Ex. 33.5)

If $X,Y$ are discrete and $\mathbb P(X=x)>0$, then $K(x,\{y\})=\mathbb P(X=x,Y=y)/\mathbb P(X=x)$. If they have a joint density $f_{X,Y}$, define $f_X(x)=\int f_{X,Y}(x,y)\,\mathrm dy$. At marginal-almost-every $x$ with $f_X(x)>0$, a conditional density is $f_{Y\mid X}(y\mid x)=f_{X,Y}(x,y)/f_X(x)$. The quotient is a *density in $y$*, not the probability of the exact event $Y=y$. It is normalised by integrating over $y$. Values assigned where $f_X(x)=0$ are not identified by this ratio.{{cite:billingsley1995}} (§33, Ex. 33.5){{cite:kolmogorov1933_slln}} (Ch. V, §3)

## Properties
The joint law factors as marginal times conditional law. In the continuous density case this is $f_{X,Y}(x,y)=f_X(x)f_{Y\mid X}(y\mid x)$ wherever the quotient is defined; integrating over $x$ gives $f_Y(y)=\int f_{Y\mid X}(y\mid x)f_X(x)\,\mathrm dx$. The discrete versions replace the integral by a sum. This is the law of total probability: the marginal combines every possible conditioning value with its proper weight.{{cite:billingsley1995}} (§33, Ex. 33.5)

If $X$ and $Y$ are independent, the conditional law of $Y$ does not depend on $x$ for $\mathbb P_X$-almost every $x$: $K(x,B)=\mathbb P(Y\in B)$. Conversely, this equality for every Borel $B$, outside a common marginal-null set, gives a product joint law and hence independence. A conditional law can vary substantially even when the two marginal laws look simple.{{cite:billingsley1995}} (§33, Ex. 33.5)

For integrable $Y$, the [tower property](tower-property.qmd) is $\mathbb E\{\mathbb E(Y\mid X)\}=\mathbb E Y$. With another variable $Z$, its nested form is $\mathbb E\{\mathbb E(Y\mid X,Z)\mid X\}=\mathbb E(Y\mid X)$ almost surely. This gives a random-sum mean: if $N$ is a count independent of identically distributed spending values $V_i$ with mean $\mu$, then $\mathbb E(\sum_{i=1}^{N}V_i)=\mu\mathbb E N$. If the variances exist and the spending values are mutually independent, the variance is $\mathbb E N\,\operatorname{Var}(V_1)+\operatorname{Var}(N)\mu^2$.{{cite:durrett2019}} (§4.1, Thm. 4.1.13)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For discrete $X$, $\mathbb P(X=x,Y=y)=\mathbb P(X=x)\mathbb P(Y=y\mid X=x)$ is the definition of conditional probability on the event $\{X=x\}$. Summing over $x$ yields the marginal of $Y$, and summing over $y$ gives one for each conditional mass function. In the continuous case, $\int f_{X,Y}(x,y)/f_X(x)\,\mathrm dy=1$ when $f_X(x)>0$. Multiplying by $f_X(x)$ recovers the joint density, and integrating over $x$ gives the stated marginal formula by Fubini's theorem. Integrating the quotient over a set $B$ and then against $\mathbb P_X$ over $A$ verifies the defining identity for $K$.{{cite:billingsley1995}} (§33, Ex. 33.5)

If $K(x,B)=\mathbb P(Y\in B)$ almost everywhere, the defining identity becomes $\mathbb P(X\in A,Y\in B)=\mathbb P_X(A)\mathbb P_Y(B)$ for every $A,B$, which is independence. If $X,Y$ are independent, the same product identity shows that the constant assignment $K(x,B)=\mathbb P_Y(B)$ satisfies the defining identity, proving the converse up to null-set choices.{{cite:billingsley1995}} (§33, Ex. 33.5)

For an integrable $Y$, the defining property of conditional expectation is $\mathbb E\{\mathbf1_A\mathbb E(Y\mid X)\}=\mathbb E(\mathbf1_A Y)$ for each event $A$ determined by $X$. Taking $A=\Omega$ proves the first tower identity. For the nested identity, every event determined by $X$ is also determined by $(X,Z)$; applying the defining property first to $\mathbb E(Y\mid X,Z)$ and then to $Y$ gives the same integral over every such $A$. Uniqueness of conditional expectation up to almost-sure equality proves the nested form.{{cite:durrett2019}} (§4.1, Thm. 4.1.13)

For the random sum $S=\sum_{i=1}^{N}V_i$, independence and identical spending moments give $\mathbb E(S\mid N)=N\mu$ and $\operatorname{Var}(S\mid N)=N\sigma^2$, where $\sigma^2=\operatorname{Var}(V_1)$. The first tower identity gives $\mathbb E S=\mu\mathbb E N$. Also $\operatorname{Var}(S)=\mathbb E\{\operatorname{Var}(S\mid N)\}+\operatorname{Var}\{\mathbb E(S\mid N)\}$: expand $\mathbb E(S^2\mid N)=\operatorname{Var}(S\mid N)+\{\mathbb E(S\mid N)\}^2$, average, and subtract $(\mathbb E S)^2$. Substitution gives $\sigma^2\mathbb E N+\mu^2\operatorname{Var}(N)$, the stated formula.{{cite:durrett2019}} (§4.1, Thm. 4.1.13)
:::
:::

## Statistical use
A regression model specifies a conditional distribution of a response $Y$ given measured covariates $X=x$. Its conditional mean may be the main prediction, but a mean alone does not fix prediction intervals or tail probabilities; the conditional spread and shape also matter. A binary model, for example, gives a Bernoulli law with success probability depending on $x$, while a count model may use a Poisson law whose mean depends on $x$. Always say which variables and covariate values the prediction conditions on.{{cite:billingsley1995}} (§33, Ex. 33.5){{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–373)

In Bayesian analysis, a posterior distribution conditions a parameter on the observed data under a stated prior and likelihood. The same factorisation principle appears: joint equals marginal times conditional, with the normalising marginal obtained by summing or integrating over possible parameter values. A posterior is therefore a conditional law, and its value depends on the joint model chosen before observing data.{{cite:wang2025_foundations}} (Ch. 20, §24.1)

## Worked example
Suppose two binary variables have joint probabilities $\mathbb P(X=0,Y=0)=1/10$, $\mathbb P(X=0,Y=1)=2/10$, $\mathbb P(X=1,Y=0)=3/10$, and $\mathbb P(X=1,Y=1)=4/10$. Then $\mathbb P(X=0)=3/10$ and $\mathbb P(X=1)=7/10$. The conditional success probabilities are $\mathbb P(Y=1\mid X=0)=(2/10)/(3/10)=2/3$ and $\mathbb P(Y=1\mid X=1)=(4/10)/(7/10)=4/7$. Weighting them by their respective $X$ probabilities gives $(3/10)(2/3)+(7/10)(4/7)=6/10=\mathbb P(Y=1)$. The two conditional probabilities are different, so $X$ and $Y$ are not independent.{{cite:billingsley1995}} (§33, Ex. 33.5)

**Your turn.** For the same table, find $\mathbb P(X=1\mid Y=0)$.

::: {.callout-tip collapse="true" title="Answer"}
The probability of $Y=0$ is $1/10+3/10=4/10$. Therefore $\mathbb P(X=1\mid Y=0)=(3/10)/(4/10)=3/4$. Reversing the conditioning direction changes the denominator.
:::

A shop serves a random number of customers $N$ with mean 4 and variance 2. Given $N=n$, spending values are independent with mean 5 and variance 4, and they are independent of $N$. What are the mean and variance of total spending?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $5\times 4=20$. The variance is $4\times 4+2\times 5^2=16+50=66$.
:::

## Common misconceptions
A conditional law given a continuous value is not obtained by dividing by $\mathbb P(X=x)$, which is usually zero. A density at $y$ is not the probability of $Y=y$. Conditional probabilities at an isolated $x$ with zero marginal probability are not uniquely fixed by the joint law, even when a convenient density formula supplies a version. Marginals alone do not determine a conditional law; the joint distribution is required. Conditioning on $X$ need not remove all randomness in $Y$, and conditional independence is a different claim from marginal independence.{{cite:kolmogorov1933_slln}} (Ch. V, §3){{cite:billingsley1995}} (§33, Ex. 33.5)

## Assumptions and limits
The displayed quotient requires a positive marginal mass or density at the conditioning value and matching discrete or continuous joint and marginal representations. A general conditional law need not have either kind of quotient. Statements about versions are made up to $\mathbb P_X$-null sets; values at null conditioning points require an additional convention or model structure. The random-sum variance formula needs finite second moments and independent, identically distributed increments independent of $N$. The triangle figure and its companion example use different sampling rules: uniform on a finite lattice versus uniform $X$ followed by uniform $Y$ on a variable-length interval.{{cite:billingsley1995}} (§33, Ex. 33.5){{cite:durrett2019}} (§4.1, Thm. 4.1.13)

## Connections
[Conditional probability](conditional-probability.qmd) on a positive-probability event supplies the discrete quotient. A [joint density](joint-probability-density.qmd) and a marginal density supply the continuous quotient where it is defined. [Conditional expectation](conditional-expectation.qmd) averages a variable under its conditional law; the [tower property](tower-property.qmd) then averages over the conditioning variable. A [Bayesian posterior](../notes/bayes-01-foundations.qmd) is a conditional distribution of parameters given data. [Independent events](independent-events.qmd) and independent variables make appropriate conditional laws equal their marginal laws, almost surely.{{cite:billingsley1995}} (§33, Ex. 33.5){{cite:wang2025_foundations}} (Ch. 20, §24.1)

## History
Kolmogorov's 1933 *Grundbegriffe der Wahrscheinlichkeitsrechnung* treated conditional probability first with respect to events and then with respect to a random variable. In Chapter V §3 he related conditional probabilities to the distribution of the conditioning variable and noted that such quantities are determined outside a set of marginal probability zero. This formalised a question that elementary event division cannot settle at an isolated zero-probability value.{{cite:kolmogorov1933_slln}} (Ch. V, §§1–3)

Modern measure-theoretic accounts express conditioning through an identity involving every event in the information being conditioned on. Billingsley's discussion of a two-dimensional density gives the conditional distribution on a vertical slice and explicitly explains why division by the probability of that slice fails when it is zero. It also makes clear that values on marginal-null slices need a separate convention when a pointwise answer is wanted.{{cite:billingsley1995}} (§33, Ex. 33.5)
