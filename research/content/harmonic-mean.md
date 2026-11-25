## Lead context

Two investments can earn the same income at different rates, and the single rate that matches that income is not the ordinary average of the rates. The same reversal appears when equal sums of money buy goods at different prices: the average price per unit is the average that uses reciprocals. {{cite:dodge2008}} (p. 240)

## Motivating example

Three investments yield the same income at rates of 5%, 10%, and 15%. The arithmetic mean of the rates is $(5+10+15)/3=10\%$. The rate at which the whole capital would have to be invested to produce the same total income is the harmonic mean,

$$
H=\frac{3}{1/5+1/10+1/15}=\frac{3}{11/30}=\frac{90}{11}\approx 8.1818\%.
$$


A buyer who spends the same amount, 200 euros, on coffee at 3, 2, and 1.5 euros per kilogram buys $200/3+200/2+200/1.5$ kilograms. The average price per kilogram is total cost divided by total quantity, which is the harmonic mean of the three prices and equals 2, not the arithmetic mean of the prices. {{cite:dodge2008}} (p. 240)

## Definition

For positive numbers $x_1,\ldots,x_n$, the harmonic mean is

$$
H=\frac{n}{\sum_{i=1}^n 1/x_i}.
$$


For positive numbers the ordering is: the harmonic mean sits between the smallest and the largest observation, and it does not exceed the geometric mean, which does not exceed the arithmetic mean. A zero observation makes a reciprocal undefined, so the harmonic mean is undefined as soon as any observation is zero. {{cite:dodge2008}} (pp. 239–240)

For two positive numbers $a$ and $b$,

$$
H=\frac{2ab}{a+b}.
$$


The gap between the arithmetic mean and this value is

$$
\frac{a+b}{2}-\frac{2ab}{a+b}=\frac{(a-b)^2}{2(a+b)}.
$$


The numerator is a square and the denominator is positive, so the difference is nonnegative and is zero only when $a=b$.

## Interpretation

The harmonic mean asks how many units a fixed outlay buys, then divides the outlay by that quantity. A low price buys many units, so it pulls the average harder than a high price of the same outlay. A very small observation has a very large reciprocal and can move the result sharply. A very large observation has a small reciprocal and moves it much less. The arithmetic mean is pulled the other way. NIST’s account of location makes the same contrast for tails: extreme values distort the mean, which is why a heavy-tailed sample can have a mean far from the bulk of the data. The harmonic mean is the reciprocal version of that sensitivity. It is largely insensitive to observations that are much larger than the rest, and much more sensitive to observations that are much smaller. {{cite:dodge2008}} (p. 240) {{cite:nist_location2002}} (§1.3.5.1, “Cauchy Distribution”)

For the six positive numbers 1, 2, 3, 4, 5, and 100 the harmonic mean is about 2.62 and the arithmetic mean is about 19.17. For 1, 6, 6, 6, 6, and 6 the harmonic mean is $36/11\approx 3.27$ and the arithmetic mean is $31/6\approx 5.17$. The single small value moves the harmonic mean. The single large value moves the arithmetic mean. {{cite:dodge2008}} (p. 240)

Replacing the harmonic mean by the arithmetic mean answers a different question. In the investment example, 10% is not the rate at which the pooled capital earns the same income as the three separate investments. In the coffee example, the arithmetic mean of the prices is not the price per kilogram of the basket that was actually bought.

## Worked example

The interest rates 5, 10, and 15 give

$$
H=\frac{90}{11}\approx 8.1818,
$$


against an arithmetic mean of 10. Person weights 100, 200, and 300 have reciprocals $1/100$, $1/200$, and $1/300$, which sum to $11/600$. The harmonic mean is

$$
\frac{3}{11/600}=\frac{1800}{11}\approx 163.636,
$$


which rounds to 164. {{cite:dodge2008}} (p. 240)

**Your turn.** One of six positive observations is replaced by zero. What happens to the harmonic mean?

::: {.callout-tip collapse="true" title="Answer"}
The harmonic mean is undefined, because a reciprocal of zero is not a number.
:::

## Connections

The arithmetic mean is the sum divided by the count. The geometric mean is the exponential of the average log, and for positive numbers it lies between the harmonic mean and the arithmetic mean. A [median](median.qmd) resists large and small outliers by using rank rather than reciprocals. The harmonic mean is the right average when the scientific quantity is a ratio of a fixed total to a sum of reciprocals: investments producing equal income at different rates, or equal expenditure at different prices. It is the wrong average when the scientific quantity is the ordinary total of the observations. {{cite:dodge2008}} (pp. 239–240) {{cite:nist_location2002}} (§1.3.5.1)

## History

Dodge points the history of the relation among the harmonic, geometric, and arithmetic means to Mitrinović’s account of the inequalities, and the history of the harmonic mean itself back to the geometric mean. The statistical use is narrower than the algebraic identity. The mean is rarely the default summary. It becomes the right summary in the two situations the encyclopedia isolates: equal income from different interest rates, and equal expenditure at different prices per unit. The ordering $H\le G\le \bar x$ for positive numbers is the property that keeps it from being interchangeable with the other two. {{cite:dodge2008}} (pp. 239–240)
