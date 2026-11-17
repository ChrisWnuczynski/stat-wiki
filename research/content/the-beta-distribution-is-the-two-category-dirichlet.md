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

## Key results — The complement carries the same variance and the opposite covariance
If $P_1\sim\operatorname{Beta}(3,2)$, then $E(P_1)=3/5=0.6$ and $\operatorname{Var}(P_1)=3\cdot2/(5^2\cdot6)=6/150=1/25=0.04$. The complement $P_2=1-P_1$ has mean $2/5=0.4$ and the same variance $1/25$. Their covariance is $-1/25$, so the correlation is $-1$ whenever the variance is positive. That correlation is the geometry of the line $p_2=1-p_1$. It is not an estimated association between two free probabilities. A density written with respect to arc length on that segment uses the factor $\sqrt2\,dp$ and a different normalising constant; probabilities of the same sub-arcs agree once the density and the measure are changed together.{{cite:dodge2008}} (p. 40, beta moments){{cite:gelman_bda2013}} (§3.4, p. 69)

A Dirichlet$(1,1)$ prior is uniform on the free coordinate. Counts $(2,5)$ update it to concentrations $(3,6)$. The posterior mean of the first coordinate is $3/9=1/3$. The same update in beta notation runs from $\operatorname{Beta}(1,1)$ to $\operatorname{Beta}(3,6)$. After the worked concentrations $(6,4)$, two further outcomes in the second category produce $(6,6)$. The mean of either coordinate is $1/2$ and the variance is $6\cdot6/(12^2\cdot13)=36/1872=1/52\approx0.019231$. The variance fell because the concentration rose from $10$ to $12$, and the mean moved to the centre because the two shapes became equal.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood” and “The Dirichlet Distribution”)

### The beta integral is the Dirichlet normaliser on the segment
The map $(p,1-p)$ sends $(0,1)$ onto the interior of the two-point simplex. Substituting into $\prod_k p_k^{\alpha_k-1}$ leaves $p^{a-1}(1-p)^{b-1}$. The integral of that kernel is $B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$, finite for every $a>0$ and $b>0$. Dividing by $B(a,b)$ produces the beta density of the free coordinate and, with it, the law of the pair. For $\operatorname{Beta}(2,3)$ the kernel is proportional to $p(1-p)^2$. The constant that integrates $p(1-p)^2$ over $(0,1)$ to one is $12$, because $B(2,3)=1!\,2!/4!=1/12$. The mean of this density is $\int_0^1 p\cdot12p(1-p)^2\,dp=2/5$, in agreement with $a/(a+b)$. Shapes below one keep the integral finite and can make the density unbounded at an endpoint. The mean and variance formulae still apply.{{cite:dodge2008}} (p. 40, beta density and beta function){{cite:downey2020_thinkbayes2}} (Ch. 18, “The Dirichlet Distribution”)

## Related concepts
The binomial update of a beta prior is the two-category case of the multinomial update of a Dirichlet prior. Adding a third category removes the identity $P_2=1-P_1$ and replaces the correlation $-1$ by a negative covariance that is no longer a perfect line. The full-conditional beta updates used for several study rates are a different construction: each rate has its own beta law, and the categories of one rate are not the coordinates of a shared Dirichlet vector unless that is the model being specified.{{cite:gelman_bda2013}} (§3.4, p. 69){{cite:downey2020_thinkbayes2}} (Ch. 18, “The Dirichlet Distribution”)
