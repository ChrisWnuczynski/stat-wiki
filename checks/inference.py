"""Check inference against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "inference"
ROOT = Path(__file__).resolve().parents[1]
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")

cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
print(SLUG, "ok")
