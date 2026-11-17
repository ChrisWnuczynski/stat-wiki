## Motivating example
Forty successes in a hundred trials give $\widehat p=0.40$. The interval built from that proportion and a normal cutoff is a statement about the procedure, computed from this one sample.

## Intuition — A normal cutoff, with the standard error filled in
A large-sample interval for a proportion starts from a normal approximation to the count. For a fair coin the approximation is the De Moivre–Laplace theorem: the centred and scaled number of heads settles to a standard normal. The Wald interval keeps a normal cutoff and replaces the unknown standard error by the value computed from the observed proportion. The resulting endpoints are functions of the data alone. Their coverage is approximate, and it is a property of the procedure before the sample is drawn.{{cite:durrett2019}} (Thm. 3.1.3, p. 115){{cite:siegrist2022_normal_distribution}} (§5.6, standard normal density)

## Definition — Plug-in standard error
For $X\sim\operatorname{Bin}(n,p)$ and $\widehat p=X/n$, the Wald interval of nominal level $95\%$ is
$$
\widehat p\pm 1.96\sqrt{\frac{\widehat p(1-\widehat p)}{n}},
$$
where $1.96$ is the $0.975$ quantile of the standard normal density, to two decimal places. At $p=1/2$ the exact standard error is $1/(2\sqrt n)$, and $(\widehat p-1/2)$ divided by that standard error is the De Moivre–Laplace statistic. The Wald formula uses $\sqrt{\widehat p(1-\widehat p)/n}$ even when $p$ is not $1/2$. That substitution is the plug-in step. It is not part of the De Moivre–Laplace theorem.{{cite:durrett2019}} (Thm. 3.1.3, p. 115){{cite:siegrist2022_normal_distribution}} (§5.6, standard normal density)

If $\widehat p=0$ or $\widehat p=1$, the plugged-in standard error is $0$, and the interval collapses to the single point $0$ or $1$. A sample of all failures then reports no width at all.

## Worked example — Forty successes in a hundred
Take $X=40$ and $n=100$, so $\widehat p=0.40$. The estimated variance is $0.40\times 0.60/100=0.0024$, and the standard error is $\sqrt{0.0024}=0.0490$ to four decimal places. The half-width is $1.96\times 0.0490$, which equals $0.096$ to three decimal places. The interval is $(0.304,\ 0.496)$.

For comparison, a fair coin with $n=100$ and $\widehat p=0.50$ has plugged-in standard error $0.05$ and half-width $1.96\times 0.05=0.098$, so the interval is $(0.402,\ 0.598)$. Here the plug-in standard error equals the true standard error at $p=1/2$.{{cite:durrett2019}} (Thm. 3.1.3, p. 115)

**Your turn.** With $n=100$ and $X=0$, compute the Wald interval. Then compute it for $X=10$.

::: {.callout-tip collapse="true" title="Answer"}
At $X=0$, $\widehat p=0$ and the standard error is $0$, so the interval is the point $0$. At $X=10$, $\widehat p=0.10$ and the variance estimate is $0.10\times 0.90/100=0.0009$, so the standard error is $0.03$. The half-width is $1.96\times 0.03=0.0588$, and the interval is $(0.0412,\ 0.1588)$.
:::

## Check yourself
### Where the normal limit applies directly
For a fair coin, the Wald standard error at the true $p=1/2$ equals $1/(2\sqrt n)$. For $n=100$, what is that number, and which theorem supplies the normal shape?

::: {.callout-tip collapse="true" title="Answer"}
$1/(2\sqrt{100})=0.05$. The normal shape is the De Moivre–Laplace theorem for the symmetric random walk, which is this statistic. The plug-in step is idle here only because $\widehat p$ happened to equal $1/2$.
:::

### A wider plug-in
Among proportions in $(0,1)$, where is $\widehat p(1-\widehat p)$ largest? What does that say about the Wald half-width for fixed $n$?

::: {.callout-tip collapse="true" title="Answer"}
The product $p(1-p)$ has derivative $1-2p$ and is largest at $p=1/2$, where it equals $1/4$. For a fixed sample size the plugged-in Wald interval is widest when $\widehat p$ is nearest one half, and it shrinks to a point as $\widehat p$ approaches $0$ or $1$.
:::

## Connections — Approximate intervals and their neighbours
The construction is one [confidence interval](confidence-interval.qmd): a normal cutoff applied to an estimated standard error. The [central limit theorem](central-limit-theorem.qmd) is the general reason a centred sample mean, scaled by its true standard deviation, looks normal; De Moivre–Laplace is the fair-coin case used above. The [normal distribution](normal-distribution.qmd) supplies the cutoff. A binomial count near $0$ or $1$, or a small $n$, is where the plug-in width is a poor stand-in for the true sampling variability.{{cite:durrett2019}} (Thm. 3.1.3, p. 115){{cite:siegrist2022_normal_distribution}} (§5.6, standard normal density)
