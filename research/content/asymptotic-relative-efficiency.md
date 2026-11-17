## Motivating example
The sample median resists extreme observations, while the sample mean uses their magnitudes. For normal measurements, how many observations does the median need to match the mean's large-sample precision? Asymptotic relative efficiency compares the leading variance constants after putting both estimators on the same sampling scale.{{cite:durrett2019}} (§3.4.1, Thm. 3.4.1, p. 144){{cite:siegrist2022_order_statistics}} (§ “Distribution of the kth Order Statistic”)

## Interpretation — State the direction of comparison
Suppose $\sqrt n(T_{j,n}-\theta)\Rightarrow N(0,\tau_j^2)$ with $0<\tau_j^2<\infty$. The efficiency of procedure two relative to procedure one is $\operatorname{ARE}(T_2;T_1)=\tau_1^2/\tau_2^2$. Matching $\tau_1^2/n_1$ with $\tau_2^2/n_2$ gives $n_2/n_1\approx1/\operatorname{ARE}(T_2;T_1)$. Stating numerator and denominator prevents a sample-size interpretation from being reversed. The normal approximation for an average follows from its finite-variance central limit theorem.{{cite:durrett2019}} (§3.4.1, Thm. 3.4.1, p. 144)

## Properties — Deriving the median's limiting variance
Let $n$ be odd and the common distribution have a unique median $m$ and positive continuous density $f$ near $m$. The event $M_n\le x$ says that at least $(n+1)/2$ observations lie at or below $x$, so its probability is a binomial upper tail with success probability $F(x)$.{{cite:siegrist2022_order_statistics}} (§ “Distribution of the kth Order Statistic”)

For $x_n=m+t/\sqrt n$, differentiability gives $F(x_n)=1/2+f(m)t/\sqrt n+o(n^{-1/2})$. The centred binomial count has variance $nF(x_n)\{1-F(x_n)\}\sim n/4$. Its standardised cutoff tends to $-2f(m)t$. A triangular-array central limit theorem applies because the bounded Bernoulli summands, divided by their diverging standard deviation, satisfy the Lindeberg condition. Therefore
$$
P\{\sqrt n(M_n-m)\le t\}\longrightarrow\Phi\{2f(m)t\},
$$
proving asymptotic variance $1/\{4f(m)^2\}$. The requirements on the median and density matter: a zero density or nonunique median can change the rate and the limit.{{cite:durrett2019}} (§3.4.2, Thm. 3.4.10, p. 148)

## Worked example — A normal mean and median
For $N(\mu,\sigma^2)$ observations, $f(\mu)=1/(\sigma\sqrt{2\pi})$. The mean has asymptotic variance constant $\sigma^2$; the median has $\pi\sigma^2/2$. Thus the median's efficiency relative to the mean is $2/\pi=0.636620$. To match a mean based on $64$ observations, the leading-order median calculation gives $64\pi/2=100.530965$, or $101$ after rounding up. This is an asymptotic planning comparison, not an exact finite-sample equality.{{cite:siegrist2022_order_statistics}} (§ “Distribution of the kth Order Statistic”){{cite:durrett2019}} (§3.4.1, p. 144)

**Your turn.** If procedure two has variance constant three and procedure one has variance constant two, what is procedure two's efficiency and required sample-size multiplier?

::: {.callout-tip collapse="true" title="Answer"}
The efficiency is $2/3$, so procedure two needs approximately $3/2$ as many observations for the same leading variance.
:::

## Assumptions and limits — Weak limits do not control rare large errors
A centred asymptotic distribution alone does not ensure that finite-sample bias is smaller than $n^{-1/2}$ or that $n$ times mean squared error converges to its variance constant. Rare extreme values can be invisible to weak convergence but dominate moments. Moment comparisons need corresponding integrability conditions.{{cite:durrett2019}} (§3.4, p. 152)

For example, $R_n=n\mathbf1\{U\le1/n\}$ with $U$ uniform on $(0,1)$ converges to zero in probability, yet $ER_n=1$ and $ER_n^2=n$. Adding $R_n$ to an asymptotically normal estimator leaves its weak limit unchanged even after multiplication by $\sqrt n$, since $P(R_n\ne0)=1/n\to0$. Its finite-sample bias need not disappear. The deterministic addition $1/n$ has a vanishing effect after multiplication by $\sqrt n$, although it changes finite-sample bias.

## Check yourself

### Translate efficiency into observations {#self-check-ex-inf-are-median}

[Practice question](../questions/ex-inf-are-median.qmd)

How many normal-sample observations does the median need to match a mean based on sixty-four?

::: {.callout-tip collapse="true" title="Answer"}
The leading sample-size ratio is $\pi/2$. The calculation gives $100.530965$, rounded up to $101$.
:::

### A rare extreme observation {#self-check-ex-sp-spike}

[Practice question](../questions/ex-sp-spike.qmd)

Compute the first two moments and probability limit of $R_n=n\mathbf1\{U\le1/n\}$.

::: {.callout-tip collapse="true" title="Answer"}
$ER_n=1$ and $ER_n^2=n$. For each positive $\varepsilon$ and sufficiently large $n$, $P(R_n>\varepsilon)=1/n\to0$. It therefore converges in probability but not in $L^1$ or $L^2$. For every $U>0$, it is eventually zero, so it also converges almost surely.
:::
