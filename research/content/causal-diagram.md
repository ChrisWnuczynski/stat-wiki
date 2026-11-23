## Lead context

A causal diagram is a drawing of assumptions. Its nodes are variables, its
arrows are claimed direct causes, and — just as importantly — its missing
arrows are claimed absences of direct causation. Hernán and Robins introduce causal diagrams as the tool for
making qualitative expert knowledge and prior assumptions about a causal
structure explicit, on the principle that investigators should draw their
assumptions before they draw their conclusions
{{cite:hernan_robins2020}} (Ch. 6, §6.1, p. 75).

The payoff is discipline about a question associational reasoning answers
badly: given an exposure $A$ and an outcome $Y$, which other variables
should be conditioned on — stratified on, adjusted for, or restricted
on — so that the remaining $A$–$Y$ association can be read as an effect
of $A$ on $Y$? The traditional answer, to adjust for whatever is
associated with both exposure and outcome and is not itself affected by
exposure, is demonstrably inadequate: it misses associations that
adjustment itself creates, and can direct the analyst to condition on
exactly the variable that manufactures bias. This article defines the
object, states the rules in words, and works two numerical examples: a
common cause that makes a null effect look large, and a common effect
that makes two independent causes look associated once the analysis
conditions on their effect.

## What a causal diagram is

A causal diagram, in the sense used here, is a directed acyclic graph, or
DAG. It consists of nodes and directed edges. Each node represents a
variable — an exposure, an outcome, a covariate, or a variable nobody has
measured. Each directed edge is an arrow from one node to another,
written here as $X \rightarrow A$ and read as “$X$ is a direct cause of
$A$”, where “direct” means direct relative to the other variables on the
graph: the effect is not mediated through any other variable the diagram
includes. A variable with an arrow into another is its parent; the variable at the head of the arrow is its child 

The graph is *directed* because every edge has a direction, and *acyclic* because no directed path forms a closed loop: following arrows in their direction, one can never return to a node already visited — no variable can cause itself at an instantaneous moment, and the future cannot cause the past {{cite:tennant_etal2021}} (p. 622).

Acyclicity restricts the representation, not nature. Where two variables
genuinely influence each other over time — pain worsening depression,
depression worsening pain — the acyclic representation expands each
construct into time-indexed copies: depression at time 1, pain at time 1,
depression at time 2 and pain at time 2 are distinct nodes, and every
arrow runs from an earlier copy to a later one, as Shrier and Platt note
for repeated measures of one construct {{cite:shrier_platt2008}}
(Background). A cyclic graph is in general shorthand for such an acyclic
graph with time-specific measurements {{cite:greenland_pearl_robins1999}}
(pp. 46–47).

Formally, Hernán and Robins define a DAG as a graph whose nodes are
random variables $V = (V_1, \dots, V_M)$ with directed edges and no
directed cycles, and a *causal* DAG by three further conditions: the lack
of an arrow is interpreted as the absence of a direct causal effect,
relative to the other variables on the graph; all common causes of any
pair of variables on the graph, even unmeasured ones, are themselves on
the graph; and any variable is a cause of its descendants
{{cite:hernan_robins2020}} (Ch. 6, Technical Point 6.1, p. 76). The
second condition is easy to miss: an unmeasured common cause belongs on
the diagram, drawn as an unmeasured node, because leaving it off would
assert falsely that the variables it causes share no such cause.

## Reading an arrow, and reading a missing arrow

An arrow and a missing arrow assert very different strengths of claim.
The presence of an arrow $X \rightarrow Y$ asserts that $X$ has a direct
causal effect on $Y$ — an effect not mediated through any other variable
on the graph — for at least one individual
{{cite:hernan_robins2020}} (Ch. 6, §6.1, p. 75). It asserts nothing else:
not whether the effect is harmful or protective, large or negligible,
linear or nonlinear, and not how $X$ interacts with any other cause of
$Y$, since a standard causal diagram does not distinguish whether an
arrow represents a harmful or a protective effect and does not encode
how two causes of one variable interact {{cite:hernan_robins2020}}
(Ch. 6, §6.1, p. 75).

The absence of an arrow asserts much more: that $X$ has no direct causal
effect on $Y$ for any unit. Every absence of a single-headed arrow is a
basic null, or no-direct-effect, assumption encoded by the graph, and
implies the absence of every effect that would have been transmitted
through that arrow {{cite:greenland_pearl_robins1999}} (p. 39). Tennant
and colleagues state the asymmetry as a reporting rule: omitting an arc
implies precisely no causal effect, a much stronger assumption than
including an arc, which allows an effect of any sign, magnitude or
parametric form, including a very small one {{cite:tennant_etal2021}}
(p. 629). A sparse diagram is therefore not a modest diagram: it makes
one strong null claim for every ordered pair of nodes it declines to
connect, whereas a dense diagram makes few claims at all.

The same logic governs whole routes. A *directed path* from $X$ to $Y$
is a sequence of arrows all pointing the same way, such as
$X \rightarrow M \rightarrow Y$; it is also called a causal path. If a
directed path runs from $X$ to $Y$, then $X$ is an *ancestor* of $Y$ and
$Y$ is a *descendant* of $X$. Producing an effect requires a causal path,
so the absence of any directed path from $X$ to $Y$ is the assumption
that $X$ has no effect on $Y$ through any route the diagram contains
{{cite:greenland_pearl_robins1999}} (p. 39). “Direct” is relative to the
variable set drawn: adding a mediator would split one arrow into two
without changing the underlying claim
{{cite:greenland_pearl_robins1999}} (pp. 38–39).

## Paths, and the three elementary structures

A *path* between two nodes is any unbroken route traced along edges, whether with or against the arrows — $A \leftarrow X \rightarrow Y$, for example. Paths, not individual arrows, are the unit of associational reasoning. Every path is built from three elementary three-node structures.

The first is the *chain*, $A \rightarrow M \rightarrow Y$, in which $M$
lies on a causal path from $A$ to $Y$ and is a mediator of the effect of
$A$ on $Y$. Association flows along the chain, and conditioning on the
middle node interrupts the flow: within a stratum of $M$, the part of the
$A$–$Y$ association transmitted through $M$ is removed, because $M$ no
longer varies to carry it. The second is the *fork*,
$A \leftarrow X \rightarrow Y$, in which $X$ is a common cause of $A$ and
$Y$. Association flows along the fork for a non-causal reason — units with
high $X$ tend to have both higher $A$ and higher $Y$ — which is the
graphical form of a [confounding variable](confounding-variable.qmd).
Conditioning on the middle node, the common cause itself, blocks the
flow: within strata of $X$ the fork transmits no association. The third
is the *collider*, $A \rightarrow C \leftarrow Y$, in which $C$ is a
common effect of $A$ and $Y$ and the two arrows collide at $C$. The
collider behaves in exactly the opposite way. Unconditionally it
transmits no association at all: the path through $C$ is blocked by
default, and $A$ and $Y$ may be perfectly independent marginally.
Conditioning on the collider — or on any descendant of it — *opens* the
path and creates an association between its causes that was not there
before.

Hernán and Robins summarise the three structures in one sentence: two variables may be associated because one causes the other, because they share common causes, or because they share a common effect and the analysis is restricted to some level of that effect or of its descendants {{cite:hernan_robins2020}} (Ch. 6, §6.3, pp. 80–81). Chance is a fourth, non-structural reason, set aside here.

## d-separation: when a path is blocked

The rules generalise to paths of any length through d-separation, where
the “d” stands for directional {{cite:greenland_pearl_robins1999}}
(p. 45). Fix two variables and a set $S$ being conditioned on. A path
between them is *blocked* by $S$ if either of two things happens along
it. The path contains a chain or a fork whose middle node is in $S$:
conditioning on a non-collider blocks the path, because within strata of
that node the segment transmits no further association. Or the path
contains a collider that is not in $S$ and has no descendant in $S$: an
unconditioned collider blocks by default. If neither happens — every
non-collider on the path is unconditioned, and every collider is
conditioned on, directly or through a descendant — the path is *open* and
can transmit association. Two variables are *d-separated* by $S$ if every
path between them is blocked by $S$. Hernán and Robins state the four
component rules explicitly: a path with an unconditioned collider is
blocked; a path with a conditioned non-collider is blocked; a conditioned
collider does not block; and a collider with a conditioned descendant
does not block — in sum, a path is blocked if and only if it contains a
conditioned non-collider, or a collider that has not been conditioned on
and has no conditioned descendants {{cite:hernan_robins2020}} (Ch. 6,
Fine Point 6.1, p. 82).

D-separation is the graphical counterpart of conditional independence: if
$S$ d-separates two variables, then under the diagram’s assumptions they
are unassociated within strata of $S$
{{cite:greenland_pearl_robins1999}} (p. 45). The converse needs care. An
open path *allows* association but does not guarantee it, because
associations along different open paths can in principle cancel — an
effect hidden by confounding of the opposite sign is the standard example
{{cite:greenland_pearl_robins1999}} (p. 40). Logically, d-separation implies independence, while independence in data does not imply d-separation in the true diagram.

## Backdoor paths and the backdoor criterion

Fix an exposure $A$, an outcome $Y$, and the total effect of $A$ on $Y$ —
the effect transmitted along all directed paths from $A$ to $Y$, the
contrast at the heart of [causality](causality.qmd) and the
[average treatment effect](average-treatment-effect.qmd). Any other path
between $A$ and $Y$ is a potential source of non-causal association. A
*backdoor path* from $A$ to $Y$ is a path between them that begins with
an arrow into $A$: its first step, leaving $A$, travels against an
arrowhead, along an edge of the form $A \leftarrow \cdots$. Greenland,
Pearl and Robins define it in exactly those terms — a path connecting $X$
to $Y$ is a backdoor path from $X$ to $Y$ if it has an arrowhead pointing
to $X$ {{cite:greenland_pearl_robins1999}} (p. 39). The causal effect
leaves $A$ through the front door, along arrows out of $A$; a backdoor
path sneaks association into $A$ from behind, through whatever causes
$A$, and carries it on to $Y$.

The simplest backdoor path is the fork $A \leftarrow X \rightarrow Y$.
Longer ones thread through several variables and may contain colliders,
which is why some backdoor paths are already blocked — by an
unconditioned collider on them — and transmit nothing unless the analyst
conditions on that collider or its descendant and opens them.
Confounding, in graphical language, is the presence of an open backdoor
path: in Hernán and Robins’ heart transplant example there is confounding
because treatment and outcome share the cause $L$, disease severity — an
open backdoor path through $L$, blocked by conditioning on $L$
{{cite:hernan_robins2020}} (Ch. 7, §7.3, p. 95).

The *backdoor criterion* states precisely when a set of variables removes
the problem. Let $S$ be a set of variables, and the target the total
effect of $A$ on $Y$. Then $S$ satisfies the backdoor criterion for
$(A, Y)$ if: (i) no variable in $S$ is a descendant of $A$; and (ii) $S$
blocks every backdoor path from $A$ to $Y$ — every path beginning with an
arrow into $A$ is blocked given $S$, counting both paths blocked by
conditioning on non-colliders in $S$ and any paths opened by conditioning
on colliders in $S$ or their descendants. When $S$ satisfies the
criterion, conditioning on $S$ makes the treated and untreated
exchangeable within levels of $S$, and the conditional association,
standardised over the distribution of $S$, gives the effect. Hernán and
Robins state the sufficient-set version: a set of measured
non-descendants of $A$ is a sufficient set for confounding adjustment
when conditioning on it blocks all backdoor paths, so that the treated
and the untreated are exchangeable within its levels
{{cite:hernan_robins2020}} (Ch. 7, §7.3, p. 94).

Neither clause is redundant. Clause (i) excludes mediators, such as $M$
in $A \rightarrow M \rightarrow Y$ — conditioning on a mediator blocks
part of the very effect being estimated — and post-exposure colliders
whose conditioning can open non-causal paths. Clause (ii) is stronger
than “block the confounders”: it requires blocking *every* backdoor path,
including paths that conditioning itself would open. Greenland, Pearl and
Robins give the equivalent criteria in their earlier form: a set $S$ of
non-descendants of exposure and outcome is sufficient if every unblocked
backdoor path is intercepted by a variable in $S$, and every unblocked
path *induced by adjustment* for $S$ is also intercepted by a variable in
$S$ {{cite:greenland_pearl_robins1999}} (pp. 43–44). The second criterion
is the addition naive reasoning misses; their central example is a set —
adjustment for an intermediate variable alone — that intercepts the
original paths but fails, because conditioning on it associates two
previously independent causes and creates a new open backdoor path around
it {{cite:greenland_pearl_robins1999}} (pp. 40–41, 43–44).

A sufficient set need not be unique, and minimally sufficient sets —
sufficient sets no proper subset of which is sufficient — need not
overlap at all {{cite:greenland_pearl_robins1999}} (p. 44): “the
confounders”, as a canonical list, is not a notion the theory supports.
Bigger is not safer either: adding a variable to a sufficient set can
destroy its sufficiency, by opening a collider path or blocking a causal
path {{cite:greenland_pearl_robins1999}} (p. 44). And the criterion is
silent about magnitude: an unblocked path may be weak, and several strong
paths may bias in opposite directions and nearly cancel
{{cite:hernan_robins2020}} (Ch. 7, §7.3, p. 95). It settles
identification, not the importance of getting it wrong.

When no measured set satisfies the criterion, the effect is not
identified by adjustment: the honest options are to measure more, change
the design, or use a method built on a different assumption. An
[instrumental variable](instrumental-variable.qmd) replaces blocking
every backdoor path with an exclusion and independence structure of its
own. A second route, mentioned briefly because its conditions are rarely available, is the front-door criterion: if the entire effect of $A$ on $Y$ is mediated by a variable $M$ sharing no unmeasured causes with either $A$ or $Y$, the counterfactual risk is identified by the front-door formula even though $A$ and $Y$ share an unmeasured cause whose backdoor path cannot be blocked, because identification runs forwards through the mediator rather than backwards through the confounder {{cite:hernan_robins2020}} (Ch. 7, Technical Point 7.4, p. 107).

## Colliders, conditioning, and selection bias

Return to $A \rightarrow C \leftarrow Y$, with $A$ and $Y$ marginally
independent, and now condition on $C$ — restrict to one level of it,
stratify on it, match on it, or model it. Shrier and Platt’s homely version is rain and sprinklers, which both cause a wet field: conditional on the field being wet, knowing the sprinklers were off raises the probability that it rained {{cite:shrier_platt2008}} (Step 4). The child in such a structure is
called a collider because the two arrows collide at the node, and
conditioning on the child, or on an effect of the child, creates a
conditional association between its parents {{cite:shrier_platt2008}}
(Step 4).

Conditioning on a descendant of the collider does the same, usually more
weakly: restricting to a level of a consequence of $C$ is partial
information about $C$, and partial information opens the path partially.
Hernán and Robins add a medication caused by heart disease to their
collider diagram: the two causes of heart disease are associated within
levels of the medication too, because conditioning on a variable affected
by a collider also opens the path {{cite:hernan_robins2020}} (Ch. 6,
§6.3, p. 81). Hence “we did not adjust for the collider itself” is no
defence: selection into a study, response, or survival to recruitment is
typically a descendant of its causes, and analysing the selected sample
at all can be conditioning on such a descendant.

That observation reorganises the taxonomy of bias. In the structural
approach Shrier and Platt adopt, biases divide into two graphical kinds:
confounding bias, from failing to condition on a common cause, and
selection bias, from conditioning on a common effect
{{cite:shrier_platt2008}} (Discussion). Berkson’s bias is the canonical instance: two diseases
independent in the general population both affect hospital admission, so
among admitted patients — the stratum defined by the common effect — the
diseases are associated, and an inpatient-only study may mistake that
association for a fact about the diseases. Recognising it as biased requires the diagram for the entire population; nothing in the hospital data alone announces that selection manufactured it {{cite:greenland_pearl_robins1999}} (p. 41).

The symmetric failure also exists: where exposure and outcome share no common cause, conditioning on a common effect of the two biases a clean comparison — Greenland, Pearl and Robins’ instance is stratifying on uterine bleeding, caused by both oestrogen and endometrial cancer, in studies of oestrogen and endometrial cancer, where adjustment for the common effect was irremediably harmful {{cite:greenland_pearl_robins1999}} (pp. 42–43).

## Worked example: a fork that fakes an effect, and a collider that fakes an association

Both examples use populations, not samples, so every proportion is exact
and no sampling variation obscures the arithmetic.

**(a) The fork.** A population of $400$ is divided by a binary variable
$X$ into two groups of $200$. The diagram, in words, has nodes $X$, $A$
and $Y$ and edges $X \rightarrow A$, $X \rightarrow Y$ and
$A \rightarrow Y$: $X$ is a common cause of exposure $A$ and outcome $Y$,
and the question is the effect of $A$ on $Y$. The only backdoor path is
$A \leftarrow X \rightarrow Y$, and $\{X\}$ satisfies the backdoor
criterion. The counts are constructed so that $A$ in fact has no effect.
Where $X = 0$, $50$ of the $200$ people have $A = 1$ and $150$ have
$A = 0$; the outcome occurs in $10$ of the $50$ with $A = 1$ and in $30$
of the $150$ with $A = 0$, a risk of $1/5$ in both groups. Where $X = 1$,
$150$ have $A = 1$ and $50$ have $A = 0$; the outcome occurs in $120$ of
the $150$ with $A = 1$ and in $40$ of the $50$ with $A = 0$, a risk of
$4/5$ in both groups. Stratum by stratum the risk difference is
$1/5 - 1/5 = 0$ and $4/5 - 4/5 = 0$. There is nothing to find.

Pool the groups and an effect appears. In total $200$ people have
$A = 1$, of whom $10 + 120 = 130$ have the outcome, a crude risk of
$130/200 = 13/20$; $200$ people have $A = 0$, of whom $30 + 40 = 70$ have
the outcome, a crude risk of $70/200 = 7/20$. The crude risk difference
is $13/20 - 7/20 = 3/10$. The entire $3/10$ is the fork at work: the exposed group is drawn disproportionately from $X = 1$ ($150$ of its $200$ members), where the outcome is common for reasons unrelated to $A$. Standardising over $X$ with weights $1/2$ and $1/2$ gives a risk under exposure of $(1/2)(1/5) + (1/2)(4/5) = 1/2$ and under no exposure of $(1/2)(1/5) + (1/2)(4/5) = 1/2$ — an adjusted difference of $0$, the truth the backdoor criterion predicted before any numbers were computed.

**(b) The collider.** A population of $400$ has two binary causes, $A$
and $B$, independent of each other: each combination $(A, B) = (0, 0)$,
$(1, 0)$, $(0, 1)$ and $(1, 1)$ occurs in exactly $100$ people.
Marginally, the risk of $B = 1$ is $200/400 = 1/2$ given $A = 1$ and
$200/400 = 1/2$ given $A = 0$, and the marginal odds ratio is $1$. The
diagram, in words, has nodes $A$, $B$ and $C$ and edges
$A \rightarrow C$ and $B \rightarrow C$, with no edge between $A$ and
$B$: $C$ is a common effect, a collider on the only path between $A$ and
$B$. Let $C = 1$ whenever at least one of $A$ and $B$ equals $1$, and
$C = 0$ only when both equal $0$ — admission, say, triggered by either of
two independent conditions.

Condition on $C = 1$, as a study recruited through admission would: only
$300$ people remain. The table of $A$ against $B$ within $C = 1$ is:

|  | $B = 1$ | $B = 0$ | Total |
|---|---:|---:|---:|
| $A = 1$ | $100$ | $100$ | $200$ |
| $A = 0$ | $100$ | $0$ | $100$ |
| Total | $200$ | $100$ | $300$ |

The bottom-right cell is empty by construction: nobody with $A = 0$ and
$B = 0$ has $C = 1$. Within the selected population the risk of $B = 1$
is $100/200 = 1/2$ given $A = 1$ but $100/100 = 1$ given $A = 0$, a risk
difference of $1/2 - 1 = -1/2$, and the odds ratio is
$(100 \times 0)/(100 \times 100) = 0$. Two variables exactly independent
in $400$ people are as strongly negatively associated as a $2 \times 2$
table permits: among the selected, knowing $A = 0$ settles $B = 1$ with
certainty. The association is a pure artefact of conditioning on their
common effect — the arithmetic inside Berkson’s bias, with selection made
deterministic so the fractions stay simple.

## Your turn

A second fork, with a genuine effect. A population of $400$ is divided by
a common cause $X$ into two groups of $200$, with edges
$X \rightarrow A$, $X \rightarrow Y$ and $A \rightarrow Y$. Where
$X = 0$, $40$ people have $A = 1$, of whom $20$ have the outcome, and
$160$ have $A = 0$, of whom $40$ have the outcome. Where $X = 1$, $160$
people have $A = 1$, of whom $120$ have the outcome, and $40$ have
$A = 0$, of whom $20$ have the outcome. Compute the risk difference
within each stratum of $X$, the crude risk difference, and the risk
difference standardised over $X$ with weights $1/2$ and $1/2$. Which
number is the effect of $A$ on $Y$?

::: {.callout-tip collapse="true" title="Answer"}

Within $X = 0$ the risks are $20/40 = 1/2$ under $A = 1$ and
$40/160 = 1/4$ under $A = 0$, a difference of $1/4$. Within $X = 1$ the
risks are $120/160 = 3/4$ and $20/40 = 1/2$, again $1/4$. Crudely, $200$
people have $A = 1$ with $20 + 120 = 140$ outcomes, a risk of
$140/200 = 7/10$, and $200$ have $A = 0$ with $40 + 20 = 60$ outcomes, a
risk of $60/200 = 3/10$, so the crude difference is $7/10 - 3/10 = 2/5$.
Standardising gives $(1/2)(1/2) + (1/2)(3/4) = 5/8$ under $A = 1$ and
$(1/2)(1/4) + (1/2)(1/2) = 3/8$ under $A = 0$, a difference of $1/4$. The
standardised difference is the effect: it agrees with both within-stratum
differences, as it must when $\{X\}$ satisfies the backdoor criterion.
The crude $2/5$ overstates the effect by $2/5 - 1/4 = 3/20$.

## A diagram is an assumption, not a discovery

Everything above is conditional on the diagram itself. A DAG does not
summarise data; it states, in advance of the data, what the analyst is
prepared to assume about the structure that generated them. Greenland,
Pearl and Robins are explicit that no approach solves the problem of
inferring causation from observational data, because all causal inference
rests on assumptions that cannot be derived from observations alone;
graphs can only convey those assumptions and indicate what measurements
are sufficient for adjustment, given them
{{cite:greenland_pearl_robins1999}} (p. 47). Shrier and Platt answer the obvious objection — how can one know the true structure in order to draw the DAG? — by noting that the structure exists whether or not it is drawn, and that the DAG approach simply makes the assumptions explicit {{cite:shrier_platt2008}} (Limitations).

A diagram should therefore be argued about, varied and reported. Where
evidence does not settle a contested arrow, Shrier and Platt recommend
drawing each plausible diagram, checking whether the same adjustment set
is sufficient under each, and reporting each interpretation if they
differ {{cite:shrier_platt2008}} (Discussion). Tennant and colleagues
turn the same obligations into reporting standards: state the estimand,
make the diagram available, state the adjustment set the diagram implies
— including variables with no available measurement — and report
alternative adjustment sets separately {{cite:tennant_etal2021}}
(pp. 628–629). What a diagram cannot show is as important as what it can. It cannot show
an effect size, a sign, or a functional form: the assumptions are
qualitative and nonparametric, implying nothing about the form of the
relations among the variables, which may be discrete or continuous with
dose–response relations of any shape {{cite:greenland_pearl_robins1999}}
(p. 39). It cannot show interaction between two causes of one node {{cite:shrier_platt2008}} (Discussion). It cannot
show sampling variation or association strength; a negligible arrow and a
decisive one are drawn identically. And it cannot show an unmeasured
variable the analyst has not thought of. One that *is* thought of can and
should be drawn — Tennant and colleagues recommend including all
plausible confounding variables regardless of whether measurements are
available, because depicting unobserved variables highlights potential
sources of unobserved confounding {{cite:tennant_etal2021}} (p. 629) —
but its presence does not make adjustment for it possible; it makes the
resulting non-identification visible, which is the next best thing.

Nor is a diagram a statistical technique: it yields no estimate, only
guidance on which covariates stratification and regression should
condition on {{cite:shrier_platt2008}} (Discussion). Estimation still
requires [potential outcomes](potential-outcomes.qmd), standardisation or
weighting, and positivity and consistency conditions no diagram can
supply.

## Counterfactual graphs in one paragraph: SWIGs

A single-world intervention graph, or SWIG, is obtained from a causal DAG
by splitting the treatment node into the treatment actually received and
the fixed value to which treatment is set, and relabelling every
descendant of treatment with its counterfactual version under that
intervention, so the graph displays counterfactual variables directly.
Hernán and Robins introduce SWIGs as the device unifying the
counterfactual and graphical approaches, with the equivalence that a
counterfactual outcome is d-separated from treatment given $L$ on the
SWIG if and only if $L$ is a non-descendant of treatment blocking all
backdoor paths in the original DAG {{cite:hernan_robins2020}} (Ch. 7,
§7.5, pp. 101–102). ## Statistical use, assumptions and limits

## Statistical use, assumptions and limits

At the design stage the diagram decides what to measure: any variable on
a backdoor path the analyst hopes to block must be measured, or
identification fails before the data arrive. At the analysis stage it
decides what to condition on, through the backdoor criterion applied to
the stated estimand — the total effect, or a direct effect, whose
adjustment set is a different and deliberate object, as
[mediation analysis](mediation-analysis.qmd) discusses. A
[propensity score](propensity-score.qmd) is not an alternative to the
diagram but an implementation of it: whether conditioning on a score
recovers an effect depends on whether the set it is built from satisfies
the backdoor criterion, a question the score cannot answer.

The assumptions, collected, are: the diagram is right in its arrows and, more demandingly, in its missing arrows; all common causes are on the graph; nothing is conditioned on without checking what that conditioning does to every path it touches; and the temporal order is the real one. None is testable from the data being analysed, although the independencies implied by a diagram’s d-separations are testable implications whose failure is evidence against it.

## Common misconceptions

**“Adjust for everything associated with exposure and outcome.”**
Association does not reveal position. A variable associated with both may
be a confounder that must be conditioned on, a mediator that must not be
(for a total effect), or a collider whose conditioning creates the
association it is meant to remove. Position, not association, decides.

**“If adding a variable changes the estimate, it was a confounder.”**
Change in estimate is neither necessary nor sufficient: conditioning on a
collider changes an estimate by manufacturing bias, and genuine
confounding can leave an estimate nearly unchanged when opposing paths
cancel.

**“The diagram was learned from the data.”** The diagrams here encode
assumptions supplied by the analyst. Algorithms that search for graphs
compatible with observed independencies rest on further assumptions and
deliver at best a class of compatible diagrams; Greenland, Pearl and
Robins caution that such structure-inference methods are controversial
{{cite:greenland_pearl_robins1999}} (p. 47).

## History

Path diagrams were an integral component of path analysis and structural equation modelling; the modern formal theory came from directed acyclic graphs in expert-systems research {{cite:greenland_pearl_robins1999}} (p. 37). Greenland, Pearl and Robins’ 1999 paper carried the theory into
epidemiology, showing where traditional criteria for confounding fail
when several potential confounders are considered simultaneously, and
supplying the graphical criteria — the backdoor test and d-separation —
that repair them {{cite:greenland_pearl_robins1999}} (pp. 37, 43–45).
Shrier and Platt’s 2008 paper addressed usability, setting out a six-step
algorithm, due to Pearl, for testing whether a proposed covariate set
would reduce or increase bias {{cite:shrier_platt2008}} (Background).
Tennant and colleagues’ 2021 review of $234$ applied articles then
documented wide variation in whether diagrams, estimands and implied
adjustment sets were reported at all, and converted the theory’s
obligations into eight recommendations for transparent reporting
{{cite:tennant_etal2021}} (pp. 620–621, 628–629).

## Connections

- [Confounding variable](confounding-variable.qmd) — the common cause:
  the fork, and the open backdoor path that conditioning on $X$ blocks.
- [Causality](causality.qmd) — the contrast a diagram serves: which
  conditional association, if any, equals the causal contrast.
- [Average treatment effect](average-treatment-effect.qmd) — a common
  target estimand, identified by adjustment when the backdoor criterion
  holds.
- [Potential outcomes](potential-outcomes.qmd) — the counterfactual
  formulation that SWIGs merge with the graphical one.
- [Propensity score](propensity-score.qmd) — a dimension-reduction device
  built from an adjustment set the diagram must first license.
- [Instrumental variable](instrumental-variable.qmd) — identification
  when no measured set satisfies the backdoor criterion.
- [Mediation analysis](mediation-analysis.qmd) — the deliberate
  conditioning on a mediator that the total-effect criterion forbids.
- [Structural equation modelling](structural-equation-modelling.qmd) —
  the older path-diagram tradition, and the nonparametric structural
  equations whose qualitative skeleton a causal diagram is.

## Check yourself

1. A diagram contains only the edges $A \rightarrow M$, $M \rightarrow Y$ and $A \rightarrow Y$. A colleague proposes estimating the total effect of $A$ on $Y$ by conditioning on $M$, because $M$ is strongly associated with both $A$ and $Y$. What is wrong with the proposal?

::: {.callout-tip collapse="true" title="Answer"}

$M$ is a mediator: it lies on the directed path $A \rightarrow M
\rightarrow Y$, so it is a descendant of $A$. The backdoor criterion
forbids descendants of $A$ in an adjustment set for the total effect, and
conditioning on $M$ blocks the part of the effect transmitted through
$M$, leaving at most a direct-effect contrast. No path from $A$ to $Y$ in
this diagram begins with an arrow into $A$, so the empty set satisfies
the backdoor criterion and the crude association is the total effect.

:::

2. Two variables $A$ and $B$ are independent in a population. Both cause
$C$, and a study is restricted to people with $C = 1$. In the worked
collider example, what were the risks of $B = 1$ given $A = 1$ and given
$A = 0$ within $C = 1$, and what created the difference?

::: {.callout-tip collapse="true" title="Answer"}

Within $C = 1$ the risk of $B = 1$ was $100/200 = 1/2$ given $A = 1$ and
$100/100 = 1$ given $A = 0$. Conditioning on the collider $C$ opened the
path $A \rightarrow C \leftarrow B$, which is blocked when $C$ is not
conditioned on. Because $C = 1$ requires at least one of its causes to be
present, the absence of $A$ forces the presence of $B$ in that example;
the association is created entirely by the restriction, and is an
instance of selection, or Berkson-type, bias.

:::

3. An analyst draws the fork diagram of the worked example, with common cause $X$, and adjusts for $X$. A reviewer objects that the diagram might be wrong, so the adjustment proves nothing. Is the reviewer right?

::: {.callout-tip collapse="true" title="Answer"}

The reviewer is right that the conclusion is conditional, and wrong if
they mean the analysis is therefore empty. Every causal analysis rests on
assumptions the data alone cannot supply; the diagram states them exactly
— here, that $X$ is the only common cause and that no omitted arrow
exists. Given the diagram, $\{X\}$ satisfies the backdoor criterion, so
the adjusted association is the effect; if the diagram is wrong the
conclusion can fail, and the diagram tells the reviewer precisely which
missing arrow or omitted common cause to propose. The remedy is to argue
about, vary and report the diagram, not to discard it for unstated
assumptions of the same kind.

:::
