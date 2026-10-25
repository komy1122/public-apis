import subprocess
import os
import tempfile
import unittest
from pathlib import Path

from readme_scope import needs_readme_validation

SCRIPT = Path(__file__).resolve().parents[1] / "readme_scope.py"


class ReadmeScopeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.repo / "README.md").write_text("Catalogue\n", encoding="utf-8")
        self.commit()
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.repo, text=True)

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")

    def test_research_only_change_does_not_run_catalogue_validation(self):
        (self.repo / "research").mkdir()
        (self.repo / "research" / "api_registry.json").write_text("{}", encoding="utf-8")
        self.commit()
        self.assertFalse(needs_readme_validation(self.base, "HEAD", cwd=self.repo))

    def test_readme_change_runs_catalogue_validation(self):
        (self.repo / "README.md").write_text("Changed catalogue\n", encoding="utf-8")
        self.commit()
        self.assertTrue(needs_readme_validation(self.base, "HEAD", cwd=self.repo))

    def test_validator_change_runs_catalogue_validation(self):
        target = self.repo / "scripts" / "validate"
        target.mkdir(parents=True)
        (target / "format.py").write_text("# changed validator\n", encoding="utf-8")
        self.commit()
        self.assertTrue(needs_readme_validation(self.base, "HEAD", cwd=self.repo))

    def test_missing_base_requires_full_validation(self):
        self.assertTrue(needs_readme_validation("", "HEAD", cwd=self.repo))

    def test_invalid_revision_is_not_silently_skipped(self):
        with self.assertRaises(subprocess.CalledProcessError):
            needs_readme_validation("not-a-revision", "HEAD", cwd=self.repo)

    def test_manual_dispatch_forces_validation_and_writes_output(self):
        output = self.repo / "output.txt"
        summary = self.repo / "summary.txt"
        env = dict(os.environ, GITHUB_EVENT_NAME="workflow_dispatch", BASE_SHA=self.base,
                   HEAD_SHA=self.base, GITHUB_OUTPUT=str(output), GITHUB_STEP_SUMMARY=str(summary))
        subprocess.run([os.sys.executable, str(SCRIPT)], cwd=self.repo, env=env,
                       check=True, capture_output=True, text=True)
        self.assertEqual(output.read_text(encoding="utf-8"), "required=true\n")
        self.assertFalse(summary.exists())
