## Motivating example
A walker chooses among neighboring sites on a path. The interior sites have two neighbors while endpoints have only one. Equal chance of choosing each available edge does not give equal long-run occupancy of the sites. The four-state chain makes that distinction visible while allowing every calculation by hand. Random walks on finite undirected graphs have stationary weights proportional to vertex degree.{{cite:durrett2012_essentials}} (§1.6.2, ex. 1.33, p. 34)

## Definition
States $1,2,3,4$ lie on a path. At every state the chain stays put with probability $1/2$. From an endpoint it moves to the only neighbour with probability $1/2$. From an interior state it moves left or right with probability $1/4$ each. With columns indexing the current state and rows the next state,
$$
Q=\begin{pmatrix}
1/2&1/4&0&0\\
1/2&1/2&1/4&0\\
0&1/4&1/2&1/2\\
0&0&1/4&1/2
\end{pmatrix}.
$$
Thus $Q_{ij}=P(X_{t+1}=i\mid X_t=j)$, columns sum to one, and a probability column evolves by $v_{t+1}=Qv_t$. Many books use row-stochastic matrices and row probability vectors; their matrix is $Q^\top$. Transposing changes the notation, not the process. A two-step probability sums over every possible intermediate state.{{cite:grinstead_snell1997}} (§11.1, transition matrices and multistep probabilities)

## Properties — Balance, symmetry and convergence
The edge flow between 1 and 2 is $\pi_1/2$ in one direction and $\pi_2/4$ in the other. Equating them gives $\pi_2=2\pi_1$; the other edges give $\pi_3=\pi_2$ and $\pi_4=\pi_1$. Thus the probability vector is $(1,2,2,1)^\top/6$. Summing pairwise balance over the departing state proves $Q\pi=\pi$, because each column's outgoing probabilities sum to one.{{cite:durrett2012_essentials}} (§1.6.2, eq. 1.11, p. 31)

To verify convergence directly, let $D=\operatorname{diag}(\pi)$. Detailed balance makes $D^{-1/2}QD^{1/2}$ symmetric, so $Q$ is diagonalizable with real eigenvalues. Its characteristic polynomial is $z(z-1)(z-3/4)(z-1/4)$. Every eigenmode except the stationary one vanishes under repeated multiplication, proving $Q^nv\to\pi$ for each initial probability vector. The self-loops remove the alternating parity behavior of a nonlazy walk on a path.{{cite:grinstead_snell1997}} (§11.3, regular chains and convergence)

## Worked example — Two steps versus equilibrium
Starting at 1 gives $v_0=(1,0,0,0)^\top$ and $v_1=(1/2,1/2,0,0)^\top$. A second multiplication gives $v_2=(3/8,1/2,1/8,0)^\top$. Equilibrium has positive probability at 4, but 4 cannot be reached from 1 in two steps. A stationary distribution describes equilibrium, not the immediate distribution from a chosen starting site.{{cite:grinstead_snell1997}} (§11.1, multistep transition probabilities)

**Your turn.** Starting at state 2, find the probability of being at state 1 after two steps.

::: {.callout-tip collapse="true" title="Answer"}
The paths are $2\to1\to1$ and $2\to2\to1$. Their probabilities are $(1/4)(1/2)$ and $(1/2)(1/4)$, totaling $1/4$.
:::

### Why the waiting-time equations have finite answers
From any starting site, a specified path can reach state 4 within three transitions with probability at least $1/32$. From 1, use $1\to2\to3\to4$, whose probability is $(1/2)(1/4)(1/4)$. From 2 or 3, a shorter path followed by self-loops gives at least the same bound. Conditioning successively at the ends of three-step blocks yields $P(T_4>3k)\le(31/32)^k$. Summing these tail bounds proves that the expected hitting time is finite, which justifies using first-step expectation equations. The bound is intentionally coarse; solving those equations extracts the sharper values. Treating a target state as absorbing turns this calculation into the usual finite absorbing-chain problem.{{cite:grinstead_snell1997}} (§11.2, expected absorption times)

## Intuition — Degree, not the self-loop, sets the long-run weight
The self-loop probability is $1/2$ at every state, so it does not by itself favour an interior state. What differs is the chance of arriving. State $2$ can be entered from $1$ and from $3$, while state $1$ can be entered only from $2$. Detailed balance turns that difference into the weights $(1,2,2,1)/6$, which are the vertex degrees of the underlying path, normalised. A long-run visitor is therefore twice as likely to be found at an interior site as at an end. The self-loops change the speed of travel. They do not change this degree weighting.{{cite:durrett2012_essentials}} (§1.6.2, eq. 1.11, p. 31){{cite:levin_peres2017}} (§1.6, pp. 13–14)

The rate of forgetting the start is set by the largest transient eigenvalue, $3/4$. After $n$ steps that mode has size $(3/4)^n$. At ten steps it is $0.05631$; at twenty steps it is $0.003171$. Starting from state $1$, the distribution at ten steps is about $(0.1854,0.3521,0.3146,0.1479)$, and the total-variation distance to $(1,2,2,1)/6$ is $0.03754$. At twenty steps that distance is $0.002114$. Equilibrium is a good description of a twenty-step position and a poor description of a two-step position, where state $4$ still has probability zero.{{cite:grinstead_snell1997}} (§11.3, regular chains and convergence)

## Common misconceptions — Stationary weight is not a hitting time
The stationary probability $1/6$ at state $4$ is the long-run fraction of visits. The expected time to reach $4$ from $1$ is $18$ steps. Those numbers answer different questions, and neither is the reciprocal of the other in a way that ignores the rest of the chain. The mean return time to $4$, for a regular chain, is $1/\pi_4=6$ steps, which counts returns after the chain has already arrived. The hitting time from a distant start includes the journey. Quoting $6$ as the time to get from state $1$ to state $4$ would be the wrong clock.{{cite:grinstead_snell1997}} (§11.5, mean first passage times)

The two-step calculation makes the same distinction in miniature. From state $2$, the probability of being at state $1$ after two steps is $1/4$, by the paths $2\to1\to1$ and $2\to2\to1$. From state $1$, two steps still cannot reach state $4$. A stationary calculation that puts mass $1/6$ on state $4$ at every time would contradict both facts. Stationarity describes the distribution that is already balanced, not the distribution that follows an arbitrary start.{{cite:grinstead_snell1997}} (§11.1, multistep transition probabilities)

## Statistical use — An arrival-time calculation
Let $h_i$ be the expected number of steps to reach 4 from $i$, with $h_4=0$. First-step conditioning gives $h_1=1+(h_1+h_2)/2$, $h_2=1+h_1/4+h_2/2+h_3/4$ and $h_3=1+h_2/4+h_3/2$. Solving yields $(h_1,h_2,h_3)=(18,16,10)$. The stationary weight $\pi_4=1/6$ alone would not give the hitting time from state 1; arrival times depend on the starting location.{{cite:grinstead_snell1997}} (§11.5, mean first passage times)
