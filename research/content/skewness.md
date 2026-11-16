## Lead context
It helps distinguish a long tail on one side from roughly balanced spread, and it can guide a choice of display or model scale.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness” and “Dealing with Skewness and Kurtosis”)

## Motivating example
The serum-creatinine measurements in the heart-failure data have a dense cluster of small values and a few much larger ones. Their median is $1.1$ and their maximum is $9.4$. The mean, about $1.394$, lies above the median because the high observations pull it upward. A histogram makes the long right tail visible; skewness puts a signed number on that asymmetry. On the original scale its sample moment skewness is about $4.4$. A log display compresses the right tail, and the same calculation on the logged values is about $1.6$. These numbers describe different scales of the same 299 observations.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness” and “Dealing with Skewness and Kurtosis”)

## Intuition
Skewness compares deviations from the mean after cubing them. A large positive deviation contributes a large positive cube; a large negative deviation contributes a large negative cube. Dividing by the standard deviation cubed makes the result unitless, so centimetres and metres give the same answer. Positive moment skewness suggests a heavier or longer right tail, and negative skewness a left tail. The number is sensitive to extreme observations, so it should be interpreted alongside a histogram or boxplot rather than as a complete picture of shape.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”, “Examples”)

## Definition
For a random variable $X$ with mean $\mu=\mathbb EX$, positive standard deviation $\sigma$, and finite absolute third moment, its moment skewness is $\gamma_1=\mathbb E[(X-\mu)^3]/\sigma^3$. This is the standardized third central moment. For observations $x_1,\ldots,x_n$, define $m_k=n^{-1}\sum_i(x_i-\bar x)^k$. The descriptive sample coefficient is $g_1=m_3/m_2^{3/2}$ when $m_2>0$. The denominator here uses $n$ inside $m_2$; inserting the usual variance with divisor $n-1$ without adjusting the formula gives a different coefficient.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”){{cite:nist_dataplot_skewness2023}} (“Description”)

Some software reports the adjusted Fisher–Pearson coefficient $G_1=\sqrt{n(n-1)}\,g_1/(n-2)$ for $n>2$. For $n=5$ the multiplier is about $1.49$, so two programs using these different definitions can disagree materially on a small sample. A report should name its coefficient before comparing values. Quantile-based alternatives such as Galton or Bowley skewness answer a related question using quartiles and react differently to an isolated extreme value.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”){{cite:nist_dataplot_skewness2023}} (“Description”)

## Interpretation
![Serum creatinine among 299 patients: a boxplot, a histogram with density estimate, and a histogram on the log scale. The log compresses the long right tail.](../figures/da-creatinine-shape.png){fig-alt="Three views of serum creatinine for 299 heart-failure patients: a boxplot with high outliers, a histogram with a long thin right tail, and a log-scale histogram with a compressed right tail."}

The three views of serum creatinine show why a number needs a picture. The raw histogram has a thin right tail and the boxplot marks high observations; the log view brings those values closer to the main cluster. The comparison of $4.4$ with $1.6$ reports the moment coefficient on each scale, and the reciprocal scale has a value near zero. None of these values says that the original measurements themselves were changed or that the transformed data follow a normal law.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples” and “Dealing with Skewness and Kurtosis”)

## Properties
If $X$ is symmetric about its mean and the third absolute moment exists, opposite deviations cancel and $\gamma_1=0$. The converse fails: zero third central moment does not guarantee symmetry. For a nonzero constant $a$, $\gamma_1(aX+b)=\operatorname{sign}(a)\gamma_1(X)$. Changing measurement units with $a>0$ therefore leaves skewness alone, while reversing an axis flips its sign. A nonlinear transformation such as a logarithm or reciprocal can change its magnitude and even its sign.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness” and “Dealing with Skewness and Kurtosis”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Under symmetry about $\mu$, the distribution of $X-\mu$ equals that of $-(X-\mu)$. If the third moment exists, its expectation must equal its own negative and is therefore zero. For $Y=aX+b$, its centred value is $Y-\mathbb EY=a(X-\mu)$ and its standard deviation is $|a|\sigma$. Thus $\gamma_1(Y)=a^3\mathbb E[(X-\mu)^3]/(|a|^3\sigma^3)=\operatorname{sign}(a)\gamma_1(X)$.{{cite:nist_skewness2002}} (§1.3.5.11, standardized third moment)

For a counterexample to the converse, put probabilities $1/20,1/2,1/4,1/5$ on $-3,-1,1,2$, respectively. They sum to one, and direct calculation gives mean $0$ and third moment $(-27/20)-(1/2)+(1/4)+(8/5)=0$. Its variance is positive, so its skewness is zero. Yet it is not symmetric: there is positive mass at $-3$ and none at $3$. Finally, for an even sample $\{1,4\}$, the conventional average-of-middle-values median is $2.5$; after reciprocation the median is $(1+1/4)/2=0.625$, whereas $1/2.5=0.4$. This proves why an unqualified median-transformation rule fails for that convention.{{cite:nist_dataplot_skewness2023}} (“Description”, moment convention)
:::
:::

## Statistical use
Use a histogram, boxplot or normal quantile plot to identify the tail and any unusual observations, then use a named skewness coefficient as a compact supplement. If positive measurements are strongly right-skewed, a log transform may make their shape easier to display or model. Recalculate summaries on that scale and explain the change in interpretation: equal log differences represent equal ratios on the original scale. A reciprocal transformation reverses order and can reverse the sign of skewness. Neither transformation repairs dependence, censoring or an unsuitable sampling model.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples” and “Dealing with Skewness and Kurtosis”)

## Worked example
For the five observations $1,2,2,3,7$, the mean is $3$ and the deviations are $-2,-1,-1,0,4$. The second central moment is $m_2=(4+1+1+0+16)/5=22/5=4.4$; the third is $m_3=(-8-1-1+0+64)/5=54/5=10.8$. Therefore $g_1=(54/5)/(22/5)^{3/2}\approx1.170$. The largest value makes a strong positive contribution to the cube. If a program reports the adjusted coefficient, the answer is $G_1=\sqrt{20}\,g_1/3\approx1.744$, a different convention for the same five observations. Neither number alone describes whether the sample has one mode or two.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”)

**Your turn.** For $1,1,2,4$, calculate $\bar x$, $m_2$, $m_3$ and the unadjusted moment skewness $g_1$. State which tail is longer by this coefficient.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”)

::: {.callout-tip collapse="true" title="Answer"}
The mean is $2$, giving deviations $-1,-1,0,2$. Thus $m_2=(1+1+0+4)/4=3/2$ and $m_3=(-1-1+0+8)/4=3/2$. The coefficient is $g_1=(3/2)/(3/2)^{3/2}=\sqrt{2/3}\approx0.8165$, so the positive tail dominates this moment calculation. For these four values, the adjusted coefficient would be $\sqrt{12}\,g_1/2=\sqrt2\approx1.4142$; it is not the requested unadjusted answer.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”)
:::

## Common misconceptions
Zero skewness is not proof of symmetry, as the four-point counterexample in the proof shows. Positive skewness does not mean most observations exceed the mean; a few large observations can give a positive third moment even when most values lie below it. The coefficient is not the same as the distance between mean and median, although those summaries often move in related directions. Finally, a lower skewness after a log transform does not by itself establish a normal distribution or justify a normal-theory interval.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”, “Examples”, “Dealing with Skewness and Kurtosis”)

## Assumptions and limits
Moment skewness is undefined for a constant variable because its standard deviation is zero. It is also undefined as a population moment when $\mathbb E|X|^3$ is infinite; a symmetric Cauchy law is a concrete example. A finite sample from that law still has a computable coefficient when its observed spread is nonzero, but NIST's Cauchy illustration shows how wildly it can be driven by extreme observations. With an even sample and the average-of-middle-values median convention, a nonlinear transform need not map the sample median to the new median, as the two-value reciprocal example proves. These limits matter when interpreting a seemingly precise shape summary.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples”){{cite:nist_dataplot_skewness2023}} (“Description”)

## Connections
The [histogram](histogram.qmd) reveals shape that a single coefficient cannot. The [median](median.qmd) and [interquartile range](interquartile-range.qmd) summarise centre and spread with less sensitivity to a long tail. A [normal quantile plot](normal-quantile-plot.qmd) helps assess whether a normal model matches the data, and [transformations of data](transformations-of-data.qmd) change the scale on which skewness is computed.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples” and “Dealing with Skewness and Kurtosis”)

## History
Karl Pearson's 1895 Royal Society paper was explicitly about “skew variation in homogeneous material,” showing that asymmetric frequency curves were already a named subject of mathematical statistics. NIST's current reference distinguishes the standardized third-moment Fisher–Pearson coefficient from later adjusted and quantile-based coefficients, so the historical name alone does not identify a unique calculation.{{cite:pearson1895}} (Description, title and DOI record, 1895){{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”)
