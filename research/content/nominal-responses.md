## Lead context
Nominal responses are labels with no order, so the model compares each label with a baseline instead of cutting a scale into tails.

## Intuition — Only \(K-1\) comparisons are free
With labels rugby, cricket and netball, saying that cricket is twice as likely as rugby and netball is three times as likely as rugby already fixes netball relative to cricket. The third log-odds is the difference of the first two. A model that wrote a separate linear predictor for every pair would over-count. Choosing one baseline and fitting the other labels against it uses each free comparison once.

## Definition — Baseline-category logits
For categories \(0,1,\ldots,K-1\) and covariate row \(x\),
\[
\log\frac{p_k}{p_0}=\beta_{0k}+x^\top\beta_k,
\qquad k=1,\ldots,K-1.
\]
The probabilities are recovered by setting the baseline linear predictor to \(0\) and normalising the exponentials. There is no requirement that the slopes \(\beta_k\) be equal, because the labels are not ordered.

## Properties — The omitted comparison is a difference
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
\[
\log\frac{p_k}{p_j}=\log\frac{p_k}{p_0}-\log\frac{p_j}{p_0}
=(\beta_{0k}-\beta_{0j})+x^\top(\beta_k-\beta_j).
\]
The right-hand side is linear in \(x\), with slope equal to the difference of the two baseline slopes.
:::
:::

## Worked example — Three probabilities, and one covariate value
Take \(p_0=1/2\), \(p_1=3/10\) and \(p_2=1/5\). These sum to \(1\). The baseline log-odds are
\[
\log\frac{p_1}{p_0}=\log\frac{3}{5}\approx -0.5108,
\qquad
\log\frac{p_2}{p_0}=\log\frac{2}{5}\approx -0.9163.
\]
Their difference is \(\log(2/3)\approx -0.4055\), which equals \(\log(p_2/p_1)\) because \((1/5)/(3/10)=2/3\).

At a single covariate value \(x=1\), the same numbers are the linear predictors \(\eta_1=-0.5108\) and \(\eta_2=-0.9163\), with \(\eta_0=0\). The normalised probabilities are proportional to \(1\), \(e^{\eta_1}=3/5\) and \(e^{\eta_2}=2/5\), and
\[
\frac{1}{1+3/5+2/5}=\frac12,
\qquad
\frac{3/5}{1+3/5+2/5}=\frac{3}{10},
\qquad
\frac{2/5}{2}=\frac15.
\]

**Your turn.** Replace \(p_2\) by \(1/10\) and \(p_0\) by \(3/5\), keeping \(p_1=3/10\). Find \(\log(p_2/p_1)\) from the two baseline log-odds, and check that the three probabilities still sum to \(1\).

::: {.callout-tip collapse="true" title="Answer"}
\(3/5+3/10+1/10=1\). Then \(\log(p_2/p_0)-\log(p_1/p_0)=\log((1/10)/(3/5))-\log((3/10)/(3/5))=\log(1/6)-\log(1/2)=\log(1/3)\), and \((1/10)/(3/10)=1/3\).
:::

## Connections — Ordered labels use a different comparison
[Ordinal responses](ordinal-responses.qmd) keep the order and model cumulative tails with a shared slope. Nominal labels have no such tail. The [logit link](logit-link.qmd) is the two-category case of the baseline formula, with a single log-odds. Changing which label is called \(0\) rewrites the coefficients and does not change the fitted probabilities.

## Check yourself — Two baseline calculations
If \(p_1/p_0=2\) and \(p_2/p_0=6\), what is \(p_2/p_1\), and what is \(\log(p_2/p_1)\)?

::: {.callout-tip collapse="true" title="Answer"}
\(p_2/p_1=6/2=3\), so the log-odds equal \(\log 3\). The same number is \(\log 6-\log 2\).
:::

The linear predictors at \(x=0\) are \(\eta_1=\log 2\) and \(\eta_2=\log 6\), with \(\eta_0=0\). What is \(p_0\)?

::: {.callout-tip collapse="true" title="Answer"}
The weights are \(1\), \(2\) and \(6\), summing to \(9\), so \(p_0=1/9\).
:::
