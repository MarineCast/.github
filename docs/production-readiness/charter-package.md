# MarineCast toolkit charters and roadmaps

**Draft package for Tyler review · 2026-10-04 · Proposed governing documents, not adopted policy.**

These eleven drafts translate the requested toolkit outcomes into bounded scope, scientific safeguards, dependencies and acceptance-gated roadmaps. They accompany the MarineCast Production Readiness Assessment. They do not authorize implementation, source acquisition, publication, repository changes or new scientific claims, and they contain no promised delivery dates.

## Contents and intended placement

Tracking note: These copies are stored centrally in `.github` for review. The following placement guidance is retained from the supplied package and describes possible future adoption in the owning repositories; this tracking PR does not perform that adoption. See the [tracking index](README.md).

Each folder corresponds to a MarineCast repository. After review, place the approved document at that repository's `docs/ROADMAP.md`:

| Repository | Draft |
| --- | --- |
| toolkit-seascape | [Seascape](toolkits/seascape.md) |
| toolkit-viewshed | [Viewshed](toolkits/viewshed.md) |
| toolkit-meteorology | [Meteorology](toolkits/meteorology.md) |
| toolkit-oceanography | [Oceanography](toolkits/oceanography.md) |
| toolkit-hydrology | [Hydrology](toolkits/hydrology.md) |
| toolkit-human | [Human](toolkits/human.md) |
| toolkit-ais | [AIS](toolkits/ais.md) |
| toolkit-governance | [Governance](toolkits/governance.md) |
| toolkit-marine-mammals | [Marine mammals](toolkits/marine-mammals.md) |
| toolkit-salmon | [Salmon](toolkits/salmon.md) |
| toolkit-acoustics | [Acoustics](toolkits/acoustics.md) |

This package is a review artifact, not a checkout or patch. Before adoption, inspect and reconcile any existing roadmap, charter, contract, scientific-hardening plan or contributor instructions. Do not blindly overwrite an existing `docs/ROADMAP.md`, duplicate governing rules or treat this package as superseding native contracts. Proposed ownership and acceptance decisions need explicit review. Approved changes should preserve relevant existing commitments and link to their governing sources.

## Shared outcome and conventions

The desired logical application shape is **date/valid interval × H3 × qualified metric**, or **H3 × qualified metric** for static variables. This does not impose a universal daily cadence, H3 resolution or long-table layout. Existing wide tables can satisfy the outcome. Native observations, source-target pairs, gauges, rasters, graphs, geometry and nonspatial records remain companion products where needed.

1. Preserve essential axes such as source role, species/stock/pod, depth, frequency band, deployment, model, forecast issue and ensemble. A declared slice or scientifically justified reduction yields the simple consumer table; dropping dimensions to obtain a unique key is unacceptable.
2. State units, datum, statistic, spatial support, domain fingerprint, calendar, interval boundaries, coverage, weights and denominators. H3 assignment may locate a sensor or gauge; it does not prove full-cell representativeness.
3. Preserve null versus observed zero and explicit missingness/quality states. Keep physical measurements, source estimates, proxies and downstream interpretations distinguishable. A dimensionless score is not automatically a probability.
4. Keep valid/observation time, forecast issue/lead, source availability, revision and as-of cutoff distinct. Static products retain reference period, applicability and release vintage. Unknown historical availability does not prove forecast eligibility.
5. Separate contract version, semantic product version, **scientific method version**, **software/package version**, **immutable generated-data release identity**, effective configuration, source versions/rights and artifact checksums. A method version identifies the scientific calculation; a software version identifies its implementation; a release ID identifies particular generated data. None substitutes for another. Record the checksum algorithm; reproducibility also requires recoverable inputs and configuration.

## Existing contract and consumer boundaries

Build on the [proposed MarineCast contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md), not a competing schema. Native manifests remain authoritative until explicit adoption. v0.1 covers single-resolution static/instant/interval cell or directed-pair tables. Forecast issue/lead time, ensembles, mixed resolution and multi-artifact publications need reviewed profiles or a contract revision; required interpretation must not be hidden in optional extensions.

[OrcaCast's inspected input contract](https://github.com/MarineCast/orcacast/blob/177bd7ad18c646ccd28fcf8d809344252581f231/src/orcacast/inputs.py) is narrower: static or ISO-week features at the configured resolution, checksum pinning and availability strictly before forecast origin. An explicit adapter must handle calendar and support alignment without implicit resampling. A successful feature join does not establish model covariate consumption or predictive validity.

## Decisions proposed for review

- Select the first bounded producer-to-consumer product, geographic domain, resolution, cadence, metric set and scientific acceptance thresholds.
- Resolve AIS ownership/extraction from Human before building a second adapter.
- Resolve Hydrology's native gauge/catchment scope versus Oceanography's marine influence scope; retain Seascape's physical outlet relationships distinctly.
- Decide whether Governance stays a reference inventory or gains separately validated effective/knowledge-time legal reconstruction.
- Preserve marine-mammal annual census as nonspatial year × pod; do not fabricate H3 attribution.
- Select one source-backed MVP each for Hydrology, AIS, Salmon and Acoustics. Their repository scaffolds are not implemented products.
- Agree source rights, publication audience, runtime support and who approves scientific eligibility. Software success, source compatibility, scientific validation and consumer acceptance are separate gates.

## Evidence and completion

Each draft pins its reviewed source SHA and links to supporting code or existing CI. Review was read-only; no fresh toolkit tests, acquisitions, regional pipelines or scientific validations were performed. CI observations describe existing runs, not tests executed for these drafts. Roadmap acceptance tests are future requirements.

Adoption is complete only after decisions are recorded, existing documentation reconciled, responsible maintainers assigned and the approved document deliberately published. A toolkit release is complete only when its own documented acceptance gates pass with inspectable evidence and limitations.
