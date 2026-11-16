## Motivating example
A loaded die has six possible faces, but they need not have equal chances. Assigning a weight to each face determines the chance of every event made from those faces, including “even” or “at least four.” A probability measure is the rule that makes all such event probabilities consistent. On larger spaces the same rule must handle countably many disjoint possibilities, which is why its additivity axiom is stronger than a finite counting recipe.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–3, probability spaces and discrete examples)

## Intuition
Start with a sample space $\Omega$ of outcomes and a collection $\mathcal F$ of events that can be assigned probabilities. The measure $\Pr$ acts on events, not on a vague “chance” in isolation. Nonnegativity prevents negative chances; normalization makes the entire sample space certain; countable additivity combines mutually exclusive events without double counting. The figure of coin-toss averages illustrates repeated trials under one particular probability measure, but it does not define the axioms and does not require every probability measure to arise from a fair coin.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–3)

## Definition
A probability measure is a nonnegative, countably additive set function on a sigma-algebra $\mathcal F$ with $\Pr(\Omega)=1$. The triple $(\Omega,\mathcal F,\Pr)$ is a probability space. The domain matters: in finite or countable discrete examples, all subsets can serve as events, but on a general uncountable space a specified sigma-algebra is needed. Countable additivity applies to pairwise disjoint events whose union remains an event, and it includes the finite sum rule as a special case.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–2, probability-space definition)

One can construct a discrete probability measure by choosing nonnegative outcome weights $p(\omega)$ that sum to one and setting $\Pr(A)=\sum_{\omega\in A}p(\omega)$. Equal weights are one choice, not an axiom. For a continuous real-valued observation, a density may determine event probabilities by integration; a probability measure need not have a density, and a single exact point can have probability zero without being excluded from the sample space.{{cite:durrett2019}} (Ch. 1, §§1.1–1.2, pp. 2–3, 10–15)

## Properties
The original Properties section derives the empty-event, monotonicity, complement and two-event union rules. Countable additivity also implies continuity from below: if events $A_n$ increase to $A$, then $\Pr(A_n)\uparrow\Pr(A)$. For decreasing events, $\Pr(A_n)\downarrow\Pr(\cap_nA_n)$ because $\Pr(A_1)\leq1$. These limit rules are needed when events are built by approximation rather than by a finite list.{{cite:durrett2019}} (Ch. 1, §1.1, probability-measure properties)

For overlapping events, additivity applies only after separating their nonoverlapping pieces. Thus $\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)$, not the plain sum. Independence is a separate statement, $\Pr(A\cap B)=\Pr(A)\Pr(B)$; the axioms alone do not make events independent. In the equal-outcome finite case, the ratio $|A|/|\Omega|$ follows because each singleton receives $1/|\Omega|$, while a loaded die needs its actual weights.{{cite:durrett2019}} (Ch. 1, §1.1, pp. 2–3)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Countable additivity applied to $\Omega$ and empty disjoint pieces gives $\Pr(\varnothing)=0$. If $A\subseteq B$, split $B=A\mathbin{\dot\cup}(B\setminus A)$ to obtain $\Pr(B)\geq\Pr(A)$. Splitting $\Omega=A\mathbin{\dot\cup}A^c$ gives $\Pr(A^c)=1-\Pr(A)$ and hence $0\leq\Pr(A)\leq1$. Splitting $A\cup B=A\mathbin{\dot\cup}(B\setminus A)$ and $B=(A\cap B)\mathbin{\dot\cup}(B\setminus A)$ gives the inclusion-exclusion formula for two events. Equal singleton weights add over $A$ to give $|A|/|\Omega|$ in a finite uniform space.{{cite:durrett2019}} (Ch. 1, §1.1, probability-measure properties and discrete example)

For increasing $A_n$, let $C_1=A_1$ and $C_n=A_n\setminus A_{n-1}$ thereafter. The $C_n$ are disjoint, $A=\cup_nC_n$, and $A_N=\cup_{n\leq N}C_n$, so countable additivity gives $\Pr(A)=\lim_N\Pr(A_N)$. For decreasing $A_n$, apply this result to $A_1\setminus A_n$, which increases to $A_1\setminus\cap_nA_n$, and subtract from the finite number $\Pr(A_1)$.{{cite:durrett2019}} (Ch. 1, §1.1, continuity theorem)
:::
:::

## Statistical use — Choosing a sample model
A statistical model specifies a probability measure for observations at each parameter value. A Bernoulli model places mass on two outcomes; a normal model assigns probabilities to intervals by integrating a density; a mixture may combine continuous and atomic mass. The measure supplies a coherent answer to every event in the chosen sigma-algebra, including tail events used for tests and coverage events used for confidence procedures. A model can satisfy all axioms yet fit the physical experiment poorly; coherence of probabilities and adequacy of a particular model are different questions.{{cite:durrett2019}} (Ch. 1, §§1.1–1.2, pp. 1–15)

## Worked example
Assign die faces one through six probabilities $(1/12,1/12,1/6,1/6,1/4,1/4)$. They sum to one, so they define a probability measure on all subsets of the six faces. The even-face event has probability $1/12+1/6+1/4=1/2$. The event “at least four” has probability $1/6+1/4+1/4=2/3$. Their intersection is faces four and six, with probability $1/6+1/4=5/12$. Hence the union has probability $1/2+2/3-5/12=3/4$, agreeing with the direct sum over faces two, four, five and six. The subtraction prevents the shared faces from being counted twice.{{cite:durrett2019}} (Ch. 1, §1.1, discrete probability measure and additivity)

**Your turn.** For the same loaded die, let $A$ be an odd face and $B$ a face below four. Find $\Pr(A)$, $\Pr(B)$, $\Pr(A\cap B)$ and $\Pr(A\cup B)$.

::: {.callout-tip collapse="true" title="Answer"}
Odd faces one, three and five have probability $1/12+1/6+1/4=1/2$. Faces one, two and three have probability $1/12+1/12+1/6=1/3$. The intersection is faces one and three, with probability $1/12+1/6=1/4$. Thus $\Pr(A\cup B)=1/2+1/3-1/4=7/12$, matching the direct sum for faces one, two, three and five.{{cite:durrett2019}} (Ch. 1, §1.1, finite additivity)
:::

## Common misconceptions
The axioms do not say all outcomes are equally likely; the loaded-die weights satisfy them. Disjoint events and independent events are different: disjoint positive-probability events cannot be independent. A probability-zero event can still be a possible outcome in a continuous model, such as one exact real value under a normal law. The measure is defined on the event sigma-algebra, so saying it assigns a number to *every conceivable subset* overstates its domain on general spaces.{{cite:durrett2019}} (Ch. 1, §§1.1–1.2, pp. 1–3, 10–15)

## Assumptions and limits — When an assignment is not a measure
Assigning probability zero to every positive integer singleton but probability one to their union, the whole positive-integer sample space, violates countable additivity. Assigning $\Pr(\{1\})=0.1$, $\Pr(\{2\})=0.2$ and $\Pr(\{1,2\})=0.6$ violates even finite additivity. Conversely, a mathematically valid fair-die measure is a poor model for a visibly weighted die. These cases separate axiomatic inconsistency from empirical model misspecification.{{cite:durrett2019}} (Ch. 1, §1.1, additivity and discrete weights)

## Connections
A [probability space](probability-space.qmd) packages the outcome set, event sigma-algebra and measure. [Events](event.qmd) are the measurable sets receiving probabilities; [countable additivity](countable-additivity.qmd) is the defining limit rule. A [random variable](random-variable.qmd) sends the original measure to a distribution on its value space, so its CDF and density, when present, are representations of that induced measure.{{cite:durrett2019}} (Ch. 1, §§1.1–1.2, pp. 1–3, 10–11)

## History
Kolmogorov's 1933 monograph organized probability using measure-theoretic axioms; Dodge's biographical entry records the publication, and Durrett's modern text states the normalized countably additive definition. The framework lets finite counting examples and continuous distributions use the same event rules without assuming equal likelihood of elementary outcomes.{{cite:dodge2008}} (p. 282, Kolmogorov entry){{cite:durrett2019}} (Ch. 1, §1.1, pp. 1–3)
