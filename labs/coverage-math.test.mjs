// Node test for confidence-interval coverage. Formulas are held to SciPy.

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import * as cover from "./coverage-math.js";

const root = dirname(fileURLToPath(import.meta.url));
const reference = JSON.parse(readFileSync(join(root, "fixtures", "stats-reference.json"), "utf8"));
const { coverageAbs, intervalAbs, sampleAbs } = reference.tolerances;

function close(actual, expected, absTol, relTol, label) {
  assert.ok(Number.isFinite(actual), `${label} not finite: ${actual}`);
  const gap = Math.abs(actual - expected);
  assert.ok(gap <= absTol + relTol * Math.abs(expected), `${label} ${actual} vs ${expected}, gap ${gap}`);
}

const normal = { population: "normal", method: "t", n: 10, level: 0.95, seed: 2026, p: 0.3 };

test("z with s and the exact binomial coverage match SciPy", () => {
  for (const row of reference.zWithS) {
    close(cover.exactMeanCoverage(row.n, row.level, "z-with-s"), row.value, coverageAbs, 1e-10, `z-with-s n=${row.n} ${row.level}`);
    assert.equal(cover.exactMeanCoverage(row.n, row.level, "t"), row.level);
    if (row.n < 100) assert.ok(row.value < row.level, `n=${row.n} should undercover`);
  }
  for (const row of reference.proportionCoverage) {
    close(
      cover.exactProportionCoverage(row.n, row.p, row.level, row.method),
      row.value,
      coverageAbs,
      1e-9,
      `${row.method} n=${row.n} p=${row.p}`,
    );
  }
});

test("interval endpoints on hand samples match SciPy", () => {
  for (const row of reference.intervals) {
    const got = row.kind === "mean"
      ? cover.meanInterval(row.values, row.method, row.level)
      : cover.proportionInterval(row.x, row.n, row.method, row.level);
    assert.equal(got.error, undefined, JSON.stringify(row));
    close(got.lower, row.lower, intervalAbs, 1e-9, "lower");
    close(got.upper, row.upper, intervalAbs, 1e-9, "upper");
    close(got.estimate, row.estimate, intervalAbs, 1e-12, "estimate");
    if (row.values && row.values.every((value) => value === row.values[0])) assert.equal(got.degenerate, true);
  }
});

test("the seeded normal sample produces SciPy's t and z-with-s intervals", () => {
  const drawn = cover.draw(reference.seededNormal.seed, { ...normal, method: "t" }, 1);
  assert.equal(drawn.error, undefined);
  drawn.intervals[0].estimate; // the first sample is the reference sample
  const again = cover.draw(reference.seededNormal.seed, { ...normal, n: 10, method: "z-with-s" }, 1);
  close(drawn.intervals[0].estimate, reference.seededNormal.t.estimate, sampleAbs, 0, "mean");
  close(drawn.intervals[0].lower, reference.seededNormal.t.lower, intervalAbs, 1e-9, "t lower");
  close(drawn.intervals[0].upper, reference.seededNormal.t.upper, intervalAbs, 1e-9, "t upper");
  close(again.intervals[0].lower, reference.seededNormal.zWithS.lower, intervalAbs, 1e-9, "z lower");
  close(again.intervals[0].estimate, drawn.intervals[0].estimate, 0, 0, "same sample");
  assert.equal(drawn.truth, 10);
  assert.equal(drawn.intervals[0].covers, cover.hitsTruth(drawn.intervals[0].lower, drawn.intervals[0].upper, 10));
});

test("asking for more intervals keeps the earlier ones", () => {
  const first = cover.draw(2026, normal, 5);
  const more = cover.draw(2026, { ...normal, method: "z-with-s" }, 12);
  const wald = cover.draw(2026, { population: "bernoulli", method: "wald", n: 15, level: 0.9, seed: 2026, p: 0.2 }, 8);
  const waldMore = cover.draw(2026, { population: "bernoulli", method: "wilson", n: 15, level: 0.99, seed: 2026, p: 0.2 }, 11);
  assert.equal(first.intervals.length, 5);
  first.intervals.forEach((row, index) => {
    close(row.estimate, more.intervals[index].estimate, 0, 0, `mean ${index}`);
  });
  assert.ok(first.intervals.some((row, index) => row.lower !== more.intervals[index].lower));
  wald.intervals.forEach((row, index) => {
    assert.equal(row.successes, waldMore.intervals[index].successes, `count ${index}`);
  });
  const none = cover.draw(2026, normal, 0);
  assert.equal(none.intervals.length, 0);
  assert.equal(none.fraction, null);
  assert.equal(none.hits, 0);
});

test("Wald collapses at 0 and 1, Wilson does not, and the sawtooth is real", () => {
  const zero = cover.proportionInterval(0, 10, "wald", 0.95);
  assert.equal(zero.lower, 0);
  assert.equal(zero.upper, 0);
  assert.equal(zero.degenerate, true);
  const wilson = cover.proportionInterval(0, 10, "wilson", 0.95);
  assert.equal(wilson.lower, 0);
  assert.ok(wilson.upper > 0.2 && wilson.upper < 0.4);
  assert.equal(cover.exactProportionCoverage(10, 0, 0.95, "wald"), 1);
  assert.equal(cover.exactProportionCoverage(10, 0, 0.95, "wilson"), 1);
  const waldMid = cover.exactProportionCoverage(10, 0.5, 0.95, "wald");
  const waldEdge = cover.exactProportionCoverage(10, 0.05, 0.95, "wald");
  const wilsonEdge = cover.exactProportionCoverage(10, 0.05, 0.95, "wilson");
  assert.ok(waldEdge < waldMid);
  assert.ok(wilsonEdge > waldEdge);
  const n2 = cover.exactMeanCoverage(2, 0.95, "z-with-s");
  assert.ok(n2 < 0.8 && n2 > 0.6, `n=2 coverage ${n2}`);
});

function plottedCoverage(curve, p) {
  const exact = curve.points.find((point) => point.p === p);
  if (exact) return exact.coverage;
  const segment = curve.segments.find((points) => points[0].p < p && p < points.at(-1).p);
  assert.ok(segment, `a continuous piece contains ${p}`);
  const right = segment.findIndex((point) => point.p >= p);
  const a = segment[right - 1];
  const b = segment[right];
  return a.coverage + (b.coverage - a.coverage) * (p - a.p) / (b.p - a.p);
}

test("Wald n=1 keeps both boundary values without the old 20% and 50% ramps", () => {
  const curve = cover.proportionCoverageCurve(1, 0.95, "wald");
  assert.equal(curve.segments.length, 3);
  for (const p of [0, 1]) assert.equal(plottedCoverage(curve, p), 1);
  for (const p of [0.00625, 0.01, 0.99, 0.99375]) assert.equal(plottedCoverage(curve, p), 0);
  assert.equal(curve.segments[1][0].p, 1e-10);
  assert.equal(curve.segments[1].at(-1).p, 1 - 1e-10);
  assert.ok(curve.segments[1].every((point) => point.coverage === 0));
  for (const p of [5e-11, 1e-10, 1.01e-10, 1 - 5e-11, 1 - 1e-10, 1 - 1.01e-10]) {
    close(plottedCoverage(curve, p), cover.exactProportionCoverage(1, p, 0.95, "wald"), 1e-15, 0, `tolerance strip ${p}`);
  }
});

test("Wald n=10 preserves the jump, its inclusive tolerance, and the near-edge coverage", () => {
  const curve = cover.proportionCoverageCurve(10, 0.95, "wald");
  const b = cover.proportionInterval(1, 10, "wald", 0.95).upper;
  close(b, 0.28593850969136847, 1e-15, 0, "one-success upper bound");
  for (const [p, expected] of [
    [0.01, 0.09550407587328956], [0.99, 0.09550407587328962],
    [b - 1e-8, 0.9277485648178875], [b, 0.9277485633827881],
    [b + 1e-10, 0.927748563368437], [b + 1.01e-10, 0.7897440923292279],
    [b + 1e-8, 0.7897441033493425],
  ]) {
    close(cover.exactProportionCoverage(10, p, 0.95, "wald"), expected, 1e-13, 0, `oracle ${p}`);
    close(plottedCoverage(curve, p), expected, 2e-5, 0, `piecewise line ${p}`);
  }
  assert.equal(cover.hitsTruth(0, b, b + 1e-10), true);
  assert.equal(cover.hitsTruth(0, b, b + 1.01e-10), false);
  const cut = b + 1e-10;
  const index = curve.points.findIndex((point) => point.p === cut);
  assert.ok(index > 0);
  close(curve.points[index].coverage, 0.927748563368437, 1e-13, 0, "exact jump point");
  close(curve.segments[index - 1].at(-1).coverage, curve.points[index].coverage, 1e-14, 0, "left limit");
  close(curve.segments[index][0].coverage, 0.7897440923281148, 1e-13, 0, "right limit");
  assert.ok(curve.segments.every((points) => !(points[0].p < cut && points.at(-1).p > cut)));
});

test("an internal tolerance strip retains its own accepted counts", () => {
  // At z = sqrt(3/8), the one- and two-success Wald endpoints meet at 1/2.
  const level = 0.4597086253925803;
  const curve = cover.proportionCoverageCurve(3, level, "wald");
  const strip = curve.segments.find((points) => points[0].p < 0.5 && points.at(-1).p > 0.5);
  assert.ok(strip.at(-1).p - strip[0].p < 3e-10);
  for (const p of [0.5 - 5e-11, 0.5, 0.5 + 5e-11]) {
    close(plottedCoverage(curve, p), 0.75, 1e-14, 0, "inside the strip");
    close(plottedCoverage(curve, p), cover.exactProportionCoverage(3, p, level, "wald"), 1e-14, 0, "oracle inside the strip");
  }
  for (const p of [0.5 - 2e-10, 0.5 + 2e-10]) {
    close(plottedCoverage(curve, p), 0.375, 1e-9, 0, "outside the strip");
  }
});

test("Wilson and maximum-n curves have bounded finite paths with fixed membership", () => {
  for (const n of [1, 10, 200]) for (const level of [0.8, 0.9, 0.95, 0.99]) for (const method of ["wald", "wilson"]) {
    const curve = cover.proportionCoverageCurve(n, level, method);
    assert.equal(curve.error, undefined);
    assert.ok(curve.points.length <= 2 * (n + 1) + 2);
    assert.equal(curve.segments.length, curve.points.length - 1);
    assert.ok(curve.segments.reduce((sum, points) => sum + points.length, 0) <= 1024 + 2 * curve.segments.length);
    for (const point of curve.points) {
      assert.equal(point.coverage, cover.exactProportionCoverage(n, point.p, level, method));
    }
    const intervals = Array.from({ length: n + 1 }, (_, k) => cover.proportionInterval(k, n, method, level));
    curve.segments.forEach((points, i) => {
      assert.equal(points[0].p, curve.points[i].p);
      assert.equal(points.at(-1).p, curve.points[i + 1].p);
      for (const point of points) {
        assert.ok(Number.isFinite(point.p) && Number.isFinite(point.coverage));
        assert.ok(point.coverage >= 0 && point.coverage <= 1 + 1e-12);
      }
      const lower = points[0].p;
      const upper = points.at(-1).p;
      const membership = (p) => intervals.map((row) => cover.hitsTruth(row.lower, row.upper, p));
      assert.deepEqual(membership(lower + (upper - lower) / 4), membership(lower + 3 * (upper - lower) / 4));
      // Interior samples must be exact, including inside the tiny edge strips.
      for (const point of points.slice(1, -1)) {
        close(point.coverage, cover.exactProportionCoverage(n, point.p, level, method), 1e-12, 0, `${method} n=${n}`);
      }
    });
  }
  for (const args of [[0, 0.95, "wald"], [201, 0.95, "wald"], [10, 1, "wald"], [10, 0.95, "t"]]) {
    assert.ok(cover.proportionCoverageCurve(...args).error);
  }
});

test("the running fraction's band is a labelled normal approximation", () => {
  const drawn = cover.draw(11, normal, 20);
  const running = cover.runningFraction(drawn.intervals);
  assert.equal(running.at(-1).fraction, drawn.fraction);
  assert.equal(running[0].fraction, drawn.intervals[0].covers ? 1 : 0);
  const band = cover.fractionBand(20, 0.95);
  assert.equal(band.normalApproximation, true);
  close(band.se, Math.sqrt(0.95 * 0.05 / 20), 1e-12, 0, "band se");
  assert.ok(band.lower < 0.95 && band.upper > 0.95);
  assert.match(cover.fractionBand(0, 0.95).error, /at least one/);
});

test("exponential coverage is a fixed-seed Monte Carlo, and a normal run sits near 95%", () => {
  const once = cover.exponentialMonteCarlo({ n: 10, level: 0.95, method: "t" });
  const twice = cover.exponentialMonteCarlo({ n: 10, level: 0.95, method: "t" });
  assert.equal(once.monteCarlo, true);
  assert.equal(once.reps, cover.LIMITS.mcReps);
  assert.equal(once.seed, cover.LIMITS.mcSeed);
  assert.equal(once.hits, twice.hits);
  close(once.se, Math.sqrt(once.coverage * (1 - once.coverage) / once.reps), 1e-12, 0, "mc se");
  assert.ok(once.coverage > 0.85 && once.coverage < 0.99, `exponential t coverage ${once.coverage}`);
  const z = cover.exponentialMonteCarlo({ n: 10, level: 0.95, method: "z-with-s" });
  assert.ok(z.coverage < once.coverage, "z with s should cover less often than t on the same design");
  const probe = cover.draw(99, { ...normal, n: 8, seed: 99 }, 400);
  const exact = cover.exactMeanCoverage(8, 0.95, "t");
  assert.ok(Math.abs(probe.fraction - exact) < 0.05, `realised ${probe.fraction}`);
});

test("a sample of size 1, a bad level, and a mismatched method are refused", () => {
  assert.match(cover.draw(1, { ...normal, n: 1 }, 5).error, /n − 1/);
  assert.match(cover.draw(1, { ...normal, method: "wald" }, 5).error, /does not belong/);
  assert.match(cover.draw(1, { ...normal, level: 0 }, 5).error, /level/);
  assert.match(cover.draw(1.5, normal, 5).error, /seed/);
  assert.match(cover.draw(1, { population: "bernoulli", method: "wald", n: 10, level: 0.95, seed: 1, p: 1.4 }, 2).error, /probability/);
  assert.match(cover.meanInterval([1], "t", 0.95).error, /two observations/);
  assert.match(cover.proportionInterval(3, 2, "wald", 0.95).error, /yeses/);
  assert.equal(cover.draw(1, { population: "bernoulli", method: "wald", n: 1, level: 0.95, seed: 1, p: 0 }, 3).error, undefined);
});
