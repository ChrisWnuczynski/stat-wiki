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

Resetting the same seed before every replicate can also change the intended experiment. If every replicate uses an identical sequence, the resulting values may be identical by construction and do not measure independent Monte Carlo variation. Reset once at an appropriate experiment boundary, then allow the state to advance according to the procedure being studied. R's example of setting a seed, generating a vector and resetting the seed demonstrates equality of the replayed vector, rather than a claim that resetting improves statistical independence.{{cite:r_base_random2026}} (§Examples)
