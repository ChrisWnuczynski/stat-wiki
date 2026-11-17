## Lead context
The pooled standard error estimates a common success probability under the equality null. It is a testing denominator; estimation of a difference generally uses a different standard error.{{cite:openintro2019}} (§6.2, pooled proportion)

## Motivating example
Two independently sampled groups have $60$ successes in $100$ trials and $75$ in $150$. The sample proportions differ by $0.10$. Under the null that their population proportions agree, both samples inform a single probability, estimated by $135/250=0.54$. Pooling therefore weights group proportions by their sample sizes.{{cite:openintro2019}} (§6.2, testing two proportions)

## Properties — Derive the denominator under the null
For independent binomial counts $X_i\sim\operatorname{Bin}(n_i,p_i)$, $\operatorname{Var}(\widehat p_1-\widehat p_2)=p_1(1-p_1)/n_1+p_2(1-p_2)/n_2$. Under $H_0:p_1=p_2=p$ this reduces to $p(1-p)(1/n_1+1/n_2)$. Maximising the joint null likelihood gives $\widehat p=(X_1+X_2)/(n_1+n_2)$, so substitution yields the pooled $z$ statistic. The binomial assumptions concern independent trials with a stable probability within each group.{{cite:dodge2008}} (pp. 44–45){{cite:openintro2019}} (§6.2, null standard error)

In a two-by-two table the null fitted cell counts are row total times column total divided by the grand total. Substituting those four expectations into Pearson's sum and simplifying gives exactly $X_P^2=z^2$ for the uncorrected procedures. Thus the $\chi_1^2$ upper tail and the two-sided normal tail agree. Rounding intermediate fitted counts can obscure the identity.

## Worked example
For the motivating counts,
$$
\widehat p_1-\widehat p_2=0.10,\qquad
SE_0=\sqrt{0.54(0.46)(1/100+1/150)}=0.06434.
$$
The statistic is $z=1.5542$, giving a two-sided normal probability $0.1201$. The null expected counts are $54,46,81,69$, all comfortably away from zero. This supports the large-sample approximation; it does not supply independence if trials were clustered.{{cite:openintro2019}} (§6.2, success–failure condition)

For a confidence interval for $p_1-p_2$, the unpooled estimate is $SE=\sqrt{0.6(0.4)/100+0.5(0.5)/150}=0.06377$. The approximate $95\%$ interval is $0.10\pm1.96(0.06377)=[-0.0250,0.2250]$. This interval and the pooled test need not be exact inverses because their variance estimates impose different restrictions.{{cite:openintro2019}} (§6.2, interval standard error versus pooled testing standard error)

**Your turn.** If both groups have observed proportion $0.5$, what are the pooled estimate and the equality-test statistic, for any positive sample sizes?

::: {.callout-tip collapse="true" title="Answer"}
The pooled estimate is $0.5$ and the numerator is zero, so $z=0$ and the two-sided normal probability is $1$.
:::

## Assumptions and limits
Small expected success or failure counts can make the normal approximation poor. Paired binary measurements require a paired analysis on the discordant pairs, with a variance that uses the within-pair dependence. A one-sided alternative is part of the rejection rule fixed before the data are seen. When the observed difference has the sign named by that alternative, symmetry of the standard normal law makes the one-sided tail half the two-sided tail. An observed difference of the opposite sign falls in the large part of a one-sided tail.{{cite:openintro2019}} (§6.2, conditions and alternative hypotheses)

## Definition — The statistic and its null standard error
For independent counts $X_i\sim\operatorname{Bin}(n_i,p_i)$ with $n_i\ge1$, write $\widehat p_i=X_i/n_i$ and
$$
\widehat p=\frac{X_1+X_2}{n_1+n_2},\qquad
z=\frac{\widehat p_1-\widehat p_2}{\sqrt{\widehat p(1-\widehat p)\bigl(1/n_1+1/n_2\bigr)}}.
$$
The denominator is defined when $0<\widehat p<1$. Under the equality null $p_1=p_2=p\in(0,1)$, the true variance of the numerator is $p(1-p)(1/n_1+1/n_2)$. Substituting the pooled maximum-likelihood estimate $\widehat p$ produces the displayed standard error. The resulting $z$ is the score statistic for that one-dimensional null, referred to a standard normal law in large samples.{{cite:dodge2008}} (pp. 44–45){{cite:openintro2019}} (§6.2, null standard error)

An interval for the difference uses a different standard error,
$$
SE_u=\sqrt{\frac{\widehat p_1(1-\widehat p_1)}{n_1}+\frac{\widehat p_2(1-\widehat p_2)}{n_2}},
$$
and the approximate interval $\widehat p_1-\widehat p_2\pm z_{1-\alpha/2}\,SE_u$. The pooled standard error is the testing denominator under a common probability. The unpooled standard error is the large-sample standard error of the estimated difference when the two probabilities are left free. The two expressions agree algebraically when $\widehat p_1=\widehat p_2$, and they diverge as soon as the sample proportions diverge.{{cite:openintro2019}} (§6.2, interval standard error versus pooled testing standard error)

## Interpretation — Sample size is the weight in the pooled estimate
The pooled estimate is the total number of successes divided by the total number of trials. With counts $10$ successes in $20$ trials and $40$ successes in $180$ trials,
$$
\widehat p=\frac{10+40}{20+180}=0.250000,
$$
while the unweighted average of the sample proportions $0.500000$ and $0.222222$ is $0.361111$. The larger trial contributes more successes and more failures, so it pulls $\widehat p$ toward $0.222222$. The numerator of $z$ is $0.500000-0.222222=0.277778$. The null standard error is
$$
SE_0=\sqrt{0.25\times0.75\times\bigl(1/20+1/180\bigr)}=0.102062,
$$
so $z=2.721655$ and the two-sided normal probability is $0.006496$. The unpooled standard error for the same counts is $0.116018$. An approximate $95\%$ interval for the difference is $0.277778\pm1.96\times0.116018$, which runs from $0.050383$ to $0.505173$. Both endpoints are positive, in line with a two-sided test that rejects equality at the $5\%$ level for these particular counts. That agreement is a feature of this numerical example. The motivating counts $60/100$ and $75/150$ produce a two-sided probability $0.1201$ and an interval $[-0.0250,0.2250]$ that contains zero, because the pooled and unpooled standard errors answer different variance questions and the normal critical value is a fixed cutoff.{{cite:openintro2019}} (§6.2, testing two proportions)

## Intuition — Why the four expected counts recover $z^2$
Arrange the data as a two-by-two table with rows as groups and columns as success and failure. Under independence of group and outcome, the fitted count in a cell is the product of its row total and its column total, divided by the grand total. For the counts above, the grand total is $200$, the success total is $50$, and the expected table is
$$
\begin{pmatrix}5&15\\45&135\end{pmatrix}.
$$
Each group is assigned the common proportion $0.25$. Pearson's statistic sums $(O-E)^2/E$ over the four cells and equals $7.407407$. The same arithmetic gives $z^2=2.721655^2=7.407407$. The identity is exact for the uncorrected procedures, before any continuity adjustment and before rounding the expected counts. Squaring removes the sign of $\widehat p_1-\widehat p_2$, so the upper tail of $\chi^2_1$ matches the two-sided standard-normal tail. A one-sided question keeps the sign and uses one normal tail.{{cite:dodge2008}} (pp. 44–45){{cite:openintro2019}} (§6.2, pooled proportion)

The algebra behind the identity is short. The deviation in the first success cell is $X_1-n_1\widehat p=(n_2X_1-n_1X_2)/(n_1+n_2)$. The failure deviation in that row is the negative of the success deviation, because the row total is fixed. The second row repeats the same absolute deviations. Substituting $\widehat p(1-\widehat p)$ for the Bernoulli variance and clearing the common factors leaves $z^2$. The derivation uses the row totals as fixed sample sizes, which is the binomial sampling scheme. A different sampling scheme, such as a single multinomial total with both margins random, still produces the same algebraic expression for this two-by-two pattern, and its reference distribution is a separate modelling choice.

## Statistical use — State the sampling unit and the alternative
The variance formula adds the two binomial variances. That addition is the variance of a difference of independent counts. Trials nested in clusters, or two measurements on the same person, share variation, and the independent-sample standard error is then the wrong denominator. The scientific report names the sampling unit, the success definition, the two sample sizes, the two proportions, the pooled estimate, $z$, and whether the alternative was one-sided or two-sided. An interval for $p_1-p_2$ is reported with $SE_u$, so a reader can see the range of differences compatible with the unrestricted fit.{{cite:openintro2019}} (§6.2, conditions and alternative hypotheses)

The normal reference is a large-sample approximation. The motivating table has null expected counts $54,46,81,69$, all far from the boundary of the table. The second table has expected counts $5,15,45,135$. The cell with expectation $5$ is the fragile one: the normal and chi-squared approximations are rougher there, and an exact conditional test that fixes both margins is a different procedure with a different conditional probability. The $z$ formula itself remains the standardised difference under the pooled null; the quality of the normal tail is a separate judgement about those expected counts.{{cite:openintro2019}} (§6.2, success–failure condition)

## Common misconceptions
The pooled estimate is a weighted mean of the two sample proportions, with weights $n_1$ and $n_2$. It equals the ordinary average of $\widehat p_1$ and $\widehat p_2$ when the sample sizes are equal, and also when the two proportions are equal. In the unequal example the proportions differ and the sample sizes differ, so $0.250000$ and $0.361111$ are different summaries. Using $0.361111$ in the null standard error would answer a different numerical question from the maximum-likelihood null.

A significant two-sided test and a confidence interval that excludes zero are related summaries, and they use different standard errors. In the motivating example the interval contains differences of both signs while $z=1.5542$. In the second example both summaries fall on the side of a positive difference. Each summary should be read with the standard error that defines it. The one-sided probability equals half the two-sided probability when the observed sign matches a direction that was fixed in advance, because the standard normal density is symmetric about zero.{{cite:openintro2019}} (§6.2, conditions and alternative hypotheses)

## Connections
The binomial variance $p(1-p)/n$ is the one-sample ingredient. The two-sample null adds two such terms and replaces the unknown common $p$ by $\widehat p$. Pearson's chi-squared statistic on one degree of freedom is the square of this $z$ for a two-by-two table. A logistic regression with a single group indicator estimates the log odds ratio; its Wald test of a zero coefficient is a related large-sample comparison and uses the logistic likelihood's curvature, so its numerical value need not reproduce $z$ on a finite table. The pooled $z$ statistic remains the direct standardisation of $\widehat p_1-\widehat p_2$ under a common success probability.{{cite:dodge2008}} (pp. 44–45){{cite:openintro2019}} (§6.2, null standard error)
