# Future code-graph comparison

Graphify remains the only persistent code graph. No alternative, including codebase-memory-mcp,
is installed or configured by this pass. Compare an alternative only when a concrete Graphify
limitation affects representative work; do not add overlapping retrieval infrastructure by default.

Use isolated checkouts at the same revisions, identical prompts and acceptance checks, and fixed
model/effort. Compare known-symbol lookup, callers, pipeline tracing, import/blast-radius analysis,
and post-rename freshness. Count tool setup, refresh/index cost and context overhead as well as
navigation. Include dynamic dispatch and ambiguous names; adjudicate against source/tests, not one
graph's output. Keep source and reproducible settings shareable, generated graphs local.

Record results with [agent-evals](../agent-evals/README.md). Alternate order or use independent
sessions so the second run does not inherit the first answer. Report cold/warm results separately,
per-task distributions, success and missed references. Use at least five matched pairs before a
replacement recommendation. Predeclare a meaningful improvement threshold (for example 20% lower
median source reads) and require no correctness regression; this is a decision criterion, not a
claim. Include installation burden, maintenance, freshness, privacy and rollback in the decision.

Retain Graphify if evidence is mixed. Any replacement requires an explicit migration of routing and
cache policy in each owning repository; do not leave two competing systems as implicit defaults.
