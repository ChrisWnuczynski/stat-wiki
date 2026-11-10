// Node test for the shared distribution functions. No browser.
// Reference numbers were computed by labs/reference_stats.py with SciPy.
//
// Tolerances live in labs/fixtures/stats-reference.json:
//   |JS - reference| <= abs + rel * |reference|

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import * as math from "./stat-math.js";

const root = dirname(fileURLToPath(import.meta.url));
const reference = JSON.parse(readFileSync(join(root, "fixtures", "stats-reference.json"), "utf8"));
const tol = reference.tolerances;

function close(actual, expected, absTol, relTol = 0, label = "") {
  assert.ok(Number.isFinite(actual), `${label} not finite: ${actual}`);
  assert.ok(Number.isFinite(expected), `${label} reference not finite: ${expected}`);
  const gap = Math.abs(actual - expected);
  assert.ok(gap <= absTol + relTol * Math.abs(expected), `${label} ${actual} vs ${expected}, gap ${gap}`);
}

test("log-gamma and log-beta match SciPy", () => {
  for (const row of reference.lgamma) close(math.lgamma(row.x), row.value, tol.lgammaAbs, tol.lgammaRel, `lgamma(${row.x})`);
  for (const row of reference.lbeta) close(math.lbeta(row.a, row.b), row.value, tol.lgammaAbs, tol.lgammaRel, `lbeta(${row.a},${row.b})`);
  close(math.lgamma(1), 0, tol.lgammaAbs, 0, "lgamma(1)");
  close(math.lgamma(2), 0, tol.lgammaAbs, 0, "lgamma(2)");
  close(math.lgamma(3), Math.log(2), tol.lgammaAbs, tol.lgammaRel, "lgamma(3)");
  assert.ok(Number.isNaN(math.lgamma(0)));
  assert.ok(Number.isNaN(math.lgamma(-1)));
});

test("beta density, cdf, survival and quantile match SciPy, including shapes below 1 and 500", () => {
  for (const row of reference.betaPdf) {
    const got = math.betaPdf(row.x, row.a, row.b);
    if (row.infinite) {
      assert.equal(got, Infinity, `pdf(${row.x}; ${row.a}, ${row.b})`);
      continue;
    }
    close(got, row.value, tol.betaAbs, tol.betaRel, `pdf(${row.x}; ${row.a}, ${row.b})`);
  }
  for (const row of reference.betaCdf) close(math.betaCdf(row.x, row.a, row.b), row.value, tol.betaAbs, tol.betaRel, `cdf(${row.x}; ${row.a}, ${row.b})`);
  for (const row of reference.betaSf) close(math.betaSurvival(row.x, row.a, row.b), row.value, tol.betaAbs, tol.betaRel, `sf(${row.x}; ${row.a}, ${row.b})`);
  for (const row of reference.betaPpf) {
    const got = math.betaQuantile(row.p, row.a, row.b);
    close(got, row.value, tol.quantileAbs, tol.quantileRel, `ppf(${row.p}; ${row.a}, ${row.b})`);
    const cdf = row.p > 0.5 ? 1 - math.betaSurvival(got, row.a, row.b) : math.betaCdf(got, row.a, row.b);
    close(cdf, row.p, 1e-8, 1e-6, `cdf of ppf(${row.p}; ${row.a}, ${row.b})`);
  }
});

test("normal and t cdf and quantiles match SciPy, including tails to 1e-12", () => {
  for (const row of reference.normalCdf) close(math.normalCdf(row.z), row.value, tol.quantileAbs, tol.quantileRel, `Phi(${row.z})`);
  for (const row of reference.normalPpf) close(math.normalQuantile(row.p), row.value, tol.quantileAbs, tol.quantileRel, `Phi^{-1}(${row.p})`);
  for (const row of reference.tCdf) close(math.tCdf(row.t, row.df), row.value, tol.quantileAbs, tol.quantileRel, `t cdf(${row.t}, ${row.df})`);
  for (const row of reference.tPpf) close(math.tQuantile(row.p, row.df), row.value, tol.quantileAbs, tol.quantileRel, `t ppf(${row.p}, ${row.df})`);
  assert.equal(math.normalCdf(0), 0.5);
  assert.equal(math.normalQuantile(0), -Infinity);
  assert.equal(math.normalQuantile(1), Infinity);
  assert.equal(math.tQuantile(0.5, 5), 0);
});

test("binomial and beta-binomial probabilities match SciPy", () => {
  for (const row of reference.binomPmf) close(math.binomPmf(row.k, row.n, row.p), row.value, tol.pmfAbs, tol.pmfRel, `binom(${row.k}; ${row.n}, ${row.p})`);
  for (const row of reference.betaBinomPmf) {
    close(math.betaBinomPmf(row.k, row.m, row.a, row.b), row.value, tol.pmfAbs, tol.pmfRel, `betabinom(${row.k}; ${row.m}, ${row.a}, ${row.b})`);
  }
  assert.equal(math.binomPmf(-1, 10, 0.3), 0);
  assert.equal(math.binomPmf(11, 10, 0.3), 0);
  assert.equal(math.binomPmf(0, 5, 0), 1);
  assert.equal(math.binomPmf(5, 5, 1), 1);
  assert.ok(Number.isNaN(math.binomPmf(1.5, 5, 0.2)));
  assert.equal(math.betaBinomPmf(3, 2, 1, 1), 0);
});

test("the seeded normal draws match the reference generator", () => {
  const uniform = math.mulberry32(reference.seededNormal.seed);
  const normal = math.normalStream(uniform);
  reference.seededNormal.values.forEach((expected, index) => {
    close(reference.seededNormal.truth + reference.seededNormal.sd * normal(), expected, tol.sampleAbs, 0, `normal draw ${index}`);
  });
  const exp = math.mulberry32(reference.seededExponential.seed);
  reference.seededExponential.values.forEach((expected, index) => {
    close(-reference.seededExponential.truth * Math.log(exp()), expected, tol.sampleAbs, 0, `exponential draw ${index}`);
  });
});

test("a bad argument is not a probability", () => {
  assert.ok(Number.isNaN(math.betaCdf(0.2, 0, 1)));
  assert.ok(Number.isNaN(math.betaQuantile(1.1, 2, 2)));
  assert.ok(Number.isNaN(math.normalQuantile(-0.1)));
  assert.ok(Number.isNaN(math.tCdf(0, 0)));
  assert.ok(Number.isNaN(math.betaBinomPmf(0, 3, -1, 1)));
  assert.equal(math.formatNumber(0), "0");
  assert.equal(math.formatNumber(1 / 3).includes("0.3333"), true);
  assert.equal(math.formatNumber(Number.NaN), "not finite");
});
