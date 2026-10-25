"""Scope catalogue checks to catalogue/validator changes, not research assets."""
import os
from pathlib import Path
import subprocess


def needs_readme_validation(base, head, cwd=None):
    if not base or set(base) == {"0"}:
        return True
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", base, head, "--", "README.md",
         "scripts/validate", "scripts/github_pull_request.sh"],
        cwd=cwd, text=True,
    )
    return bool(changed.strip())


if __name__ == "__main__":
    manual = os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch"
    required = manual or needs_readme_validation(
        os.environ.get("BASE_SHA", ""), os.environ.get("HEAD_SHA", "HEAD")
    )
    value = str(required).lower()
    if os.environ.get("GITHUB_OUTPUT"):
        with Path(os.environ["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as stream:
            stream.write(f"required={value}\n")
    print(f"Catalogue validation required: {value}")
    if not required:
        print("README and its validators are unchanged. Research registry has its own offline check.")
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a", encoding="utf-8") as stream:
                stream.write("README and catalogue validators unchanged; catalogue checks are not applicable. "
                             "Research registry is checked separately. Inherited README errors remain unresolved.\n")
