# Instruction routing review — 2026-09-15

Static review of the final instructions, not autonomous-task benchmark results. No rows are added
to results.csv for this review. Source/tests and explicit contracts remain authoritative.

| Scenario | Route | Material not loaded by default |
| --- | --- | --- |
| Fix a small typo in meteorology | WORKSPACE → meteorology AGENTS → target prose; check reference/diff | Infrastructure, architecture, scientific skills, graph |
| Change distance attenuation in viewshed | WORKSPACE → viewshed AGENTS → scientific-change + methodology; data-contract-change for changed scientific hash; validation | Regional-run unless executing a regional workflow |
| Rename widely used pipeline function | Owning AGENTS → architecture → Graphify explain/callers → references/source/tests; viewshed validation and pipeline-safety if orchestration changes | Broad graph dump, unrelated scientific prose |
| Change a product consumed by another toolkit | WORKSPACE → consumer contract + INFRASTRUCTURE → both AGENTS → producer graph/contracts; affected repo validation | Sibling private implementation imports |
| Find all functions matching a syntax pattern | Owner → ast-grep CLI scoped to source; rg + inspection fallback when unavailable | Graph rebuild, syntax MCP server |
| Find literal config key | Owner → rg -n -F → necessary surrounding source/config | Serena, broad graph query |
| Documentation-only scientific contract change | Owner → relevant scientific/product skill/docs → reference/diff checks | Package suite unless behavior/check requirements also change |
| Add regression test in viewshed | Owner → validation skill → relevant source/test contract | Regional execution |

## Ambiguities resolved

- Starting at MarineCast does not imply descendant skill discovery. Repo AGENTS explicitly links
  skill files for manual loading; standalone clones still carry all local skills.
- Graphify's installed global skill says to query immediately; toolkit navigation prefers explain
  for known symbols. Local scope/progressive routing governs ordinary navigation; an explicit user
  request for a query still wins. The global skill was not modified.
- Missing/stale graph coverage falls back to targeted search. A question does not trigger extraction.
- `affected --relation calls --depth 1` follows callers. A successful no-match result is not proof
  of no usage: DomainBuildStage returned none in the local smoke check; inspect references/source
  for constructors or dynamic use before making a rename claim.
- Prose edits that change scientific contracts trigger the corresponding skill; typos do not.
- Ordinary changes load architecture only for ownership/import decisions, not merely because the
  repository has an architecture document.

## Safeguard preservation map

Viewshed's prior long AGENTS sections were moved or retained as follows:

| Prior guidance | Current owner |
| --- | --- |
| Scope, shared boundaries, public API/architecture constraints | AGENTS |
| Distance attenuation, independent distance, viewability meanings | AGENTS core + scientific-change detail |
| Config validation, parity, read-only loading, hashes, keys, joins, atomic writes, provenance | data-contract-change |
| Workflow distinctions, containment, promotion, rollback, manifest identity | pipeline-safety |
| Environment, data availability, regional case-study location/history | regional-run |
| Focused tests, Ruff/Black/mypy/compile, conditional component CI, numerical edge cases, historical evidence | validation |
| Per-repo checks, actual-vs-unrun reporting, no generated staging | AGENTS completion + validation detail |

Other toolkit domain and implementation-boundary sections were preserved. Their existing docs
remain the specialized guidance; no placeholder skills were added. Infrastructure, architecture,
scientific documents and producer code were not rewritten. Scaffolds remain unchanged.

## Remaining empirical checks

Confirm skill discovery in a fresh toolkit-scoped Codex task and manual routing in a fresh
workspace-root task. Collect roughly 20 real tasks to evaluate actual context, correction rate
and time. Static routing and smaller instruction files do not prove token or latency savings.
