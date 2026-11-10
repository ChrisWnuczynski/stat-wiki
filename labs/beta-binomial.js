// Beta–Binomial laboratory. Draws its own SVG. The calculations are in
// beta-binomial-math.js.

import { DEFAULTS, LIMITS, PRESETS, densityCurves, prediction, tosses, update, validate } from "./beta-binomial-math.js";
import { controlRow, graphFrame, installLabChrome, markerLegend, readoutLine } from "./lab-chrome.js";
import { formatNumber } from "./stat-math.js";
import { band, chartColors, createPlot, drawAxes, message, niceTicks, plotBox, plotClip, rule, scaleLinear, stroke, svgEl } from "./svg-chart.js";

function field(labelText, wide = false) {
  const label = document.createElement("label");
  label.className = wide ? "control-field control-field-wide" : "control-field";
  const span = document.createElement("span");
  span.textContent = labelText;
  label.appendChild(span);
  return label;
}

function sliderPair(labelText, { min, max, step, value, wide = false }) {
  const label = field(labelText, wide);
  const wrap = document.createElement("span");
  wrap.className = "control-slider";
  const slider = document.createElement("input");
  slider.type = "range";
  slider.min = String(min);
  slider.max = String(max);
  slider.step = String(step);
  slider.value = String(value);
  slider.setAttribute("aria-label", labelText);
  const number = document.createElement("input");
  number.type = "number";
  number.min = String(min);
  number.max = String(max);
  number.step = String(step);
  number.value = String(value);
  number.setAttribute("aria-label", `${labelText} as a number`);
  wrap.append(slider, number);
  label.appendChild(wrap);
  const show = (next) => {
    slider.value = String(next);
    number.value = String(next);
  };
  return { label, slider, number, show };
}

function button(text) {
  const node = document.createElement("button");
  node.type = "button";
  node.textContent = text;
  return node;
}

function readNumber(input) {
  if (input.value.trim() === "") return Number.NaN;
  return Number(input.value);
}

export function mount(root) {
  installLabChrome();
  root.replaceChildren();
  const form = controlRow("Beta–Binomial controls");
  const alpha = sliderPair("Prior heads α", { min: LIMITS.shapeMin, max: LIMITS.shapeMax, step: 0.1, value: DEFAULTS.alpha, wide: true });
  const beta = sliderPair("Prior tails β", { min: LIMITS.shapeMin, max: LIMITS.shapeMax, step: 0.1, value: DEFAULTS.beta, wide: true });
  const n = sliderPair("Tosses n", { min: 0, max: LIMITS.nMax, step: 1, value: DEFAULTS.n });
  const x = sliderPair("Heads x", { min: 0, max: DEFAULTS.n, step: 1, value: DEFAULTS.x });
  const truth = sliderPair("True probability", { min: 0, max: 1, step: 0.01, value: DEFAULTS.truth, wide: true });
  const future = sliderPair("Future tosses m", { min: 1, max: LIMITS.futureMax, step: 1, value: DEFAULTS.future });
  const seedLabel = field("Toss seed", false);
  seedLabel.classList.add("control-field-fixed");
  const seed = document.createElement("input");
  seed.type = "number";
  seed.step = "1";
  seed.value = String(DEFAULTS.seed);
  seed.setAttribute("aria-label", "Toss seed");
  seedLabel.appendChild(seed);
  const presets = document.createElement("div");
  presets.className = "control-actions";
  presets.setAttribute("role", "group");
  presets.setAttribute("aria-label", "Prior presets");
  const presetButtons = PRESETS.map((preset) => {
    const node = button(preset.label);
    node.title = preset.detail;
    node.setAttribute("aria-pressed", preset.alpha === DEFAULTS.alpha && preset.beta === DEFAULTS.beta ? "true" : "false");
    presets.appendChild(node);
    return node;
  });
  const actions = document.createElement("div");
  actions.className = "control-actions";
  const head = button("+ head");
  const tail = button("+ tail");
  const toss = button("Toss 10");
  const restore = button("Reset");
  actions.append(head, tail, toss, restore);
  const hint = document.createElement("p");
  hint.className = "control-hint";
  hint.textContent = "Toss i of this seed is the same draw however the tosses are batched. + head and + tail are edits, not draws. The generator is not R's.";
  const note = document.createElement("p");
  note.className = "control-note";
  note.setAttribute("role", "status");
  form.append(presets, alpha.label, beta.label, n.label, x.label, truth.label, future.label, seedLabel, actions, hint, note);

  const readout = document.createElement("div");
  const density = graphFrame("Prior, scaled likelihood and posterior");
  const densityNote = document.createElement("p");
  densityNote.className = "graph-note";
  const forecast = graphFrame("Heads in future tosses");
  const forecastNote = document.createElement("p");
  forecastNote.className = "graph-note";
  root.append(form, readout, density.section, forecast.section);
  density.section.append(densityNote);
  forecast.section.append(forecastNote);
  const plotA = createPlot(density.plot, { height: 340, label: "Prior, likelihood and posterior" });
  const plotB = createPlot(forecast.plot, { height: 280, label: "Predictive distribution of future heads" });

  function markPresets(a, b) {
    PRESETS.forEach((preset, index) => {
      presetButtons[index].setAttribute("aria-pressed", preset.alpha === a && preset.beta === b ? "true" : "false");
    });
  }

  function render() {
    const a = readNumber(alpha.number);
    const b = readNumber(beta.number);
    let tossesN = readNumber(n.number);
    let heads = readNumber(x.number);
    const m = readNumber(future.number);
    const theta = readNumber(truth.number);
    const seedValue = readNumber(seed);
    if (Number.isInteger(tossesN)) {
      x.slider.max = String(Math.max(0, tossesN));
      x.number.max = String(Math.max(0, tossesN));
      if (Number.isInteger(heads) && heads > tossesN) {
        heads = tossesN;
        x.show(heads);
      }
    }
    markPresets(a, b);
    const problem = validate({ alpha: a, beta: b, n: tossesN, x: heads })
      || (!(m >= 1) || !Number.isInteger(m) || m > LIMITS.futureMax ? `Future tosses must be a whole number from 1 to ${LIMITS.futureMax}.` : null)
      || (!(theta >= 0 && theta <= 1) ? "The true probability must be from 0 to 1." : null)
      || (!Number.isInteger(seedValue) ? "The toss seed must be a whole number." : null);
    if (problem) {
      note.textContent = problem;
      readout.replaceChildren();
      densityNote.textContent = "";
      forecastNote.textContent = "";
      const say = (label) => ({ svg, width, height, colors }) => {
        message(svg, width, height, colors, "Not drawn.");
        plotA.setLabel(label);
      };
      plotA.draw((ctx) => {
        message(ctx.svg, ctx.width, ctx.height, ctx.colors, "Not drawn.");
      });
      plotA.setLabel(problem);
      plotB.draw((ctx) => message(ctx.svg, ctx.width, ctx.height, ctx.colors, "Not drawn."));
      plotB.setLabel(problem);
      return;
    }
    note.textContent = "";
    const updated = update({ alpha: a, beta: b, n: tossesN, x: heads });
    const predicted = prediction({ alpha: a, beta: b, n: tossesN, x: heads }, m);
    const post = updated.posterior;
    const entries = [
      { label: "Posterior", value: `Beta(${formatNumber(post.a)}, ${formatNumber(post.b)})` },
      {
        label: "Mean",
        value: tossesN === 0
          ? formatNumber(post.mean)
          : `${formatNumber(post.mean)} = ${formatNumber(updated.weight)}×${formatNumber(updated.prior.mean)} + ${formatNumber(1 - updated.weight)}×${formatNumber(updated.proportion)}`,
      },
      { label: "SD", value: formatNumber(post.sd) },
      { label: "Mode", value: post.mode === null ? post.modeNote : formatNumber(post.mode) },
      { label: "95% interval", value: `(${formatNumber(post.lower)}, ${formatNumber(post.upper)})` },
    ];
    readout.replaceChildren(readoutLine(entries));
    const curves = densityCurves({ alpha: a, beta: b, n: tossesN, x: heads });
    const interior = curves.filter((row) => row.theta > 0.02 && row.theta < 0.98);
    const finite = interior.flatMap((row) => [row.prior, row.likelihood, row.posterior]).filter((value) => Number.isFinite(value));
    const yMax = Math.max(1, ...finite) * 1.15;
    const clipped = curves.some((row) => [row.prior, row.likelihood, row.posterior].some((value) => !Number.isFinite(value) || value > yMax));
    const notes = [];
    if (tossesN === 0) notes.push("No tosses yet, so the posterior is the prior and there is no sample proportion.");
    if (clipped) notes.push("A density is unbounded or too tall for the axis, so the curve is clipped.");
    densityNote.textContent = notes.join(" ");
    plotA.setLabel(`Posterior Beta(${formatNumber(post.a)}, ${formatNumber(post.b)}), mean ${formatNumber(post.mean)}`);
    plotA.draw(({ svg, width, height, colors }) => {
      const box = plotBox(width, height);
      const xScale = scaleLinear([0, 1], [box.left, box.left + box.innerWidth]);
      const yScale = scaleLinear([0, yMax], [box.top + box.innerHeight, box.top]);
      const left = xScale(post.lower);
      const right = xScale(post.upper);
      band(svg, left, box.top, Math.max(0, right - left), box.innerHeight, colors.posterior, 0.16);
      drawAxes(svg, box, {
        xScale, yScale,
        xTicks: [0, 0.25, 0.5, 0.75, 1],
        yTicks: niceTicks(0, yMax, 4),
        colors,
        xFormat: (value) => formatNumber(value),
        yFormat: (value) => formatNumber(value),
      });
      const clip = plotClip(svg, box);
      const layer = svgEl(svg, "g", { "clip-path": `url(#${clip})` });
      const place = (key) => curves.map((row) => [xScale(row.theta), yScale(Math.min(row[key], yMax))]);
      stroke(layer, place("prior"), { stroke: colors.prior, width: 1.8, dash: "6 4" });
      stroke(layer, place("likelihood"), { stroke: colors.likelihood, width: 1.8 });
      stroke(layer, place("posterior"), { stroke: colors.posterior, width: 2.4 });
      if (tossesN > 0) rule(layer, xScale(heads / tossesN), box.top, xScale(heads / tossesN), box.top + box.innerHeight, { stroke: colors.text, width: 1.2, dash: "3 3" });
      rule(layer, xScale(theta), box.top, xScale(theta), box.top + box.innerHeight, { stroke: colors.truth, width: 1.6 });
    });
    const ink = chartColors();
    const legend = markerLegend([
      { text: "Prior", color: ink.prior, kind: "line", dash: "dashed" },
      { text: "Scaled likelihood", color: ink.likelihood, kind: "line" },
      { text: "Posterior", color: ink.posterior, kind: "line" },
      { text: "95% interval", color: ink.posterior, kind: "tick" },
      { text: tossesN > 0 ? "Heads / tosses" : "Heads / tosses (none yet)", color: ink.text, kind: "line", dash: "dotted" },
      { text: "True probability", color: ink.truth, kind: "line" },
    ]);
    const old = density.section.querySelector(".legend-row");
    if (old) old.remove();
    density.section.appendChild(legend);

    const peak = Math.max(...predicted.rows.flatMap((row) => [row.predictive, row.plugIn]), 0.01);
    forecastNote.textContent = `Predictive mean ${formatNumber(predicted.mean)}. Predictive variance ${formatNumber(predicted.predictiveVariance)}; plug-in variance ${formatNumber(predicted.plugInVariance)}.`;
    plotB.setLabel(`Predictive distribution for ${m} future tosses`);
    plotB.draw(({ svg, width, height, colors }) => {
      const box = plotBox(width, height, { bottom: 36 });
      const yMaxBar = peak * 1.15;
      const xScale = scaleLinear([-0.5, m + 0.5], [box.left, box.left + box.innerWidth]);
      const yScale = scaleLinear([0, yMaxBar], [box.top + box.innerHeight, box.top]);
      drawAxes(svg, box, {
        xScale, yScale,
        xTicks: niceTicks(0, m, Math.min(m, 8)).filter((tick) => Number.isInteger(tick)),
        yTicks: niceTicks(0, yMaxBar, 4),
        colors,
        xFormat: (value) => String(value),
        yFormat: (value) => formatNumber(value),
      });
      const gap = Math.max(1, (xScale(1) - xScale(0)) * 0.34);
      for (const row of predicted.rows) {
        const base = yScale(0);
        const predHeight = base - yScale(row.predictive);
        const plugHeight = base - yScale(row.plugIn);
        svgEl(svg, "rect", { x: xScale(row.k) - gap, y: yScale(row.predictive), width: gap * 0.9, height: Math.max(0, predHeight), fill: colors.posterior });
        svgEl(svg, "rect", { x: xScale(row.k) + gap * 0.05, y: yScale(row.plugIn), width: gap * 0.9, height: Math.max(0, plugHeight), fill: colors.plug });
      }
    });
    const bars = markerLegend([
      { text: "Posterior predictive", color: ink.posterior, kind: "tick" },
      { text: "Plug-in binomial", color: ink.plug, kind: "tick" },
    ]);
    const oldBars = forecast.section.querySelector(".legend-row");
    if (oldBars) oldBars.remove();
    forecast.section.appendChild(bars);
  }

  for (const pair of [alpha, beta, n, x, truth, future]) {
    pair.slider.addEventListener("input", () => {
      pair.number.value = pair.slider.value;
      render();
    });
    pair.number.addEventListener("input", () => {
      if (pair.number.value.trim() !== "" && Number.isFinite(Number(pair.number.value))) pair.slider.value = pair.number.value;
      render();
    });
  }
  seed.addEventListener("input", render);
  presetButtons.forEach((node, index) => {
    node.addEventListener("click", () => {
      alpha.show(PRESETS[index].alpha);
      beta.show(PRESETS[index].beta);
      render();
    });
  });
  head.addEventListener("click", () => shift(1, 1));
  tail.addEventListener("click", () => shift(1, 0));
  function shift(dn, dx) {
    const tossesN = readNumber(n.number);
    const heads = readNumber(x.number);
    if (!Number.isInteger(tossesN) || !Number.isInteger(heads)) {
      render();
      return;
    }
    if (tossesN >= LIMITS.nMax) {
      note.textContent = `The page stops at ${LIMITS.nMax} tosses.`;
      return;
    }
    n.show(tossesN + dn);
    x.show(heads + dx);
    render();
  }
  toss.addEventListener("click", () => {
    const tossesN = readNumber(n.number);
    const heads = readNumber(x.number);
    const theta = readNumber(truth.number);
    const seedValue = readNumber(seed);
    if (!Number.isInteger(tossesN) || !Number.isInteger(heads) || !Number.isInteger(seedValue)) {
      render();
      return;
    }
    const count = Math.min(10, LIMITS.nMax - tossesN);
    if (count < 1) {
      note.textContent = `The page stops at ${LIMITS.nMax} tosses.`;
      return;
    }
    const drawn = tosses(seedValue, theta, tossesN, count);
    if (drawn.error) {
      note.textContent = drawn.error;
      return;
    }
    n.show(tossesN + count);
    x.show(heads + drawn.heads);
    render();
  });
  restore.addEventListener("click", () => {
    alpha.show(DEFAULTS.alpha);
    beta.show(DEFAULTS.beta);
    n.show(DEFAULTS.n);
    x.show(DEFAULTS.x);
    truth.show(DEFAULTS.truth);
    future.show(DEFAULTS.future);
    seed.value = String(DEFAULTS.seed);
    render();
  });
  render();
  return () => {
    plotA.destroy();
    plotB.destroy();
  };
}
