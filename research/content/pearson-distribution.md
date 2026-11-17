## Lead context
A normal curve is fixed once its mean and its standard deviation are fixed. Many measured batches are skew, or they stop at a hard boundary, and a single extra shape is not enough for them. The Pearson distributions are the frequency curves obtained by letting the slope of the normal curve acquire a linear and then a quadratic term in the denominator.{{cite:pearson1895}} (p. 381)

## Motivating example
Draw \(r\) balls from a bag that holds \(pn\) black balls and \(qn\) white balls, and record how many black balls appear. If \(r>pn\), that count cannot exceed \(pn\), so the frequency polygon is skew and stops at both ends. The same counting series is a hypergeometric series. Passing to a continuous curve with the same slope relation produces a family that contains the normal curve, the skew binomial limit, and the two-sided limited curves as cases of one formula.{{cite:pearson1895}} (p. 360)

## Intuition
At the mode the curve is flat, so the origin can be put there and the slope can be written as a multiple of the abscissa. For the normal curve the multiple is constant. A skew binomial makes the multiple depend on a linear function of the abscissa, which lets the curve stop on one side and run out on the other. Dependence among the draws, as in sampling without replacement, puts a quadratic in the denominator. The roots of that quadratic decide whether the curve stops, or runs to infinity, on each side.{{cite:pearson1895}} (pp. 356–357, 381)

## Definition
With the origin at the mode, the logarithmic slope of a Pearson curve is
\[
\frac{1}{y}\frac{dy}{dx}=-\frac{x}{c_1+c_2x+c_3x^2}.
\]
The normal curve is the special case \(c_2=c_3=0\),
\[
\frac{1}{y}\frac{dy}{dx}=-\frac{x}{c_1},
\]
and the curve tied to the skew binomial is the case \(c_3=0\),
\[
\frac{1}{y}\frac{dy}{dx}=-\frac{x}{c_1+c_2x}.
\]
The quadratic denominator contains both of those as special cases.{{cite:pearson1895}} (p. 381)

In this memoir the solutions are sorted by range and symmetry:

- Type I is skew, with the range limited in both directions.
- Type II is symmetric, with the range limited in both directions.
- Type III is skew, with the range limited in one direction only.
- Type IV is skew, with the range unlimited in both directions.
- Type V is symmetric, with the range unlimited in both directions, and it is the normal curve.{{cite:pearson1895}} (p. 360)

## Properties
The sign of \(\beta_2^2-4\beta_1\beta_3\) in the hypergeometric slope splits the integral into a trigonometric case and a logarithmic case. For a draw of \(r\) items from \(n\), the integral is trigonometric when \(r/n\) lies between
\[
\frac12\pm\sqrt{\Bigl(p+\frac1n\Bigr)\Bigl(q+\frac1n\Bigr)},
\]
and logarithmic when \(r/n\) lies outside that interval. If those limits fall outside \([0,1]\), every admissible \(r\) gives the trigonometric integral. For \(n=100\) that happens when \(p\) lies between \(0.3995\) and \(0.6005\).{{cite:pearson1895}} (p. 362)

The trigonometric case is Type IV,
\[
y=\frac{y_0}{(1+x^2/a^2)^m}\exp\bigl(-\nu\tan^{-1}(x/a)\bigr),
\]
unlimited on both sides and asymmetric unless \(\nu=0\).{{cite:pearson1895}} (p. 362) The logarithmic case has real roots \(a_1,a_2\) and the form
\[
y=y_0\Bigl(1+\frac{x}{a_1}\Bigr)^{\nu a_1}\Bigl(1-\frac{x}{a_2}\Bigr)^{\nu a_2},
\]
which stops at \(x=-a_1\) and at \(x=a_2\).{{cite:pearson1895}} (p. 364) Sending one end to infinity produces Type III,
\[
y=y_0\Bigl(1+\frac{x}{a}\Bigr)^{\gamma a}e^{-\gamma x},
\]
limited on one side. Setting the two ends equal produces Type II,
\[
y=y_0\Bigl(1-\frac{x^2}{a^2}\Bigr)^m.
\]
A further limit of that symmetric curve is \(y=y_0e^{-px^2}\), the normal curve.{{cite:pearson1895}} (pp. 365, 372–373)

For Type III, measured from the start of the range, the central moments about the mean are
\[
\mu_2=\frac{p+1}{\gamma^2},\qquad
\mu_3=\frac{2(p+1)}{\gamma^3},\qquad
\mu_4=\frac{3(p+1)(p+3)}{\gamma^4},
\]
where \(p=\gamma a\). The memoir’s skewness is the distance from the mode to the mean, in units of the standard deviation,
\[
\frac{d}{\sqrt{\mu_2}}=\frac12\frac{\mu_3}{\mu_2^{3/2}}=\frac{1}{\sqrt{p+1}}.
\]
The fourth-moment ratio is \(\mu_4/\mu_2^2=3(p+3)/(p+1)\). For a normal curve that ratio equals 3, and for a symmetrical point-binomial it is smaller than 3.{{cite:pearson1895}} (pp. 372–373)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
From \(\mu_2=(p+1)/\gamma^2\) and \(\mu_3=2(p+1)/\gamma^3\),
\[
\frac{\mu_3}{\mu_2}=\frac{2}{\gamma},\qquad
\frac{\mu_3}{\mu_2^{3/2}}=\frac{2}{\sqrt{p+1}}.
\]
Half of that ratio is \(1/\sqrt{p+1}\). The same quantity is the gap \(d=1/\gamma\) between mode and mean, divided by \(\sqrt{\mu_2}=\sqrt{p+1}/\gamma\). For the fourth moment,
\[
\frac{\mu_4}{\mu_2^2}=\frac{3(p+1)(p+3)/\gamma^4}{(p+1)^2/\gamma^4}=\frac{3(p+3)}{p+1}.
\]
At \(p=3\) and \(\gamma=2\) this is \(3\cdot6/4=9/2\).{{cite:pearson1895}} (p. 373)
:::
:::

## Statistical use
Fit a type by the range the measurements can actually occupy and by the third and fourth moments. A batch that cannot pass a lower and an upper bound, and that is not symmetric, is a candidate for Type I. A symmetric batch that is flatter than the normal curve, in the sense \(\mu_4<3\mu_2^2\), is a candidate for the limited Type II rather than for the normal curve. A batch with one hard boundary, such as a mortality counted from birth, is a candidate for Type III, and the two moments \(\mu_2\) and \(\mu_3\) determine \(\gamma=2\mu_2/\mu_3\) and \(p=4\mu_2^3/\mu_3^2-1\).{{cite:pearson1895}} (pp. 360, 372–373) The third and fourth moments are the quantities that carry a departure from the normal curve.{{cite:dodge2008}} (p. 344)

## Worked example
For \(n=100\),
\[
\frac1n\Bigl(1+\frac1n\Bigr)=\frac{101}{10000}=0.0101,\qquad
\sqrt{0.0101}=\frac{\sqrt{101}}{100}\approx 0.1004988.
\]
The critical values of \(p\) are \(0.5\pm 0.1004988\), that is \(0.3995012\) and \(0.6004988\), which round to the printed limits \(0.3995\) and \(0.6005\). Inside that interval every draw size gives the trigonometric integral.{{cite:pearson1895}} (p. 362)

For a Type III curve with \(p=3\) and \(\gamma=2\),
\[
\mu_2=\frac{4}{4}=1,\qquad
\mu_3=\frac{2\cdot 4}{8}=1,\qquad
\mu_4=\frac{3\cdot 4\cdot 6}{16}=\frac{9}{2}.
\]
The third-moment ratio \(\mu_3/\mu_2^{3/2}\) equals 1. The memoir’s skewness is half of that, \(1/2\), and \(\mu_4/\mu_2^2=9/2\), above the normal value 3.{{cite:pearson1895}} (p. 373)

**Your turn.** For a Type III curve with \(p=8\) and \(\gamma=1\), compute \(\mu_2\), the memoir’s skewness \(1/\sqrt{p+1}\), and the ratio \(\mu_4/\mu_2^2\).

::: {.callout-tip collapse="true" title="Answer"}
The second moment is \(\mu_2=9\). The memoir’s skewness is \(1/\sqrt{9}=1/3\). The fourth-moment ratio is \(3(8+3)/(8+1)=11/3\).
:::

## Common misconceptions
The memoir’s Type V is the normal curve. It is not a separate skew type. The labels (i) through (vii) on the real-root solutions are subtypes and limits: (iv) is the one-sided Type III, (v) is the symmetric Type II, and (vii) is again the normal curve \(y=y_0e^{-px^2}\).{{cite:pearson1895}} (pp. 360, 365) The skewness printed in the Type III section is \((1/2)\mu_3/\mu_2^{3/2}\), the gap from mode to mean in standard units. The full third-moment ratio \(\mu_3/\mu_2^{3/2}\) is twice that number.{{cite:pearson1895}} (p. 373)

## Assumptions and limits
The slope equation is written with the origin at the mode, so a zero of the numerator sits at \(x=0\). A curve fitted on a different origin needs the linear shift put back into the numerator. The constants \(c_1,c_2,c_3\) have to give a non-negative ordinate on the interval where the expression is real, and \(y_0\) is chosen so that the area equals the total frequency. The Type III normalising constant is written with \(\Gamma(p+1)\), the integral of \(z^p e^{-z}\). The quadratic slope is offered for homogeneous material, the case in which one curve, rather than a mixture, is the description.{{cite:pearson1895}} (pp. 373, 381)

## Connections
[Kurtosis](kurtosis.qmd) is the fourth-moment comparison with the normal value 3, which is the comparison that separates Type II from the normal curve. [Skewness](skewness.qmd) is the third-moment companion. The [gamma distribution](gamma-distribution.qmd) is the one-sided Type III curve written with a gamma function. The exponential law, the Type III case with the mode on the boundary, is the tail used for [fat tails](fat-tails.qmd). A [histogram](histogram.qmd) is the picture to which one of these curves is fitted.

## History
The normal curve was already in use as the limit of a symmetric binomial. The 1895 memoir keeps a finite number of contributory causes, allows them to be unequal, and replaces the binomial and the hypergeometric polygon by the curves with the same slope. Type III had already been written down, without discussion, in the Proceedings of the Royal Society, volume 54, page 331. The five types, and the slope with a quadratic denominator, are set out in this memoir. The third and fourth moments are what mark a fitted curve off from the normal curve, which is the role recorded for the system published in 1894 and 1895.{{cite:pearson1895}} (pp. 357, 360, 381){{cite:dodge2008}} (p. 344)
