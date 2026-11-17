import assert from "node:assert/strict";
import test from "node:test";
import { curve, familyById } from "./distribution-explorer-math.js";

test("bernoulli masses sum to one", () => {
  const family = familyById("bernoulli");
  const drawn = curve(family, { p: 0.3 });
  assert.equal(drawn.density[0], 0.7);
  assert.equal(drawn.density[1], 0.3);
  assert.ok(Math.abs(drawn.density.reduce((s, y) => s + y, 0) - 1) < 1e-12);
});

test("normal density at the mean", () => {
  const family = familyById("normal");
  const atMean = family.pmf(0, { mu: 0, sigma: 1 });
  assert.ok(Math.abs(atMean - 1 / Math.sqrt(2 * Math.PI)) < 1e-12);
  assert.ok(Math.abs(family.cdf(0, { mu: 0, sigma: 1 }) - 0.5) < 1e-12);
});

test("exponential distribution function at the mean", () => {
  const family = familyById("exponential");
  const atMean = family.cdf(1, { lambda: 1 });
  assert.ok(Math.abs(atMean - (1 - Math.exp(-1))) < 1e-12);
});

test("poisson mean mass", () => {
  const family = familyById("poisson");
  const p0 = family.pmf(0, { lambda: 2 });
  assert.ok(Math.abs(p0 - Math.exp(-2)) < 1e-12);
  const drawn = curve(family, { lambda: 2 });
  const total = drawn.density.reduce((s, y) => s + y, 0);
  assert.ok(total > 0.99 && total <= 1);
});
