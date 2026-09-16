# MarineCast organization documentation

This repository hosts the MarineCast GitHub organization profile and shared architecture guidance.

- [Organization profile](profile/README.md): ecosystem overview and toolkit directory.
- [Infrastructure](INFRASTRUCTURE.md): repository ownership, data contracts, integration, and operational boundaries.
- [Data-product contract v0.1](contracts/README.md): proposed manifest specification, schema and synthetic examples; adoption is not yet established.
- [Agent instructions](AGENTS.md): guidance for maintaining this repository.

Each toolkit maintains its own `AGENTS.md`. Instructions in this repository are not automatically
inherited by other organization repositories.

## Optional agent tooling and evaluation

- [Code navigation](docs/code-navigation.md): selective Graphify, syntax and literal retrieval.
- [Context audit](docs/context-audit.md): file-size findings and limitations.
- [Serena pilot proposal](docs/serena-evaluation.md) and [future graph comparison](docs/code-graph-evaluation.md).
- [Agent benchmarks](agent-evals/README.md): collect real task measurements.

These are on-demand references, not required preloads for ordinary toolkit tasks.
