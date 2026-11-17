## Motivating example
After a regression has estimated its coefficients, the residual sum of squares still leaves uncertainty about the noise variance. Integrating over coefficient uncertainty gives a distribution for that variance. Its residual degrees of freedom depend on how many independently estimable coefficients were fitted.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

## Statement
Let $y\mid\beta,v\sim N_n(X\beta,vI)$ with $X$ of full column rank $p$, $n>p$, and positive residual sum of squares $R$. Under $\pi(\beta,v)\propto1/v$ with respect to $d\beta\,dv$,
$$
v\mid y,X\sim\operatorname{InvGamma}\left(\frac{n-p}{2},\frac R2\right),\qquad
f(v)\propto v^{-(n-p)/2-1}\exp\{-R/(2v)\},\quad v>0.
$$
The rank and residual conditions make this posterior proper. The prior remains improper; a proper posterior does not provide a normalised prior predictive distribution.{{cite:prado_ferreira_west2021}} (§1.5.3.1, pp. 21–22)

## Intuition — Integrating a normal volume
The coefficient posterior at fixed $v$ is normal, with covariance $v(X^\top X)^{-1}$. Its normalising volume is proportional to $v^{p/2}$. Integrating the coefficient kernel therefore subtracts $p/2$ from the inverse-gamma shape implied by the likelihood power. Fixing the coefficients and integrating them answer different questions.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

## Proof
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The least-squares equations give
$$
\|y-X\beta\|^2=R+(\beta-\widehat\beta)^\top X^\top X(\beta-\widehat\beta).
$$
The joint posterior kernel is $v^{-n/2-1}$ times the exponential of minus this expression divided by $2v$. Integrating the quadratic exponential over $\mathbb R^p$ contributes $(2\pi v)^{p/2}|X^\top X|^{-1/2}$. The remaining variance kernel is precisely $v^{-(n-p)/2-1}e^{-R/(2v)}$. Under $w=R/v$, the Jacobian gives the chi-squared kernel with $n-p$ degrees of freedom.{{cite:prado_ferreira_west2021}} (§§1.5.2–1.5.3.1, pp. 20–21)
:::
:::

## Statistical use — A distribution before a loss function
The inverse-gamma law gives a posterior mean $R/(n-p-2)$ when $n-p>2$ and a mode $R/(n-p+2)$. A positive residual degree of freedom makes the distribution proper but does not ensure a finite mean. Choosing a mean, median, or mode is an additional decision about how to summarise posterior uncertainty. Sensitivity to a variance prior also depends on the model and the amount of information available.{{cite:gelman2006}} (§§2.1–2.2, pp. 516–517)

## Worked example
With $n=10$, $p=2$ and $R=16$, the posterior is $\operatorname{InvGamma}(4,8)$. Its mean is $8/3=2.666667$, its mode is $8/5=1.6$, and the residual estimate is $R/(n-p)=2$. The posterior variance is $8^2/\{(4-1)^2(4-2)\}=32/9$. These different summaries describe the same positively skewed distribution.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

**Your turn.** If $n-p=2$ and $R=4$, is the variance posterior proper? Does its mean exist?

::: {.callout-tip collapse="true" title="Answer"}
The law is $\operatorname{InvGamma}(1,2)$ and is proper. Its mean is infinite because the shape is $1$.
:::
