## Motivating example
A host reveals an empty door after a contestant has chosen one of three doors. Two closed doors remain, but the revealed information was selected using knowledge of the prize. The probabilities therefore depend on the host's rule, not just on the number of doors still closed. Conditional probability makes this dependence explicit.{{cite:grinstead_snell1997}} (§4.1, pp. 137–139)

## Intuition — An unconditional strategy and a conditional observation
Under the standard rules, the prize is uniformly placed, the contestant picks a door independently, and the host always opens an unchosen empty door and always offers a switch. Staying wins exactly when the first choice was correct, probability $1/3$. Switching wins exactly when it was wrong, probability $2/3$. This strategy argument does not require the host to choose randomly when two empty doors are available. Conditioning on a particular named door being opened does require that tie-breaking probability.{{cite:grinstead_snell1997}} (§4.1, Monty Hall example)

The distinction resembles other selection problems: observing a possible outcome does not tell us its likelihood under each hidden state until the observation mechanism is specified. Bayes' formula combines prior probability and that likelihood, then normalizes over compatible states.{{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem)

## Properties — A host with a preferred door
Fix the contestant's choice as $A$ and let $q=P(\text{host opens }B\mid\text{prize at }A)$. If the prize is at $C$, the standard host must open $B$; if it is at $B$, the host cannot open $B$. Hence
$$P(A\mid B\text{ opened})=\frac{q}{q+1},\qquad
P(C\mid B\text{ opened})=\frac1{q+1}.$$
The denominator comes from $P(B\text{ opened})=(q+1)/3$. At $q=1/2$ these are $1/3,2/3$. At $q=1$ they are $1/2,1/2$ for this observed branch. The unconditional switch success probability remains $2/3$, since the event that the first pick was wrong has not changed.{{cite:grinstead_snell1997}} (§4.1, conditional and unconditional formulations)

More generally, if prior door probabilities are $a,b,c$ summing to one, the same observation has probability $aq+c$ and the posterior chance of winning by switching to $C$ is $c/(aq+c)$ when this denominator is positive. This follows by applying the product rule to the mutually exclusive states and dividing by their total. It also shows why a nonuniform prize placement can change the answer.

## Worked example — A biased host and a forgetful host
Suppose $q=0.8$ with uniform prize placement and the host opens $B$. The posterior probabilities for prize at $A$ and $C$ are $4/9$ and $5/9$. Switching still has an advantage on this branch, but its conditional success probability is no longer $2/3$.

For a different mechanism, let the host choose an unchosen door uniformly without knowing the prize location, and observe that the host opened $B$ and it was empty. This event has likelihood $1/2$ when the prize is at either $A$ or $C$, and zero when it is at $B$. Equal priors then give posterior probabilities $1/2,1/2$. The standard host's forced safe reveal and this chance safe reveal are different experiments.{{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem, host-rule exercises)

**Your turn.** Under the standard host rule, let $q=1/4$ and observe door $B$ opened. Find the probabilities of winning by staying and switching.

::: {.callout-tip collapse="true" title="Answer"}
The posterior probabilities are $(1/4)/(1+1/4)=1/5$ for staying and $1/(1+1/4)=4/5$ for switching. Their sum is one.
:::

## Connections — More doors and the meaning of a reveal
With $N$ equally likely doors, suppose a knowledgeable host always opens $N-2$ unchosen empty doors and offers the one remaining alternative. Switching then wins with probability $(N-1)/N$, because it wins exactly when the initial choice is wrong. The result depends on the host leaving a single alternative under those rules. A host who opens fewer doors or offers switches selectively requires a fresh probability model.{{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem){{cite:grinstead_snell1997}} (§4.1, tree measures)
