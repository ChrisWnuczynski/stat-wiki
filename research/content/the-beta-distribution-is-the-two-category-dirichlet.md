## Motivating example
A binary outcome can be described by a single success probability $p$, or by the pair $(p,1-p)$. A prior for the pair must respect that constraint. Treating its coordinates as two independent beta variables would put probability on pairs whose sum differs from one. The two-category Dirichlet instead places all its probability on the line segment where the coordinates add to one. Its free coordinate has precisely a beta distribution.{{cite:downey2020_thinkbayes2}} (Ch. 18, “The Dirichlet Distribution”)

## Statement
A two-component Dirichlet vector is described by positive shape parameters $a,b$. The beta density for its first coordinate is
$$f(p)=\frac{p^{a-1}(1-p)^{b-1}}{B(a,b)},\qquad0<p<1,$$
where $B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$. The second coordinate is the deterministic complement. The Dirichlet kernel and its multinomial count update reduce to the beta kernel and binomial update when there are two categories.{{cite:gelman_bda2013}} (§3.4, p. 69) These formulas use density with respect to $dp$, the free-coordinate measure on the simplex. A density with respect to arc length along the embedded line segment would have a different constant, because its length element is $\sqrt2\,dp$. Probabilities are unchanged when density and measure are changed together.{{cite:dodge2008}} (p. 40, beta density and beta function)

## Intuition — Negative dependence is forced by the sum
The first coordinate has mean $a/(a+b)$ and variance $ab/[(a+b)^2(a+b+1)]$. The second has mean $b/(a+b)$ and the same variance. Because $P_2=1-P_1$,
$$\operatorname{Cov}(P_1,P_2)=-\operatorname{Var}(P_1).$$
For positive finite shapes that variance is positive, so their correlation is exactly $-1$. This is a constraint on a random vector, rather than evidence that a rise in one probability causes a fall in another. Beta moments give all these identities directly.{{cite:dodge2008}} (p. 40, beta moments)

Multiplying both concentrations by a common factor leaves the mean pair unchanged but changes its spread. Their sum describes concentration around the mean. The shapes themselves, rather than the number of categories alone, determine how much probability lies near either endpoint. Shapes below one can give an unbounded density at a boundary while the total integral remains finite.{{cite:dodge2008}} (p. 40)

## Proof
Put $K=2$ into the Dirichlet kernel $\prod_k p_k^{\alpha_k-1}$ and eliminate the second coordinate using $p_2=1-p_1$. The kernel becomes $p^{a-1}(1-p)^{b-1}$. Its integral over the free coordinate is $B(a,b)$, which is finite for positive shapes. Hence the normalised law is beta. The beta marginals of a general Dirichlet vector provide the same result: its first marginal has shapes $a$ and the sum of all other shapes, here just $b$.{{cite:downey2020_thinkbayes2}} (Ch. 18, “The Dirichlet Distribution”); {{cite:dodge2008}} (p. 40)

## Statistical use — One update expressed two ways
For counts $(x,n-x)$, a Dirichlet prior with concentrations $(a,b)$ updates to concentrations $(a+x,b+n-x)$. The single-probability description updates from $\operatorname{Beta}(a,b)$ to $\operatorname{Beta}(a+x,b+n-x)$. These calculations give identical posterior probabilities and predictive probabilities, because they describe the same random object in different coordinates. The vector notation is convenient when adding a third category; binary formulas cannot be extended by treating three probabilities as unconstrained independent variables.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood” and “The Dirichlet Distribution”)

## Worked example
### Updating a complementary pair
With concentrations $(2,3)$, the means are $0.4$ and $0.6$. The variance of either coordinate is $1/25=0.04$ and their covariance is $-0.04$. After four outcomes of the first kind and one of the second, the concentration pair is $(6,4)$. The mean pair becomes $(0.6,0.4)$ and its first-coordinate variance is $6/275\approx0.021818$. An additional outcome has probability $0.6$ of being in the first category.

**Your turn.** What is the posterior after two further outcomes in the second category?

::: {.callout-tip collapse="true" title="Answer"}
The shapes become $(6,6)$. The mean probability of either category is $1/2$, and the variance of the first probability is $1/52$.
:::

## Common misconceptions — Coordinate symmetry is conditional
Exchanging the labels exchanges the shapes. The distribution is invariant under exchanging the two labels only when $a=b$. A uniform distribution on the free coordinate is the special case $a=b=1$, rather than every symmetric beta law. Label exchange preserves the model family; it need not preserve a particular member of that family.{{cite:dodge2008}} (p. 40)
