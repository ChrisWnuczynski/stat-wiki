## Motivating example

A scientist plots a kernel density estimate of three measured values to see whether the distribution has one peak or several. With a tiny bandwidth each observation can make its own sharp bump; with a very wide one, distinct features can blur together. Choosing the bandwidth decides which scales of variation the display and estimate will retain, so the choice must answer a statistical purpose rather than simply make a pleasing curve.{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.1–2.2, effect of bandwidth)

## Intuition

Kernel density estimation puts a small smooth density around every observation and averages the contributions. The bandwidth is the width of those contributions. Narrow kernels follow individual data points and fluctuate more across samples; broad kernels average over more observations and can miss bends or modes of the underlying density. A choice that performs well at one sample size or for one target need not work for another. The goal is to balance smoothing bias against sampling variation, then check the resulting estimate in the scientific context.{{cite:hansen_larsson2026_density}} (Ch. 2 §2.1, qualitative bandwidth effect)

## Definition

For observations $X_1,\ldots,X_n$ on the real line and a normalized kernel $K$, the density estimate at bandwidth $h>0$ is $\widehat f_h(x)=(nh)^{-1}\sum_{i=1}^n K((x-X_i)/h)$. The bandwidth is in the units of $X$; changing units requires rescaling $h$ too. A multivariate estimate can replace $h^2$ by a symmetric positive-definite bandwidth matrix $H$ and write $|H|^{-1/2}K\{H^{-1/2}(\mathbf x-\mathbf X_i)\}$ for each observation. A diagonal $H$ smooths separately along the chosen axes; a full $H$ can orient smoothing to correlated directions. The target remains the density of the variables actually retained.{{cite:hansen_larsson2026_density}} (Ch. 2 §2.1, univariate estimator)

One target is mean integrated squared error, $\mathrm{MISE}(H)=\E\int\{\widehat f(\mathbf x;H)-f(\mathbf x)\}^2d\mathbf x$, where expectation runs over fresh samples from the unknown density $f$. The ideal bandwidth minimizes this risk, but $f$ is unknown. In a univariate, twice-smooth setting, an asymptotic approximation takes the form $Ah^4+B/(nh)$ for positive constants $A$ and $B$: squared bias grows with $h$, while variance shrinks as $nh$ grows. The approximate optimum is proportional to $n^{-1/5}$, a guide rather than an exact finite-sample answer{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.1–2.2, effect of bandwidth).

## Interpretation — Match the loss to the purpose

Different selection rules optimize different goals. A normal-reference rule plugs a scale estimate into a formula derived for a normal-shaped target; it is fast but can blur a skewed or multimodal density. A plug-in method estimates unknown curvature quantities that appear in the asymptotic risk formula. Least-squares cross-validation estimates integrated squared-error risk; likelihood cross-validation asks whether a density fitted without each held-out observation assigns that observation high density. These objectives can rank bandwidths differently, especially in small samples or tails.{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.2.2, 2.4, plug-in and CV)

The matrix choice in several dimensions is more than choosing a scalar on each coordinate. A full symmetric $p\times p$ matrix has $p(p+1)/2$ free entries, and its orientation can matter when data are correlated. Optimizing many entries from limited data is unstable; dimensionality also slows the convergence of nonparametric density estimates. Projecting to fewer coordinates may help estimation, but the resulting density is for the projection and cannot recover variation in discarded directions{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.1–2.2, effect of bandwidth).

## Properties — Why validation leaves observations out

If the value $X_i$ helps build the estimate used to score itself, a Gaussian kernel contributes $K(0)/(nh)$ to $\widehat f_h(X_i)$. This term grows as $h$ approaches zero, tempting an in-sample likelihood toward spikes at every observation. Leave-one-out likelihood avoids that self-contribution: use $\widehat f_{h,-i}(X_i)=\{(n-1)h\}^{-1}\sum_{j\ne i}K((X_i-X_j)/h)$, then maximize $\sum_i\log\widehat f_{h,-i}(X_i)$ over candidate bandwidths. The selected value is used to fit the final estimate on all observations. If a compact-support kernel gives zero left-out density, the log score is undefined or $-\infty$; kernel and score choice matter.{{cite:hansen_larsson2026_density}} (Ch. 2 §2.4, leave-one-out CV and log score)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For a symmetric unit-integral kernel and a sufficiently smooth density, Taylor expansion of $f(x+hu)$ inside $\E\widehat f_h(x)$ removes the first-order term because $\int uK(u)du=0$. The leading pointwise bias is proportional to $h^2f''(x)$. Independence of the observations makes the leading pointwise variance proportional to $1/(nh)$. Squaring the bias and integrating gives approximate MISE $Ah^4+B/(nh)$ with $A,B>0$. Differentiating yields $4Ah^3-B/(nh^2)=0$, hence $h_*^5=B/(4An)$ and $h_*\propto n^{-1/5}$. Substitution gives risk of order $n^{-4/5}$. The argument assumes the smoothness and integrability needed for the expansion{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.1–2.2, effect of bandwidth).

For a Gaussian kernel $K(0)>0$, the full-sample estimate at each observed $X_i$ includes $K(0)/(nh)$, which diverges as $h\downarrow0$. Removing observation $i$ removes this automatic contribution. This explains the leave-one-out construction; it does not prove that the resulting empirical choice is always optimal. {{cite:hansen_larsson2026_density}} (Ch. 2 §2.4, validation construction)
:::
:::

## Statistical use — Choose, compare, and report

First specify whether the density is for display, estimation of a whole distribution, or tail probabilities. Inspect the measurements and their units, fit a reasonable initial bandwidth, and examine nearby values for features that appear or disappear. If using cross-validation, keep the held-out observations out of each fit and report the candidate range and scoring rule. A normal-reference or plug-in bandwidth can be a useful starting point; R's `bw.nrd0`, `bw.ucv` and `bw.SJ` implement distinct rules rather than interchangeable labels. Boundaries, outliers and repeated values deserve attention because they can change what a smoothed curve means.{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.2, 2.4)

In high dimension, estimating a full $H$ demands far more information than estimating one $h$. Coordinate scaling should be considered before comparing diagonal widths, and a dimension-reduction step should be stated as a change of target. A default software limit is not a mathematical dimension at which density estimation suddenly becomes impossible. The difficulty depends on sample size, smoothness and effective dimension{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.1–2.2, effect of bandwidth).

For a density supported only on nonnegative values, ordinary symmetric kernels can put positive estimated mass below zero near the boundary; changing $h$ alone does not repair that boundary bias. A dataset with one extreme value can inflate a standard-deviation-based reference bandwidth and flatten the main group. In a tiny sample, leave-one-out scores can be sensitive to a single isolated observation, and a compact-support kernel may assign it zero density for narrow widths. Examine the support, robust scale and plausible candidate range before trusting a selected number.{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.2, 2.4, scale and validation)
## Worked example

Take the three observed values $x=(0,1,2)$ and a Gaussian kernel $K(u)=e^{-u^2/2}/\sqrt{2\pi}$. Compare $h=0.5$, $1$ and $2$ by leave-one-out mean log density. At $h=1$, the left-out estimate for the middle observation is $\{K(1)+K(-1)\}/2=0.241971$; for either endpoint it is $\{K(1)+K(2)\}/2=0.147981$. The mean of their three logarithms is about $-1.746761$. At $h=0.5$ the corresponding endpoint and center densities are about $0.054125$ and $0.107982$, giving mean log score $-2.686239$; at $h=2$ they are $0.148509$ and $0.176033$, giving $-1.850435$. Among these candidates, $h=1$ scores highest. This is a comparison under one stated criterion, not proof that the population-optimal bandwidth is exactly one.{{cite:hansen_larsson2026_density}} (Ch. 2 §2.4, leave-one-out log-likelihood)

**Your turn.** Double every observation to $(0,2,4)$ and compare candidate widths $h=1$ and $h=2$ using the same criterion. Without recomputing every Gaussian value, which width wins and why?

::: {.callout-tip collapse="true" title="Answer"}
Doubling the data and bandwidth preserves all standardized distances $(x_i-x_j)/h$. Each left-out density is halved because of the $1/h$ factor, so every mean log score falls by $\log2$. Thus $h=1$ on the doubled data corresponds to $h=0.5$ above and scores about $-2.686239-\log2\approx-3.379386$; $h=2$ corresponds to the earlier $h=1$ and scores about $-1.746761-\log2\approx-2.439908$. The latter is higher, so choose $h=2$ from the two candidates.
:::

## Common misconceptions

A smoother curve is not necessarily a better density estimate: oversmoothing can erase real structure. More peaks do not automatically mean more generating populations: undersmoothing can turn sample noise into bumps. The bandwidth is not dimensionless; changing measurement units changes its numerical value. Cross-validation also does not reveal the true density or eliminate all modeling choices; it selects among candidates for the chosen score. These are distinct issues of bias, mixture interpretation, scaling and empirical selection.{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.1–2.4)

## Connections

The [kernel density estimator](kernel-density-estimator.qmd) is the object whose smoothing is tuned. [Gaussian kernel](gaussian-kernel.qmd) and [Epanechnikov kernel](epanechnikov-kernel.qmd) describe possible shapes. [Cross-validation](cross-validation.qmd) supplies out-of-sample scoring, while [Kullback–Leibler divergence](kullback-leibler-divergence.qmd) and integrated squared error express different notions of closeness to a target density. In [kernel density discriminant analysis](kernel-density-discriminant-analysis.qmd), bandwidth choices also affect a classification boundary.{{cite:hansen_larsson2026_density}} (Ch. 2 §§2.1–2.4)

## History

Silverman's historical survey identifies Rosenblatt's 1956 work as an early published treatment of kernel density estimation; Parzen's 1962 work helped establish the form now commonly used. As density estimation became practical, bandwidth choice became a central problem rather than a cosmetic plotting adjustment. Current statistical software exposes normal-reference, cross-validation and plug-in selectors, reflecting different ways to estimate the unknown risk.{{cite:silverman1986}} (§2.11, Discussion and bibliography){{cite:hansen_larsson2026_density}} (Ch. 2 §2.1, historical introduction)
