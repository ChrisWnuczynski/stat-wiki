## Motivating example
Suppose a packaging line fills four labelled compartments with equal probability. Even when the mechanism is fair, the four observed counts will differ. Pearson's statistic combines those differences after measuring each against its expected size. Its reference distribution emerges from a multinomial sampling model, not from the visual similarity of a histogram to a bell curve. The approximation becomes useful when the sample is large relative to the number and probabilities of the cells.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, test statistic and critical region)

## Statement

**A fixed multinomial model.**
Let $X\sim\operatorname{Multinomial}(n,p)$ with a fixed number $k$ of categories, $p_i>0$ and $\sum_i p_i=1$. With the probabilities specified before looking at the counts,
$$T_n=\sum_{i=1}^k\frac{(X_i-np_i)^2}{np_i}\ \Rightarrow\ \chi^2_{k-1}.$$
The probabilities are the null-model probabilities, rather than the observed proportions substituted into the denominator. The restriction $\sum_i X_i=n$ removes one independent direction of variation, giving $k-1$ degrees of freedom. When parameters are fitted to the counts, an additional adjustment is required.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, definition and parameter estimation)

Large expected counts support the approximation, while a zero expected count makes the displayed statistic undefined. A structural impossibility should be excluded from the sample space before forming the test. If such a cell nevertheless has a positive observation, the proposed model assigns the data probability zero. An observed zero with a positive expectation is different and contributes the expected count to the statistic.{{cite:openintro2019}} (Chapter 6, “Testing for goodness of fit using chi-square”, conditions and expected counts)

## Intuition — Standardised counts live in a hyperplane
Write $D=\operatorname{diag}(p_1,\ldots,p_k)$ and $q=(\sqrt{p_1},\ldots,\sqrt{p_k})^T$. The vector
$$Z_n=D^{-1/2}(X-np)/\sqrt n$$
has mean zero and covariance $I-qq^T$. Also $q^TZ_n=0$ exactly, since the counts sum to $n$. The matrix $I-qq^T$ projects onto the $k-1$ dimensional space orthogonal to $q$. Pearson's statistic is the squared length $Z_n^TZ_n$. Its limit is the sum of squares of independent standard normals along an orthonormal basis of that space. This explains both the weighting and the degrees of freedom behind the chi-square calibration.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, statistic and degrees of freedom)

## Proof
Assume the multinomial central limit theorem. It gives $Z_n\Rightarrow Z$ with $Z\sim N_k(0,I-qq^T)$. Choose a matrix $B$ with $k-1$ orthonormal columns spanning $q^\perp$. Then $BB^T=I-qq^T$, and $Z$ has the same law as $BU$ for $U\sim N_{k-1}(0,I)$. Consequently $Z^TZ=U^TB^TBU=U^TU$. Continuity of the squared norm gives the asserted limit. No independence between the individual cell counts is needed; their negative covariances are precisely what the projection represents.

## Worked example — Four compartments
Take observed counts $(18,26,22,34)$ with total $100$ and four null probabilities equal to $1/4$. Each expected count is $25$. The contributions are $1.96$, $0.04$, $0.36$ and $3.24$, giving $T=5.60$. There are three degrees of freedom; the upper-tail probability is $0.132778$. At level $0.05$, this statistic is below the critical value $7.814728$. The sample does not provide enough evidence to reject the specified proportions. The decision does not establish that the probabilities are exactly equal.

**Your turn.** Change the counts to $(20,20,30,30)$, keeping the same null model. What is the statistic?

::: {.callout-tip collapse="true" title="Answer"}
The four deviations are $-5,-5,5,5$, so the statistic is $4(25/25)=4$ on three degrees of freedom.
:::

## Statistical use — Choose the cells before calibrating the tail
The test combines all directions of departure from the specified probabilities, so a small tail probability does not identify a particular alternative. Inspecting the individual contributions can reveal where the mismatch is concentrated. Changing bins or pooling categories after inspecting their departures changes the selection procedure and its null calibration. A grouping rule should therefore be specified as part of the analysis plan.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, binned data and sensitivity to binning)

The approximation also assumes independent sampled units under the multinomial model. Clustered observations can produce extra variation even when the marginal proportions are correct. Increasing the sample size does not repair a wrong dependence model. For a genuinely small independent sample, a multinomial calculation or a simulation that reproduces the null mechanism can be more appropriate than treating the asymptotic tail as exact.{{cite:openintro2019}} (Chapter 6, “Testing for goodness of fit using chi-square”, independence and sample-size conditions)
