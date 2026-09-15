# Organization documentation agent guidance

## Scope and required reading

This repository maintains the MarineCast organization profile and shared ecosystem documentation.
Read [INFRASTRUCTURE.md](INFRASTRUCTURE.md) before changing architecture or repository descriptions.
This `AGENTS.md` applies to this checkout; it does not automatically govern other MarineCast repositories.

## Ownership

- `profile/README.md`: public GitHub organization overview, toolkit directory, and project status.
- `INFRASTRUCTURE.md`: current repository responsibilities, intended integration contracts, and
  operational boundaries for work across repositories.
- `README.md`: entry point explaining this documentation repository.
- `AGENTS.md`: instructions for maintaining these documents.

## Editing contracts

- Verify names against the target repositories or their configured remotes. Use `toolkit-<domain>`
  repository names; do not confuse them with Python distribution names such as `viewshed-toolkit`.
- Distinguish observed implementation from planned capabilities. A repository's existence is not
  evidence that a data pipeline, deployment, or public release works.
- Keep the public profile concise. Put detailed cross-repository contracts in `INFRASTRUCTURE.md`
  and implementation commands in the owning toolkit's documentation.
- Preserve toolkit-specific scientific contracts. Do not present a proposed shared schema as an
  implemented standard, or copy viewshed-specific pair keys into unrelated domains.
- Keep workstation paths, credentials, restricted source data, and local generated artifacts out
  of public organization documentation.
- When responsibilities or repository names change, update the profile and infrastructure guide
  together, and identify affected toolkit instructions. Do not move or rename repositories merely
  to make documentation match an intended design.

## Validation and handoff

Run `git status --short`, inspect the diff, and run `git diff --check` from this repository.
Check local relative links and verify repository links against remotes or live metadata. State
whether remote availability was checked. No Python tests or regional pipelines are needed for
prose-only changes. Preserve unrelated modifications and report publishing separately from local edits.
