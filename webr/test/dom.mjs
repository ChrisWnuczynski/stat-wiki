// The small DOM surface used by runner.js, for the dependency-free Node tests.
// Event dispatch returns listener promises so tests can await UI cleanup exactly.
class Element {
  constructor(tagName) {
    this.tagName = tagName;
    this.children = [];
    this.className = "";
    this.dataset = {};
    this.attributes = {};
    this.listeners = new Map();
    this.hidden = false;
    this.disabled = false;
    this.text = "";
  }

  set textContent(text) { this.text = text; this.children = []; }
  get textContent() { return this.text + this.children.map((child) => child.textContent).join(""); }
  set innerHTML(html) {
    this.replaceChildren();
    for (const [, tag, attributes, text] of html.matchAll(/<(button|span)\b([^>]*)>([^<]*)<\/\1>/g)) {
      const child = new Element(tag);
      child.className = /class="([^"]*)"/.exec(attributes)?.[1] ?? "";
      child.hidden = /\bhidden\b/.test(attributes);
      child.textContent = text;
      this.appendChild(child);
    }
  }

  appendChild(child) { child.parent = this; this.children.push(child); return child; }
  replaceChildren(...children) { this.text = ""; this.children = []; children.forEach((child) => this.appendChild(child)); }
  setAttribute(name, value) { this.attributes[name] = value; }
  getBoundingClientRect() { return { width: 640 }; }
  focus() {}
  matches(selector) {
    const [tag, ...classes] = selector.split(".");
    return (!tag || tag === this.tagName) && classes.every((name) => this.className.split(" ").includes(name));
  }
  querySelector(selector) {
    for (const child of this.children) {
      if (child.matches(selector)) return child;
      const match = child.querySelector(selector);
      if (match) return match;
    }
    return null;
  }
  closest(selector) { return this.matches(selector) ? this : this.parent?.closest(selector) ?? null; }
  before(element) { this.insertSibling(element, 0); }
  after(element) { this.insertSibling(element, 1); }
  insertSibling(element, offset) {
    element.parent = this.parent;
    this.parent.children.splice(this.parent.children.indexOf(this) + offset, 0, element);
  }
  remove() { this.parent.children.splice(this.parent.children.indexOf(this), 1); }
  addEventListener(type, listener) {
    if (!this.listeners.has(type)) this.listeners.set(type, []);
    this.listeners.get(type).push(listener);
  }
  async dispatchEvent(event) {
    await Promise.all((this.listeners.get(event.type) ?? []).map((listener) => listener(event)));
  }
  click() { return this.disabled ? Promise.resolve() : this.dispatchEvent({ type: "click" }); }
}

export function pageDocument(codes) {
  const main = new Element("main");
  const pres = codes.map((code) => {
    const holder = main.appendChild(new Element("div"));
    holder.className = "sourceCode";
    const pre = holder.appendChild(new Element("pre"));
    pre.className = "sourceCode r";
    pre.appendChild(new Element("code")).textContent = code;
    return pre;
  });
  const head = new Element("head");
  return {
    head,
    createElement: (tag) => new Element(tag),
    getElementById: (id) => head.children.find((child) => child.id === id) ?? null,
    querySelectorAll: () => pres,
  };
}
