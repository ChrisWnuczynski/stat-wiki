// Distribution laboratory. One family, parameter sliders, mass or density, and the distribution function.

import { controlRow, graphFrame, installLabChrome, readoutLine } from "./lab-chrome.js";
import { curve, FAMILIES, familyById } from "./distribution-explorer-math.js";
import { formatNumber } from "./stat-math.js";
import { axisScales, createPlot, drawAxes, message, niceTicks, plotBox, plotClip, stroke, svgEl } from "./svg-chart.js";

function field(labelText) {
  const label = document.createElement("label");
  label.className = "control-field";
  const span = document.createElement("span");
  span.textContent = labelText;
  label.appendChild(span);
  return label;
}

let nextInputId = 0;
let nextHintId = 0;

function shiftStepValue(slider, dir, multiple = 10) {
  const min = Number(slider.min);
  const max = Number(slider.max);
  const step = Number(slider.step) || 1;
  const current = Math.min(max, Math.max(min, Number(slider.value)));
  const maxIndex = Math.max(0, Math.round((max - min) / step));
  const index = Math.max(0, Math.min(maxIndex, Math.round((current - min) / step) + dir * multiple));
  const text = String(slider.step || "1");
  const dot = text.indexOf(".");
  const decimals = dot < 0 ? 0 : text.length - dot - 1;
  return Number(Math.min(max, Math.max(min, min + index * step)).toFixed(decimals));
}

function sliderPair(spec, onInput, hintId) {
  const label = field(spec.label);
  const wrap = document.createElement("span");
  wrap.className = "control-slider";
  const slider = document.createElement("input");
  slider.type = "range";
  slider.min = String(spec.min);
  slider.max = String(spec.max);
  slider.step = String(spec.step);
  slider.value = String(spec.value);
  slider.setAttribute("aria-label", spec.label);
  if (hintId) slider.setAttribute("aria-describedby", hintId);
  const candidate = slider.cloneNode();
  const number = document.createElement("input");
  number.type = "number";
  number.min = String(spec.min);
  number.max = String(spec.max);
  number.step = String(spec.step);
  number.required = true;
  number.value = String(spec.value);
  number.setAttribute("aria-label", `${spec.label} as a number`);
  const feedback = document.createElement("span");
  feedback.id = `distribution-input-${++nextInputId}`;
  feedback.className = "control-note";
  const status = document.createElement("span");
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  status.setAttribute("aria-atomic", "true");
  status.style.display = "block";
  status.appendChild(feedback);
  number.setAttribute("aria-describedby", feedback.id);
  const sync = (input) => {
    const value = input.valueAsNumber;
    // Number validity tolerates values near a step; the range still rounds them.
    candidate.value = input.value;
    if (!Number.isFinite(value) || !input.validity.valid || candidate.valueAsNumber !== value) {
      number.setAttribute("aria-invalid", "true");
      feedback.textContent = `${spec.label} must be a number from ${spec.min} to ${spec.max} in steps of ${spec.step}. Showing ${spec.value}.`;
      return;
    }
    number.removeAttribute("aria-invalid");
    feedback.textContent = "";
    slider.value = String(value);
    // Keep the text being edited, including a decimal point before its digits.
    if (input === slider) number.value = String(value);
    spec.value = value;
    onInput();
  };
  slider.addEventListener("input", () => sync(slider));
  slider.addEventListener("keydown", (event) => {
    if (!event.shiftKey || event.altKey || event.ctrlKey || event.metaKey) return;
    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight" && event.key !== "ArrowUp" && event.key !== "ArrowDown") return;
    event.preventDefault();
    const dir = event.key === "ArrowLeft" || event.key === "ArrowDown" ? -1 : 1;
    slider.value = String(shiftStepValue(slider, dir));
    sync(slider);
  });
  number.addEventListener("input", () => sync(number));
  wrap.append(slider, number);
  // Keep the empty live region exposed without adding a row to the label's flex layout.
  const controls = document.createElement("span");
  controls.append(wrap, status);
  label.appendChild(controls);
  return label;
}

function clipY(y, yMax) {
  if (y === Infinity) return yMax;
  if (!Number.isFinite(y)) return NaN;
  return Math.min(Math.max(y, 0), yMax);
}

// kind is "curve", "stems", or "step". Pixel positions use the inner frame,
// so a later change cannot treat the margins as the scale range.
export function panelGeometry({ xs, ys, width, height, yMax, kind }) {
  if (!xs || !xs.length || !(yMax > 0) || !(width > 0) || !(height > 0)) return null;
  const x0 = xs[0];
  const x1 = xs[xs.length - 1];
  if (!Number.isFinite(x0) || !Number.isFinite(x1)) return null;
  const box = plotBox(width, height);
  const scales = axisScales(box, [x0, x1], [0, yMax]);
  const yAt = (y) => {
    const clipped = clipY(y, yMax);
    return Number.isFinite(clipped) ? scales.y(clipped) : NaN;
  };
  let marks;
  if (kind === "stems") {
    const stems = [];
    for (let i = 0; i < xs.length; i += 1) {
      const y = yAt(ys[i]);
      if (!Number.isFinite(y)) continue;
      stems.push({ x: scales.x(xs[i]), y0: scales.y(0), y1: y });
    }
    marks = { kind: "stems", stems };
  } else if (kind === "step") {
    const points = [[scales.x(x0), scales.y(0)]];
    for (let i = 0; i < xs.length; i += 1) {
      const x = scales.x(xs[i]);
      const y = yAt(ys[i]);
      points.push([x, y]);
      if (i + 1 < xs.length) points.push([scales.x(xs[i + 1]), y]);
    }
    marks = { kind: "step", points };
  } else {
    marks = { kind: "curve", points: xs.map((x, i) => [scales.x(x), yAt(ys[i])]) };
  }
  return {
    box,
    scales,
    xTicks: niceTicks(x0, x1, 5),
    yTicks: niceTicks(0, yMax, 4),
    marks,
  };
}

function drawPanel(plot, series, label, yMax, kind) {
  plot.setLabel(label);
  plot.draw(({ svg, width, height, colors }) => {
    const geometry = panelGeometry({
      xs: series.xs,
      ys: series.ys,
      width,
      height,
      yMax,
      kind,
    });
    if (!geometry) {
      message(svg, width, height, colors, "Not drawn");
      return;
    }
    const { box, scales, marks } = geometry;
    drawAxes(svg, box, {
      xScale: scales.x,
      yScale: scales.y,
      xTicks: geometry.xTicks,
      yTicks: geometry.yTicks,
      colors,
      xFormat: (value) => formatNumber(value),
      yFormat: (value) => formatNumber(value),
    });
    const clip = plotClip(svg, box);
    const layer = svgEl(svg, "g", { "clip-path": `url(#${clip})` });
    if (marks.kind === "stems") {
      for (const stem of marks.stems) {
        svgEl(layer, "line", {
          x1: stem.x,
          x2: stem.x,
          y1: stem.y0,
          y2: stem.y1,
          stroke: colors.posterior,
          "stroke-width": 2,
          "vector-effect": "non-scaling-stroke",
        });
        svgEl(layer, "circle", { cx: stem.x, cy: stem.y1, r: 2.6, fill: colors.posterior });
      }
      return;
    }
    stroke(layer, marks.points, { stroke: colors.posterior, width: 2 });
  });
}

export function mount(root) {
  installLabChrome();
  const state = { id: "normal" };
  const form = controlRow("Distribution controls");
  const readout = document.createElement("div");
  const density = graphFrame("Probability mass or density");
  const cdf = graphFrame("Distribution function");
  root.append(form, readout, density.section, cdf.section);
  const densityPlot = createPlot(density.plot, { label: "Probability mass or density" });
  const cdfPlot = createPlot(cdf.plot, { label: "Distribution function" });

  const redraw = () => {
    const family = familyById(state.id);
    const values = {};
    for (const spec of family.params) values[spec.key] = spec.value;
    const drawn = curve(family, values);
    const finite = drawn.density.filter((y) => Number.isFinite(y) && y < 1e6);
    const yMax = Math.max(0.05, ...finite) * 1.1;
    const densityKind = family.discrete ? "stems" : "curve";
    const cdfKind = family.discrete ? "step" : "curve";
    drawPanel(densityPlot, { xs: drawn.xs, ys: drawn.density }, `${family.name} ${family.discrete ? "probability mass" : "density"}`, yMax, densityKind);
    drawPanel(cdfPlot, { xs: drawn.xs, ys: drawn.cdf }, `${family.name} distribution function`, 1, cdfKind);
    const bits = family.params.map((spec) => ({
      label: spec.label,
      value: formatNumber(spec.value),
    }));
    readout.replaceChildren(readoutLine([{ label: family.name, value: bits.map((bit) => `${bit.label} ${bit.value}`).join(", ") }]));
  };

  const selectLabel = field("Family");
  const select = document.createElement("select");
  select.setAttribute("aria-label", "Distribution family");
  for (const family of FAMILIES) {
    const option = document.createElement("option");
    option.value = family.id;
    option.textContent = family.name;
    select.appendChild(option);
  }
  select.value = state.id;
  selectLabel.appendChild(select);
  form.appendChild(selectLabel);

  const hint = document.createElement("p");
  hint.id = `distribution-control-hint-${++nextHintId}`;
  hint.className = "control-hint";
  let parameterControls = [];
  const renderParameters = () => {
    // Keep the native selector attached and focused throughout keyboard changes.
    for (const control of parameterControls) control.remove();
    const family = familyById(state.id);
    const changes = family.params.map((spec) => `${spec.label} by ${Number((spec.step * 10).toPrecision(12))}`);
    hint.textContent = `Arrow keys move a focused slider. Shift changes ${changes.join(" and ")}.`;
    parameterControls = family.params.map((spec) => sliderPair(spec, redraw, hint.id));
    form.append(...parameterControls, hint);
    redraw();
  };
  select.addEventListener("change", () => {
    state.id = select.value;
    renderParameters();
  });
  renderParameters();
  return () => {
    densityPlot.destroy();
    cdfPlot.destroy();
  };
}
