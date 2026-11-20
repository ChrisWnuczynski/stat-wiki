## Motivating example
A small trial can produce a table with several sparse cells. Rather than approximate its count distribution by a continuous curve, one can enumerate possible tables after conditioning on the observed margins. Fisher's test uses this conditional experiment. Its calibration is finite-sample, and the possible tail probabilities are discrete.{{cite:agresti1992_exact_survey}} (§§1.3–2.1, pp. 133–135)

## Definition — Conditional independence as an odds-ratio hypothesis
Write the table as rows $(a,b)$ and $(c,d)$. Under independence, the population odds ratio is one. If row totals and the first column total are fixed, the top-left count $A$ has a hypergeometric law. It counts how many first-column labels fall in the first row under random allocation.{{cite:dodge2008}} (p. 247, Hypergeometric Distribution) For total $n$, first-row total $r$ and first-column total $s$,
$$\Pr(A=k\mid r,s,n)=\frac{\binom r k\binom{n-r}{s-k}}{\binom n s}.$$
The possible $k$ run from $\max(0,r+s-n)$ through $\min(r,s)$. Conditioning removes the nuisance marginal probabilities from the null law.{{cite:agresti1992_exact_survey}} (§1.3, eq. 1.2, pp. 133–134)

## Properties — Exact calibration and two-sided conventions
A one-sided alternative with odds ratio greater than one treats larger top-left counts as stronger evidence. Its tail includes the observed count. A probability-ordering two-sided test includes all tables whose null probability is no larger than the observed table's. Doubling a one-sided tail is another convention and can differ when the null law is asymmetric. The test and its convention should therefore be identified together.{{cite:agresti1992_exact_survey}} (§2.1, pp. 134–135)

For fixed margins, an exact nonrandomised test can have rejection probability below its nominal level. Its attainable probabilities jump between table configurations. Increasing the nominal level slightly need not change the rejection set. That discreteness is compatible with finite-sample control.{{cite:agresti1992_exact_survey}} (§§2.1–2.2, pp. 134–135)

## Worked example — A probability ordering for twenty people
For rows $(8,2)$ and $(3,7)$, the margins give $n=20$, $r=10$ and $s=11$. The top-left count ranges from one to ten. The observed table's probability is $0.0321505$, and the upper tail from eight through ten has probability $0.0348893$. Including every table with probability no greater than the observed one gives counts $1,2,3,8,9,10$ and two-sided probability $0.0697785$. At level $0.05$, the upper-tail test rejects while this two-sided test does not. Choosing the direction after seeing the table would change the testing procedure.

**Your turn.** What is the observed cross-product odds ratio for this table? Is it the same object as the exact test's $p$-value?

::: {.callout-tip collapse="true" title="Answer"}
The sample cross-product ratio is $(8\cdot7)/(2\cdot3)=28/3$. It measures observed association on an odds scale. The $p$-value is a tail probability under a specified null distribution.
:::

## Check yourself

Use the definitions and calculations above to work through these questions.

### A smaller conditional experiment {#self-check-ex-inf-fisher-smaller}

[A smaller conditional experiment](../questions/ex-inf-fisher-smaller.qmd). List the top-left counts and compute the upper tail.

::: {.callout-tip collapse="true" title="Answer"}
The possible counts are $0,1,2,3$. At three, the mass is $\binom43\binom30/\binom73=4/35$. No larger count is possible, so the one-sided tail is also $4/35$.
:::

### Identify the sampling design {#self-check-ex-inf-homogeneity-or-independence}

[Identify the sampling design](../questions/ex-inf-homogeneity-or-independence.qmd). Distinguish the fixed and random margins.

::: {.callout-tip collapse="true" title="Answer"}
The two-drug trial fixes treatment totals and tests homogeneity of improvement probabilities. The clinic survey fixes only its total and tests independence of classifications. The factories fix factory totals and test homogeneity of defective probabilities.
:::
