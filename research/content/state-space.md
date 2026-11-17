## Motivating example
A weather label such as “rainy” or “dry” seems to give a two-state model. But if tomorrow's chance of rain depends on whether today is the first rainy day of a spell, today's label alone omits information needed for the next prediction. Recording both yesterday's and today's labels gives four possible states and makes the one-step rule explicit. A useful state space is therefore chosen to capture the features that govern what happens next, not merely to name the observable outcomes.{{cite:levin_peres2017}} (§1.1, pp. 2–4, states and transition rules)

## Intuition
The *index set* says when observations are made; the *state space* says what each observation can be. A daily count may have index set $\{0,1,2,\ldots\}$ and state space $\{0,1,2,\ldots\}$. A continuously monitored temperature process uses a continuous time index and real-valued states. Neither choice alone fixes the probabilities: a transition mechanism or joint law is still needed. Choosing a state too small can make a model's claimed Markov property false, while choosing one larger than necessary can make calculation harder.{{cite:levin_peres2017}} (§1.1, pp. 2–4){{cite:hastings1970}} (§2.2, pp. 100–101, continuous-state extension)

## Definition
For a process $\{X_t:t\in T\}$, its state space $S$ is a set in which each $X_t$ takes values. The index $t$ belongs to $T$ and the value $X_t$ belongs to $S$; these roles should not be interchanged. The underlying sample space $\Omega$ describes complete random outcomes. A realised path $t\mapsto X_t(\omega)$ is instead an element of a path space such as $S^T$. For a countable Markov state space the transition rule can be written as a matrix $P(i,j)$, whereas continuous states require probabilities of sets, represented by a transition kernel.{{cite:levin_peres2017}} (§1.1, pp. 2–4, finite-state formulation){{cite:hastings1970}} (§2.2, pp. 100–101, passage to continuous states)

States can themselves be structured objects. A queue may use the number waiting when arrivals and service have suitable memoryless laws; with a nonmemoryless service time, the elapsed service time may also be needed. A vector of variables can be one state, and its state space can be a product set. The state must distinguish any situations whose next-step laws differ. It need not remember history that has no further effect on those laws.{{cite:levin_peres2017}} (§1.1, p. 2, dependence on the current state)

## Properties
For a finite state space with $m$ states, a transition matrix has $m$ rows and $m$ columns; row $i$ is the distribution of the next state given state $i$. Each row is nonnegative and sums to one. An initial distribution and this matrix determine the law at later times by $\mu_t=\mu_0P^t$. A larger state description means a larger transition matrix, but it can turn an invalid memoryless claim into a valid Markov model.{{cite:levin_peres2017}} (§1.1, pp. 2–5, eqs. 1.1 and 1.10)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose a binary process $Y_t$ is specified by the rule $\Pr(Y_{t+1}=1\mid Y_0,\ldots,Y_t)=p_{Y_{t-1},Y_t}$ for $t\geq1$, where $p_{00}=p_{10}=0.2$, $p_{01}=0.3$ and $p_{11}=0.8$. Put $X_t=(Y_{t-1},Y_t)$. If $X_t=(a,b)$, then $X_{t+1}=(b,c)$ and the probability of $c$ depends only on $(a,b)$, regardless of earlier values. Thus $X_t$ has the Markov property on the four ordered pairs. The smaller process $Y_t$ does not: given $Y_t=1$, its next-rain probability is $0.3$ after $Y_{t-1}=0$ but $0.8$ after $Y_{t-1}=1$. This direct conditional-probability difference proves that today's weather alone is not a sufficient state for the specified rule. More generally, conditioning on the predecessor state gives $\mu_{t+1}(j)=\sum_i\mu_t(i)P(i,j)$, or $\mu_{t+1}=\mu_tP$; repeated substitution yields $\mu_t=\mu_0P^t$.{{cite:levin_peres2017}} (§1.1, pp. 2–5, Markov property and transition equations)
:::
:::

## Statistical use — Choosing the variables carried forward
State design begins with the prediction question. For a queue, does a count suffice to predict the next event, or does the remaining service time matter? For a weather spell, does the next-day probability depend on today's label alone, or on the current run length? Once the state is chosen, check whether two histories ending at the same proposed state really imply the same next-state distribution. This is a modelling condition; it is not established just by writing a transition matrix. The pair construction in the proof gives a simple way to repair a specific failure.{{cite:levin_peres2017}} (§1.1, pp. 2–3, conditional formulation)

## Worked example
Let $Y_t=1$ mean rain and $Y_t=0$ mean dry. Suppose the chance of rain tomorrow is $0.2$ after a dry day, $0.3$ after a first rainy day, and $0.8$ after at least two consecutive rainy days. Retain the last two labels as $X_t=(Y_{t-1},Y_t)$ and order the four states as $(0,0),(0,1),(1,0),(1,1)$. The transition matrix is

$$
P=\begin{pmatrix}
0.8&0.2&0&0\\
0&0&0.7&0.3\\
0.8&0.2&0&0\\
0&0&0.2&0.8
\end{pmatrix}.
$$

For example, from $(0,1)$ tomorrow is dry with probability $0.7$, giving new state $(1,0)$, or rainy with probability $0.3$, giving $(1,1)$. To have two more rainy days from $(0,1)$, both successive moves must go to $(1,1)$, with probability $0.3(0.8)=0.24$. From $(1,1)$ the same two-day event has probability $0.8^2=0.64$. Today's visible weather is rainy in both cases, yet the predictions differ; the four-state description preserves the relevant past.{{cite:levin_peres2017}} (§1.1, pp. 2–4, transition-matrix method)

**Your turn.** Starting from state $(1,0)$, find the distribution of the next state and the probability that it is raining two days later.

::: {.callout-tip collapse="true" title="Answer"}
From $(1,0)$ the next state is $(0,0)$ with probability $0.8$ or $(0,1)$ with probability $0.2$. Another day later, rain has probability $0.2$ from $(0,0)$ and $0.3$ from $(0,1)$. Thus $\Pr(Y_{t+2}=1\mid X_t=(1,0))=0.8(0.2)+0.2(0.3)=0.22$. The two-day answer sums over both possible intermediate states.
:::

## Common misconceptions
The state space is not the set of time points; a daily binary series has infinitely many possible times but only two possible observed labels at any one time. It is not the sample space $\Omega$ either: one random outcome can determine an entire path, not just a single state. Nor does listing states make a process Markov; the weather example needs extra memory to give one transition rule per state. Finally, more states are not always better: redundant history can inflate the transition system without improving predictions.{{cite:levin_peres2017}} (§1.1, pp. 2–4)

## Assumptions and limits — When a proposed state is incomplete
In the worked model, taking $S=\{0,1\}$ and calling $Y_t$ a Markov chain gives incompatible next-rain probabilities after histories $(0,1)$ and $(1,1)$. A queue with deterministic service duration offers another failure: two queues with the same number of customers but different elapsed service times have different chances of a near-term completion. Adding elapsed time to the state can restore a local transition rule. With a hidden environment that changes arrival rates, even count plus service age may be insufficient unless the environment or its conditional distribution is represented. Each failure identifies a particular missing predictor, rather than a flaw in the abstract definition of state space.{{cite:levin_peres2017}} (§1.1, pp. 2–3, state sufficiency)

## Connections
The [stochastic process](stochastic-process.qmd) definition pairs a state space with a time index. A [transition matrix](transition-matrix.qmd) describes moves when the state set is finite or countable. The [Markov property](markov-property.qmd) asks whether the next-state law depends on the current state alone. The question on [Markov property and invariance](../questions/c-12.qmd) tests that sufficiency idea; [same marginals, different joints](../questions/ex-sp-same-marginals.qmd) shows why a state set and one-time distributions do not determine paths; [stationary increments are not a fixed level](../questions/ex-sp-increments-and-levels.qmd) tests the distinction between time and state.{{cite:levin_peres2017}} (§1.1, pp. 2–5)

## History
Markov's 1906 work made dependence between successive observations a subject of mathematical probability. Early chain examples use discrete collections of states; the same state-and-transition language later extended to continuous variables, for which transition densities or kernels replace finite matrices. The important modelling choice persists across both settings: the current state must carry the information needed to specify the next transition.{{cite:dodge2008}} (pp. 330–331, Markov entry){{cite:levin_peres2017}} (Ch. 1 Notes, p. 19; §1.1, pp. 2–5){{cite:hastings1970}} (§2.2, pp. 100–101, continuous-state construction)
