## Motivating example

Two fair coins have four equally probable ordered outcomes, yet the number of heads has only three possible values. Counting those three values as equally probable would give the wrong model. Equal likelihood belongs to a specified sample space with specified probabilities; it need not survive a many-to-one recording rule.{{cite:grinstead_snell1997}} (§1.2, pp.25–26, Def.1.3)

## Statement

For a finite sample space $\Omega$ with $N\ge1$ equally probable elementary outcomes, $P(A)=|A|/N$. Conditional on a nonempty event $B$, every outcome in $B$ still has probability $1/|B|$, hence
$$P(A\mid B)=\frac{|A\cap B|}{|B|}.$$
The word elementary matters: an event that collects several elementary outcomes receives the sum of their probabilities.{{cite:grinstead_snell1997}} (§1.2, pp.25–26)

## Proof

Every singleton has a common probability $p$. Finite additivity and $P(\Omega)=1$ give $Np=1$, so $p=1/N$. The disjoint union of the singletons in $A$ gives $P(A)=|A|/N$. Dividing $P(A\cap B)$ by $P(B)>0$ gives the conditional counting formula.{{cite:grinstead_snell1997}} (§1.2, pp.25–26)

## Intuition — Probability follows the elementary outcomes

Recording the number of heads in two independent fair tosses maps $TT$ to zero, $HT$ and $TH$ to one, and $HH$ to two. Their probabilities are therefore $(1/4,1/2,1/4)$. A sample space lists possible observations; a probability measure also specifies their weights. Symmetry can justify equal weights, but merely lacking information about the weights does not establish physical symmetry.{{cite:grinstead_snell1997}} (§1.2, pp.26–27)

## Worked example

Roll two independent fair dice and condition on at least one die showing six. There are eleven eligible ordered pairs: six with first die six, six with second die six, minus the double-counted pair $(6,6)$. Exactly two, $(1,6)$ and $(6,1)$, have sum seven, giving conditional probability $2/11$. Without that conditioning the probability is $6/36=1/6$. The denominator changes with the information supplied.{{cite:grinstead_snell1997}} (§1.2, p.26, Ex.1.11)

**Your turn.** Three independent fair tosses produce a count of heads. Are the four possible counts equally likely?

::: {.callout-tip collapse="true" title="Answer"}
No. The eight ordered sequences have probability $1/8$ each. The counts zero, one, two and three have respectively one, three, three and one preimages, giving probabilities $(1,3,3,1)/8$.
:::

## Statistical use — Birthdays and the choice of model

In a model with independent birthdays uniformly distributed over $365$ days, the chance of a collision among $n\le365$ people is
$$1-\prod_{j=0}^{n-1}\left(1-\frac j{365}\right).$$
The complementary product counts sequentially distinct birthdays. It gives approximately $0.50730$ at $n=23$, $0.89123$ at forty, and $0.97037$ at fifty. At twenty-three people there are $\binom{23}{2}=253$ pairs, but their collision events are dependent, so multiplying a single-pair probability by that count is not an exact calculation. The numerical answer depends on the uniform and independent birthday assumptions.{{cite:grinstead_snell1997}} (§3.1, pp.77–79, Ex.3.3)

## Related concepts

A random variable groups elementary outcomes by their recorded value. Its mass at a value is the sum over that value's preimage. The same principle underlies the dice-sum distribution and distinguishes a uniform distribution on sequences from a nonuniform distribution on counts.{{cite:siegrist2022_events}} (§2.2, “Random Variables”)
