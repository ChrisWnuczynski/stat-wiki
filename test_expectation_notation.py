"""The expectation-notation guard catches new maths and ignores the backlog."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import expectation_notation

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "checks" / "expectation-notation.py"


def _hits(source: str) -> list[expectation_notation.Violation]:
    return expectation_notation.find_violations(source)


def _flagged(source: str) -> bool:
    return bool(_hits(source))


class FormTests(unittest.TestCase):
    def test_mathrm_is_caught(self) -> None:
        hits = _hits(r"The mean is $\mathrm{E}(X)$.")
        self.assertEqual(len(hits), 1)
        self.assertIn(r"\mathrm{E}", hits[0].snippet)
        self.assertIn(r"\E", hits[0].message("research/content/sample.md"))
        self.assertIn("research/content/sample.md:1:", hits[0].message("research/content/sample.md"))

    def test_operatorname_is_caught(self) -> None:
        hits = _hits(r"$$\operatorname{E}[X]$$")
        self.assertEqual(len(hits), 1)
        self.assertIn(r"\operatorname{E}", hits[0].snippet)
        starred = _hits(r"$\operatorname*{E}(X)$")
        self.assertEqual(len(starred), 1)

    def test_bare_call_bracket_and_juxtaposition_are_caught(self) -> None:
        for source in (
            r"$E(X)$",
            r"$E[X]$",
            r"$E X$",
            r"$EX$",
            r"$E|X|$",
            r"$E\{X\}$",
            r"$E_\theta(X)$",
            r"$E_q[h(X)]$",
            r"$E\,\log X$",
            r"$E \left(X\right)$",
        ):
            with self.subTest(source=source):
                self.assertTrue(_flagged(source), source)

    def test_quantity_names_pass(self) -> None:
        for source in (
            r"$E_i$",
            r"$E_{ij}$",
            r"$E_{i+}$",
            r"$(O_i-E_i)^2/E_i$",
            r"$E_i^2$",
            r"$E_i(w)$",
            r"$E_I(w)$",
            r"$|E|\log p$",
            r"$SS_E$",
            r"$p_E$",
            r"$E=\sum_j E_j$",
            r"$E_t=f_t(x)$",
            r"$EBIC$",
            r"$ELBO$",
        ):
            with self.subTest(source=source):
                self.assertFalse(_flagged(source), source)

    def test_shorthand_and_blackboard_pass(self) -> None:
        for source in (
            r"$\E(X)$",
            r"$\E[X]$",
            r"$\E X$",
            r"$\mathbb{E}(X)$",
            r"$\mathbb E(X)$",
            r"$\E_\theta(X)$",
            r"$\mathbb EX$",
            r"$\mathbb EX^2$",
            r"$\mathcal E=\{\delta\}$",
        ):
            with self.subTest(source=source):
                self.assertFalse(_flagged(source), source)

    def test_loss_named_e_is_reported_because_it_matches_the_operator(self) -> None:
        # A function named E is not distinguished from expectation. Documented rule.
        hits = _hits(r"$E(w)=(w-3)^2$")
        self.assertEqual(len(hits), 1)
        self.assertIn(r"\E", hits[0].message("labs/sample.qmd"))

    def test_other_delimiters_and_display_lines(self) -> None:
        display = "$$\nE(W)=\\frac{n(N+1)}{2}.\n$$"
        hits = _hits(display)
        self.assertEqual([item.line for item in hits], [2])
        self.assertTrue(_flagged(r"See \(E(X)\) and \[E[Y]\]."))
        equation = "\\begin{equation}\nE(X)=\\mu.\n\\end{equation}"
        self.assertEqual([item.line for item in _hits(equation)], [2])

    def test_code_and_prose_are_not_maths(self) -> None:
        self.assertFalse(_flagged("The symbol E(X) is not in maths."))
        self.assertFalse(_flagged("Use `$E(X)$` in code."))
        fenced = "```\n$E(X)$\n```\nThen $\\E(Y)$.\n"
        self.assertFalse(_flagged(fenced))

    def test_line_break_before_a_bare_e_is_still_bare(self) -> None:
        self.assertTrue(_flagged(r"$\\E(X)$"))
        self.assertFalse(_flagged(r"$\E(X)$"))

    def test_generated_articles_are_out_of_scope(self) -> None:
        self.assertFalse(expectation_notation.in_scope("articles/expectation.qmd"))
        self.assertFalse(expectation_notation.in_scope("sources/book/chapters/01.qmd"))
        self.assertTrue(expectation_notation.in_scope("research/content/expectation.md"))
        self.assertTrue(expectation_notation.in_scope("labs/kernel-density.qmd"))
        self.assertFalse(expectation_notation.in_scope("labs/kde-math.js"))


class DiffFilterTests(unittest.TestCase):
    def test_parser_keeps_added_lines_only(self) -> None:
        diff = "\n".join(
            [
                "diff --git a/research/content/old.md b/research/content/old.md",
                "--- a/research/content/old.md",
                "+++ b/research/content/old.md",
                "@@ -3,0 +4 @@",
                "+$E(X)$",
                "@@ -10 +11 @@",
                "-old",
                "+$E_i$",
                "diff --git a/articles/foo.qmd b/articles/foo.qmd",
                "--- a/articles/foo.qmd",
                "+++ b/articles/foo.qmd",
                "@@ -1 +1 @@",
                "-$E(X)$",
                "+$E(Y)$",
                "diff --git a/labs/demo.qmd b/labs/demo.qmd",
                "new file mode 100644",
                "--- /dev/null",
                "+++ b/labs/demo.qmd",
                "@@ -0,0 +1,2 @@",
                "+# Lab",
                r"+$\operatorname{E}(X)$",
                "",
            ]
        )
        added = expectation_notation.parse_added_lines(diff)
        self.assertEqual(added["research/content/old.md"], {4, 11})
        self.assertEqual(added["articles/foo.qmd"], {1})
        self.assertEqual(added["labs/demo.qmd"], {1, 2})

    def test_untouched_formula_survives_a_prose_edit(self) -> None:
        old = "Intro.\nBacklog $E(X)$ stays.\n"
        new = "A rewritten introduction.\nBacklog $E(X)$ stays.\n"
        self.assertEqual(expectation_notation.violations_in_changed_spans(old, new), [])
        changed = "Intro.\nBacklog $E(Y)$ stays.\n"
        fired = expectation_notation.violations_in_changed_spans(old, changed)
        self.assertEqual(len(fired), 1)
        self.assertEqual(fired[0].line, 2)
        self.assertIn(r"\E", fired[0].message("research/content/old.md"))

    def test_new_maths_region_flags_an_unchanged_operator_line(self) -> None:
        old = "See E(X) in the paragraph.\n"
        new = "$$\nSee E(X) in the paragraph.\n$$\n"
        fired = expectation_notation.violations_in_changed_spans(old, new)
        self.assertEqual([item.line for item in fired], [2])
        self.assertEqual(fired[0].block_first, 1)
        self.assertEqual(fired[0].block_last, 3)
        self.assertIn(r"\E", fired[0].message("research/content/old.md"))

    def test_argument_on_the_next_line_flags_a_bare_e(self) -> None:
        old = "$$\nE\n$$\n"
        new = "$$\nE\n[X]\n$$\n"
        fired = expectation_notation.violations_in_changed_spans(old, new)
        self.assertEqual([item.line for item in fired], [2])
        self.assertIn(r"\E", fired[0].message("research/content/old.md"))

    def test_unchanged_lab_shorthand_is_not_a_failure(self) -> None:
        text = (ROOT / "labs" / "kernel-density.qmd").read_text(encoding="utf-8")
        self.assertEqual(expectation_notation.violations_in_changed_spans(text, text), [])
        self.assertEqual(expectation_notation.violations_touching(text, set()), [])

    def test_real_expected_counts_page_has_no_hit(self) -> None:
        text = (ROOT / "research/content/observed-and-expected-counts.md").read_text(encoding="utf-8")
        self.assertEqual(_hits(text), [])

    def test_real_backlog_is_visible_but_silent_when_the_file_is_unchanged(self) -> None:
        backlog = 0
        for path in sorted((ROOT / "research" / "content").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            hits = _hits(text)
            backlog += len(hits)
            self.assertEqual(expectation_notation.violations_in_changed_spans(text, text), [])
        self.assertGreater(backlog, 0)


class GuardCliTests(unittest.TestCase):
    def test_each_form_fires_and_the_backlog_does_not(self) -> None:
        samples = {
            "mathrm": r"New $\mathrm{E}(X)$.",
            "operatorname": r"New $\operatorname{E}[Y]$.",
            "bare": r"New $E(Z)$.",
        }
        for kind, bad in samples.items():
            with self.subTest(kind=kind):
                with tempfile.TemporaryDirectory() as tmp:
                    repo = Path(tmp)
                    self._git(repo, ["init", "-b", "main"])
                    content = repo / "research" / "content"
                    content.mkdir(parents=True)
                    old = content / "old.md"
                    old.write_text(
                        "Backlog $E(X)$ and quantity $E_i$ and $E_{ij}$.\nSecond line.\n",
                        encoding="utf-8",
                    )
                    self._commit(repo, "base")
                    base = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
                    proc = self._run(repo, base)
                    self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
                    self.assertIn("no new non-standard", proc.stdout)

                    old.write_text(
                        "Backlog $E(X)$ and quantity $E_i$ and $E_{ij}$.\n"
                        "Edited prose only.\n",
                        encoding="utf-8",
                    )
                    proc = self._run(repo, base)
                    self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

                    old.write_text(
                        "Backlog $E(X)$ and quantity $E_i$ and $E_{ij}$.\n"
                        + bad
                        + "\n",
                        encoding="utf-8",
                    )
                    proc = self._run(repo, base)
                    self.assertEqual(proc.returncode, 1, proc.stdout + proc.stderr)
                    self.assertIn("research/content/old.md:2:", proc.stdout)
                    self.assertIn(r"\E", proc.stdout)

                    good = content / "new.md"
                    good.write_text("Fresh $\\E(X)$ and $E_i$ and $\\mathbb{E}[Y]$.\n", encoding="utf-8")
                    old.write_text(
                        "Backlog $E(X)$ and quantity $E_i$ and $E_{ij}$.\nSecond line.\n",
                        encoding="utf-8",
                    )
                    proc = self._run(repo, base)
                    self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_cli_flags_spans_that_touch_a_changed_line(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._git(repo, ["init", "-b", "main"])
            content = repo / "research" / "content"
            content.mkdir(parents=True)
            page = content / "old.md"
            page.write_text("See E(X) in the paragraph.\n", encoding="utf-8")
            self._commit(repo, "base")
            base = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
            page.write_text("$$\nSee E(X) in the paragraph.\n$$\n", encoding="utf-8")
            wrapped = self._run(repo, base)
            self.assertEqual(wrapped.returncode, 1, wrapped.stdout + wrapped.stderr)
            self.assertIn("research/content/old.md:2:", wrapped.stdout)

            page.write_text("$$\nE\n$$\n", encoding="utf-8")
            self._commit(repo, "display")
            base = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
            page.write_text("$$\nE\n[X]\n$$\n", encoding="utf-8")
            argument = self._run(repo, base)
            self.assertEqual(argument.returncode, 1, argument.stdout + argument.stderr)
            self.assertIn("research/content/old.md:2:", argument.stdout)

            page.write_text("Intro.\n$E(X)$ stays.\n", encoding="utf-8")
            self._commit(repo, "legacy")
            base = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
            page.write_text("Rewritten introduction.\n$E(X)$ stays.\n", encoding="utf-8")
            prose = self._run(repo, base)
            self.assertEqual(prose.returncode, 0, prose.stdout + prose.stderr)

            labs = repo / "labs"
            labs.mkdir()
            lab = labs / "kernel-density.qmd"
            lab.write_text((ROOT / "labs" / "kernel-density.qmd").read_text(encoding="utf-8"), encoding="utf-8")
            self._commit(repo, "lab")
            base = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
            lab_lines = lab.read_text(encoding="utf-8").splitlines()
            lab_lines[6] = "A rewritten opening sentence."
            lab.write_text("\n".join(lab_lines) + "\n", encoding="utf-8")
            edited = self._run(repo, base)
            self.assertEqual(edited.returncode, 0, edited.stdout + edited.stderr)

    def test_research_prose_is_expanded_before_it_is_copied(self) -> None:
        import build_wiki

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.md"
            path.write_text(
                "## Definition\nThe mean is $\\E(X)$, $\\Var(X)$, and $\\Pr(A)$.\n```\n\\E\n```\n",
                encoding="utf-8",
            )
            researched, _titles = build_wiki.read_research_content(path, {"Definition"})
        body = researched["Definition"]
        self.assertIn(r"\mathbb{E}(X)", body)
        self.assertIn(r"\operatorname{Var}(X)", body)
        self.assertIn(r"\Pr(A)", body)
        self.assertIn("```\n\\E\n```", body)

    def test_pull_request_diff_uses_the_merge_parent_when_the_base_moves(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._git(repo, ["init", "-b", "main"])
            content = repo / "research" / "content"
            content.mkdir(parents=True)
            page = content / "old.md"
            page.write_text("Backlog $E(X)$ stays.\n", encoding="utf-8")
            self._commit(repo, "base")
            old_base = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
            self._git(repo, ["checkout", "-b", "feature"])
            page.write_text("Backlog $E(X)$ stays.\nNew $\\mathrm{E}(Y)$.\n", encoding="utf-8")
            self._commit(repo, "add notation")
            feature = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
            self._git(repo, ["checkout", "main"])
            page.write_text("Main moved the backlog $E(X)$ line.\n", encoding="utf-8")
            self._commit(repo, "main moves")
            moved = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
            self._git(repo, ["checkout", "--detach", old_base])
            self._git(
                repo,
                [
                    "-c",
                    "user.email=expectation-guard@example.com",
                    "-c",
                    "user.name=Expectation Guard",
                    "merge",
                    "--no-ff",
                    feature,
                    "-m",
                    "merge",
                ],
            )
            proc = self._run(repo, moved, {"GITHUB_EVENT_NAME": "pull_request"})
            self.assertEqual(proc.returncode, 1, proc.stdout + proc.stderr)
            self.assertIn("research/content/old.md:2:", proc.stdout)
            self.assertNotIn("research/content/old.md:1:", proc.stdout)

    def test_missing_merge_base_still_flags_only_the_new_line(self) -> None:
        # A shallow checkout cannot compute a merge-base. The fallback diffs
        # the two trees, so an untouched backlog line still passes.
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._git(repo, ["init", "-b", "main"])
            content = repo / "research" / "content"
            content.mkdir(parents=True)
            page = content / "old.md"
            page.write_text("Backlog $E(X)$ stays.\n", encoding="utf-8")
            self._commit(repo, "base")
            base = self._git(repo, ["rev-parse", "HEAD"]).stdout.strip()
            self._git(repo, ["checkout", "--orphan", "side"])
            page.write_text("Backlog $E(X)$ stays.\nNew $\\mathrm{E}(Y)$.\n", encoding="utf-8")
            self._commit(repo, "unrelated")
            merged = subprocess.run(
                ["git", "merge-base", "HEAD", base],
                cwd=repo,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(merged.returncode, 0)
            proc = self._run(repo, base)
            self.assertEqual(proc.returncode, 1, proc.stdout + proc.stderr)
            self.assertIn("research/content/old.md:2:", proc.stdout)
            self.assertNotIn("research/content/old.md:1:", proc.stdout)
            self.assertIn(r"\E", proc.stdout)

    def test_checkout_adds_no_expectation_violation(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("no new non-standard", proc.stdout)

    def _run(
        self,
        repo: Path,
        base: str,
        extra: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        for key in ("GIT_DIR", "GIT_WORK_TREE", "GITHUB_BASE_REF", "GITHUB_EVENT_NAME"):
            env.pop(key, None)
        env["EXPECTATION_NOTATION_BASE"] = base
        if extra:
            env.update(extra)
        return subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=repo,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

    def _commit(self, repo: Path, message: str) -> None:
        self._git(repo, ["add", "."])
        self._git(
            repo,
            [
                "-c",
                "user.email=expectation-guard@example.com",
                "-c",
                "user.name=Expectation Guard",
                "commit",
                "-m",
                message,
            ],
        )

    def _git(self, repo: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True,
        )


if __name__ == "__main__":
    unittest.main()
