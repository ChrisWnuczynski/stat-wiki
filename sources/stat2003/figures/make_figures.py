"""Draw the figures for the Probability chapters.

Run this file with Python. It writes one PDF per figure next to this file.
The build converts them to PNG.
Needs numpy, scipy and matplotlib. Random draws use fixed seeds, so the
figures come out the same every time.
"""

from math import comb
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from scipy import stats  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY, RED, TAN, BLUE, GREY = "#1d4a7a", "#a83232", "#d6bf98", "#c9d6e6", "#8a8f98"

plt.rcParams.update(
    {
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 10,
        "axes.edgecolor": "#444444",
        "axes.linewidth": 0.8,
        "axes.grid": True,
        "grid.color": "#e3e6ea",
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "savefig.bbox": "tight",
    }
)


def save(fig, name):
    fig.savefig(HERE / f"{name}.pdf")
    plt.close(fig)


def coin_averages():
    rng = np.random.default_rng(2003)
    n = 100
    t = np.arange(1, n + 1)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    for _ in range(20):
        x = rng.random(n) < 0.5
        ax.plot(t, np.cumsum(x) / t, color=NAVY, alpha=0.35, lw=1)
    ax.axhline(0.5, color=RED, lw=1, ls="--")
    ax.set_xlabel("number of tosses $n$")
    ax.set_ylabel("proportion of heads")
    ax.set_ylim(0, 1)
    save(fig, "prob-coin-averages")


def birthday():
    n = np.arange(1, 81)
    p = 1 - np.cumprod((365 - n + 1) / 365)
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(n, p, color=NAVY, lw=1.8)
    ax.axhline(0.5, color=GREY, lw=0.9, ls="--")
    ax.plot(23, p[22], "o", color=RED, ms=5)
    ax.annotate(f"23 people: {p[22]:.3f}", (23, p[22]), xytext=(30, 0.35), color=RED,
                arrowprops={"arrowstyle": "-", "color": RED, "lw": 0.8})
    ax.set_xlabel("number of people $n$")
    ax.set_ylabel("P(some shared birthday)")
    ax.set_ylim(0, 1.02)
    save(fig, "prob-birthday")


def discrete_pmfs():
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 2.6))
    k = np.arange(0, 11)
    axes[0].bar(k, stats.binom.pmf(k, 10, 0.7), color=NAVY, width=0.7)
    axes[0].set_title(r"$\mathrm{Bin}(10,\ 0.7)$", fontsize=10)
    k = np.arange(1, 16)
    axes[1].bar(k, stats.geom.pmf(k, 0.3), color=NAVY, width=0.7)
    axes[1].set_title(r"$\mathrm{Geom}(0.3)$", fontsize=10)
    k = np.arange(0, 25)
    axes[2].bar(k, stats.poisson.pmf(k, 10), color=NAVY, width=0.7)
    axes[2].set_title(r"$\mathrm{Poisson}(10)$", fontsize=10)
    for ax in axes:
        ax.set_xlabel("$x$")
    axes[0].set_ylabel("probability")
    fig.tight_layout()
    save(fig, "prob-discrete-pmfs")


def continuous_densities():
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 2.8))
    x = np.linspace(0, 5, 400)
    for lam, col in ((0.5, TAN), (1, NAVY), (2, RED)):
        axes[0].plot(x, lam * np.exp(-lam * x), color=col, lw=1.6, label=rf"$\lambda={lam}$")
    axes[0].set_title("exponential", fontsize=10)
    axes[0].legend()
    x = np.linspace(-5, 5, 400)
    for s, col in ((0.5, RED), (1, NAVY), (2, TAN)):
        axes[1].plot(x, stats.norm.pdf(x, 0, s), color=col, lw=1.6, label=rf"$\sigma={s}$")
    axes[1].set_title(r"normal, $\mu=0$", fontsize=10)
    axes[1].legend()
    for ax in axes:
        ax.set_xlabel("$x$")
    axes[0].set_ylabel("density")
    fig.tight_layout()
    save(fig, "prob-continuous-densities")


def inverse_transform():
    x = np.linspace(-0.5, 4, 400)
    F = stats.gamma.cdf(x, 2, scale=0.6)
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.plot(x, F, color=NAVY, lw=1.8)
    for u in (0.2, 0.55, 0.85):
        xq = stats.gamma.ppf(u, 2, scale=0.6)
        ax.plot([-0.5, xq], [u, u], color=RED, lw=0.9, ls="--")
        ax.plot([xq, xq], [u, 0], color=RED, lw=0.9, ls="--")
        ax.plot(xq, 0, "o", color=RED, ms=4)
        ax.text(-0.45, u + 0.02, rf"$U={u}$", color=RED, fontsize=9)
    ax.set_xlabel(r"$x$, with $X=F^{-1}(U)$ marked on the axis")
    ax.set_ylabel("$F(x)$")
    ax.set_xlim(-0.5, 4)
    ax.set_ylim(0, 1.02)
    save(fig, "prob-inverse-transform")


def acceptance_rejection():
    rng = np.random.default_rng(7)
    n = 600
    x = rng.random(n)
    y = 1.5 * rng.random(n)
    keep = y <= 6 * x * (1 - x)
    xs = np.linspace(0, 1, 300)
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.plot(x[~keep], y[~keep], "o", ms=2.5, color=BLUE)
    ax.plot(x[keep], y[keep], "o", ms=2.5, color=NAVY)
    ax.plot(xs, 6 * xs * (1 - xs), color=RED, lw=1.6)
    ax.axhline(1.5, color=GREY, lw=0.9, ls="--")
    ax.set_title(f"{keep.sum()} of {n} kept", fontsize=10)
    ax.set_xlabel("$X$")
    ax.set_ylabel("$Y$")
    save(fig, "prob-acceptance-rejection")


def correlation():
    rng = np.random.default_rng(4)
    fig, axes = plt.subplots(1, 4, figsize=(7.8, 2.2), sharex=True, sharey=True)
    for ax, rho in zip(axes, (0, 0.4, 0.7, -0.9)):
        u, v = rng.standard_normal((2, 200))
        ax.plot(u, rho * u + np.sqrt(1 - rho**2) * v, "o", ms=2, color=NAVY, alpha=0.7)
        ax.set_title(rf"$\rho={rho}$", fontsize=10)
        ax.set_aspect("equal")
    axes[0].set_xlim(-3.5, 3.5)
    axes[0].set_ylim(-3.5, 3.5)
    save(fig, "prob-correlation")


def clt():
    rng = np.random.default_rng(5)
    fig, axes = plt.subplots(2, 3, figsize=(7.6, 4.0), sharex=True)
    z = np.linspace(-4, 4, 300)
    for row, (name, draw, mu, sd) in enumerate(
        (("uniform", lambda s: rng.random(s), 0.5, np.sqrt(1 / 12)), ("exponential", lambda s: rng.exponential(1, s), 1, 1))
    ):
        for col, n in enumerate((1, 2, 10)):
            s = draw((20000, n)).sum(1)
            zs = (s - n * mu) / (sd * np.sqrt(n))
            ax = axes[row, col]
            ax.hist(zs, bins=60, range=(-4, 4), density=True, color=BLUE)
            ax.plot(z, stats.norm.pdf(z), color=RED, lw=1.2)
            ax.set_title(f"{name}, $n={n}$", fontsize=9)
            ax.set_ylim(0, 0.8)
    for ax in axes[1]:
        ax.set_xlabel("standardised sum")
    save(fig, "prob-clt")


def binomial_normal():
    k = np.arange(0, 21)
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.step(np.r_[-1, k], np.r_[0, stats.binom.cdf(k, 20, 0.5)], where="post", color=NAVY, lw=1.6, label=r"$\mathrm{Bin}(20,1/2)$")
    x = np.linspace(-1, 21, 400)
    ax.plot(x, stats.norm.cdf(x, 10, np.sqrt(5)), color=RED, lw=1.3, label=r"$\mathrm{N}(10,5)$")
    ax.set_xlim(2, 18)
    ax.set_xlabel("$k$")
    ax.set_ylabel(r"$P(X\leq k)$")
    ax.legend(loc="upper left")
    save(fig, "prob-binomial-normal")


def stepping_stones():
    P = np.array([[0, 1 / 3, 0, 1 / 3, 1 / 3, 0], [0.5, 0, 0.5, 0, 0, 0], [0.5, 0, 0, 0.5, 0, 0],
                  [0, 0, 0, 0, 0, 1], [0, 0, 0, 0.5, 0, 0.5], [0, 0, 0.5, 0, 0.5, 0]])
    rng = np.random.default_rng(6)
    path = [0]
    for _ in range(60):
        path.append(rng.choice(6, p=P[path[-1]]))
    fig, axes = plt.subplots(1, 2, figsize=(7.8, 2.9))
    axes[0].plot(np.array(path) + 1, "-o", color=NAVY, ms=3, lw=0.8)
    axes[0].set_xlabel("step")
    axes[0].set_ylabel("stone")
    axes[0].set_yticks(range(1, 7))
    pi = np.array([12, 4, 20, 25, 22, 36]) / 119
    dist = [np.eye(6)[0]]
    for _ in range(30):
        dist.append(dist[-1] @ P)
    dist = np.array(dist)
    shades = ("#0d2747", NAVY, "#5f86b2", "#9fb7d3", TAN, RED)
    for j in range(6):
        axes[1].plot(dist[:, j], color=shades[j], lw=1.3, label=f"stone {j + 1}")
        axes[1].axhline(pi[j], color=shades[j], lw=0.8, ls="--")
    axes[1].set_xlabel("step $n$")
    axes[1].set_ylabel("probability")
    axes[1].legend(fontsize=7, ncol=2, loc="upper right")
    fig.tight_layout()
    save(fig, "prob-stepping-stones")


def random_walk():
    rng = np.random.default_rng(8)
    steps = rng.choice([-1, 1], 500)
    fig, ax = plt.subplots(figsize=(7, 2.8))
    ax.plot(np.r_[0, np.cumsum(steps)], color=NAVY, lw=1)
    ax.axhline(0, color=GREY, lw=0.9)
    ax.set_xlabel("step $n$")
    ax.set_ylabel("$X_n$")
    save(fig, "prob-random-walk")


def systems():
    fig, axes = plt.subplots(1, 3, figsize=(7.8, 2.2), gridspec_kw={"width_ratios": [1, 1, 1.2]})

    def box(ax, x, y, label):
        ax.add_patch(plt.Rectangle((x - 0.25, y - 0.18), 0.5, 0.36, fc="white", ec=NAVY, lw=1.2, zorder=3))
        ax.text(x, y, label, ha="center", va="center", zorder=4)

    def line(ax, xs, ys):
        ax.plot(xs, ys, color="#333333", lw=1, zorder=1)

    ax = axes[0]
    line(ax, [0, 4], [0, 0])
    for i, x in enumerate((1, 2, 3), 1):
        box(ax, x, 0, str(i))
    ax.set_title("series", fontsize=10)
    ax.set_xlim(-0.2, 4.2)
    ax.set_ylim(-1.2, 1.2)
    ax = axes[1]
    line(ax, [0, 0.8], [0, 0])
    line(ax, [3.2, 4], [0, 0])
    line(ax, [0.8, 0.8], [-0.8, 0.8])
    line(ax, [3.2, 3.2], [-0.8, 0.8])
    for i, y in enumerate((0.8, 0, -0.8), 1):
        line(ax, [0.8, 3.2], [y, y])
        box(ax, 2, y, str(i))
    ax.set_title("parallel", fontsize=10)
    ax.set_xlim(-0.2, 4.2)
    ax.set_ylim(-1.2, 1.2)
    ax = axes[2]
    a, b, top, bot = (0, 0), (5, 0), (2.5, 0.85), (2.5, -0.85)
    line(ax, [a[0], top[0]], [a[1], top[1]])
    line(ax, [a[0], bot[0]], [a[1], bot[1]])
    line(ax, [top[0], b[0]], [top[1], b[1]])
    line(ax, [bot[0], b[0]], [bot[1], b[1]])
    line(ax, [top[0], bot[0]], [top[1], bot[1]])
    box(ax, 1.25, 0.43, "1")
    box(ax, 1.25, -0.43, "2")
    box(ax, 2.5, 0, "3")
    box(ax, 3.75, 0.43, "4")
    box(ax, 3.75, -0.43, "5")
    ax.set_title("bridge", fontsize=10)
    ax.set_xlim(-0.2, 5.2)
    ax.set_ylim(-1.2, 1.2)
    for ax in axes:
        ax.axis("off")
    save(fig, "prob-systems")


def system_survival():
    t = np.linspace(0, 3, 400)
    q = np.exp(-t)
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(t, q, color="#222222", lw=1.6, label="one component, mean 1")
    ax.plot(t, 2 * q - q**2, color=NAVY, lw=1.6, label="two in parallel, mean 1.5")
    ax.plot(t, q**2, color=TAN, lw=1.6, label="two in series, mean 0.5")
    ax.plot(t, 3 * q**2 - 2 * q**3, color=RED, lw=1.6, ls="--", label="2 out of 3, mean 0.83")
    ax.axvline(np.log(2), color=GREY, lw=0.8)
    ax.set_xlabel("time $t$")
    ax.set_ylabel("P(system works at $t$)")
    ax.legend(loc="upper right")
    save(fig, "prob-system-survival")


def weibull_hazards():
    t = np.linspace(0.01, 2.5, 400)
    fig, ax = plt.subplots(figsize=(7, 3.0))
    for beta, col in ((0.5, TAN), (1, NAVY), (2, RED), (3, "#0d2747")):
        ax.plot(t, beta * t ** (beta - 1), color=col, lw=1.6, label=rf"$\beta={beta}$")
    ax.set_ylim(0, 4)
    ax.set_xlabel("time $t$")
    ax.set_ylabel("hazard $h(t)$")
    ax.legend(loc="upper left")
    save(fig, "prob-weibull-hazards")


if __name__ == "__main__":
    for draw in (coin_averages, birthday, discrete_pmfs, continuous_densities, inverse_transform, acceptance_rejection,
                 correlation, clt, binomial_normal, stepping_stones, random_walk, systems, system_survival, weibull_hazards):
        draw()
    print("Figures written to", HERE)
