## Motivating example

A small regression estimates a mean response and an error variance from the same observations. Treating the error variance as known makes coefficient uncertainty look too simple, while assigning unrelated priors to coefficients and variance loses an especially convenient joint update. The normal–inverse-Gamma family ties the coefficient prior spread to the residual variance. Multiplying that prior by a Gaussian likelihood produces another member of the same family, so both uncertainties can be updated exactly.{{cite:gelman_bda2013}} (Ch. 3, §3.3, pp. 67–69){{cite:forssen_ekstrom2026}} (Ch. 25, §§25.1–25.2, eqs. 25.2 and 25.7)

Conjugate families became especially useful when posterior integrals had to be done analytically. The normal–inverse-chi-squared form in Gelman and colleagues' account is the same joint idea under a different variance parameterization; translating that convention is necessary before comparing update formulas.{{cite:forssen_ekstrom2026}} (Ch. 25, §25.1, motivation for conjugate priors){{cite:gelman_bda2013}} (Ch. 3, §3.3, pp. 67–69)

## Statement

The inverse-Gamma convention here uses shape $a$ and scale $b$: its density kernel in $v=\sigma^2$ is $v^{-a-1}\exp(-b/v)$ on $v>0$. The conditional normal prior has covariance $vV_0$, not merely $V_0$. This shared factor of $v$ is what makes the joint family closed under the normal regression likelihood. The updated $V_n$ in the statement is a covariance *scale*; the actual conditional covariance is $\sigma^2V_n$. Integrating over $\sigma^2$ yields a heavier-tailed marginal distribution for $\boldsymbol\beta$.{{cite:gelman_bda2013}} (Ch. 3, §3.3, pp. 67–69){{cite:forssen_ekstrom2026}} (Ch. 25, §§25.1–25.2, eqs. 25.2–25.8)

## Key results

The posterior inverse-Gamma shape adds $n/2$ because the likelihood of $n$ independent normal responses contributes a factor $(\sigma^2)^{-n/2}$. The updated scale adds half a nonnegative penalized sum of squares to $b_0$. This latter term measures fit after the coefficient estimate balances data and prior, so it is not generally the ordinary residual sum of squares at an unpenalized estimate. The posterior marginal of $\boldsymbol\beta$ is multivariate Student with $2a_n$ degrees of freedom, centre $\boldsymbol m_n$, and scale matrix $(b_n/a_n)V_n$.{{cite:forssen_ekstrom2026}} (Ch. 25, §25.2, eqs. 25.7–25.8)

When $a_n>1$, the posterior mean of $\sigma^2$ is $b_n/(a_n-1)$; its mode is $b_n/(a_n+1)$. Neither equals $b_n$ or $b_n/a_n$. If the shape is at most one, the posterior variance mean does not exist even though the posterior is proper. A fitted mean at a new predictor value is uncertain through $\boldsymbol\beta$; a new response has that uncertainty *plus* a fresh residual, so its predictive spread is wider.{{cite:forssen_ekstrom2026}} (Ch. 25, §§25.1–25.3, eqs. 25.4, 25.8)

## Worked example

For an intercept-only model, observe $y=(2,4)$ and set the design matrix to a column of two ones. Take $\beta\mid\sigma^2\sim N(0,\sigma^2)$, so $m_0=0$, $V_0=1$, and put $\sigma^2\sim\operatorname{InvGamma}(2,3)$. The design has $X^\top X=2$ and $X^\top y=6$, hence $V_n=(1+2)^{-1}=1/3$ and $m_n=(1/3)(6)=2$. The shape becomes $a_n=2+2/2=3$. Since $y^\top y=2^2+4^2=20$ and $m_n^2/V_n=4/(1/3)=12$, the updated scale is $b_n=3+(20-12)/2=7$. Thus $\beta\mid\sigma^2,y\sim N(2,\sigma^2/3)$ and $\sigma^2\mid y\sim\operatorname{InvGamma}(3,7)$.{{cite:forssen_ekstrom2026}} (Ch. 25, §25.2, eq. 25.7)

The posterior variance mean is $7/(3-1)=3.5$, whereas its mode is $7/(3+1)=1.75$. Marginally, $\beta$ has a Student law with $2a_n=6$ degrees of freedom, centre $2$, and scale $\sqrt{(7/3)(1/3)}=\sqrt7/3\approx0.88192$. The heavier tails come from averaging over possible residual variances, not from changing the conditional normal form.{{cite:forssen_ekstrom2026}} (Ch. 25, §§25.1–25.2, eqs. 25.4 and 25.8)

**Your turn.** Keep that intercept-only prior but observe $y=(1,3)$. Compute the posterior $m_n$, $V_n$, $a_n$, and $b_n$, then give the mean and mode of $\sigma^2\mid y$.

::: {.callout-tip collapse="true" title="Answer"}
Now $X^\top y=4$ and $y^\top y=10$. Hence $V_n=1/3$, $m_n=4/3$, $a_n=3$, and $b_n=3+\{10-(4/3)^2/(1/3)\}/2=3+(10-16/3)/2=16/3$. The posterior variance mean is $(16/3)/(3-1)=8/3\approx2.667$, and its mode is $(16/3)/(3+1)=4/3\approx1.333$. The coefficient centre has moved toward the new sample mean, while the prior still contributes one unit of precision.{{cite:forssen_ekstrom2026}} (Ch. 25, §§25.1–25.2, eqs. 25.4 and 25.7)
:::

## Common misconceptions

Conjugacy is a statement about the joint prior and posterior family, not a guarantee that the Gaussian sampling model fits the data. The prior for $\beta$ is conditionally normal but not independent of $\sigma^2$: changing variance changes its conditional spread. $V_n$ is not itself the posterior covariance of $\beta$, and the inverse-Gamma scale $b_n$ is not the posterior mean of $\sigma^2$. Finally, a posterior mean for $\sigma^2$ need not exist for every positive shape even though the posterior density is proper.{{cite:gelman_bda2013}} (Ch. 3, §3.3, pp. 67–69){{cite:forssen_ekstrom2026}} (Ch. 25, §§25.1–25.2)

## Generalizations — When conjugacy is inadequate

The formulas presume a common Gaussian error variance. If one observation is an extreme outlier under a heavy-tailed process, $y^\top y$ can dominate the scale update and the conjugate posterior can be confidently wrong about a misspecified model. If variance differs by predictor value, one common $\sigma^2$ cannot describe the errors. A Laplace coefficient prior or a non-Gaussian response generally breaks this exact normal–inverse-Gamma update, though numerical posterior computation can still be used. These cases call for a model change, not merely new hyperparameter values.{{cite:gelman_bda2013}} (Ch. 3, §3.3, pp. 67–69, outlying-measurement example){{cite:forssen_ekstrom2026}} (Ch. 25, §25.1, scope of conjugate model)
