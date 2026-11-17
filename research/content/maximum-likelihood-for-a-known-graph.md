## Motivating example
A Gaussian graphical model can specify that two variables are conditionally independent given the others while allowing them to remain marginally correlated. The corresponding zero lies in the precision matrix, not necessarily in the covariance matrix. Estimation for a known graph therefore requires a coherent positive-definite matrix satisfying all the precision zeros together; zeroing selected sample covariances generally fits a different model.{{cite:dempster1972_cov}} (p. 157, covariance-selection formulation)

## Definition — Optimise over a convex precision domain
For iid $X_i\sim N_p(\mu,\Sigma)$, write $S=n^{-1}\sum_i(X_i-\bar X)(X_i-\bar X)^\top$ and $\Theta=\Sigma^{-1}$. After maximising over the unrestricted mean, the log-likelihood divided by $n/2$ is
$$L(\Theta)=\log\det\Theta-\operatorname{tr}(S\Theta)+C.$$
For every absent edge $i\ne j$, impose $\Theta_{ij}=0$, and require $\Theta\succ0$. The feasible set is an intersection of the positive-definite cone and a linear subspace, hence convex. The zero pattern is supplied in advance; estimating which zeros to impose is an additional model-selection problem.{{cite:wainwright_jordan2008}} (§3.3, Gaussian graphical models, pp. 44–45; §6.1, maximum likelihood)

## Properties — Score equations match free sufficient statistics
Put $W=\Theta^{-1}$. A permitted symmetric perturbation $H$ changes $L$ at first order by $\operatorname{tr}[(W-S)H]$, because $d\log\det\Theta[H]=\operatorname{tr}(\Theta^{-1}H)$. Perturbing a diagonal entry gives $w_{ii}=s_{ii}$ at an interior optimum. Perturbing both symmetric positions on an edge gives $2(w_{ij}-s_{ij})=0$, so covariance entries match the sample entries on every edge as well. For a missing edge that perturbation is forbidden, and its covariance need not match the sample value. These are exponential-family moment-matching equations for the free parameters.{{cite:speed_kiiveri1986}} (§3, p. 142, eq. 4)

For a nonzero symmetric direction $H$, the second derivative of $L(\Theta+tH)$ at zero is $-\operatorname{tr}(\Theta^{-1}H\Theta^{-1}H)$. Set $B=\Theta^{-1/2}H\Theta^{-1/2}$ to rewrite this as $-\operatorname{tr}(B^2)<0$. Strict concavity implies that a feasible solution of the score equations is the unique global maximum whenever a finite interior maximiser exists. Thus verifying feasibility and edge matching is a direct way to certify a computed fit.{{cite:wainwright_jordan2008}} (§3.5.1, convexity of the log partition function; §6.1, likelihood moment matching)

For the block update, write $\beta=W_{AA}^{-1}w_{AB}$. The block equations in $W\Theta=I$ give $\theta_{AB}=-\beta\theta_{BB}$ and $1/\theta_{BB}=w_{BB}-w_{AB}^\top\beta$. Prescribed precision zeros therefore become zeros in $\beta$. Matching the free edge covariances then gives $W_{AA}^{*}\beta^{*}=s_{AB}^{*}$, followed by $w_{AB}=W_{AA}\beta$. This derives the reduced regression equations while keeping the covariance and precision constraints distinct.{{cite:friedman_glasso2008}} (§2, p. 435, eqs. 2.13–2.14)

## Worked example — Complete a three-node chain
Let the graph have edges $1$–$2$ and $2$–$3$, and take
$$S=\begin{pmatrix}1&2/5&3/10\\2/5&1&1/2\\3/10&1/2&1\end{pmatrix}.$$
A fitted covariance must match its diagonal and two edge entries, leaving only $w_{13}$ free. The $(1,3)$ entry of the inverse is zero precisely when $w_{13}=w_{12}w_{23}/w_{22}=1/5$. Thus
$$W=\begin{pmatrix}1&2/5&1/5\\2/5&1&1/2\\1/5&1/2&1\end{pmatrix},\qquad
\widehat\Theta=\begin{pmatrix}25/21&-10/21&0\\-10/21&32/21&-2/3\\0&-2/3&4/3\end{pmatrix}.$$
The leading principal minors of $W$ are $1$, $21/25$ and $63/100$, all positive. This proves feasibility. The inverse has the required zero and the covariance matches all free sufficient statistics, so strict concavity certifies the fit. The marginal covariance $w_{13}=1/5$ remains nonzero.

**Your turn.** Keep the diagonal variances equal to one, but change $s_{12}$ to $1/5$ and $s_{23}$ to $3/5$. What chain-completion value is required for $w_{13}$?

::: {.callout-tip collapse="true" title="Answer"}
The chain constraint gives $w_{13}=w_{12}w_{23}/w_{22}=(1/5)(3/5)=3/25$. The zero belongs to the inverse covariance, not to this completed covariance entry.
:::

## Statistical use — Check a fitting algorithm against its equations
A block-regression sweep updates one variable at a time, using only its permitted graph neighbours and filling its covariance row consistently. On a chain the completion can be written explicitly, while general graphs can require repeated sweeps. At termination, compare the imposed precision zeros, the free covariance entries and positive definiteness. A small change between successive iterates is useful diagnostic information but is weaker than checking these defining conditions.{{cite:friedman_glasso2008}} (§2, p. 435, eqs. 2.13–2.14)

## Assumptions and limits — Singularity changes existence
When $S\succ0$, the Gaussian objective has a well-behaved finite fit for a fixed zero pattern. If $S$ is singular, constrained maximum likelihood can still exist for some graphs and fail for others. The graph structure and sample configuration then matter. The inverse of a singular sample covariance is unavailable, and a numerical routine must not silently replace it with an unconstrained generalised inverse and call the result the constrained MLE. Gaussian conditional-independence interpretation also relies on a jointly Gaussian model; a zero precision entry outside that family does not generally establish conditional independence.{{cite:speed_kiiveri1986}} (§3, Theorem 1, pp. 142–143; §2, Gaussian conditional independence)
