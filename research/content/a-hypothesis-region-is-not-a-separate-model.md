## Lead context
A region has a probability under a specified posterior; treating it as a competing model additionally specifies a prior within that region and prior odds.

## Motivating example
A continuous parameter posterior places most mass above a scientific threshold. That answers a question about the parameter within one model. A comparison with an exact point-null model asks a different question because the point must receive positive prior model probability to have positive posterior probability. These two calculations can give quite different numerical answers.{{cite:kass_raftery1995}} (§5.1, pp. 781–782)

## Definition — Posterior mass on a subset
Within a likelihood family $L(\theta)$ and proper prior density $\pi(\theta)$, posterior probability of a measurable region $H$ is
$$
\mathbb{P}(H\mid x)=\frac{\int_H L(\theta)\pi(\theta)d\theta}{\int_\Theta L(\theta)\pi(\theta)d\theta},
$$
assuming the denominator is finite and positive. Calling $H$ a hypothesis does not change this integral. A continuous posterior assigns zero mass to individual points, so moving a single boundary point from one region to its complement changes neither probability.{{cite:kass_raftery1995}} (§5.1, pp. 781–782)

## Connections — Regions can induce explicitly specified models
The distinction does not prohibit model comparison between regions. If $H_0,H_1$ partition $\Theta$ and $w_k=\mathbb{P}(H_k)>0$, define conditional priors
$$
\pi_k(\theta)=\pi(\theta)\mathbf1_{H_k}(\theta)/w_k.
$$
Their marginal likelihoods are $m_k=\int L\pi_k$. Direct substitution gives
$$
\frac{\mathbb{P}(H_1\mid x)}{\mathbb{P}(H_0\mid x)}=\frac{m_1}{m_0}\frac{w_1}{w_0}.
$$
Thus a partition of one proper prior can induce two models with Bayes factor equal to posterior odds divided by prior odds. Their priors and odds are specified by the conditioning construction. Choosing different within-region priors defines a different comparison.{{cite:kass_raftery1995}} (§3.1, pp. 776–777)

## Interpretation — A surface can have zero mass
An independence model for a $2\times3$ multinomial table is a lower-dimensional subset of the saturated probability simplex. The saturated model has five free probabilities; independence has one free row probability and two free column probabilities. It is a subset of the larger parameter space, but an absolutely continuous prior on that five-dimensional space assigns the independence surface probability zero. Integrating its continuous posterior over that surface therefore cannot produce a positive posterior independence probability.{{cite:kass_raftery1995}} (§5.1, pp. 781–782)

A model-index construction instead gives positive prior weight to the independence model and a normalised parameter prior on its own lower-dimensional space. Its prior mass cannot be obtained by ordinary conditioning on a zero-probability event in the full-dimensional density. This is why the model prior is an additional specification, rather than a relabelling of a continuous posterior region.{{cite:schwarz1978}} (§2, p. 462)

## Worked example
Observe seven successes in ten independent Bernoulli trials and use a uniform prior for success probability $\theta$. Multiplying likelihood by prior gives a Beta$(8,4)$ posterior. For $H_1=\{\theta>1/2\}$,
$$
\mathbb{P}(H_1\mid x)=\frac{227}{256}=0.88671875,\qquad
\mathbb{P}(H_0\mid x)=\frac{29}{256}.
$$
The uniform prior gives equal mass to the two half-intervals. Conditioning that prior on each interval therefore produces a region-model Bayes factor $B_{10}=227/29\approx7.827586$. The equality between this factor and posterior odds uses those equal prior region probabilities.{{cite:kass_raftery1995}} (§3.1, pp. 776–777)

Now compare the exact point model $M_0:\theta=1/2$ with a uniform-prior alternative $M_1$. The sampling probability of seven successes under $M_0$ is $\binom{10}{7}2^{-10}$. Under the alternative it is $1/11$, obtained by integrating the binomial likelihood over $(0,1)$. Hence
$$
B_{01}=11\binom{10}{7}2^{-10}=\frac{165}{128}\approx1.289063.
$$
With equal prior model probabilities, $\mathbb{P}(M_0\mid x)=165/293\approx0.563140$. This point-model probability differs from both the posterior probability above one half and the zero probability of an exact point under the continuous Beta posterior. The models and their prior measures determine the question.{{cite:schwarz1978}} (§2, p. 462){{cite:kass_raftery1995}} (§5.1, pp. 781–782)

**Your turn.** Under the continuous Beta posterior, does assigning $\theta=1/2$ to $H_1$ instead of $H_0$ change the answer? What if the posterior has an atom there?

::: {.callout-tip collapse="true" title="Answer"}
The continuous posterior gives that point mass zero, so neither region probability changes. With an atom of posterior mass $a>0$ at one half, moving the boundary transfers exactly $a$ from one region probability to the other.
:::

## Check yourself
### Deriving a posterior kernel {#self-check-exr-fruit-posterior}
[Fruit posterior](../questions/exr-fruit-posterior.qmd): identify the gamma shape, rate and mean.

::: {.callout-tip collapse="true" title="Answer"}
The prior kernel is $\theta^{11}e^{-\theta}$ and the likelihood contributes $\theta^{177}e^{-20\theta}$. Their product is $\theta^{188}e^{-21\theta}$, giving shape $189$, rate $21$ and mean $9$. This lies between prior mean $12$ and maximum likelihood estimate $177/20=8.85$.
:::

### A boundary with and without an atom {#self-check-exr-who-owns-the-boundary}
[Who owns the boundary?](../questions/exr-who-owns-the-boundary.qmd): prove the continuous result and give a discrete contrast.

::: {.callout-tip collapse="true" title="Answer"}
A density integrates to zero over a singleton, so the continuous posterior gives $\mathbb{P}(\theta=10\mid x)=0$. Adding or removing that point changes a region integral by zero. In contrast, if a discrete posterior assigns probability $0.3$ to $\theta=10$, changing which hypothesis contains ten changes each region probability by $0.3$ in opposite directions.
:::
