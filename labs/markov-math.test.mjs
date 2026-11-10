// Node test for the Markov-chain laboratory. Stationary vectors are held
// to a NumPy null-space calculation from labs/reference_stats.py.

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import * as markov from "./markov-math.js";
import { mulberry32 } from "./stat-math.js";

const root = dirname(fileURLToPath(import.meta.url));
const reference = JSON.parse(readFileSync(join(root, "fixtures", "stats-reference.json"), "utf8"));
const { stationaryAbs } = reference.tolerances;

function close(actual, expected, absTol, label) {
  assert.ok(Number.isFinite(actual), `${label} not finite: ${actual}`);
  const gap = Math.abs(actual - expected);
  assert.ok(gap <= absTol, `${label} ${actual} vs ${expected}, gap ${gap}`);
}

function closeVector(actual, expected, label) {
  assert.equal(actual.length, expected.length, label);
  actual.forEach((value, index) => close(value, expected[index], stationaryAbs, `${label}[${index}]`));
  close(actual.reduce((sum, value) => sum + value, 0), 1, 1e-12, `${label} total`);
}

function byName(name) {
  return reference.markov.find((row) => row.name === name);
}

test("preset matrices are the reference chains, and the exercise chain is absent", () => {
  for (const row of reference.markov) {
    if (row.name === "absorbing") continue;
    const preset = markov.PRESETS.find((item) => item.id === row.name);
    assert.ok(preset, row.name);
    preset.matrix.forEach((line, i) => line.forEach((value, j) => close(value, row.matrix[i][j], 0, `${row.name} P[${i}][${j}]`)));
    assert.equal(markov.validateMatrix(preset.matrix), null, row.name);
  }
  const exercise = [
    [0.5, 0.5, 0],
    [0.25, 0.5, 0.25],
    [0, 0.5, 0.5],
  ];
  assert.equal(markov.PRESETS.some((item) => JSON.stringify(item.matrix) === JSON.stringify(exercise)), false);
});

test("classes, periods and stationary distributions match the null-space reference", () => {
  for (const row of reference.markov) {
    const chain = markov.analyse(row.matrix);
    assert.equal(chain.error, undefined, row.name);
    const closed = chain.classes.filter((item) => item.closed).map((item) => item.states);
    assert.deepEqual(closed, row.closedClasses, row.name);
    assert.equal(chain.unique, row.nullity === 1, row.name);
    assert.equal(chain.distributions.length, row.extremal.length, row.name);
    row.extremal.forEach((vector, index) => closeVector(chain.distributions[index].pi, vector, `${row.name} extremal ${index}`));
    if (row.exactPi) closeVector(chain.distributions[0].pi, row.exactPi, `${row.name} exact`);
  }
});

test("the stepping stones and the weather chain match the known powers", () => {
  const checks = reference.markovChecks;
  const stepping = markov.PRESETS.find((item) => item.id === "stepping").matrix;
  const two = markov.distributionPath(0, stepping, 2);
  two.distributions[2].forEach((value, index) => close(value, checks.steppingP2Row0[index], 1e-12, `P2[${index}]`));
  const ten = markov.distributionPath(0, stepping, 10);
  close(ten.distributions[10][0], checks.steppingP10State0, 1e-12, "P10 stone 1");
  assert.deepEqual(
    checks.steppingRounded3dp,
    [0.101, 0.034, 0.168, 0.21, 0.185, 0.303],
  );
  const weather = markov.PRESETS.find((item) => item.id === "weather").matrix;
  const fromWet = markov.distributionPath(1, weather, 2);
  fromWet.distributions[2].forEach((value, index) => close(value, checks.weatherP2FromWet[index], 1e-12, `weather[${index}]`));
  const chain = markov.analyse(weather);
  close(chain.distributions[0].pi[0], 2 / 3, 1e-12, "weather dry");
  close(chain.distributions[0].pi[1], 1 / 3, 1e-12, "weather wet");
  const start = [1, 0];
  let dist = start;
  for (let t = 0; t < 5; t++) {
    const next = [dist[0] * 0.8 + dist[1] * 0.4, dist[0] * 0.2 + dist[1] * 0.6];
    const gap = markov.tv(dist, chain.distributions[0].pi);
    dist = next;
    close(markov.tv(dist, chain.distributions[0].pi), gap * checks.weatherRate, 1e-12, `rate step ${t}`);
  }
});

test("the two-cycle oscillates while its occupation settles, and the sticky chain is slow", () => {
  const cycle = markov.PRESETS.find((item) => item.id === "cycle");
  const chain = markov.analyse(cycle.matrix);
  assert.equal(chain.classes[0].period, 2);
  assert.equal(chain.unique, true);
  assert.equal(chain.settles, false);
  const path = markov.distributionPath(0, cycle.matrix, 6);
  for (let t = 0; t <= 6; t++) {
    close(path.distributions[t][t % 2], 1, 1e-12, `cycle mass ${t}`);
    close(markov.tv(path.distributions[t], chain.distributions[0].pi), 0.5, 1e-12, `cycle tv ${t}`);
  }
  const simulated = markov.simulate(1, 0, cycle.matrix, 8);
  assert.deepEqual(simulated.path, [0, 1, 0, 1, 0, 1, 0, 1, 0]);
  const fractions = markov.occupation(simulated.path, 2);
  close(fractions.at(-1)[0], 5 / 9, 1e-12, "cycle occupation");

  const sticky = markov.PRESETS.find((item) => item.id === "sticky");
  const stickyChain = markov.analyse(sticky.matrix);
  stickyChain.distributions[0].pi.forEach((value) => close(value, 1 / 3, 1e-12, "sticky pi"));
  assert.equal(stickyChain.classes[0].period, 1);
  assert.equal(stickyChain.settles, true);
  const early = markov.distributionPath(0, sticky.matrix, 20).distributions[20];
  assert.ok(early[0] > 0.5, `sticky still remembers the start: ${early[0]}`);
});

test("a reducible chain has one stationary vector per closed class, and absorption mixes them", () => {
  const reducible = markov.PRESETS.find((item) => item.id === "reducible");
  const chain = markov.analyse(reducible.matrix);
  assert.equal(chain.unique, false);
  assert.equal(chain.settles, true);
  assert.equal(chain.classes.find((item) => item.states[0] === 0).period, 0);
  const limit = markov.limitingFrom(reducible.matrix, 0, chain);
  closeVector(limit, [0, 1 / 3, 1 / 6, 0.5], "reducible mixture");
  const inside = markov.limitingFrom(reducible.matrix, 3, chain);
  closeVector(inside, chain.distributions[1].pi, "start inside C");

  const absorbing = byName("absorbing");
  const absorbed = markov.analyse(absorbing.matrix);
  const fromStart = markov.limitingFrom(absorbing.matrix, 0, absorbed);
  closeVector(fromStart, [0, 0, 0.5, 0.5], "two-step absorption");
  const evolved = markov.distributionPath(0, absorbing.matrix, 8).distributions[8];
  closeVector(evolved, fromStart, "absorption by step 8");
});

test("simulation follows the rows, and a longer path keeps the shorter one", () => {
  const weather = markov.PRESETS.find((item) => item.id === "weather").matrix;
  const draws = mulberry32(2026);
  let state = 0;
  const expected = [0];
  for (let step = 0; step < 12; step++) {
    const u = draws();
    state = u < weather[state][0] ? 0 : 1;
    expected.push(state);
  }
  const short = markov.simulate(2026, 0, weather, 12);
  const long = markov.simulate(2026, 0, weather, 40);
  assert.deepEqual(short.path, expected);
  assert.deepEqual(long.path.slice(0, 13), short.path);
  const fractions = markov.occupation(short.path, 2);
  fractions.forEach((row) => close(row[0] + row[1], 1, 1e-12, "occupation"));
  const chain = markov.analyse(weather);
  const distributions = markov.distributionPath(0, weather, 30).distributions;
  assert.ok(markov.tv(distributions[30], chain.distributions[0].pi) < markov.tv(distributions[1], chain.distributions[0].pi));
});

test("a matrix that is not stochastic is refused and can be rescaled", () => {
  assert.match(markov.validateMatrix([[1]]), /2 to 6/);
  assert.match(markov.validateMatrix([[1, 0], [0, 0]]), /sums to 0/);
  assert.match(markov.validateMatrix([[1, 0], [-0.2, 1.2]]), /negative/);
  assert.match(markov.validateMatrix([[1, Number.NaN], [0, 1]]), /not a finite/);
  assert.match(markov.distributionPath(0, [[0.2, 0.2], [0.4, 0.6]], 3).error, /sums/);
  const scaled = markov.normaliseRows([
    [1, 1, 0],
    [0, 0, 0],
    [1, 1, 1],
  ]);
  assert.match(scaled.error, /sums to 0/);
  const ok = markov.normaliseRows([
    [2, 2],
    [1, 3],
  ]);
  assert.equal(ok.error, undefined);
  close(ok.matrix[0][0], 0.5, 0, "rescaled");
  close(ok.matrix[1][1], 0.75, 0, "rescaled");
  assert.equal(markov.validateMatrix(ok.matrix), null);
  assert.match(markov.simulate(0, 5, markov.PRESETS[1].matrix, 1).error, /starting state/);
  assert.match(markov.distributionPath(0, markov.PRESETS[1].matrix, -1).error, /steps/);
});
