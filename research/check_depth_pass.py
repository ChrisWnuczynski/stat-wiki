"""Check depth-pass pages against the research page rules.

    python research/check_depth_pass.py --ranks 368-382 [--run-checks]

Run it after `python build_wiki.py` (with any pending overlay applied). It
applies the rules that test_citations.py enforces for completed ranks, plus
the depth-pass rules for every page type, to the researched pages in the
range. Errors exit with status 1; warnings are printed for review.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

LOCATION = re.compile(
    r"^\s*\((?:Ch\.|§|Thm\.|Lem\.|Lems\.|Cor\.|Prop\.|Props\.|Def\.|Ex\.|Exercise|Example|Eq\.|eq\.|Sec\.|Alg\.|"
    r"Algorithm|Table|Fig\.|Appendix|App\.|p\.|pp\.|Glossary|Description|Details|Value|entries\b|[“\"])"
)
EDITOR_TEST = re.compile(
    r"\b(?:inherited(?!\s+traits\b)|retained\s+(?:example|figure|formula|property|section|content|chapter)|"
    r"existing\s+(?:example|figure|formula|property|section|content|chapter)|"
    r"original definition|opened\s+(?:source|paper|pdf|book|text)|verified\s+source|"
    r"source chapter|the example above was kept|not claiming|not (?:a )?claim)\b",
    re.I,
)
EDITOR_WORDS = re.compile(
    r"\b(?:inherited|retained|existing|original|originally|kept|not a claim|not claiming|earlier version|"
    r"previous version|this revision|this edit|we added|was added|were added|now includes|opened|"
    r"this page (?:now|was))\b",
    re.I,
)
CANONICAL_ALWAYS = {"Lead context", "Motivating example", "Worked example", "Check yourself"}
TEMPLATE_KEYS = {
    "concept": {"Lead context", "Motivating example", "Intuition", "Definition", "Interpretation", "Properties",
                "Statistical use", "Worked example", "Common misconceptions", "Assumptions and limits",
                "Connections", "Check yourself", "History"},
    "theorem": {"Lead context", "Motivating example", "Statement", "Intuition", "Key results", "Proof",
                "Generalizations", "Related concepts", "Statistical use", "Common misconceptions",
                "Check yourself", "History", "Worked example"},
    "distribution": {"Lead context", "Motivating example", "Intuition", "Definition", "Properties",
                     "Related distributions", "Statistical inference", "Generating random samples",
                     "Worked example", "Examples", "Common misconceptions", "Assumptions and limits",
                     "Connections", "Check yourself", "History"},
}
PENDING_KEYS = {"slug", "rank", "batch", "tier", "type", "sections", "words_before", "words_after",
                "figures_before", "figures_after", "sources_read", "proofs", "tests", "skipped",
                "unverified", "bibliography", "article_leads", "proofs_todo", "todo", "self_checks",
                "shared_edits", "oai"}


def prose_words(text: str) -> int:
    return len(re.findall(r"\b[\w-]+\b", re.sub(r"</?[A-Za-z][\w-]*(?:\s+[^>\n]*)?/?>", " ", text)))


def sections(raw: str) -> list[tuple[str, str, str]]:
    out = []
    for match in re.finditer(r"(?ms)^## ([^\n]+)\n(.*?)(?=^## |\Z)", raw):
        key, _, title = match.group(1).partition(" — ")
        out.append((key.strip(), title.strip(), match.group(2)))
    return out


def page_type(slug: str, body: str) -> str:
    distributions = json.loads((ROOT / "distributions.json").read_text(encoding="utf-8"))
    if slug in distributions:
        return "distribution"
    if "| Statement | [Read statement](#statement) |" in body:
        return "theorem"
    return "concept"


def check_page(rank: int, slug: str, works: dict, baseline: dict, run_checks: bool) -> tuple[list[str], list[str]]:
    import theorem_depth

    errors: list[str] = []
    warnings: list[str] = []
    research_path = ROOT / "research" / "content" / f"{slug}.md"
    article_path = ROOT / "articles" / f"{slug}.qmd"
    if not research_path.is_file():
        return [f"no research/content/{slug}.md"], warnings
    if not article_path.is_file():
        return ["articles not built; run python build_wiki.py"], warnings
    raw = research_path.read_text(encoding="utf-8")
    full = article_path.read_text(encoding="utf-8")
    body = full.split("## See also", 1)[0]
    kind = page_type(slug, full)
    secs = sections(raw)
    keys = [key for key, _, _ in secs]

    for key, title, text in secs:
        if key not in TEMPLATE_KEYS[kind]:
            errors.append(f"section {key!r} is not allowed on a {kind} page")
        if title and key in CANONICAL_ALWAYS:
            errors.append(f"{key!r} must keep its canonical heading (no display title)")
        if title and kind == "theorem" and key == "Statement":
            errors.append("theorem 'Statement' heading must stay canonical")
        if title and kind == "theorem" and slug in theorem_depth.RESULT_DEPTH and key in {"Intuition", "Related concepts"}:
            errors.append(f"{key!r} must stay canonical on a result-depth page")
        if title and kind == "distribution" and key in {"Definition", "Related distributions", "Statistical inference"}:
            errors.append(f"distribution heading {key!r} must stay canonical")
    if len(keys) != len(set(keys)):
        errors.append("repeated section")
    if not any(title for _, title, _ in secs):
        errors.append("no topic-specific heading (Key — Display title)")
    for key, title, _ in secs:
        if title and not re.search(rf"(?m)^## {re.escape(title)} \{{#[^}}]+\}}$", body):
            errors.append(f"display heading {title!r} does not render")

    for heading in ("Motivating example", "Worked example", "Check yourself"):
        if f"## {heading}\n" not in raw:
            errors.append(f"missing ## {heading}")
    if "## Worked example\n" in raw:
        worked = raw.split("## Worked example\n", 1)[1].split("\n## ", 1)[0]
        if "**Your turn.**" not in worked:
            errors.append("Worked example lacks a **Your turn.** prompt")
        if 'collapse="true"' not in worked:
            errors.append("Your turn answer is not hidden")
    if "## Check yourself {#check-yourself}" not in body:
        errors.append("Check yourself does not render")
    else:
        check = body.split("## Check yourself {#check-yourself}", 1)[1].split("\n## ", 1)[0]
        questions = re.findall(r"(?m)^### ", check)
        answers = check.count('collapse="true" title="Answer"')
        if len(questions) not in (2, 3):
            errors.append(f"Check yourself has {len(questions)} questions; need 2–3")
        if answers != len(questions):
            errors.append(f"Check yourself has {answers} hidden answers for {len(questions)} questions")

    lead = dict((k, t) for k, _, t in secs).get("Lead context", "")
    if re.search(r"\$|\\\(|\\\[|\*\*", lead):
        errors.append("Lead context has mathematics or bold text")

    for match in EDITOR_WORDS.finditer(raw):
        errors.append(f"editor wording {match.group(0)!r} in research content")
    match = EDITOR_TEST.search(body)
    if match:
        errors.append(f"editor wording {match.group(0)!r} in the generated page")

    for match in re.finditer(r"\{\{cite:([^}]+)\}\}", raw):
        for key in (k.strip() for k in match.group(1).split(",")):
            if key not in works:
                errors.append(f"unknown citation key {key}")
            if key == "dodge2008":
                errors.append("dodge2008 cited although the Dodge source was not read in this pass")
        after = raw[match.end():match.end() + 80]
        if not LOCATION.match(after):
            errors.append(f"citation without a location: {match.group(0)}{after[:30]!r}")
        if re.match(r"\s*\([^)]*(?:Abstract|abstract|publisher (?:contents|summary|record)|lecture notes)", after):
            errors.append(f"abstract or publisher listing cited: {match.group(0)}")

    for target in re.findall(r"\]\(([^)#\s]+\.qmd)(?:#[^)]*)?\)", raw):
        if not (article_path.parent / target).resolve().is_file():
            errors.append(f"broken link {target}")

    if "Statistical use" in keys and "Assumptions and limits" in keys:
        warnings.append("both 'Statistical use' and 'Assumptions and limits' present; check the page is not a stock skeleton")
    words = prose_words(body)
    floor = baseline.get(slug, {}).get("words", 0)
    if words < floor:
        errors.append(f"{words} words is below the baseline {floor}")

    check_path = ROOT / "checks" / f"{slug}.py"
    if not check_path.is_file():
        errors.append(f"no checks/{slug}.py")
    else:
        source = check_path.read_text(encoding="utf-8")
        if '"articles"' not in source and "articles/" not in source:
            errors.append("check script does not read its generated article")
        if run_checks:
            run = subprocess.run([sys.executable, str(check_path)], cwd=ROOT, capture_output=True, text=True)
            if run.returncode:
                errors.append(f"check script failed: {(run.stdout + run.stderr).strip()[-300:]}")

    pending_path = ROOT / "research" / "pending" / f"{slug}.json"
    if not pending_path.is_file():
        errors.append(f"no research/pending/{slug}.json")
    else:
        pending = json.loads(pending_path.read_text(encoding="utf-8"))
        extra = set(pending) - PENDING_KEYS
        if extra:
            errors.append(f"pending file has unknown keys {sorted(extra)}")
        if pending.get("slug") != slug or pending.get("rank") != rank:
            errors.append("pending slug or rank does not match the ranking")
        if set(pending.get("article_leads") or {}) - {slug}:
            errors.append("pending article_leads names another slug")
    if not (ROOT / "research" / f"{slug}.md").is_file():
        errors.append(f"no research/{slug}.md log")
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ranks", required=True, help="rank range such as 368-382")
    parser.add_argument("--slugs", help="comma-separated subset of the range")
    parser.add_argument("--run-checks", action="store_true", help="also run each checks/<slug>.py")
    args = parser.parse_args(argv)
    ranking = json.loads((ROOT / "research" / "ranking.json").read_text(encoding="utf-8"))
    works = json.loads((ROOT / "bibliography.json").read_text(encoding="utf-8"))["works"]
    baseline = json.loads((ROOT / "research" / "baseline.json").read_text(encoding="utf-8"))
    low, _, high = args.ranks.partition("-")
    only = set(args.slugs.split(",")) if args.slugs else None
    failed = 0
    for rank, row in enumerate(ranking, start=1):
        if not int(low) <= rank <= int(high or low) or (only and row["slug"] not in only):
            continue
        errors, warnings = check_page(rank, row["slug"], works, baseline, args.run_checks)
        status = "FAIL" if errors else "ok"
        print(f"{rank} {row['slug']}: {status}")
        for error in errors:
            print(f"    error: {error}")
        for warning in warnings:
            print(f"    warning: {warning}")
        failed += bool(errors)
    print(f"{failed} page(s) with errors")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
