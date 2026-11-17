## Motivating example

Serum creatinine was measured for 299 patients after heart failure. Most values lie near 1 mg/dL, while a few stretch toward 9; a single mean cannot show that long right tail. The middle panel below groups the measurements into adjacent intervals. Its bars make the crowded low values and sparse high values visible, while the boxplot and logarithmic view provide different checks on the same sample. A histogram is useful precisely because it shows where observations concentrate before a distributional model is chosen.{{cite:chicco_jurman2020}} (§Methods, 299-patient data){{cite:nist_histogram}} (“Questions,” location, spread, skewness and outliers)

![Serum creatinine for 299 patients: boxplot, histogram with a density curve, and a view on the logarithmic scale. The central histogram shows the long right tail.](../figures/da-creatinine-shape.pdf){#fig-hist-creatinine fig-alt="Three panels for serum creatinine: a boxplot with high outliers, a histogram concentrated near one with a sparse right tail, and a log-scale distribution with a shorter visual tail."}

## Intuition — Why bin width changes the picture

A histogram replaces individual measurements by counts in intervals. It deliberately loses exact positions within each interval, gaining an overview of location, spread, skew, gaps and possible modes. A narrow bin width preserves more local detail but can leave many erratic or empty bars; a wide width gives a steadier outline but can merge distinct groups. The starting edge matters too: shifting an otherwise identical grid can move observations across boundaries. The bin choice is part of the display, so a feature worth interpreting should persist under several reasonable choices.{{cite:nist_histogram}} (“Definition” and “Questions”){{cite:scott1979_histograms}} (§§1–3, bin-width bias and variance)

## Definition

Choose ordered bin edges $b_0<\cdots<b_m$, and count $n_j$ observations in each interval $[b_j,b_{j+1})$, with a final closed right edge if needed to include the maximum. The bin width is $w_j=b_{j+1}-b_j$. A frequency histogram uses count height $n_j$ when widths are equal. A relative-frequency histogram uses $n_j/n$. A *density histogram* uses height $n_j/(nw_j)$, so the rectangle's **area**, rather than its height alone, is the fraction $n_j/n$ of observations in that interval. With unequal widths, density scaling is essential for comparing bars fairly.{{cite:nist_histogram}} (“Definition,” two normalisations){{cite:dodge2008}} (p. 243, “Histogram,” Mathematical Aspects)

## Properties

The areas of a density histogram sum to one when the bins cover all $n$ observations. This makes its vertical units “proportion per measurement unit” and permits a probability density curve to be drawn on the same scale. A bar can therefore have height greater than one if its width is narrow; the total *area* remains one. If all bins instead have a common width $w$, relative-frequency heights $n_j/n$ sum to one, but their total area is $w$, so those heights cannot generally be compared directly with a density curve.{{cite:nist_histogram}} (“Definition,” normalisation and density overlay)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Each density bar has area $w_j\,n_j/(nw_j)=n_j/n$. The disjoint bins assign every observation to exactly one interval, so $\sum_jn_j=n$. Hence the total area is $\sum_jn_j/n=1$. If the last edge is not made inclusive and equals an observed maximum, that observation would be omitted and the calculation would fail; a complete bin convention prevents the omission. If the observations are independent draws from a density $f$, the probability of bin $j$ is $p_j=\int_{b_j}^{b_{j+1}}f(x)\,dx$, and $n_j$ is binomial with parameters $n,p_j$. Its density height consequently has expectation $p_j/w_j$ and variance $p_j(1-p_j)/(nw_j^2)$. The expected height averages the true density across the bin, while the variance records sampling noise.{{cite:nist_histogram}} (“Definition,” area normalisation){{cite:scott1979_histograms}} (§2, expectation and variance of histogram height)
:::
:::

### What the bars estimate
The calculation reveals why a histogram is an estimator as well as a picture. It estimates the *average* density over each interval, so a peak narrower than the bin is flattened even when the sample is large. Narrowing the bin reduces that averaging, but also leaves fewer observations in it and makes its height less stable. For an ordinary smooth density, Scott's integrated-error analysis balances these effects and gives the characteristic $n^{-1/3}$ order for width. That rate describes the growth of detail with sample size; it does not prescribe one unchanging number of bars. The width and the grid origin should be reported when exact graphical conclusions matter. {{cite:scott1979_histograms}} (§§2–3, bias, variance and integrated error)

### Choosing the bins
Scott studied histogram width as a density-estimation problem, balancing variance from very narrow bins against bias from very wide ones. For a smooth continuous density his analysis leads to widths that shrink on the order of $n^{-1/3}$ as the sample grows. A practical normal-reference choice is about $3.49s\,n^{-1/3}$, where $s$ is a sample standard deviation. The Freedman–Diaconis choice $h=2\operatorname{IQR}/n^{1/3}$ substitutes a resistant spread measure, so one extreme observation has less influence on the proposed width. Both are starting points; a very small sample, tied measurements or a narrow subgroup may need explicit bin edges and inspection at several widths. {{cite:scott1979_histograms}} (§§3 and 5, asymptotic and normal-reference widths)

The creatinine display is a good reason to inspect the right tail and perhaps use a logarithmic scale, but the histogram alone does not establish a log-normal, gamma or any other sampling model. In the figure, the kernel density estimate smooths across observations instead of counting them in fixed intervals; it has its own bandwidth choice. Neither display reveals whether the creatinine distribution *conditional* on other patient features has the same shape as its marginal distribution. {{cite:nist_histogram}} (“Questions” and distributional-model cautions){{cite:chicco_jurman2020}} (§Methods, measured features)

## Worked example

Consider twelve measurements, in the same units: $0.2,0.4,0.8,1.1,1.2,1.4,1.8,2.1,2.4,2.6,3.0,5.7$. With unit-width bins $[0,1),[1,2),[2,3),[3,4),[4,5),[5,6)$, the counts are $3,4,3,1,0,1$. On a density scale the heights are $3/12=0.25$, $4/12\approx0.3333$, $3/12=0.25$, $1/12\approx0.0833$, $0$, and $1/12\approx0.0833$. The six areas sum to one. The empty $[4,5)$ bin separates the value $5.7$ from the main cluster, a detail worth checking against the raw measurements.{{cite:nist_histogram}} (“Definition,” density normalisation)

Now combine adjacent bins into $[0,2),[2,4),[4,6)$. Their counts become $7,4,1$, and their density heights are $7/24\approx0.2917$, $4/24\approx0.1667$, and $1/24\approx0.0417$. The broad last bar hides the empty interval between $4$ and $5$; the sample has not changed. This is why an apparent gap or mode should be read alongside the chosen edges. {{cite:scott1979_histograms}} (§§1–3, bin-width sensitivity)

**Your turn.** Eight observations are $0.2,0.6,0.9,1.1,1.4,1.8,2.2,3.6$. Using bins $[0,1),[1,2),[2,4)$, find the counts, the density heights and each rectangle's area.

::: {.callout-tip collapse="true" title="Answer"}
The counts are $3,3,2$ and the widths are $1,1,2$. The density heights are $3/8=0.375$, $3/8=0.375$ and $2/(8\cdot2)=0.125$. The areas are $0.375$, $0.375$ and $2/8=0.25$, summing to one. The third bar has a lower height partly because it is twice as wide; its area records the two observations.
:::

## Statistical use

Use the same edges and vertical scale when comparing samples, especially when their sizes differ. A count histogram of 1,000 people will tend to have taller bars than one of 100 even when their underlying shapes match; a density histogram makes the shapes more directly comparable. For example, 20 people out of 100 and 200 out of 1,000 both give a $20\%$ share in a two-unit-wide interval. Their count heights differ tenfold, whereas both density heights are $0.20/2=0.10$ per unit. The comparison concerns proportions of the two populations; it does not erase uncertainty from their different sample sizes. Keep the measurement unit on the horizontal axis and state whether the vertical axis shows counts, proportions or density. A density height can exceed one, and shifting the bin origin can change the counts.{{cite:nist_histogram}} (“Definition,” count and density axes)

A histogram shows one variable at a time. It cannot reveal association between two measurements, account for sampling bias, or distinguish a continuous population from a mixture merely because two bumps appear in a small sample. For the patient data, the median creatinine is 1.10 mg/dL and the maximum is 9.40 mg/dL: the distance between them explains the visual tail, while the histogram shows how sparsely that tail is populated. The same figure's log-scale panel draws in high values without deleting them. These are descriptions of the participants; the study design, measurement process and any conditional outcome model require separate analysis. {{cite:nist_histogram}} (“Questions” and “Related Techniques”){{cite:chicco_jurman2020}} (§Methods, study design)

## Common misconceptions

Bar height is not automatically a probability: on a density scale it is probability *per unit of the horizontal axis*, and area gives the bin fraction. A histogram also differs from a bar chart of categories: its neighbouring bars represent ordered numerical intervals, while categories need not be adjacent on a numerical scale. Choosing a convenient binning does not prove that a data set has exactly that many modes, and a smooth-looking histogram does not demonstrate a normal distribution. Finally, an empty interval is an observation about the sample and its chosen edges, not evidence that the population density is zero there.{{cite:nist_histogram}} (“Definition” and “Questions”){{cite:scott1979_histograms}} (§§1–3, width dependence)

## Assumptions and limits

Even four observations can change their outline when the origin moves. For $0.9,1.1,1.9,2.1$, unit bins $[0,1),[1,2),[2,3)$ have counts $1,2,1$; shifting them by half a unit to $[-0.5,0.5),[0.5,1.5),[1.5,2.5)$ gives $0,2,2$. Any strong shape claim from those four bars would depend on an arbitrary boundary. An outlier can also stretch automatic ranges and leave the main body compressed into a few bins. Heaped or rounded measurements can create spikes at recording increments; missing or censored values can erase a tail. Check the raw measurements and how they were collected before treating any bar pattern as a population feature.{{cite:nist_histogram}} (“Definition,” arbitrary classes; “Questions,” outliers and modes){{cite:scott1979_histograms}} (§§1 and 5, small samples and width sensitivity)

## Connections

[Kernel density estimation](kernel-density-estimator.qmd) replaces hard bin boundaries with smooth kernels and a bandwidth. A [boxplot](five-number-summary-and-boxplot.qmd) compresses the same variable into quartiles and outlier flags, while a [normal quantile plot](normal-quantile-plot.qmd) compares its ordered values with a reference shape. [Skewness](skewness.qmd) gives a numerical asymmetry summary, but a histogram reveals whether that number comes from a long tail or an isolated extreme point. [Transformations of data](transformations-of-data.qmd) change the horizontal scale and can clarify a long right tail.{{cite:nist_histogram}} (“Related Techniques” and “Questions”)

## History

Karl Pearson first used the term *histogram* in 1895, while the older practice of grouping observations in frequency displays predates that name. Scott's 1979 paper treated bin width as an estimation choice with a measurable bias–variance tradeoff. Freedman and Diaconis's later IQR-based choice offered a less outlier-sensitive way to set width. These developments explain why a histogram is both a descriptive picture and a statistical estimate whose binning matters.{{cite:dodge2008}} (p. 243, “Histogram,” History){{cite:scott1979_histograms}} (§§1, 3 and 5)
