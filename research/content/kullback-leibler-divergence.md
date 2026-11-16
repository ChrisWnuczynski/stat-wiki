## Lead context
Kullback–Leibler divergence measures how much a probability model q is surprised, on average, when the observations actually follow p.

## Motivating example
A coin lands heads with probability $0.8$. Someone who predicts with a fair coin, probability $0.5$, pays a penalty every toss. In nats,
$$
0.8\log(1.6)+0.2\log(0.4)\approx 0.1927.
$$
The reverse comparison, predicting the biased coin when the coin is fair, costs about $0.2231$ nats. The two numbers differ. A divergence that was a distance would not.{{cite:shannon1948}} (Thm. 2, discrete entropy)

## Intuition
Shannon's entropy $H=-\sum p_i\log p_i$ is the average surprise of outcomes drawn from $p$, when the code is also built from $p$. If the code is built from another distribution $q$, the average surprise is $-\sum p_i\log q_i$. The extra surprise is
$$
D(p\,\Vert\,q)=\sum_i p_i\log\frac{p_i}{q_i}= -\sum_i p_i\log q_i - H(p).
$$
The entropy does not depend on $q$. Choosing $q$ to minimise $D(p\,\Vert\,q)$ is the same as choosing $q$ to maximise the expected log score $\sum p_i\log q_i$.{{cite:shannon1948}} (Thm. 2)

The logarithm may be natural, giving nats, or base $2$, giving bits. The two differ by the constant factor $\log 2$. The value $0.1927$ nats is $0.2781$ bits.

## Definition
For discrete distributions on the same set, with $q_i>0$ whenever $p_i>0$,
$$
D(p\,\Vert\,q)=\sum_i p_i\log\frac{p_i}{q_i},
$$
and the convention $0\log 0=0$ covers a zero mass in $p$. For densities the sum becomes $\int p\log(p/q)$. The integral is infinite when $q$ puts no mass where $p$ does.

Hastie, Tibshirani and Friedman identify the mutual information of a random vector with this divergence between the joint density and the product of its marginals. Independence makes that divergence zero.{{cite:hastie_esl2009}} (§14.7, pp. 561, mutual information as Kullback–Leibler distance)

## Interpretation — What is held fixed
In model fitting the unknown true distribution plays the role of $p$ and the fitted distribution plays the role of $q$. The constant $\int p\log p$ cancels when two candidates are compared, so ranking models by expected log score is ranking them by $D(p\,\Vert\,q)$. Akaike's criterion estimates that expected score from the training log-likelihood, with a penalty for the number of fitted parameters. The divergence itself is a population comparison. It is not a test statistic with a critical value.

The order matters. $D(p\,\Vert\,q)$ penalises a $q$ that is too small where $p$ is positive. $D(q\,\Vert\,p)$ penalises the opposite mismatch. A fair-coin model for a biased coin, and a biased-coin model for a fair coin, are different errors, as the numbers $0.1927$ and $0.2231$ show.

## Properties
The divergence is nonnegative, and it is zero only when $p=q$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Where $p_i>0$, the inequality $\log u\le u-1$ at $u=q_i/p_i$ gives
$$
\log\frac{q_i}{p_i}\le\frac{q_i}{p_i}-1.
$$
Multiply by $p_i$, which is nonnegative, and sum:
$$
\sum_i p_i\log\frac{q_i}{p_i}\le\sum_i(q_i-p_i)=0,
$$
because both distributions sum to $1$ and $q_i$ is summed only over the support of $p$ when $q$ covers that support. Therefore $D(p\,\Vert\,q)\ge 0$. Equality in $\log u=u-1$ holds only at $u=1$, so $q_i=p_i$ wherever $p_i>0$.{{cite:shannon1948}} (Thm. 2)

For the two-point example,
$$
0.8\log 1.6+0.2\log 0.4=0.192744757\ldots,
$$
which rounds to $0.1927$ nats. Dividing by $\log 2$ gives $0.2781$ bits. The reverse divergence rounds to $0.2231$ nats.
:::
:::

## Statistical use — Scores, codes, and fitted models
A code built for $q$ has expected length, under the true $p$, equal to the entropy of $p$ plus $D(p\,\Vert\,q)$, up to the choice of logarithm base. That is the operational reading of the extra surprise. In a parametric model the same gap is the population target that maximum likelihood estimates when the model is wrong: the fitted parameter settles on the member of the family closest to the truth in this divergence, not on a parameter the truth does not have.

For a joint distribution, mutual information is $D(p\,\Vert\,p_1 p_2\cdots)$. It is zero precisely when the coordinates are independent, which is why an independent-component analysis can hunt for a rotation that makes this divergence small.{{cite:hastie_esl2009}} (§14.7, pp. 561)

## Worked example
Take $p=(0.8,0.2)$ and $q=(0.5,0.5)$, with natural logarithms. Then
$$
D(p\,\Vert\,q)=0.8\log 1.6+0.2\log 0.4\approx 0.1927
$$
nats, and
$$
D(q\,\Vert\,p)=0.5\log(0.5/0.8)+0.5\log(0.5/0.2)\approx 0.2231
$$
nats. In bits the first value is $0.2781$. Replacing $q$ by $p$ gives
$$
0.8\log 1+0.2\log 1=0.
$$
A third candidate $r=(0.8,0.2)$ is $p$ itself. Any other $r$ on the two-point set leaves a positive penalty.{{cite:shannon1948}} (Thm. 2)

**Your turn.** Compute $D(p\,\Vert\,r)$ for $p=(0.8,0.2)$ and $r=(0.9,0.1)$, to four decimal places in nats, and say whether it is smaller than $0.1927$.

::: {.callout-tip collapse="true" title="Answer"}
$$
0.8\log(0.8/0.9)+0.2\log(0.2/0.1)=0.8\log(8/9)+0.2\log 2\approx 0.0444.
$$
This is smaller than $0.1927$. The candidate $r$ is closer to $p$ than the fair coin is, in the forward divergence.{{cite:shannon1948}} (Thm. 2)
:::

## Common misconceptions
The divergence is not symmetric, and it does not satisfy the triangle inequality, so it is not a distance in the geometric sense. Calling it a distance, as some displays do when they mean this discrepancy, does not create those two properties.

A small divergence does not mean the probabilities are close in every coordinate. One very small $q_i$ under a moderate $p_i$ can dominate the sum, because $\log(p_i/q_i)$ becomes large.

Bits and nats are not interchangeable numbers. Forgetting $\log 2$ reports $0.1927$ where the code length in bits is $0.2781$.

Finally, $D(p\,\Vert\,q)$ with the true distribution in the first slot is the fitting target. Swapping the slots scores a different experiment, in which $q$ is true and $p$ is the prediction.

## Assumptions and limits — When the sum is infinite or the log is illegal
If some $q_i=0$ while $p_i>0$, the term $p_i\log(p_i/q_i)$ is infinite. A model that declares an observed outcome impossible is infinitely far from the truth in this divergence, however well it fits the other outcomes. The inequality $\log u\le u-1$ was applied only on the support of $p$, so a $q$ that puts extra mass outside that support does not by itself create a finite penalty. The penalty comes from being too thin where $p$ lives.

The discrete formula assumes a common set of atoms. A density and a point mass on the line are not compared by writing a ratio of their formulas. One of them is not absolutely continuous with respect to the other, and the divergence is infinite.

Changing the base of the logarithm changes the numerical value and not the ranking of candidates, because every value is multiplied by the same positive constant.

## Connections
[Gibbs' inequality](gibbs-inequality.qmd) is the statement $D(p\,\Vert\,q)\ge 0$. [Akaike's information criterion](akaike-information-criterion.qmd) estimates the expected log score whose population version differs from this divergence by a constant. Mutual information for a joint law is this divergence between the joint distribution and the product of its marginals.{{cite:hastie_esl2009}} (§14.7, pp. 561){{cite:shannon1948}} (Thm. 2)

## Check yourself
### A zero that should be zero
Compute $D(p\,\Vert\,p)$ for $p=(0.8,0.2)$.

::: {.callout-tip collapse="true" title="Answer"}
Each ratio is $1$, and $\log 1=0$, so the divergence is $0$.{{cite:shannon1948}} (Thm. 2)
:::

### Which direction is larger?
For $p=(0.8,0.2)$ and $q=(0.5,0.5)$, which of $0.1927$ and $0.2231$ is $D(q\,\Vert\,p)$?

::: {.callout-tip collapse="true" title="Answer"}
$D(q\,\Vert\,p)\approx 0.2231$ nats. The smaller number $0.1927$ is $D(p\,\Vert\,q)$, the penalty for using a fair coin when the truth is $p$.{{cite:shannon1948}} (Thm. 2)
:::

### Bits
The forward divergence is about $0.1927$ nats. Divide the unrounded value by $\log 2$ and round to four decimals. What is the result in bits?

::: {.callout-tip collapse="true" title="Answer"}
The unrounded divergence divided by $\log 2$ equals $0.2781$ bits.{{cite:shannon1948}} (Thm. 2)
:::

## History
Shannon's 1948 paper introduces the entropy $H=-K\sum p_i\log p_i$ as the quantity fixed, up to the choice of unit $K$, by his assumptions on information, and he identifies it with the entropy of statistical mechanics. The divergence above is the gap between that entropy and the average surprise of a code built from a different distribution.{{cite:shannon1948}} (Thm. 2) Hastie, Tibshirani and Friedman use the same gap as the mutual information between coordinates, the Kullback–Leibler discrepancy from a joint density to the product of its marginals.{{cite:hastie_esl2009}} (§14.7, pp. 561)
