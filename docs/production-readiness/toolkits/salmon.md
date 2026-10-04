# Salmon toolkit charter and roadmap

Status: Draft for Tyler review, not adopted policy. Date: 2026-10-04.

## Purpose and desired outcome

Make salmon observations and estimates usable as reproducible, species-aware data products while preserving what each source actually measures. Applications should receive logical date × H3 × metric tables with every necessary biological, geographic, and temporal dimension retained. Static H3 × metric context can describe approved reference geography with a stated applicability period.

The proposed MVP is one approved source contract, one native adapter, and one auditable site-to-H3 export, developed against synthetic fixtures first. This charter proposes a bounded measurement product; it does not promise a marine prey-availability surface or select a live source.

## Boundaries and non-goals

The toolkit should preserve species, stock, run, life stage where supplied, site, watershed, observation method, source identity, and actual time intervals. An annual estimate cannot silently become daily data. A count, an expanded estimate, and a modeled value must remain distinguishable. Non-goals for the MVP include stock assessment, population forecasting, causal habitat claims, and species-specific application suitability scores.

## Native data and application-facing H3 products

Retain native records, source definitions, revisions, biological identifiers, geographic references, sampling effort, and uncertainty. The H3 application projection must retain a recoverable link to native measurements and preserve dimensions needed for unique identity. Mapping a counting site into a cell expresses site location; it does not assign its catchment, migration corridor, or marine influence to that entire cell. Multiple sites or stocks in one cell must remain distinguishable unless an explicit, reviewed aggregation applies.

Reuse the proposed [.github contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md), including identity, H3 support, time intervals, units, missingness, provenance, rights, checksums, and immutable publication. Native manifests remain authoritative until explicit adoption. Date labels must preserve the declared temporal support. Long versus wide layout, cadence, and H3 resolution remain product-specific until approved. Static products have no fabricated row-level date. Forecast issue/lead time, ensembles, and other unsupported structures require a reviewed profile or contract revision; do not drop axes or hide required semantics in optional extensions.

## Current verified baseline

The complete [toolkit-salmon tree at 807d5405474036b19555e0ac133591460f824392](https://github.com/MarineCast/toolkit-salmon/tree/807d5405474036b19555e0ac133591460f824392) contains only a 17-byte README.md. No implementation, schema, export, package, tests, or CI is present in that tree. No live source is approved by the reviewed evidence, and no tests were run for this charter. All capabilities and milestones below are proposals.

## Known and proposed metric families

Candidate families include passage counts, escapement estimates, and catch observations. They describe different processes and require separate quantity definitions, uncertainty, coverage, and applicable methods. Marine prey availability would require additional evidence and modeling; it cannot be inferred by renaming passage, escapement, or catch.

## Science, quality and rights

A missing count is null with an explicit reason, never zero. True zero requires valid observation support. Document partial sampling, closures, detection methods, estimate expansion, revisions, uncertainty, and comparability across sites. Keep source availability, retrieval, observation interval, and release identities separate so retrospective applications can avoid using information unavailable at the time.

Rights and redistribution must be approved before source data are published. Preserve attribution and respect sensitive location or community data restrictions. Scientific measurements remain separate from ecological or application interpretation. Quality checks must identify impossible values, unit mismatches, overlapping reporting intervals, duplicate biological keys, and unintended aggregation across stocks or methods.

## Dependencies

Dependencies are source-owner definitions and rights, stable biological/site identifiers, reproducible geography, and a consumer willing to validate the proposed product.

## Phased milestones and acceptance tests

1. **Select one measurement and source.** Acceptance: Tyler approves the quantity, source contract, rights, intended use, maintained identifiers, and limitations; no live-source name is assumed by this draft.
2. **Build native fixtures and adapter.** Acceptance: synthetic cases preserve stock/run/site/interval distinctions, revisions, zero, missingness, and partial coverage; an authorized sample can be reconciled to its source.
3. **Add a site-H3 projection.** Acceptance: mapping and spatial support are documented, full keys remain unique, units and time boundaries validate, and a consumer round-trip preserves native interpretation.
4. **Publish one reproducible release.** Acceptance: a clean-installed entry point demonstrates approved data, configuration, source provenance, artifact hash, contract validation, negative fixtures, and an immutable publication procedure together.

The acceptance suite must run in CI, including clean package installation and synthetic/offline contract tests; document any live or native-runtime checks separately.

## Unresolved decisions

Open decisions are the initial metric/source, rights, identifiers, uncertainty representation, source revision policy, observation cadence, H3 resolution, and physical layout. Cross-toolkit biological naming needs agreement before joins. No deadline is implied.

## Definition of done

The MVP is done when one approved measurement can be reproduced from native evidence and safely joined by a consumer without turning a site observation into marine prey availability. Tyler review and documented acceptance are required before this draft becomes governing policy.
