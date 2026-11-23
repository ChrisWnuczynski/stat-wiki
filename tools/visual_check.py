"""Render checks for the visual audit.

Layout checks use headless Chromium. The maths scan reads every rendered page
and ignores KaTeX, so a dropped command cannot hide inside a formula.

    python tools/visual_check.py --site _site --screenshots /opt/cursor/artifacts
"""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

MATH_RE = re.compile(r"\\\(|\\\[|\^\{|_\{|\(\s*\)|\[\s*,\s*\]")
SKIP_TAGS = {"script", "style", "katex", "annotation", "code", "pre"}
# A bare void tag is start-only, so it must not take a stack slot.
VOID_TAGS = frozenset({
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
})


class VisibleText(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.nodes: list[str] = []
        self._skip = 0
        self._stack: list[bool] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in VOID_TAGS:
            return
        classes = dict(attrs).get("class", "")
        names = set(str(classes).split())
        skip = tag in SKIP_TAGS or "katex" in names or "math" in names
        self._stack.append(skip)
        if skip:
            self._skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_TAGS:
            return
        if self._stack and self._stack.pop() and self._skip:
            self._skip -= 1

    def handle_startendtag(self, tag: str, attrs) -> None:
        if tag in VOID_TAGS:
            self.handle_starttag(tag, attrs)
            return
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if self._skip or not data.strip():
            return
        self.nodes.append(data)


def maths_hits(html: str) -> list[str]:
    """Broken fragments in one text node.

    A parenthesis that only wraps a rendered formula is two text nodes around
    the formula, so it is not an empty pair.
    """
    parser = VisibleText()
    parser.feed(html)
    hits: list[str] = []
    for node in parser.nodes:
        hits.extend(match.group(0) for match in MATH_RE.finditer(node))
    return hits


def scan_site(site: Path) -> tuple[int, list[tuple[str, str]]]:
    pages = sorted(site.rglob("*.html"))
    bad: list[tuple[str, str]] = []
    for path in pages:
        hits = maths_hits(path.read_text(encoding="utf-8", errors="replace"))
        if hits:
            bad.append((path.relative_to(site).as_posix(), hits[0]))
    return len(pages), bad


def layout_checks(site: Path, screenshots: Path | None) -> list[str]:
    from playwright.sync_api import sync_playwright

    problems: list[str] = []
    screenshots = screenshots.resolve() if screenshots else None
    if screenshots:
        screenshots.mkdir(parents=True, exist_ok=True)

    def page_url(name: str) -> str:
        return (site / name).resolve().as_uri()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        for width in (1024, 1280, 390):
            page.set_viewport_size({"width": width, "height": 800})
            page.goto(page_url("articles/beta-distribution.html"), wait_until="networkidle")
            info = page.evaluate(
                """() => {
                  const box = document.querySelector('.infobox');
                  const content = document.querySelector('#quarto-document-content');
                  const table = box && box.querySelector('table');
                  if (!box || !table || !content) return {missing: true};
                  const br = box.getBoundingClientRect();
                  const tr = table.getBoundingClientRect();
                  const floated = getComputedStyle(box).float === 'right' || getComputedStyle(box).float === 'left';
                  const contentWidth = content.getBoundingClientRect().width;
                  let column = contentWidth;
                  if (floated) column = contentWidth - br.width - 24;
                  return {
                    floated,
                    tablePast: tr.right - br.right,
                    tableBefore: br.left - tr.left,
                    paraWidth: column,
                    contentWidth,
                  };
                }"""
            )
            if info.get("missing"):
                problems.append(f"beta-distribution at {width}: no infobox table")
            else:
                if info["tablePast"] > 2 or info["tableBefore"] > 2:
                    problems.append(
                        f"beta-distribution at {width}: table escapes the infobox "
                        f"by {info['tablePast']:.1f}px"
                    )
                if width >= 1000:
                    if info["paraWidth"] < 400:
                        problems.append(
                            f"beta-distribution at {width}: body column is {info['paraWidth']:.0f}px"
                        )
                elif info["floated"] or info["paraWidth"] < info["contentWidth"] * 0.85:
                    problems.append(f"beta-distribution at {width}: infobox still squeezes the column")
            if screenshots and width in {1024, 1280}:
                page.screenshot(path=str(screenshots / f"beta-distribution-{width}.png"), full_page=False)

        for name, shot in (
            ("articles/conditional-expectation.html", "conditional-expectation.png"),
            ("articles/kurtosis.html", "kurtosis.png"),
        ):
            page.set_viewport_size({"width": 1280, "height": 800})
            page.goto(page_url(name), wait_until="networkidle")
            hits = maths_hits(page.content())
            if hits:
                problems.append(f"{name}: visible maths fragment {hits[0]!r}")
            active = page.locator("#quarto-sidebar a.sidebar-link.active")
            if name.endswith("kurtosis.html") and active.count() < 1:
                problems.append("kurtosis: sidebar has no active item")
            if screenshots:
                page.screenshot(path=str(screenshots / shot), full_page=False)
                if name.endswith("kurtosis.html"):
                    page.screenshot(path=str(screenshots / "kurtosis-sidebar-desktop.png"), full_page=False)
                    page.set_viewport_size({"width": 390, "height": 844})
                    toggle = page.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first
                    if toggle.count():
                        toggle.click()
                        page.wait_for_timeout(400)
                    page.screenshot(path=str(screenshots / "kurtosis-sidebar-mobile.png"), full_page=False)
        problems.extend(sidebar_scroll_checks(browser, site, screenshots))
        problems.extend(sidebar_history_checks(browser, site, screenshots))
        browser.close()
        # The default Playwright launch disables BFCache; exercise the cached path too.
        cached_browser = playwright.chromium.launch(channel="chromium", ignore_default_args=["--disable-back-forward-cache"])
        problems.extend(sidebar_history_checks(cached_browser, site, screenshots, bfcache=True))
        cached_browser.close()
    return problems


def sidebar_scroll_checks(browser, site: Path, screenshots: Path | None) -> list[str]:
    """Exercise the rendered, hydrated menu with native wheel/pointer/keyboard input."""
    from functools import partial
    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
    from threading import Thread

    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    problems: list[str] = []
    with ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(site.resolve()))) as server:
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f"http://127.0.0.1:{server.server_port}"
        for width, height in ((1363, 936), (390, 844)):
            context = browser.new_context(viewport={"width": width, "height": height})
            page = context.new_page()
            root = page.locator("#quarto-sidebar")

            def settle():
                # The old 400ms callback queued another callback at 350ms.
                page.wait_for_timeout(1100)

            def state():
                return root.evaluate("""el => ({top: el.scrollTop, body: scrollY,
                    viewport_top: el.getBoundingClientRect().top, max: el.scrollHeight - el.clientHeight,
                    open: [...el.querySelectorAll('.sidebar-section.collapse.show')].map(e => e.id)})""")

            def pointer(locator, button="left"):
                # locator.click() may scroll ancestors before dispatch; use viewport coordinates.
                rect = locator.bounding_box()
                bounds = root.bounding_box()
                assert rect and bounds and rect["height"] > 0, "missing sidebar target"
                x, y = rect["x"] + rect["width"] / 2, rect["y"] + rect["height"] / 2
                assert bounds["y"] <= y <= min(height, bounds["y"] + bounds["height"]), "target needs wheel scrolling"
                page.mouse.click(x, y, button=button)

            def wheel_to(top):
                bounds = root.bounding_box()
                page.mouse.move(bounds["x"] + 100, max(bounds["y"] + 50, height / 2))
                page.mouse.wheel(0, top - state()["top"])
                page.wait_for_timeout(300)

            def wheel_into(locator):
                rect, bounds = locator.bounding_box(), root.bounding_box()
                assert rect and rect["height"] > 0, f"target is in a closed branch: {locator} at {page.url}"
                wheel_to(state()["top"] + rect["y"] - bounds["y"] - min(220, bounds["height"] / 3))

            def group(label):
                return root.locator('a.sidebar-link[data-bs-toggle="collapse"]').filter(has_text=re.compile(r"^\s*" + re.escape(label) + r"\s*$")).first

            def open_drawer():
                if width < 992 and not root.is_visible():
                    toggle = page.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first
                    # This control is outside the sidebar.
                    rect = toggle.bounding_box()
                    assert rect, "missing drawer control"
                    page.mouse.click(rect["x"] + rect["width"] / 2, rect["y"] + rect["height"] / 2)
                    focus = page.evaluate_handle("document.activeElement")
                    settle()
                    assert focus.evaluate("e => e === document.activeElement"), "drawer timer moved focus"
                    focus.dispose()

            def load(path="/"):
                page.goto(base + path, wait_until="networkidle")
                page.wait_for_selector('#quarto-sidebar ul[data-hydrated="true"]', state="attached")
                settle()
                open_drawer()

            def unchanged(before, label):
                after = state()
                assert abs(after["top"] - before["top"]) <= 2, f"{label}: sidebar {before['top']} -> {after['top']}"
                assert abs(after["body"] - before["body"]) <= 2, f"{label}: document {before['body']} -> {after['body']}"

            try:
                load()
                assert state()["max"] > 250, "sidebar is not realistically scrollable"
                if width >= 992:
                    page.mouse.move(width - 350, height / 2)
                    page.mouse.wheel(0, 260)
                    page.wait_for_timeout(300)
                    assert state()["body"] > 100, "test did not independently scroll the document"
                wheel_into(group("Data analysis"))
                before = state()
                assert before["top"] > 100, "test did not intentionally scroll down"
                pointer(group("Data analysis"))
                settle()
                unchanged(before, "expand Data analysis")
                assert group("Data analysis").get_attribute("aria-expanded") == "true"
                studies = group("Studies, data, and evidence")
                wheel_into(studies)
                before = state()
                pointer(studies)
                settle()
                unchanged(before, "expand nested Studies")
                assert studies.get_attribute("aria-expanded") == "true"
                assert page.locator(studies.get_attribute("data-bs-target")).is_visible()
                chevron = studies.locator("..").locator("a.sidebar-item-toggle")
                before = state()
                pointer(chevron)
                focus = page.evaluate_handle("document.activeElement")
                settle()
                unchanged(before, "collapse nested Studies chevron")
                assert studies.get_attribute("aria-expanded") == "false"
                assert not page.locator(studies.get_attribute("data-bs-target")).is_visible()
                assert focus.evaluate("e => e === document.activeElement"), "toggle timer moved focus"
                focus.dispose()
                pointer(studies)
                settle()
                assert studies.get_attribute("aria-expanded") == "true"
                if width >= 992:
                    page.mouse.move(width - 350, height / 2)
                    page.mouse.wheel(0, -state()["body"])
                    page.wait_for_timeout(300)
                    assert state()["body"] == 0, "document did not return to its normal navigation position"

                leaf = root.locator('a[href$="/articles/sampling-bias.html"]')
                wheel_into(leaf)
                # Leave the chosen row away from the automatic reveal position.
                wheel_to(state()["top"] - 120)
                before, row_y = state(), leaf.bounding_box()["y"]
                pointer(leaf)
                page.wait_for_url("**/articles/sampling-bias.html")
                page.wait_for_load_state("networkidle")
                settle()
                assert page.evaluate("document.activeElement.tagName") == "BODY", "leaf restoration moved focus"
                open_drawer()
                after = state()
                assert abs(after["top"] - before["top"]) <= 2, f"leaf navigation: sidebar {before['top']} -> {after['top']}"
                assert after["body"] == 0, "leaf navigation changed default document position"
                assert set(before["open"]).issubset(after["open"]), "leaf navigation closed an existing branch"
                active = root.locator('a.sidebar-link.active[aria-current="page"]')
                assert active.count() == 1 and active.get_attribute("href").endswith("sampling-bias.html")
                # The existing mobile breadcrumb can wrap and move the whole drawer.
                # Keep the row's position within its scroll viewport, independently of that layout.
                row_before = row_y - before["viewport_top"]
                row_after = active.bounding_box()["y"] - after["viewport_top"]
                assert abs(row_after - row_before) <= 2, "selected row moved within the sidebar viewport"
                if width >= 992:
                    assert abs(after["viewport_top"] - before["viewport_top"]) <= 2, "desktop sidebar moved"
                print(f"sidebar leaf at {width}px: scroll {before['top']} -> {after['top']}; row within sidebar {row_before:.1f} -> {row_after:.1f}; document {before['body']} -> {after['body']}")
                if screenshots:
                    page.screenshot(path=str(screenshots / f"sidebar-scroll-{width}.png"))

                # Clicking the active leaf is another native document navigation.
                before = state()
                active = root.locator('a.sidebar-link.active[aria-current="page"]')
                with page.expect_navigation(wait_until="networkidle"):
                    pointer(active)
                settle()
                assert page.evaluate("document.activeElement.tagName") == "BODY", "active leaf restoration moved focus"
                open_drawer()
                unchanged(before, "active leaf re-click")
                assert set(before["open"]).issubset(state()["open"]), "active leaf re-click lost an open branch"

                # An independent open branch must also survive a link near the top.
                lab = root.locator('a[href$="/labs/distributions.html"]')
                wheel_into(lab)
                before, row_y = state(), lab.bounding_box()["y"]
                pointer(lab)
                page.wait_for_url("**/labs/distributions.html")
                page.wait_for_load_state("networkidle")
                settle()
                open_drawer()
                assert abs(state()["top"] - before["top"]) <= 2, "near-top leaf reset sidebar position"
                assert group("Data analysis").get_attribute("aria-expanded") == "true", "near-top leaf lost independent branch"
                assert abs((root.locator('a.sidebar-link.active').bounding_box()["y"] - state()["viewport_top"]) - (row_y - before["viewport_top"])) <= 2, "near-top row moved within sidebar"

                # Tab/Enter navigation must retain native focus and link behavior.
                leaf = root.locator('a[href$="/articles/sampling-bias.html"]')
                wheel_into(leaf)
                before = state()
                pointer(leaf)
                page.wait_for_url("**/articles/sampling-bias.html")
                page.wait_for_load_state("networkidle")
                settle()
                open_drawer()
                unchanged(before, "return leaf navigation")
                assert set(before["open"]).issubset(state()["open"]), "return leaf lost an open branch"
                leaf = root.locator('a[href$="/articles/sampling-bias.html"]')
                # Reach the current leaf through the native Tab order, then follow its predecessor.
                for _ in range(200):
                    page.keyboard.press("Tab")
                    if leaf.evaluate("e => e === document.activeElement"):
                        break
                else:
                    raise AssertionError("Tab did not reach the current sidebar leaf")
                page.keyboard.press("Shift+Tab")
                target = page.evaluate("document.activeElement.href")
                assert target and target != page.url, "no preceding keyboard leaf"
                before = state()
                page.keyboard.press("Enter")
                page.wait_for_url(target)
                page.wait_for_load_state("networkidle")
                settle()
                assert page.evaluate("document.activeElement.tagName") == "BODY", "keyboard leaf restoration moved focus"
                open_drawer()
                assert abs(state()["top"] - before["top"]) <= 2, "keyboard leaf reset sidebar position"
                assert state()["body"] == 0, "keyboard leaf changed document position"

                # Ordinary leaf history stays with the browser, with no saved sidebar record.
                page.go_back(wait_until="networkidle")
                settle()
                assert page.url.endswith("/articles/sampling-bias.html"), "Back lost the previous leaf"
                assert page.evaluate("sessionStorage.getItem('statwiki-sidebar-navigation')") is None
                page.go_forward(wait_until="networkidle")
                settle()
                assert page.url == target, "Forward lost the next leaf"
                assert page.evaluate("sessionStorage.getItem('statwiki-sidebar-navigation')") is None
                # Quarto's existing Zenscroll uses manual history restoration.
                assert page.evaluate("history.scrollRestoration") == "manual", "sidebar changed Quarto history restoration"
                open_drawer()

                # A direct deep link has no saved navigation and still reveals its active row.
                direct = context.new_page()
                direct.goto(base + "/articles/kurtosis.html", wait_until="networkidle")
                direct.wait_for_timeout(1100)
                if width < 992:
                    direct.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first.click()
                    direct.wait_for_timeout(1100)
                active = direct.locator('#quarto-sidebar a.sidebar-link.active[aria-current="page"]')
                box, bounds = active.bounding_box(), direct.locator("#quarto-sidebar").bounding_box()
                assert box and bounds and box["y"] >= bounds["y"] and box["y"] + box["height"] <= min(height, bounds["y"] + bounds["height"]), "direct deep link did not reveal active row"
                direct.close()

                load()
                wheel_into(group("Data analysis"))
                pointer(group("Data analysis"))
                settle()
                lab = root.locator('a[href$="/labs/distributions.html"]')
                wheel_into(lab)
                before = state()
                for mode in ("Control", "middle", "target"):
                    if mode == "target":
                        lab.evaluate("e => e.target = '_blank'")
                    with context.expect_page() as opened:
                        if mode == "Control":
                            page.keyboard.down("Control")
                        pointer(lab, button="middle" if mode == "middle" else "left")
                        if mode == "Control":
                            page.keyboard.up("Control")
                    other = opened.value
                    other.wait_for_load_state("networkidle")
                    other.wait_for_timeout(1100)
                    assert other.url.endswith("/labs/distributions.html"), f"{mode}: native new-tab link failed"
                    assert other.locator('#quarto-sidebar a[data-bs-toggle="collapse"]').filter(has_text=re.compile(r"^\s*Data analysis\s*$")).first.get_attribute("aria-expanded") == "false", f"{mode}: new tab inherited unrelated open branch"
                    assert page.evaluate("sessionStorage.getItem('statwiki-sidebar-navigation')") is None, f"{mode}: left a navigation record"
                    other.close()
                    unchanged(before, f"{mode} new-tab click")
                lab.evaluate("e => e.removeAttribute('target')")

                # Same-document fragment links keep the browser's document scrolling.
                load("/articles/sampling-bias.html")
                active = root.locator('a.sidebar-link.active')
                wheel_into(active)
                anchor = page.locator("main section[id]").first.get_attribute("id")
                assert anchor, "missing fragment target"
                active.evaluate("(e, id) => e.hash = id", anchor)
                before = state()
                pointer(active)
                settle()
                assert page.url.endswith("#" + anchor), "sidebar handler changed native fragment navigation"
                assert abs(state()["top"] - before["top"]) <= 2, "fragment navigation repositioned sidebar"
                assert page.evaluate("sessionStorage.getItem('statwiki-sidebar-navigation')") is None

                # Returning through history must not create a sidebar navigation record.
                page.go_back(wait_until="networkidle")
                settle()
                page.go_forward(wait_until="networkidle")
                settle()
                assert page.url.endswith("#" + anchor), "Back/Forward lost the fragment"
                assert page.evaluate("sessionStorage.getItem('statwiki-sidebar-navigation')") is None
                blocked = browser.new_context(viewport={"width": width, "height": height})
                blocked.add_init_script("""for (const method of ['getItem', 'setItem', 'removeItem']) {
                    const original = Storage.prototype[method];
                    Storage.prototype[method] = function(key, ...args) {
                        if (key === 'statwiki-sidebar-navigation') throw new DOMException('Blocked', 'SecurityError');
                        return original.call(this, key, ...args);
                    };
                }""")
                try:
                    blocked_page = blocked.new_page()
                    errors = []
                    blocked_page.on("pageerror", lambda error: errors.append(str(error)))
                    blocked_page.goto(base + "/", wait_until="networkidle")
                    blocked_page.wait_for_timeout(1100)
                    if width < 992:
                        blocked_page.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first.click()
                        blocked_page.wait_for_timeout(1100)
                    lab = blocked_page.locator('#quarto-sidebar a[href$="/labs/distributions.html"]')
                    rect = lab.bounding_box()
                    assert rect and 0 < rect["y"] < height, "blocked-storage leaf is not visible"
                    blocked_page.mouse.click(rect["x"] + rect["width"] / 2, rect["y"] + rect["height"] / 2)
                    blocked_page.wait_for_url("**/labs/distributions.html")
                    blocked_page.wait_for_load_state("networkidle")
                    blocked_page.wait_for_timeout(1100)
                    assert not errors, f"storage failure escaped: {errors}"
                    assert blocked_page.locator('#quarto-sidebar a.active[aria-current="page"]').count() == 1
                finally:
                    blocked.close()
                print(f"sidebar scroll: toggles, pointer/keyboard leaves, direct links, new tabs, fragments, history and blocked storage passed at {width}px")
            except Exception as exc:
                problems.append(f"sidebar scroll at {width}: {exc}")
            finally:
                context.close()
        server.shutdown()
        thread.join()
    return problems


def sidebar_history_checks(browser, site: Path, screenshots: Path | None, *, bfcache=False) -> list[str]:
    """Back/Forward must restore the departed entry, not another visit to its URL."""
    from functools import partial
    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
    from threading import Thread

    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    problems: list[str] = []
    with ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(site.resolve()))) as server:
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f"http://127.0.0.1:{server.server_port}"
        for width, height in ((1363, 936), (390, 844)):
            context = browser.new_context(viewport={"width": width, "height": height})
            context.add_init_script("""window.sidebarHistoryShows = [];
                addEventListener('pageshow', e => sidebarHistoryShows.push(e.persisted));""")
            page = context.new_page()
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            root = page.locator("#quarto-sidebar")

            def settle():
                page.wait_for_timeout(1100)

            def state():
                return root.evaluate("""el => ({top: el.scrollTop, body: scrollY,
                    open: [...el.querySelectorAll('.sidebar-section.collapse.show')].map(e => e.id),
                    url: location.href, origin: performance.timeOrigin,
                    type: performance.getEntriesByType('navigation')[0].type,
                    entry: window.navigation?.currentEntry?.key,
                    persisted: window.sidebarHistoryShows.at(-1), history: history.state})""")

            def drawer():
                if width < 992 and not root.is_visible():
                    rect = page.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first.bounding_box()
                    assert rect, "missing mobile drawer toggle"
                    page.mouse.click(rect["x"] + rect["width"] / 2, rect["y"] + rect["height"] / 2)
                    settle()

            def wheel(top):
                rect = root.bounding_box()
                page.mouse.move(rect["x"] + 100, max(rect["y"] + 50, height / 2))
                page.mouse.wheel(0, top - state()["top"])
                page.wait_for_timeout(300)

            def pointer(locator):
                rect, bounds = locator.bounding_box(), root.bounding_box()
                assert rect and rect["height"] > 0, "history target is collapsed"
                y = rect["y"] + rect["height"] / 2
                assert bounds["y"] <= y < min(height, bounds["y"] + bounds["height"]), "history target needs wheel input"
                page.mouse.click(rect["x"] + rect["width"] / 2, y)

            def into(locator):
                rect, bounds = locator.bounding_box(), root.bounding_box()
                assert rect and rect["height"] > 0, "history target is collapsed"
                wheel(state()["top"] + rect["y"] - bounds["y"] - 180)

            def follow(path, offset=0):
                link = root.locator('a[href$="' + path + '"]')
                into(link)
                if offset:
                    wheel(state()["top"] + offset)
                before = state()
                pointer(link)
                page.wait_for_url("**" + path)
                page.wait_for_load_state("load")
                settle()
                assert page.evaluate("document.activeElement.tagName") == "BODY", "history setup moved focus"
                drawer()
                after = state()
                assert abs(after["top"] - before["top"]) <= 2, "ordinary link lost sidebar position"
                assert set(before["open"]).issubset(after["open"]), "ordinary link lost an open group"
                return before

            def restored(expected, label):
                if not bfcache:
                    page.wait_for_load_state("load")
                settle()
                assert page.url == expected["url"], f"{label}: wrong history entry"
                drawer()
                actual = state()
                assert abs(actual["top"] - expected["top"]) <= 2, f"{label}: sidebar {expected['top']} -> {actual['top']}"
                assert actual["entry"] == expected["entry"], f"{label}: changed history entry identity"
                assert actual["open"] == expected["open"], f"{label}: open groups changed"
                assert abs(actual["body"] - expected["body"]) <= 2, f"{label}: body history {expected['body']} -> {actual['body']}"
                assert actual["persisted"] == bfcache, f"{label}: expected BFCache={bfcache}, got {actual}"
                if bfcache:
                    assert actual["origin"] == expected["origin"], f"{label}: document was recreated"
                else:
                    assert actual["type"] == "back_forward", f"{label}: not a cold history navigation"
                    assert actual["origin"] != expected["origin"], f"{label}: document was not recreated"
                assert actual["history"].get("sidebarTestOwner") == "preserve", "unrelated history state was replaced"
                assert page.evaluate("history.scrollRestoration") == "manual", "Quarto body restoration changed"
                assert page.evaluate("sessionStorage.getItem('statwiki-sidebar-navigation')") is None
                print(f"sidebar history {width}px BFCache={bfcache} {label}: {expected['top']} -> {actual['top']}; groups {len(actual['open'])}; persisted={actual['persisted']}")
                return actual

            def owner():
                page.evaluate("history.replaceState({...history.state, sidebarTestOwner: 'preserve'}, '')")

            try:
                page.goto(base + "/articles/sampling-bias.html", wait_until="networkidle")
                settle()
                drawer()
                owner()
                sampling1 = follow("/labs/distributions.html")
                owner()
                if width >= 992:
                    page.mouse.move(width - 400, height / 2)
                    page.mouse.wheel(0, 320)
                    page.wait_for_timeout(300)
                    assert state()["body"] > 200, "history fixture did not scroll the body"
                lab1 = follow("/articles/sampling-bias.html")
                owner()
                # This is the same URL as sampling1, with a distinct viewport and group set.
                extra = root.locator('a.sidebar-link[data-bs-toggle="collapse"]').filter(has_text=re.compile(r"^\s*Descriptive statistics\s*$")).first
                into(extra)
                pointer(extra)
                settle()
                sampling2 = follow("/labs/distributions.html", offset=70)
                assert abs(sampling2["top"] - sampling1["top"]) > 20, "repeat-URL fixture needs distinct positions"
                assert sampling2["open"] != sampling1["open"], "repeat-URL fixture needs distinct groups"
                assert sampling2["entry"] != sampling1["entry"], "repeated URL did not create distinct entries"
                owner()
                wheel(state()["top"] + 91)
                lab2 = state()
                page.go_back(wait_until="commit")
                restored(sampling2, "Back to second Sampling bias")
                page.go_back(wait_until="commit")
                restored(lab1, "Back across topic to first Explorer")
                page.go_back(wait_until="commit")
                restored(sampling1, "Back to first Sampling bias")
                page.go_forward(wait_until="commit")
                restored(lab1, "Forward to first Explorer")
                page.go_forward(wait_until="commit")
                restored(sampling2, "Forward to second Sampling bias")
                page.go_forward(wait_until="commit")
                restored(lab2, "Forward to second Explorer")
                if screenshots:
                    page.screenshot(path=str(screenshots / f"sidebar-history-{width}-{bfcache}.png"))

                # A same-tab active reclick retains the existing one-time transfer behavior.
                active = root.locator('a.sidebar-link.active[aria-current="page"]')
                into(active)
                before = state()
                with page.expect_navigation(wait_until="load"):
                    pointer(active)
                settle()
                drawer()
                assert abs(state()["top"] - before["top"]) <= 2, "same-tab reclick lost sidebar position"
                assert state()["open"] == before["open"], "same-tab reclick lost open groups"

                # Input before the delayed restore callbacks is an explicit manual override.
                follow("/articles/sampling-bias.html")
                page.go_back(wait_until="commit")
                drawer()
                wheel(state()["top"] + 140)
                manual = state()
                settle()
                assert abs(state()["top"] - manual["top"]) <= 2, "delayed history restore overrode wheel input"
                if width < 992:
                    owner()
                    closed_view = state()
                    toggle = page.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first
                    rect = toggle.bounding_box()
                    page.mouse.click(rect["x"] + rect["width"] / 2, rect["y"] + rect["height"] / 2)
                    settle()
                    assert not root.is_visible(), "drawer fixture did not close"
                    page.goto(base + "/articles/sampling-bias.html", wait_until="networkidle")
                    page.go_back(wait_until="commit")
                    restored(closed_view, "Back with the drawer previously closed")
                assert not errors, f"history navigation errors: {errors}"
                if not bfcache:
                    # Bad or unavailable state must fall back to the ordinary active row.
                    # These are fault injections, separate from the real input comparisons above.
                    for fault in ("storage", "entry-api", "json", "malformed", "wrong-page", "primitive"):
                        fallback = browser.new_context(viewport={"width": width, "height": height})
                        fault_script = {
                            "storage": "for (const method of ['getItem', 'setItem', 'removeItem']) { const original = Storage.prototype[method]; Storage.prototype[method] = function(key, ...args) { if (key.startsWith('statwiki-sidebar-')) throw new DOMException('Blocked', 'SecurityError'); return original.call(this, key, ...args); }; }",
                            "entry-api": "Object.defineProperty(window, 'navigation', {value: undefined});",
                            "json": "if (performance.getEntriesByType('navigation')[0]?.type === 'back_forward') sessionStorage.setItem('statwiki-sidebar-history:' + navigation.currentEntry.key, '{');",
                            "malformed": "if (performance.getEntriesByType('navigation')[0]?.type === 'back_forward') sessionStorage.setItem('statwiki-sidebar-history:' + navigation.currentEntry.key, JSON.stringify({url: location.href, top: -1, open: [3]}));",
                            "wrong-page": "if (performance.getEntriesByType('navigation')[0]?.type === 'back_forward') sessionStorage.setItem('statwiki-sidebar-history:' + navigation.currentEntry.key, JSON.stringify({url: location.origin + '/different.html', top: 500, open: []}));",
                            "primitive": "history.replaceState('another owner', '');",
                        }[fault]
                        fallback.add_init_script(fault_script)
                        try:
                            fault_page = fallback.new_page()
                            fault_errors = []
                            fault_page.on("pageerror", lambda error: fault_errors.append(str(error)))
                            fault_page.goto(base + "/labs/distributions.html", wait_until="networkidle")
                            fault_page.wait_for_timeout(1100)
                            if width < 992:
                                rect = fault_page.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first.bounding_box()
                                fault_page.mouse.click(rect["x"] + rect["width"] / 2, rect["y"] + rect["height"] / 2)
                                fault_page.wait_for_timeout(1100)
                            fallback_top = fault_page.locator("#quarto-sidebar").evaluate("e => e.scrollTop")
                            fault_page.goto(base + "/articles/sampling-bias.html", wait_until="networkidle")
                            fault_page.go_back(wait_until="commit")
                            fault_page.wait_for_timeout(1100)
                            if width < 992:
                                rect = fault_page.locator(".quarto-btn-toggle, #quarto-sidebar-toggle").first.bounding_box()
                                fault_page.mouse.click(rect["x"] + rect["width"] / 2, rect["y"] + rect["height"] / 2)
                                fault_page.wait_for_timeout(1100)
                            selected = fault_page.locator('#quarto-sidebar a.active[aria-current="page"]')
                            assert selected.count() == 1 and selected.get_attribute("href").endswith("/labs/distributions.html"), f"{fault}: lost active page"
                            assert selected.is_visible(), f"{fault}: active ancestors are closed"
                            assert abs(fault_page.locator("#quarto-sidebar").evaluate("e => e.scrollTop") - fallback_top) <= 2, f"{fault}: did not fall back to the direct active-row position"
                            assert not fault_errors, f"{fault}: uncaught errors {fault_errors}"
                            if fault == "primitive":
                                assert fault_page.evaluate("history.state") == "another owner", "primitive history state was replaced"
                        finally:
                            fallback.close()
                    print(f"sidebar history fallback at {width}px: blocked storage, unavailable entry API, malformed and mismatched snapshots, primitive state passed")
            except Exception as exc:
                problems.append(f"sidebar history at {width}, BFCache={bfcache}: {exc}")
            finally:
                context.close()
        server.shutdown()
        thread.join()
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("_site"))
    parser.add_argument("--screenshots", type=Path)
    parser.add_argument("--skip-browser", action="store_true")
    args = parser.parse_args()
    site = args.site
    if not site.is_dir():
        print(f"No rendered site at {site}", file=sys.stderr)
        return 1
    total, bad = scan_site(site)
    print(f"maths pages: {len(bad)} of {total} still show a broken fragment")
    for path, hit in bad[:20]:
        print(f"  {path}: {hit}")
    problems = [] if args.skip_browser else layout_checks(site, args.screenshots)
    for problem in problems:
        print("layout:", problem)
    if bad or problems:
        return 1
    print("visual checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
