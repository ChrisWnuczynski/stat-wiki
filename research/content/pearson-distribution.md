## Lead context
A Pearson distribution is a frequency curve whose slope, on the logarithmic scale and with the origin at the mode, is a rational function: the numerator is linear in the abscissa and the denominator is a quadratic. Karl Pearson introduced the family in 1895 as a replacement for the normal curve when a homogeneous batch is skewed or has a limited range. The normal curve sits inside the family as a limit. The other types are the curves that the same slope equation produces when the quadratic takes a different shape.{{cite:pearson1895}} (pp. 360, 367){{cite:dodge2008}} (p. 344)

## Motivating example
A batch of measurements can be bounded on one side, as a waiting time is bounded at zero, and still pile up away from that bound. The normal curve is symmetric and unbounded, so it cannot be the frequency curve of that batch. Pearson's question was which single curve, fitted from the moments, would carry the skewness and the bound together. For material he treated as homogeneous, the answer is one curve from the system, not a mixture of two normal curves.{{cite:pearson1895}} (p. 367){{cite:dodge2008}} (p. 344)

## Intuition
Start from a histogram and ask how the height changes as the abscissa moves. At the mode the height is stationary, so the slope is zero there. Away from the mode the slope is pulled back toward the mode, and the strength of that pull can depend on where one stands. Writing the logarithmic slope as

$$
\frac{1}{y}\frac{dy}{dx}=\frac{x}{c_0+c_1 x+c_2 x^2},
$$


with the origin at the mode, puts that pull into one formula. The sign of the discriminant of the quadratic, and whether a root falls inside the range of the data, decides which named type comes out. A constant denominator gives the normal curve. A linear denominator that hits zero on one side gives a one-sided curve. A quadratic with two real roots can stop the curve at both ends.{{cite:pearson1895}} (pp. 360, 362)

## Definition
The system is the set of positive solutions of that slope equation, normalised so that the area equals the total frequency. Pearson classified the solutions by the range they occupy.

Type I is limited in both directions and skew. Type II is the symmetric curve of limited range. Type III is limited in one direction only, with equation, in the memoir's notation,

$$
y=y_0\Bigl(1+\frac{x}{a}\Bigr)^{p}e^{-\gamma x},
$$


and with moments, after the origin is moved to the mean,

$$
\mu_2=\frac{p+1}{\gamma^2},\qquad
\mu_3=\frac{2(p+1)}{\gamma^3},\qquad
\mu_4=\frac{3(p+1)(p+3)}{\gamma^4}.
$$


Type IV is unlimited in both directions and skew. Type V in the memoir is the normal curve, recovered as the skewness tends to zero. The labels (i) through (vii) on the real-root solutions are subtypes and limits of these, not a second list of families: (iv) is the one-sided Type III, (v) is the symmetric Type II, and (vii) is again $y=y_0 e^{-px^2}$.{{cite:pearson1895}} (pp. 362, 373)

The hypergeometric series is the discrete parent. The curves stand to that series as the normal curve stands to the symmetric binomial. When the ratio of the draw size to the bag size falls between two bounds, the integral that matches the series is trigonometric; outside those bounds it is logarithmic.{{cite:pearson1895}} (p. 362)

## Properties
The third and fourth moments are the quantities that carry a departure from the normal curve. For Type III the two lower moments determine the parameters,

$$
\gamma=\frac{2\mu_2}{\mu_3},\qquad p=\frac{4\mu_2^3}{\mu_3^2}-1,
$$


so a one-sided fit does not need a separate estimate of the fourth moment. The memoir's skewness is the gap from the mode to the mean, in units of $\sqrt{\mu_2}$. That gap equals half the third-moment ratio:

$$
\frac{\mu_3}{\mu_2^{3/2}}=\frac{2}{\sqrt{p+1}},\qquad
\text{skewness}=\frac{1}{\sqrt{p+1}}.
$$


The fourth-moment ratio collapses to

$$
\frac{\mu_4}{\mu_2^2}=\frac{3(p+3)}{p+1}.
$$


At the normal limit this ratio is 3. A larger value is the Type III curve's excess of fourth moment. The normalising constant of Type III is written with $\Gamma(p+1)$, the integral of $z^p e^{-z}$.{{cite:pearson1895}} (p. 373)

The trigonometric window has a numerical edge. For a bag of $n=100$, the product that sets the bounds is

$$
\frac{1}{n}\Bigl(1+\frac{1}{n}\Bigr)=\frac{101}{10000}=0.0101,
$$


and $\sqrt{0.0101}\approx 0.1004988$. The critical values of the proportion $p$ are $0.5\pm 0.1004988$, which round to $0.3995$ and $0.6005$. If the proportion drawn lies between those two printed limits, every draw size gives the trigonometric integral.{{cite:pearson1895}} (p. 362)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
From $\mu_2=(p+1)/\gamma^2$ and $\mu_3=2(p+1)/\gamma^3$,

$$
\frac{\mu_3}{\mu_2}=\frac{2}{\gamma},\qquad
\frac{\mu_3}{\mu_2^{3/2}}=\frac{2}{\sqrt{p+1}}.
$$


Half of that ratio is $1/\sqrt{p+1}$. The same quantity is the gap $d=1/\gamma$ between mode and mean, divided by $\sqrt{\mu_2}=\sqrt{p+1}/\gamma$. For the fourth moment,

$$
\frac{\mu_4}{\mu_2^2}=\frac{3(p+1)(p+3)/\gamma^4}{(p+1)^2/\gamma^4}=\frac{3(p+3)}{p+1}.
$$


At $p=3$ and $\gamma=2$ this is $3\cdot 6/4=9/2$.{{cite:pearson1895}} (p. 373)
:::
:::

## Worked example
For a Type III curve with $p=3$ and $\gamma=2$,

$$
\mu_2=\frac{4}{4}=1,\qquad
\mu_3=\frac{2\cdot 4}{8}=1,\qquad
\mu_4=\frac{3\cdot 4\cdot 6}{16}=\frac{9}{2}.
$$


The third-moment ratio $\mu_3/\mu_2^{3/2}$ equals 1. The memoir's skewness is half of that, $1/2$, and $\mu_4/\mu_2^2=9/2$, above the normal value 3. The same $n=100$ window used above places every trigonometric integral between the proportions $0.3995$ and $0.6005$.{{cite:pearson1895}} (pp. 362, 373)

**Your turn.** For a Type III curve with $p=8$ and $\gamma=1$, compute $\mu_2$, the memoir's skewness $1/\sqrt{p+1}$, and the ratio $\mu_4/\mu_2^2$.

::: {.callout-tip collapse="true" title="Answer"}
The second moment is $\mu_2=9$. The memoir's skewness is $1/\sqrt{9}=1/3$. The fourth-moment ratio is $3(8+3)/(8+1)=11/3$.
:::

## Assumptions and limits
The slope equation is written with the origin at the mode, so a zero of the numerator sits at $x=0$. A curve fitted on a different origin needs the linear shift put back into the numerator. The constants have to give a non-negative ordinate on the interval where the expression is real, and $y_0$ is chosen so that the area equals the total frequency. The quadratic slope is offered for homogeneous material, the case in which one curve, rather than a mixture, is the description. A batch that is a blend of two populations can look skew for a reason the single curve does not name.{{cite:pearson1895}} (pp. 367, 373)

The memoir's Type V is the normal curve. It is not a separate skew type. The printed skewness $(1/2)\mu_3/\mu_2^{3/2}$ is the gap from mode to mean in standard units. The full third-moment ratio is twice that number. Quoting one of them as if it were the other doubles or halves the asymmetry.{{cite:pearson1895}} (pp. 360, 373)

## Connections
[Kurtosis](kurtosis.qmd) is the fourth-moment comparison with the normal value 3, which is the comparison that separates a limited symmetric type from the normal curve. [Skewness](skewness.qmd) is the third-moment companion. The [gamma distribution](gamma-distribution.qmd) is the one-sided Type III curve written with a gamma function. A [histogram](histogram.qmd) is the picture to which one of these curves is fitted. Pearson's 1895 memoir is the source of the slope equation and of the moment formulae used above. The third and fourth moments remained, after that memoir, the standard numerical summary of a departure from the normal curve.{{cite:dodge2008}} (p. 344){{cite:pearson1895}} (pp. 367, 373)
