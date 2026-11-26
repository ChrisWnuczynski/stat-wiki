## Lead context

The Dirichlet process is a prior distribution over probability
distributions. Where an ordinary Bayesian model places a prior on a
finite-dimensional parameter — a mean, a coefficient, a vector of
category probabilities — a Dirichlet process prior places a prior on
the unknown distribution $G$ itself, and observations are modelled as
drawn from $G$. The prior is specified by a probability
distribution $G_0$, the base measure, which is the prior mean of $G$,
and a positive number $\alpha$, the concentration parameter, which
controls how tightly $G$ concentrates around $G_0$. The framework is
the founding example of Bayesian nonparametrics. Ferguson introduced
the process in 1973, setting two requirements for such a prior: its
support should be large, and its posterior given a sample should be
manageable analytically {{cite:ferguson1973}} (p. 209).

Three facts organise what follows. First, the process is defined by a
consistency requirement: on every finite partition, the random cell
probabilities follow a [Dirichlet distribution](dirichlet-distribution.qmd)
with parameters determined by $G_0$ and $\alpha$. Second, a draw from
a Dirichlet process is discrete with probability one, even when $G_0$
is continuous — a theorem, not an approximation. Third, the prior is
conjugate: the posterior of $G$ given a sample is again a Dirichlet
process, with parameters combining $G_0$ with the empirical
distribution {{cite:ferguson1973}} (Theorem 1, pp. 217–218).

## Motivating example — Why a prior on distributions?

Consider estimating an unknown distribution from a sample, without
assuming it belongs to a named family. A Bayesian answer requires a
probability distribution over the candidate distributions, so that
Bayes' rule can update it in the light of the sample. Ferguson states
the difficulty directly: in nonparametric problems the parameter space
is a set of probability distributions, and workable priors on such a
space were hard to find.
His two desirable properties were that "(I) The support of the prior
distribution should be large — with respect to some suitable topology
on the space of probability distributions on the sample space" and that
"(II) Posterior distributions given a sample of observations from the
true probability distribution should be manageable analytically"
{{cite:ferguson1973}} (p. 209). The properties pull in opposite
directions: a prior diffuse enough to reach every plausible
distribution usually has an uncomputable posterior, and a prior chosen
for convenience excludes most distributions in advance.

The Dirichlet process was designed to satisfy both. Property (II) is
delivered by the conjugacy proved below. Property (I) holds in this
sense: for any fixed probability measure $Q$ absolutely continuous with
respect to the parameter measure, and any finite collection of sets,
$G$ falls within any stated tolerance of $Q$ on all of them
simultaneously with positive probability {{cite:ferguson1973}} (Proposition 3, pp. 215–216). On the real line,
with the topology of convergence in distribution, the support is all
probability measures supported inside the support of the base measure
{{cite:ferguson1973}} (pp. 215–216). A base measure with full support
thus gives a prior supported on the whole space of distributions: no
shape is excluded in advance. What the prior does exclude, with
probability one, is continuity of the drawn distribution itself.

This is the sense in which the process is nonparametric: the parameter,
$G$, is infinite-dimensional, and a fitted model's effective complexity
— the number of distinct values or components in use — grows with the
sample size rather than being fixed in advance, provided $G_0$ has
infinite support. If $G_0$ is carried by finitely many points, the
picture collapses to the finite analogue: $G$ is then a
Dirichlet-distributed weight vector on those points, and the number of
distinct values can never exceed the size of that support, however
large the sample grows. The finite-dimensional
analogue is [Dirichlet–multinomial
conjugacy](dirichlet-multinomial-conjugacy.qmd): counts add to Dirichlet
parameters on a fixed partition. The Dirichlet process extends that
construction to all finite partitions at once, which is why the same
conjugacy reappears as its posterior result.

## Definition — Dirichlet marginals on every finite partition

Let the sample space be a set $\mathcal{X}$ with a collection of
measurable subsets. A random probability measure $G$ is a random object
whose realisations are probability measures: for each measurable set
$A$, $G(A)$ is a random variable in $[0, 1]$, and with probability one
the realised function $A \mapsto G(A)$ is a probability measure. Let
$G_0$ be a fixed probability measure on $\mathcal{X}$ and $\alpha >
0$. Then $G$ follows a Dirichlet process with concentration $\alpha$
and base measure $G_0$, written

$$G \sim \mathrm{DP}(\alpha, G_0),$$

if, for every finite measurable partition $A_1, \dots, A_k$ of
$\mathcal{X}$ — disjoint measurable sets whose union is $\mathcal{X}$,
for any $k \geq 1$ — the random vector of cell probabilities has the
Dirichlet distribution

$$(G(A_1), \dots, G(A_k)) \sim
\mathrm{Dirichlet}(\alpha G_0(A_1), \dots, \alpha G_0(A_k)).$$

Ferguson's original definition uses a single finite non-null measure
$\alpha(\cdot)$ in place of the pair $(\alpha, G_0)$, with Dirichlet
parameters $(\alpha(A_1), \dots, \alpha(A_k))$ {{cite:ferguson1973}} (Definition 1, p. 214). The formulations coincide, with $\alpha(A) =
\alpha G_0(A)$: $\alpha$ is the total mass and $G_0$ the normalised
measure — where the mass of $G$ is expected to lie, and how strongly
that expectation is held.

Two points require care. First, the requirement is imposed for every
finite partition simultaneously, and the Dirichlet family is coherent
under refinement and coarsening: aggregating cells gives a Dirichlet
vector with aggregated parameters. That coherence makes the definition
consistent — the law of $(G(A_1), \dots, G(A_k))$ does not depend on
which larger partition the sets came from — and Ferguson verifies the
Kolmogorov consistency conditions {{cite:ferguson1973}} (pp. 213–214).
Second, the definition specifies distributions rather than a
realisation; Sethuraman notes a gap in passing to a countably additive
random measure, which his constructive definition, below, removes
{{cite:sethuraman1994}} (p. 641).

The definition determines the prior mean and variance of $G(A)$ for any
set $A$: the partition $\{A, A^c\}$ gives $G(A) \sim
\mathrm{Beta}(\alpha G_0(A), \alpha(1 - G_0(A)))$, since a
two-component Dirichlet vector is a beta distribution. The Dirichlet
moments recorded by Ferguson {{cite:ferguson1973}} (§2, p. 212), applied
to this marginal, give

$$\E[G(A)] = G_0(A), \qquad
\mathrm{Var}(G(A)) = \frac{G_0(A)(1 - G_0(A))}{\alpha + 1}.$$

The expectation is Ferguson's Proposition 1: $\E[P(A)] = \alpha(A)/\alpha(\mathcal{X})$ {{cite:ferguson1973}} (Proposition 1, pp. 214–215). The variance formula is exact: the prior mean of $G(A)$
does not depend on $\alpha$, and its variance is the largest possible
for a probability with that mean, $G_0(A)(1 - G_0(A))$, divided by
$\alpha + 1$. As $\alpha$ grows, $G$ concentrates around $G_0$; as
$\alpha$ shrinks towards zero, it concentrates on distributions
carried by very few atoms, as stick-breaking will show. Numerically,
if $G_0(A) = 1/2$, then $\mathrm{Var}(G(A))$ is $1/8 = 0.125$ when
$\alpha = 1$, $1/16 = 0.0625$ when $\alpha = 3$, and $1/40 = 0.025$
when $\alpha = 9$. So $\alpha$ is a prior sample size: $G_0$ enters
the posterior with the weight of $\alpha$ pseudo-observations, against
$n$ real ones.

## Properties — Discreteness, stick-breaking, the urn, and conjugacy

### Draws are discrete: the atoms come first

A realisation of a Dirichlet process is, with probability one, a
discrete probability measure: $G$ places all its mass on a countable
collection of points. This holds without any condition on $G_0$. If
$G_0$ is the standard normal distribution — with a density, no atoms,
and $G_0(\{x\}) = 0$ for every point $x$ — a draw $G \sim
\mathrm{DP}(\alpha, G_0)$ still has the form $G = \sum_k \pi_k
\delta_{\theta_k}$, where $\delta_{\theta}$ places mass one at
$\theta$. Ferguson's abstract states the conclusion of his Section 4
alternative definition, which "exhibits a version of the Dirichlet
process that gives probability one to the set of discrete probability
measures" {{cite:ferguson1973}} (pp. 209–210); his Section 4
construction, normalising a gamma process's jumps, produces the
discrete realisation directly {{cite:ferguson1973}} (§4, pp. 218–220).
Sethuraman's abstract records the same property as the second of his
three basic results {{cite:sethuraman1994}} (p. 639), and Neal states
it as the starting point for mixture modelling: "Since realizations of
the Dirichlet process are discrete with probability one, these models
can be viewed as countably infinite mixtures" {{cite:neal2000_dpmm}} (p. 251).

Discreteness has an immediate consequence for sampling: draws from a
realised $G$ coincide with positive probability, because two draws may
select the same atom. Antoniak computes the first instance exactly:
for a nonatomic parameter measure, the probability that the second draw
equals the first is $1/(\alpha + 1)$ {{cite:antoniak1974}} (§4, pp. 1160–1161) — $1/2$ when $\alpha = 1$, $1/3$ when $\alpha = 2$,
against zero under any continuous sampling distribution. Ferguson flags
the cost: the disadvantage appears "mainly because in sampling from a
$P$ chosen by a Dirichlet process, we expect eventually to see one
observation exactly equal to another", and his goodness-of-fit example
shows such a prior turning a test of uniformity into a test of
continuity against discreteness {{cite:ferguson1973}} (p. 210). The
standard remedy, convolving $G$ with a continuous kernel, is the
Dirichlet process mixture treated under 'Dirichlet process mixtures:
recovering continuous densities' below.

### The stick-breaking construction

The partition definition specifies distributions but does not exhibit a
realisation. Sethuraman's constructive definition does. Let $V_1, V_2,
\dots$ be independent with $V_k \sim \mathrm{Beta}(1, \alpha)$,
independently of independent draws $\theta_1, \theta_2, \dots$ from
$G_0$. Define weights by

$$\pi_1 = V_1, \qquad \pi_k = V_k \prod_{j < k} (1 - V_j)
\quad \text{for } k \geq 2,$$

and set $G = \sum_{k=1}^{\infty} \pi_k \delta_{\theta_k}$. In
Sethuraman's notation the break variables are independent
Beta$(1, \alpha(\mathcal{X}))$ — $\alpha$ the total mass — the atoms
are drawn from the normalised measure $\beta =
\alpha(\cdot)/\alpha(\mathcal{X})$, and $\sum_{1 \leq m \leq n} p_m
= 1 - \prod_{1 \leq m \leq n} (1 - \theta_m)$ tends to one with
probability one {{cite:sethuraman1994}} (§2, p. 642). In the
$(\alpha, G_0)$ parametrisation, $\beta$ is $G_0$. Sethuraman proves
the constructed $G$ has the required Dirichlet finite-dimensional
distributions; built from point masses, it is discrete by construction
{{cite:sethuraman1994}} (pp. 641–642).

The name describes the arithmetic. Begin with a stick of unit length.
Break off a fraction $V_1$; that piece, of length $\pi_1 = V_1$, is the
weight of $\theta_1$. From the remainder, of length $1 - V_1$, break
off a fraction $V_2$; that piece, of length $\pi_2 = V_2(1 - V_1)$, is
the weight of $\theta_2$. Continue indefinitely. The mass remaining
after $K$ breaks, $\prod_{j \leq K} (1 - V_j)$, tends to zero with
probability one, so the weights sum to one. The expected weights are
exact: $\E[V_k] = 1/(1 + \alpha)$ and independence gives $\E[\pi_k] =
\frac{1}{1 + \alpha} \left(\frac{\alpha}{1 + \alpha}\right)^{k-1}$,
a geometric sequence; for $\alpha = 2$, $\E[\pi_1] = 1/3$ and
$\E[\pi_2] = 2/9$. Large $\alpha$ spreads mass over many atoms; small
$\alpha$ makes the first few breaks large, so a draw is dominated by a
handful of atoms.

### The Pólya urn and the Chinese restaurant process

Integrating out $G$ changes the viewpoint from the random measure to
the observations, and gives the description most useful for clustering.
Let $X_1, X_2, \dots$ be drawn from $G \sim
\mathrm{DP}(\alpha, G_0)$, independently conditionally on $G$:
sampling independence holds given the shared random measure, and it
is the integration over $G$ that makes the sequence dependent. The
sequence is [exchangeable](exchangeability.qmd), so it can be
described by its successive conditionals, which have a closed form. Blackwell and
MacQueen define a Pólya sequence by $P(X_1 \in B) =
\alpha(B)/\alpha(\mathcal{X})$ and

$$P(X_{n+1} \in B \mid X_1, \dots, X_n) =
\frac{\alpha(B) + \sum_{i=1}^{n} \delta_{X_i}(B)}{\alpha(\mathcal{X}) + n}$$

for every measurable set $B$, where $\delta_{x}(B)$ is one if $x \in B$
and zero otherwise {{cite:blackwell_macqueen1973}} (eq. (2), p. 353).
In $(\alpha, G_0)$ notation, the conditional distribution of $X_{n+1}$
given the past is $\frac{\alpha}{\alpha + n} G_0 + \frac{1}{\alpha + n}
\sum_{i=1}^{n} \delta_{X_i}$: a weighted average of the base measure
and the empirical distribution so far. Blackwell and MacQueen prove
the converse as well: a Pólya sequence's empirical distribution
converges with probability one to a limiting discrete measure with
Ferguson's Dirichlet distribution, and given the limit the observations
are independent with that distribution {{cite:blackwell_macqueen1973}} (Theorem, p. 354). Urn and process are two descriptions of one object:
a ball is drawn, returned, and a second ball of the same colour added,
so seen colours become more likely to recur. Neal records the same
conditional as his equation (2.2) {{cite:neal2000_dpmm}} (p. 251).

The Chinese restaurant process is this same urn scheme retold as a
seating rule; it is not a second model, and not a separate invention
layered on top of the Dirichlet process. Customers arrive one at a
time; the first sits at a new table, and each later customer either
joins an occupied table, with probability proportional to the number
already seated there, or starts a new table, with probability
proportional to $\alpha$. If $n$ customers are seated at tables with
occupancies $n_1, \dots, n_K$, the next joins table $j$ with
probability $n_j/(\alpha + n)$ and starts a new table with probability
$\alpha/(\alpha + n)$. These are the urn probabilities grouped by table: joining table $j$
is the event $X_{n+1} = \theta_j^{*}$, where $\theta_j^{*}$ is the
shared value at that table; a new table is a fresh draw from $G_0$.
The tables are the clusters of the model, with one caveat: a fresh
draw from $G_0$ can coincide with an existing table's value when
$G_0$ has atoms, so the number of tables and the number of distinct
values among the observations can differ. The implication between
the two descriptions runs one way only: joining a specific table
implies sharing that table's value, but sharing a value does not
imply sharing a table — two tables can carry the same value, opened
by separate fresh draws that happened to coincide. The two counts
agree when $G_0$ is nonatomic, since a fresh draw then differs from
every previous value with probability one. The same distinction
governs ties: for two draws, the probability of a tie is
$\frac{1}{\alpha + 1} + \frac{\alpha}{\alpha + 1} \Pr(Y = Y')$,
where $Y$ and $Y'$ are independent draws from $G_0$ — the first term
is the chance the second draw joins the first draw's table, the
second the chance that a fresh draw from $G_0$ lands on the same
value. For nonatomic $G_0$, $\Pr(Y = Y') = 0$ and the formula
reduces to the $1/(\alpha + 1)$ computed above; for a point-mass
$G_0$, $\Pr(Y = Y') = 1$ and a tie is certain.
Antoniak's sampling calculations are the restaurant arithmetic
without the metaphor: at step $i$ the draw opens a new table —
takes a fresh draw from $G_0$ — with probability
$\alpha/(\alpha + i - 1)$, whatever the pattern of repetitions so
far {{cite:antoniak1974}} (§4, pp. 1160–1161). A new table is not
automatically a new value. When $G_0$ is nonatomic, Antoniak's
setting, a fresh draw is a new distinct value with probability one,
and $\alpha/(\alpha + i - 1)$ is also the probability that the draw
at step $i$ is distinct from all previous draws. When $G_0$ has
atoms it need not be: if $G_0$ is a point mass, every observation
has the same value, new tables keep opening at rate
$\alpha/(\alpha + i - 1)$, and after the first observation the
probability of a new distinct value is zero.

The seating rule is also the prior on partitions, and it is not
neutral: arrivals prefer large tables, so partitions with a few large
clusters are favoured over balanced ones with the same number of
tables. Its strength is controlled entirely by $\alpha$: the rate of new
tables depends only on the magnitude $\alpha$ of the parameter
measure, not on its shape $G_0$, and in the nonatomic case Antoniak
treats, the same is true of the rate of new distinct values
{{cite:antoniak1974}} (p. 1161).

### The posterior: conjugacy

The conjugacy promised by property (II) is exact. Let $G \sim
\mathrm{DP}(\alpha, G_0)$ and let $X_1, \dots, X_n$ be a sample from
$G$. Then the conditional distribution of $G$ given the sample is again
a Dirichlet process,

$$G \mid X_1, \dots, X_n \sim
\mathrm{DP}\left(\alpha + n,\ \frac{\alpha G_0 + \sum_{i=1}^{n}
\delta_{X_i}}{\alpha + n}\right).$$

This is Ferguson's main theorem: the posterior, given a sample, is a
Dirichlet process with parameter $\alpha + \sum_{i=1}^{n}
\delta_{X_i}$ {{cite:ferguson1973}} (Theorem 1, pp. 217–218).
Sethuraman lists the same closure as his third basic property: "the
posterior distribution is also a Dirichlet measure"
{{cite:sethuraman1994}} (p. 639).

The posterior concentration is $\alpha + n$: pseudo-observations and
real observations count identically. The posterior base measure is the
weighted average of $G_0$ and the empirical distribution, with weights
$\alpha/(\alpha + n)$ and $n/(\alpha + n)$, so every prior result
transfers. In particular,

$$\E[G(A) \mid X_1, \dots, X_n] =
\frac{\alpha G_0(A) + \#\{i : X_i \in A\}}{\alpha + n},$$

which is also the predictive probability that a further draw falls in
$A$ — the urn conditional, read as a posterior statement. The posterior
variance of $G(A)$ is $\bar{G}(A)(1 - \bar{G}(A))/(\alpha + n + 1)$.
As $n$ grows with $\alpha$ fixed, $\bar{G}$ approaches the empirical
distribution and this variance shrinks at rate $1/n$: the prior washes
out of set-by-set summaries, the summary-level consistency the sources
support. Escobar and West use the same bookkeeping, where $\alpha = 1$
"corresponds to the initial prior $G_0$ receiving the weight of one
observation in the posterior" {{cite:escobar_west1995}} (p. 578).

Ties enter $\bar{G}$ with multiplicity: a value occurring $m$ times
receives mass $m/(\alpha + n)$ there. A posterior draw is still
discrete; smoothing comes from the mixture construction, not the update.

## Worked example

### Five breaks of the stick

Suppose the first five break fractions are realised as

$$V_1 = \frac{1}{2}, \quad V_2 = \frac{1}{3}, \quad V_3 = \frac{1}{4},
\quad V_4 = \frac{1}{5}, \quad V_5 = \frac{1}{6}.$$

| Break $k$ | $V_k$ | Stick remaining before break | Weight $\pi_k$ |
|---:|---:|---:|---:|
| 1 | $1/2$ | $1$ | $1/2$ |
| 2 | $1/3$ | $1/2$ | $1/6$ |
| 3 | $1/4$ | $1/3$ | $1/12$ |
| 4 | $1/5$ | $1/4$ | $1/20$ |
| 5 | $1/6$ | $1/5$ | $1/30$ |

For instance, $\pi_3 = V_3(1 - V_1)(1 - V_2) = (1/4)(1/2)(2/3) =
1/12$, and the remaining entries follow the same pattern. In decimal
form the weights are approximately $0.5$, $0.166667$, $0.083333$,
$0.05$ and $0.033333$. Their sum is $1/2 + 1/6 + 1/12 + 1/20 + 1/30 =
5/6$, and the mass remaining for all subsequent atoms is the unbroken
remainder,

$$\prod_{j=1}^{5} (1 - V_j) = \frac{1}{2} \times \frac{2}{3} \times
\frac{3}{4} \times \frac{4}{5} \times \frac{5}{6} = \frac{1}{6},$$

so $5/6 + 1/6 = 1$, as it must. Here the weights follow the pattern
$\pi_k = 1/(k(k+1))$, a property of these fractions, not of
stick-breaking in general. Realised weights need not decrease in
general, and the remainder $1/6 \approx 0.166667$ is the total weight
of all later atoms: truncation levels are set by the expected remainder
$\left(\frac{\alpha}{1 + \alpha}\right)^K$ after $K$ breaks, not by
the atom count.

### The sixth customer, and how many tables to expect

**Seating probabilities.** Let $\alpha = 2$, and suppose the first five
customers are seated with three at one table and two at another. For
the sixth customer the denominator is $\alpha + n = 2 + 5 = 7$, so

$$P(\text{join the table of 3}) = \frac{3}{7} \approx 0.428571, \qquad
P(\text{join the table of 2}) = \frac{2}{7} \approx 0.285714, \qquad
P(\text{new table}) = \frac{2}{7} \approx 0.285714.$$

The probabilities sum to $3/7 + 2/7 + 2/7 = 1$. A new table is exactly
as probable as joining the smaller table, because $\alpha = 2$ gives
the unexplored space the weight of two customers. Under $\alpha = 1$
the same seating would give a new-table probability of $1/6$: $\alpha$,
not the data pattern, sets the rate at which new clusters open.

**Expected number of tables.** Let $K_n$ be the number of occupied
tables after $n$ customers. Summing the indicators of new tables,
each with probability $\alpha/(\alpha + i - 1)$ at step $i$, gives

$$\E[K_n] = \sum_{i=1}^{n} \frac{\alpha}{\alpha + i - 1},$$

Antoniak's formula for the expected number of tables
{{cite:antoniak1974}} (§4, pp. 1160–1161). When $G_0$ is nonatomic,
$K_n$ is also the number of distinct values among $X_1, \dots, X_n$;
with an atomic $G_0$ the number of distinct values is at most $K_n$,
and can be strictly smaller.

For $\alpha = 2$ and $n = 5$ this is $2/2 + 2/3 + 2/4 + 2/5 + 2/6 =
29/10 = 2.9$ exactly. For $\alpha = 1$ the terms simplify to $1/i$, and
for $n = 10$,

$$\E[K_{10}] = \sum_{i=1}^{10} \frac{1}{i} = H_{10} =
\frac{7381}{2520} \approx 2.928968,$$

where $H_{10}$ is the tenth harmonic number. Ten draws under $\alpha = 1$ thus produce, on average, fewer than
three tables — and, when $G_0$ is nonatomic, fewer than three
distinct values: the discreteness of $G$ is the typical behaviour
of the model, not a tail event. The expectation grows only logarithmically in $n$ — Escobar and
West give the approximation $\E[K_n] \approx \alpha
\log\left(\frac{\alpha + n}{\alpha}\right)$, which for $\alpha = 1$
and $n = 10$ gives $\log 11 \approx 2.397895$, below the exact
$2.928968$ at this small $n$ {{cite:escobar_west1995}} (p. 578) — yet
it still tends to infinity with $n$, as Antoniak notes
{{cite:antoniak1974}} (§4, pp. 1160–1161): new clusters never stop
arriving, only more and more slowly.

### A posterior with ties

Let the prior be $\mathrm{DP}(3, G_0)$ with $G_0$ uniform on
$[0, 1]$, and suppose the sample of size $n = 4$ is $X_1 = 0.2$,
$X_2 = 0.2$, $X_3 = 0.7$, $X_4 = 0.2$: $0.2$ occurs three times and
$0.7$ once. By conjugacy, the posterior is a Dirichlet process with
concentration $3 + 4 = 7$ and base measure

$$\bar{G} = \frac{3 G_0 + 3\delta_{0.2} + \delta_{0.7}}{7}.$$

Thus $\bar{G}$ places weight $3/7$ on the atom at $0.2$, weight $1/7$
on the atom at $0.7$, and the remaining $3/7$ spread over $[0, 1]$
according to $G_0$.

Take $A = [0, 0.5]$, so $G_0(A) = 1/2$ and $A$ contains three of the
four observations. The posterior mean is

$$\E[G(A) \mid \text{data}] = \frac{3 \times \frac{1}{2} + 3}{7}
= \frac{9}{14} \approx 0.642857.$$

Predictively, $P(X_5 = 0.2 \mid \text{data}) = 3/7$, $P(X_5 = 0.7
\mid \text{data}) = 1/7$, and the probability that a new value falls
in $A$ is $(3/7)(1/2) = 3/14$; joining the atom in $A$ and drawing a new
value in $A$ give $3/7 + 3/14 = 9/14$, agreeing with the posterior
mean, as the theory requires. The posterior variance of $G(A)$ is

$$\mathrm{Var}(G(A) \mid \text{data}) =
\frac{(9/14)(5/14)}{7 + 1} = \frac{45}{1568} \approx 0.028699.$$

One caution: $\bar{G}$ is not a posterior draw. A draw's weight at
$0.2$ is random — marginally a beta random variable centred near $3/7$
— not a fixed $3/7$. Reporting $\bar{G}$ as "the estimated
distribution" conflates the posterior mean with the random measure.

## Statistical use — Mixtures, computation, and uses

Used directly, the Dirichlet process is a prior for an unknown
distribution when the data are genuinely discrete, or when only set
probabilities and functionals such as means and quantiles are of
interest — Ferguson's applications, including a distribution function,
a mean, quantiles, and a two-sample problem in which the Mann–Whitney
statistic appears {{cite:ferguson1973}} (§5). Used as a mixing distribution, it gives the mixture: density
estimation and clustering with the component count inferred rather than
fixed. Used inside larger [hierarchical Bayesian
models](hierarchical-bayesian-model.qmd), it gives each group its own
distribution drawn from a shared prior. In each use the engine is the
same pair of results: the urn predictive distribution, and the
conjugate posterior for $G$.

### Dirichlet process mixtures: recovering continuous densities

The discreteness of $G$ is a defect for density estimation and a virtue
for clustering; the mixture model keeps the virtue while removing the
defect. Antoniak's 1974 paper is the origin. He considers the random
measure as a mixing distribution for a parameter that determines the
distribution from which observations are made, and shows the posterior
of the random measure is then no longer a simple Dirichlet process but
a mixture of Dirichlet processes, with a closure property: sampling
from a mixture of Dirichlet processes, with the sample distorted by
random error, returns a posterior in the same class
{{cite:antoniak1974}} (Abstract, p. 1152; Theorem 3, pp. 1158–1159).
His corollary to Theorem 3 states the single-model version: if $\theta$ is a sample
from a Dirichlet process $P$ and $X$ is drawn from a transition
probability $F(\theta, \cdot)$ given $\theta$, then $P$ given $X$ is
a mixture of Dirichlet processes {{cite:antoniak1974}} (pp. 1159–1160, the corollary to Theorem 3). Neal dates the models the same way: "Dirichlet process
mixture models go back to Antoniak (1974) and Ferguson (1983)"
{{cite:neal2000_dpmm}} (§2, p. 250).

In Neal's notation, observations $y_1, \dots, y_n$ are generated by

$$y_i \mid \theta_i \sim F(\theta_i), \qquad
\theta_i \mid G \sim G, \qquad G \sim \mathrm{DP}(\alpha, G_0),$$

where $F(\theta)$ is a sampling distribution indexed by $\theta$ — the
kernel {{cite:neal2000_dpmm}} (eq. (2.1), pp. 250–251). Marginally, the
distribution of an observation is the kernel convolution

$$f(y) = \int F(y \mid \theta) \, dG(\theta)
= \sum_{k=1}^{\infty} \pi_k F(y \mid \theta_k),$$

substituting the stick-breaking form of $G$. If $F(\cdot \mid \theta)$
is a continuous density for each $\theta$ — a normal density with
$\theta = (\mu, \sigma^2)$, in the most common case — then $f$ is a
continuous density, a countably infinite mixture of continuous
components, even though $G$ is discrete. The discreteness has moved to
where it is useful: the latent $\theta_i$ coincide with positive
probability, so observations cluster around shared components, while
the observable density is smooth. This is a [finite mixture
model](finite-mixture-model.qmd) with the component count left open:
the model is also the limit, as $K \to \infty$, of a $K$-component
mixture whose proportions have a symmetric Dirichlet prior with
parameter $\alpha/K$ per component {{cite:neal2000_dpmm}} (pp. 251–252), and the prior probability that two observations share a
component is $1/(1 + \alpha)$ {{cite:neal2000_dpmm}} (p. 252).

Escobar and West give the canonical instance, a mixture of normals for
density estimation: $G$ over mean–variance pairs follows a Dirichlet
process with $\E[G] = G_0$, where $G_0$ is a normal/inverse-gamma prior,
conjugate to the normal kernel, and $\alpha$ is a precision parameter
for the concentration of $G$ about $G_0$ {{cite:escobar_west1995}} (§2, p. 578). The predictive density is a data-adaptive kernel estimate
with component parameters shrunk towards the prior, inheriting a kernel
method's smoothing while letting the data determine the number and
placement of components {{cite:escobar_west1995}} (p. 578). Inference
about the number of components $K$ is a by-product: its prior is
induced by $\alpha$ and $n$ through Antoniak's formulas, and for
$\alpha$ small relative to $n$ — with $n$ between 50 and 250, say —
the prior for $K$ "heavily favors single-digit values"
{{cite:escobar_west1995}} (p. 578). A mixture thus counts clusters
under a prior expecting few of them, not neutrally.

### Computation

Exact posterior computation is not available beyond very small samples.
Neal states the obstruction plainly: "Exact computation of posterior
expectations for a Dirichlet process mixture model is infeasible when
there are more than a few observations", because the posterior ranges
over all partitions of the observations and their component parameters
{{cite:neal2000_dpmm}} (§3, p. 252). The standard
route is Markov chain Monte Carlo over the latent allocations,
integrating $G$ out and working with the urn conditionals: each
assignment is resampled from a conditional combining the urn
probabilities — proportional to cluster size for an existing cluster,
proportional to $\alpha$ for a new one — with the observation's
likelihood under each candidate.

When $G_0$ is conjugate to the kernel, component parameters integrate
out analytically and allocations are resampled by Gibbs sampling;
Neal's Algorithm 1, used earlier by Escobar, resamples each $\theta_i$
given the other allocations and the data {{cite:neal2000_dpmm}} (Algorithm 1, p. 253). The conjugate case is the exception in
applications, and Neal's contribution is methods for non-conjugate
$G_0$: Metropolis–Hastings updates of the allocation indicators using
the conditional prior as the proposal, and Gibbs samplers extended with
auxiliary parameters drawn from $G_0$ for the unoccupied components a
new cluster might use — his Algorithm 8, whose equilibrium distribution
is exactly the posterior for any number of auxiliary parameters
{{cite:neal2000_dpmm}} (Abstract, p. 249; Algorithm 8, p. 262). Escobar and West's earlier
sampler follows the same logic {{cite:escobar_west1995}} (§3, pp. 579–580).

A sweep's cost grows with the number of occupied clusters as well as
with $n$; and because the chain moves one allocation at a time, splits
and merges of large clusters are rare, so mixing over partitions can be
slow even when within-cluster parameters mix well. Optimisation-based
alternatives — see [variational inference](variational-inference.qmd)
— and gradient-based samplers — see [Hamiltonian Monte
Carlo](hamiltonian-monte-carlo.qmd) — address different parts of this
cost. [Importance sampling](importance-sampling.qmd), the earlier
simulation route, was displaced because its weights degenerate over the
partition space {{cite:escobar_west1995}} (p. 578).

## Common misconceptions

**"The Dirichlet process is a prior over smooth densities."** It is a
prior over discrete distributions: every draw is a weighted sum of
point masses, whatever $G_0$ is. Smooth densities arise only after the
draw is convolved with a continuous kernel, in a mixture.

**"$G_0$ is the distribution the data came from."** $G_0$ is the prior
mean, $\E[G(A)] = G_0(A)$. A draw $G$ differs from $G_0$ in every
realisation, by an amount governed by $\alpha$; confusing the mean
with a draw understates the spread by exactly the variance $G_0(A)(1 -
G_0(A))/(\alpha + 1)$.

**"$\alpha$ is a minor technical constant."** $\alpha$ is the prior
sample size. It sets the prior variance of $G(A)$, the tie probability
— $1/(\alpha + 1)$ when $G_0$ is nonatomic, larger when $G_0$ has
atoms — the expected table count $\sum_i \alpha/(\alpha + i - 1)$,
and the weight of $G_0$ against the data in the posterior.

**"The Chinese restaurant process is an alternative to the Dirichlet
process."** It is the Dirichlet process with $G$ integrated out,
described through seating probabilities. Restaurant and urn rules give
identical probabilities for every partition; neither approximates the
other.

**"The number of clusters found is the number that are really there."**
The model has infinitely many components available and finitely many
occupied. The occupied count is a posterior quantity under a prior
favouring few, unequal clusters; it counts components used to represent
the data, not a census of subpopulations.

**"Nonparametric means assumption-free."** The process assumes
exchangeability, a base measure whose support contains the truth, a
concentration parameter, and — in the mixture — a kernel family. It
removes only the assumption of a named finite-dimensional form.

## Assumptions and limits — Discreteness, concentration, and computation

Each of these limits traces to a result above.

*Discreteness.* Prior and posterior draws are discrete with probability
one. Any use requiring $G$ itself to be continuous is a misuse; the
mixture construction exists because of this limit, not as a refinement.

*Sensitivity to $\alpha$.* The concentration parameter controls the
prior variance of every $G(A)$, the tie probability ($1/(\alpha + 1)$
for a nonatomic base, larger when the base has atoms), the expected
number of occupied tables, and the pull towards $G_0$ in the
posterior — one choice seen from four sides. Escobar and West's
observation that realistic $\alpha$ makes the prior for the component
count favour single-digit values {{cite:escobar_west1995}} (p. 578) is
the sharpest warning: with thousands of observations, a default
$\alpha = 1$ still encodes a prior expectation of about $\log n$
clusters. A prior on $\alpha$, as Neal's hyperparameter updates allow
{{cite:neal2000_dpmm}} (§7), propagates the uncertainty but does not
remove the dependence.

*The prior on partitions favours unequal clusters.* The restaurant rule
joins large tables preferentially, so partitions with a few large
clusters and many small ones have higher prior probability than
balanced ones with the same number of clusters. Where the question
concerns the partition itself — subtypes, regimes, communities — this
is a substantive assumption, made by the urn rule whether or not it is
acknowledged.

*Computation.* Posterior expectations require Markov chain sampling
over partitions {{cite:neal2000_dpmm}} (§3, p. 252). Results are Monte
Carlo estimates whose error depends on the mixing of an allocation
chain, and cluster summaries inherit mixture label ambiguity: the chain
visits partitions, not named clusters, so a reported "cluster" is a
summary built from co-allocation frequencies, not a parameter.

*What consistency does and does not say.* The posterior base measure
converges to the empirical distribution as $n$ grows, so posterior
means of $G(A)$ are consistent at each fixed $A$ — a statement about
one-dimensional summaries of $G$, not a guarantee about densities,
cluster counts or partitions in a mixture model, whose posterior
behaviour depends on the kernel and on $G_0$ as well.

## Connections

- [Bayesian inference](bayesian-inference.qmd) — Bayes' rule with a
  prior whose parameter is a distribution; the process's conjugacy is
  the infinite-dimensional counterpart of the finite conjugate families.
- [Dirichlet distribution](dirichlet-distribution.qmd) — the
  finite-dimensional law imposed on every finite partition; the process
  is determined by requiring it coherently for all partitions at once.
- [Dirichlet–multinomial conjugacy](dirichlet-multinomial-conjugacy.qmd)
  — the finite-partition special case of the posterior update: counts
  add to Dirichlet parameters, as a sample adds point masses to the
  parameter measure of the process.
- [Exchangeability](exchangeability.qmd) — the symmetry validating the
  urn and restaurant descriptions: an exchangeable sequence from a
  random $G$ is generated by the Pólya urn conditionals.
- [Finite mixture model](finite-mixture-model.qmd) — a Dirichlet
  process mixture is the limit of finite mixtures as the component
  count grows, under a symmetric Dirichlet$(\alpha/K)$ prior.
- [Hierarchical Bayesian model](hierarchical-bayesian-model.qmd) —
  a Dirichlet process at the group level gives each group its own
  distribution, with $G_0$ and $\alpha$ controlling shared atoms.
- [Variational inference](variational-inference.qmd) — an
  optimisation-based alternative to allocation Gibbs sampling, usually
  applied to a truncated stick-breaking representation.
- [Hamiltonian Monte Carlo](hamiltonian-monte-carlo.qmd) — a
  gradient-based sampler for continuous kernel parameters,
  complementing the discrete allocation updates.
- [Importance sampling](importance-sampling.qmd) — the earlier
  simulation method for these posteriors, displaced by
  allocation-resampling methods because its weights degenerate over
  the partition space.

## History

Thomas S. Ferguson introduced the Dirichlet process in "A Bayesian
analysis of some nonparametric problems", in the *Annals of Statistics*
in 1973 {{cite:ferguson1973}} (pp. 209–210). The paper defined the
process by its Dirichlet finite-dimensional distributions, proved the
posterior is again a Dirichlet process, gave a normalised gamma process
construction making discreteness explicit, and developed applications
to distribution functions, means and quantiles {{cite:ferguson1973}} (§§3–5, pp. 213–230). In the same issue, Blackwell and MacQueen
connected Ferguson's distributions to generalised Pólya urn schemes
{{cite:blackwell_macqueen1973}} (pp. 353–354). Antoniak (1974) extended
the theory to mixtures of Dirichlet processes and derived the tie and
distinct-value formulas underlying the restaurant representation
{{cite:antoniak1974}} (pp. 1152, 1160–1161).

For two decades the process was principally theoretical, because its
posteriors could not be computed for the mixture models where it was
most needed. Sethuraman's constructive definition, published in
*Statistica Sinica* in 1994 after circulating from 1980, rebuilt the
process from independent beta variables and point masses, with
self-contained proofs of discreteness and posterior closure
{{cite:sethuraman1994}} (pp. 639, 642). Escobar and West (1995) made
mixtures of normals a working method for density estimation
{{cite:escobar_west1995}} (pp. 577–578), and Neal's 2000 review
completed the computational picture, systematising Gibbs sampling for
conjugate priors and adding auxiliary-parameter and Metropolis–Hastings
methods for non-conjugate priors {{cite:neal2000_dpmm}} (pp. 249–250).
Stick-breaking has since become the representation through which the
process is usually implemented.

## Check yourself

1. Stick-breaking fractions $V_1 = 1/4$ and $V_2 = 1/2$ are realised.
What are the weights $\pi_1$ and $\pi_2$ of the first two atoms, and
how much mass remains for the later atoms?

::: {.callout-tip collapse="true" title="Answer"}

$\pi_1 = V_1 = 1/4$. The second break takes half of the remaining
$3/4$, so $\pi_2 = (1/2)(3/4) = 3/8$. The mass remaining after two
breaks is $(3/4)(1/2) = 3/8$, and $1/4 + 3/8 + 3/8 = 1$.

:::

2. In a Chinese restaurant process with $\alpha = 1$, four customers
are seated: three at one table and one at another. What are the
probabilities that the fifth customer joins the table of three, joins
the table of one, and starts a new table?

::: {.callout-tip collapse="true" title="Answer"}

The denominator is $\alpha + n = 1 + 4 = 5$: the table of three with
probability $3/5$, the table of one with probability $1/5$, and a new
table with probability $\alpha/(\alpha + n) = 1/5$, summing to $1$.

:::

3. A prior $G \sim \mathrm{DP}(1, G_0)$ has $G_0(A) = 1/4$ for a set
$A$. Two observations are drawn from $G$, and both fall in $A$. What is
the posterior mean of $G(A)$?

::: {.callout-tip collapse="true" title="Answer"}

The posterior has concentration $1 + 2 = 3$, and its mean at $A$ is
$(\alpha G_0(A) + 2)/(\alpha + n) = (1 \times 1/4 + 2)/3 = 3/4$. The
two observations outweigh the prior's single pseudo-observation, which
assigned $A$ probability $1/4$.

:::
