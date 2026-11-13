// Small SVG charts for the laboratories. No statistics.
// Scales are linear. The picture uses the wiki ink and redraws when the
// theme or the width changes.

import { themeInk, watchTheme } from "./lab-chrome.js";

const SVG = "http://www.w3.org/2000/svg";
let serial = 0;

export function chartColors() {
  const ink = themeInk();
  const dark = ink.dark;
  return {
    ...ink,
    prior: dark ? "#c4b5fd" : "#5b21b6",
    likelihood: dark ? "#e0b15a" : "#9a6b12",
    posterior: dark ? "#9eb6f0" : "#1d4e9e",
    truth: dark ? "#f0b7a4" : "#9a3412",
    plug: dark ? "#7dcea0" : "#1f7a4d",
    miss: dark ? "#f0a0a0" : "#9f1239",
    hit: dark ? "#9eb6f0" : "#1d4e9e",
    states: dark
      ? ["#9eb6f0", "#f0b7a4", "#7dcea0", "#e0b15a", "#f0a0a0", "#c4b5fd"]
      : ["#1d4e9e", "#9a3412", "#1f7a4d", "#9a6b12", "#9f1239", "#5b21b6"],
  };
}

export function createPlot(host, { height = 320, label = "Chart" } = {}) {
  host.replaceChildren();
  const svg = document.createElementNS(SVG, "svg");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-label", label);
  svg.style.display = "block";
  svg.style.width = "100%";
  svg.style.height = "auto";
  host.appendChild(svg);
  let currentLabel = label;
  let draw = () => {};
  let frame = 0;
  const render = () => {
    const width = Math.max(280, Math.round(host.clientWidth || 640));
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.replaceChildren();
    if (currentLabel) {
      const titleEl = document.createElementNS(SVG, "title");
      titleEl.textContent = currentLabel;
      svg.appendChild(titleEl);
    }
    draw({ svg, width, height, colors: chartColors() });
  };
  const observer = new ResizeObserver(() => {
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(render);
  });
  observer.observe(host);
  const stopTheme = watchTheme(() => render());
  render();
  return {
    draw(fn) {
      draw = fn;
      render();
    },
    setLabel(text) {
      currentLabel = text;
      svg.setAttribute("aria-label", text);
      let titleEl = svg.querySelector("title");
      if (text) {
        if (!titleEl) {
          titleEl = document.createElementNS(SVG, "title");
          svg.prepend(titleEl);
        }
        titleEl.textContent = text;
      } else if (titleEl) {
        titleEl.remove();
      }
    },
    destroy() {
      observer.disconnect();
      stopTheme();
      cancelAnimationFrame(frame);
    },
  };
}

export function scaleLinear(domain, range) {
  const [d0, d1] = domain;
  const [r0, r1] = range;
  const span = d1 - d0 || 1;
  return (value) => r0 + ((value - d0) / span) * (r1 - r0);
}

export function niceTicks(min, max, count = 5) {
  if (!(max > min) || !Number.isFinite(min) || !Number.isFinite(max)) return [min];
  const step0 = (max - min) / Math.max(1, count);
  const mag = 10 ** Math.floor(Math.log10(step0));
  const err = step0 / mag;
  const step = (err >= 7.5 ? 10 : err >= 3.5 ? 5 : err >= 1.5 ? 2 : 1) * mag;
  const start = Math.ceil((min - step * 1e-9) / step) * step;
  const ticks = [];
  for (let value = start; value <= max + step * 1e-6 && ticks.length < 12; value += step) {
    ticks.push(Number(value.toPrecision(12)));
  }
  return ticks.length ? ticks : [min, max];
}

export function plotBox(width, height, margin = {}) {
  const box = { top: 14, right: 14, bottom: 38, left: 52, ...margin, width, height };
  box.innerWidth = Math.max(20, width - box.left - box.right);
  box.innerHeight = Math.max(20, height - box.top - box.bottom);
  return box;
}

export function svgEl(parent, name, attrs = {}) {
  const node = document.createElementNS(SVG, name);
  for (const [key, value] of Object.entries(attrs)) {
    if (value === undefined || value === null || value === false) continue;
    node.setAttribute(key, String(value));
  }
  parent.appendChild(node);
  return node;
}

export function rule(parent, x1, y1, x2, y2, style = {}) {
  return svgEl(parent, "line", {
    x1, y1, x2, y2,
    stroke: style.stroke,
    "stroke-width": style.width ?? 1.5,
    "stroke-dasharray": style.dash,
    "vector-effect": "non-scaling-stroke",
  });
}

export function text(parent, x, y, value, style = {}) {
  const node = svgEl(parent, "text", {
    x, y,
    fill: style.fill,
    "font-size": style.size ?? 11,
    "font-family": "sans-serif",
    "text-anchor": style.anchor ?? "middle",
    "dominant-baseline": style.baseline ?? "auto",
  });
  node.textContent = value;
  if (style.rotate) node.setAttribute("transform", `rotate(${style.rotate} ${x} ${y})`);
  return node;
}

export function stroke(parent, points, style = {}) {
  let run = [];
  const flush = () => {
    if (run.length >= 2) {
      svgEl(parent, "polyline", {
        points: run.map((point) => `${point[0].toFixed(2)},${point[1].toFixed(2)}`).join(" "),
        fill: "none",
        stroke: style.stroke,
        "stroke-width": style.width ?? 1.8,
        "stroke-dasharray": style.dash,
        "stroke-linejoin": "round",
        "stroke-linecap": "round",
        "vector-effect": "non-scaling-stroke",
      });
    } else if (run.length === 1) {
      svgEl(parent, "circle", { cx: run[0][0].toFixed(2), cy: run[0][1].toFixed(2), r: style.radius ?? 2.6, fill: style.stroke });
    }
    run = [];
  };
  for (const point of points) {
    if (!point || !Number.isFinite(point[0]) || !Number.isFinite(point[1])) flush();
    else run.push(point);
  }
  flush();
}

export function band(parent, x, y, width, height, fill, opacity = 0.18) {
  if (!(width > 0) || !(height > 0)) return;
  svgEl(parent, "rect", { x, y, width, height, fill, "fill-opacity": opacity });
}

export function drawAxes(svg, box, { xScale, yScale, xTicks, yTicks, colors, xFormat, yFormat }) {
  for (const tick of yTicks) {
    const y = yScale(tick);
    rule(svg, box.left, y, box.left + box.innerWidth, y, { stroke: colors.border, width: 1, dash: "2 3" });
    text(svg, box.left - 6, y, yFormat(tick), { fill: colors.muted, anchor: "end", baseline: "middle" });
  }
  for (const tick of xTicks) {
    text(svg, xScale(tick), box.top + box.innerHeight + 16, xFormat(tick), { fill: colors.muted, anchor: "middle" });
  }
  rule(svg, box.left, box.top, box.left, box.top + box.innerHeight, { stroke: colors.muted, width: 1 });
  rule(svg, box.left, box.top + box.innerHeight, box.left + box.innerWidth, box.top + box.innerHeight, { stroke: colors.muted, width: 1 });
}

export function message(svg, width, height, colors, value) {
  text(svg, width / 2, height / 2, value, { fill: colors.muted, anchor: "middle", baseline: "middle", size: 14 });
}

export function plotClip(svg, box) {
  const id = `clip-${++serial}`;
  const defs = svgEl(svg, "defs");
  const clip = svgEl(defs, "clipPath", { id });
  svgEl(clip, "rect", { x: box.left, y: box.top, width: box.innerWidth, height: box.innerHeight });
  return id;
}
