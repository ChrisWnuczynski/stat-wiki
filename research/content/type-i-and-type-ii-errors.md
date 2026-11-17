## Motivating example

A coach wants evidence that a player now lands more than 60% of first serves. With 15 independent serves, a rule that declares improvement after at least 13 successes can wrongly declare improvement when the true rate is still 60%, or miss improvement when the true rate has risen to 80%. Naming the two mistakes makes it possible to compare rules before seeing the serves. The power-curve figure below shows the consequences of changing the cutoff.{{cite:siegrist2022_testing}} (§9.1, Hypotheses and Errors)

## Definition

Let $R$ be the rejection region of a test of $H_0$ against $H_1$. A **type I error** occurs when the data fall in $R$ although $H_0$ is true. A **type II error** occurs when the data fall outside $R$ although an alternative is true. The latter decision is *failure to reject*, not a demonstration that $H_0$ is true. For a simple null with distribution $P_0$, the false-rejection probability is $P_0(R)$; for a composite null it can differ across parameter values, and the test's size is $sup_{	hetainTheta_0}P_\theta(R)$. A level-$\alpha$ test has size at most $\alpha$, so a discrete test may have actual size below its advertised level.{{cite:siegrist2022_testing}} (§9.1, Hypotheses and Errors){{cite:dodge2008}} (pp. 550–552, Type I Error and Type II Error)

At a specified alternative $\theta\in\Theta_1$, write $\beta(\theta)=P_\theta(R^c)$ for the probability of type II error. Its complement $1-\beta(\theta)=P_\theta(R)$ is **power**. There is usually no single beta for a composite alternative: a weak change can be hard to detect while a large one is easy. The two errors are probabilities under *different* hypothetical distributions; neither is a posterior probability that one hypothesis is true given the observed data. {{cite:siegrist2022_testing}} (§9.1, Errors and Power)

## Interpretation

The normal-density figure uses a two-sided $z$ rule with null $N(0,1)$ and cutoffs $\pm1.960$. Both null tails together have area $0.05$, the type I probability. An observed $z=2.30$ has two-sided $p\approx0.021$, which is an observed tail area, not the probability that this particular rejection is a mistake. Under the pictured $N(2,1)$ alternative, the area *between* the cutoffs is $\beta\approx0.484$ and the remaining area gives power $\approx0.516$. A test can therefore have small type I probability and still miss nearly half of changes of this size.{{cite:siegrist2022_testing}} (§9.1, Errors, Power and P-value)

The first-serve curve gives a discrete counterpart. For $X\sim\operatorname{Bin}(15,p)$, rejecting $H_0:p=0.6$ when $X\ge13$ has actual size $0.0271$ and power $0.398$ at $p=0.8$; at $p=0.9$ its power is $0.816$. Moving the cutoff to $12$ increases power at every $p$, but raises size to $0.0905$, above a $0.05$ limit. This is a property of the *rule*, before the 15 serves are observed. {{cite:siegrist2022_testing}} (§9.1, Errors and Power)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The rejection and nonrejection regions $R$ and $R^c$ partition the sample space. Hence for any fixed alternative $\theta$, $P_\theta(R)+P_\theta(R^c)=1$, proving power $=1-\beta(\theta)$. If $R_1\subseteq R_2$, then $P_\theta(R_1)\le P_\theta(R_2)$ under every distribution: enlarging a rejection region cannot lower either type I probability under a null or power under an alternative. For a normal statistic $Z\sim N(\delta,1)$ rejected when $Z>c$, standardization gives $\alpha=1-\Phi(c)$ at $\delta=0$ and $\beta(\delta)=\Phi(c-\delta)$ at a fixed $\delta>0$. These identities explain the tradeoff in a one-sided normal test. They do not imply that increasing sample size must raise type I error: sample size can separate the null and alternative distributions while retaining the same null cutoff.{{cite:siegrist2022_testing}} (§9.1, Errors and Power)
:::
:::

## Worked example

Suppose a standardized measurement is $Z\sim N(0,1)$ under $H_0$ and $Z\sim N(1,1)$ under a specified alternative. Reject above $1.645$. The null tail is $\alpha\approx0.0500$. Under the alternative, nonrejection means $Z\le1.645$, giving $\beta=\Phi(1.645-1)\approx0.7405$ and power $\approx0.2595$. Thus this apparently stringent test catches only about one quarter of shifts of one standard deviation in a single reading. The probabilities describe repeated use of the rule under each stipulated model, not the truth probability of the hypothesis after one result.{{cite:siegrist2022_testing}} (§9.1, Errors and Power)

**Your turn.** Keep the same cutoff and null model, but suppose the alternative mean is $2$. What are beta and power, and which error probability stays fixed?

::: {.callout-tip collapse="true" title="Answer"}
Under $N(2,1)$, $\beta=\Phi(1.645-2)\approx0.3612$ and power is $1-\beta\approx0.6388$. The null distribution and rejection rule have not changed, so the type I probability remains about $0.0500$. A larger shift is easier to detect.
:::

## Common misconceptions

A 5% level does not mean a 5% probability that a rejected null was true: level conditions on the null being true, whereas that statement conditions on the observed rejection. A $p$-value of $0.021$ is an observed null tail area, not a new estimated type I probability for this decision. Failing to reject does not establish the null: the serve test misses a true 80% success rate with probability about $0.602$. Finally, beta is not fixed by alpha alone; it changes with the alternative, sample size and test statistic.{{cite:siegrist2022_testing}} (§9.1, Errors, Power and P-value)

## Assumptions and limits — When the nominal errors fail

If serves come in dependent streaks, $X$ is not binomial and the quoted $0.0271$ size need not hold. If the normal $z$ test uses a standard error that is too small, its actual null tail can exceed $0.05$. Testing twenty independent nulls separately at level $0.05$ gives a chance $1-0.95^{20}\approx0.642$ of at least one false rejection, so a single-test level is not a familywise guarantee. Even with a valid model, the 15-serve rule's type II probability at $p=0.8$ is about $0.602$: a nonrejection is weak evidence when the test has such limited power.{{cite:siegrist2022_testing}} (§9.1, Errors and Power)

## Connections

The power function collects rejection probabilities across all parameter values: on the null it records false-rejection probabilities, and on the alternative it records detection probabilities. Choosing a rejection region therefore links type I/type II error to critical values, sample-size planning, Neyman–Pearson comparisons and confidence-set coverage. A confidence interval that excludes the null value gives a corresponding rejection rule; its coverage under the null controls that rule's type I probability.{{cite:siegrist2022_testing}} (§9.1, Power and Equivalence Between Hypothesis Test and Confidence Sets)

## History

Neyman and E. S. Pearson's 1928 work considered both error types explicitly, so that a test had to account for an alternative as well as a null. The resulting framework evaluates a procedure by its long-run error probabilities across possible data-generating distributions.{{cite:dodge2008}} (p. 551, History){{cite:siegrist2022_testing}} (§9.1, Preliminaries)
