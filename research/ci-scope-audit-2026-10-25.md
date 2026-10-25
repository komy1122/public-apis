# Catalogue and research CI boundaries

The failed README check for PR #1 at 35c219b did not originate in the new API registry. The PR changed five research/CI files and no README lines. Running the existing format validator on the branch and origin/master produced the same 634 diagnostic messages.

The legacy full-catalogue validator must not treat an unrelated research-only PR as a new catalogue failure. The workflow now checks the git diff before validating README/links. README changes or changes to scripts/validate or scripts/github_pull_request.sh still require full catalogue validation. Missing initial base or manual dispatch also requires full validation. Invalid revisions fail rather than silently skip.

The independent research/api_registry.json check remains required for its own changes. Catalogue validator unit tests also remain in their existing workflow. No catalogue error is ignored within the validator, and no README entry is rewritten by this fix. The inherited 634 catalogue diagnostics remain technical debt; passing a research-only PR does not mean the catalogue is clean or its API endpoints were tested live.

Regression coverage uses real temporary Git repositories to exercise research-only, README, validator and invalid-base cases. No provider API calls or secrets are used.
