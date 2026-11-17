## Motivating example
Five crop varieties generate ten pairwise mean comparisons. A researcher who inspects them all and reports the most promising one has made a different selection from a researcher who specified one comparison before observing data. Error control must refer to the family of claims actually being supported. A collection of nominal 95% intervals does not automatically have 95% simultaneous coverage.{{cite:holmes_huber2019_msmb}} (§6.8, The family wise error rate)

## Intuition — One failure among many
Let $A_j$ be the event that interval $j$ misses its target. Familywise error is $P(\bigcup_j A_j)$. With $m$ independent tests each of size $\alpha$ under its null, this is $1-(1-\alpha)^m$. Pairwise mean comparisons share observations and are generally dependent, so that independent formula is an illustration rather than a formula for every family. The union bound always gives $P(\bigcup_j A_j)\le\sum_jP(A_j)$ without an independence assumption.{{cite:holmes_huber2019_msmb}} (§6.8, eq. (6.6)){{cite:nist_bonferroni2002}} (§7.4.7.3, Bonferroni general inequality)

## Properties — Bonferroni and Tukey answer different families
Bonferroni assigns each of $m$ statements an error budget $\alpha/m$. The union bound then proves that the probability of any error is at most $\alpha$. For two-sided intervals based on a $t_\nu$ pivot, the multiplier is $t_{\nu;1-\alpha/(2m)}$. This construction supports any prespecified finite set of valid individual pivots, including contrasts beyond pairwise differences.{{cite:nist_bonferroni2002}} (§7.4.7.3, confidence interval formula)

Tukey's equal-size method exploits the structure of all pairwise mean differences. Assume independent normal errors with common variance, $k$ groups of size $r$, and an independent pooled error variance estimate $s^2$ with $\nu=k(r-1)$ degrees of freedom. For standardized mean errors $Z_i=\sqrt r(\overline Y_i-\mu_i)/\sigma$, all pairwise estimation errors are bounded by $\max_i Z_i-\min_i Z_i$. Dividing this range by $s/\sigma$ gives a studentized range variable, so its $1-\alpha$ quantile produces simultaneous half-width $q_{k,\nu;1-\alpha}s/\sqrt r$. This proves why one range calibration controls every pair at once.{{cite:nist_handbook2002}} (§7.4.7.1, Tukey's method)

Familywise error differs from the false discovery rate, which averages the false fraction among rejections. A method controlling one quantity should not be advertised as controlling the other. Also, failing to exclude zero is compatible with imprecise estimation; it does not establish that the group means are equal.{{cite:holmes_huber2019_msmb}} (§§6.8–6.9, FWER and false discovery rate)

## Worked example — Ten chances and a simultaneous interval
For ten independent null tests at individual level $0.05$, the probability of at least one rejection is $1-0.95^{10}\approx0.401263$. Bonferroni uses level $0.005$ per test for a familywise target of $0.05$ and works even when the tests are dependent.

For the five-variety balanced illustration, the pooled mean square is $10.57$ with ten error degrees of freedom and three observations per group. The studentized-range quantile is approximately $4.6543$, producing half-width $4.6543\sqrt{10.57/3}\approx8.7364$. A mean difference of $-10.8667$ then has simultaneous interval about $(-19.60,-2.13)$ and excludes zero. All ten intervals must use the same family definition and model assumptions. Their joint calibration does not repair a confounded crop comparison.{{cite:nist_handbook2002}} (§7.4.7.1, Studentized Range Distribution)

**Your turn.** A study plans four tests and wants familywise error at most $0.05$. Find the Bonferroni per-test level and adjusted p-value for a raw p-value of $0.009$.

::: {.callout-tip collapse="true" title="Answer"}
The per-test level is $0.05/4=0.0125$. The adjusted p-value is $\min(1,4\times0.009)=0.036$, so this test rejects at familywise level $0.05$.
:::

## Assumptions and limits
The family should describe the claims intended for joint interpretation. Splitting a search into small families after seeing favorable results changes its error interpretation. Tukey's exact balanced calibration depends on the normal common-variance model; unequal variances call for methods suited to that setting. Bonferroni can be conservative, especially with strongly overlapping error events, but its elementary bound remains valid without knowing their dependence.{{cite:holmes_huber2019_msmb}} (§6.8.1){{cite:nist_bonferroni2002}} (§7.4.7.3)
