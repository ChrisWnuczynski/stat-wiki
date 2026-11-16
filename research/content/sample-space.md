## Motivating example
Drawing two balls from a bag can be recorded as an ordered pair of labelled balls, an ordered pair of colours, or simply the number of red balls. Each choice asks a different question about the same physical draw. A sample space fixes which outcome is recorded before any probability is assigned; choosing it carefully prevents a count of colour descriptions from being mistaken for a count of equally likely draws.{{cite:siegrist2022_random_experiments}} (§2.1, Experiments){{cite:siegrist2022_events}} (§2.2, Sample Spaces)

## Intuition — Outcomes before events
An outcome is one complete result at the chosen level of detail, while an event is a collection of outcomes. For a die whose face is recorded, $\Omega=\{1,2,3,4,5,6\}$ and “even” is the event $\{2,4,6\}$. If only parity is recorded, the sample space can instead be $\{\text{even},\text{odd}\}$. Those two spaces describe the same experiment at different resolutions; neither carries probabilities until a model supplies them.{{cite:siegrist2022_events}} (§2.2, The Set of Outcomes; Events)

## Definition
A probability model adds a collection $\mathcal F$ of admissible events and a probability measure $P$ to the outcome set $\Omega$. On a finite sample space one commonly takes every subset as an event. For a continuous space, a sigma-algebra of measurable subsets is needed so that complements and countable unions of events are events; arbitrary subsets need not be measurable. The triple $(\Omega,\mathcal F,P)$ is a probability space, while “sample space” often refers just to $\Omega$ in elementary discussion.{{cite:siegrist2022_events}} (§2.2, Sample Spaces; Events)

## Properties
When a finite space has $N$ equally likely elementary outcomes, an event containing $k$ outcomes has probability $k/N$. The equal-likelihood condition is part of the model, not a consequence of the set notation. The four counting rules listed above require us to decide whether order matters and whether replacement occurs. For two ordered draws without replacement from $m$ labelled objects there are $m(m-1)$ possible pairs; recording an unordered pair gives $\binom m2$ possibilities instead.{{cite:siegrist2022_events}} (§2.2, Sample Spaces; Examples and Applications)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose $\Omega=\{\omega_1,\ldots,\omega_N\}$ and all singleton outcomes have the same probability $p$. Because the singletons partition $\Omega$, finite additivity and $P(\Omega)=1$ give $Np=1$, hence $p=1/N$. If $A$ contains $k$ of them, its disjoint-singleton decomposition gives $P(A)=kp=k/N$. The formula fails as a counting shortcut when the elementary outcomes have unequal probabilities.{{cite:siegrist2022_events}} (§2.2, Events; The Algebra of Events)
:::
:::

## Statistical use
A data record is often a function of a finer outcome. In [Three cards in order](../questions/ex-prob-three-cards.qmd), the card labels and draw order define the equally likely elementary outcomes. In [The sum of two dice](../questions/ex-prob-dice-sum-pmf.qmd), the ordered pair is the outcome and the sum is a random variable on that space. Their answers count or combine outcomes before assigning probabilities to the recorded summary. This distinction also matters when likelihoods are built from coarsened or aggregated data.{{cite:siegrist2022_events}} (§2.2, Random Variables; Examples and Applications)

## Worked example
A bag has three labelled red balls and two labelled blue balls. Draw two without replacement and record their order. There are $5\cdot4=20$ equally likely ordered pairs. The event “one red and one blue” has $3\cdot2$ red-then-blue pairs and $2\cdot3$ blue-then-red pairs, hence $12$ pairs and probability $12/20=0.6$. If only the ordered colours are recorded, the four outcomes $RR,RB,BR,BB$ have probabilities $0.3,0.3,0.3,0.1$ respectively. Treating those four colour outcomes as equally likely would give the wrong answer.{{cite:siegrist2022_events}} (§2.2, Sample Spaces; Examples and Applications)

**Your turn.** For the same bag and draw, record only the number $R$ of red balls. What is its sample space, and what probabilities belong to its outcomes?

::: {.callout-tip collapse="true" title="Answer"}
The possible values are $\{0,1,2\}$. Both blue has $2\cdot1=2$ ordered pairs, so $P(R=0)=2/20=0.1$. One of each colour has $12$ pairs, so $P(R=1)=12/20=0.6$. Both red has $3\cdot2=6$ pairs, so $P(R=2)=6/20=0.3$. The probabilities sum to one; the three counts are not equally likely.{{cite:siegrist2022_events}} (§2.2, Random Variables; Examples and Applications)
:::

## Common misconceptions
The sample space is the set of possible outcomes, not the observed sample of data from repeated experiments. An event such as “at least one red” is a subset of that space, not necessarily one elementary outcome. Equal likelihood of labelled draws does not imply equal likelihood of their summaries: the number of heads in three fair tosses has four possible values but its middle values have more underlying sequences. Finally, changing the sample space does not change a physical probability when the induced event weights are transferred correctly.{{cite:siegrist2022_events}} (§2.2, Sample Spaces; Random Variables)

## Assumptions and limits
The bag calculation assumes each labelled ball is equally likely at the first draw and each remaining ball equally likely at the second. A mechanism that makes a heavy ball easier to draw breaks the $1/20$ weight even though the set of possible pairs stays the same. If a model leaves out a possible outcome, such as a die landing on an edge when that can occur, its sample space and assigned probabilities do not describe the actual experiment. For continuous outcomes, counting points cannot replace integration: every exact point can have probability zero while an interval has positive probability.{{cite:siegrist2022_events}} (§2.2, Sample Spaces; Geometric Models)

## Connections
The [event](event.qmd) page explains how subsets express claims about outcomes, and [probability measure](probability-measure.qmd) assigns their weights. A [random variable](random-variable.qmd) maps outcomes to numerical summaries, often creating a coarser distribution. [Equally likely outcomes](equally-likely-outcomes.qmd) justifies finite counting after symmetry is established; [four ways of counting draws](four-ways-of-counting-draws.qmd) handles order and replacement. These choices should be settled before a numerical probability is calculated.{{cite:siegrist2022_events}} (§2.2, Sample Spaces; Random Variables)

## History
Finite games of chance supplied early examples of sample spaces that could be counted outcome by outcome. Kolmogorov's 1933 measure-theoretic formulation made the outcome set, a family of events, and a normalized probability measure the foundation for much broader models, including infinite spaces. This formalization explains why the event family becomes explicit when a simple list of outcomes is no longer sufficient.{{cite:vovk_shafer2003_kolmogorov}} (§§1–2, pp. 21–24){{cite:dodge2008}} (p. 467, “Sample Space”)
