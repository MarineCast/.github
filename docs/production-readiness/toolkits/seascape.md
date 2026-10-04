# Seascape: proposed charter and roadmap

**Draft for Tyler review · 2026-10-04 · Not adopted policy.** Milestones below propose acceptance gates, not delivery dates or completed work.

## Purpose and desired outcome

Provide reproducible descriptions of the physical marine setting that applications can join without losing spatial support, source quality, or scientific meaning. The application-facing outcome is a static **H3 × metric** table, backed by lossless native products and immutable releases. Static describes the table's time axis; it does not mean a coastline, habitat inventory, or source survey never changes.

## Boundaries and non-goals

Own physical seascape measurements, geometry, support and defensible derived descriptors. Preserve water networks, selected outlet relationships and native habitat evidence where a single cell value is insufficient. Do not infer species occurrence, abundance, prey availability, legal protection or observer effort. A mapped positive habitat feature is not evidence of complete survey coverage or absence elsewhere. Do not turn source-type codes into uncertainty estimates or unsupported rock/sediment data into bottom-hardness area.

## Native data and application-facing H3 products

Retain raster, geometry, graph and relationship companions. R8 water-overlap support and the R6 parent union are different sampling definitions. Depth is aggregated from source pixels directly at each resolution; generic averaging between H3 resolutions is not an approved substitute. Preserve datum, units, statistic, support denominator, source/reference period and uncertainty. Long/wide layout and supported resolutions remain product decisions requiring review.

## Current verified baseline

Reviewed snapshot: [`162bc906a3e6cd73146870e9c2e343cacf62e0bb`](https://github.com/MarineCast/toolkit-seascape/tree/162bc906a3e6cd73146870e9c2e343cacf62e0bb).

The [matrix implementation](https://github.com/MarineCast/toolkit-seascape/blob/162bc906a3e6cd73146870e9c2e343cacf62e0bb/src/seascape/metric_matrix.py) already produces one row per H3 index/resolution with namespaced metric columns, currently defaulting to R6 and R8. It resolves audited immutable schema-3 releases, verifies checksums/support, preserves nulls and quality evidence, and writes atomically. Existing exact-head CI passed; no fresh tests or regional runs were performed for this review. Python support is narrowly 3.14, with a rasterio version cap.

The [capability inventory](https://github.com/MarineCast/toolkit-seascape/blob/162bc906a3e6cd73146870e9c2e343cacf62e0bb/docs/capability-coverage.md) distinguishes implemented methods from fixture-tested extensions and materialized releases. Checked-in catalogs describe older materializations; corrected methods still need a source-backed candidate.

## Known and proposed metric families

- **Implemented families:** bathymetric depth/terrain/geomorphic descriptors; shoreline character, proximity/exposure and morphometry; fluvial/estuary relationships; modeled sediment/rock evidence; selected mapped vegetation/habitat evidence. Some corrected calculations remain unmaterialized.
- **Fixture-tested or pending:** optional intertidal/habitat producers, selected outlet relationships, nearshore transitions, passage/sill candidates and gateway descriptors require reviewed regional inputs or registries.
- **Blocked/proposed:** finer bathymetry, physical hardness, observed sediment detail, additional benthic habitats and shelf geometry need suitable sources and definitions. Null columns do not constitute capability.

## Science, quality and rights

Use the proposed [MarineCast contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md) through an explicit native-to-shared mapping; adoption is not yet established. Retain native manifests. Pin contract/product versions, release identity, code/package version, effective configuration, source versions, rights and exact artifact hashes. Reference period, release availability and applicability must survive downstream use; reviewed profile changes are needed where v0.1 is insufficient.

## Dependencies

Dependencies include reviewed source registrations, canonical marine support, source-specific datum/geometry handling, the supported geospatial runtime and downstream adapter agreement. Unknown rights block redistribution. Missing or partial observations remain null/status-qualified, never default zero.

## Phased milestones and acceptance tests

1. **Agree one bounded product.** Select domain, metric set, resolution, sources and permitted uses. Acceptance: a reviewed metric/support register separates current, pending and unsupported quantities; every metric has units, denominator and allowed reductions.
2. **Materialize current methods.** Build a source-backed schema-3 candidate. Acceptance: unique keys and exact domain checks; raw-source spot checks against independent calculations; pixel-weight and datum fixtures; null/zero and positive-only habitat coverage tests; all provenance and rights recoverable.
3. **Qualify publication and adapter.** Exercise clean installation, checksum failure, partial publication and rollback. Acceptance: immutable artifacts reproduce the declared matrix; quality/status survive export/reload; incompatible resolution/support is rejected; a pinned consumer join does not expand rows or invent dates.
4. **Extend selectively.** Add a source-blocked family only after source and scientific review. Acceptance: retained-source validation, reviewed footprint/absence semantics and a separately versioned method accompany every new family.

## Unresolved decisions

Tyler must review the initial domain/resolution, required source vintages, quality thresholds, habitat priorities and hydrology/oceanography boundary for outlet-related products. Qualify runtime maintenance, including replacement ARM64 CI capacity when needed.

## Definition of done

A product is done when its bounded scientific claims, rights, support, current-method validation, reproducibility and consumer projection pass the gates above, with documented limitations. Publishing a table or passing fixtures alone does not establish scientific readiness.
