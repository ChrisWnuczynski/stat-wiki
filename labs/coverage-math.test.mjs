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
