// Node test for Beta-Binomial updating. Summaries are held to SciPy.

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import * as beta from "./beta-binomial-math.js";
import { mount } from "./beta-binomial.js";
import { betaBinomPmf, betaPdf } from "./stat-math.js";
import { installLabDom, pressKey } from "./test/dom.mjs";

const root = dirname(fileURLToPath(import.meta.url));
const reference = JSON.parse(readFileSync(join(root, "fixtures", "stats-reference.json"), "utf8"));
const { betaAbs, betaRel, quantileAbs, quantileRel } = reference.tolerances;

function close(actual, expected, absTol, relTol, label) {
  assert.ok(Number.isFinite(actual), `${label} not finite: ${actual}`);
  const gap = Math.abs(actual - expected);
  assert.ok(gap <= absTol + relTol * Math.abs(expected), `${label} ${actual} vs ${expected}, gap ${gap}`);
}

test("posterior summaries match SciPy, including the chapter's three priors", () => {
  for (const row of reference.betaLab) {
    const label = `Beta(${row.alpha},${row.beta}) with ${row.x}/${row.n}`;
    const updated = beta.update({ alpha: row.alpha, beta: row.beta, n: row.n, x: row.x, level: row.level });
    assert.equal(updated.error, undefined, label);
    close(updated.posterior.a, row.postA, 0, 0, `${label} a`);
    close(updated.posterior.b, row.postB, 0, 0, `${label} b`);
    close(updated.posterior.mean, row.postMean, 1e-12, 0, `${label} mean`);
    close(updated.posterior.sd, row.postSd, 1e-12, 1e-12, `${label} sd`);
    close(updated.weight, row.weight, 1e-12, 0, `${label} weight`);
    close(updated.blended, row.blended, 1e-12, 0, `${label} blended`);
    close(updated.blended, updated.posterior.mean, 1e-12, 0, `${label} identity`);
    if (row.postMode === null) assert.equal(updated.posterior.mode, null, label);
    else close(updated.posterior.mode, row.postMode, 1e-12, 0, `${label} mode`);
    close(updated.posterior.lower, row.lower, quantileAbs, quantileRel, `${label} lower`);
    close(updated.posterior.upper, row.upper, quantileAbs, quantileRel, `${label} upper`);
    if (row.proportion === null) assert.equal(updated.proportion, null, label);
    else close(updated.proportion, row.proportion, 0, 0, `${label} proportion`);
    const predicted = beta.prediction({ alpha: row.alpha, beta: row.beta, n: row.n, x: row.x }, row.future);
    assert.equal(predicted.error, undefined, label);
    close(predicted.mean, row.predMean, 1e-12, 1e-12, `${label} predictive mean`);
    close(predicted.predictiveVariance, row.predVar, 1e-9, 1e-9, `${label} predictive variance`);
    close(predicted.plugInVariance, row.plugVar, 1e-12, 1e-12, `${label} plug-in variance`);
    const mass = predicted.rows.reduce((sum, item) => sum + item.predictive, 0);
    close(mass, 1, 1e-12, 0, `${label} predictive total`);
  }
});

test("a uniform prior and 3 heads in 10 tosses has posterior mean 1/3", () => {
  const updated = beta.update({ alpha: 1, beta: 1, n: 10, x: 3 });
  assert.equal(updated.posterior.mean, 1 / 3);
  assert.equal(updated.posterior.mode, 0.3);
  const chapter = beta.PRESETS.map((item) => [item.alpha, item.beta]);
  assert.deepEqual(chapter, [[5, 5], [1, 1], [0.6, 0.6]]);
});

test("modes at the boundary and a flat density are named, not invented", () => {
  const cases = [
    [0.6, 0.6, null, "none: the density is unbounded at both ends"],
    [0.6, 1, 0, ""],
    [0.6, 2, 0, ""],
    [1, 0.6, 1, ""],
    [1, 1, null, "every point: the density is flat"],
    [1, 2, 0, ""],
    [2, 0.6, 1, ""],
    [2, 1, 1, ""],
    [2, 2, 0.5, ""],
  ];
  for (const [a, b, mode, modeNote] of cases) {
    const summary = beta.betaSummary(a, b);
    assert.equal(summary.mode, mode, `Beta(${a}, ${b}) mode`);
    assert.equal(summary.modeNote, modeNote, `Beta(${a}, ${b}) mode note`);
    const updated = beta.update({ alpha: a, beta: b, n: 0, x: 0 });
    assert.deepEqual(updated.prior, summary);
    assert.deepEqual(updated.posterior, summary);
  }
  assert.equal(beta.betaSummary(1, 1).mode, null);
  assert.match(beta.betaSummary(1, 1).modeNote, /flat/);
  assert.equal(beta.betaSummary(0.5, 0.5).mode, null);
  assert.match(beta.betaSummary(0.5, 0.5).modeNote, /both ends/);
  assert.equal(beta.betaSummary(0.5, 2).mode, 0);
  assert.equal(beta.betaSummary(2, 0.5).mode, 1);
  assert.equal(beta.betaSummary(3, 3).mode, 0.5);
});

test("one tail preserves the zero boundary mode for a Beta(0.6, 1) prior", () => {
  const updated = beta.update({ alpha: 0.6, beta: 1, n: 1, x: 0 });
  assert.equal(updated.posterior.a, 0.6);
  assert.equal(updated.posterior.b, 2);
  assert.equal(updated.posterior.mode, 0);
  assert.equal(updated.posterior.modeNote, "");
});

test("no tosses leaves the prior as the posterior", () => {
  const updated = beta.update({ alpha: 5, beta: 5, n: 0, x: 0 });
  assert.equal(updated.proportion, null);
  assert.equal(updated.weight, 1);
  assert.equal(updated.posterior.mean, updated.prior.mean);
  assert.equal(updated.posterior.lower, updated.prior.lower);
});

test("the curves are the beta densities, and a bad input is refused", () => {
  const curves = beta.densityCurves({ alpha: 5, beta: 5, n: 10, x: 3 }, 40);
  assert.ok(curves.length > 10);
  assert.ok(curves[0].theta > 0 && curves.at(-1).theta < 1);
  for (const row of curves) {
    close(row.prior, betaPdf(row.theta, 5, 5), betaAbs, betaRel, "prior curve");
    close(row.likelihood, betaPdf(row.theta, 4, 8), betaAbs, betaRel, "likelihood curve");
    close(row.posterior, betaPdf(row.theta, 8, 12), betaAbs, betaRel, "posterior curve");
  }
  assert.match(beta.update({ alpha: 0, beta: 1, n: 10, x: 1 }).error, /α/);
  assert.match(beta.update({ alpha: 1, beta: 1, n: 10, x: 11 }).error, /heads/);
  assert.match(beta.update({ alpha: 1, beta: 1, n: -1, x: 0 }).error, /tosses/);
  assert.match(beta.prediction({ alpha: 1, beta: 1, n: 0, x: 0 }, 0).error, /Future/);
  assert.equal(beta.validate({ alpha: 2, beta: 2, n: 3, x: 1 }), null);
});

test("seeded tosses are prefix-stable and use the true probability", () => {
  const first = beta.tosses(2026, 0.3, 0, 10);
  const second = beta.tosses(2026, 0.3, 0, 25);
  const rest = beta.tosses(2026, 0.3, 10, 15);
  assert.equal(first.heads + rest.heads, second.heads);
  assert.equal(first.heads + first.tails, 10);
  assert.equal(beta.tosses(2026, 0, 0, 20).heads, 0);
  assert.equal(beta.tosses(2026, 1, 0, 8).heads, 8);
  assert.match(beta.tosses(2026, 1.2, 0, 1).error, /true probability/);
  const fair = beta.tosses(7, 1, 0, 1);
  assert.equal(fair.heads, 1);
});

test("one predictive probability matches the beta-binomial mass", () => {
  const predicted = beta.prediction({ alpha: 2, beta: 2, n: 10, x: 8 }, 5);
  assert.equal(predicted.rows[4].predictive, betaBinomPmf(4, 5, 10, 4));
  assert.ok(predicted.predictiveVariance > predicted.plugInVariance);
});

test("Shift-arrows accelerate every Beta-Binomial slider and keep numeric twins in step", (t) => {
  const { root, cleanup } = installLabDom(t);
  cleanup(mount(root));

  const hint = root.querySelector(".control-hint");
  assert.ok(hint?.id);
  assert.match(hint.textContent, /Arrow keys move a focused slider\. Shift changes α and β by 1, n, x and m by 10, and the true probability by 0\.1\./);

  const labels = ["Prior heads α", "Prior tails β", "Tosses n", "Heads x", "True probability", "Future tosses m"];
  for (const label of labels) {
    const slider = root.querySelector(`input[aria-label="${label}"]`);
    assert.equal(slider.getAttribute("aria-describedby"), hint.id, label);
  }

  const alphaSlider = root.querySelector('input[aria-label="Prior heads α"]');
  const alphaNumber = root.querySelector('input[aria-label="Prior heads α as a number"]');
  assert.equal(pressKey(alphaSlider, "ArrowRight", { shiftKey: true }).defaultPrevented, true);
  assert.equal(alphaSlider.value, "6");
  assert.equal(alphaNumber.value, "6");
  for (let i = 0; i < 10; i += 1) pressKey(alphaSlider, "ArrowLeft", { shiftKey: true });
  assert.equal(alphaSlider.value, "0.1");
  assert.equal(alphaNumber.value, "0.1");

  const nSlider = root.querySelector('input[aria-label="Tosses n"]');
  const nNumber = root.querySelector('input[aria-label="Tosses n as a number"]');
  const xSlider = root.querySelector('input[aria-label="Heads x"]');
  const xNumber = root.querySelector('input[aria-label="Heads x as a number"]');
  pressKey(nSlider, "ArrowRight", { shiftKey: true });
  assert.equal(nSlider.value, "20");
  assert.equal(nNumber.value, "20");
  pressKey(xSlider, "ArrowRight", { shiftKey: true });
  assert.equal(xSlider.value, "13");
  assert.equal(xNumber.value, "13");
  // Stepping n down clamps x to the new toss count.
  pressKey(nSlider, "ArrowLeft", { shiftKey: true });
  assert.equal(nSlider.value, "10");
  assert.equal(xSlider.value, "10");
  assert.equal(xNumber.value, "10");

  const truthSlider = root.querySelector('input[aria-label="True probability"]');
  const truthNumber = root.querySelector('input[aria-label="True probability as a number"]');
  pressKey(truthSlider, "ArrowLeft", { shiftKey: true });
  assert.equal(truthSlider.value, "0.2");
  assert.equal(truthNumber.value, "0.2");

  const futureSlider = root.querySelector('input[aria-label="Future tosses m"]');
  const futureNumber = root.querySelector('input[aria-label="Future tosses m as a number"]');
  pressKey(futureSlider, "ArrowUp", { shiftKey: true });
  assert.equal(futureSlider.value, "15");
  assert.equal(futureNumber.value, "15");
  pressKey(futureSlider, "ArrowDown", { shiftKey: true });
  pressKey(futureSlider, "ArrowDown", { shiftKey: true });
  assert.equal(futureSlider.value, "1");
  assert.equal(futureNumber.value, "1");
});
