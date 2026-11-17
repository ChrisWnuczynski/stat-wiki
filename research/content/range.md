## Motivating example
A workshop measures the lengths of five parts and wants to know the largest observed mismatch. The measurements $4,8,9,11,13$ have range $9$. This is a useful answer for fitting the longest part into a space designed for the shortest. It is a less complete answer to how tightly most parts cluster: moving the middle three measurements changes their pattern without changing the range. The distinction between central spread and tail spread is essential when choosing a summary.{{cite:nist_handbook2002}} (§1.3.5.6, “Measures of Scale”)

## Definition
For a nonempty finite sample, write its order statistics as $x_{(1)}\le\cdots\le x_{(n)}$. Its range is
$$R_n=x_{(n)}-x_{(1)}.$$
The statistic is nonnegative and has the same measurement units as the observations. It is zero exactly when every observation is equal. For a one-observation sample the range is zero even though a population from which the observation was drawn may be very variable. These statements concern an observed sample, rather than the entire support of its population.{{cite:dodge2008}} (p. 448, “Range”)

A reported pair of endpoints and a reported range contain different information. Endpoints $4$ and $13$ locate the interval; the number $9$ gives only its width. Adding a constant to every measurement moves both endpoints together and leaves that width alone. Multiplying by a negative number reverses their order, so the general rule is $R(a+bx)=|b|R(x)$.{{cite:nist_handbook2002}} (§1.3.5.6, range definition)

## Properties — What adding an observation can do
Appending a value $z$ gives the exact recursion
$$R_{n+1}=\max\{x_{(n)},z\}-\min\{x_{(1)},z\}.$$
If $z$ lies between the endpoints, neither endpoint changes. If it lies above them, the increase is $z-x_{(n)}$; if below, the increase is $x_{(1)}-z$. Consequently a growing sample has a nondecreasing range. Comparing ranges of samples of very different sizes mixes population variation with the opportunity to observe a more extreme value.

The recursion also proves why a range is sensitive to contamination. For $n\ge2$, holding all but one observation fixed and sending that observation to arbitrarily large values sends the range to infinity. A single replacement is enough; the replacement fraction is $1/n$. The interquartile range describes central ranks instead, although its numerical robustness also depends on sample size and the quartile convention.{{cite:nist_handbook2002}} (§1.3.5.6, range, interquartile range and robustness)

The range alone cannot distinguish a central pile from a divided sample. The samples $0,0,0,10,10$ and $0,4,5,6,10$ both have range $10$. The first has a gap between two piles; the second has three observations near its centre. A plot can reveal this difference immediately. Treating the range as a description of all variation would discard that information.{{cite:dodge2008}} (p. 448, “Domains and limitations”)

## Worked example — Two batches with the same span
Consider batch A, $2,4,6,8,10$, and batch B, $2,2,6,10,10$. Both have mean and median $6$, and both have range $8$. Their sums of squared deviations from the mean are $40$ and $64$, so their sample variances are $10$ and $16$. Their standard deviations are approximately $3.162$ and $4$. Equal ranges do not imply equal standard deviations because squared deviations use the interior observations as well as the endpoints.{{cite:nist_handbook2002}} (§1.3.5.6, variance versus range)

Under the interpolated quartile positions $1+(n-1)p$, batch A has quartiles $4$ and $8$, hence interquartile range $4$. Batch B has quartiles $2$ and $10$, hence interquartile range $8$. In these small samples the central half is already close to the endpoints, which makes reporting the data themselves particularly useful.

**Your turn.** Start with $3,5,8,12$. Append $7$, then append $20$. Find the range after each addition. What happens to all three ranges if every measurement is converted by $y=100-2x$?

::: {.callout-tip collapse="true" title="Answer"}
The starting range is $12-3=9$. Appending $7$ leaves it at $9$. Appending $20$ changes it to $20-3=17$. The transformation multiplies every range by $|-2|=2$, giving $18,18,34$. The constant $100$ changes location but makes no contribution to spread.
:::

## Assumptions and limits
Calculating a range requires an ordered numerical scale. Coding categories with integers does not create meaningful distances between them. Rounding can conceal a small span, and a detection limit can conceal an endpoint. For grouped observations, subtracting the centres of the first and last occupied classes approximates a range; it need not equal the largest raw value minus the smallest. A description should distinguish those quantities.{{cite:dodge2008}} (p. 448, grouped observations)

For comparing variation, accompany the range with the sample size and at least one description of the interior, such as quartiles or a histogram. A large range can be scientifically important even when caused by a single observation. Investigating that observation means checking its measurement and context; its extremeness alone does not establish that it is erroneous.
