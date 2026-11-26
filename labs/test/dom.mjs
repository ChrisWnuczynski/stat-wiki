// Dependency-free DOM stand-in for Node tests of the laboratory UI modules.

class TextNode {
  constructor(text) {
    this.nodeType = 3;
    this.textContent = String(text);
    this.parentElement = null;
  }

  remove() {
    if (!this.parentElement) return;
    const list = this.parentElement.children;
    const index = list.indexOf(this);
    if (index >= 0) list.splice(index, 1);
    this.parentElement = null;
  }
}

function matchSingleSelector(element, selector) {
  let rest = selector.trim();
  if (!rest || !(element instanceof LabElement)) return false;
  const attrs = [];
  rest = rest.replace(/\[([^=\]]+)(?:="([^"]*)")?\]/g, (_, name, value) => {
    attrs.push([name, value]);
    return "";
  });
  let id = null;
  rest = rest.replace(/#([A-Za-z0-9_-]+)/, (_, found) => {
    id = found;
    return "";
  });
  const parts = rest.split(".");
  const tag = parts[0];
  const classes = parts.slice(1).filter(Boolean);
  if (tag && element.tagName !== tag.toUpperCase()) return false;
  if (id !== null && element.id !== id) return false;
  for (const cls of classes) {
    if (!element.classList.contains(cls)) return false;
  }
  for (const [name, value] of attrs) {
    if (value === undefined) {
      if (!element.hasAttribute(name)) return false;
    } else if (element.getAttribute(name) !== value) {
      return false;
    }
  }
  return true;
}

class LabElement {
  constructor(tagName, namespaceURI = null) {
    this.nodeType = 1;
    this.tagName = String(tagName).toUpperCase();
    this.namespaceURI = namespaceURI;
    this.children = [];
    this.parentElement = null;
    this.attributes = new Map();
    this.listeners = new Map();
    this.dataset = {};
    this.style = {};
    this.clientWidth = 640;
    this.title = "";
    this.required = false;
    this.disabled = false;
    this._type = "";
    this._min = "";
    this._max = "";
    this._step = "";
    this._value = "";
    this._hasValue = false;
    const self = this;
    this.classList = {
      add(...names) {
        const set = new Set(self.className.split(/\s+/).filter(Boolean));
        for (const name of names) set.add(name);
        self.className = [...set].join(" ");
      },
      remove(...names) {
        const set = new Set(self.className.split(/\s+/).filter(Boolean));
        for (const name of names) set.delete(name);
        self.className = [...set].join(" ");
      },
      contains(name) {
        return self.className.split(/\s+/).filter(Boolean).includes(name);
      },
      toggle(name, force) {
        const present = this.contains(name);
        const shouldAdd = force === undefined ? !present : Boolean(force);
        if (shouldAdd) this.add(name);
        else this.remove(name);
        return shouldAdd;
      },
    };
  }

  get id() {
    return this.attributes.get("id") ?? "";
  }

  set id(value) {
    this.setAttribute("id", String(value));
  }

  get className() {
    return this.attributes.get("class") ?? "";
  }

  set className(value) {
    this.setAttribute("class", String(value));
  }

  get type() {
    return this._type;
  }

  set type(value) {
    this._type = String(value);
    this.setAttribute("type", this._type);
  }

  get min() {
    return this._min;
  }

  set min(value) {
    this._min = String(value);
    this.setAttribute("min", this._min);
    if (this._type === "range" && this._hasValue) this._value = this._sanitizeRange(this._value);
  }

  get max() {
    return this._max;
  }

  set max(value) {
    this._max = String(value);
    this.setAttribute("max", this._max);
    if (this._type === "range" && this._hasValue) this._value = this._sanitizeRange(this._value);
  }

  get step() {
    return this._step;
  }

  set step(value) {
    this._step = String(value);
    this.setAttribute("step", this._step);
    if (this._type === "range" && this._hasValue) this._value = this._sanitizeRange(this._value);
  }

  _sanitizeRange(raw) {
    const min = this._min === "" ? 0 : Number(this._min);
    const max = this._max === "" ? 100 : Number(this._max);
    const fallback = min + (max - min) / 2;
    const num = raw === "" ? fallback : Number(raw);
    if (!Number.isFinite(num)) return String(fallback);
    const clamped = Math.min(max, Math.max(min, num));
    if (this._step === "" || this._step === "any") return String(clamped);
    const step = Number(this._step);
    if (!(step > 0)) return String(clamped);
    const steps = Math.round((clamped - min) / step);
    let snapped = min + steps * step;
    if (snapped > max + 1e-12) snapped -= step;
    const text = String(this._step);
    const dot = text.indexOf(".");
    const decimals = dot < 0 ? 0 : text.length - dot - 1;
    return String(Number(Math.min(max, Math.max(min, snapped)).toFixed(decimals)));
  }

  get value() {
    if (this.tagName === "SELECT") {
      if (this._hasValue) return this._value;
      const first = this.children.find((child) => child instanceof LabElement && child.tagName === "OPTION");
      return first ? first.value : "";
    }
    return this._value;
  }

  set value(next) {
    const text = String(next);
    this._hasValue = true;
    this._value = this._type === "range" ? this._sanitizeRange(text) : text;
  }

  get valueAsNumber() {
    const raw = this.value;
    if (raw.trim() === "") return Number.NaN;
    return Number(raw);
  }

  get validity() {
    const self = this;
    return {
      get valid() {
        if (self.tagName !== "INPUT") return true;
        const raw = self.value;
        if (raw.trim() === "") return !self.required;
        const num = Number(raw);
        if (!Number.isFinite(num)) return false;
        if (self._min !== "" && num < Number(self._min)) return false;
        if (self._max !== "" && num > Number(self._max)) return false;
        if (self._step !== "" && self._step !== "any") {
          const step = Number(self._step);
          const base = self._min !== "" ? Number(self._min) : 0;
          if (step > 0) {
            const ratio = (num - base) / step;
            if (Math.abs(ratio - Math.round(ratio)) > 1e-7) return false;
          }
        }
        return true;
      },
    };
  }

  get textContent() {
    return this.children.map((child) => child.textContent).join("");
  }

  set textContent(text) {
    for (const child of this.children) child.parentElement = null;
    this.children = text === "" ? [] : [this._adopt(new TextNode(text))];
  }

  _adopt(node) {
    const child = typeof node === "string" ? new TextNode(node) : node;
    if (child.parentElement) child.remove();
    child.parentElement = this;
    return child;
  }

  appendChild(node) {
    const child = this._adopt(node);
    this.children.push(child);
    return child;
  }

  append(...nodes) {
    for (const node of nodes) this.appendChild(node);
  }

  prepend(...nodes) {
    const adopted = nodes.map((node) => this._adopt(node));
    this.children.unshift(...adopted);
  }

  replaceChildren(...nodes) {
    for (const child of this.children) child.parentElement = null;
    this.children = [];
    this.append(...nodes);
  }

  remove() {
    if (!this.parentElement) return;
    const list = this.parentElement.children;
    const index = list.indexOf(this);
    if (index >= 0) list.splice(index, 1);
    this.parentElement = null;
  }

  cloneNode() {
    const copy = new LabElement(this.tagName, this.namespaceURI);
    for (const [key, value] of this.attributes.entries()) copy.attributes.set(key, value);
    copy._type = this._type;
    copy._min = this._min;
    copy._max = this._max;
    copy._step = this._step;
    copy._value = this._value;
    copy._hasValue = this._hasValue;
    copy.required = this.required;
    copy.disabled = this.disabled;
    return copy;
  }

  setAttribute(name, value) {
    this.attributes.set(name, String(value));
  }

  getAttribute(name) {
    return this.attributes.has(name) ? this.attributes.get(name) : null;
  }

  removeAttribute(name) {
    this.attributes.delete(name);
  }

  hasAttribute(name) {
    return this.attributes.has(name);
  }

  matches(selector) {
    return selector.split(",").some((part) => matchSingleSelector(this, part));
  }

  querySelector(selector) {
    for (const child of this.children) {
      if (!(child instanceof LabElement)) continue;
      if (child.matches(selector)) return child;
      const nested = child.querySelector(selector);
      if (nested) return nested;
    }
    return null;
  }

  querySelectorAll(selector) {
    const out = [];
    const visit = (node) => {
      for (const child of node.children) {
        if (!(child instanceof LabElement)) continue;
        if (child.matches(selector)) out.push(child);
        visit(child);
      }
    };
    visit(this);
    return out;
  }

  addEventListener(type, listener) {
    if (!this.listeners.has(type)) this.listeners.set(type, []);
    this.listeners.get(type).push(listener);
  }

  dispatchEvent(event) {
    for (const listener of this.listeners.get(event.type) ?? []) listener(event);
    return !event.defaultPrevented;
  }

  click() {
    if (this.disabled) return;
    this.dispatchEvent({ type: "click", preventDefault() {} });
  }
}

export function pressKey(target, key, modifiers = {}) {
  let prevented = false;
  const event = {
    type: "keydown",
    key,
    shiftKey: Boolean(modifiers.shiftKey),
    altKey: Boolean(modifiers.altKey),
    ctrlKey: Boolean(modifiers.ctrlKey),
    metaKey: Boolean(modifiers.metaKey),
    get defaultPrevented() {
      return prevented;
    },
    preventDefault() {
      prevented = true;
    },
  };
  target.dispatchEvent(event);
  return event;
}

export function installLabDom(t) {
  const names = ["document", "getComputedStyle", "MutationObserver", "ResizeObserver", "requestAnimationFrame", "cancelAnimationFrame"];
  const saved = new Map(names.map((name) => [name, Object.getOwnPropertyDescriptor(globalThis, name)]));
  const cleanups = [];
  const html = new LabElement("html");
  const head = html.appendChild(new LabElement("head"));
  const body = html.appendChild(new LabElement("body"));
  const root = body.appendChild(new LabElement("div"));
  const doc = {
    head,
    body,
    documentElement: html,
    createElement: (tag) => new LabElement(tag),
    createElementNS: (ns, tag) => new LabElement(tag, ns),
    createTextNode: (text) => new TextNode(text),
    getElementById: (id) => html.querySelector(`#${id}`),
    querySelector: (selector) => html.querySelector(selector),
    querySelectorAll: (selector) => html.querySelectorAll(selector),
  };
  globalThis.document = doc;
  globalThis.getComputedStyle = () => ({ getPropertyValue: () => "" });
  globalThis.MutationObserver = class { observe() {} disconnect() {} };
  globalThis.ResizeObserver = class { observe() {} disconnect() {} };
  globalThis.requestAnimationFrame = () => 0;
  globalThis.cancelAnimationFrame = () => {};
  t.after(() => {
    while (cleanups.length) cleanups.pop()();
    for (const [name, descriptor] of saved.entries()) {
      if (descriptor) Object.defineProperty(globalThis, name, descriptor);
      else delete globalThis[name];
    }
  });
  return { document: doc, root, cleanup: (fn) => cleanups.push(fn) };
}
