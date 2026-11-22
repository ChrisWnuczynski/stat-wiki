## Lead context
It gives a common scale for comparing uncertain payoffs and is the starting point for variance and many estimators. An expected value need not be a value that can actually occur.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)

## Motivating example
An outdoor event costs an extra 100 dollars if it rains, and rain has probability 0.3. Across many events with the same conditions, the average extra cost would be 30 dollars per event, although any single event costs either zero or 100 dollars extra. That planning value is an expectation, not a forecast of the next bill.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)

## Intuition
Think of each possible outcome as carrying a weight equal to its probability. An outcome with twice the probability contributes twice as much to the weighted average. For a fair six-sided die the expectation is 3.5, even though no throw can show 3.5; the number describes the centre of the distribution rather than its most likely face.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)

## Definition
Here $X$ is a random variable, $x$ ranges over its possible realised values, and $f(x)$ is its probability mass or density at $x$, as appropriate. The sum or integral must converge absolutely for a finite expectation. A distribution can also mix point masses and continuous parts; in that case the common definition is $\mathbb{E}X=\int x\,\mathrm{d}F_X(x)$, where $F_X$ is the distribution of $X$. A function $g(X)$ likewise has an expectation when $\mathbb{E}|g(X)|<\infty$.{{cite:grinstead_snell1997}} (Ch. 6, §6.1) {{cite:durrett2019}} (§4.1.2, Thm. 4.1.13)

## Properties
### Linearity and indicators

For integrable random variables $X$ and $Y$ and constants $a,b$, $\mathbb{E}(aX+bY)=a\mathbb{E}X+b\mathbb{E}Y$, whether or not $X$ and $Y$ are independent. This lets a total's expected value be computed from its parts even when those parts are dependent. For an event $A$, its indicator $\mathbf1_A$ equals one when $A$ occurs and zero otherwise, so $\mathbb{E}\mathbf1_A=\mathbb{P}(A)$; counting occurrences is therefore an application of linearity.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)

The [expectation-of-a-function](expectation-of-a-function.qmd) formula above evaluates $g(X)$ without first finding the entire distribution of $g(X)$. The [tower property](tower-property.qmd) says that averaging a conditional mean over the conditioning variable restores the overall mean; averaging in stages through nested information sets gives the same result.{{cite:durrett2019}} (§4.1.2, Thm. 4.1.13)

Proof idea: expectation is an integral, so linearity follows from linearity of integration. The function rule is integration against the image distribution, while the tower rule follows from the defining integral identity of conditional expectation.{{cite:durrett2019}} (§4.1.2, Thm. 4.1.13)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For integrable $X,Y$, linearity of the integral gives $\int(aX+bY)\,\mathrm{d}\mathbb{P}=a\int X\,\mathrm{d}\mathbb{P}+b\int Y\,\mathrm{d}\mathbb{P}$; no independence is used. The integral of $\mathbf1_A$ is $\mathbb{P}(A)$. The discrete proof of the function rule, by grouping equal values of $g$, appears above. For a continuous $X$ with density $f$, the image-distribution integration rule gives $\int g(X)\,\mathrm{d}\mathbb{P}=\int g(x)f(x)\,\mathrm{d}x$; it holds first for indicators and simple functions, then for nonnegative functions by monotone convergence, and for integrable functions by splitting positive and negative parts. For the tower rule, put $\mathcal F=\sigma(X)$ and $\mathcal G=\sigma(X,Z)$, so $\mathcal F\subseteq\mathcal G$. For every $A\in\mathcal F$, the definition of conditional expectation gives $\int_A\mathbb{E}(Y\mid\mathcal G)\,\mathrm{d}\mathbb{P}=\int_A Y\,\mathrm{d}\mathbb{P}$. By the uniqueness of conditional expectation, $\mathbb{E}[\mathbb{E}(Y\mid\mathcal G)\mid\mathcal F]=\mathbb{E}(Y\mid\mathcal F)$ almost surely, proving the displayed nested version. Taking the coarser information set to be the trivial sigma-field gives $\mathbb{E}[\mathbb{E}(Y\mid X)]=\mathbb{E}Y$.{{cite:durrett2019}} (§4.1.2, Thm. 4.1.13) {{cite:grinstead_snell1997}} (Ch. 6, §6.1)
:::
:::

## Statistical use
Suppose $X_1,\ldots,X_n$ measure the same population quantity and each has mean $\mu$. Their sample average $\overline X=(X_1+\cdots+X_n)/n$ has expectation $\mu$ by linearity, even if observations are dependent. Dependence affects its variance, so this calculation alone says nothing about how precise the average is. In decision problems, expected cost or reward puts uncertain options on the same long-run scale, while the distribution and its spread still matter to a risk-sensitive decision.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)

## Worked example
A fair die game costs 2 dollars to enter and pays 8 dollars only when a six is thrown. Let $X$ be the player's net gain. It is $6$ with probability $1/6$ and $-2$ with probability $5/6$, so $\mathbb{E}X=6(1/6)-2(5/6)=-2/3$ dollar per play. The player can win 6 dollars on a particular throw, but under repeated fair play the average gain tends toward a loss of about 67 cents per round.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)

**Your turn.** A new game costs 1.50 dollars and pays 6 dollars if a fair die shows five or six. What is the expected net gain per play?

::: {.callout-tip collapse="true" title="Answer"}
The net gain is $4.50$ with probability $1/3$ and $-1.50$ with probability $2/3$. Thus $\mathbb{E}X=4.50(1/3)-1.50(2/3)=0.50$ dollar.
:::

Two fair dice are thrown until both faces are six; the expected number of throws is the mean of that geometric wait. For the spike $X_n=n\mathbf1_{\{U\leq1/n\}}$ with $U$ uniform on $(0,1)$, the probability $\mathrm{P}(X_n>\varepsilon)$, the expectation $\mathbb{E}X_n$, and the second moment $\mathbb{E}X_n^2$ decide which modes of convergence to $0$ hold.

::: {.callout-tip collapse="true" title="Answers"}
The chance of double six on each independent throw is $1/36$, so the geometric waiting time has expectation $36$ throws. For the spike $X_n=n\mathbf1_{\{U\leq1/n\}}$ with uniform $U$, $\mathbb{E}X_n=n(1/n)=1$ although $X_n$ converges to zero in probability and almost surely; moreover $\mathbb{E}X_n^2=n$. Thus neither $L^1$ nor $L^2$ convergence holds.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)
:::

**Your turn.** A fair coin pays 3 dollars on heads and 1 dollar on tails. What is the expected payment?

::: {.callout-tip collapse="true" title="Answer"}
Each face has probability $1/2$, so the expectation is $(3+1)/2=2$ dollars.
:::

**Your turn.** An event has probability 0.4. What is the expectation of its indicator?

::: {.callout-tip collapse="true" title="Answer"}
The indicator equals 1 when the event occurs and 0 otherwise, so its expectation equals the probability, 0.4.
:::

**Your turn.** Suppose $\mathbb{E}X=2$ and $\mathbb{E}Y=5$. What is $\mathbb{E}(3X-Y)$?

::: {.callout-tip collapse="true" title="Answer"}
Linearity gives $3\times 2-5=1$. The calculation does not require $X$ and $Y$ to be independent.
:::

## Common misconceptions
Expectation need not be an attainable outcome: the fair die's mean is 3.5, while every observed face is an integer. It is also distinct from the median or the most probable value, which answer different questions about the distribution. Linearity does not require independence; for example, $X$ and $-X$ are completely dependent but their sum and its expectation are zero when $X$ is integrable.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)

## Assumptions and limits
Some random variables have no finite expectation. In the St Petersburg game, a fair coin is tossed until its first head; if that happens on toss $n$, the payoff is $2^n$ with probability $2^{-n}$. Each possible $n$ contributes one to the expectation, so the infinite sum diverges. A finite observed average from such a game is still an average of the observations, but it is not estimating a finite population expectation. When positive and negative tails are both nonintegrable, subtracting their divergent contributions does not define a valid expectation.{{cite:grinstead_snell1997}} (Ch. 6, §6.1)

## Connections
[Variance](variance.qmd) averages squared deviations from the expectation, so it describes spread around the centre defined here. [Conditional expectation](conditional-expectation.qmd) recalculates that average given information; its [tower property](tower-property.qmd) explains why averaging conditional means recovers the original expectation. A [sample mean](summary-statistics.qmd) averages realised data, while expectation averages over a probability distribution; repeated sampling connects the two under suitable conditions.{{cite:grinstead_snell1997}} (Ch. 6, §6.1) {{cite:durrett2019}} (§4.1.2, Thm. 4.1.13)

## History
In his 1657 treatise on games of chance, Christiaan Huygens asked what a chance in an unfinished game was fairly worth. His first propositions valued equal chances by averaging possible winnings and unequal numbers of chances by weighting those winnings. The practical problem was the fair division of a stake, rather than a formal measure-theoretic definition.{{cite:huygens1657}} (Props. I–III)
