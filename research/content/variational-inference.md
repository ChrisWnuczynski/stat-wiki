## Lead context

Variational inference is a method for approximating a probability density
that cannot be computed exactly, most often a Bayesian posterior density,
by solving an optimisation problem instead of a sampling problem. The
analyst first specifies a family of densities, called the variational
family, whose members are simple enough that expectations under them can
be computed. Variational inference then selects the member of that family
closest to the target density, where closeness is measured by the
Kullback–Leibler divergence from the approximation to the target. The
selected density is used in place of the posterior: its mean stands in for
the posterior mean, its quantiles for posterior quantiles, and so on.
Blei, Kucukelbir and McAuliffe define the method in exactly these terms:
"first posit a family of densities and then find the member of that family
which is close to the target", with closeness measured by
Kullback–Leibler divergence {{cite:blei_kucukelbir_mcauliffe2017}} (§1, pp. 859–860).

Two features of that definition should be fixed at the outset. First, the
output is an approximation, not the posterior itself, and it carries no
guarantee of exactness as computation increases: if no member of the
family equals the posterior, the remaining error does not vanish however
long the optimisation runs. Second, everything depends on the family: a
richer family can come closer to the posterior but is harder to optimise
over; a poorer family optimises easily and may approximate badly.

## Motivating example — A posterior that cannot be computed

Let $x = (x_1, \dots, x_n)$ denote observed data and let
$z = (z_1, \dots, z_m)$ denote latent variables: parameters, random
effects, missing values, or any other quantities that the model treats as
unobserved. A Bayesian model specifies a joint density
$p(z, x) = p(z)\, p(x \mid z)$, the product of a prior density $p(z)$ and
a likelihood $p(x \mid z)$. Inference about $z$ after seeing $x$ is
summarised by the posterior density, given by [Bayes'
rule](bayes-rule.qmd),

$$p(z \mid x) = \frac{p(z, x)}{p(x)}, \qquad
p(x) = \int p(z, x)\, dz.$$

The denominator $p(x)$ is the marginal likelihood, or evidence: the joint
density integrated over every configuration of the latent variables. It is
this integral that usually cannot be computed. With continuous or
numerous latent variables, or a likelihood that does not combine with
the prior in closed form, it has no analytic solution and numerical
integration is defeated by the dimension of $z$. Blei, Kucukelbir and McAuliffe set up
the problem in this form, noting that in complex Bayesian models the
computation of the posterior "often requires approximate inference"
{{cite:blei_kucukelbir_mcauliffe2017}} (§1, p. 859). Jordan, Ghahramani,
Jaakkola and Saul make the same point for graphical models: exact
inference algorithms exist, but "there are other cases … in which the
time or space complexity of the exact calculation is unacceptable and it
is necessary to have recourse to approximation procedures"
{{cite:jordan_etal1999_variational}} (p. 184).

The classical response is [Markov chain Monte
Carlo](markov-chain.qmd): construct a Markov chain whose stationary
distribution is $p(z \mid x)$, run it, and summarise the posterior from
the draws. That approach is asymptotically exact, but for large $n$ or
large $m$ its cost can be prohibitive. Variational inference replaces
simulation with optimisation, and in return accepts an approximation
whose error does not disappear with more computation. Blei, Kucukelbir
and McAuliffe state the trade-off plainly: compared with Markov chain
Monte Carlo, variational inference "tends to be faster and easier to
scale to large data", but "does not enjoy such guarantees — it can only
find a density close to the target"
{{cite:blei_kucukelbir_mcauliffe2017}} (§1, pp. 859–860).

## Definition — The approximating family, the evidence lower bound, and the mean-field family

### The approximating family and the direction of the divergence

Let $\mathcal{Q}$ be a family of densities over $z$. Each $q \in
\mathcal{Q}$ is a candidate approximation to $p(z \mid x)$, and $q$ is
typically described by its own parameters, called variational parameters.
Variational inference chooses

$$q^{*}(z) = \arg\min_{q \in \mathcal{Q}}\
\mathrm{KL}\bigl(q(z) \,\|\, p(z \mid x)\bigr),$$

where the [Kullback–Leibler
divergence](kullback-leibler-divergence.qmd) from $q$ to $p(z \mid x)$ is

$$\mathrm{KL}\bigl(q(z) \,\|\, p(z \mid x)\bigr)
= \mathbb{E}_q[\log q(z)] - \mathbb{E}_q[\log p(z \mid x)],$$

with $\mathbb{E}_q$ denoting expectation under $q$
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.2, eqs. 10–11). The divergence
is nonnegative, and it is zero only when $q$ equals the posterior almost
everywhere; it is not symmetric, so the direction written here is a
substantive choice, not a convention.

The direction $\mathrm{KL}(q \| p)$ has two consequences. The first is
computational, and it is the reason the direction is chosen:
expectations are taken under $q$, the density the analyst controls,
rather than under the intractable posterior. The second is behavioural:
the integrand is weighted by $q$ itself, so the divergence penalises $q$
heavily for placing mass where $p$ has little mass, and penalises it
much less for failing to place mass where $p$ has mass. Blei, Kucukelbir and McAuliffe describe
the resulting behaviour in their Gaussian example: the divergence
"penalizes placing mass in $q(\cdot)$ on areas where $p(\cdot)$ has
little mass, but penalizes less the reverse", so the fitted $q$ avoids
spreading into low-posterior regions even when that means its marginal
variances under-represent those of the target
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.4). An approximation fitted
this way tends to be contained within the posterior rather than covering
it: it locks onto a region of high posterior density and reports less
spread than the posterior has. The reverse divergence,
$\mathrm{KL}(p \| q)$, would have the opposite tendency, but it requires
expectations under the posterior and so cannot be optimised directly;
methods built around it, such as expectation propagation, need a
different construction {{cite:blei_kucukelbir_mcauliffe2017}} (§5.4).

The family $\mathcal{Q}$ is the other substantive choice. It must be
flexible enough to contain a density close to the posterior, yet simple
enough that the expectations in the objective derived next can be
computed and optimised. As Blei, Kucukelbir and McAuliffe put it, "the
reach of the family $\mathcal{Q}$ manages the complexity of this
optimization" {{cite:blei_kucukelbir_mcauliffe2017}} (§1, p. 860).
Together, divergence direction and family determine what the
approximation can represent, before any algorithm is run.

### The evidence lower bound

The optimisation just stated cannot be carried out as written, because
the divergence contains the posterior, and expanding the posterior
exposes the intractable evidence:

$$\mathrm{KL}\bigl(q(z) \,\|\, p(z \mid x)\bigr)
= \mathbb{E}_q[\log q(z)] - \mathbb{E}_q[\log p(z, x)] + \log p(x).$$

The term $\log p(x)$ does not depend on $q$, but it is unknown — computing
it was the original problem. The resolution is to optimise a different
function that differs from the divergence only by that constant. The
evidence lower bound, abbreviated ELBO, is

$$\mathrm{ELBO}(q) = \mathbb{E}_q[\log p(z, x)] - \mathbb{E}_q[\log q(z)],$$

which involves only the joint density $p(z, x)$ — a quantity the analyst
can evaluate pointwise, since it is the product of the prior and the
likelihood — and the candidate $q$ itself
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.2, eq. 13). Adding the two
displays gives the identity on which the whole method rests:

$$\log p(x) = \mathrm{ELBO}(q) +
\mathrm{KL}\bigl(q(z) \,\|\, p(z \mid x)\bigr).$$

Since the left-hand side is fixed by the data and the model, maximising
the ELBO over $\mathcal{Q}$ is exactly the same problem as minimising the
divergence: every increase in the ELBO is an equal decrease in
$\mathrm{KL}(q \| p(z \mid x))$
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.2, eq. 14). And since the
divergence is nonnegative, the identity also shows that
$\mathrm{ELBO}(q) \le \log p(x)$ for every $q$: the ELBO is a lower bound
on the log evidence, which is the source of its name. Jordan, Ghahramani,
Jaakkola and Saul derive the same bound through Jensen's inequality, and
note that the difference between the two sides "is easily seen to be the
KL divergence", so that minimising the divergence yields "the tightest
lower bound" available within the family
{{cite:jordan_etal1999_variational}} (§6, eq. 43, pp. 213–214).

The ELBO admits a second decomposition that explains what the optimum
balances. Splitting the joint density into prior and likelihood gives

$$\mathrm{ELBO}(q) = \mathbb{E}_q[\log p(x \mid z)]
- \mathrm{KL}\bigl(q(z) \,\|\, p(z)\bigr).$$

The first term rewards $q$ for concentrating on latent configurations
that explain the observed data well; the second penalises $q$ for
departing from the prior. Blei, Kucukelbir and McAuliffe note that "the
variational objective mirrors the usual balance between likelihood and
prior" {{cite:blei_kucukelbir_mcauliffe2017}} (§2.2). This decomposition
also marks the boundary between variational inference and the [EM
algorithm](em-algorithm.qmd). The first term of the ELBO is the expected
complete-data log likelihood that EM optimises with respect to model
parameters; EM, however, computes its expectations under the exact
posterior $p(z \mid x)$, which is precisely what is unavailable here.
Jordan, Ghahramani, Jaakkola and Saul describe variational inference for
parameter estimation as a restricted form of the EM iteration, in which
the E step is replaced by optimisation over the approximating family
{{cite:jordan_etal1999_variational}} (§6.2, pp. 214–215).

One caution about the bound itself: because
$\log p(x) - \mathrm{ELBO}(q^{*})$ equals the divergence of the fitted
approximation, a loose family leaves a gap of unknown size. The ELBO is
sometimes used as a stand-in for the marginal likelihood in model
comparison, but, as Blei, Kucukelbir and McAuliffe warn, "selecting based
on a bound is not justified in theory"
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.2). A larger ELBO certifies a
better approximation to a fixed model's posterior; across models it
certifies nothing without further argument.

### The mean-field family

The family used most often, and the one for which the classical
algorithms were developed, is the mean-field family: the latent variables
are partitioned into $m$ groups — in the simplest version, one group per
variable — and $q$ is required to factorise across the groups,

$$q(z) = \prod_{j=1}^{m} q_j(z_j),$$

where each factor $q_j$ is a density over its own group, with its own
variational parameters {{cite:blei_kucukelbir_mcauliffe2017}} (§2.3, eq. 15). The name is borrowed from statistical physics, where the same
factorisation approximates interacting systems by independent components.
Under $q$, distinct groups are independent by construction. That is the
family's strength and its defining defect at once: expectations under a
factorised $q$ separate into expectations under the individual factors,
which is what makes optimisation tractable, but no member of the family
can represent posterior dependence between groups. If the posterior
correlates $z_1$ and $z_2$ strongly, every mean-field approximation
reports them as independent, whatever the data say.

Within the family, each factor is otherwise unrestricted: $q_j$ may be
any density over $z_j$. In conditionally conjugate models — those in
which each complete conditional $p(z_j \mid z_{-j}, x)$ lies in the same
family as the prior for $z_j$ — the optimal factors have the same
functional form as those complete conditionals, and variational
inference reduces to updating their parameters
{{cite:blei_kucukelbir_mcauliffe2017}} (§§4.1–4.2). Outside that setting
the factors are usually fixed parametric densities, such as normals with
free means and variances.

Richer families exist: structured families factorise only across a
coarser partition, and full-rank Gaussian families keep a complete
covariance matrix at the cost of many more parameters. Blei, Kucukelbir
and McAuliffe identify the tension as an open problem: the mean-field
family "makes strong independence assumptions" that "limit the
expressibility of the variational family", and developing "better
approximations while maintaining efficient optimization" remains an
active direction {{cite:blei_kucukelbir_mcauliffe2017}} (§5.4).

## Properties — Coordinate ascent and stochastic optimisation

### Coordinate ascent (CAVI)

Optimising the ELBO over all mean-field factors at once is generally not
possible in closed form, but optimising one factor while the others are
held fixed is. This is coordinate ascent variational inference, or CAVI:
cycle through the factors, replace each by its conditional optimum given
the current values of the rest, and repeat until the ELBO stops
increasing. Blei, Kucukelbir and McAuliffe describe it as the most
commonly used algorithm for the problem: it "iteratively optimizes each
factor of the mean-field variational density, while holding the others
fixed", and "climbs the ELBO to a local optimum"
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.4).

The conditional optimum has an explicit form. Write $z_{-j}$ for all
latent variables except $z_j$. Holding $q_\ell$ fixed for $\ell \ne j$,
the factor that maximises the ELBO is

$$q_j^{*}(z_j) \propto
\exp\left\{ \mathbb{E}_{-j}\bigl[\log p(z_j, z_{-j}, x)\bigr] \right\}
\propto \exp\left\{ \mathbb{E}_{-j}\bigl[\log p(z_j \mid z_{-j}, x)\bigr]
\right\},$$

where $\mathbb{E}_{-j}$ is expectation under the product of the fixed
factors {{cite:blei_kucukelbir_mcauliffe2017}} (§2.4, eqs. 17–18). In
words: the optimal factor is the exponentiated expected log complete
conditional — the model's own conditional for $z_j$, averaged over the
current approximations to everything else. The mean-field assumption is
what makes the update legitimate: the expectation does not involve $q_j$
itself. In conditionally conjugate models the right-hand side is a known
density whose parameters are functions of expectations under the other
factors, and CAVI becomes a cycle of parameter updates resembling those
of a [Gibbs sampler](gibbs-sampling.qmd), with expectations in place of
draws {{cite:blei_kucukelbir_mcauliffe2017}} (§2.4).

Three properties of CAVI matter for practice. First, every update
increases the ELBO or leaves it unchanged, so the ELBO sequence is
monotone and convergence can be monitored directly from the objective:
run until its change falls below a small threshold
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.4). Second, the optimum
reached is in general only local. The ELBO is typically non-convex in
the variational parameters, and different initialisations can lead CAVI
to different local optima; Blei, Kucukelbir and McAuliffe illustrate
this with ten random initialisations of a mixture model reaching
visibly different solutions
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.4, Figure 2). The standard
response is to run from several starting points, keeping the run with
the highest ELBO — for a fixed model, the run with the smallest
divergence from the posterior.
Third, each CAVI sweep touches every observation, since expectations
involving the likelihood sum over all $n$ data points; for large $n$
that full pass per iteration is the bottleneck stochastic variational
inference removes.

### Stochastic variational inference and gradient methods

CAVI's full pass through the data at every iteration limits it to
datasets of moderate size. Stochastic variational inference, developed by
Hoffman, Blei, Wang and Paisley, removes that limit by applying
stochastic optimisation to the same ELBO: instead of computing the exact
gradient of the ELBO, the algorithm computes a noisy but unbiased
estimate of it from a subsample of the data, and follows that estimate
with a decreasing step size {{cite:hoffman_etal2013_svi}} (§2, pp. 1303–1305). Their summary of the iteration is to "subsample one or
more data points", analyse the subsample at the current variational
parameters, and take a closed-form step for the global parameters
{{cite:hoffman_etal2013_svi}} (§1).

The construction separates local from global latent variables. Local
variables are attached to individual observations, while global variables
are shared across the dataset. For a sampled observation, its local
variational parameters are optimised exactly, by the usual coordinate
update; those parameters define an intermediate setting of the global
parameters — the coordinate update that would result if the sampled
observation stood in for the whole dataset — and the global parameters
are then moved a step of size $\rho_t$ towards it:

$$\lambda_t = (1 - \rho_t)\, \lambda_{t-1} + \rho_t\, \hat{\lambda}_t,$$

where $\lambda$ collects the global variational parameters and
$\hat{\lambda}_t$ is the intermediate setting at iteration $t$
{{cite:hoffman_etal2013_svi}} (§2). The gradient being followed is not the
ordinary gradient but the natural gradient, which rescales the gradient
by the inverse Fisher information of the variational family; for the
conditionally conjugate models Hoffman and colleagues treat, the natural
gradient has a simple form that makes the update above exact rather than
approximate {{cite:hoffman_etal2013_svi}} (§2.3). Step sizes follow a
Robbins–Monro schedule, $\rho_t = (t + \tau)^{-\kappa}$ with delay
$\tau \ge 0$ and forgetting rate $\kappa \in (0.5, 1]$, satisfying
$\sum_t \rho_t = \infty$ and $\sum_t \rho_t^2 < \infty$, the conditions
under which stochastic optimisation converges to a local optimum
{{cite:hoffman_etal2013_svi}} (§§2–4).

The scale achieved is the point of the method. Hoffman, Blei, Wang and
Paisley applied it to topic models on collections of 300,000 articles
from *Nature*, 1.8 million articles from *The New York Times*, and 3.8
million articles from Wikipedia — data sizes at which batch coordinate
ascent "can only handle a smaller subset"
{{cite:hoffman_etal2013_svi}} (abstract, p. 1303). The costs are those of
any stochastic optimisation: the objective is no longer monotone along
the iterates, and convergence is to a local optimum whose quality
depends on the step-size schedule and initialisation.

Two further developments extend variational inference beyond models with
tractable complete conditionals. Black-box variational inference writes
the gradient of the ELBO as an expectation under $q$ involving the score
function $\nabla \log q$, estimates it by Monte Carlo draws from $q$,
and follows the estimates with stochastic optimisation; no
model-specific derivation is required, at the price of gradient
estimates whose variance can be large. Blei, Kucukelbir and McAuliffe
survey this work under the heading of "black box" inference methods,
noting that the newest approaches "avoid any model-specific derivations"
{{cite:blei_kucukelbir_mcauliffe2017}} (§5.3). The reparameterisation
approach instead writes a draw from $q$ as a deterministic function of
parameter-free noise, when $q$ permits it, and differentiates through
that function to obtain gradient estimates with typically much lower
variance. Both approaches keep the same objective and change only how
its gradient is estimated; they widen the class of models the method
reaches without changing what its optimum represents.

## Worked example

### Mean-field for a correlated normal posterior

Suppose the posterior is bivariate normal with mean zero, unit marginal
variances, and correlation $\rho = 0.8$:

$$p(z \mid x) = \mathrm{N}\!\left(0,\ \Sigma\right), \qquad
\Sigma = \begin{pmatrix} 1 & 0.8 \\ 0.8 & 1 \end{pmatrix}.$$

This is the example Blei, Kucukelbir and McAuliffe use to display the
mean-field approximation, in their Figure 1: the approximating density
"has the same mean as the original density", but "its covariance is, by
construction, decoupled", and "the marginal variances of the
approximation under-represent those of the target"
{{cite:blei_kucukelbir_mcauliffe2017}} (§2.4). Here the numbers can be
given exactly.

Take the mean-field family $q(z) = q_1(z_1)\, q_2(z_2)$ with
$q_j = \mathrm{N}(m_j, s_j^2)$. The posterior precision matrix is

$$\Sigma^{-1} = \frac{1}{1 - \rho^2}
\begin{pmatrix} 1 & -\rho \\ -\rho & 1 \end{pmatrix}
= \frac{1}{0.36}
\begin{pmatrix} 1 & -0.8 \\ -0.8 & 1 \end{pmatrix},$$

so each diagonal entry of the precision is $1/(1-\rho^2) = 1/0.36$. For a
Gaussian target, the optimal mean-field factor for $z_j$ is normal with
mean equal to the posterior mean and variance equal to the reciprocal of
that diagonal precision entry. Hence the optimum is $m_1 = m_2 = 0$ and

$$s_1^2 = s_2^2 = 1 - \rho^2 = 0.36, \qquad s_1 = s_2 = 0.6.$$

The mean is recovered exactly; the spread is not. Each true marginal
standard deviation is $1$, while the approximation reports $0.6$, and
each true marginal variance is $1$, while the approximation reports
$0.36$ — $36\%$ of the correct value. The correlation, $0.8$ in the
posterior, is reported as $0$, because no factorised density can report
anything else. Note what the number $0.36$ is: $1 - \rho^2$ is the
conditional variance of $z_1$ given $z_2$ under the posterior. The
mean-field factor adopts the conditional spread — how tightly $z_1$ is
pinned down when $z_2$ is known — as if it were the marginal spread,
discarding the variation that comes through the unknown $z_2$.

The minimised divergence can also be computed exactly. For
$q^{*} = \mathrm{N}(0, \mathrm{diag}(0.36, 0.36))$,

$$\mathrm{KL}(q^{*} \| p)
= \tfrac{1}{2}\left[\mathrm{tr}(\Sigma^{-1} \mathrm{diag}(0.36, 0.36))
- 2 + \log \frac{\det \Sigma}{\det \mathrm{diag}(0.36, 0.36)}\right]
= \tfrac{1}{2} \log \frac{0.36}{0.1296}
= -\tfrac{1}{2} \log(1 - \rho^2) \approx 0.511 \text{ nats},$$

where the trace term equals $2$ exactly, cancelling the $-2$. By the ELBO
identity, this is also the exact gap $\log p(x) - \mathrm{ELBO}(q^{*})$
for any model with this posterior: the best mean-field bound falls short
of the log evidence by about $0.511$ nats, and no optimisation within
the family can reduce that shortfall. Posterior correlation that the
family cannot express is converted, mechanically, into understated
marginal variances and a strictly positive divergence at the optimum.

### When the family contains the posterior

Variational inference is exact in one circumstance: when the chosen
family contains the posterior itself. Then the minimum of the divergence
is zero, the optimal $q$ is the posterior, and the ELBO equals the log
marginal likelihood. A one-dimensional normal–normal model shows all
three statements with checkable numbers; see [normal–normal
conjugacy](normal-normal-conjugacy.qmd) for the exact posterior used
here.

Let the prior be $\theta \sim \mathrm{N}(0, \tau^2)$ with
$\tau^2 = 4$, and let five observations
$x = (1.1,\ 1.6,\ 2.1,\ 2.6,\ 3.1)$ be drawn independently from
$\mathrm{N}(\theta, \sigma^2)$ with $\sigma^2 = 1$ known. The sample sum
is $\sum_i x_i = 10.5$, the sample mean is $\bar{x} = 2.1$, and the sum of
squared deviations is $\sum_i (x_i - \bar{x})^2 = 2.5$. The exact
posterior is normal with precision $1/\tau^2 + n/\sigma^2 = 1/4 + 5 =
21/4$, hence

$$\text{posterior variance} = \frac{4}{21} \approx 0.1905, \qquad
\text{posterior mean} = \frac{4}{21} \times 10.5 = 2, \qquad
\text{posterior sd} \approx 0.4364.$$

Choose as variational family all normal densities
$q(\theta) = \mathrm{N}(m, w)$, with free mean $m$ and variance $w$. This
family contains the posterior, $\mathrm{N}(2, 4/21)$, so the theory
predicts $q^{*} = \mathrm{N}(2, 4/21)$ and
$\mathrm{ELBO}(q^{*}) = \log p(x)$. The log marginal likelihood is
available in closed form here: marginally,
$x \sim \mathrm{N}(0,\ \sigma^2 I + \tau^2 \mathbf{1}\mathbf{1}^{\top})$,
with determinant $21$ and quadratic form $x^{\top} C^{-1} x = 3.55$,
giving

$$\log p(x) = -\tfrac{5}{2} \log(2\pi) - \tfrac{1}{2} \log 21
- \tfrac{1}{2}(3.55) \approx -7.8920.$$

Evaluating the ELBO at $q^{*}$ from its decomposition confirms the
identity term by term:
$\mathbb{E}_{q^{*}}[\log p(x \mid \theta)] \approx -6.3459$,
$\mathbb{E}_{q^{*}}[\log p(\theta)] \approx -2.1359$, and the entropy term
$-\mathbb{E}_{q^{*}}[\log q^{*}(\theta)] \approx 0.5898$, summing to
$-7.8920$ — equal to $\log p(x)$, as it must be when the divergence term
in the identity is zero. A suboptimal member shows the gap opening: for
$q = \mathrm{N}(2, 1)$, which has the correct mean but the prior-scale
variance in place of the posterior variance, the same computation gives
$\mathrm{ELBO}(q) \approx -9.1878$, and correspondingly
$\mathrm{KL}(q \| p(\theta \mid x)) = \log p(x) - \mathrm{ELBO}(q)
\approx 1.2959$ nats.

The example separates two sources of error that are entangled in real
applications. Optimisation error is the failure to find the best member
of the family; approximation error is the divergence of the best member
from the posterior. Here approximation error is zero by construction, so
any shortfall of a computed ELBO below $-7.8920$ is optimisation error
alone. In the bivariate example, by contrast, the entire $0.511$-nat
shortfall is approximation error. Reporting a fitted approximation
without asking which of the two errors dominates leaves the quality of
the inference unassessed.

## Statistical use — Where it is used, and its strengths

Variational inference is used where [Bayesian
inference](bayesian-inference.qmd) is wanted at a scale, or at a speed,
that sampling cannot deliver: large hierarchical models, topic models
for text, genome-wide association studies, image analysis, and repeated
fitting inside larger pipelines such as cross-validation. A fitted $q$
can also serve as a proposal distribution for a Metropolis–Hastings
sampler. Its natural competitor is Markov chain Monte Carlo, including
[Hamiltonian Monte Carlo](hamiltonian-monte-carlo.qmd), and the choice
between them is a choice about which error to accept: Monte Carlo error,
which decreases with computation, or approximation error, which is fixed
by the family and is not directly observable.

The strengths are consequences of the method being an optimisation.
Speed: Blei, Kucukelbir and McAuliffe report that variational inference
"tends to be faster than classical methods, such as Markov chain Monte
Carlo sampling" {{cite:blei_kucukelbir_mcauliffe2017}} (abstract, p. 859).
Scalability: because the objective is a sum over observations, stochastic
optimisation applies, and the method extends to datasets that do not fit
in memory {{cite:hoffman_etal2013_svi}} (§2). Diagnostics: the objective
is a number, computed at every iteration, whose increase tracks
progress — a check with no equally direct analogue for a Markov chain,
whose convergence must be inferred from the behaviour of its draws. A
plateau in the objective is the usual practical signal to stop, but it
certifies neither a stationary point nor a local optimum: an optimiser
can stall on a flat region, or crawl along a shallow valley, while the
objective barely moves. The batch
algorithm is also deterministic: the same initialisation and data return
the same answer.

## Common misconceptions

**"The ELBO is the log marginal likelihood."** It is a lower bound on
it. The two are equal only when the fitted $q$ equals the posterior, in
which case the divergence term in the identity is zero. In worked
example 1 the gap at the optimum is $0.511$ nats; treating the bound as
the evidence understates the model's log marginal likelihood by exactly
that gap. On the evidence scale itself the understatement is
multiplicative, not additive: the bound is the evidence times
$e^{-0.511} \approx 0.60$. And comparing two models by their bounds
compares log evidence minus two different, unknown gaps.

**"A converged variational fit has found the posterior."** Even where
an algorithm genuinely reaches a local optimum of the ELBO within the
chosen family — and a plateau in the objective does not by itself
certify that it has — the optimum says nothing about whether a better
local optimum exists, and nothing about how far the family's best
member is from the posterior. Both worked
examples converge perfectly; one of them still reports a variance of
$0.36$ where the truth is $1$.

**"Mean-field assumes the posterior is independent, so it is only a
rough device."** The assumption is about the approximating family, not a
claim about the posterior, and its consequences are precise: posterior
means are often recovered well — exactly, in worked example 1 — while
variances and correlations are distorted, the marginal variances
typically, though not invariably, understated (see Assumptions and
limits).

**"Variational inference is a faster kind of MCMC."** The two solve
different problems. Markov chain Monte Carlo simulates from the
posterior and is asymptotically exact; variational inference optimises
over a family and is exact only when the family contains the posterior.
[Importance sampling](importance-sampling.qmd) belongs to the first
tradition, variational inference to the second, and their error
behaviour — decreasing with computation in one case, fixed by the family
in the other — is the operational difference.

**"Stochastic variational inference fixes the accuracy problems of
variational inference."** It fixes a computational problem — the cost of
full data passes — by following noisy gradients of the same ELBO. The
optimum it approaches is the optimum of the same objective over the same
family, with the same variance-understating tendency; Hoffman, Blei, Wang
and Paisley present it as a method that lets "complex Bayesian models"
be applied "to massive data sets", not as a change to what is being
approximated {{cite:hoffman_etal2013_svi}} (abstract, p. 1303).

## Assumptions and limits — Variance, optima, and the chosen family

None of these limits is removed by running the optimisation for longer.

*Variance understatement — a tendency, not a guarantee.* An
approximation fitted by minimising $\mathrm{KL}(q \| p)$ is typically
contained within the posterior rather than spread across it, and a
factorised family compounds the effect by replacing marginal spreads
with conditional ones. Blei, Kucukelbir and McAuliffe state the usual
behaviour directly: "variational inference generally underestimates
the variance of the posterior density; this is a consequence of its
objective function" {{cite:blei_kucukelbir_mcauliffe2017}} (§1, p. 860).
Worked example 1 is the mechanism in miniature, an exact calculation:
a marginal variance of $1$ reported as $0.36$, so intervals built from
such an approximation are too narrow and tail probabilities
understated. But the direction is not a theorem. Take a posterior
placing probabilities $0.3$, $0.3$ and $0.4$ on the three points
$(-1, 0)$, $(1, 0)$ and $(0, 1)$: a product approximation whose reverse
divergence is finite must sit on a single slice of constant $Y$, and
the optimum chooses $Y = 0$, giving $\mathrm{Var}_q(X) = 1$ against
$\mathrm{Var}_p(X) = 0.6$ and $P_q(|X| > 0.5) = 1$ against $0.6$ — a
marginal variance and a tail probability *overstated*. Understated
spread is the common failure, and the one to expect; it is not
guaranteed.

*Local optima.* The ELBO is generally non-convex in the variational
parameters, so CAVI and stochastic variants alike can converge to
local optima that depend on initialisation. Comparing two runs' ELBOs
identifies the better of them but does not certify that either is near
the family's global optimum.

*Family dependence.* Every conclusion is conditional on $\mathcal{Q}$.
Dependence outside the family is reported as absent; multimodality
outside the family is reported as a single mode; heavy tails outside the
family are reported as light. No internal diagnostic measures the
divergence actually achieved, because the gap
$\log p(x) - \mathrm{ELBO}(q^{*})$ is the divergence, and $\log p(x)$ is
unknown. Comparisons with sampling on the same model and richer families
fitted as a sensitivity analysis are external checks, not properties of
the fit itself.

*No automatic exactness.* Increasing the computational budget improves
the optimisation, not the family: a variational fit run to convergence
has extracted everything its family contains, and the bivariate
example's $0.511$ nats remain. Enlarging the family is the only remedy.
Relatedly, summaries that require joint draws from $q$ — the probability
that two parameters are simultaneously in a region, for instance —
inherit the family's independence assumptions exactly, however many
draws are taken.

Where the posterior's spread is itself the quantity of interest —
interval estimation, decision problems sensitive to tail probabilities —
the variance-understating tendency is directly material, and a
variational answer should be corroborated. Where a point summary is
wanted at scale, the trade is often favourable, and empirical work cited
by Blei, Kucukelbir and McAuliffe finds that posterior predictive
performance need not suffer even when posterior variances are understated
{{cite:blei_kucukelbir_mcauliffe2017}} (§1).

## Connections

- [Bayesian inference](bayesian-inference.qmd) — the framework whose
  posterior density variational inference approximates when the evidence
  integral cannot be computed.
- [Kullback–Leibler divergence](kullback-leibler-divergence.qmd) — the
  measure of closeness being minimised, in the direction
  $\mathrm{KL}(q \| p)$; its asymmetry is responsible for the
  approximation's variance-understating tendency.
- [EM algorithm](em-algorithm.qmd) — the parameter-estimation algorithm
  whose expected complete-data log likelihood is the first term of the
  ELBO; variational inference is its restricted analogue when the exact
  posterior is unavailable.
- [Gibbs sampling](gibbs-sampling.qmd) — the sampling algorithm whose
  complete conditionals reappear, as expectations rather than draws, in
  the CAVI update for conditionally conjugate models.
- [Markov chain](markov-chain.qmd) — the basis of Markov chain Monte
  Carlo, the asymptotically exact alternative against which variational
  inference trades accuracy for speed and scale.
- [Hamiltonian Monte Carlo](hamiltonian-monte-carlo.qmd) — a sampling
  method often preferred to variational inference when posterior spread
  must be represented faithfully and the model permits it.
- [Importance sampling](importance-sampling.qmd) — a simulation-based
  approximation strategy with the opposite error profile: no family
  restriction, but Monte Carlo error in place of approximation error.
- [Normal–normal conjugacy](normal-normal-conjugacy.qmd) — the exact
  posterior used in worked example 2, where the variational family
  contains the posterior and the ELBO attains the log marginal
  likelihood.
- [Hierarchical Bayesian model](hierarchical-bayesian-model.qmd) — a
  model class in which many groups of latent variables make exact
  inference infeasible and mean-field factorisation across groups is the
  standard variational choice.
- [Prior and posterior predictive
  distributions](prior-and-posterior-predictive-distributions.qmd) —
  predictions formed from a fitted $q$ in place of the posterior; these
  can remain accurate even when the approximation understates posterior
  variance.
- [Dirichlet process](dirichlet-process.qmd) — the prior in the
  nonparametric topic model that Hoffman, Blei, Wang and Paisley fitted
  with stochastic variational inference.

## History

Variational methods entered statistics from statistical physics, where
mean-field approximations had long been used to replace interacting
systems by independent components. Peterson and Anderson's 1987
variational procedure for a neural network is identified by Blei,
Kucukelbir and McAuliffe as arguably the first such procedure for a
particular model; work through the 1990s turned these procedures into a
general method for graphical models, while a parallel line, from Hinton
and van Camp's 1993 algorithm and Neal and Hinton's connection to the EM
algorithm, arrived at the same objective from parameter estimation
{{cite:blei_kucukelbir_mcauliffe2017}} (§1). Jordan, Ghahramani, Jaakkola
and Saul's 1999 tutorial, "An Introduction to Variational Methods for
Graphical Models", gave the unified presentation: variational
transformations, bounds on probabilities of interest, and the derivation,
through Jensen's inequality and convex duality, of the lower bound on
the log likelihood whose gap is the Kullback–Leibler divergence
{{cite:jordan_etal1999_variational}} (§§5–6, pp. 183–185, 213–215).

Hoffman, Blei, Wang and Paisley's stochastic variational inference of
2013 then changed the scale at which the method operates, replacing
batch coordinate ascent with stochastic optimisation on natural gradients
and demonstrating fits on document collections in the millions
{{cite:hoffman_etal2013_svi}} (§§1–2, pp. 1303–1305). Work in the same
period on black-box and reparameterisation gradients removed the need for
model-specific coordinate updates, and Blei, Kucukelbir and McAuliffe's
2017 review in the *Journal of the American Statistical Association*
presented the method to a statistical audience and catalogued its open
problems, among them the absence of a statistical theory comparable to
that available for Markov chain Monte Carlo
{{cite:blei_kucukelbir_mcauliffe2017}} (§§5.2–5.4). Nonparametric
extensions, in which some latent variables are governed by a [Dirichlet
process](dirichlet-process.qmd), were among the early large-scale
applications of the stochastic algorithm
{{cite:hoffman_etal2013_svi}} (abstract, p. 1303).

## Check yourself

1. In worked example 1, the optimal mean-field factors have variance
$0.36$ while the true marginal variances are $1$. Where does the number
$0.36$ come from, and why does minimising $\mathrm{KL}(q \| p)$ produce
it rather than the marginal variance?

::: {.callout-tip collapse="true" title="Answer"}

$0.36 = 1 - \rho^2$ with $\rho = 0.8$. It is the reciprocal of the
diagonal entry of the posterior precision matrix, and it equals the
conditional variance of either variable given the other under the
posterior. The divergence $\mathrm{KL}(q \| p)$ is weighted by $q$, so it
penalises $q$ for placing mass where $p$ has little mass far more than it
penalises $q$ for omitting mass where $p$ has it. A factorised $q$ with
marginal variance $1$ would place substantial mass in regions where the
correlated posterior is thin; shrinking each factor to the conditional
spread avoids that penalty, at the cost of understating the marginal
spread.

:::

2. A colleague fits a model by variational inference, obtains
$\mathrm{ELBO}(q^{*}) = -512.3$, and reports $\log p(x) = -512.3$ as the
model's log marginal likelihood. What is wrong, and what can be said
about $\log p(x)$?

::: {.callout-tip collapse="true" title="Answer"}

The identity $\log p(x) = \mathrm{ELBO}(q) +
\mathrm{KL}(q \| p(z \mid x))$ holds for every $q$, and the divergence
is nonnegative, so $\log p(x) \ge -512.3$, with equality only if the
fitted $q^{*}$ equals the posterior. What can be said is that $-512.3$
is a lower bound on the log marginal likelihood, and that the size of
the gap is exactly the divergence of the approximation — which is
unknown, because computing it would require the evidence itself.
Reporting the bound as the evidence understates the log marginal
likelihood by that unknown amount — and understates the marginal
likelihood itself by the multiplicative factor
$e^{-\mathrm{KL}(q^{*} \| p)}$, not by an additive amount.

:::

3. In worked example 2, the ELBO at the optimum equals the log marginal
likelihood exactly, yet in worked example 1 a gap of about $0.511$ nats
remains at the optimum. Both optimisations were carried out exactly.
What differs between the two examples?

::: {.callout-tip collapse="true" title="Answer"}

The approximating family. In example 2 the family of all normal
densities contains the true posterior, so the minimum of the divergence
over the family is zero and the ELBO attains $\log p(x)$. In example 1
the mean-field family contains only factorised densities, and the
correlated posterior is not among them, so the smallest achievable
divergence is $-\tfrac{1}{2}\log(1 - \rho^2) \approx 0.511$ nats. The
residual gap is approximation error, fixed by the family; no improvement
in the optimisation could remove it. Only enlarging the family — for
instance to full-rank Gaussians, which contain this posterior — would
close it.

:::
