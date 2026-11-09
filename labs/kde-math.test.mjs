// Node test for the kernel density module. No R, no Python, no browser.
// Reference numbers were computed by labs/reference_kde.py from the exact
// draws in labs/fixtures/samples.json, and checked against R there.
//
// Tolerances, also stored in fixtures/reference.json:
//   bandwidthAbs 1e-9     |JS bw.nrd0 - R stats::bw.nrd0|
//   riskAbs 1e-8 and riskRel 1e-8
//                         |JS - reference| <= riskAbs + riskRel * |reference|
//                         for ISE, MISE, integrated variance, integrated squared bias
//   decompositionAbs 1e-9 |IVar + IBias^2 - MISE|
//   kdeAbs 1e-12          hand-evaluated Gaussian kernel sum
//   quadratureAbs 1e-4    phi and a kernel estimate integrate to about 1
//                         (this is not how ISE or MISE are computed)
//   prefix and uniforms   exact
//   repeated normals      1e-12, the same seed through Box-Muller
//
// A sample of size 0 cannot be an estimate. Size 1 has a kernel estimate,
// an ISE, and a MISE, and does not have an R bw.nrd0 bandwidth.

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import * as kde from "./kde-math.js";

const root = dirname(fileURLToPath(import.meta.url));
const reference = JSON.parse(readFileSync(join(root, "fixtures", "reference.json"), "utf8"));
const samples = JSON.parse(readFileSync(join(root, "fixtures", "samples.json"), "utf8"));
const { bandwidthAbs, riskAbs, riskRel, decompositionAbs, kdeAbs, quadratureAbs } = reference.tolerances;

function close(actual, expected, absTol, relTol = 0) {
  assert.ok(Number.isFinite(actual), `not finite: ${actual}`);
  const gap = Math.abs(actual - expected);
  assert.ok(gap <= absTol + relTol * Math.abs(expected), `${actual} vs ${expected}, gap ${gap}`);
}

function phi(x) {
  return Math.exp(-0.5 * x * x) / Math.sqrt(2 * Math.PI);
}

test("hand kernel sum matches the normal density and the published four decimals", () => {
  const got = kde.kdeAt(0, reference.handSample, reference.handH);
  assert.equal(got.error, undefined);
  const expected = (phi(1) + phi(0) + phi(2)) / 3;
  close(got.value, expected, kdeAbs);
  close(got.value, reference.handKde, kdeAbs);
  assert.equal(Number(got.value.toFixed(4)), reference.publishedHandKde4dp);
});

test("a standard normal density and a three-point kernel estimate integrate to one", () => {
  const xs = [];
  const step = 0.01;
  for (let x = -12; x <= 12; x += step) xs.push(x);
  let phiArea = 0;
  let kdeArea = 0;
  const sample = reference.handSample;
  for (let i = 1; i < xs.length; i++) {
    const width = xs[i] - xs[i - 1];
    phiArea += 0.5 * (phi(xs[i]) + phi(xs[i - 1])) * width;
    const left = sample.reduce((sum, xi) => sum + phi((xs[i - 1] - xi) / 1), 0) / sample.length;
    const right = sample.reduce((sum, xi) => sum + phi((xs[i] - xi) / 1), 0) / sample.length;
    kdeArea += 0.5 * (left + right) * width;
  }
  close(phiArea, 1, quadratureAbs);
  close(kdeArea, 1, quadratureAbs);
});

test("exact ISE, MISE, and the variance-bias split match the R and Python reference", () => {
  for (const row of reference.cases) {
    const ise = kde.iseExact(row.values, row.h, row.components);
    assert.equal(ise.error, undefined, row.name);
    close(ise.value, row.ise, riskAbs, riskRel);
    const risk = kde.miseParts(row.n, row.h, row.components);
    assert.equal(risk.error, undefined, row.name);
    close(risk.integratedVariance, row.integratedVariance, riskAbs, riskRel);
    close(risk.integratedSquaredBias, row.integratedSquaredBias, riskAbs, riskRel);
    close(risk.mise, row.mise, riskAbs, riskRel);
    close(risk.integratedVariance + risk.integratedSquaredBias, risk.mise, decompositionAbs, 0);
    if (row.n >= 2) {
      const bw = kde.silvermanNrd0(row.values);
      assert.equal(bw.error, undefined, row.name);
      assert.ok(bw.value > 0 && Number.isFinite(bw.value));
      close(bw.value, row.bw, bandwidthAbs);
    }
  }
});

test("the matched normal observation has ISE zero and a positive MISE", () => {
  const row = reference.cases.find((item) => item.name === "point-mass-match");
  const ise = kde.iseExact(row.values, row.h, row.components);
  close(ise.value, 0, 1e-12);
  const risk = kde.miseParts(1, 1, row.components);
  assert.ok(risk.mise > 0);
  assert.ok(risk.integratedSquaredBias >= -1e-12);
});

test("MISE ignores the sample and ISE does not", () => {
  const mixture = kde.population("mixture").components;
  const seq = kde.sequence(3500);
  const first = kde.samplePrefix(seq, "mixture", 40).values;
  const second = kde.samplePrefix(kde.sequence(99), "mixture", 40).values;
  const h = 0.5;
  const left = kde.miseParts(40, h, mixture);
  const right = kde.miseParts(40, h, mixture);
  assert.equal(left.mise, right.mise);
  assert.equal(left.integratedVariance, right.integratedVariance);
  assert.equal(left.integratedSquaredBias, right.integratedSquaredBias);
  const iseA = kde.iseExact(first, h, mixture).value;
  const iseB = kde.iseExact(second, h, mixture).value;
  assert.notEqual(iseA, iseB);
});

test("bw.nrd0 matches R, including ties, small n, zero IQR, and the fallback", () => {
  for (const row of reference.bandwidthCases) {
    const got = kde.silvermanNrd0(row.values);
    if (row.error) {
      assert.equal(typeof got.error, "string", row.name);
      assert.equal(got.value, undefined, row.name);
      continue;
    }
    assert.equal(got.error, undefined, `${row.name}: ${got.error}`);
    assert.ok(Number.isFinite(got.value) && got.value > 0, row.name);
    close(got.value, row.bw, bandwidthAbs);
  }
  assert.equal(kde.silvermanNrd0([]).error, kde.ERRORS.bandwidthTooSmall);
  assert.equal(kde.silvermanNrd0([3]).error, kde.ERRORS.bandwidthTooSmall);
  assert.equal(kde.silvermanNrd0([1, Number.NaN]).error.includes("non-finite"), true);
  assert.equal(kde.silvermanNrd0([1, Number.POSITIVE_INFINITY]).value, undefined);
});

test("failed calculations do not invent a number", () => {
  assert.equal(kde.kdeAt(0, [], 1).error, kde.ERRORS.kdeTooSmall);
  assert.equal(kde.iseExact([], 1, kde.population("normal").components).error, kde.ERRORS.iseTooSmall);
  assert.equal(kde.miseParts(0, 1, kde.population("normal").components).error, kde.ERRORS.miseTooSmall);
  assert.equal(kde.miseParts(1.5, 1, kde.population("normal").components).error, kde.ERRORS.miseTooSmall);
  assert.equal(kde.kdeAt(0, [0, 1], 0).error, kde.ERRORS.bandwidthNotPositive);
  assert.equal(kde.kdeAt(0, [0, 1], -0.2).value, undefined);
  assert.equal(kde.iseExact([0, 1], Number.NaN, kde.population("normal").components).value, undefined);
  assert.equal(kde.miseParts(10, Number.POSITIVE_INFINITY, kde.population("normal").components).value, undefined);
  const badWeights = [{ weight: 0.2, mean: 0, sd: 1 }];
  assert.equal(kde.iseExact([0, 1], 0.4, badWeights).value, undefined);
  assert.match(kde.miseParts(5, 0.4, badWeights).error, /sum to 1/);
  assert.equal(kde.iseExact([0, 1], 0.4, [{ weight: 1, mean: 0, sd: 0 }]).value, undefined);
  assert.equal(kde.kdeAt(0, [0, Number.NaN], 0.3).value, undefined);
});

test("tiny and large bandwidths stay finite, and a flat sample does not collapse the rule", () => {
  const spread = [-1.2, -0.4, 0.2, 0.7, 1.5];
  for (const h of [1e-6, 1e-3, 0.05, 10, 100]) {
    const ise = kde.iseExact(spread, h, kde.population("mixture").components);
    const risk = kde.miseParts(spread.length, h, kde.population("mixture").components);
    assert.equal(ise.error, undefined, String(h));
    assert.equal(risk.error, undefined, String(h));
    assert.ok(Number.isFinite(ise.value) && Number.isFinite(risk.mise));
  }
  const flat = kde.silvermanNrd0([0, 0, 0, 0]);
  assert.ok(flat.value > 0);
  const near = kde.silvermanNrd0([1, 1, 1 + 1e-8]);
  assert.ok(near.value > 0 && Number.isFinite(near.value));
  const duplicates = kde.iseExact([1, 1, 1, 1], 0.3, kde.population("normal").components);
  assert.ok(Number.isFinite(duplicates.value));
});

test("the same seed is stable, and n is a prefix of one sequence", () => {
  assert.deepEqual(kde.uniformStream(3500, 6), samples.uniforms3500);
  const once = kde.sequence(3500);
  const twice = kde.sequence(3500);
  assert.equal(once.length, kde.MAX_N);
  for (let i = 0; i < once.length; i++) {
    close(once[i].z, twice[i].z, 1e-12, 1e-12);
    assert.equal(once[i].u, twice[i].u);
  }
  const byName = Object.fromEntries(samples.samples.map((item) => [item.name, item]));
  const mixture120 = kde.samplePrefix(once, "mixture", 120).values;
  const mixture40 = kde.samplePrefix(once, "mixture", 40).values;
  assert.deepEqual(mixture40, mixture120.slice(0, 40));
  for (let i = 0; i < mixture120.length; i++) close(mixture120[i], byName["mixture-n120"].values[i], 1e-12, 1e-12);
  for (let i = 0; i < mixture40.length; i++) close(mixture40[i], byName["mixture-n40"].values[i], 1e-12, 1e-12);
  const normal80 = kde.samplePrefix(once, "normal", 80).values;
  for (let i = 0; i < normal80.length; i++) close(normal80[i], byName["normal-n80"].values[i], 1e-12, 1e-12);
  const seq7 = kde.sequence(7);
  const extra = kde.realise(seq7, byName["extra-mixture-n25"].components, 25).values;
  for (let i = 0; i < extra.length; i++) close(extra[i], byName["extra-mixture-n25"].values[i], 1e-12, 1e-12);
  const normal15 = kde.samplePrefix(seq7, "normal", 15).values;
  for (let i = 0; i < normal15.length; i++) close(normal15[i], byName["normal-n15"].values[i], 1e-12, 1e-12);
});

test("changing the population reuses the underlying draws, and h is not an input", () => {
  const seq = kde.sequence(11);
  const normal = kde.samplePrefix(seq, "normal", 30).values;
  const mixture = kde.samplePrefix(seq, "mixture", 30).values;
  assert.equal(normal.length, 30);
  assert.ok(normal.some((value, i) => value !== mixture[i]));
  assert.equal(kde.samplePrefix.length, 3);
});

test("integrated variance falls and integrated squared bias rises across a wide gap in h", () => {
  const components = kde.population("mixture").components;
  const narrow = kde.miseParts(80, 0.08, components);
  const wide = kde.miseParts(80, 1.6, components);
  assert.ok(wide.integratedSquaredBias > narrow.integratedSquaredBias);
  assert.ok(wide.integratedVariance < narrow.integratedVariance);
  assert.ok(narrow.integratedVariance > 0);
  assert.ok(wide.integratedSquaredBias > 0);
});

test("the cached pairwise ISE matches the direct sum, and one curve at n=200 stays cheap", () => {
  const components = kde.population("mixture").components;
  const values = kde.samplePrefix(kde.sequence(3500), "mixture", 200).values;
  const cache = kde.pairCache(values);
  for (const h of [0.15, 0.6, 1.4]) {
    close(kde.iseFromCache(cache, h, components).value, kde.iseExact(values, h, components).value, 1e-12, 1e-12);
  }
  const grid = kde.bandwidthGrid(kde.BAND_LO, kde.BAND_HI, kde.CURVE_COUNT);
  const started = performance.now();
  const curve = kde.iseCurve(cache, grid, components);
  const elapsed = performance.now() - started;
  assert.equal(curve.error, undefined);
  assert.equal(curve.values.length, kde.CURVE_COUNT);
  assert.ok(curve.values.every(Number.isFinite));
  // Measured around 15 ms for 41 bandwidths at n=200. A worker is not warranted.
  // The limit is loose so a busy CI runner still passes.
  assert.ok(elapsed < 250, `ISE curve took ${elapsed} ms`);
});

test("grid minima pick the smallest closed-form value and refuse non-finite input", () => {
  const best = kde.gridMin([0.2, 0.4, 0.6], [0.5, 0.1, 0.2]);
  assert.equal(best.x, 0.4);
  assert.equal(kde.gridMin([0.2], [Number.NaN]).value, undefined);
  const components = kde.population("normal").components;
  const minMise = kde.minimiseRisk(
    (h) => {
      const row = kde.miseParts(50, h, components);
      return row.error ? row : { value: row.mise };
    },
    kde.BAND_LO,
    kde.BAND_HI,
    21,
    kde.MISE_STEP,
  );
  assert.equal(minMise.error, undefined);
  assert.ok(minMise.x > kde.BAND_LO && minMise.x < kde.BAND_HI);
  assert.ok(minMise.y <= kde.miseParts(50, 0.2, components).mise);
  assert.ok(minMise.y <= kde.miseParts(50, 1.5, components).mise);
});
