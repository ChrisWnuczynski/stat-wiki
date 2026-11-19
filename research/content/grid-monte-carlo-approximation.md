## Motivating example
A posterior involving two hyperparameters may be evaluated accurately on a rectangular grid even when direct sampling is awkward. Once the grid weights are normalised, independent samples can be drawn from that finite approximation. This separates the numerical approximation of a density from the random error of Monte Carlo summaries.{{cite:downey2020_thinkbayes2}} (§§13.2–13.4)

## Definition — Cell masses before random draws
Let $q(z)$ be an unnormalised posterior density, and partition a bounded integration region into cells $C_i$ with representative points $z_i$ and volumes $v_i$. A midpoint approximation assigns
$$
w_i=q(z_i)v_i,\qquad p_i=\frac{w_i}{\sum_jw_j}.
$$
The weights must be finite and nonnegative, with a positive total. The common volume cancels on an equally spaced grid. For unequal cells, normalising density heights alone changes their relative probability masses. The resulting finite distribution approximates the posterior on the chosen region; its accuracy depends on the domain and resolution.{{cite:downey2020_thinkbayes2}} (§§13.2–13.3, grid posterior construction){{cite:grinstead_snell1997}} (§2.2, density and probability)

## Interpretation — Inverting the cumulative weights
Flatten the cells into a list and form $F_i=\sum_{j\le i}p_j$. An independent uniform draw selects the first index with $F_i\ge U$. The interval of uniforms selecting cell $i$ has length $p_i$, proving that the draw has the desired cell probabilities. Repeating with independent uniforms produces independent cell indices.{{cite:grinstead_snell1997}} (§1.1, simulation of discrete distributions)

A draw placed at $z_i$ has a discrete distribution. Adding uniform jitter within the chosen cell instead produces a piecewise-constant density with that cell's mass $p_i$. These are distinct approximations, although they give the same cell probabilities. A grid can also be used deterministically: $\sum_i p_i g(z_i)$ is the expectation under the discrete approximation and has no Monte Carlo sampling error.{{cite:grinstead_snell1997}} (§§2.1–2.2)

## Worked example — What additional simulation changes
At points $0,1,2$, suppose the unnormalised masses are $1,2,1$. The normalised probabilities are $(1/4,1/2,1/4)$, the cumulative probabilities are $(1/4,3/4,1)$, and the mean is $1$. The variance is $1/2$, giving standard error $\sqrt{0.5/10000}=0.007071$ for the average of $10000$ independent draws. Summing the three weighted values gives the same mean exactly under this finite distribution.{{cite:grinstead_snell1997}} (§§6.1–6.2, expectation and variance)

More draws reduce sampling uncertainty around that grid expectation. They do not recover probability mass outside the chosen region or resolve variation within a cell. Those require expanding the domain or refining the grid, followed by comparing the posterior summaries. Posterior marginal distributions can be computed by summing weights over the other coordinates.{{cite:downey2020_thinkbayes2}} (§13.4)

**Your turn.** Two cells have equal density height but volumes $1$ and $3$. What are their normalised probabilities?

::: {.callout-tip collapse="true" title="Answer"}
Their masses are proportional to volume, giving probabilities $1/4$ and $3/4$. Equal density heights do not imply equal probability for unequal cells.
:::

## Properties — Transformations and conditional simulation
For a smooth invertible parameter transformation, the density on the grid is $q_z(z)=q_\theta(\theta(z))|\det D\theta(z)|$. For $\alpha=e^{z_1}$ and $\beta=e^{z_2}$, the determinant is $\alpha\beta$. The Jacobian belongs in the density before the cell-volume factor; applying it twice changes the target.{{cite:pishro_nik2014}} (§5.2.4, method of transformations)

After drawing hyperparameters, independently drawing the remaining parameters from their conditional posterior completes one draw from the approximating joint model. For a beta–binomial hierarchy this gives $\theta_j\mid\alpha,\beta,y\sim\operatorname{Beta}(y_j+\alpha,n_j-y_j+\beta)$. Independence between repetitions comes from fresh independent random inputs at every stage. It differs from constructing a Markov chain whose successive states are dependent.{{cite:downey2020_thinkbayes2}} (§18.4, beta–binomial conjugacy; Ch. 19, MCMC)
