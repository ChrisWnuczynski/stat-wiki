## Motivating example
Two regression coefficients can have an approximately elliptical posterior at any fixed noise variance. If that variance is uncertain, a mixture over ellipse scales has heavier tails. Distinguishing the conditional normal distribution from the marginal Student distribution prevents a normal standard deviation from being mistaken for a marginal credible-interval scale.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

## Key results — Least-squares geometry fixes the conditional covariance
For $y\mid\beta,v\sim N_n(X\beta,vI)$ and reference prior $p(\beta,v)\propto1/v$ relative to $d\beta\,dv$, put $C=(X^\top X)^{-1}$. At fixed $v>0$,
$$
\beta\mid v,y,X\sim N_p(\hat\beta,vC).
$$
Its covariance depends on predictor geometry as well as the noise variance. For any fixed vector $a$, $a^\top\beta\mid v,y,X\sim N(a^\top\hat\beta,v a^\top Ca)$. Cross-covariances of coefficients matter when computing uncertainty for a fitted mean.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21){{cite:pishro_nik2014}} (§6.1.5)

The least-squares identity is
$$
\|y-X\beta\|^2=SSE+(\beta-\hat\beta)^\top X^\top X(\beta-\hat\beta).
$$
The cross term is zero by $X^\top(y-X\hat\beta)=0$. At fixed $v$, the first term is constant in $\beta$ and the second is a normal quadratic with precision $X^\top X/v$. Full column rank makes that precision positive definite. With the reference prior, propriety of the full joint posterior additionally requires $n>p$ and positive SSE.{{cite:prado_ferreira_west2021}} (§§1.5.2–1.5.3.1, pp. 20–21)

For a nonzero contrast $a$, let $c=a^\top Ca$, $m=a^\top\hat\beta$, $\nu=n-p$ and $s^2=SSE/\nu$. Integrating its normal conditional against $v\mid D\sim\operatorname{InvGamma}(\nu/2,SSE/2)$ gives a density proportional to
$$
\int_0^\infty v^{-(\nu+3)/2}
\exp\!\left[-\frac{SSE+(u-m)^2/c}{2v}\right]dv
\ \propto\ \left\{1+\frac{(u-m)^2}{\nu s^2c}\right\}^{-(\nu+1)/2}.
$$
The substitution $z=\{SSE+(u-m)^2/c\}/(2v)$ reduces the integral to a gamma integral. This identifies $a^\top\beta\mid D\sim t_\nu(m,s\sqrt c)$ and explains the heavier tails directly.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

## Generalizations — Prior precision adds to data precision
For a proper normal prior $\beta\sim N(m_0,V_0)$ independent of a fixed $v$, the same square completion gives
$$
V_n=(X^\top X/v+V_0^{-1})^{-1},\qquad
m_n=V_n(X^\top y/v+V_0^{-1}m_0).
$$
The posterior is $N(m_n,V_n)$. The reference conditional is obtained by setting prior precision to zero when the likelihood has full rank. A proper prior can regularise a rank-deficient design, but its posterior centre need not equal the unregularised least-squares estimate.{{cite:rasmussen_williams2006}} (§2.1.1, pp. 8–10, eqs. 2.7–2.8)

## Worked example

### Covariance between intercept and slope
For $x=(0,1,2,3,4)$ and $y=(1,2,1,4,2)$, the least-squares estimate and inverse cross-product matrix are
$$
\hat\beta=\begin{pmatrix}1.2\\0.4\end{pmatrix},\qquad
C=\begin{pmatrix}0.6&-0.2\\-0.2&0.1\end{pmatrix},\qquad SSE=4.4.
$$
At $v=1$, conditional standard deviations are $\sqrt{0.6}=0.774597$ and $\sqrt{0.1}=0.316228$; at $v=4$ each doubles. For the mean response at $x_*=2$, $a=(1,2)^\top$ gives $a^\top Ca=0.2$, not $0.6+4(0.1)=1$. The covariance term $4(-0.2)$ accounts for the difference.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21){{cite:pishro_nik2014}} (§6.1.5)

Here the variance marginal is $\operatorname{InvGamma}(3/2,2.2)$, using density proportional to $v^{-a-1}e^{-b/v}$. The slope marginal is $t_3(0.4,\sqrt{(4.4/3)(0.1)})$, with location and scale as displayed. Its probability of being positive is $0.813489$. The heavier-tailed marginal averages uncertainty over $v$, rather than replacing it by a single estimate.{{cite:prado_ferreira_west2021}} (§1.5.3.1, p. 21)

**Your turn.** In this example, what are the conditional mean and variance of $\beta_0+2\beta_1$ when $v=4$?

::: {.callout-tip collapse="true" title="Answer"}
The mean is $1.2+2(0.4)=2$. The variance is $4(0.2)=0.8$.
:::
