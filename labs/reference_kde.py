#!/usr/bin/env python3
"""Independent ISE, MISE, and R bw.nrd0 for the kernel density laboratory.

Reads labs/fixtures/samples.json (exact JavaScript draws). Writes
labs/fixtures/reference.json. Does not import the JavaScript module.

ISE and MISE use the Gaussian overlap identity. They are not quadrature.
bw.nrd0 is R's stats::bw.nrd0, shelled out for every bandwidth fixture.
A second copy of the overlap formulas in R must agree with this file
before a number is written down.
"""

from __future__ import annotations

import json
import math
import random
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SAMPLES = ROOT / "fixtures" / "samples.json"
DEST = ROOT / "fixtures" / "reference.json"

# Tolerances used by labs/kde-math.test.mjs and by the R cross-check here.
TOLERANCES = {
    "bandwidthAbs": 1e-9,
    "riskAbs": 1e-8,
    "riskRel": 1e-8,
    "decompositionAbs": 1e-9,
    "kdeAbs": 1e-12,
    "quadratureAbs": 1e-4,
    "monteCarloAbs": 0.015,
    "note": (
        "bandwidthAbs is |JS - R bw.nrd0|. "
        "riskAbs and riskRel apply as |JS - reference| <= riskAbs + riskRel * |reference| "
        "for ISE, MISE, integrated variance, and integrated squared bias. "
        "decompositionAbs is |IVar + IBias^2 - MISE|. "
        "kdeAbs is the hand-evaluated kernel sum. "
        "quadratureAbs checks that phi and a three-point kernel estimate integrate to 1; "
        "ISE and MISE themselves are not integrated numerically. "
        "monteCarloAbs is |mean of exact ISE over independent Python draws - MISE|."
    ),
}

IRIS_PETAL_LENGTH = [
    1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5, 1.5, 1.6, 1.4, 1.1, 1.2, 1.5, 1.3, 1.4,
    1.7, 1.5, 1.7, 1.5, 1.0, 1.7, 1.9, 1.6, 1.6, 1.5, 1.4, 1.6, 1.6, 1.5, 1.5, 1.4, 1.5, 1.2,
    1.3, 1.4, 1.3, 1.5, 1.3, 1.3, 1.3, 1.6, 1.9, 1.4, 1.6, 1.4, 1.5, 1.4, 4.7, 4.5, 4.9, 4.0,
    4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4.0, 4.7, 3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4.0,
    4.9, 4.7, 4.3, 4.4, 4.8, 5.0, 4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1, 4.0,
    4.4, 4.6, 4.0, 3.3, 4.2, 4.2, 4.2, 4.3, 3.0, 4.1, 6.0, 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3,
    5.8, 6.1, 5.1, 5.3, 5.5, 5.0, 5.1, 5.3, 5.5, 6.7, 6.9, 5.0, 5.7, 4.9, 6.7, 4.9, 5.7, 6.0,
    4.8, 4.9, 5.6, 5.8, 6.1, 6.4, 5.6, 5.1, 5.6, 6.1, 5.6, 5.5, 4.8, 5.4, 5.6, 5.1, 5.1, 5.9,
    5.7, 5.2, 5.0, 5.2, 5.4, 5.1,
]

NORMAL = [{"weight": 1.0, "mean": 0.0, "sd": 1.0}]
BANDWIDTHS = [0.2, 0.5, 1.0, 1.5]


def phi(x: float, sd: float) -> float:
    z = x / sd
    return math.exp(-0.5 * z * z) / (sd * math.sqrt(2.0 * math.pi))


def ise(values: list[float], h: float, components: list[dict]) -> float:
    n = len(values)
    fit_sd = h * math.sqrt(2.0)
    fit = 0.0
    for xi in values:
        for xj in values:
            fit += phi(xi - xj, fit_sd)
    fit /= n * n
    cross = 0.0
    for xi in values:
        for comp in components:
            cross += comp["weight"] * phi(xi - comp["mean"], math.hypot(h, comp["sd"]))
    cross *= 2.0 / n
    truth = 0.0
    for left in components:
        for right in components:
            truth += left["weight"] * right["weight"] * phi(
                left["mean"] - right["mean"], math.hypot(left["sd"], right["sd"])
            )
    return fit - cross + truth


def omega(a: float, h: float, components: list[dict]) -> float:
    total = 0.0
    for left in components:
        for right in components:
            sd = math.sqrt(a * h * h + left["sd"] ** 2 + right["sd"] ** 2)
            total += left["weight"] * phi(left["mean"] - right["mean"], sd) * right["weight"]
    return total


def mise_parts(n: int, h: float, components: list[dict]) -> dict:
    q0 = omega(0.0, h, components)
    q1 = omega(1.0, h, components)
    q2 = omega(2.0, h, components)
    integrated_variance = (1.0 / (2.0 * math.sqrt(math.pi) * h) - q2) / n
    integrated_squared_bias = q2 - 2.0 * q1 + q0
    return {
        "integratedVariance": integrated_variance,
        "integratedSquaredBias": integrated_squared_bias,
        "mise": integrated_variance + integrated_squared_bias,
    }


def quantile_type7(sorted_values: list[float], p: float) -> float:
    n = len(sorted_values)
    pos = (n - 1) * p
    lo = math.floor(pos)
    gamma = pos - lo
    if gamma == 0 or lo >= n - 1:
        return sorted_values[min(lo, n - 1)]
    return (1.0 - gamma) * sorted_values[lo] + gamma * sorted_values[lo + 1]


def bw_nrd0(values: list[float]) -> float:
    """Python transcription of stats::bw.nrd0, checked against R before use."""
    n = len(values)
    if n < 2:
        raise ValueError("need at least 2 data points")
    mean = sum(values) / n
    hi = math.sqrt(sum((v - mean) ** 2 for v in values) / (n - 1))
    ordered = sorted(values)
    iqr = quantile_type7(ordered, 0.75) - quantile_type7(ordered, 0.25)
    lo = min(hi, iqr / 1.34)
    if not lo > 0:
        lo = hi
        if not lo > 0:
            lo = abs(values[0])
            if not lo > 0:
                lo = 1.0
    return 0.9 * lo * n ** -0.2


def r_num(values: list[float]) -> str:
    return "c(" + ",".join(format(float(v), ".17g") for v in values) + ")"


def r_batch(jobs: list[dict]) -> list[dict]:
    """jobs: {name, values, optional components and h and n}. No extra R packages."""
    lines = [
        "phi <- function(x, sd) exp(-0.5 * (x / sd)^2) / (sd * sqrt(2 * pi))",
        "ise_r <- function(x, h, w, mu, sig) {",
        "  n <- length(x)",
        "  fit <- 0",
        "  for (i in seq_len(n)) for (j in seq_len(n)) fit <- fit + phi(x[i] - x[j], h * sqrt(2))",
        "  fit <- fit / n^2",
        "  cross <- 0",
        "  for (i in seq_len(n)) for (k in seq_along(w)) cross <- cross + w[k] * phi(x[i] - mu[k], sqrt(h^2 + sig[k]^2))",
        "  cross <- 2 * cross / n",
        "  truth <- 0",
        "  for (k in seq_along(w)) for (l in seq_along(w)) truth <- truth + w[k] * w[l] * phi(mu[k] - mu[l], sqrt(sig[k]^2 + sig[l]^2))",
        "  fit - cross + truth",
        "}",
        "mise_r <- function(n, h, w, mu, sig) {",
        "  omega <- function(a) {",
        "    total <- 0",
        "    for (k in seq_along(w)) for (l in seq_along(w)) {",
        "      sd <- sqrt(a * h^2 + sig[k]^2 + sig[l]^2)",
        "      total <- total + w[k] * phi(mu[k] - mu[l], sd) * w[l]",
        "    }",
        "    total",
        "  }",
        "  q0 <- omega(0); q1 <- omega(1); q2 <- omega(2)",
        "  ivar <- (1 / (2 * sqrt(pi) * h) - q2) / n",
        "  ibias <- q2 - 2 * q1 + q0",
        "  c(ivar, ibias, ivar + ibias)",
        "}",
        "emit <- function(name, bw, ise, ivar, ibias, mise) {",
        '  cat(sprintf("%s\\t%s\\t%s\\t%s\\t%s\\t%s\\n", name, bw, ise, ivar, ibias, mise))',
        "}",
    ]
    for job in jobs:
        name = job["name"].replace('"', "")
        lines.append(f'x <- {r_num(job["values"])}')
        lines.append('bw <- tryCatch(sprintf("%.17g", as.numeric(stats::bw.nrd0(x))), error = function(e) paste0("ERROR ", conditionMessage(e)))')
        if job.get("components"):
            weights = [c["weight"] for c in job["components"]]
            means = [c["mean"] for c in job["components"]]
            sds = [c["sd"] for c in job["components"]]
            lines.append(f'w <- {r_num(weights)}')
            lines.append(f'mu <- {r_num(means)}')
            lines.append(f'sig <- {r_num(sds)}')
            lines.append(f'ise <- sprintf("%.17g", ise_r(x, {job["h"]!r}, w, mu, sig))')
            lines.append(f'risk <- mise_r({int(job["n"])}, {job["h"]!r}, w, mu, sig)')
            lines.append(
                f'emit("{name}", bw, ise, sprintf("%.17g", risk[1]), sprintf("%.17g", risk[2]), sprintf("%.17g", risk[3]))'
            )
        else:
            lines.append(f'emit("{name}", bw, "NA", "NA", "NA", "NA")')
    completed = subprocess.run(
        ["Rscript", "-"],
        input="\n".join(lines) + "\n",
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(completed.stderr[-2000:])
    rows = []
    for line in completed.stdout.splitlines():
        name, bw, ise_s, ivar_s, ibias_s, mise_s = line.split("\t")
        row: dict = {"name": name}
        if bw.startswith("ERROR "):
            row["bwError"] = bw[len("ERROR ") :]
        else:
            row["bw"] = float(bw)
        if ise_s != "NA":
            row["ise"] = float(ise_s)
            row["integratedVariance"] = float(ivar_s)
            row["integratedSquaredBias"] = float(ibias_s)
            row["mise"] = float(mise_s)
        rows.append(row)
    return rows


def trap(xs: list[float], ys: list[float]) -> float:
    total = 0.0
    for i in range(1, len(xs)):
        total += 0.5 * (ys[i] + ys[i - 1]) * (xs[i] - xs[i - 1])
    return total


def main() -> None:
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))
    risk_jobs = []
    for item in samples["samples"]:
        for h in BANDWIDTHS:
            risk_jobs.append(
                {
                    "name": f"{item['name']}-h{h}",
                    "values": item["values"],
                    "h": h,
                    "n": item["n"],
                    "components": item["components"],
                    "population": item["population"],
                    "seed": item["seed"],
                }
            )
    # One observation on the true normal: ISE is identically 0 when h = sigma = 1.
    risk_jobs.append(
        {
            "name": "point-mass-match",
            "values": [0.0],
            "h": 1.0,
            "n": 1,
            "components": NORMAL,
            "population": "normal",
            "seed": None,
        }
    )
    hand = [-1.0, 0.0, 2.0]
    risk_jobs.append(
        {
            "name": "hand-three",
            "values": hand,
            "h": 1.0,
            "n": 3,
            "components": NORMAL,
            "population": "normal",
            "seed": None,
        }
    )

    bw_only = [
        ("iris-petal-length", IRIS_PETAL_LENGTH),
        ("n-one", [1.0]),
        ("n-two", [0.0, 1.0]),
        ("constant-zero", [0.0, 0.0, 0.0, 0.0]),
        ("constant-two", [2.0, 2.0, 2.0, 2.0, 2.0]),
        ("ties", [1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0]),
        ("zero-iqr", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0]),
        ("near-zero-sd", [1.0, 1.0, 1.0 + 1e-8]),
        ("small-n-three", [5.0, 5.0, 9.0]),
        ("negatives", [-4.0, -1.0, -1.0, 0.0, 2.0, 8.0]),
        ("shifted", [1e6, 1e6 + 1.0, 1e6 + 4.0, 1e6 + 4.0]),
    ]
    for item in samples["samples"]:
        bw_only.append((f"bw-{item['name']}", item["values"]))

    r_jobs = []
    for job in risk_jobs:
        r_jobs.append(
            {
                "name": job["name"],
                "values": job["values"],
                "h": job["h"],
                "n": job["n"],
                "components": job["components"],
            }
        )
    for name, values in bw_only:
        r_jobs.append({"name": name, "values": values})

    r_rows = {row["name"]: row for row in r_batch(r_jobs)}

    cases = []
    for job in risk_jobs:
        py_ise = ise(job["values"], job["h"], job["components"])
        py_mise = mise_parts(job["n"], job["h"], job["components"])
        got = r_rows[job["name"]]
        for key, py_value in (
            ("ise", py_ise),
            ("integratedVariance", py_mise["integratedVariance"]),
            ("integratedSquaredBias", py_mise["integratedSquaredBias"]),
            ("mise", py_mise["mise"]),
        ):
            gap = abs(py_value - got[key])
            if gap > TOLERANCES["riskAbs"] + TOLERANCES["riskRel"] * abs(got[key]):
                raise SystemExit(f"{job['name']} {key}: Python {py_value} vs R {got[key]}")
        if abs(py_mise["integratedVariance"] + py_mise["integratedSquaredBias"] - py_mise["mise"]) > 0:
            raise SystemExit("MISE decomposition did not add up in Python")
        row = {
            "name": job["name"],
            "n": job["n"],
            "h": job["h"],
            "population": job["population"],
            "seed": job["seed"],
            "components": job["components"],
            "values": job["values"],
            "ise": got["ise"],
            "integratedVariance": got["integratedVariance"],
            "integratedSquaredBias": got["integratedSquaredBias"],
            "mise": got["mise"],
        }
        if "bw" in got:
            py_bw = bw_nrd0(job["values"])
            if abs(py_bw - got["bw"]) > TOLERANCES["bandwidthAbs"]:
                raise SystemExit(f"{job['name']} bw: Python {py_bw} vs R {got['bw']}")
            row["bw"] = got["bw"]
        elif job["n"] >= 2:
            raise SystemExit(f"{job['name']} missing R bandwidth")
        cases.append(row)

    bandwidth_cases = []
    for name, values in bw_only:
        got = r_rows[name]
        row = {"name": name, "values": values}
        if "bwError" in got:
            row["error"] = got["bwError"]
            try:
                bw_nrd0(values)
            except ValueError:
                pass
            else:
                if name == "n-one":
                    raise SystemExit("Python bw.nrd0 accepted n=1")
        else:
            py_bw = bw_nrd0(values)
            if abs(py_bw - got["bw"]) > TOLERANCES["bandwidthAbs"]:
                raise SystemExit(f"{name}: Python {py_bw} vs R {got['bw']}")
            if not math.isfinite(got["bw"]) or not got["bw"] > 0:
                raise SystemExit(f"{name}: R bandwidth was not strictly positive ({got['bw']})")
            row["bw"] = got["bw"]
        bandwidth_cases.append(row)

    phi0 = phi(0.0, 1.0)
    phi1 = phi(1.0, 1.0)
    phi2 = phi(2.0, 1.0)
    hand_kde = (phi1 + phi0 + phi2) / 3.0
    if round(hand_kde, 4) != 0.2316:
        raise SystemExit(f"hand kde rounded to {hand_kde}, expected 0.2316")

    grid = [(-12 + 24 * i / 4000) for i in range(4001)]
    quad_phi = trap(grid, [phi(x, 1.0) for x in grid])
    quad_kde = trap(
        grid,
        [sum(phi(x - xi, 1.0) for xi in hand) / 3.0 for x in grid],
    )

    # Monte Carlo with Python's RNG, not the JavaScript generator.
    # Mean of the exact ISE against the closed-form MISE.
    mixture = [
        {"weight": 0.5, "mean": -1.5, "sd": 0.5},
        {"weight": 0.5, "mean": 1.5, "sd": 0.5},
    ]
    mc_n = 40
    mc_h = 0.45
    mc_reps = 80
    rng = random.Random(20261109)
    mc_ises = []
    for _ in range(mc_reps):
        draw = []
        for _j in range(mc_n):
            u1 = rng.random() or 2**-32
            u2 = rng.random()
            z = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
            comp = mixture[0] if rng.random() < 0.5 else mixture[1]
            draw.append(comp["mean"] + comp["sd"] * z)
        mc_ises.append(ise(draw, mc_h, mixture))
    mc_mean = sum(mc_ises) / mc_reps
    mc_mise = mise_parts(mc_n, mc_h, mixture)["mise"]
    mc_gap = abs(mc_mean - mc_mise)
    print(f"Monte Carlo mean ISE {mc_mean:.6f} vs MISE {mc_mise:.6f}, gap {mc_gap:.6f}")
    if mc_gap > TOLERANCES["monteCarloAbs"]:
        raise SystemExit("Monte Carlo mean of exact ISE is far from MISE")

    if abs(quad_phi - 1.0) > TOLERANCES["quadratureAbs"] or abs(quad_kde - 1.0) > TOLERANCES["quadratureAbs"]:
        raise SystemExit(f"normalisation quadrature failed: phi {quad_phi}, kde {quad_kde}")
    point = next(row for row in cases if row["name"] == "point-mass-match")
    if abs(point["ise"]) > 1e-12:
        raise SystemExit(f"matched one-point ISE was {point['ise']}")

    reference = {
        "tolerances": TOLERANCES,
        "publishedHandKde4dp": 0.2316,
        "handKde": hand_kde,
        "handSample": hand,
        "handH": 1.0,
        "quadraturePhi": quad_phi,
        "quadratureKde": quad_kde,
        "monteCarlo": {"n": mc_n, "h": mc_h, "reps": mc_reps, "meanIse": mc_mean, "mise": mc_mise, "gap": mc_gap},
        "irisBwRounded4dp": round(next(row["bw"] for row in bandwidth_cases if row["name"] == "iris-petal-length"), 4),
        "cases": cases,
        "bandwidthCases": bandwidth_cases,
    }
    DEST.write_text(json.dumps(reference), encoding="utf-8")
    print(f"wrote {DEST}")
    print(f"iris bw.nrd0 rounded to 4 d.p. is {reference['irisBwRounded4dp']}")
    if reference["irisBwRounded4dp"] != 0.5832:
        raise SystemExit("iris bw.nrd0 did not match the chapter's 0.5832")


if __name__ == "__main__":
    main()
