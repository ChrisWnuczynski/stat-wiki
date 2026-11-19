#!/usr/bin/env bash
# Download the published wiki.json once Pages is serving this deploy's copy.
#
# www.statwiki.io is GitHub Pages. The CDN caches wiki.json for about 10
# minutes (cache-control: max-age=600) and ignores a cache-busting query, so
# a fetch right after "Build and publish" can still be the previous file.
# The indexer is incremental: indexing that stale copy would record the old
# pages as up to date.
#
# PUBLISH_STARTED is the triggering publish run's start time. The build
# rewrites wiki.json during that run, and Pages reports that time as
# Last-Modified. Accept the body only when Last-Modified is at or after the
# run start. A manual workflow_dispatch leaves PUBLISH_STARTED empty and
# takes the file that is live now, which is the catch-up Chris runs by hand.
#
# The saved file is what the indexer reads. It does not fetch the URL again.

set -euo pipefail

url="${WIKI_URL:-https://www.statwiki.io/wiki.json}"
out="${WIKI_FILE:?Set WIKI_FILE to the path where wiki.json should be saved}"
started="${PUBLISH_STARTED:-}"
skew="${WAIT_SKEW_SECONDS:-0}"

if [[ -n "$started" ]]; then
  attempts="${WAIT_ATTEMPTS:-40}"
  delay="${WAIT_SECONDS:-20}"
else
  attempts="${WAIT_ATTEMPTS:-8}"
  delay="${WAIT_SECONDS:-15}"
fi

if [[ "${GITHUB_EVENT_NAME:-}" == "workflow_run" && -z "$started" ]]; then
  echo "::error::This run followed a publish but has no start time, so it cannot tell the new wiki.json from the cached one."
  exit 1
fi

header_value() {
  local name="$1" file="$2"
  awk -v name="$name" '
    BEGIN { IGNORECASE = 1 }
    {
      gsub(/\r/, "")
      key = tolower(name) ":"
      if (index(tolower($0), key) == 1) {
        value = $0
        sub(/^[^:]+:[ \t]*/, "", value)
      }
    }
    END { print value }
  ' "$file"
}

epoch_of() {
  date -u -d "$1" +%s
}

entry_count() {
  python3 - "$1" <<'PY'
import json
import sys
with open(sys.argv[1], encoding="utf-8") as handle:
    document = json.load(handle)
entries = document.get("entries")
version = document.get("version")
if not isinstance(version, int) or version < 1 or not isinstance(entries, list) or len(entries) == 0:
    raise SystemExit(1)
print(len(entries))
PY
}

mkdir -p "$(dirname "$out")"
headers="$(mktemp)"
trap 'rm -f "$headers"' EXIT

start_epoch=""
if [[ -n "$started" ]]; then
  start_epoch="$(epoch_of "$started")"
  echo "Waiting until ${url} was modified at or after ${started}."
else
  echo "Waiting for a usable ${url}."
fi

for ((attempt = 1; attempt <= attempts; attempt++)); do
  rm -f "$out"
  code="000"
  if ! code="$(curl -sS -L --max-time 120 -A "statwiki-ask-index" -D "$headers" -o "$out" -w "%{http_code}" "$url")"; then
    code="curl-failed"
  fi
  modified="$(header_value "last-modified" "$headers")"
  age="$(header_value "age" "$headers")"
  cache="$(header_value "x-cache" "$headers")"
  kind="$(header_value "content-type" "$headers")"
  echo "attempt ${attempt}/${attempts}: HTTP ${code} last-modified ${modified:-none} age ${age:-none} x-cache ${cache:-none}"

  fresh=1
  if [[ -n "$start_epoch" ]]; then
    fresh=0
    if [[ -n "$modified" ]]; then
      if modified_epoch="$(epoch_of "$modified")"; then
        if ((modified_epoch + skew >= start_epoch)); then
          fresh=1
        fi
      else
        echo "could not parse Last-Modified: ${modified}"
      fi
    fi
  fi

  if [[ "$code" == "200" && "$fresh" == "1" && "$kind" == *"json"* ]]; then
    if count="$(entry_count "$out")"; then
      echo "wiki.json is ready (${count} entries) -> ${out}"
      exit 0
    fi
    echo "response was not a usable wiki.json"
  fi
  rm -f "$out"

  if ((attempt < attempts)); then
    sleep "$delay"
  fi
done

if [[ -n "$started" ]]; then
  echo "::error::${url} was still older than this publish (started ${started}) after ${attempts} attempts, ${delay}s apart. Pages caches wiki.json for about 10 minutes. Re-run Index Ask StatWiki once Last-Modified is ${started} or later."
else
  echo "::error::${url} did not return a usable wiki.json after ${attempts} attempts, ${delay}s apart."
fi
exit 1
