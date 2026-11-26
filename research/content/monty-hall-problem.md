## Motivating example
A host reveals an empty door after a contestant has chosen one of three doors. Two closed doors remain, but the revealed information was selected using knowledge of the prize. The probabilities therefore depend on the host's rule, not just on the number of doors still closed. Conditional probability makes this dependence explicit.{{cite:grinstead_snell1997}} (§4.1, pp. 137–139)

## Intuition — An unconditional strategy and a conditional observation
Under the standard rules, the prize is uniformly placed, the contestant picks a door independently, and the host always opens an unchosen empty door and always offers a switch. Staying wins exactly when the first choice was correct, probability $1/3$. Switching wins exactly when it was wrong, probability $2/3$. This strategy argument does not require the host to choose randomly when two empty doors are available. Conditioning on a particular named door being opened does require that tie-breaking probability.{{cite:grinstead_snell1997}} (§4.1, Monty Hall example)

The distinction resembles other selection problems: observing a possible outcome does not tell us its likelihood under each hidden state until the observation mechanism is specified. Bayes' formula combines prior probability and that likelihood, then normalizes over compatible states.{{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem)

## Properties — A host with a preferred door
Fix the contestant's choice as $A$ and let $q=\mathbb{P}(\text{host opens }B\mid\text{prize at }A)$. If the prize is at $C$, the standard host must open $B$; if it is at $B$, the host cannot open $B$. Hence
$$\mathbb{P}(A\mid B\text{ opened})=\frac{q}{q+1},\qquad
\mathbb{P}(C\mid B\text{ opened})=\frac1{q+1}.$$
The denominator comes from $\mathbb{P}(B\text{ opened})=(q+1)/3$. At $q=1/2$ these are $1/3,2/3$. At $q=1$ they are $1/2,1/2$ for this observed branch. The unconditional switch success probability remains $2/3$, since the event that the first pick was wrong has not changed.{{cite:grinstead_snell1997}} (§4.1, conditional and unconditional formulations)

More generally, if prior door probabilities are $a,b,c$ summing to one, the same observation has probability $aq+c$ and the posterior chance of winning by switching to $C$ is $c/(aq+c)$ when this denominator is positive. This follows by applying the product rule to the mutually exclusive states and dividing by their total. It also shows why a nonuniform prize placement can change the answer.

## Worked example — A biased host and a forgetful host
Suppose $q=0.8$ with uniform prize placement and the host opens $B$. The posterior probabilities for prize at $A$ and $C$ are $4/9$ and $5/9$. Switching still has an advantage on this branch, but its conditional success probability is no longer $2/3$.

For a different mechanism, let the host choose an unchosen door uniformly without knowing the prize location, and observe that the host opened $B$ and it was empty. This event has likelihood $1/2$ when the prize is at either $A$ or $C$, and zero when it is at $B$. Equal priors then give posterior probabilities $1/2,1/2$. The standard host's forced safe reveal and this chance safe reveal are different experiments.{{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem, host-rule exercises)

**Your turn.** Under the standard host rule, let $q=1/4$ and observe door $B$ opened. Find the probabilities of winning by staying and switching.

::: {.callout-tip collapse="true" title="Answer"}
The posterior probabilities are $(1/4)/(1+1/4)=1/5$ for staying and $1/(1+1/4)=4/5$ for switching. Their sum is one.
:::

## Connections — More doors and the meaning of a reveal
With $N$ equally likely doors, suppose a knowledgeable host always opens $N-2$ unchosen empty doors and offers the one remaining alternative. Switching then wins with probability $(N-1)/N$, because it wins exactly when the initial choice is wrong. For ten doors that probability is $9/10$. The result depends on the host leaving a single alternative under those rules. A host who opens fewer doors or offers switches selectively requires a fresh probability model.{{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem){{cite:grinstead_snell1997}} (§4.1, tree measures)

## Assumptions and limits — The likelihood of the opened door
Fix the contestant's first choice as door $A$. Let the prize be uniformly placed, and let $q$ be the probability that a knowledgeable host opens $B$ when the prize is behind $A$ and both $B$ and $C$ are available. If the prize is behind $C$, the host must open $B$. If the prize is behind $B$, the host cannot open $B$. The law of total probability therefore gives
$$\mathbb{P}(\text{host opens }B)=\frac13 q+\frac13\cdot 0+\frac13\cdot 1=\frac{q+1}3.$$
Bayes' formula then divides the joint probabilities by this margin. The posterior probability that the prize is behind $A$ is $q/(q+1)$, and the posterior probability that it is behind $C$ is $1/(q+1)$. At $q=1/2$ these are $1/3$ and $2/3$. At $q=1$, the host opens $B$ whenever the prize is behind $A$, and the two closed doors that remain after $B$ is opened are equally likely: both posteriors equal $1/2$. The unconditional always-switch strategy still wins with probability $2/3$, because it wins on the event that the first pick was wrong, an event of probability $2/3$ that does not depend on which door the host preferred.{{cite:grinstead_snell1997}} (§4.1, conditional and unconditional formulations)

The same arithmetic accepts unequal prize probabilities $a,b,c$. The probability of the observed open door is $aq+c$, and the posterior probability of winning by switching to $C$ is $c/(aq+c)$ when the denominator is positive. A prize that is more often behind $C$ raises the value of switching. A prize that is more often behind the contestant's first choice lowers it. The three-door puzzle with $a=b=c=1/3$ is one point in that family.{{cite:grinstead_snell1997}} (§4.1, pp. 137–139)

## Common misconceptions
Two closed doors do not by themselves have equal probability. The host's rule is what assigns the likelihood of the observation under each prize location. A host who opens an unchosen door uniformly, without knowing where the prize is, and who happens to reveal an empty door, gives likelihood $1/2$ to the prize being behind either remaining closed door and likelihood $0$ to the prize being behind the opened door. Equal priors then leave posterior probabilities $1/2$ and $1/2$. The standard host is forced to open an empty door. The forgetful host sometimes opens the prize and, on the occasions when the opened door is empty, has not concentrated probability on the remaining alternative in the same way. The two experiments can share the sentence "an empty door was opened."{{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem, host-rule exercises)

The strategy probability and the conditional probability answer different questions. Always switching, before anyone names the opened door, wins on two of the three prize locations. Conditioning on the host having opened a particular door $B$ uses $q$. At $q=1/4$ the conditional probabilities are $1/5$ for staying and $4/5$ for switching. At $q=0.8$ they are $4/9$ and $5/9$. Someone who quotes $2/3$ after seeing a named door has used the tie-breaking value $q=1/2$, whether or not the host actually uses that value. The quote is right for that host and wrong for a host who always prefers $B$.{{cite:grinstead_snell1997}} (§4.1, Monty Hall example){{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem)

## Statistical use — Write the observation mechanism first
The calculation is a small Bayesian update. The prior is the prize placement. The likelihood is the probability of the host's action given the prize and the contestant's choice. The posterior is proportional to the product, normalized over the prize locations that could have produced the action. Omitting the likelihood and resetting the prior to be uniform on the remaining closed doors answers a different problem, one in which the opened door was not selected using knowledge of the prize. That reset is sometimes a reasonable model of a randomly revealed empty door. It is not the model of a host who must reveal an empty door.{{cite:downey2020_thinkbayes2}} (Ch. 2, The Monty Hall Problem){{cite:grinstead_snell1997}} (§4.1, pp. 137–139)

The same distinction appears whenever a displayed subset of outcomes was chosen by someone who saw the hidden state. A card shown because it is an ace, a patient recruited because a test was positive, or a door opened because it is empty each need the probability of the display given the hidden state. Counting the remaining possibilities as if the display had been a simple deletion treats the selection probability as constant across hidden states. In the standard puzzle that probability is one when the first choice was wrong and $q$ when the first choice was right. The ratio of those selection probabilities is the whole difference between $1/3$ and $1/2$.{{cite:grinstead_snell1997}} (§4.1, conditional and unconditional formulations)
