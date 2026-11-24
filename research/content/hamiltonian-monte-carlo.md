## Lead context

Hamiltonian Monte Carlo (HMC) is a Markov chain Monte Carlo method for
sampling from a continuous probability distribution whose density can be
evaluated, up to an unknown normalising constant, and differentiated. It
differs from the [Metropolis–Hastings algorithm](metropolis-hastings-algorithm.qmd)
with a random-walk proposal in how the proposal is constructed: instead of
perturbing the current point by an undirected random step, HMC augments the
variables of interest with auxiliary momentum variables, simulates a
deterministic trajectory governed by Hamiltonian dynamics, and proposes the
endpoint of that trajectory. Because the trajectory is directed, a proposal
can be far from the current point and still have a high probability of
acceptance. Neal states the purpose directly: Hamiltonian dynamics "can be
used to produce distant proposals for the Metropolis algorithm, thereby
avoiding the slow exploration of the state space that results from the
diffusive behaviour of simple random-walk proposals" {{cite:neal2011_hmc}} (pp. 113–114). The price of the construction is that the gradient of the log
density must be available, and that two tuning quantities — a step size and
a trajectory length — must be chosen well.

## Motivating example — Why random-walk proposals explore slowly

Consider the random-walk form of Metropolis–Hastings: from a current point
$q$, propose $q^*$ by adding a symmetric random perturbation, and accept or
reject by the usual ratio of target densities. If the perturbation is
large, most proposals land where the target density is much lower and are
rejected. If it is small, most are accepted, but each move is short and
its direction is unrelated to the previous move's. Displacement then
accumulates diffusively: after $n$ accepted steps of typical length $s$,
the distance travelled is of order $s\sqrt{n}$, not $sn$, because
successive steps partly cancel. Reaching a point at distance $D$ takes of
order $(D/s)^2$ steps rather than $D/s$.

The difficulty sharpens as the dimension $d$ grows and as the target becomes
more strongly correlated. In high dimensions, probability mass for many
standard targets concentrates in a comparatively narrow region — Betancourt
calls the region where mass and density balance the typical set — and a
proposal that is not informed by the local shape of the density will
typically propose points outside it {{cite:betancourt2017_hmc}} (§§1.3–1.4, pp. 6–8).
With correlated parameters, an isotropic perturbation must be small enough
to be accepted across the narrowest direction of the target, which makes
progress along the widest direction slower still. Hoffman and Gelman
summarise the comparison in cost terms: for a target of dimension $d$, the
cost per effectively independent draw is roughly of order $d^{5/4}$ for HMC
against of order $d^2$ for random-walk Metropolis, a comparison they
attribute to Creutz {{cite:hoffman_gelman2014}} (§1, p. 1594). These are scaling
statements about particular analyses, not guarantees for a given target,
but they identify the mechanism HMC is designed to remove: undirected,
step-by-step diffusion. [Gibbs sampling](gibbs-sampling.qmd) avoids a
proposal scale by sampling full conditional distributions, but it moves one
component, or one block, at a time, and can also move slowly when
components are strongly correlated.

## Definition — Momentum, Hamilton's equations, and the leapfrog integrator

### Augmenting the target with momentum

Let $q$ be a $d$-dimensional vector of variables of interest — in Bayesian
work, usually the parameters of a model — and let the target density for
$q$, known up to a normalising constant, be written $P(q)$. Define the
potential energy function

$$U(q) = -\log P(q),$$

where any additive constant may be absorbed into $U$, since only
differences of $U$ will matter. For a Bayesian posterior, Neal writes this
as $U(q) = -\log[\pi(q) L(q \mid D)]$, with $\pi(q)$ the prior density and
$L(q \mid D)$ the likelihood of data $D$ {{cite:neal2011_hmc}} (p. 123).

Now introduce a $d$-dimensional auxiliary vector $p$, the momentum, with a
distribution chosen by the user and independent of $q$. The standard choice
makes the components of $p$ independent normal variables, the $i$-th with
mean zero and variance $m_i$, where $m_i > 0$ is called a mass. This choice
is encoded in a kinetic energy function

$$K(p) = \sum_{i=1}^{d} \frac{p_i^2}{2 m_i},$$

which is $-\log$ of the Gaussian density for $p$, up to an additive
constant. In matrix form, with $M$ the diagonal matrix with entries
$m_1, \dots, m_d$, $K(p) = p^T M^{-1} p / 2$, and $M$ is called the mass
matrix {{cite:neal2011_hmc}} (pp. 115–116). The Hamiltonian is the total
energy

$$H(q, p) = U(q) + K(p).$$

Because $H$ separates into a term in $q$ and a term in $p$, the joint
density proportional to $\exp(-H(q, p))$ factorises:

$$\exp(-H(q, p)) = \exp(-U(q)) \exp(-K(p)) \propto P(q) \times (\text{Gaussian density of } p).$$

This is the canonical distribution construction: a distribution is
represented as $\exp(-E(x)) / Z$ for an energy function $E$, with $Z$ a
normalising constant {{cite:neal2011_hmc}} (p. 123). It follows that $q$
and $p$ are independent under the joint distribution, the marginal
distribution of $q$ is exactly the target, and sampling the joint
distribution and discarding $p$ is a valid way to sample the target — the
marginalisation idea used throughout
[Monte Carlo methods](monte-carlo-method.qmd), with the auxiliary variable
introduced for computational reasons. The momentum has no interpretation
in the original problem; it exists so that Hamiltonian dynamics has
something to act on.

### Hamilton's equations

Hamiltonian dynamics is the deterministic evolution of $(q, p)$ in time
$t$ governed by the partial derivatives of $H$:

$$\frac{d q_i}{d t} = \frac{\partial H}{\partial p_i},
\qquad
\frac{d p_i}{d t} = -\frac{\partial H}{\partial q_i}$$

{{cite:neal2011_hmc}} (p. 115). For the separated Hamiltonian above, these
become

$$\frac{d q_i}{d t} = \frac{p_i}{m_i},
\qquad
\frac{d p_i}{d t} = -\frac{\partial U}{\partial q_i},$$

where $\partial U / \partial q_i$ is minus the $i$-th partial derivative of
the log target density. The first equation says that position moves in the
direction of the momentum, at a rate set by the mass. The second says that
momentum is pulled towards regions of lower potential energy — that is,
towards higher target density — with a force given by the gradient. A
trajectory therefore does not simply run downhill and stop: as $q$ moves
into a region of lower $U$, $p$ grows, and the motion carries $q$ through
that region and up the far side, trading kinetic for potential energy and
back. Neal's physical picture is a frictionless puck sliding on a surface
whose height is $U(q)$ {{cite:neal2011_hmc}} (§2).

Three properties of the exact dynamics do the work in the algorithm.

**Conservation of energy.** Along any exact trajectory, $H$ is constant:
differentiating $H(q(t), p(t))$ and substituting Hamilton's equations gives
$dH/dt = 0$ identically {{cite:neal2011_hmc}} (p. 117). An exact trajectory
stays on a surface of constant total energy, and hence, by the factorisation
above, on a surface of constant joint density.

**Reversibility.** The mapping $T_s$ that carries a state at time $t$ to
its state at time $t + s$ is one-to-one, with inverse $T_{-s}$; when
$K(p) = K(-p)$, as for the quadratic kinetic energy, the inverse mapping is
also obtained by negating $p$, applying $T_s$, and negating $p$ again
{{cite:neal2011_hmc}} (p. 117).

**Volume preservation.** $T_s$ preserves volume in $(q, p)$ space: a region
of volume $V$ is mapped to a region of volume $V$. Neal notes that this is
Liouville's theorem, and that its significance for Monte Carlo is that no
Jacobian determinant enters the acceptance probability for a proposal
generated this way; for a general deterministic proposal mapping, that
determinant would have to be computed, and might be infeasible to compute
{{cite:neal2011_hmc}} (pp. 117–119).

One consequence is a limit as much as a property: because exact dynamics
conserves $H$, a trajectory alone explores only one energy surface. The
missing movement between energy surfaces is supplied by resampling the
momentum, as described below.

### The leapfrog integrator

Hamilton's equations cannot usually be solved in closed form, and are not
simulated exactly. Time is discretised with a step size $\varepsilon > 0$,
and the state is advanced in steps of $\varepsilon$. The discretisation
used in HMC is the leapfrog method. One leapfrog step, from time $t$ to
$t + \varepsilon$, consists of three sub-steps, applied componentwise:

$$p_i(t + \varepsilon/2) = p_i(t) - \frac{\varepsilon}{2} \frac{\partial U}{\partial q_i}(q(t)),$$

$$q_i(t + \varepsilon) = q_i(t) + \varepsilon \, \frac{p_i(t + \varepsilon/2)}{m_i},$$

$$p_i(t + \varepsilon) = p_i(t + \varepsilon/2) - \frac{\varepsilon}{2} \frac{\partial U}{\partial q_i}(q(t + \varepsilon)).$$

That is: a half step for the momentum, using the gradient at the current
position; a full step for the position, using the new momentum; and a
second half step for the momentum, using the gradient at the new position
{{cite:neal2011_hmc}} (pp. 121–122). When several steps are taken in
succession, the closing half step of one step and the opening half step of
the next combine into a single full momentum step, so the interior of a
trajectory alternates full position and full momentum updates, with half
steps only at the two ends {{cite:neal2011_hmc}} (p. 122).

Leapfrog is used, rather than a simpler scheme such as Euler's method,
because it is a symplectic integrator. Each of its three sub-steps is a
shear transformation — it shifts one set of coordinates by an amount
depending only on the other set — and each shear is a symplectic map,
as is any composition of symplectic maps. Two exact properties follow.
First, it preserves volume exactly: a symplectic map always does, and
the shears make this visible directly, since each has a Jacobian matrix
with determinant one {{cite:neal2011_hmc}} (p. 122). Second, the
composition is symmetric, so the integrator is reversible: negating
$p$, applying the same number of leapfrog steps, and negating $p$
again undoes the trajectory {{cite:neal2011_hmc}} (p. 122).
Symplecticity is the defining property; volume preservation is a
consequence of it, not its definition, and in more than two dimensions
volume preservation alone does not imply it. Betancourt's treatment
makes the same point about why symplectic integrators, specifically,
are suitable {{cite:betancourt2017_hmc}} (§5.1, p. 37).

What leapfrog does not retain is exact conservation of energy. Its local
error is of order $\varepsilon^3$, and its global error over a fixed time
interval is of order $\varepsilon^2$; Neal attributes the even order of
the global error to the method's reversibility {{cite:neal2011_hmc}} (p. 122). The computed $H$ therefore oscillates around, or drifts from,
its initial value along a trajectory, by an amount that is small when
$\varepsilon$ is small and the trajectory is stable, but is not zero.
Betancourt describes the effect geometrically: the numerical trajectory
follows a perturbed energy level set rather than the exact one
{{cite:betancourt2017_hmc}} (§5.2, p. 38). Exact simulation is not required,
because this error is not ignored — it is measured, through the change in
$H$, and corrected by the Metropolis step below.

Stability imposes a hard limit on $\varepsilon$. For the one-dimensional
Gaussian Hamiltonian $H(q, p) = q^2/(2\sigma^2) + p^2/2$, Neal shows that
leapfrog trajectories are stable when $\varepsilon < 2\sigma$ and unstable
when $\varepsilon > 2\sigma$, with $H$ then growing without bound; in
several dimensions the limit is governed, roughly, by the width of the
target in its most constrained direction {{cite:neal2011_hmc}} (§4.2). An
unstable trajectory's endpoint has an enormously larger $H$ than its
starting point and is rejected with probability effectively one.

### One HMC iteration

An iteration of HMC consists of two steps, each of which leaves the joint
canonical distribution of $(q, p)$ invariant {{cite:neal2011_hmc}} (p. 124).

**Step 1: resample the momentum.** Draw a new $p$ from its Gaussian
distribution, independently of the current $q$ and of the previous $p$.
Because $p$ is drawn from its correct conditional distribution given $q$
— the same as its marginal, by independence — this step leaves the joint
distribution invariant. It also moves the state between energy surfaces:
the new $p$ gives a new kinetic energy, hence a new total energy. Neal
stresses that without this resampling, $H$ would remain (nearly)
constant along a trajectory: the exact motion trades kinetic for
potential energy and back, but since $K \ge 0$, $U(q)$ could never
exceed the initial *total* energy, so the chain could not reach the
whole target {{cite:neal2011_hmc}} (p. 124).

**Step 2: a Metropolis proposal from a trajectory.** Starting from the
current $(q, p)$, take $L$ leapfrog steps of size $\varepsilon$, then
negate the momentum. Call the result $(q^*, p^*)$. Accept it as the next
state with probability

$$\min\left(1, \exp\left(H(q, p) - H(q^*, p^*)\right)\right)
= \min\left(1, \exp\left(-U(q^*) + U(q) - K(p^*) + K(p)\right)\right)$$

{{cite:neal2011_hmc}} (p. 124). If the proposal is rejected, the next state
is the current state, and the current $q$ is counted again in any average
over the chain. The negation of $p$ at the end of the trajectory makes the
proposal symmetric, which is what the acceptance formula above requires;
in practice the negation can be omitted when $K(p) = K(-p)$ and the
momentum is about to be resampled anyway, since $K$ is unchanged by it
{{cite:neal2011_hmc}} (p. 124).

Note what the acceptance probability depends on: the change in the total
energy, not the change in $U$ alone. If the dynamics were simulated
exactly, $H$ would be conserved, the exponent would be zero, and every
proposal would be accepted, however distant $q^*$ was from $q$. With
leapfrog, acceptance is governed by the accumulated energy error of the
trajectory. A trajectory that ends with $H$ slightly above its starting
value is accepted with probability slightly below one; one that ends with
$H$ below its starting value is accepted with probability one.

That this procedure has the correct invariant distribution is shown by
detailed balance. Neal's argument partitions $(q, p)$ space into small
regions of equal volume, uses reversibility to pair each region with its
image under the leapfrog-plus-negation mapping, uses volume preservation
to give the image the same volume, and then checks the detailed balance
identity directly from the acceptance formula {{cite:neal2011_hmc}} (pp. 124–126). Together with the invariance of the resampling step, this
gives a [Markov chain](markov-chain.qmd) for $q$ alone with the target as
its invariant distribution. Invariance is not convergence from an arbitrary
starting point: Neal notes that near periodicities of the trajectory — for
the one-dimensional Gaussian, a trajectory length near a multiple of the
period $2\pi$ — can make the chain slow or non-ergodic, and recommends
randomising $\varepsilon$ or $L$ over a small interval as a safeguard
{{cite:neal2011_hmc}} (p. 127).

## Properties — Tuning, divergences, and the No-U-Turn sampler

### Tuning: step size, trajectory length, and the mass matrix

HMC has two tuning quantities that ordinary use cannot avoid, $\varepsilon$
and $L$, and their roles are different and nearly separable
{{cite:neal2011_hmc}} (§4.2).

The step size $\varepsilon$ controls accuracy. Too large, and trajectories
become unstable or accumulate enough energy error that almost every
proposal is rejected; Neal notes that the error in $H$ usually does not
grow with the number of steps, provided $\varepsilon$ is small enough for
stability, so the choice of $\varepsilon$ is almost independent of $L$
{{cite:neal2011_hmc}} (§4.2). Too small, and computation is wasted: halving
$\varepsilon$ doubles the number of gradient evaluations needed to cover
the same integration time. In Neal's scaling analysis for high-dimensional
targets, the acceptance probability that minimises cost at fixed accuracy
is about $0.65$ {{cite:neal2011_hmc}} (§4.4) — a figure for the setting
analysed there, not a universal target, but the reason practical tuning
aims for a high, not a near-one, acceptance rate.

The number of steps $L$, through the integration time $\varepsilon L$,
controls how far a single iteration travels. If $\varepsilon L$ is too
short, successive $q$ values are close and, because the momentum is
resampled each iteration, the chain again explores by something close to a
random walk, at much greater cost per step. If it is too long, the
trajectory wastes computation and may turn back on itself: Neal's
two-dimensional Gaussian trajectory with correlation $0.95$, computed with
$L = 25$ steps of $\varepsilon = 0.25$, reverses direction part-way and
ends with an energy error of $+0.41$, giving an acceptance probability of
$\exp(-0.41) \approx 0.66$ {{cite:neal2011_hmc}} (pp. 128–129). Neal's
practical advice is trial and error from preliminary runs — $L = 100$ as
a starting trial for a difficult problem, $L = 1000$ if autocorrelation
remains high — judged by trace plots and autocorrelation of slowly moving
quantities {{cite:neal2011_hmc}} (§4.2). In his 100-dimensional Gaussian
illustration, with coordinate standard deviations from $0.01$ to $1.00$,
HMC used $L = 150$ with $\varepsilon$ drawn uniformly from
$(0.0104, 0.0156)$ per iteration, and its rejection rate was $0.13$
against $0.75$ for a comparably tuned random-walk Metropolis
{{cite:neal2011_hmc}} (§3.3). That example also shows the constraint the
mass matrix addresses: with all masses equal, the step size is limited by
the narrowest coordinate, while the trajectory must traverse the widest.

The mass matrix $M$ — equivalently, in Betancourt's geometric language,
the metric that defines the kinetic energy — rescales the problem. The
convention matters: with kinetic energy $p^\top M^{-1} p / 2$ the momentum
is drawn with covariance $M$, and for a Gaussian target with covariance
$\Sigma$ Hamilton's equations give $\ddot{q} = -M^{-1} \Sigma^{-1} q$, so
the directions evolve on a common timescale when $M^{-1}$ approximates
$\Sigma$. It is the inverse mass that should match the target's
covariance — equivalently, the masses themselves should be large where
the target is narrow and small where it is wide — and setting the $m_i$
that way makes the dynamics treat all directions more evenly
{{cite:neal2011_hmc}} (§4.1). Betancourt develops this as the choice
of a Euclidean metric, notes that the ideal choice makes the inverse metric
resemble the covariance of the target, and describes estimating that
covariance during an initial window and then fixing the metric
{{cite:betancourt2017_hmc}} (§4.2, p. 31). A single fixed metric can only correct
global scale and correlation: where the target's local scale varies with
position — the funnel geometry below — no constant $M$ is right everywhere,
which is the motivation for the position-dependent (Riemannian) kinetic
energies Betancourt also discusses {{cite:betancourt2017_hmc}} (§4.2, pp. 31–32).

### Divergences as a diagnostic

A divergent transition is a leapfrog trajectory whose computed energy error
grows explosively, rather than oscillating within a modest range.
Betancourt's account gives divergences a specific diagnostic meaning.
Regions where the target has very high curvature — narrow necks and sharp
funnels, characteristic of hierarchical models — cannot be resolved by a
leapfrog step of the size that works elsewhere; a trajectory entering such
a region becomes unstable and diverges, and the sampler then fails to
explore that region properly, which biases estimates based on the chain
{{cite:betancourt2017_hmc}} (§6.2, p. 45). Because the integrator fails exactly
where the geometry is pathological, Betancourt argues that divergent
transitions are "extremely sensitive identifiers" of those regions, and
that any divergences should prompt suspicion of the validity of the
resulting estimates {{cite:betancourt2017_hmc}} (§6.2, p. 45). Reducing
$\varepsilon$ removes divergences when the pathology is mild; when they
persist at any step size, his recommendation is to change the target
itself — stronger priors, or a different parametrisation, such as
alternating between centred and non-centred parametrisations in latent
Gaussian models {{cite:betancourt2017_hmc}} (§6.2, p. 45).

A funnel makes this concrete. In a hierarchical model where a group-level
scale parameter can approach zero, the conditional distribution of the
group parameters collapses as the scale shrinks: in the neck of the funnel
the target is confined to a very narrow region in some directions, while
in the mouth it is wide. A single $\varepsilon$ cannot be small enough for
the neck and efficient in the mouth, and trajectories that approach the
neck diverge or are rejected, so the neck is under-explored. Divergences
concentrated at small values of the scale parameter are the observable
signature. Betancourt also records the limit of the diagnostic: absence of
divergences does not certify adequate exploration, since a pathology the
trajectories never reach produces no divergence to report
{{cite:betancourt2017_hmc}} (§6.3, p. 45).

### The No-U-Turn Sampler

The sensitivity of HMC to $L$ is the specific problem the No-U-Turn Sampler
(NUTS) of Hoffman and Gelman was built to remove. Their statement of the
problem is that if $L$ is too small, HMC exhibits random-walk behaviour,
and if $L$ is too large, it wastes computation; and that, unlike
$\varepsilon$, $L$ could not then be tuned by the standard adaptive
methods, so setting it required costly tuning runs
{{cite:hoffman_gelman2014}} (§1, p. 1594). NUTS eliminates the need to set $L$ by
building the trajectory adaptively within each iteration and stopping when
the trajectory begins to double back on itself.

In outline — a summary of the construction, not a substitute for the
algorithm as published — NUTS proceeds as follows
{{cite:hoffman_gelman2014}} (§3, pp. 1597–1606). It introduces a slice variable drawn so
that the current state lies in the slice it defines, which is used to
select candidate states along the trajectory in a way that preserves
detailed balance. It then extends the trajectory by repeated doubling:
at each stage it adds, in a randomly chosen direction (forwards or
backwards in time), as many leapfrog steps again as the trajectory built
so far contains, so the set of states forms a balanced binary tree whose
leaves are position–momentum states. Two conditions in this construction
must not be conflated. A state that falls outside the slice is excluded
from the candidate set, but doubling does not stop there: a newly
generated state stops the doubling only when its log joint density falls
below $\log u - \Delta_{\max}$, the threshold at which the energy error
is treated as out of control, or when the subtrajectory between the
endpoints of any balanced subtree begins to make a U-turn — formally,
when the vector from one endpoint to the other has a negative dot
product with the momentum at either endpoint, meaning the endpoints
are starting to approach each other {{cite:hoffman_gelman2014}} (Algorithm 3, p. 1606).
That criterion is stated for an identity mass matrix; with a general
mass matrix the momenta in the dot products are replaced by the
velocities $M^{-1} p$, not reused unchanged.
A candidate is then selected from the admissible
states in the tree. Hoffman and Gelman also give a dual-averaging
procedure, based on Nesterov's primal–dual averaging, that adapts
$\varepsilon$ during an initial phase towards a target average acceptance
statistic, so that NUTS can be run with no hand-tuning of either quantity
{{cite:hoffman_gelman2014}} (§3.2, pp. 1607–1609). Their empirical finding was that
this tuning-free version performed at least as efficiently as, and
sometimes more efficiently than, a well-tuned standard HMC, per effective
sample and ignoring the cost of tuning the latter
{{cite:hoffman_gelman2014}} (§4.4, pp. 1616–1618).

## Worked example — One Gaussian, four leapfrog steps

Take the simplest possible target: a standard normal density for a scalar
$q$, so that, up to an additive constant,

$$U(q) = \frac{q^2}{2}, \qquad K(p) = \frac{p^2}{2}, \qquad
H(q, p) = \frac{q^2 + p^2}{2},$$

with mass $m = 1$. Hamilton's equations are $dq/dt = p$ and $dp/dt = -q$,
whose solutions are rotations in the $(q, p)$ plane: for initial state
$(q_0, p_0)$,

$$q(t) = q_0 \cos t + p_0 \sin t, \qquad p(t) = -q_0 \sin t + p_0 \cos t$$

{{cite:neal2011_hmc}} (p. 116). Start a trajectory at $q_0 = 0.5$,
$p_0 = 1.0$, so $H(q_0, p_0) = (0.25 + 1)/2 = 0.625$ exactly. Take $L = 4$
leapfrog steps with $\varepsilon = 0.5$, a total integration time of
$2.0$. Since $dU/dq = q$, each step is: $p \leftarrow p - 0.25 q$ (half
step); $q \leftarrow q + 0.5 p$ (full step); $p \leftarrow p - 0.25 q$
(half step, at the new $q$). The computed trajectory, with $H$ evaluated at
each step, is:

| Step | $p$ after half step | $q$ | $p$ | $H(q, p)$ |
|---:|---:|---:|---:|---:|
| 0 (start) | — | 0.500000 | 1.000000 | 0.625000 |
| 1 | 0.875000 | 0.937500 | 0.640625 | 0.644653 |
| 2 | 0.406250 | 1.140625 | 0.121094 | 0.657845 |
| 3 | −0.164062 | 1.058594 | −0.428711 | 0.652207 |
| 4 | −0.693359 | 0.711914 | −0.871338 | 0.633026 |

Reading the first step in full: the half step gives
$p = 1.0 - 0.25 \times 0.5 = 0.875$; the position step gives
$q = 0.5 + 0.5 \times 0.875 = 0.9375$; the closing half step gives
$p = 0.875 - 0.25 \times 0.9375 = 0.640625$. The remaining steps repeat the
same three operations.

Three features of the table are the points of the example. First, $H$ is
not conserved by the leapfrog trajectory: it rises to $0.657845$ at step 2
and falls back to $0.633026$ at step 4. The energy error at the endpoint,
which is all the Metropolis step sees, is
$H(q^*, p^*) - H(q_0, p_0) = 0.633026 - 0.625000 = +0.008026$. Second, the
acceptance probability for the proposal $q^* = 0.711914$ is therefore

$$\min\left(1, \exp(0.625000 - 0.633026)\right) = \exp(-0.008026) \approx 0.992006,$$

so this distant proposal — $q$ has moved from $0.5$ to about $0.71$, by way
of $1.14$ — is accepted with probability about $0.992$. Third, the
leapfrog endpoint is close to, but not equal to, the exact endpoint. The
exact trajectory at $t = 2$ is
$q(2) = 0.5 \cos 2 + \sin 2 \approx 0.701224$ and
$p(2) = -0.5 \sin 2 + \cos 2 \approx -0.870796$, with $H$ exactly $0.625$.
The leapfrog errors at the endpoint are $+0.010690$ in $q$ and $-0.000542$
in $p$: small at this step size, and exactly the sort of error the
acceptance probability above corrects for. With $\varepsilon$ near the
stability limit of $2$ for this target ($\sigma = 1$), the errors, and the
energy error in particular, would be far larger.

## Statistical use — Where HMC is used, and its strengths

HMC, usually in its NUTS form, is the default sampler in general-purpose
probabilistic programming systems such as Stan, and is used for Bayesian
posterior sampling in hierarchical, latent-variable and other
continuous-parameter models where random-walk Metropolis mixes too slowly
and where full conditional distributions for Gibbs sampling are unavailable
or highly correlated. Its strengths follow from the construction: proposals
are distant yet frequently accepted, exploration is directed rather than
diffusive, and the energy error is observable at every iteration, giving
an internal diagnostic — in the acceptance rate, and in divergences —
that random-walk methods do not supply.

## Common misconceptions

**"HMC accepts almost every proposal, so tuning hardly matters."** High
acceptance is easy to obtain by making $\varepsilon$ very small or
$\varepsilon L$ very short, at the cost of wasting gradient evaluations or
reintroducing random-walk behaviour. The relevant measure is cost per
effectively independent draw, and Neal's analysis puts the cost-minimising
acceptance probability near $0.65$ in the high-dimensional setting
analysed, well below one {{cite:neal2011_hmc}} (§4.4).

**"The trajectory follows the exact dynamics, so no correction is
needed."** The trajectory follows leapfrog dynamics, which conserve neither
$H$ nor the target density exactly. In the worked example, four steps at
$\varepsilon = 0.5$ produced an energy error of $+0.008026$ and an
acceptance probability of $0.992006$, not $1$. The Metropolis step using
the change in $H$ is part of the algorithm, not an optional
refinement; omitting it leaves a chain with no known invariant
distribution — the numerical dynamics are not known to preserve the
target, or any definite perturbation of it, exactly.

**"Resampling the momentum is a minor implementation detail."** It is the
step that moves the chain between energy levels. Confinement by energy
is a statement about the exact flow: exact dynamics conserve $H$, and
since $K \ge 0$ a position with $U(q) > H$ is then ruled out by energy
alone. That excludes less than is often assumed — in the worked example
below, with $H = 0.625$, the energetically allowed interval
$|q| \le \sqrt{1.25}$ already carries about $0.7364$ of the target
probability. Without resampling, nothing redraws the momentum, so the
chain cannot move between energy levels with the frequencies the
canonical distribution assigns them {{cite:neal2011_hmc}} (p. 124).

**"A divergent transition is just a rejected proposal."** A rejection at a
well-behaved endpoint is routine. A divergence signals that the integrator
entered a region whose curvature the step size could not resolve, and that
the region is consequently under-explored; Betancourt's recommendation is
to treat any divergences as grounds for suspecting the estimates, not as
wasted iterations to be ignored {{cite:betancourt2017_hmc}} (§6.2, p. 45).

**"NUTS has no tuning parameters, so no checking is needed."** NUTS removes
the need to set $L$ by hand and adapts $\varepsilon$, but it retains a mass
matrix, a target acceptance statistic for the adaptation, and maximum
limits on the doubling; and its output requires the same convergence and
divergence checks as any HMC run {{cite:hoffman_gelman2014}} (§3, Algorithm 6, p. 1611).

**"HMC handles any posterior, including discrete parameters."** It does
not. The state space must be continuous and the log density differentiable
(almost everywhere); discrete parameters have to be marginalised out or
updated by a different method {{cite:neal2011_hmc}} (p. 124).

## Assumptions and limits — Gradients, tuning, and geometry

Its limits are equally specific.

**A gradient is required.** The target density must be differentiable, and
its gradient computable at every point of every trajectory; Neal allows
non-differentiability only on a set of probability zero
{{cite:neal2011_hmc}} (p. 124). Each leapfrog step costs at least one
gradient evaluation, so a trajectory of $L$ steps costs at least $L$ per
iteration, whether or not its endpoint is accepted.

**Continuous parameters only.** HMC samples from continuous distributions
on $\mathbb{R}^d$ {{cite:neal2011_hmc}} (p. 124). A discrete parameter has
no gradient and no Hamiltonian trajectory; discrete parameters must be
summed out (marginalised) before sampling, handled by another update
within a larger scheme, or the model must be reformulated. There is no
leapfrog update for a parameter that takes values in a finite set.

**Tuning is costly, and bad tuning is not benign.** Performance depends
critically on $\varepsilon$ and $L$ {{cite:neal2011_hmc}} (§5.6), and the
best values can differ between regions of the target: a step size stable
in one region can be unstable in another that preliminary runs never
reached, in which case the chain may fail to visit that region and produce
a drastically wrong result while appearing well behaved
{{cite:neal2011_hmc}} (§4.2). NUTS and dual averaging reduce this burden;
they do not remove the need to choose a mass matrix, nor fix a target
whose geometry defeats a constant metric.

**Difficult geometry remains difficult.** Isolated modes are not crossed
by Hamiltonian trajectories any more readily than by other local updates;
Neal notes that HMC is neither more nor less vulnerable here than other
local MCMC methods, and that combining runs each confined to one mode is
not valid {{cite:neal2011_hmc}} (§4.2). Funnels and other regions of
extreme, position-dependent curvature produce divergences and biased
exploration, as described above. Heavy tails can also defeat a poorly
chosen kinetic energy, a failure Betancourt discusses under geometric
ergodicity {{cite:betancourt2017_hmc}} (§6.1, p. 44).

**The output is a dependent sample.** As with any MCMC method, the retained
$q$ values are correlated draws whose averages estimate posterior
expectations only once the chain has converged and run long enough; HMC
changes how efficiently that point is reached, not what has to be checked.

## Connections

- [Metropolis–Hastings algorithm](metropolis-hastings-algorithm.qmd) — HMC
  is a Metropolis–Hastings method whose proposal is the endpoint of a
  Hamiltonian trajectory.
- [Gibbs sampling](gibbs-sampling.qmd) — updates components from their full
  conditionals, where HMC updates all components jointly along a trajectory.
- [Monte Carlo method](monte-carlo-method.qmd) — expectations estimated by
  averages over simulated draws; HMC supplies draws that direct simulation
  cannot reach.
- [Markov chain](markov-chain.qmd) — HMC's chain on the augmented
  $(q, p)$ space has an invariant distribution whose $q$-marginal is the target.
- [Variational inference](variational-inference.qmd) — optimises an
  approximating distribution rather than simulating a chain, trading HMC's
  asymptotic exactness for speed.
- [Importance sampling](importance-sampling.qmd) — weights independent draws
  rather than running a chain; it degrades in high dimensions in ways HMC
  was designed to avoid.
- [Dirichlet process](dirichlet-process.qmd) — models built on it routinely
  produce hierarchical posteriors with funnel-like geometry, where HMC's
  divergence diagnostics are frequently exercised.

## History

The method originated outside statistics. In 1987, Duane, Kennedy,
Pendleton and Roweth united molecular dynamics simulation with Monte Carlo
sampling in a paper they called "Hybrid Monte Carlo", applied to lattice
field theory calculations in quantum chromodynamics; this account of the
paper's content and application is Neal's {{cite:neal2011_hmc}} (pp. 113–114). Its bibliographic details, as given in the reference lists
of both Neal and Betancourt, are: Duane, S., Kennedy, A. D., Pendleton,
B. J. and Roweth, D. (1987), "Hybrid Monte Carlo", *Physics Letters B*,
195, 216–222 {{cite:betancourt2017_hmc}} (p. 59). Neal records that
statistical applications began with his own use of the method for neural
network models, and that he gave a statistically oriented tutorial in a
1993 review {{cite:neal2011_hmc}} (pp. 113–114). Betancourt adds that
MacKay's 2003 book first used the name "Hamiltonian Monte Carlo", and
that Neal's 2011 review brought the method into the mainstream of
statistical computing, with implementations such as Stan then making it
pervasive {{cite:betancourt2017_hmc}} (p. 3). The No-U-Turn Sampler
followed in 2014 {{cite:hoffman_gelman2014}} (abstract, p. 1593).

## Check yourself

1. In the worked example, the leapfrog trajectory ends at
$q^* = 0.711914$, $p^* = -0.871338$, with $H(q^*, p^*) = 0.633026$ against
a starting $H$ of $0.625$. A second trajectory is proposed from the same
starting state but with a coarser discretisation, and ends with
$H(q^*, p^*) = 0.725$. What is the acceptance probability in each case,
and why is the first not exactly $1$ even though the target is a single
Gaussian?

::: {.callout-tip collapse="true" title="Answer"}

For the worked example, the acceptance probability is
$\min(1, \exp(0.625 - 0.633026)) = \exp(-0.008026) \approx 0.992006$. For
the coarser trajectory it is $\exp(0.625 - 0.725) = \exp(-0.1) \approx
0.905$. The first is not exactly $1$ because the proposal was generated by
leapfrog integration, which does not conserve $H$ exactly: the endpoint's
total energy is $0.008026$ above the starting value, and the Metropolis
acceptance probability $\min(1, \exp(H_{\text{old}} - H_{\text{new}}))$
converts exactly that energy error into a rejection chance. Exact
Hamiltonian dynamics would conserve $H$ and always be accepted.

:::

2. Suppose an HMC implementation is modified so that the momentum is drawn
once, at the start of the run, and never resampled: each iteration simply
continues the trajectory from where the previous one ended, with the
Metropolis step retained. Why can this chain not sample the target
correctly, however long it runs?

::: {.callout-tip collapse="true" title="Answer"}

Under the exact dynamics the total energy $H(q, p)$ is conserved, so a
trajectory stays on the energy surface of the initial draw; leapfrog
dynamics conserve $H$ only approximately. The Metropolis step is not a
hard energy tube either: for a finite energy change it accepts every
proposal that lowers $H$, and accepts one that raises $H$ by $\Delta H$
with probability $\exp(-\Delta H)$. But those accepted energy changes are
only integration errors — nothing in the modified algorithm ever redraws
the momentum, so the chain cannot visit energy levels with the
frequencies the canonical distribution assigns them, and the position
marginal is not the target. (Energy alone also rules out less than one
might think: a position with $U(q) > H$ is unreachable at energy $H$,
since $K(p) \ge 0$, but how much of the target that excludes depends on
the draw.) Resampling $p$ at each iteration is what changes $H$ and lets
the chain move between energy surfaces.

:::

3. A run of NUTS on a hierarchical model reports several hundred divergent
transitions, almost all of them occurring when a group-level scale
parameter is close to zero, and no divergences elsewhere. Reducing the
step size by a factor of two does not remove them. What is the likely
geometry responsible, what does it imply for the estimates from this run,
and what are the two kinds of remedy available?

::: {.callout-tip collapse="true" title="Answer"}

The pattern is the signature of a funnel: as the scale parameter
approaches zero, the conditional distribution of the group parameters
collapses, so the target's curvature in the neck is far greater than in
its mouth, and no single step size resolves both. Trajectories entering
the neck diverge, so the neck is under-explored and estimates from the run
should be treated as suspect. The two kinds of remedy are to change the
computation — already tried here, in the form of a smaller step size, and
failed — and to change the target: strengthen the prior on the scale
parameter, or reparametrise the model; for a latent Gaussian hierarchy, a
non-centred parametrisation removes the funnel by construction.

:::
