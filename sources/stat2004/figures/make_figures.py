"""Draw the figures for the Statistical inference chapters.

Run from anywhere: python sources/stat2004/figures/make_figures.py
It writes one PDF per figure next to this file. The build converts them to PNG.
Needs numpy, scipy and matplotlib. Random draws use fixed seeds, so the
figures come out the same every time.
"""

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


def coverage():
    # Seed 28 gives 2 misses in 40, the expected number at 95%.
    rng = np.random.default_rng(28)
    mu, n, reps = 10.0, 10, 40
    q = stats.t.ppf(0.975, n - 1)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    for k in range(reps):
        x = rng.normal(mu, 1.0, n)
        half = q * x.std(ddof=1) / np.sqrt(n)
        lo, hi = x.mean() - half, x.mean() + half
        miss = not (lo < mu < hi)
        ax.plot([k + 1, k + 1], [lo, hi], color=RED if miss else NAVY, lw=2.2 if miss else 1.4)
        ax.plot(k + 1, x.mean(), "o", ms=3, color=RED if miss else NAVY)
    ax.axhline(mu, color="#333333", lw=0.9, ls="--")
    ax.text(reps + 0.8, mu, r"$\mu$", va="center")
    ax.set_xlabel("sample number")
    ax.set_ylabel(r"95% interval for $\mu$")
    ax.set_xlim(0, reps + 2)
    save(fig, "inf-coverage")


def t_densities():
    x = np.linspace(-5, 5, 600)
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.plot(x, stats.norm.pdf(x), color="#222222", lw=1.6, label="standard normal")
    for df, col, ls in ((1, RED, "-"), (3, TAN, "-"), (10, NAVY, "--")):
        ax.plot(x, stats.t.pdf(x, df), color=col, lw=1.6, ls=ls, label=rf"$t_{{{df}}}$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel("density")
    ax.legend(loc="upper right")
    save(fig, "inf-t-densities")


def p_value_area():
    # Caffeine example: one-sided t test on 39 degrees of freedom.
    t_obs, df, crit = 2.575, 39, stats.t.ppf(0.99, 39)
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), gridspec_kw={"width_ratios": [1.3, 1]})
    for ax, (a, b) in zip(axes, ((-4, 4), (2.0, 4.0))):
        x = np.linspace(a, b, 600)
        y = stats.t.pdf(x, df)
        ax.plot(x, y, color=NAVY, lw=1.6)
        right = x >= crit
        ax.fill_between(x[right], y[right], color=BLUE, label="critical region, area 0.01")
        beyond = x >= t_obs
        ax.fill_between(x[beyond], y[beyond], color=RED, alpha=0.75, label=r"$p$-value, area 0.007")
        ax.axvline(t_obs, color=RED, lw=1)
        ax.set_xlabel(r"$T$ under $H_0$")
    axes[0].set_ylabel(r"$t_{39}$ density")
    axes[0].axvspan(2.0, 4.0, color="#f3f5f7", zorder=0)
    axes[0].set_title("whole density", fontsize=10)
    axes[1].set_title("right tail, enlarged", fontsize=10)
    axes[1].text(t_obs + 0.06, 0.028, rf"$t={t_obs}$", color=RED)
    axes[1].text(crit - 0.06, 0.006, rf"$t_{{39;0.99}}={crit:.2f}$", ha="right", color=NAVY)
    axes[1].legend(loc="upper right", fontsize=8)
    save(fig, "inf-p-value")


def power_curve():
    p = np.linspace(0.4, 1, 300)
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.plot(p, stats.binom.sf(12, 15, p), color=NAVY, lw=1.8, label=r"reject when $X\geq 13$")
    ax.plot(p, stats.binom.sf(11, 15, p), color=TAN, lw=1.8, ls="--", label=r"reject when $X\geq 12$")
    ax.axvline(0.6, color=GREY, lw=0.9)
    ax.text(0.605, 0.85, r"$H_0:\ p=0.6$", color="#444444")
    for c, col in ((12, NAVY), (11, TAN)):
        size = stats.binom.sf(c, 15, 0.6)
        ax.plot(0.6, size, "o", color=col, ms=4)
    ax.set_xlabel(r"true first-serve probability $p$")
    ax.set_ylabel("power")
    ax.set_ylim(0, 1.02)
    ax.legend(loc="center right")
    save(fig, "inf-power-curve")


def houses():
    counts = np.array([584, 398, 168, 35, 9, 4, 0, 1, 0, 1])
    k = np.arange(len(counts))
    mu = (k * counts).sum() / counts.sum()
    expected = counts.sum() * stats.poisson.pmf(k, mu)
    fig, ax = plt.subplots(figsize=(7, 3.0))
    ax.bar(k - 0.2, counts, width=0.4, color=NAVY, label="observed plots")
    ax.bar(k + 0.2, expected, width=0.4, color=TAN, label=rf"Poisson($\hat\mu={mu:.3f}$) expectation")
    ax.set_xticks(k)
    ax.set_xlabel("houses on a plot")
    ax.set_ylabel("number of plots")
    ax.legend(loc="upper right")
    save(fig, "inf-houses-poisson")


def heart_oxygen():
    hr = np.array([94, 96, 95, 95, 94, 95, 94, 104, 104, 106, 108, 110, 113, 113, 118, 115, 121, 127, 131.0])
    vo = np.array([0.473, 0.753, 0.929, 0.939, 0.832, 0.983, 1.049, 1.178, 1.176, 1.292,
                   1.403, 1.499, 1.529, 1.599, 1.749, 1.746, 1.897, 2.040, 2.231])
    n = len(hr)
    fit = stats.linregress(hr, vo)
    s = np.sqrt(((vo - fit.intercept - fit.slope * hr) ** 2).sum() / (n - 2))
    sxx = ((hr - hr.mean()) ** 2).sum()
    q = stats.t.ppf(0.975, n - 2)
    x = np.linspace(90, 142, 200)
    yhat = fit.intercept + fit.slope * x
    mean_half = q * s * np.sqrt(1 / n + (x - hr.mean()) ** 2 / sxx)
    pred_half = q * s * np.sqrt(1 + 1 / n + (x - hr.mean()) ** 2 / sxx)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.fill_between(x, yhat - pred_half, yhat + pred_half, color=BLUE, label="95% prediction interval")
    ax.fill_between(x, yhat - mean_half, yhat + mean_half, color=TAN, label="95% interval for the mean")
    ax.plot(x, yhat, color=NAVY, lw=1.2)
    ax.plot(hr, vo, "o", color=NAVY, ms=4)
    ax.axvspan(131, 142, color="#f3f5f7", zorder=0)
    ax.text(132, 0.6, "beyond the\nobserved rates", color="#555555", fontsize=9)
    ax.set_xlabel("heart rate (beats per minute)")
    ax.set_ylabel(r"oxygen intake")
    ax.set_xlim(90, 142)
    ax.legend(loc="upper left")
    save(fig, "inf-heart-oxygen")


def regression_effect():
    # Simulated father and son heights with the published summary values:
    # means 67 and 68 inches, both standard deviations 2.7, correlation 0.5.
    rng = np.random.default_rng(1078)
    n, rho, sd = 1078, 0.5, 2.7
    u, v = rng.standard_normal((2, n))
    father = 67 + sd * u
    son = 68 + sd * (rho * u + np.sqrt(1 - rho**2) * v)
    fit = stats.linregress(father, son)
    x = np.linspace(58, 76, 50)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(father, son, "o", ms=2.2, color=NAVY, alpha=0.45)
    ax.plot(x, x + 1, color=RED, lw=1.4, ls="--", label=r"$y=x+1$")
    ax.plot(x, fit.intercept + fit.slope * x, color="#222222", lw=1.6, label=rf"least squares, slope ${fit.slope:.2f}$")
    for centre in (63, 71):
        ax.axvspan(centre - 0.5, centre + 0.5, color=TAN, alpha=0.35, zorder=0)
    ax.set_xlabel("height of the father (inches)")
    ax.set_ylabel("height of the son (inches)")
    ax.legend(loc="upper left")
    save(fig, "inf-regression-effect")


def hardness():
    y = np.array([[9.3, 9.4, 9.2, 9.7], [9.4, 9.3, 9.4, 9.6], [9.6, 9.8, 9.5, 10.0], [10.0, 9.9, 9.7, 10.2]])
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), sharey=True)
    tips = np.arange(1, 5)
    for i in range(4):
        axes[0].plot(tips, y[i], "o", color=NAVY, ms=4)
    axes[0].set_title("ignoring the coupon", fontsize=10)
    shades = ("#9fb7d3", "#5f86b2", NAVY, "#0d2747")
    for i in range(4):
        axes[1].plot(tips, y[i], "-o", color=shades[i], ms=4, lw=1.2, label=f"coupon {i + 1}")
    axes[1].set_title("one line per coupon", fontsize=10)
    for ax in axes:
        ax.set_xticks(tips)
        ax.set_xlabel("tip")
    axes[0].set_ylabel("hardness reading")
    axes[1].legend(loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=8)
    save(fig, "inf-hardness-blocks")


def corn():
    groups = [[46.2, 51.9, 48.7], [49.2, 58.6, 57.4], [60.3, 58.7, 60.4], [48.9, 51.4, 44.6], [52.5, 54.0, 49.3]]
    means = [np.mean(g) for g in groups]
    grand = np.mean(np.concatenate(groups))
    fig, ax = plt.subplots(figsize=(7, 3.0))
    for j, g in enumerate(groups, 1):
        ax.plot([j] * len(g), g, "o", color=NAVY, ms=5)
        ax.plot([j - 0.25, j + 0.25], [means[j - 1]] * 2, color=RED, lw=2)
    ax.axhline(grand, color=GREY, ls="--", lw=1)
    ax.text(5.35, grand, "grand\nmean", va="center", fontsize=9, color="#555555")
    ax.set_xticks(range(1, 6))
    ax.set_xlim(0.5, 5.9)
    ax.set_xlabel("variety")
    ax.set_ylabel("yield")
    save(fig, "inf-corn-groups")


if __name__ == "__main__":
    for draw in (coverage, t_densities, p_value_area, power_curve, houses, heart_oxygen, regression_effect, hardness, corn):
        draw()
    print("Figures written to", HERE)
