"""Parameter-labelled previews for scalar and selected vector distributions."""

from __future__ import annotations

import math
import os
from pathlib import Path


def write_plots(facts: dict, target: Path) -> None:
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/statwiki-matplotlib")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import stats
    from scipy.special import gammaln

    target.mkdir(parents=True, exist_ok=True)
    for stale in target.glob("*.png"):
        stale.unlink()
    discrete = {"bernoulli", "binom", "compoisson", "geom", "hypergeom", "nbinom", "poisson"}
    for slug, item in facts.items():
        spec = item["plot"]
        if not spec:
            continue
        kind = spec["scipy"]
        if kind == "mvnorm2":
            mean, cov = spec["args"]
            coords = np.linspace(-3, 3, 65)
            xx, yy = np.meshgrid(coords, coords)
            points = np.stack((xx, yy), axis=-1)
            law = stats.multivariate_normal(mean=mean, cov=cov)
            for view in spec["views"]:
                zz = law.pdf(points) if view == "pdf" else law.cdf(points)
                fig, ax = plt.subplots(figsize=(4.6, 3.4))
                filled = ax.contourf(xx, yy, zz, levels=12, cmap="Blues")
                ax.contour(xx, yy, zz, levels=7, colors="#17436c", linewidths=0.5)
                ax.set(xlabel="first component", ylabel="second component",
                       title=f"Bivariate normal {view.upper()} ({spec['parameters']})", aspect="equal")
                fig.colorbar(filled, ax=ax, shrink=0.8)
                fig.tight_layout()
                fig.savefig(target / f"{slug}-{view}.png", dpi=120)
                plt.close(fig)
            continue
        if kind in {"dirichlet3", "multinomial3"}:
            if kind == "dirichlet3":
                alpha = np.asarray(spec["args"], dtype=float)
                x1, x2 = np.meshgrid(np.linspace(0.01, 0.98, 70), np.linspace(0.01, 0.98, 70))
                x3 = 1 - x1 - x2
                inside = x3 > 0.01
                a, b, c = x1[inside], x2[inside], x3[inside]
                density = np.exp(gammaln(alpha.sum()) - gammaln(alpha).sum()
                                 + (alpha[0] - 1) * np.log(a) + (alpha[1] - 1) * np.log(b)
                                 + (alpha[2] - 1) * np.log(c))
                title = "Dirichlet density"
            else:
                n, probabilities = spec["args"]
                a, b = np.meshgrid(np.arange(n + 1), np.arange(n + 1))
                c = n - a - b
                inside = c >= 0
                counts = np.stack((a[inside], b[inside], c[inside]), axis=-1)
                a, b, c = counts[:, 0] / n, counts[:, 1] / n, counts[:, 2] / n
                density = stats.multinomial.pmf(counts, n=n, p=probabilities)
                title = "Multinomial PMF"
            horizontal = b + 0.5 * c
            vertical = math.sqrt(3) * c / 2
            fig, ax = plt.subplots(figsize=(4.6, 3.8))
            if kind == "dirichlet3":
                colored = ax.tricontourf(horizontal, vertical, density, levels=12, cmap="Blues")
            else:
                colored = ax.scatter(horizontal, vertical, c=density, s=22 + 1600 * density,
                                     cmap="Blues", edgecolor="#17436c", linewidth=0.3)
            ax.plot([0, 1, 0.5, 0], [0, 0, math.sqrt(3) / 2, 0], color="#17436c", linewidth=1)
            ax.set(xlabel="second category share", ylabel="third category share",
                   title=f"{title} ({spec['parameters']})", aspect="equal")
            fig.colorbar(colored, ax=ax, shrink=0.8)
            fig.tight_layout()
            fig.savefig(target / f"{slug}-pdf.png", dpi=120)
            plt.close(fig)
            continue
        lo, hi = spec["domain"]
        x = np.arange(int(lo), int(hi) + 1) if kind in discrete else np.linspace(lo, hi, 500)
        if kind == "compoisson":
            lam, nu = spec["args"]
            weights = np.array([math.exp(k * math.log(lam) - nu * math.lgamma(k + 1)) for k in range(120)])
            weights /= weights.sum()
            y_pdf = weights[x.astype(int)]
            y_cdf = np.cumsum(weights)[x.astype(int)]
        else:
            law = getattr(stats, kind)(*spec["args"])
            y_pdf = law.pmf(x) if kind in discrete else law.pdf(x)
            y_cdf = law.cdf(x)
        for label, y in (("pdf", y_pdf), ("cdf", y_cdf)):
            if label not in spec["views"]:
                continue
            fig, ax = plt.subplots(figsize=(4.6, 2.7))
            if kind in discrete:
                ax.vlines(x, 0, y, color="#2563a6", linewidth=1.8)
                ax.plot(x, y, "o", color="#2563a6", markersize=3)
            else:
                ax.plot(x, y, color="#2563a6", linewidth=2)
            chart = "PMF" if kind in discrete and label == "pdf" else label.upper()
            ax.set(xlabel="x", ylabel=chart, title=f"{chart} ({spec['parameters']})")
            ax.set_xlim(lo, hi)
            ax.set_ylim(bottom=0, top=1.04 if label == "cdf" else None)
            ax.grid(alpha=0.18)
            fig.tight_layout()
            fig.savefig(target / f"{slug}-{label}.png", dpi=120)
            plt.close(fig)
