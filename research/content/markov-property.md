## Motivating example

A weather forecast may use today's condition to predict tomorrow's, even after yesterday's condition is known. If today's condition captures everything in the recorded history that matters for the next day, the weather-state process has the Markov property. The rule makes prediction manageable: one transition distribution for each current state replaces a different rule for every possible history.{{cite:levin_peres2017}} (§1.1, pp. 2–4, Markov definition)

## Intuition

“No memory” is shorthand for a *conditional* statement. Yesterday can help predict tomorrow when today's state is unknown, because yesterday provides information about today. Once today's state is given, the Markov model says that earlier states add nothing to the next-state distribution. That is different from independence of successive states. The condition also depends on how the state was defined: working versus failed may omit machine age, while working-with-age can carry the information needed for prediction.{{cite:levin_peres2017}} (§§1.1–1.2, pp. 2–6)

## Definition

For any history with positive probability, the conditional law of $X_{n+1}$ given $X_0,\ldots,X_n$ equals its law given $X_n$. In a finite state space, it is enough to check the equality for each possible next state. A homogeneous Markov chain also uses the same transition law at each time $n$; the Markov property itself permits time-varying transition probabilities. Conditional probabilities given a zero-probability history are not specified by the elementary ratio formula, so the displayed finite-state equality is understood on histories for which conditioning is defined.{{cite:levin_peres2017}} (§1.1, pp. 2–3, positive-probability histories)

The Markov condition can be written as $X_{n+1}\perp (X_0,\ldots,X_{n-1})\mid X_n$. This is a one-step conditional-independence relation. It extends to the whole future given the present for a chain constructed by repeatedly using its transition rule. The distribution of $X_0$ and the transition probabilities together determine all finite path probabilities; the transition matrix alone does not specify how a path starts. {{cite:levin_peres2017}} (§1.1, pp. 2–4, path probability and transition matrix)

## Properties

For a homogeneous finite chain and a positive-probability path $i_0,\ldots,i_n$, its probability is $\Pr(X_0=i_0)\prod_{t=0}^{n-1}P_{i_ti_{t+1}}$. Summing over intermediate states gives $P^{m+n}=P^mP^n$. Those identities allow exact short-horizon predictions without enumerating histories one by one. They say nothing yet about whether probabilities settle to a long-run law; irreducibility and aperiodicity address that separate question.{{cite:levin_peres2017}} (§§1.1, 1.3, pp. 2–4, 7–8)

State augmentation can convert certain higher-order dynamics into a first-order Markov chain. If the next binary outcome depends on the last two outcomes, take the ordered pair $(X_{n-1},X_n)$ as the new state. Its next state is $(X_n,X_{n+1})$, and the pair contains exactly the information required for the rule. Whether such a representation is useful depends on how many states it creates and whether the assumed rule fits the process. {{cite:levin_peres2017}} (§1.1, Markov state description)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The probability chain rule factors a path as $\Pr(X_0=i_0)\prod_{t=0}^{n-1}\Pr(X_{t+1}=i_{t+1}\mid X_0=i_0,\ldots,X_t=i_t)$. The Markov property replaces each conditional factor by $P_{i_ti_{t+1}}$ in a homogeneous chain. For $m+n$ steps, condition on the state $k$ at time $m$ and use the same rule for the remaining $n$ steps: $\Pr(X_{m+n}=j\mid X_0=i)=\sum_k(P^m)_{ik}(P^n)_{kj}$. This is the $(i,j)$ entry of $P^mP^n$.{{cite:levin_peres2017}} (§1.1, pp. 2–4)

If the next-outcome law depends on $(X_{n-1},X_n)$, then conditioning on the entire history of pairs reveals the same last pair. The next pair $(X_n,X_{n+1})$ therefore has a law determined by the current pair. This proves the stated augmented-state Markov representation under the assumed two-step rule. {{cite:levin_peres2017}} (§1.1, state and transition definition)
:::
:::

## Statistical use — Choosing a state

To use a Markov model, define the observation times and state variables before estimating transition probabilities. Then compare transitions from the same current state across different earlier histories. A systematic difference is evidence that the proposed state leaves out predictive information. A transition matrix can be estimated from observed counts in a homogeneous finite chain, but sparse state-to-state counts make estimates uncertain. In simulation, drawing each next state from the row indexed by the present state enforces the Markov rule by construction.{{cite:levin_peres2017}} (§§1.1–1.2, pp. 2–6)

Suppose a binary process has $\Pr(X_{n+1}=1\mid X_n=0,X_{n-1}=0)=0.2$ but $\Pr(X_{n+1}=1\mid X_n=0,X_{n-1}=1)=0.8$. The same current state gives different next-state laws, so the binary process fails the one-step Markov condition. A state containing the last pair can repair this particular model. A weather process with a hidden changing season may likewise show history dependence if only dry or wet is recorded; adding the season may help, but a time-varying external driver needs its own modeling assumptions.{{cite:levin_peres2017}} (§1.1, state-dependent transition definition)
## Worked example

Use states dry and wet with transition matrix $P=\begin{pmatrix}0.8&0.2\\0.4&0.6\end{pmatrix}$. Suppose the initial chance of dry is $0.5$. Then $\Pr(X_1=\mathrm{dry})=0.5(0.8)+0.5(0.4)=0.6$. If today is dry, the chance of a dry tomorrow is $0.8$ whether yesterday was dry or wet. But given only that yesterday was wet, the chance of dry two days later is $0.4(0.8)+0.6(0.4)=0.56$. The past can affect an *unconditional-on-today* forecast without violating the conditional Markov rule.{{cite:levin_peres2017}} (§1.1, pp. 2–4, two-state transitions)

**Your turn.** With the same matrix, suppose yesterday was dry. Find the chance of wet two days later. Then state the chance of wet tomorrow if today is known to be wet, regardless of yesterday.

::: {.callout-tip collapse="true" title="Answer"}
From a dry start, the two paths ending wet have probabilities $0.8(0.2)$ and $0.2(0.6)$, summing to $0.28$. Once today's state is known to be wet, the next-day wet probability is $0.6$ under the Markov rule, whatever yesterday's condition. The two questions condition on different information.
:::

## Common misconceptions

Markov does not mean independent across time; transition probabilities can strongly favor staying in the same state. It does not mean the process has a stationary distribution or has reached one. Time homogeneity is another condition and is not part of the memory rule. Finally, a process can fail to be Markov in a coarse state description and become Markov after the state is enriched; the choice of state is a modeling decision.{{cite:levin_peres2017}} (§§1.1, 1.3, 1.5, pp. 2–10)

## Connections

[Finite-state Markov chains](finite-state-markov-chain.qmd) express the condition in a transition matrix. [Conditional independence](conditional-independence.qmd) is its probability-language form; [Chapman–Kolmogorov equations](chapman-kolmogorov-equations.qmd) compose its transitions. A [stationary distribution](stationary-distribution.qmd) is an invariant law, while [limiting distribution](limiting-distribution.qmd) requires additional convergence conditions.{{cite:levin_peres2017}} (§§1.1, 1.5, 4.3)

## History

Markov's studies of dependent quantities gave a systematic route beyond independent-trial calculations; Dodge's biographical entry connects his work to the later theory of stochastic processes. Modern finite-chain treatments state the property through conditional probabilities and transition matrices, making clear which part of the past the state is intended to summarize.{{cite:dodge2008}} (pp. 330–331, Markov entry){{cite:levin_peres2017}} (§1.1, pp. 2–4)
