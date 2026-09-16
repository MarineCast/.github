# Serena pilot proposal: viewshed only

Status (2026-09-15): documentation prepared; no Serena server, project configuration, hooks or
machine-wide installation added. Neither `serena` nor `uv` was on the inspected PATH. Toolkit
correctness and validation remain independent of this tool.

## Hypothesis and overlap

Serena offers language-server symbol lookup, references and symbol-level edits. It could reduce
source reads for a widely used pipeline function or a narrow method change. Graphify already
provides structural relationships and blast-radius navigation; ast-grep matches syntax shapes;
`rg` finds literal values. Serena must show incremental benefit, not merely duplicate those tools.
See the upstream [overview](https://oraios.github.io/serena/01-about/000_intro.html).

Viewshed is the first candidate because it has layered orchestration, public facades and existing
architecture tests. Begin with definition/reference lookup; try edits only on an isolated branch
with a clean baseline. Confirm the Python language server can resolve the src layout and project
interpreter; unresolved geospatial imports must not be mistaken for absent references.

## Opt-in setup, not executed

Prerequisites: Git, Codex CLI, and `uv` with Python 3.13 available (uvx may download it). An operator
may install uv with `brew install uv`. Clone Serena into an isolated tools directory and record its
revision before comparing runs. This avoids silently changing versions mid-pilot:

```sh
# Choose a new tools directory outside all toolkit checkouts.
git clone https://github.com/oraios/serena /path/to/tools/serena
git -C /path/to/tools/serena rev-parse HEAD
uv run --directory /path/to/tools/serena serena start-mcp-server --help
cd /path/to/MarineCast/Toolkits/toolkit-viewshed
codex \
  -c 'mcp_servers.serena.command="uv"' \
  -c 'mcp_servers.serena.args=["run","--directory","/path/to/tools/serena","serena","start-mcp-server","--project","/path/to/MarineCast/Toolkits/toolkit-viewshed","--context","codex","--open-web-dashboard","false"]' \
  -c 'mcp_servers.serena.startup_timeout_sec=120'
```

Replace all `/path/to` placeholders. `-c` is a session override verified in local `codex --help`;
no shared config is edited. The upstream [running guide](https://oraios.github.io/serena/02-usage/020_running.html)
supports the source-clone launch and explicit project selection; its
[Codex integration guide](https://oraios.github.io/serena/02-usage/030_clients.html) specifies the
`codex` context and `/mcp` connection check. Actual startup/language-server resolution was not tested.
Keep any generated `.serena` caches local; inspect and locally exclude them before a pilot commit.
Do not enable global setup commands, reminders or hooks for this experiment.

## Evaluation and removal

Use [agent-evals](../agent-evals/README.md) with matched tasks/revisions and fixed model/effort.
Record cold startup/index time separately from warm navigation. Measure unique source files read
before a correct result, searches, tool calls, tokens when available, wall time, corrections and
missed references. Include find-callers, rename, and targeted bug-fix cases, then repeat without Serena.

Proposed decision rule (not a measured benefit): retain only if at least five matched pairs show
lower median source reads with no correctness loss and tolerable startup cost. Remove the pilot
if references are unreliable, edits broaden unexpectedly, tool choice becomes ambiguous, or overhead
outweighs retrieval savings. Stop the session and restart without the override; review/remove only
pilot-created configuration/cache files. Never delete unrelated settings or graph caches. Expansion
to other toolkits requires evidence and a separate decision.
