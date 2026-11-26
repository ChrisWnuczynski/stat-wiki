## Lead context

Importance sampling is a [Monte Carlo method](monte-carlo-method.qmd) for
estimating an expectation under a distribution that is hard to sample from,
or under which the quantity of interest is rarely seen, by sampling instead
from a second, more convenient distribution and correcting each draw with a
weight. If $p$ is the density of the target distribution, $h$ is the
function whose expectation is wanted, and $q$ is the density of the
proposal distribution actually sampled, the correction is the ratio
$w(x) = p(x)/q(x)$, and the estimate is a weighted average of the values
$h(x_i)$ at the proposal draws. The method appears as the second of the
general strategies listed by Hastings in 1970 for problems in which direct
sampling from $p$ is difficult: sample from $q$ instead, and estimate the
integral $\int h(x) p(x)\, dx$ by averaging $h(x_i) p(x_i)/q(x_i)$
{{cite:hastings1970}} (§1, p. 97). It is used in two distinct situations. In the first, $p$ is fully known
and sampling from $q$ is a device for reducing variance, as when a rare
event is made common under $q$ so that it is actually observed. In the
second, $p$ is known only up to a normalising constant — the usual
situation for a Bayesian posterior — and a ratio form, the self-normalised
estimator, is required. Tokdar and Kass describe importance sampling as a
collection of Monte Carlo methods built on this single identity, used
together with Markov chain Monte Carlo as a foundation for simulation-based
numerical integration {{cite:tokdar_kass2010}} (p. 54).

## Definition — The identity and the support condition

Let $X$ be a random quantity with density $p$ with respect to a common
reference measure (Lebesgue measure for a continuous variable, counting
measure for a discrete one), and let $h$ be a real-valued function. The
target is

$$\mu = \E_p[h(X)] = \int h(x) p(x)\, dx,$$

where $E_p$ denotes expectation under $p$ and the integral is over the
whole space of possible values of $X$. Let $q$ be a second density, the
proposal. Wherever $q(x) > 0$, the integrand can be multiplied and divided
by $q(x)$ without changing its value:

$$\mu = \int h(x) \frac{p(x)}{q(x)} q(x)\, dx = \E_q[h(X) w(X)],$$

where $E_q$ denotes expectation under $q$ and
$w(x) = p(x)/q(x)$ is the importance weight at $x$. The identity is exact; no approximation has been made. What has changed
is the distribution from which draws are taken.

The division is legitimate only where it is needed. The precise requirement
is the support condition: $q(x) > 0$ wherever $|h(x)| p(x) > 0$. If $q$
assigns density zero to a set on which $h(x) p(x)$ is nonzero, draws from
$q$ never fall in that set, its contribution to $\mu$ is never seen, and
the estimator converges to the integral over the part of the space that $q$
does reach — a wrong value, reached with no warning from the sample itself.
Tokdar and Kass state the condition in the form $q(x) > 0$ whenever
$f(x) p(x) \ne 0$, with $f$ in the role of $h$ here
{{cite:tokdar_kass2010}} (p. 54, eq. (2)). Owen gives the same condition
and notes the safer sufficient version: choose $q$ positive wherever $p$
is positive, which covers every $h$ at once {{cite:owen2013_mc}} (§9.1).
For the self-normalised estimator (treated under 'The self-normalised
estimator' below) the stronger version is the one required, because its
denominator estimates an integral of $p$
itself, for which the relevant function is the constant $1$, not $h$
{{cite:owen2013_mc}} (§9.2).

## Properties — The plain estimator, its variance, the proposal, and the self-normalised form

### The estimator when $p$ is normalised

Suppose first that $p$ is a fully specified, normalised density, so that
$w(x)$ can be computed exactly. Draw $x_1, \dots, x_N$ independently from
$q$. The importance sampling estimator is

$$\widehat{\mu} = \frac{1}{N} \sum_{i=1}^{N} h(x_i) w(x_i).$$

It is exactly unbiased, not merely approximately: each term has expectation
$\E_q[h(X) w(X)] = \mu$ by the identity above, provided the support
condition holds and $\E_p[|h(X)|]$ is finite. Hastings writes the estimator
in exactly this form, as the average of $h(x_i) p(x_i)/q(x_i)$ over a sample
drawn from $q$ {{cite:hastings1970}} (§1, p. 97). By the strong law of large numbers $\widehat{\mu}$ converges to
$\mu$ with probability one as $N \to \infty$, and by the central
limit theorem its error is approximately normal with variance given
in the next section, whenever the second moment
$\E_q[h(X)^2 w(X)^2]$ is finite. That moment condition belongs to
this estimator. The self-normalised ratio form has its own central
limit theorem, with a different, centred moment condition, stated
in its section below; neither condition covers both estimators.
Tokdar and Kass record the strong law and the central limit results
for the two forms separately {{cite:tokdar_kass2010}} (p. 54).

Two special cases fix the meaning of the weights. If $q = p$, then
$w(x) = 1$ for all $x$ and the estimator is the ordinary Monte Carlo
average of $h$ over draws from $p$. If $h$ is the indicator of a set $A$,
the estimator is the average of the weights of the draws that fall in $A$;
draws outside $A$ contribute exactly zero, however large their weights.

### Variance: the weights decide everything

Unbiasedness says nothing about precision. Because the terms
$h(x_i) w(x_i)$ are independent draws from $q$, the exact variance of the
estimator, when it is finite, is

$$\text{Var}_q(\widehat{\mu}) = \frac{1}{N}\left( \int \frac{h(x)^2 p(x)^2}{q(x)}\, dx - \mu^2 \right) = \frac{1}{N}\left( \E_q[h(X)^2 w(X)^2] - \mu^2 \right).$$

Owen writes the per-draw variance in this form and draws the two practical
conclusions from it: the numerator rewards a proposal close to
$|h| p$ in shape, and the denominator punishes a proposal that comes close
to zero anywhere that $|h| p$ does not {{cite:owen2013_mc}} (§9.1). The
variance is small when $q$ places its draws where $|h(x)| p(x)$ is large
and when the weights of the drawn points are nearly constant. It is large
— and can be infinite — when some draws carry weights vastly larger than
others.

The benchmark case $h \equiv 1$, for which $\mu = 1$ exactly, isolates the
role of the weights. The per-draw variance is then
$\E_q[(w(X) - 1)^2] = \E_q[w(X)^2] - 1$, since $\E_q[w(X)] = \int p(x)\, dx = 1$.
Tokdar and Kass give this as $\text{Var}(\widehat{\mu}_f) = \E_q[(w(X)-1)^2]/m$
for a sample of size $m$ when the function is identically $1$
{{cite:tokdar_kass2010}} (p. 54, eq. (5)). The quantity
$\E_q[w(X)^2] - 1$ is the chi-squared divergence between $p$ and $q$,

$$D_{\chi^2}(p \, \| \, q) = \int \frac{(p(x) - q(x))^2}{q(x)}\, dx = \int \frac{p(x)^2}{q(x)}\, dx - 1,$$

so the difficulty of estimating even a constant under $p$ by sampling from
$q$ is exactly a divergence between the two densities. For a general $h$
the relevant second moment is $\E_q[h(X)^2 w(X)^2]$, which can be much
smaller than the worst case suggested by the divergence when $h$ is small
where the weights are large — the first worked example below turns on
exactly this point — or much larger, when $h$ is large where the weights
are large. A small chi-squared divergence is a guarantee for all $h$ that
are nearly constant under $p$; Tokdar and Kass use the same quantity,
written $cv^2 = \E_q[(w(X)-1)^2]$, as the efficiency criterion to be
minimised when choosing among parametric proposals
{{cite:tokdar_kass2010}} (pp. 55–56, eq. (6)).

For nonnegative $h$ there is an optimal proposal,
$q^*(x) = h(x) p(x)/\mu$, proportional to $h p$. Under $q^*$ every term
$h(x_i) w(x_i)$ equals $\mu$ exactly, so the estimator has variance zero.
This is a benchmark, not a method: $q^*$ depends on the unknown $\mu$, and
sampling from it is usually as hard as the original problem. Its practical
content is directional — a good proposal mimics the shape of $|h| p$, not
the shape of $p$ alone {{cite:owen2013_mc}} (§9.1). For an indicator $h$,
$q^*$ is the distribution of $X$ under $p$ conditional on $X \in A$: the
ideal way to estimate a rare-event probability is to sample from the event
itself, reweighted.

### Choosing the proposal: tails, tilting and defensive mixtures

Three requirements compete. The proposal must be easy to sample from; its
density must be computable at the drawn points; and its shape must follow
$|h| p$ closely enough that the weights do not vary wildly. The precise
form of the third requirement is a moment condition, not a tail
comparison: the variance is finite exactly when
$\E_q[h(X)^2 w(X)^2] = \int h(x)^2 p(x)^2/q(x)\, dx$ is finite. Tail
thickness is a heuristic for that integral, no more. A proposal with
thinner tails than the target can still satisfy it: for $h \equiv 1$,
a $N(0,1)$ target and a $N(0, 3/4)$ proposal, $p^2/q$ is proportional
to $\exp(-x^2/3)$ and is integrable, even though the proposal's tails
are thinner; the same comparison with proposal variance at most $1/2$
makes the integral diverge. What is fatal is not thinness itself but a
ratio $p^2/q$ that grows fast enough, in a region $q$ still visits, to
defeat integrability. Owen's tail comparison is the practical guidance:
a normal target with a Student $t$ proposal is safe, while a $t$ target
with a normal proposal is problematic {{cite:owen2013_mc}} (§9.1).

In Bayesian problems a standard construction takes $q$ to be a normal or
Student $t$ density centred at the posterior mode, with scale from the
curvature of the log posterior at the mode — an importance-sampling version
of the Laplace approximation. Tokdar and Kass describe this construction,
with the mode found by minimising $-\log p(x)$ and the scale from the
inverse Hessian there, and record the usual preference for the Student
version: its heavier tails give greater assurance that
$\E_q[w(X)^2]$ is finite {{cite:tokdar_kass2010}} (p. 55). Owen likewise
recommends a $t$ distribution rather than a normal for safety when a
Gaussian proposal is built from a mode and a Hessian
{{cite:owen2013_mc}} (§9.7).

A second construction changes a parameter of the target family itself.
Exponential tilting takes a proposal from the same family as $p$ with a
shifted parameter — the $N(0,1)$ target and $N(3,1)$ proposal of the first
worked example are the simplest instance — and Owen treats it as the
standard device for rare-event problems {{cite:owen2013_mc}} (§9.6).

A third construction insures against a proposal that is wrong somewhere.
A defensive mixture combines a best-guess proposal $q_2$ with a safe
component $q_1$ — in the original defensive construction, the target $p$
itself — as $q_\alpha = \alpha_1 q_1 + \alpha_2 q_2$ with
$\alpha_1 + \alpha_2 = 1$ and, for example, $\alpha_1 = 1/10$. Because
$q_\alpha(x) \ge \alpha_1 p(x)$ everywhere, the weight satisfies
$w(x) \le 1/\alpha_1$ for all $x$: the weights are bounded, and the second
moment of the weights themselves, $\E_q[w(X)^2]$, is at most $1/\alpha_1$.
That bound is a statement about the weights, and it secures finite
variance for the plain estimator of a bounded integrand — in particular
for the constant $1$, the normalising-constant problem. It does not by
itself control $\E_q[w(X)^2 h(X)^2]$ for an unbounded $h$: with $p = q$
uniform on $(0,1)$ the weights are identically $1$, yet $h(x) = x^{-3/4}$
has finite mean $4$ while $\E_q[w(X)^2 h(X)^2] = \int_0^1 x^{-3/2}\, dx$
is infinite, so that estimator has infinite variance despite perfectly
bounded weights. The finite-variance condition remains the moment
condition on the product, $\E_q[w(X)^2 h(X)^2] < \infty$; bounded weights
are a way to meet it for bounded $h$, not a substitute for it. The price
of the insurance is spending a fraction $\alpha_1$ of the draws on the
safe component. Owen presents defensive mixtures, attributed there to
Hesterberg (1995), as the way to bound the importance ratio while keeping
a tuned component {{cite:owen2013_mc}} (§9.10). Mixtures serve a second
purpose as well: one component can be placed at each mode, singularity or
failure mechanism that is known about, so that no important region depends
on a single component having found it {{cite:owen2013_mc}} (§9.10).

### The self-normalised estimator

In [Bayesian inference](bayesian-inference.qmd) the target is a posterior
density, and Bayes' rule supplies it only as an unnormalised density
$\tilde{p}(x) = L(x) \pi(x)$, the product of a likelihood $L$ and a prior
density $\pi$, with $p(x) = \tilde{p}(x)/Z$ and
$Z = \int \tilde{p}(x)\, dx$ the marginal likelihood of the data under the
model. The constant $Z$ is generally unknown — computing it is itself one
of the hard integrals of the subject — so the exact weights $p(x)/q(x)$
cannot be formed. What can be formed is the unnormalised weight
$\tilde{w}(x) = \tilde{p}(x)/q(x) = Z w(x)$, which differs from the exact
weight by the same unknown factor $Z$ at every point.

The factor cancels in a ratio — but the derivation needs the
stronger support condition, and needs it here, not as a later
caveat: $q(x) > 0$ wherever $\tilde{p}(x) > 0$, equivalently
wherever $p(x) > 0$. The denominator of the ratio estimates
$Z = \int \tilde{p}(x)\, dx$, the expectation of the constant
function $1$ against the unnormalised target, and the identity for
that expectation requires $q$ positive wherever $\tilde{p}$ is —
including where $h$ vanishes. Under only the weaker, $h$-dependent
condition of the first section, the numerator could still target
$Z\mu$ while the denominator targets the integral of $\tilde{p}$
over just the part of the space $q$ reaches, and the ratio would
converge to a wrong value. Impose the strong condition from the
start. Both $\mu = \E_p[h(X)]$ and $1$ are then expectations that
the unnormalised weights can estimate: applied to $h$, the plain
estimator with $\tilde{w}$ in place of $w$ estimates $Z\mu$;
applied to the constant function $1$, it estimates $Z$. Dividing
the first by the second gives the self-normalised estimator

$$\widetilde{\mu} = \frac{\sum_{i=1}^{N} \tilde{w}(x_i) h(x_i)}{\sum_{i=1}^{N} \tilde{w}(x_i)} = \frac{\sum_{i=1}^{N} w(x_i) h(x_i)}{\sum_{i=1}^{N} w(x_i)},$$

a weighted average of the values $h(x_i)$ with normalised weights
$w_i / \sum_j w_j$ that sum to one — defined only when the
denominator is positive. The weights are nonnegative, so the
denominator vanishes exactly when every drawn point has
$\tilde{w}(x_i) = 0$, an event of positive probability whenever $q$
can draw points at which $\tilde{p}$ is zero. Every statement about
$\widetilde{\mu}$ below is conditional on the denominator being
positive; under the support condition that event has probability
tending to one, but it is not certain at any finite $N$. Tokdar and Kass give this ratio
estimate as the standard replacement when the density is known only up to
a multiplicative constant {{cite:tokdar_kass2010}} (p. 54, eq. (4)), and
Owen derives it the same way, as the cancellation of the unknown constants
of both $p$ and $q$ in a ratio of two importance sampling estimates
{{cite:owen2013_mc}} (§9.2).

The ratio form changes the estimator's properties in three ways, and the
differences from the plain estimator are exact statements, not matters of
taste. First, $\widetilde{\mu}$ is generally biased at finite $N$: it is
a ratio of two random averages, and the expectation of a ratio is
not in general the ratio of the expectations. 'Generally' is the
correct qualification, not 'always': if $h$ is a constant function,
$h \equiv c$, the ratio equals $c$ exactly on every sample with a
positive denominator, so that estimator is exact rather than
biased. For non-constant $h$ the bias is typically nonzero. A Taylor
expansion of the ratio about the limits of its numerator and
denominator — the delta method — produces a formal first-order bias
term of order $1/N$, with a coefficient depending on the covariance,
under $q$, of $\tilde{w}(X)$ and $\tilde{w}(X) h(X)$; but that term
is an asymptotic approximation, and the second moments it needs —
$\E_q[\tilde{w}(X)^2]$ and $\E_q[\tilde{w}(X)^2 h(X)^2]$ finite, with
$Z > 0$ — do not by themselves make the bias genuinely of order
$1/N$. They do not even guarantee that the bias exists: take $q$
uniform on $(0,1)$, $\tilde{w}(x) \propto e^{-1/x}$ and
$h(x) = e^{1/(2x)}$, where both displayed moments and $Z$ are
finite, yet on the event that all $N$ draws fall below
$\varepsilon$ — an event of probability $\varepsilon^N$ — the ratio
is at least $e^{1/(2\varepsilon)}$, so its expectation is infinite
at every finite $N$. A genuine $1/N$ bias expansion needs stronger
hypotheses, such as bounded weights, or higher moments together with
control of the denominator near zero; without them, the consistency
below is the exact statement and no rate for the bias is claimed.
Second, the estimator is
consistent: numerator and denominator each obey the strong law of large
numbers, converging to $Z\mu$ and $Z$ respectively, so their ratio
converges to $\mu$ with probability one {{cite:tokdar_kass2010}} (p. 54).
Third, its large-sample variance is not the plain estimator's variance.
The delta method gives the approximation

$$\text{Var}_q(\widetilde{\mu}) \approx \frac{1}{N} \E_q\left[ w(X)^2 (h(X) - \mu)^2 \right],$$

in which the weights multiply the centred values $h(X) - \mu$
rather than $h(X)$ itself; Owen obtains this expression by Taylor
expansion of the ratio {{cite:owen2013_mc}} (§9.2). The central
limit theorem for the ratio is therefore stated with the centred
moment condition: when $\E_q[w(X)^2 (h(X) - \mu)^2]$ is finite,
$\sqrt{N}(\widetilde{\mu} - \mu)$ is approximately normal with
variance $\E_q[w(X)^2 (h(X) - \mu)^2]$ — the centred moment itself.
The factor $1/N$ belongs to the variance of $\widetilde{\mu}$, not
to the variance of its root-$N$ scaling. This is a condition on the
centred product $w(X)(h(X) - \mu)$, distinct from the plain
estimator's condition $\E_q[h(X)^2 w(X)^2] < \infty$, and neither
should be quoted as sufficient for both estimators. One consequence is that the optimal
proposal also changes: for the self-normalised estimator it is
proportional to $p(x) |h(x) - \mu|$, not to $p(x) |h(x)|$, so zero
variance is unattainable even in the benchmark sense — the best proposal
still leaves variance of the order of $\E_p[|h(X) - \mu|]^2 / N$
{{cite:owen2013_mc}} (§9.2).

The denominator of the ratio is an estimate in its own right. The average
unnormalised weight, $(1/N) \sum_i \tilde{w}(x_i)$, is an unbiased and
consistent estimate of $Z$, because
$\E_q[\tilde{w}(X)] = \int \tilde{p}(x)\, dx = Z$. In the Bayesian setting
$Z$ is the marginal likelihood, the quantity that enters Bayes factors
between models; importance sampling therefore supplies, from one set of
draws, both posterior expectations (through the ratio) and an estimate of
the marginal likelihood (through the mean unnormalised weight). The second
worked example computes both from the same five draws. The estimate of $Z$
inherits the fragility of the plain estimator — it is a plain estimator,
of the constant function — and can be dominated by a handful of large
weights when the proposal is poorly matched.

### Effective sample size and the diagnosis of degeneracy

A set of weighted draws carries less information than the same number of
unweighted draws. Given weights $w_1, \dots, w_N$ at the drawn points, the
[effective sample size](effective-sample-size.qmd) of the weighted sample
is

$$N_{\text{eff}} = \frac{\left(\sum_{i=1}^{N} w_i\right)^2}{\sum_{i=1}^{N} w_i^2}.$$

The formula is a variance comparison, not an arbitrary index. If values
$Y_i$ with common variance $\sigma^2$ are combined in a weighted average
with fixed weights, the variance of the weighted average is
$\sigma^2 \sum_i w_i^2 / (\sum_i w_i)^2 = \sigma^2 / N_{\text{eff}}$:
exactly the variance that $N_{\text{eff}}$ equally weighted independent
values would give. Owen presents the measure in this form, attributed
there to Kong (1992) and to Evans and Swartz (1995), under the name
effective sample size $n_e$ {{cite:owen2013_mc}} (§9.3). It satisfies
$1 \le N_{\text{eff}} \le N$, with $N_{\text{eff}} = N$ only when all the
weights are equal and $N_{\text{eff}}$ near $1$ when a single weight
dominates the sum. It is unchanged if every weight is multiplied by the
same constant, so it can be computed from unnormalised weights, which is
what makes it available in the self-normalised setting. The repo's article
on [effective sample size](effective-sample-size.qmd) treats the
corresponding notion for dependent, unweighted draws, such as Markov chain
output; the present formula is the weighted, independent-draw version, and
the two should not be interchanged.

The effective sample size is a diagnostic, and its limits should be
stated plainly. It summarises the variability of the weights actually
drawn. It cannot detect a region the proposal never visited: if $q$ misses
part of the support of $|h| p$ entirely, the drawn weights can be
comfortably equal, $N_{\text{eff}}$ comfortably large, and the estimate
wrong by the whole contribution of the missed region. It is also a
statement about the weights alone, not about $h$, because what matters for
$\mu$ is the variability of $h(x_i) w(x_i)$, not of $w(x_i)$ alone. Used
with those limits in mind — and reported alongside the largest normalised
weight — it is the standard first check on an importance sampling
calculation {{cite:owen2013_mc}} (§9.3).

## Worked example

### A rare-event probability

Let $Z$ be standard normal and estimate $\mu = P(Z > 3)$ by importance
sampling. The exact value is $\mu = 1 - \Phi(3) = 0.001349898$, where
$\Phi$ is the standard normal distribution function. Under crude Monte Carlo — sampling from
$p$, the $N(0,1)$ density itself — the per-draw contribution is a
Bernoulli variable with success probability $\mu$, so the per-draw
variance is exactly $\mu(1-\mu) = 1.348076 \times 10^{-3}$, and almost
every draw contributes zero.

Take instead the proposal $q$ to be the $N(3,1)$ density: the same family,
tilted so that its centre sits on the boundary of the rare set. Writing
$\phi$ for the standard normal density, the weight function is

$$w(x) = \frac{\phi(x)}{\phi(x-3)} = \exp\left(\frac{9}{2} - 3x\right),$$

an exact closed form: the normalising constants and the quadratic terms
partly cancel, leaving a decreasing exponential. On the rare set itself the
weights are small and shrink rapidly: $w(3) = e^{-9/2} \approx 0.011109$
and $w(4) \approx 0.000553$. Half of all proposal draws fall in the set
$\{x > 3\}$, by symmetry of $N(3,1)$ about $3$, and each is downweighted to
compensate.

The per-draw second moment of the importance sampling contribution
$w(X) \mathbf{1}\{X > 3\}$ under $q$ also has an exact closed form.
Squaring the target density and dividing by the proposal density gives
$\phi(x)^2/\phi(x-3) = e^{9} \phi(x+3)$, so

$$\E_q\left[w(X)^2 \mathbf{1}\{X > 3\}\right] = e^{9} \int_3^{\infty} \phi(x+3)\, dx = e^{9} \left(1 - \Phi(6)\right) = 8103.083928 \times 9.865876 \times 10^{-10} \approx 7.994402 \times 10^{-6}.$$

The per-draw variance is therefore exactly this second moment minus
$\mu^2$:

$$7.994402 \times 10^{-6} - (0.001349898)^2 \approx 6.172178 \times 10^{-6},$$

against the crude per-draw variance $1.348076 \times 10^{-3}$. The tilted
proposal reduces the variance per draw by a factor of about $218$. In
sample-size terms, a relative standard error of $10\%$ requires
$N = (\text{per-draw variance}/\mu^2)/0.01$ draws: about $73{,}980$ draws
by crude Monte Carlo, against $339$ draws by importance sampling with this
proposal. Both figures are exact consequences of the two per-draw
variances, not simulation results.

The example also disciplines the chi-squared discussion in 'Variance:
the weights decide everything' above. For this pair, $\E_q[w(X)^2] = e^{9} \approx 8103.08$, so the
chi-squared divergence $D_{\chi^2}(p \, \| \, q) = e^9 - 1 \approx
8102.08$ is enormous: estimating the constant $1 = \E_p[1]$ from $N(3,1)$
draws would be very poor, because draws far below $3$ carry weights like
$e^{9/2} \approx 90$ and larger. The rare-event estimate is nevertheless
excellent, because $h(x) = \mathbf{1}\{x > 3\}$ is zero exactly where the
weights explode, and the second moment that governs it,
$\E_q[w(X)^2 h(X)^2]$, is the small number computed above. A divergence is
a property of the pair of densities; the variance of an estimate is a
property of the triple $(p, q, h)$.

### A self-normalised posterior mean in five draws

A coin is tossed four times with three heads and one tail. With a uniform
prior on the success probability $\theta \in (0,1)$, the posterior density
is proportional to $\tilde{p}(\theta) = \theta^3 (1-\theta)$; the
normalised posterior is the Beta$(4,2)$ distribution, whose mean is
exactly $4/6 = 2/3 \approx 0.666667$ and whose normalising constant is
exactly $Z = \int_0^1 \theta^3(1-\theta)\, d\theta = 1/20 = 0.05$. Treat
$\tilde{p}$ as known only up to its constant, as a posterior ordinarily is,
and take the proposal $q$ to be the uniform density on $(0,1)$, which
equals $1$ everywhere, so the unnormalised weight of a draw $\theta$ is
simply $\tilde{w}(\theta) = \theta^3 (1-\theta)$. Suppose the five proposal
draws are $0.2$, $0.4$, $0.5$, $0.6$ and $0.8$ — a stated, deterministic
set, so that every number below is exact arithmetic, not a simulation
report.

| Draw $\theta_i$ | Unnormalised weight $\tilde{w}_i = \theta_i^3 (1-\theta_i)$ | Normalised weight $\tilde{w}_i / \sum_j \tilde{w}_j$ |
|---:|---:|---:|
| 0.2 | $4/625 = 0.0064$ | $64/2961 \approx 0.021614$ |
| 0.4 | $24/625 = 0.0384$ | $128/987 \approx 0.129686$ |
| 0.5 | $1/16 = 0.0625$ | $625/2961 \approx 0.211077$ |
| 0.6 | $54/625 = 0.0864$ | $96/329 \approx 0.291793$ |
| 0.8 | $64/625 = 0.1024$ | $1024/2961 \approx 0.345829$ |

The weights sum to $\sum_i \tilde{w}_i = 2961/10000 = 0.2961$. The
self-normalised estimate of the posterior mean is the weighted average of
the draws:

$$\widetilde{\mu} = \frac{\sum_i \tilde{w}_i \theta_i}{\sum_i \tilde{w}_i} = \frac{0.18165}{0.2961} = \frac{173}{282} \approx 0.613475,$$

where the numerator is
$0.0064 \times 0.2 + 0.0384 \times 0.4 + 0.0625 \times 0.5 + 0.0864 \times
0.6 + 0.1024 \times 0.8 = 0.18165$ exactly. The estimate $0.6135$ is not
the exact posterior mean $0.6667$, and the gap should be read correctly:
it is the sampling variability of the ratio at $N = 5$ on display. A
single sample cannot demonstrate bias — bias is a property of the
estimator's average over repeated samples — and nothing in the method
promises closeness at this sample size. The same weights estimate the normalising
constant: the mean unnormalised weight is $0.2961/5 = 0.05922$, against
the exact $Z = 0.05$ — the marginal-likelihood estimate from this
calculation, obtained from the same draws at no extra cost.

The effective sample size of the five weighted draws is

$$N_{\text{eff}} = \frac{(0.2961)^2}{0.0064^2 + 0.0384^2 + 0.0625^2 + 0.0864^2 + 0.1024^2} = \frac{0.08767521}{0.02337249} \approx 3.7512.$$

That number is a statement about the weights alone: they are as uneven
as about $3.75$ equal weights would be. It is not a measure of the
information this sample carries about the posterior mean specifically —
accuracy for that integrand depends on the products
$\tilde{w}_i \theta_i$, not on the weights in isolation. The largest
normalised weight is $0.346$: no single draw dominates, which is why the
effective sample size is a substantial fraction of $5$ rather than a
number near $1$.

## Statistical use — Where importance sampling is used

Importance sampling is used in three broad settings. The first is
rare-event simulation: failure probabilities of engineered systems,
extreme losses in finance, and small tail probabilities generally, where
crude Monte Carlo would need an impractical number of draws to see the
event at all. The second is [Bayesian inference](bayesian-inference.qmd),
where the self-normalised estimator turns draws from a tractable proposal
— a Laplace-style normal or $t$ approximation, a prior, or a fitted
approximation such as the output of
[variational inference](variational-inference.qmd) — into estimates of
posterior expectations, and the mean unnormalised weight estimates the
marginal likelihood. The third is reuse: one set of draws, reweighted, can
estimate expectations under a range of nearby targets, as in sensitivity
analyses that vary a parameter of the model. Its competitors clarify what
it is. Against rejection sampling it keeps every draw: rejection sampling
discards proposals and returns unweighted draws from $p$ itself, but
requires a known bound on $w(x) = p(x)/q(x)$, whereas importance sampling
requires no bound, works when the ratio is unbounded, and pays by
returning weighted draws whose quality varies {{cite:owen2013_mc}} (§9.5).
Against Markov chain Monte Carlo, including
[Hamiltonian Monte Carlo](hamiltonian-monte-carlo.qmd), it offers
independent draws and an estimate of the normalising constant, but no
mechanism for discovering regions of the target that the proposal did not
already cover.

## Assumptions and limits — Support, moments, and weight degeneracy

Its assumptions are few and sharp. The support condition must hold:
$q(x) > 0$ wherever $|h(x)| p(x)$ is nonzero, and, for the self-normalised
estimator, wherever $p(x) > 0$. Both densities must be evaluable at the
drawn points, the target up to the constant the setting allows. For the
variance formulas and the normal approximation to the error, the second
moment $\E_q[h(X)^2 w(X)^2]$ must be finite; unbiasedness and consistency
do not need it, which is why an estimate can be consistent, apparently
stable over long runs, and still have infinite variance — the sample
variance then understates the true variability, because the draws that
would reveal it are those the proposal produces too rarely.

The limits follow from the same formulas. A proposal with thinner tails
than the target can give infinite variance. A proposal that misses a mode
gives an estimate wrong by that mode's contribution, with no internal
signal of the omission: the weights of the draws that occurred cannot
report on draws that never occurred. In high dimensions the weights
degenerate unless the proposal is exponentially close to the target. And the self-normalised estimator is generally biased at finite
$N$ — exact only in special cases such as a constant integrand,
when its denominator is positive — so reporting it as if it were
the unbiased plain estimator misstates its properties.
Diagnostics based on the drawn weights — the effective sample size and
the largest normalised weight — are necessary checks, not sufficient ones.

### High dimensions: weight degeneracy

The method's characteristic failure is already visible in Hastings's 1970
account: importance sampling "is a difficult method to use in a large
number of dimensions, since the values of the weights $w(x_i) = p(x_i)/q(x_i)$
for reasonable values of $N$ may all be extremely small, or a few may be
extremely large" {{cite:hastings1970}} (§1, p. 97). The mechanism is
multiplicative. In $d$ dimensions a density ratio is typically a product
of $d$ one-dimensional factors; the logarithm of the weight is a sum of
$d$ terms, with variance growing proportionally to $d$, so the weights
vary over a range exponential in $d$, and the chi-squared divergence
between product densities compounds across coordinates. The consequence is
weight degeneracy: as the dimension grows, the largest normalised weight
tends towards one and the effective sample size towards one, however large
$N$ is, unless $N$ grows exponentially with the discrepancy between $p$
and $q$. A nominal sample of ten thousand draws can be, in effect, a
sample of three.

Tokdar and Kass locate the same difficulty from the approximation side:
for a high-dimensional target, a proposal that is easy to sample from and
yet close to $p$ is hard to identify, because the region where $p$ is
large occupies an extremely small fraction of the volume
{{cite:tokdar_kass2010}} (p. 55). Their review's response is structural:
where the target factorises along a chain — as in state-space models —
the proposal can be built sequentially, one conditional factor at a time,
with the weight accumulated as a product of one-step ratios. That
construction is sequential importance sampling, and with resampling added
it is the basis of particle filtering {{cite:tokdar_kass2010}} (pp. 56–58). It manages degeneracy by rebuilding the sample as it goes; it
does not repeal the multiplicative mechanism, and the plain, one-shot
estimator of this article remains a low-to-moderate-dimensional tool
unless the proposal is very close to the target.

## Common misconceptions

**"Importance sampling draws from the target distribution."** It does not.
Every draw comes from the proposal $q$; the target $p$ enters only through
the weights. The output is a weighted sample, and treating the draws as an
unweighted sample from $p$ — averaging the $h(x_i)$ without weights, for
instance — estimates $\E_q[h(X)]$, not $\E_p[h(X)]$.

**"An unbiased estimator cannot be badly wrong."** The plain estimator is
exactly unbiased under the support condition, including when its variance
is infinite. Unbiasedness is a statement about the average over repeated
runs; a single run of an infinite-variance estimator can be far from
$\mu$, and the runs that correct the average are those containing a rare,
enormous weight.

**"The self-normalised estimator is unbiased because the constant
cancels."** The constant cancels exactly; unbiasedness does not follow.
The estimator is a ratio of two random quantities, its bias is in
general nonzero at finite $N$ and vanishes as $N$ grows, with no
universal rate (a constant $h$ is the exception: its ratio is exact
whenever the denominator is positive), and only its consistency —
convergence to $\mu$ as $N$ grows — is exact. In the second worked example the estimate from five draws is
$0.6135$ against an exact mean of $0.6667$; that gap is the sampling
variability of the ratio at small $N$, not an error in the arithmetic,
and a single sample could not exhibit bias in any case.

**"A large effective sample size certifies the estimate."** The effective
sample size summarises the weights that were drawn. It is silent about
regions the proposal never reached and about functions $h$ other than the
one implicitly weighted. It is a check on degeneracy, not a certificate of
correctness.

**"The proposal should approximate the target as closely as possible."**
The variance is governed by $|h| p$, not by $p$ alone. For a rare-event
probability the best proposals are centred on the rare set and can be far
from $p$ as densities — in the first worked example the chi-squared
divergence between target and proposal is about $8102$, yet the variance
falls by a factor of about $218$. Closeness to $p$ is the right goal only
when $h$ is nearly constant.

**"More draws fix a bad proposal."** More draws reduce variance at the
rate $1/N$ when the variance is finite. They do not repair a support
violation at any $N$, they do not make an infinite variance finite, and in
high dimensions the number of draws needed to overcome weight degeneracy
grows exponentially with the discrepancy between $p$ and $q$.

## Connections

- [Monte Carlo method](monte-carlo-method.qmd) — the general method of
  estimating expectations by sampling, of which importance sampling is the
  weighted form; that article mentions importance sampling in passing, and
  the present article is the full treatment.
- [Effective sample size](effective-sample-size.qmd) — the number of
  independent unweighted draws a sample is worth; there it is developed
  for dependent draws, here in the weighted form
  $(\sum_i w_i)^2 / \sum_i w_i^2$ for independent weighted draws.
- [Bayesian inference](bayesian-inference.qmd) — the setting in which the
  target is known only up to a normalising constant, the self-normalised
  estimator is the standard tool, and the mean unnormalised weight
  estimates the marginal likelihood.
- [Variational inference](variational-inference.qmd) — a fitted
  variational approximation is a natural proposal distribution: draws from
  it, reweighted by the ratio of the unnormalised posterior density to
  the proposal density, give consistent estimates of posterior
  expectations under the support condition — the approximation's error
  is corrected in the limit, not removed at any finite sample size.
- [Hamiltonian Monte Carlo](hamiltonian-monte-carlo.qmd) — the Markov
  chain alternative for posterior expectations, which needs no proposal
  covering the whole target but returns dependent, unweighted draws and no
  estimate of the normalising constant.
- [Dirichlet process](dirichlet-process.qmd) — inference for Dirichlet
  process mixtures is a setting in which weighted and sequential forms of
  importance sampling handle posteriors that direct sampling cannot reach.

## History

The weighting identity is older than its name in statistics. Importance
sampling was introduced as a variance reduction device in statistical
physics in the 1950s — Tokdar and Kass trace its introduction to work of
Hammersley and Morton (1954) and of Rosenbluth and Rosenbluth (1955) on
Monte Carlo calculation in physics, and describe it as a variance
reduction technique from that setting {{cite:tokdar_kass2010}} (p. 54).
Hastings's 1970 exposition brought the method into the statistician's
standard toolkit as one of the general strategies for expectations under
hard distributions, alongside the Markov chain methods that are that
paper's main subject, and already contained the warning about weights in
high dimensions quoted above {{cite:hastings1970}} (§1, p. 97). The
self-normalised, ratio form became central with the growth of Bayesian
computation, where unnormalised posteriors are the rule; Tokdar and Kass
record the strong law and central limit results for both forms and cite
Geweke (1989) for their development in the Bayesian econometric setting
{{cite:tokdar_kass2010}} (p. 54). Later development ran in the directions
their review organises: adaptive parametric proposals fitted by optimising
an efficiency criterion, sequential constructions with resampling for
chain-structured targets, and combinations with Markov chain sampling
{{cite:tokdar_kass2010}} (pp. 55–59). Owen gives the
method a chapter of its own {{cite:owen2013_mc}} (ch. 9).

## Check yourself

1. Let $X$ take the values $1$ and $2$ with $p(1) = p(2) = 1/2$, let
$h(x) = x$, and let the proposal be $q(1) = 1$, $q(2) = 0$. What value
does the importance sampling estimator take on every run, what is the true
$\mu$, and which condition has failed?

::: {.callout-tip collapse="true" title="Answer"}

Every draw equals $1$, its weight is $w(1) = p(1)/q(1) = 1/2$, so the
estimator is identically $h(1) w(1) = 1/2$, whatever $N$ is. The true
value is $\mu = (1/2)(1) + (1/2)(2) = 3/2$. The support condition has
failed: $q(2) = 0$ while $|h(2)| p(2) = 1 > 0$, so the contribution of the
value $2$ — which is $1$, two-thirds of $\mu$ — is never sampled. No
increase in $N$ repairs this, and the drawn weights, all equal to $1/2$,
give no indication that anything is missing.

:::

2. Four draws have unnormalised weights $1$, $1$, $2$ and $6$, and the
corresponding values of $h$ are $0$, $1$, $2$ and $3$. Compute the
self-normalised estimate of $\mu$, the effective sample size, and the
largest normalised weight, and comment on the sample.

::: {.callout-tip collapse="true" title="Answer"}

The weights sum to $10$, so the self-normalised estimate is
$(1 \times 0 + 1 \times 1 + 2 \times 2 + 6 \times 3)/10 = 23/10 = 2.3$.
The sum of squared weights is $1 + 1 + 4 + 36 = 42$, so the effective
sample size is $10^2/42 = 50/21 \approx 2.381$: four weighted draws worth
about $2.38$ unweighted ones. The largest normalised weight is
$6/10 = 0.6$: a single draw supplies three-fifths of the estimate, which
is the degeneracy the effective sample size is reporting.

:::

3. Let $p$ be the $N(0,1)$ density and $q$ the $N(0, s^2)$ density. For
which values of $s$ is $\E_q[w(X)^2]$ finite? What happens for $s = 0.6$,
and why does no finite sample reveal the problem directly?

::: {.callout-tip collapse="true" title="Answer"}

The integrand of $\E_q[w(X)^2] = \int p(x)^2/q(x)\, dx$ is proportional to
$\exp(-x^2 + x^2/(2s^2))$, which is integrable exactly when the exponent's
coefficient is negative: $-1 + 1/(2s^2) < 0$, that is, $s^2 > 1/2$, or
$s > 1/\sqrt{2} \approx 0.707$. For $s = 0.6$ the second moment is
infinite, so the plain estimator of any $h$ whose integrand shares this
tail behaviour has infinite variance even though $q$ is a normal density
with the same centre and a similar spread. A finite sample does not reveal
it directly because the draws responsible — points far in the tails,
where the weight $\exp(x^2(1/(2s^2) - 1/2))$-type growth is largest — are
rare under $q$ itself; a run that omits them looks stable, and its sample
variance understates the true variability.

:::
