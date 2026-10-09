# Selective code navigation

Use this guide for tool setup or navigation-policy changes, not as a prerequisite for every task.
Identify the owning checkout first (the local MarineCast `WORKSPACE.yaml` is a routing index).
Load that repository's AGENTS and only the applicable skills/architecture sections. Cross-repository
contracts remain in [INFRASTRUCTURE.md](../INFRASTRUCTURE.md).

| Need | First tool | Retrieve next |
| --- | --- | --- |
| Known symbol, callers, imports, dependencies, blast radius | Scoped source search, or existing fresh Graphify `explain` when relationships need exploration | Identified symbol bodies and relevant tests |
| Unknown owner/module within one checkout | Static ownership map, then scoped search or narrow existing-graph `query` | Matching symbols, not entire neighborhoods |
| Repeated syntax, call shapes, codemod candidates | ast-grep CLI | Matches within candidate directories |
| Literal config key, string, filename or prose | `rg -n -F` / `rg --files` | Matching lines plus necessary context |
| Semantic references or symbol editing in pilot | Optional Serena, viewshed only | Relevant references/body; verify against source/tests |
| Context footprint | Repomix audit or metadata-only inventory | Counts and paths, never repository dumps |

Do not add a source-code vector store or a second persistent graph. Documentation and scientific
contracts remain intact; selective loading, rather than deletion, is the optimization.

## Graphify: verified local CLI, 2026-09-15

Identify the installed CLI/version and owning toolkit first. Before using an existing graph,
check its manifest against task-relevant source paths and changes. Missing/new paths or changed
content require source fallback; matching mtimes alone do not prove freshness. Record revision,
dirty state, extraction mode/version and exclusions when available. Graph/report/HTML sidecars
may have different dates; use only evidence current for the task. A routing availability flag is
not a freshness guarantee. Do not rebuild merely to answer a question.

Run inside the owning toolkit, using its existing graph when coverage is adequate:

```sh
graphify explain "normalize_tides"
graphify affected "normalize_tides" --relation calls --depth 1
graphify query "normalize_tides" --context call --budget 1500
```

`affected` reverses the selected relation: `calls` finds callers, not callees. `explain` displays
immediate connections and direction. Query context uses singular `call`; edge relation uses
plural `calls`. The filtered query is an optional expansion after `explain`. For an unknown module, choose a
discriminating graph term and follow the results.
Do not compensate for a large/truncated result by automatically increasing the budget.

Checked `graphify --help`, `query --help`, `explain --help`, and `affected --help`. In this installed
version the subcommand help forms do not provide dedicated help: query/explain can treat `--help`
as a search term and try to open the default graph, while affected refers back to global help.
Use global help as the CLI syntax reference. The earlier broad oceanography query exceeded its
requested budget; the budget is not a reliable hard limit.

Install Graphify only in an isolated developer environment (`graphifyy==0.9.62`), separate from
runtime dependencies. A shell can invoke its absolute executable without activating that environment.
The local workspace AGENTS records the existing machine-specific installation. Only for an explicitly requested build/refresh after
structural changes settle, use `graphify extract . --code-only --no-cluster` inside that repository.
Never run it at the workspace/grouping root. Never commit caches or enable installation hooks implicitly.
A question/build request does not implicitly authorize installation or upgrade. The global skill's
navigation entry point should load only existing-index guidance; semantic extraction and export
recipes belong behind explicit requests. Keep AST-only omissions and dynamic-reference limits
visible and verify source/tests, especially after no-match results.

This CLI can write query logs and cache stamps during query/explain/path. For a strictly read-only
audit inspect JSON directly, or use an isolated copy when within scope. Do not save feedback,
reflect or change learning overlays implicitly. Graph size/extraction counters are not task token
telemetry; collect actual time/read/token evidence using [agent evaluations](../agent-evals/README.md)
before claiming savings.

## Syntax-aware search: optional ast-grep CLI

Neither `ast-grep` nor `sg` was on the inspected PATH. No installation was performed. On macOS:

```sh
brew install ast-grep
ast-grep --version
ast-grep run --help
# From the relevant checkout; narrow src/path before searching.
ast-grep run --lang python --pattern 'normalize_tides($$$ARGS)' src/oceanography
ast-grep run --lang python --kind function_definition src/oceanography
```

Single quotes protect `$` metavariables from shell expansion. These examples follow the upstream
[installation guide](https://ast-grep.github.io/guide/quick-start) and
[CLI reference](https://ast-grep.github.io/reference/cli/run); they were not executed locally.
Prefer the full `ast-grep` executable name to avoid `sg` command-name collisions. If unavailable,
use scoped `rg` plus source inspection and report that syntax matching was not performed. Review
matches before any rewrite; syntax matches do not prove semantic equivalence. No MCP server or
Python runtime dependency is required.

## Literal search and source retrieval

```sh
rg --files src tests -g '*tide*'
rg -n -F 'TIDE_HOURLY_RANGE_M' src/oceanography tests
sed -n '119,145p' src/oceanography/build.py
```

The last range is an example from the current graph; recheck source locations after edits. Expand
reads when correctness needs context. Do not impose an arbitrary file-count cap on an unresolved bug.

## Skill discovery from a parent workspace

[Codex's skill documentation](https://developers.openai.com/codex/skills/) describes discovery from
CWD upward to the repository root, not recursive discovery of nested repositories. Therefore a
workspace-root task explicitly reads the skill path linked in the selected toolkit's AGENTS.
Starting Codex inside the toolkit enables normal repository skill discovery; changing a shell's
working directory in an existing task is not evidence of re-discovery. No root skill copies or
symlink farm is needed. End-to-end discovery in a new app task remains an empirical check.
