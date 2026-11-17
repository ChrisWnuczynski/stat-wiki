## Lead context
Two states belong to the same communicating class when the chain can travel from each to the other, so the class is the set of states that share a future.{{cite:siegrist2022_markov_recurrence}} (§4, to-and-from relation)

## Motivating example
A machine is either working or broken. From working it always breaks at the next inspection, and once broken it stays broken. The two states do not share a future: the broken state can be reached from the working state, and the working state cannot be reached from the broken state. Putting them in one class would say that the chain can come back, which this transition rule never does.{{cite:siegrist2022_markov_recurrence}} (§4, closed sets and equivalence classes)

## Intuition
Draw an arrow from $i$ to $j$ when one step has positive probability. A longer trip is a path of arrows. State $j$ is accessible from $i$, written $i\to j$, when $i=j$ or some path runs from $i$ to $j$. That relation is reflexive and transitive. It becomes an equivalence relation only after it is made symmetric: $i$ communicates with $j$ when $i\to j$ and $j\to i$. The equivalence classes of that two-way relation are the communicating classes.{{cite:siegrist2022_markov_recurrence}} (§4, leads-to relation and equivalence classes)

A class is not the same thing as a closed set. A set is closed when no arrow leaves it. An equivalence class can fail to be closed, because a state may lead out to a state that does not lead back. A closed set can fail to be a single class, because it may contain two groups that cannot reach each other.{{cite:siegrist2022_markov_recurrence}} (§4, closed sets need not be classes)

## Definition
Let $P$ be the transition matrix of a discrete-time chain on a countable set $S$. Write $P^n(i,j)$ for the $n$-step probability. Then $i\to j$ when $P^n(i,j)>0$ for some integer $n\ge 0$, with the $n=0$ case counting $i\to i$. States $i$ and $j$ communicate when each leads to the other. The communicating class of $i$ is
\[
[i]=\{j\in S: i\leftrightarrow j\}.
\]
The classes partition $S$. A nonempty set $A$ is closed when $i\in A$ and $i\to j$ imply $j\in A$. A closed set with no proper closed subset is irreducible. An irreducible set is a communicating class, and a chain whose whole state space is irreducible is called an irreducible chain.{{cite:siegrist2022_markov_recurrence}} (§4, equivalence classes and irreducible sets)

## Interpretation
Inside a closed class the chain stays forever if it starts there, and the restriction of $P$ to that class is itself a transition matrix. Outside a closed class, a state that can reach the class and is not in it is on the way in or on the way out. In a finite chain every finite closed set contains a recurrent state, and a finite irreducible class is recurrent: every state in it is visited infinitely often with probability one. A finite class that is not closed is transient. Recurrence and transience do not mix inside one communicating class.{{cite:siegrist2022_markov_recurrence}} (§4, class properties and finite closed sets)

The period is a class property as well. The period of $i$ is the greatest common divisor of the times $n\ge 1$ with $P^n(i,i)>0$. If $i$ communicates with $j$, the two periods agree, so one speaks of the period of the class. A self-loop forces period $1$. A self-loop is not necessary: return times $2$ and $3$ already have greatest common divisor $1$.{{cite:siegrist2022_markov_period}} (§5, period is a class property; a self-loop is sufficient but not necessary)

## Properties
Communication is an equivalence relation, so the classes are disjoint and cover $S$. If $A$ is closed, then $(P^n)$ restricted to $A$ equals the $n$th power of the restricted matrix: paths that would have left $A$ have probability zero. If $A$ is a recurrent class then $A$ is irreducible. In a finite chain the transient states are exactly those that lie in no closed class.{{cite:siegrist2022_markov_recurrence}} (§4, canonical decomposition)

Aperiodicity is not required for a stationary distribution. The deterministic alternation
\[
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
has one communicating class, period $2$, and stationary distribution $(1/2,1/2)$. Its powers do not converge: $P^{2m}=I$ and $P^{2m+1}=P$. The stationary distribution describes long-run frequencies along a path. It does not describe the one-step distribution, which keeps flipping.{{cite:siegrist2022_markov_period}} (§5, period and limiting behaviour)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Reflexivity is the convention $n=0$. Symmetry is the definition of $\leftrightarrow$. If $i\to j$ in $r$ steps and $j\to k$ in $s$ steps, the Chapman–Kolmogorov inequality $P^{r+s}(i,k)\ge P^r(i,j)P^s(j,k)$ gives $i\to k$. Thus $\leftrightarrow$ is an equivalence relation and its classes partition $S$.{{cite:siegrist2022_markov_recurrence}} (§4, transitivity of leads-to)

If $A$ is closed and $i\in A$, $j\notin A$, then $P(i,j)=0$, so each row of $P$ restricted to $A$ sums to one. If $i$ communicates with $j$ and $d(i)$ divides every return time to $i$, the same divisor divides every return time to $j$: a return to $j$ of length $n$, sandwiched between a trip $i\to j$ and a trip $j\to i$, produces a return to $i$ whose length differs from $n$ by a fixed sum already divisible by $d(i)$. Hence $d(i)=d(j)$.{{cite:siegrist2022_markov_period}} (§5, proof that the period is shared)

For the alternation, $P^2=I$, so returns occur at the even times and the period is $2$. The vector $(1/2,1/2)$ satisfies $\pi P=\pi$ because each row of $P$ merely swaps the two coordinates. The powers alternate, so $\lim_n P^n$ does not exist.{{cite:siegrist2022_markov_period}} (§5, periodicity complicates limits)
:::
:::

## Statistical use — Which long-run sentence is available
Before solving $\pi P=\pi$, name the closed classes. Each finite closed class carries its own stationary distribution, and a chain that can start in more than one of them does not have a unique stationary law. A unique positive stationary distribution on a finite set needs one closed class, that is, an irreducible finite chain. Convergence of $P^n$ to that distribution needs the class to be aperiodic as well. The alternation has the stationary law and does not have the limit.{{cite:siegrist2022_markov_recurrence}} (§4, finite irreducible classes){{cite:siegrist2022_markov_period}} (§5, limiting behaviour)

## Worked example
Take states $\{0,1\}$ and
\[
P=\begin{pmatrix}0&1\\0&1\end{pmatrix}.
\]
State $0$ leads to $0$ in zero steps and to $1$ in one step. State $1$ leads only to $1$. The communicating classes are $\{0\}$ and $\{1\}$. The set $\{1\}$ is closed. The set $\{0\}$ is a class and is not closed, because $0\to 1$ and $1\notin\{0\}$. The whole space is closed and is not one class.{{cite:siegrist2022_markov_recurrence}} (§4, the two-state example)

Now take states $\{a,b,c\}$ and
\[
P=\begin{pmatrix}0&1/3&2/3\\0&0&1\\1&0&0\end{pmatrix}.
\]
There is a path between every pair, so the chain is one class and that class is closed. No diagonal entry is positive. Still $P^2(a,a)\ge (2/3)\cdot 1=2/3$ by the path $a\to c\to a$, and $P^3(a,a)\ge (1/3)\cdot 1\cdot 1=1/3$ by the path $a\to b\to c\to a$. The return times include $2$ and $3$, whose greatest common divisor is $1$, so the class is aperiodic.{{cite:siegrist2022_markov_period}} (§5, returns at times $2$ and $3$)

**Your turn.** Label the rows of the alternation matrix as states $1$ and $2$. Compute $P^2$ and the period of state $1$.

::: {.callout-tip collapse="true" title="Answer"}
$P^2=I$, so the chain returns to $1$ in two steps and not in one step. The period is $2$. State $2$ has the same period because the two states communicate.
:::

## Common misconceptions
A closed set is not automatically one communicating class. In the two-state example the whole space is closed and splits into $\{0\}$ and $\{1\}$. A communicating class is not automatically closed: $\{0\}$ communicates with itself and still leads out.{{cite:siegrist2022_markov_recurrence}} (§4, the two comparisons)

A stationary distribution is not a limit of $P^n$. The alternation has $\pi=(1/2,1/2)$ and $P^n$ equal to $P$ or $I$ according to the parity of $n$. Averaging the two matrices gives $\pi$ in each row. The sequence of matrices does not settle.{{cite:siegrist2022_markov_period}} (§5, limiting behaviour)

Absence of a self-loop is not periodicity. The three-state chain above has zeros on the diagonal and period $1$, because $2$ and $3$ are return times.{{cite:siegrist2022_markov_period}} (§5, a self-loop is not necessary)

## Assumptions and limits — When the class picture is not the chain
The arrows record positive probability, not the size of that probability. A transition of $10^{-9}$ still puts two states in the same class, and a computation that thresholds tiny probabilities can split a class the mathematics does not split. The finite-state recurrence claim uses finiteness. Siegrist's argument picks one state that is visited infinitely often because a finite set cannot share infinitely many visits without one state taking infinitely many; that counting step stops applying when the closed set is infinite. The period is a greatest common divisor of return times, so it is undefined as a class property until communication has been checked. Two states with the same period need not communicate.{{cite:siegrist2022_markov_recurrence}} (§4, countable state space){{cite:siegrist2022_markov_period}} (§5, period within a class)

## Connections
An [irreducible Markov chain](irreducible-markov-chain.qmd) is a chain with one communicating class. A [stationary distribution](stationary-distribution.qmd) solves $\pi P=\pi$; uniqueness on a finite set uses that single closed class. The [limiting distribution](limiting-distribution.qmd) needs aperiodicity of that class as well. A self-loop is one way to force period $1$, and it is not the only way.{{cite:siegrist2022_markov_recurrence}} (§4, irreducible chains){{cite:siegrist2022_markov_period}} (§5, aperiodicity)

## Check yourself

1. In the matrix with rows $(0,1)$ and $(0,1)$, is $\{0,1\}$ a communicating class?

::: {.callout-tip collapse="true" title="Answer"}
No. State $1$ does not lead to state $0$, so the states do not communicate. There are two classes, $\{0\}$ and $\{1\}$.
:::

2. For the alternation, does $\pi=(1/2,1/2)$ satisfy $\pi P=\pi$?

::: {.callout-tip collapse="true" title="Answer"}
Yes. Each coordinate of $\pi P$ is $1/2$, because each column of $P$ contains a single $1$. The chain still has period $2$, so the stationary equation has a solution and $P^n$ does not converge.
:::

3. If a state has a self-loop, what is its period?

::: {.callout-tip collapse="true" title="Answer"}
The period is $1$. A return in one step is on the list whose greatest common divisor is the period, and that divisor is then $1$. The rest of the class is aperiodic as well.
:::

## History
The classification used here is the equivalence relation of mutual accessibility for a discrete-time chain: $i$ leads to $j$ when some $n$-step probability is positive, including the zero-step case $i\to i$, and communication is the two-way relation. Closed sets are the sets that no path leaves. Siegrist's account shows by a two-state chain that a class need not be closed and a closed set need not be a single class, and it shows that recurrence is constant on a class. The period, defined as the greatest common divisor of the return times, is constant on a class for the same path-sandwiching reason.{{cite:siegrist2022_markov_recurrence}} (§4, equivalence classes){{cite:siegrist2022_markov_period}} (§5, period is a class property)
