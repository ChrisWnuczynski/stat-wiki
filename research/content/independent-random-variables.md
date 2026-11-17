## Lead context
Independent random variables carry no information about one another: the probability of any combination is the product of the separate probabilities.

## Motivating example
Two rolls of one fair die are independent. The face on the first roll does not change the chance of a six on the second, and the probability of two sixes is $(1/6)\times(1/6)$. A different experiment looks similar and is not independent. A die is drawn at random from a box that contains a biased die, and then rolled twice. The first roll says something about which die was drawn, so it changes the probability of the second roll.

## Intuition — The joint distribution factors
Independence is a property of the joint distribution, not of the two marginals. Discrete random variables $X$ and $Y$ are independent when $\Pr(X=x,Y=y)=\Pr(X=x)\Pr(Y=y)$ at every pair $(x,y)$. Knowing $Y=y$ then leaves the conditional distribution of $X$ equal to its marginal. Continuous variables with a joint density are independent when that density is the product of the marginal densities. An infinite sequence is independent when every finite subcollection is.{{cite:pishro_nik2014}} (§5.1, independent random variables)

## Definition — Product formula and the product of expectations
Discrete $X_1,\ldots,X_n$ are independent when, for every point,
$$
\Pr(X_1=x_1,\ldots,X_n=x_n)=\prod_{k=1}^n \Pr(X_k=x_k).
$$
If $X$ and $Y$ are independent and the expectations exist, then $\E[XY]=\E[X]\E[Y]$. The converse is false: uncorrelated variables need not be independent.{{cite:pishro_nik2014}} (§5.1, independent random variables)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For independent discrete variables with finite support,
$$
\E[XY]=\sum_{x,y} xy\,\Pr(X=x,Y=y)=\sum_{x,y} xy\,\Pr(X=x)\Pr(Y=y).
$$
The double sum separates into $\bigl(\sum_x x\Pr(X=x)\bigr)\bigl(\sum_y y\Pr(Y=y)\bigr)$.{{cite:pishro_nik2014}} (§5.1, independent random variables)
:::
:::

## Worked example
Let $X$ and $Y$ be independent Bernoulli variables with $\Pr(X=1)=0.4$ and $\Pr(Y=1)=0.5$. Then $\E[X]=0.4$, $\E[Y]=0.5$ and $\E[XY]=\Pr(X=Y=1)=0.4\times 0.5=0.2$, which equals the product of the means. A different joint distribution on $\{0,1\}^2$,
$$
\begin{align*}
\Pr(0,0)&=0.2,&\Pr(0,1)&=0.3,\\
\Pr(1,0)&=0.1,&\Pr(1,1)&=0.4,
\end{align*}
$$
has $\E[X]=0.5$, $\E[Y]=0.7$ and $\E[XY]=0.4$. The product of the means is $0.35$, not $0.4$, so $X$ and $Y$ are not independent. The marginals alone cannot show this. The joint probability $\Pr(X=1,Y=1)=0.4$ disagrees with $0.5\times 0.7=0.35$.

**Your turn.** In the independent Bernoulli pair, find $\Pr(X=0,Y=1)$.

::: {.callout-tip collapse="true" title="Answer"}
$\Pr(X=0)=0.6$ and $\Pr(Y=1)=0.5$, so the joint probability is $0.6\times 0.5=0.3$.
:::

## Connections — Events, conditional independence, and sums
[Independent events](independent-events.qmd) are the same product rule for sets. [Conditional independence](conditional-independence.qmd) is the product rule inside a conditional distribution: variables can be dependent on the margin and independent given a third variable. Independence is what lets a [convolution](convolution.qmd) use the product of the marginals, and what lets the variance of a sum equal the sum of the variances.

