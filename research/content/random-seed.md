## Motivating example
Two runs of a simulation can produce different estimates merely because they consume different pseudorandom streams. A recorded starting state lets an analyst replay the numerical experiment and distinguish such variation from a change in the model or algorithm. This is a property of a deterministic generator's state, rather than evidence that its output is a physical source of randomness.{{cite:dodge2008}} (p. 223, deterministic pseudorandom generation)

## Definition — A state initialises a deterministic transition
For a generator with state $S_i$, write its update as $S_{i+1}=F(S_i)$ and its numerical output as $U_i=G(S_i)$. Once $S_0$, the transition rule and the output rule are fixed, all subsequent outputs are determined. A simple congruential generator can have a single integer state; more elaborate algorithms use vectors together with a position index. The user-facing seed argument can initialise that larger state without being identical to the complete state itself.{{cite:dodge2008}} (p. 223, congruential generation){{cite:r_base_random2026}} (§Description and §Details, generator state and `set.seed`)

This state description explains reproducibility by induction. Equal initial states give equal first outputs. Applying the same transition preserves equality of the next states, so the argument repeats for every step. Equal seed labels do not give the same output if they initialise different algorithms or if the algorithms consume random inputs in a different order. Reproducibility therefore includes the configuration and the sequence of calls, not only one printed integer.

## Properties — Reproducibility and statistical quality answer different questions
A finite deterministic state space eventually repeats a state. Once it repeats, the future repeats as well. A sufficiently long period can avoid immediate repetitions in a numerical experiment, but a long cycle alone does not establish the absence of harmful correlations or lattice patterns. For a demonstration of state control, even a deliberately tiny generator is useful; for substantive simulation, its statistical quality must be evaluated separately.{{cite:dodge2008}} (p. 223, cycle length and choice of constants)

R's `.Random.seed` stores generator state, while `set.seed` is the recommended user interface for initialisation. `RNGkind` controls the uniform generator and related normal and sampling methods. `RNGversion` supports reproducing configurations associated with earlier R versions. Those are software controls; the deterministic-state argument does not require any particular programming language.{{cite:r_base_random2026}} (§Description, §Usage and §Details)

## Worked example — Trace every state in a tiny cycle
Consider the illustrative recurrence $S_{i+1}=(5S_i+1)\bmod8$ with output $U_i=S_i/8$. Starting at seed one and listing the state before each update gives
$$1,6,7,4,5,2,3,0,1.$$
Every state appears before the return to one, so its period is eight. Starting instead at seed three gives $3,0,1,6,7,4,5,2,3$. These are positions on one cycle; the two streams should not be regarded as independent draws from two new physical experiments.

The first three reported outputs from seed one are $0.125$, $0.750$ and $0.875$. If one call consumes the first output before the main simulation begins, the next reported value is $0.750$ rather than $0.125$. The initial seed has not changed, but the program is requesting a different part of the sequence. This is an explicit calculation with the toy recurrence, not a description of R's default generator.{{cite:r_base_random2026}} (§Details, available generator algorithms)

**Your turn.** Under the same toy recurrence, take seed zero. What are the first three states, including the seed, and their corresponding outputs?

::: {.callout-tip collapse="true" title="Answer"}
The states are $0,1,6$, giving outputs $0.000$, $0.125$ and $0.750$. The next state is seven.
:::

## Statistical use — Record the experiment as well as the seed
A reproducible numerical report specifies the generator configuration, software environment, seed or state-restoration protocol, and the order in which stochastic operations are run. Parallel execution requires special care because work scheduling can change which operation consumes a stream. Merely assigning nearby seeds does not mathematically establish independent streams; a generator's documented stream-splitting or substream facility provides a more explicit design.{{cite:r_base_random2026}} (§Details, L’Ecuyer-CMRG and multiple streams)

Resetting the same seed before every replicate changes the experiment being run. If every replicate replays one sequence, the replicates are copies of a single deterministic stream and their sample variance is zero whenever the procedure's calls are the same. Independent Monte Carlo variation uses a stream that advances, or a documented split into substreams. One reset at the start of the experiment, followed by the procedure's own calls, is the pattern that makes a later replay match the original run. R's example of setting a seed, generating a vector and resetting the seed shows that the replayed vector matches. The match is a statement about determinism.{{cite:r_base_random2026}} (§Examples)

## Intuition — The seed selects a position on a cycle
The toy recurrence $S\mapsto(5S+1)\bmod 8$ has eight states. Starting at $1$ visits every residue before returning, so the period is the whole state space. Starting at $3$ visits the same eight states in a rotated order. The two seeds are two entry points on one cycle. Their outputs $S/8$ are therefore dependent in a strong sense: each is a shift of the other. A ninth draw from seed $1$ repeats the first output $0.125$, because the state has returned to $1$.

Seed $2$ produces the states $2,3,0,1$ and the outputs $0.250$, $0.375$, $0.000$, $0.125$ before the next state $6$. Those four numbers sit on the same cycle as seed $1$. Consuming one extra draw at the start of a program advances the entry point by one step. From seed $1$ the first output is $0.125$ and the second is $0.750$. A program that discards one draw and then records “the first” output records $0.750$. The seed integer is still $1$. The state that the next call sees is $6$.{{cite:dodge2008}} (p. 223, cycle length and choice of constants)

The same arithmetic on a different modulus shows that a full cycle is a property of the constants together with the modulus. The map $S\mapsto(5S+1)\bmod 7$ started at $1$ visits $1,6,3,2,4,0$ and returns, an orbit of length $6$. The missing state $5$ satisfies $(5\cdot5+1)\bmod 7=5$, so it is a fixed point and a second orbit. Full period on the toy modulus $8$ does not transfer to modulus $7$ with the same multiplier and increment. Publishing the seed without the modulus, the multiplier and the increment leaves the sequence underdetermined.

## Common misconceptions
A long period means the state takes a long time to repeat. It says little, by itself, about equidistribution in several dimensions or about correlations at the lags a particular simulation uses. The toy generator is a teaching device for state updates. Substantive simulation uses a generator whose statistical properties have been studied for the sample sizes at hand, and the seed is then a handle for replaying that generator.{{cite:dodge2008}} (p. 223, deterministic pseudorandom generation)

Nearby seeds are sometimes treated as a source of independent streams. In the toy cycle, seeds $1$ and $3$ produce shifts of one sequence. Assigning them to two parallel workers creates two overlapping views of the same cycle. A generator with an explicit substream interface assigns disjoint blocks of the period, which is a different construction from adding one to an integer seed.{{cite:r_base_random2026}} (§Details, L’Ecuyer-CMRG and multiple streams)

## Connections
The output $U_i=G(S_i)$ is the number that enters a Monte Carlo average. The state $S_i$ is the object that makes the average replayable. Inverse-transform sampling, accept–reject sampling and a bootstrap all consume these outputs in an order determined by the algorithm's branches. A change in that order, even with the same seed, pairs the underlying uniforms with different steps of the algorithm. Recording the generator kind, the seed, and the sequence of random calls is what makes the numerical experiment a function of a documented initial state.{{cite:r_base_random2026}} (§Description and §Details, generator state and `set.seed`)
