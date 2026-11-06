# Publish local edits to the wiki: commit everything here and push it to GitHub.
# GitHub then rebuilds https://chriswnuczynski.github.io/stat-wiki/
# (about 4 minutes; progress at https://github.com/ChrisWnuczynski/stat-wiki/actions).
#
#   powershell -ExecutionPolicy Bypass -File publish.ps1 "What changed"
#
# Building locally first is optional. It only checks pages here and refreshes
# the desktop app: python build_wiki.py, then quarto render.

param([string]$Message = "Update the wiki")

# git reports progress on stderr, so failures are read from exit codes instead.
$ErrorActionPreference = "Continue"
Set-Location $PSScriptRoot

git add -A
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
  git commit -q -m $Message
  if ($LASTEXITCODE -ne 0) { throw "Commit failed." }
}

# Bring in edits made on GitHub or another device, then push.
git pull --rebase -q
if ($LASTEXITCODE -ne 0) { throw "Your edits and the GitHub edits touch the same lines. Ask Claude to sort out the rebase." }

$ahead = git rev-list --count "@{u}..HEAD"
if ($ahead -eq "0") { "Nothing new to publish."; exit 0 }
git push -q
if ($LASTEXITCODE -ne 0) { throw "Push failed." }
"Pushed. GitHub is rebuilding the site: https://github.com/ChrisWnuczynski/stat-wiki/actions"
