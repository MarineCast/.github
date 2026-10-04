# Viewshed: proposed charter and roadmap

**Draft for Tyler review · 2026-10-04 · Not adopted policy.** Milestones propose acceptance gates; no delivery dates or new test successes are implied.

## Purpose and desired outcome

Describe physical viewing relationships between potential observation locations and marine cells. Deliver auditable native directed-pair products and static application-facing **H3 × metric** summaries with explicit role, reduction and candidate support. The desired outcome is a reproducible viewability input whose physical meaning remains intact when another toolkit adds activity or weather.

## Boundaries and non-goals

Own terrain, vegetation, distance and composed static viewability calculations. Keep land-source and water-source roles distinct. Physical visibility is not observed platform activity, observer effort, reporting capture, species occurrence or detection probability. Do not label summed opportunity weights as probabilities or assume a pair outside the modeled candidate universe is blocked. Weather and human activity belong to their domain producers and explicit downstream combinations.

## Native data and application-facing H3 products

Keep the directed pair companion and distinguish source from target, including source type in combined identities. Declared slices/reductions yield H3 × metric; they must not discard pair identity silently. Means and sums use the configured candidate population, without effort weighting. Sums can exceed one. Water-source canopy fields remain not applicable. Long/wide storage, resolution and distance limits require product-specific approval.

## Current verified baseline

Reviewed snapshot: [`0c0c33b60ab34f6e22d87ff235538d82112f2589`](https://github.com/MarineCast/toolkit-viewshed/tree/0c0c33b60ab34f6e22d87ff235538d82112f2589).

Native products are static source-H3 × target-H3 pairs, ordinarily R7 with a configured 30 km candidate universe. [H3 summaries](https://github.com/MarineCast/toolkit-viewshed/blob/0c0c33b60ab34f6e22d87ff235538d82112f2589/src/viewshed_toolkit/pipeline/finalize/aggregate.py) already provide per-source/per-target reductions. Existing exact-head CI passed. This review did not execute fresh tests or reproduce source-derived defects.

Two production blockers were identified: [overwrite finalization](https://github.com/MarineCast/toolkit-viewshed/blob/0c0c33b60ab34f6e22d87ff235538d82112f2589/src/viewshed_toolkit/pipeline/finalize/final_artifacts.py#L1137-L1250) can relabel retained factors with current configuration without trusted producer-lineage validation; [visible-source counting](https://github.com/MarineCast/toolkit-viewshed/blob/0c0c33b60ab34f6e22d87ff235538d82112f2589/src/viewshed_toolkit/pipeline/weights/view_score.py) can include null in a unique count. [PR 11](https://github.com/MarineCast/toolkit-viewshed/pull/11) addresses lineage but was unmerged at review.

## Known and proposed metric families

- **Implemented:** terrain, vegetation, distance and composed static pair weights; candidate-pair/cell counts; positive-pair fraction; mean, maximum and sum reductions by source or target; canopy summaries conditional on terrain support.
- **Proposed qualification:** a role-qualified H3 publication profile with verified pair-to-summary equivalence, complete provenance, explicit candidate denominators and quality limits.
- **Out of scope:** direct detection probabilities or biologically calibrated observation surfaces without separate data and validation.

## Science, quality and rights

Use the proposed [MarineCast contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md), which already supports directed cell pairs, through reviewed adoption rather than a competing schema. Preserve native manifests and separate contract/product versions, release identity, code/package version, effective configuration, source versions and artifact hashes. `KNOWLEDGE_TIME_UTC` is build knowledge, not observation time; static reference vintages and availability need explicit consumer handling.

[Committed real-data evidence](https://github.com/MarineCast/toolkit-viewshed/blob/0c0c33b60ab34f6e22d87ff235538d82112f2589/docs/reports/real-data-examples-validation.md) covers 5,424 San Juan pairs and reports 9.69% missing mapped-land canopy pixels with zero-height fallback. That assumption requires sensitivity analysis; it is not complete canopy evidence. Unknown/partial inputs remain visible in quality states, never silently converted to certainty or zero.

## Dependencies

Dependencies include source/target support, elevation/canopy inputs, geospatial runtime, source rights and agreed Human interfaces.

## Phased milestones and acceptance tests

1. **Restore trustworthy correctness.** Complete reviewed lineage and counting fixes. Acceptance: stale configuration/source/build identities fail reuse and overwrite; rollback preserves the prior release; all-blocked source groups count zero, with exact mixed/all-visible counts; regressions run against the final package.
2. **Qualify the physical method.** Select a bounded domain and approved source vintages. Acceptance: independent line-of-sight checks, candidate-boundary fixtures, canopy fallback sensitivity and declared coverage thresholds; report disagreements rather than tuning them away.
3. **Publish explicit H3 summaries.** Define role-qualified keys and allowed reductions. Acceptance: summaries equal independently recomputed pair reductions; reversed roles, omitted dimensions and mismatched support fail; null/not-applicable semantics survive round-trip; atomic immutable publication rejects stale/missing artifacts.
4. **Verify downstream use.** Exercise a checksum-pinned consumer fixture. Acceptance: no row expansion or implicit resampling, preserved build availability and physical labels, clean installed-wheel/native-runtime checks and a documented bounded production-scale run.

## Unresolved decisions

Review the first domain, R7 versus consumer resolution, candidate distance, canopy coverage/fallback thresholds and ownership of dynamic composition with Human. No universal cadence is required for static physical geometry.

## Definition of done

Done means lineage-safe, independently checked pair evidence and H3 reductions, qualified rights/runtime/publication, and a reproducible consumer mapping. Any claim about real detection remains a separate scientific decision.
