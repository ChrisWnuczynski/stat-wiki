## Lead context
A joint mass function describes combinations of values; its margins describe one coordinate at a time.

## Motivating example
A retailer records whether an order contains an urgent item and whether it arrives late. Knowing each percentage separately does not determine how often urgency and lateness occur together. A joint table stores that overlap and supplies the probabilities needed to ask whether the variables are independent. Multivariate discrete distributions assign mass to whole tuples of values.{{cite:dodge2008}} (p. 275)

## Definition — Probability on a grid
For discrete variables $X$ and $Y$, write $p(x,y)=P(X=x,Y=y)$. A valid joint mass function is nonnegative everywhere and satisfies $\sum_x\sum_y p(x,y)=1$. Values outside its support have mass zero. The coordinates can have different sets of possible values; the table need not be square.{{cite:dodge2008}} (p. 275)

For any set $A$ of pairs, $P((X,Y)\in A)=\sum_{(x,y)\in A}p(x,y)$. The marginal mass $p_X(x)=\sum_y p(x,y)$ adds all pairs with first coordinate $x$; $p_Y(y)$ adds down the other direction. Thus marginalisation discards information about which coordinate values occur together.{{cite:grinstead_snell1997}} (§4.1, joint distributions, pp. 142–144)

## Properties — Conditioning and independence
When $p_Y(y)>0$, the conditional mass is $p_{X\mid Y}(x\mid y)=p(x,y)/p_Y(y)$. The denominator normalises the column corresponding to the observed value of $Y$. Conditioning on a zero-probability value is not defined by this ratio. Independence requires $p(x,y)=p_X(x)p_Y(y)$ for every pair, rather than just a few selected cells.{{cite:grinstead_snell1997}} (§4.1, pp. 134–135, 140–144)

Expectations of functions use the joint table directly:
$$
E\{g(X,Y)\}=\sum_x\sum_y g(x,y)p(x,y),
$$
provided the expectation exists. For finite support this is a finite weighted sum. It gives $E(XY)$ and hence $\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y)$. Zero covariance alone is a weaker restriction than factorisation of all joint masses.{{cite:grinstead_snell1997}} (§§6.1–6.2)

## Worked example
Let $X$ and $Y$ be indicators with table

| $x\backslash y$ | 0 | 1 | Row total |
|--:|--:|--:|--:|
| 0 | 0.1 | 0.2 | 0.3 |
| 1 | 0.3 | 0.4 | 0.7 |
| Column total | 0.4 | 0.6 | 1 |

Then $P(X=1)=0.7$, $P(Y=1)=0.6$, and $P(X=1,Y=1)=0.4$. Independence would require the last number to be $0.7(0.6)=0.42$, so the variables are dependent. Their covariance is $0.4-0.42=-0.02$. Conditioning on $Y=0$ gives $P(X=1\mid Y=0)=0.3/0.4=3/4$, while conditioning on $Y=1$ gives $0.4/0.6=2/3$.{{cite:grinstead_snell1997}} (§4.1, conditional and joint distributions)

The probability that at least one indicator is one is $0.2+0.3+0.4=0.9$. This is also $1-p(0,0)$ and agrees with the union formula $0.7+0.6-0.4=0.9$. Both calculations use the same joint information. Marginal probabilities alone would leave the overlap unknown.{{cite:grinstead_snell1997}} (§4.1)

**Your turn.** Find $P(X=Y)$ and $P(X=0\mid X=Y)$.

::: {.callout-tip collapse="true" title="Answer"}
The equality event consists of $(0,0)$ and $(1,1)$ and has probability $0.1+0.4=0.5$. Its part with $X=0$ has probability $0.1$, so the conditional probability is $0.1/0.5=0.2$.
:::

## Interpretation — A support constraint can expose dependence
If a joint cell is zero but both corresponding marginal masses are positive, independence fails immediately. The pair cannot occur even though each coordinate value occurs separately. For example, let $X$ take $-1,0,1$ with probabilities $1/4,1/2,1/4$ and set $Y=X^2$. Symmetry gives $E(X)=E(XY)=0$, so covariance is zero, yet $Y$ is determined by $X$. Their joint support, rather than covariance, displays that dependence.{{cite:grinstead_snell1997}} (§4.1, independence; §6.2, covariance)
