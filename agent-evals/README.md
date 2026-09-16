# Lightweight agent performance evaluation

This is a manual evidence log, not a workspace test suite. `results.csv` starts with a header only.
Use [task-template.md](task-template.md) to record about 20 normal Codex tasks, ideally two examples
of each category below. Do not invent baseline results or infer billed token savings from file size.

Categories: targeted bug fix; trace pipeline; add feature; schema change; refactor; find callers;
blast-radius analysis; documentation-only change; test addition; cross-repository contract change.

## Collection protocol

1. Record repository revision(s), instruction revision, tooling versions, model/effort, task scope
   and acceptance criteria before work. Use independent checkouts/sessions for matched comparisons.
2. From the task transcript, collect every file path whose source content was shown (direct reads,
   search snippets and semantic tool bodies all count). Keep the ordered path list in task notes.
3. End the measurement at the first result that passes the acceptance checks and review. If later
   correction is needed, extend the interval and counts. Log failures too; do not select only wins.
4. Append one CSV row using a CSV writer. Quote descriptions and notes correctly. Leave unavailable
   fields empty, never use zero for unknown. Tool booleans and success use `true`/`false`/empty.
5. After roughly 20 tasks, compare medians and ranges within comparable categories and success
   rates. Report sample size and uncertainty. Observational tasks alone do not establish causality;
   use matched replay tasks when testing a tool decision.

Primary metric: `source_files_opened`, unique implementation/config source paths exposed before the
first correct implementation or accepted read-only answer. Tests are counted separately as
`test_files_opened`; instruction/docs as `instruction_doc_files_opened`. Count partial reads and
search snippets, but not filenames alone. Repeated reads affect tool calls and tokens, not unique
file count. For documentation-only tasks source count is usually zero; compare documentation reads
instead. Cross-repository tasks qualify paths with repository name and sum distinct paths.

`searches_run`: each executed rg/Graphify/ast-grep/reference-search operation, including no matches.
`tool_calls`: all API tool invocations, including failed ones; count underlying calls in an
orchestration batch separately, not the wrapper as another call. Retain the counting convention
in notes if a host exposes only partial telemetry. `wall_time_seconds`: task start to accepted
result; record user waits and cold indexing separately in notes. `corrections_required`: distinct
review/test failures requiring a revision. `tests_run`: exact command(s) and outcome, not a yes/no.
Token fields use actual host telemetry only; note model, cache accounting and scope. Never infer
them from word counts or quote an unavailable counter as zero. Link private transcript evidence
locally; do not commit private prompts, absolute workstation paths, data or credentials.

Useful comparisons: routing-only baseline versus optimized routing; Graphify versus optional Serena;
rg versus ast-grep for syntax tasks. Keep model, scientific acceptance and task difficulty comparable.
A shorter answer that misses scientific safeguards is a failure, regardless of token use.

## Supporting checks

- [Routing review](routing-review.md): static scenario checks, not measured agent performance.
- `python3 agent-evals/context_inventory.py /path/to/MarineCast`: metadata-only context audit;
  no packages required, source content is never printed. It does not estimate actual model tokens.

- `python agent-evals/validate_setup.py /path/to/MarineCast`: validate local routing, skill
  frontmatter, graph exclusions and relative links using a developer interpreter with PyYAML.
  This optional checker does not add a dependency to any toolkit or prove agent task performance.
