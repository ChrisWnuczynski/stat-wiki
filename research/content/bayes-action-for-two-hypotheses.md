## Motivating example
A quality controller can release a shipment or investigate it. A posterior probability of poor quality answers an uncertainty question; a decision additionally requires the consequences of a mistaken release and an unnecessary investigation. The action with the higher chance of naming the true hypothesis can have the higher expected cost.{{cite:pishro_nik2014}} (§9.1.8, minimum cost hypothesis test)

## Key results — A probability threshold determined by consequences
Put $q=P(H_1\mid x)$, where $H_1$ denotes the event requiring action $a_1$. Correct decisions have zero loss, a missed event costs $L_{01}$ and a false alarm costs $L_{10}$. Choosing $a_1$ minimises posterior risk exactly when
$$
L_{10}(1-q)<L_{01}q
\quad\Longleftrightarrow\quad
q>\frac{L_{10}}{L_{01}+L_{10}}.
$$
Equality makes both actions optimal. This version remains meaningful at $q=0$ or $1$, where an odds ratio may involve division by zero. Multiplying both costs by the same positive constant leaves the action unchanged.{{cite:pishro_nik2014}} (§9.1.8)

For a general loss table, let $L(a,h)$ denote the cost of taking action $a$ when state $h$ holds. Compare $\sum_hL(a,h)P(h\mid x)$ across actions. Nonzero correct-decision costs can therefore be included without reinterpreting the posterior probabilities. A cost-free statement of the hypotheses does not determine this table.{{cite:rasmussen_williams2006}} (§3.1.1, pp. 35–36)

When the hypotheses have likelihoods $f_0(x),f_1(x)$ and prior probabilities $\pi_0,\pi_1$, posterior odds equal $(\pi_1/\pi_0)f_1(x)/f_0(x)$. Thus prior odds, likelihood ratio and loss ratio enter different parts of the calculation. Changing a decision cost changes the action threshold, while the posterior probability under a fixed model stays the same.{{cite:pishro_nik2014}} (§9.1.8)

## Worked example

### The fruit posterior under two loss tables
For the fruit-count model, the shape–rate posterior $\theta\mid x\sim\operatorname{Gamma}(189,21)$ gives $P(H_1\mid x)=P(\theta>10\mid x)=0.06701619$. With equal unit error costs, release has posterior risk $0.06701619$ and investigation has risk $0.93298381$, so release is preferred. These are posterior expected losses under the two-action model.{{cite:rasmussen_williams2006}} (§3.1.1, p. 36)

Now let a mistaken release cost $20$ and an unnecessary investigation cost $1$. The risks become $20(0.06701619)=1.34032384$ and $0.93298381$. Investigation now has lower risk. Equivalently, the threshold is $1/21=0.04761905$, below the posterior event probability. The posterior distribution and its equal-tailed interval have not changed. The same probability calculation supports a different action once the consequences change.{{cite:pishro_nik2014}} (§9.1.8)

Randomising between the two actions cannot improve on the smaller risk: a mixture with probability $r$ on $a_1$ has risk $r\rho(a_1\mid x)+(1-r)\rho(a_0\mid x)$, a convex combination. At a tie every such mixture has that same risk. If an additional action such as collecting another measurement is available, its cost and future consequences must be included in a larger decision problem.{{cite:rasmussen_williams2006}} (§3.1.1, p. 36)

**Your turn.** Keep the posterior event probability fixed, but set the missed-event cost to $10$ instead of $20$. Which action wins?

::: {.callout-tip collapse="true" title="Answer"}
Release has risk $0.67016192$, below investigation risk $0.93298381$. Its threshold is $1/11\approx0.09091$, above the event probability, so release is preferred.
:::
