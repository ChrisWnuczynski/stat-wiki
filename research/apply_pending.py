"""Apply proposed shared-file changes from research/pending/<slug>.json.

Batch workers never edit shared files. They record proposals in a pending
file, and this script applies them:

    python research/apply_pending.py --ranks 368-382 --overlay
        Merge new bibliography works, article leads and self-check ids into the
        working files so a local build can resolve them. Undo with --restore
        before committing.
    python research/apply_pending.py --restore
        Return every shared file the build or the overlay touches to HEAD.
    python research/apply_pending.py --ranks 368-382 --integrate
        The overlay, plus todo lines appended to research/todo.md. Prints any
        free-form shared edits for review by hand.
    python research/apply_pending.py --ranks 368-382 --proofs-todo
        After a build, keep specific reasons in the regenerated proofs-todo.json:
        a pending reason first, then the reason committed at HEAD.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PENDING = ROOT / "research" / "pending"
GENERIC_REASON = "A reviewed proof sketch is still needed."
SHARED = ["bibliography.json", "article_leads.json", "research/self-checks.json", "proofs-todo.json",
          "overview.qmd", "labs"]
LEAD_KEYS = {"field", "article", "term", "verb", "description", "proper"}


def ranked_slugs(spec: str) -> list[str]:
    ranking = json.loads((ROOT / "research" / "ranking.json").read_text(encoding="utf-8"))
    low, _, high = spec.partition("-")
    low_i, high_i = int(low), int(high or low)
    return [row["slug"] for rank, row in enumerate(ranking, start=1) if low_i <= rank <= high_i]


def load(slugs: list[str]) -> list[dict]:
    rows = []
    for slug in slugs:
        path = PENDING / f"{slug}.json"
        if not path.is_file():
            print(f"missing pending file: {path.relative_to(ROOT)}", file=sys.stderr)
            continue
        rows.append(json.loads(path.read_text(encoding="utf-8")))
    return rows


def write_json(path: Path, data, indent: int = 2) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=indent) + "\n", encoding="utf-8")


def append_works(text: str, works: dict) -> str:
    """Append works before the closing braces, in the file's indent-2 layout."""
    if not works:
        return text
    body = text.rstrip()
    assert body.endswith("}\n}") or body.endswith("}\n  }\n}"), "unexpected bibliography.json ending"
    head, _, _ = body.rpartition("\n  }\n}")
    pieces = []
    for key, work in works.items():
        block = json.dumps({key: work}, ensure_ascii=False, indent=2)[2:-2]
        pieces.append("\n".join("  " + line for line in block.splitlines()))
    return head + ",\n" + ",\n".join(pieces) + "\n  }\n}\n"


def set_lead(text: str, slug: str, lead: dict) -> str:
    """Replace one slug's single-line entry in article_leads.json."""
    lines = text.splitlines(keepends=True)
    prefix = f'  "{slug}": '
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            comma = "," if line.rstrip("\n").endswith(",") else ""
            lines[i] = prefix + json.dumps(lead, ensure_ascii=False) + comma + "\n"
            return "".join(lines)
    raise KeyError(f"{slug} has no line in article_leads.json")


def overlay(rows: list[dict]) -> list[str]:
    problems: list[str] = []
    bib_path = ROOT / "bibliography.json"
    bib_text = bib_path.read_text(encoding="utf-8")
    works = json.loads(bib_text)["works"]
    leads_path = ROOT / "article_leads.json"
    leads_text = leads_path.read_text(encoding="utf-8")
    checks_path = ROOT / "research" / "self-checks.json"
    checks = json.loads(checks_path.read_text(encoding="utf-8"))
    new_works: dict = {}
    led, checked = [], []
    for row in rows:
        slug = row["slug"]
        for key, work in (row.get("bibliography") or {}).items():
            if key in works or key in new_works:
                existing = works.get(key, new_works.get(key))
                if existing != work:
                    problems.append(f"{slug}: bibliography key {key} already exists with different fields; kept the first")
                continue
            new_works[key] = work
        for lead_slug, lead in (row.get("article_leads") or {}).items():
            if lead_slug != slug:
                problems.append(f"{slug}: article_leads may only change its own slug, not {lead_slug}")
                continue
            if not set(lead) <= LEAD_KEYS or not {"field", "article", "term", "verb", "description"} <= set(lead):
                problems.append(f"{slug}: article_leads entry has wrong keys {sorted(lead)}")
                continue
            leads_text = set_lead(leads_text, slug, lead)
            led.append(slug)
        if row.get("self_checks"):
            checks[slug] = row["self_checks"]
            checked.append(slug)
    bib_path.write_text(append_works(bib_text, new_works), encoding="utf-8")
    json.loads(bib_path.read_text(encoding="utf-8"))
    leads_path.write_text(leads_text, encoding="utf-8")
    json.loads(leads_text)
    if checked:
        write_json(checks_path, checks)
    print(f"bibliography +{len(new_works)} {list(new_works)}")
    print(f"article leads replaced: {led}")
    print(f"self-checks set: {checked}")
    return problems


def integrate_todo(rows: list[dict]) -> None:
    todo_path = ROOT / "research" / "todo.md"
    text = todo_path.read_text(encoding="utf-8")
    new = []
    for row in rows:
        for item in row.get("todo") or []:
            line = item if item.startswith("- ") else f"- {item}"
            if line not in text and line not in new:
                new.append(line)
    if new:
        todo_path.write_text(text.rstrip("\n") + "\n" + "\n".join(new) + "\n", encoding="utf-8")
    print(f"todo.md +{len(new)} lines")


def merge_proofs_todo(rows: list[dict]) -> None:
    path = ROOT / "proofs-todo.json"
    generated = json.loads(path.read_text(encoding="utf-8"))
    committed = json.loads(subprocess.run(["git", "show", "HEAD:proofs-todo.json"], cwd=ROOT, check=True,
                                          capture_output=True, text=True).stdout)
    head_reason = {row["slug"]: row["reason"] for row in committed if row["reason"] != GENERIC_REASON}
    pending_reason = {}
    for row in rows:
        for entry in row.get("proofs_todo") or []:
            pending_reason[entry["slug"]] = entry["reason"]
    used = set()
    for entry in generated:
        if entry["reason"] != GENERIC_REASON:
            continue
        if entry["slug"] in pending_reason:
            entry["reason"] = pending_reason[entry["slug"]]
            used.add(entry["slug"])
        elif entry["slug"] in head_reason:
            entry["reason"] = head_reason[entry["slug"]]
    unused = sorted(set(pending_reason) - used)
    if unused:
        print(f"pending proofs_todo reasons with no generated entry (page proved or not a result page): {unused}")
    write_json(path, generated)
    gone = sorted({row["slug"] for row in committed} - {row["slug"] for row in generated})
    print(f"proofs-todo.json: {len(generated)} entries; left the list: {gone}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ranks", help="rank range such as 368-382")
    parser.add_argument("--slugs", help="comma-separated slugs")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--overlay", action="store_true")
    mode.add_argument("--integrate", action="store_true")
    mode.add_argument("--restore", action="store_true")
    mode.add_argument("--proofs-todo", action="store_true")
    args = parser.parse_args(argv)
    if args.restore:
        subprocess.run(["git", "checkout", "HEAD", "--", *SHARED], cwd=ROOT, check=True)
        print("shared files restored to HEAD")
        return 0
    slugs = ranked_slugs(args.ranks) if args.ranks else []
    if args.slugs:
        slugs += [s.strip() for s in args.slugs.split(",") if s.strip()]
    rows = load(slugs)
    if args.proofs_todo:
        merge_proofs_todo(rows)
        return 0
    problems = overlay(rows)
    if args.integrate:
        integrate_todo(rows)
        for row in rows:
            for edit in row.get("shared_edits") or []:
                print(f"REVIEW {row['slug']}: {json.dumps(edit, ensure_ascii=False)}")
    for problem in problems:
        print(f"PROBLEM {problem}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
