## Motivating example
A nonlinear statement about regression coefficients, such as a joint sign restriction, may be easier to assess with posterior draws than with a closed-form probability integral. In conjugate normal regression, a variance marginal and a normal coefficient conditional can be sampled directly. Fresh randomness in each repetition gives independent pairs without a Markov-chain iteration.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

## Key results — A marginal followed by a conditional
Under the reference prior $p(\beta,v)\propto1/v$, full column rank, $n>p$ and positive SSE, put $a=(n-p)/2$, $b=SSE/2$ and $C=(X^\top X)^{-1}$. The joint posterior factorisation is
$$
p(\beta,v\mid D)=p(v\mid D)p(\beta\mid v,D),\qquad
v\mid D\sim\operatorname{InvGamma}(a,b),\quad
\beta\mid v,D\sim N_p(\hat\beta,vC).
$$
Drawing in this order produces that joint density. Repeating with independent inputs produces iid pairs, although the coordinates within a pair generally depend on one another. Drawing coefficients independently from their separate marginals would usually destroy their posterior dependence.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

Let $L$ be a Cholesky factor with $LL^\top=C$. Independently draw $G\sim\operatorname{Gamma}(a,1)$ in shape–rate form and $Z\sim N_p(0,I)$, then set
$$
v=b/G,\qquad\beta=\hat\beta+\sqrt v\,LZ.
$$
The reciprocal change of variables gives the inverse-gamma marginal. Conditional on $v$, the affine-normal rule gives the required covariance $vLL^\top=vC$. A triangular solve can implement the same transformation without explicitly constructing an inverse matrix.{{cite:pishro_nik2014}} (§6.1.5, normal random vectors){{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

## Generalizations — Prediction adds a further conditional draw
At a future design vector $x_*$, a draw of the latent mean is $x_*^\top\beta$. A new observation additionally draws an independent residual $\sqrt v Z_*$, giving $\widetilde y=x_*^\top\beta+\sqrt v Z_*$. This distinguishes uncertainty about the mean from the extra noise of a new response. At fixed $v$, their variances are $v x_*^\top Cx_*$ and $v(1+x_*^\top Cx_*)$.{{cite:rasmussen_williams2006}} (§2.1.1, pp. 9–11){{cite:pishro_nik2014}} (§6.1.5)

Replacing the variance marginal by its full conditional $p(v\mid\beta,D)$ and alternating with a coefficient full conditional instead constructs a Gibbs chain. Direct sampling needs an available marginal; it does not follow merely from knowing all full conditionals. Conversely, an independently specified prior does not automatically rule out analytic marginalisation and direct sampling.{{cite:prado_ferreira_west2021}} (§§1.5.3.1–1.5.3.2, pp. 21–24)

## Worked example

### A regression probability and its simulation error
Use $n=10,p=2$, $\hat\beta=(1,2)^\top$, $C=\operatorname{diag}(1/10,1/40)$ and $SSE=16$. Direct draws use $v\sim\operatorname{InvGamma}(4,8)$ followed by $\beta\mid v,D\sim N_2(\hat\beta,vC)$. The slope marginal is $t_8(2,\sqrt{0.05})$, so
$$
\mathbb{P}(\beta_1>1.5\mid D)=0.9721167.
$$
For $M=10{,}000$ independent pairs, averaging $\mathbf1\{\beta_1^{(m)}>1.5\}$ has standard deviation $\sqrt{q(1-q)/M}\approx0.001646$, where $q$ is that probability. This is Monte Carlo error conditional on the model and observed data, rather than uncertainty about which statistical model is appropriate.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

**Your turn.** What happens to that Monte Carlo standard deviation when the number of independent pairs increases fourfold?

::: {.callout-tip collapse="true" title="Answer"}
The variance of an average of independent Bernoulli indicators is $q(1-q)/M$. Four times as many draws halves its standard deviation, to about $0.000823$.
:::
