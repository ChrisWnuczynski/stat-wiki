## Motivating example — A lottery ticket and a password are different objects
Choosing several labels requires deciding whether their order is recorded and whether a label may be repeated. A password usually records order and permits repetition. A committee records membership and does not repeat a person. The same population size and number of selections can therefore produce very different outcome counts. Counting starts by describing the recorded outcome, rather than choosing a formula from its appearance.{{cite:dodge2008}} (p. 98, Combination; p. 421, Permutation)

## Statement
Take $n\ge1$ distinct labels and $k\ge0$ selections. Ordered draws with repetition have $n^k$ outcomes. Ordered draws without repetition have $n(n-1)\cdots(n-k+1)$ outcomes when $k\le n$, and none when $k>n$. Unordered draws without repetition have $\binom nk$ outcomes. Unordered draws with repetition are **multisets**, described by nonnegative counts summing to $k$, and have $\binom{n+k-1}{k}$ outcomes. Sets cannot represent repeated membership; multisets can. The count for an empty selection is one in all admissible cases.{{cite:grinstead_snell1997}} (§§3.1–3.2)

## Proof
With order and repetition, each of the $k$ positions has $n$ choices, so multiplication gives $n^k$. Without repetition, successive positions have $n,n-1,\ldots,n-k+1$ choices. If order is then forgotten while all labels are distinct, each set corresponds to exactly $k!$ ordered outcomes, yielding $n!/[k!(n-k)!]$. This division by a common multiplicity is valid because every such set has the same number of orderings.{{cite:grinstead_snell1997}} (§3.1, permutations; §3.2, combinations)

For multisets, write the count vector $(c_1,\ldots,c_n)$ with $\sum c_i=k$. Place $k$ stars and $n-1$ separators in a row. The stars before the first separator count label one, the next group counts label two, and so on. Choosing separator positions among $n+k-1$ positions gives $\binom{n+k-1}{n-1}=\binom{n+k-1}{k}$. Empty groups are allowed and represent zero counts.{{cite:grinstead_snell1997}} (§3.2, counting selections with repetition)

## Key results — Counting does not imply equal probabilities
Uniform independent draws generate equally likely ordered sequences, but their unordered multisets need not be equally likely. A count vector $c$ corresponds to $k!/\prod_i c_i!$ sequences. Repetitions change that multiplicity, so the induced multiset probabilities differ. A probability calculation by favourable counts divided by total counts is justified only after checking that the counted outcomes are equiprobable.{{cite:grinstead_snell1997}} (§3.2, multinomial coefficients)

## Worked example — Two draws from three labels
For labels $A,B,C$ and $k=2$, the four counts are $9$, $6$, $3$ and $6$ in the order listed above. The six multisets are $AA,AB,AC,BB,BC,CC$. Under independent uniform ordered sampling, $AA$ has probability $1/9$, whereas $AB$ has probability $2/9$ because it can arise from $AB$ or $BA$. Uniformly choosing one of the six multisets is a different sampling experiment.{{cite:dodge2008}} (p. 98, combinations; p. 421, permutations)

**Your turn.** How many unordered selections of three labels with repetition are possible from four labels?

::: {.callout-tip collapse="true" title="Answer"}
There are $\binom{4+3-1}{3}=\binom63=20$ multisets.
:::

## Common misconceptions — Do not divide by a varying multiplicity
The shortcut of dividing an ordered count by $k!$ works for unordered selections without repetition because every selected label is distinct. With repetition, the ordered sequences corresponding to a multiset have different multiplicities: $AA$ has only one ordering while $AB$ has two. The stars-and-separators argument counts multisets directly and avoids that mistaken division. When sampling mechanisms are unequal, the correct next step is to add their probability weights.{{cite:grinstead_snell1997}} (§3.2)


## Statistical use — Match the probability denominator to the experiment
Before using a counting formula in a probability calculation, state which elementary outcomes are equally likely. Independent uniform draws make ordered sequences equally likely, but collapsing them into unordered multisets produces different multiplicities. Sampling a uniform subset without replacement instead makes subsets the natural elementary outcomes. The combinatorial count is therefore part of the probability model: choosing the right number of possible descriptions alone does not establish equal probability for those descriptions.{{cite:grinstead_snell1997}} (§§3.1–3.2, counting and sampling)
