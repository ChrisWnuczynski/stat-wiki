"""Rank generated concept pages by substantive incoming links and question use.

Run from the repository root after build_wiki.py. Navigation, infoboxes,
references, and copied question text are omitted from incoming-link counts.
Question use is read from the generator's unique-question count on each page.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
ARTICLE_DIR = ROOT / "articles"
PAGE_DIRS = ("articles", "notes", "reference", "labs")
LINK = re.compile(r"\]\(([^)\s]+\.qmd)(?:#[^)]*)?\)")
QUESTION_COUNT = re.compile(r"\*\*Questions? that uses? it\*\* \((\d+)\)")


def substantive_text(body: str) -> str:
    body = re.sub(r"\A---\n.*?\n---\n", "", body, count=1, flags=re.S)
    body = re.sub(r"(?ms)^:::: \{\.infobox\}.*?^::::\s*", "", body)
    body = re.sub(r"(?ms)^::: \{\.hatnote\}.*?^:::\s*", "", body)
    body = re.sub(r"(?ms)^## (?:See also|References|Used in)\b.*?(?=^## |\Z)", "", body)
    body = re.sub(r"(?ms)^```\{=html\}.*?^```\s*", "", body)
    body = re.sub(r"(?ms)^::: \{\.mainarticle\}.*?^:::\s*", "", body)
    return body


def main() -> None:
    pages = sorted(ARTICLE_DIR.glob("*.qmd"))
    targets = {page.resolve(): page.stem for page in pages}
    incoming: dict[str, set[Path]] = defaultdict(set)
    for dirname in PAGE_DIRS:
        for source in (ROOT / dirname).rglob("*.qmd"):
            body = substantive_text(source.read_text(encoding="utf-8"))
            for relative in LINK.findall(body):
                target = (source.parent / unquote(relative)).resolve()
                slug = targets.get(target)
                if slug and source.resolve() != target:
                    incoming[slug].add(source.relative_to(ROOT))

    rows = []
    for page in pages:
        body = page.read_text(encoding="utf-8")
        title = re.search(r'^title:\s*"(.*?)"$', body, flags=re.M)
        match = QUESTION_COUNT.search(body)
        questions = int(match.group(1)) if match else 0
        links = len(incoming[page.stem])
        rows.append({"slug": page.stem, "title": title.group(1) if title else page.stem,
                     "incoming": links, "questions": questions, "score": links + questions})
    rows.sort(key=lambda row: (-row["score"], -row["incoming"], row["slug"]))

    lines = ["# Concept-page research order", "",
             "Score = distinct incoming substantive wiki pages + distinct practice questions using the article.",
             "Question pages, automatic navigation, infoboxes, references, and copied question excerpts do not add incoming-link counts.", "",
             "| Rank | Article | Incoming | Questions | Score |", "|--:|:--|--:|--:|--:|"]
    for rank, row in enumerate(rows, 1):
        lines.append(f"| {rank} | [{row['title']}](../articles/{row['slug']}.qmd) | {row['incoming']} | {row['questions']} | {row['score']} |")
    (ROOT / "research" / "RANKING.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "research" / "ranking.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Ranked {len(rows)} concept pages")
    for rank, row in enumerate(rows[:30], 1):
        print(f"{rank:3}  {row['slug']:52} {row['incoming']:3} incoming + {row['questions']:2} questions = {row['score']:3}")


if __name__ == "__main__":
    main()
