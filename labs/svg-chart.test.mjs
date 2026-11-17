import assert from "node:assert/strict";
import test from "node:test";
import { axisScales, measuredChartWidth, plotBox } from "./svg-chart.js";

test("a zero container width does not collapse the viewBox", () => {
  assert.equal(measuredChartWidth(0), 640);
  assert.equal(measuredChartWidth(undefined), 640);
  assert.equal(measuredChartWidth(Number.NaN), 640);
  assert.equal(measuredChartWidth(-20), 640);
  assert.equal(measuredChartWidth(400), 400);
  assert.equal(measuredChartWidth(100.2), 280);
});

test("scales cross the inner frame, with x increasing and y upward", () => {
  const box = plotBox(640, 320);
  const scales = axisScales(box, [-4, 4], [0, 0.44]);
  assert.equal(scales.x(-4), box.left);
  assert.equal(scales.x(4), box.left + box.innerWidth);
  assert.ok(scales.x(4) - scales.x(-4) > 400);
  assert.ok(scales.x(0) > scales.x(-4));
  assert.ok(scales.x(4) > scales.x(0));
  assert.equal(scales.y(0), box.top + box.innerHeight);
  assert.equal(scales.y(0.44), box.top);
  assert.ok(scales.y(0) - scales.y(0.44) > 200);
  assert.ok(scales.y(0.44) < scales.y(0.2));
  assert.ok(scales.y(0.2) < scales.y(0));
  // Margins are not coordinates. The old range [left, right] ran backwards
  // across 38 pixels, and [bottom, top] sat in the top of the frame.
  assert.notEqual(scales.x(4), box.right);
  assert.ok(scales.y(0) > box.bottom);
});
