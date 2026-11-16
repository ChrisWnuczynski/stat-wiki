## Motivating example
Imagine a customer moving through a service system. From the waiting room the customer may remain there for another step or leave for a completed state, from which return is impossible. The waiting-room state can be visited repeatedly, but not with certainty after departure. By contrast, a state inside a small closed network of rooms will eventually be revisited even if the next move goes elsewhere. Recurrence describes this eventual-return distinction.

## Intuition
Start a Markov chain in state $i$ and ask whether it ever visits $i$ again at a strictly later time. If that probability is one, $i$ is recurrent; if there is a positive chance of no return, it is transient. Recurrence is not the same as a large one-step self-transition probability. A chain may leave $i$ at once and still be certain to return, or it may linger for many steps before escaping forever.

After each return to $i$, the Markov property restarts the same return experiment. If the return chance is below one, the number of visits has a geometric tail and finite mean. If it is one, visits recur indefinitely with probability one. For finite closed communicating classes, eventual return also has finite expected time. On an infinite state space, certainty of return and finiteness of expected return time must be distinguished.

## Definition
Let $X_0=i$ and define $T_i^+=\inf\{n\geq1:X_n=i\}$, with $T_i^+=\infty$ if there is no later visit. State $i$ is recurrent when $f_i=\Pr_i(T_i^+<\infty)=1$, and transient when $f_i<1$. A recurrent state is positive recurrent if $\mathbb E_iT_i^+<\infty$ and null recurrent if this expectation is infinite. The probability and expectation refer to a chain started at $i$, not to a particular observed path of finite length.

Communicating states share recurrence classification, so it is often more useful to classify a communicating class than every state separately. A closed class has no transition out of it. In a finite chain, each closed irreducible class is positive recurrent; states that can be left for a closed class without a return route are transient. An absorbing state is the simplest closed class and returns to itself after one step.

## Properties
If $f_i<1$, the expected total number of visits to $i$, counting time zero, is $1/(1-f_i)$. This result turns a return probability into a tangible amount of time spent at a state. It does not say when those visits occur. The mean first-return time is defined only when return is certain, and it can be infinite for a null-recurrent state.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
At each visit to $i$, the strong Markov property makes the chance of a further return equal to $f_i$. Thus the chance of at least $k+1$ total visits is $f_i^k$ for $k\geq0$. Summing these tail probabilities gives $\mathbb E_iN_i=\sum_{k\geq0}f_i^k=1/(1-f_i)$ when $f_i<1$; when $f_i=1$ the chain returns after every visit almost surely and the sum diverges. Now fix a state $i$ in a finite closed irreducible class $C$. From each $j\in C$ there is a finite positive-probability path to $i$. Finiteness lets us choose a common block length $L$ and a lower bound $\delta>0$ on the chance of hitting $i$ within $L$ steps from any $j\in C$. The Markov property then bounds the chance of avoiding $i$ for $kL$ steps by $(1-\delta)^k$. Both the hitting probability one and a finite expected hitting time follow. Starting at $i$, take one step and apply the same bound, proving positive recurrence. In a finite chain, a state outside all closed classes has a positive-probability path into a closed class from which it cannot return; repeating finite-step opportunities shows that such a state is transient.
:::
:::

## Interpretation
An absorbing state is recurrent, even though it may be an undesirable outcome. Conversely a transient state can be visited many times before its final departure. The labels describe path structure, not value or importance. Stationary distributions in a finite chain put their mass on closed recurrent classes; a transient state can still dominate a short initial period and matter greatly for a finite-horizon question.

Recurrence is compatible with periodic motion. A deterministic two-state alternation returns to each state every two steps and is positive recurrent, yet its one-time distribution oscillates from a fixed start. Thus recurrence alone does not imply that transition probabilities converge to a stationary distribution without an aperiodicity condition.

## Statistical use
Draw a directed graph of positive transition probabilities and identify communicating classes and exits. In a finite model, closed classes identify the long-run regions; transient states describe routes into them. Return probabilities and expected visit counts then quantify repeated use of a queue, retries in a protocol or repeated contacts with a treatment state. When transitions are estimated from data, a small unobserved exit probability can change a state from recurrent to transient, so scientific knowledge about whether an exit is truly impossible matters.

## Worked example
Consider states $A,B,C$. From $A$ the chain stays at $A$ with probability $0.5$ and moves to $B$ with probability $0.5$; from $B$ it moves to $C$ with probability one; $C$ is absorbing. Starting at $A$, a later return occurs only if the first move stays at $A$, so $f_A=0.5$. The expected total visits to $A$ are $1/(1-0.5)=2$, including the initial visit. State $B$ is transient because its next move cannot lead back. State $C$ is recurrent and positive recurrent, with return time one. Repeated chances of leaving $A$ eventually lead to $C$ with probability one, even though several visits to $A$ may precede that move.

**Your turn.** Change the self-transition probability at $A$ to $0.75$, with probability $0.25$ of moving to $B$ and all other transitions unchanged. Find $f_A$ and the expected total number of visits to $A$. Does increasing its self-transition probability make $A$ recurrent?

::: {.callout-tip collapse="true" title="Answer"}
Now $f_A=0.75$ and $\mathbb E_AN_A=1/(1-0.75)=4$. State $A$ remains transient because there is still probability $0.25$ of leaving for a route with no return. Its expected visit count rises, but recurrence would require eventual-return probability one.
:::

## Common misconceptions
A high chance of staying one more step is not recurrence; the $0.75$ example still escapes eventually. A recurrent state need not return quickly: null recurrence allows an infinite mean return time. An absorbing state is recurrent by the definition, not transient because the process “ends” there. And seeing a return in a finite simulated path cannot establish that every path returns with probability one.

## Assumptions and limits
If a model treats $C$ as absorbing but an unmodelled reset can send the process back to $A$, the class structure and recurrence labels can change. Infinite state spaces also defeat the simple rule that every closed irreducible class is positive recurrent; an unbounded random walk can wander for arbitrarily long periods. A deterministic two-cycle shows a different limit: both states are recurrent, yet transition probabilities at a fixed late time keep alternating. These counterexamples concern missing transitions, state-space size and periodicity.

## Connections
[Communicating classes](communicating-classes.qmd) group states with shared return behaviour. An [irreducible Markov chain](irreducible-markov-chain.qmd) has one such class; in a finite closed chain its states are positive recurrent. A [stationary distribution](stationary-distribution.qmd) describes long-run occupancy of recurrent classes, while [periodicity](recurrence-and-period.qmd) controls whether one-time distributions settle. Dodge's biographical account connects Markov's work on dependent processes with the later theory of chains.{{cite:dodge2008}} (pp. 330–331, “Markov, Andrei Andreevich”)

## History
Dodge attributes the early development of Markovian dependence to Andrei Markov's work and records its appearance in his Kazan University publications.{{cite:dodge2008}} (pp. 330–331, “Markov, Andrei Andreevich”) The distinction between states that can be left forever and states that must be revisited is one way to understand the long-run structure of those dependent processes.
