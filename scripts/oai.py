"""Send one prompt file to the OpenAI chat API and print the reply.

Usage:
    python scripts/oai.py PROMPT_FILE [--tier draft|review] [--model ID]
                          [--system FILE] [--json] [--tag LABEL] [--no-cache]
    python scripts/oai.py --usage

The key is read from OPENAI_API_KEY and is never printed. In a cloud session
whose network proxy adds the credential for api.openai.com, the variable may be
unset; a placeholder is then sent and the proxy replaces it.

Replies are cached in research/.oai-cache/ (or $STATWIKI_OAI_CACHE) by a hash of model, system text,
prompt and mode, and every live call appends its token counts to
research/.oai-cache/usage.jsonl. Nothing from this script should be committed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path(os.environ.get("STATWIKI_OAI_CACHE") or ROOT / "research" / ".oai-cache")
USAGE = CACHE / "usage.jsonl"
MODELS = {"draft": "gpt-5.4-mini", "review": "gpt-5.5"}
ENDPOINT = "https://api.openai.com/v1/chat/completions"


def call(model: str, system: str, prompt: str, as_json: bool, effort: str | None) -> tuple[str, dict]:
    key = os.environ.get("OPENAI_API_KEY") or "sk-placeholder-replaced-by-proxy"
    body: dict = {
        "model": model,
        "messages": ([{"role": "system", "content": system}] if system else [])
        + [{"role": "user", "content": prompt}],
    }
    if as_json:
        body["response_format"] = {"type": "json_object"}
    if effort:
        body["reasoning_effort"] = effort
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    last = ""
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=600) as response:
                data = json.loads(response.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"] or "", data.get("usage", {})
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400]
            last = f"HTTP {exc.code}: {detail}"
            if exc.code not in (429, 500, 502, 503, 504):
                break
        except (urllib.error.URLError, TimeoutError) as exc:
            last = f"network error: {exc}"
        time.sleep(2 ** attempt * 3)
    raise RuntimeError(last.replace(key, "<key>"))


def usage_summary() -> int:
    if not USAGE.is_file():
        print("No usage recorded.")
        return 0
    totals: dict[tuple[str, str], list[int]] = defaultdict(lambda: [0, 0, 0])
    for line in USAGE.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        cell = totals[(row.get("tag", ""), row["model"])]
        cell[0] += 1
        cell[1] += row.get("prompt_tokens", 0)
        cell[2] += row.get("completion_tokens", 0)
    print("tag\tmodel\tcalls\tprompt_tokens\tcompletion_tokens")
    for (tag, model), (calls, p, c) in sorted(totals.items()):
        print(f"{tag}\t{model}\t{calls}\t{p}\t{c}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("prompt_file", nargs="?")
    parser.add_argument("--tier", choices=sorted(MODELS), default="draft")
    parser.add_argument("--model", help="override the tier's model")
    parser.add_argument("--system", help="file with system instructions")
    parser.add_argument("--json", action="store_true", help="ask for a JSON object and validate it")
    parser.add_argument("--effort", choices=["minimal", "low", "medium", "high"], help="reasoning effort")
    parser.add_argument("--tag", default="", help="label for the usage log, such as a batch name")
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("--usage", action="store_true", help="print token totals by tag and model")
    args = parser.parse_args(argv)
    if args.usage:
        return usage_summary()
    if not args.prompt_file:
        parser.error("a prompt file is required")
    prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    system = Path(args.system).read_text(encoding="utf-8") if args.system else ""
    model = args.model or MODELS[args.tier]
    digest = hashlib.sha256(json.dumps([model, system, prompt, args.json, args.effort]).encode("utf-8")).hexdigest()
    CACHE.mkdir(parents=True, exist_ok=True)
    cached = CACHE / f"{digest}.txt"
    if cached.is_file() and not args.no_cache:
        print(cached.read_text(encoding="utf-8"))
        return 0
    try:
        text, usage = call(model, system, prompt, args.json, args.effort)
    except RuntimeError as exc:
        print(f"oai.py: request failed ({exc})", file=sys.stderr)
        return 2
    if args.json:
        try:
            json.loads(text)
        except json.JSONDecodeError:
            print("oai.py: reply was not valid JSON", file=sys.stderr)
            print(text)
            return 3
    cached.write_text(text, encoding="utf-8")
    with USAGE.open("a", encoding="utf-8") as log:
        log.write(json.dumps({"time": time.strftime("%Y-%m-%dT%H:%M:%S"), "tag": args.tag, "model": model,
                              "prompt_tokens": usage.get("prompt_tokens", 0),
                              "completion_tokens": usage.get("completion_tokens", 0)}) + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
