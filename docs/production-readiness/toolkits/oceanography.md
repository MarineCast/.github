# Oceanography: proposed charter and roadmap

**Draft for Tyler review · 2026-10-04 · Not adopted policy.** Proposed milestones require evidence; no delivery dates or new test successes are asserted.

## Purpose and desired outcome

Provide traceable ocean-condition measurements and carefully labeled physical proxies as application-facing **date/interval × H3 × metric** products. Preserve native model, satellite, tide and gauge semantics so a consumer can distinguish an observed quantity, model estimate, composite and uncalibrated influence index.

## Boundaries and non-goals

Own marine-condition transformations and explicitly defined ocean-facing influence products. Gauge/catchment acquisition versus marine river influence is an unresolved boundary with Hydrology. Do not infer biological suitability, abundance or prey from environmental values. An influence kernel is not calibrated freshwater concentration; a tide proxy is not automatically an independently validated local prediction.

## Native data and application-facing H3 products

Preserve depth/layer, source model, harmonic constituent, gauge/outlet identity, compositing window and any other distinguishing axis. Satellite native pixel centers are assigned to H3 with cosine-latitude-weighted valid means, not exact polygon intersection. Tide/river R8 water kernels reduce to R6 with water-area weights. Missing expected gauges invalidate affected parents; missing pixels/gauges are not zeros. A seven-day chlorophyll composite can have only one valid day. Family `FEATURE_STATUS` indicating any available metric must not be interpreted as all fields complete.

Long/wide layout, approved resolution and cadence remain product-specific. Native companions and explicit reductions support the simpler table rather than being discarded to obtain it.

## Current verified baseline

Reviewed snapshot: [`c378eb7f580e34bad0161cc023d4ecb5cd90238f`](https://github.com/MarineCast/toolkit-oceanography/tree/c378eb7f580e34bad0161cc023d4ecb5cd90238f).

The [builder](https://github.com/MarineCast/toolkit-oceanography/blob/c378eb7f580e34bad0161cc023d4ecb5cd90238f/src/oceanography/build.py) emits daily per-family `FEATURES.parquet` keyed by date/H3/resolution with metrics and QC, using explicit R5/R6 products. Seven families are implemented: tide proxies, SalishSeaCast currents, river influence, satellite SST, satellite chlorophyll, HYCOM currents and DFO harmonics. The feature catalog still covers five families and needs reconciliation.

Production blockers remain: caught build exceptions can become unavailable-support outputs with missing metric columns; [CLI](https://github.com/MarineCast/toolkit-oceanography/blob/c378eb7f580e34bad0161cc023d4ecb5cd90238f/src/oceanography/cli.py) status does not reliably fail required-family failures; artifacts and manifests lack a global generation transaction; code fingerprints omit normalization/configuration helpers; support/geometry preflight is incomplete.

Existing [exact-head CI](https://github.com/MarineCast/toolkit-oceanography/actions/runs/36842634076) passed Python 3.11/3.14 research tests. Wheel smoke uses system-site packages; tide extras/private UTide dependencies and a standalone live replay remain unqualified. No fresh tests or production builds occurred for this review.

## Known and proposed metric families

- **Implemented:** the seven families above, with family-specific units/QC and selected composite/harmonic calculations.
- **Proposed near-term:** schema-stable complete-or-explicitly-unavailable family releases, a complete metric register and one scientifically qualified bounded product.
- **Deferred:** expanded forecasts, ensembles, depths or derived ecological interpretations without reviewed contracts and source/method validation.

## Science, quality and rights

Use the proposed [MarineCast contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md) through reviewed adoption. Forecast issue/lead, ensembles and multi-artifact generations need a reviewed revision/profile. Native manifests remain authoritative until adoption; separate contract/product versions, release identity, code/package, configuration, source revisions and artifact hashes.

UTC and provider-day discharge cannot be silently interchanged. Availability remains unknown and forecast eligibility false until supported evidence/policy exists. Retain valid, issue, available and revision times distinctly wherever applicable; never use a later vintage in an earlier replay.

## Dependencies

Dependencies include canonical water support/connectivity, complete feature definitions, provider rights, acquisition runtimes and Hydrology ownership agreement.

## Phased milestones and acceptance tests

1. **Make failures safe.** Complete registry and preflight for all seven families. Acceptance: successful/unavailable outputs have identical declared metric schemas; required failures return nonzero; disconnected cells, missing gauges, geometry/support mismatch and invalid configurations fail appropriately.
2. **Make releases reproducible.** Add complete portable fingerprints and atomic generation publication. Acceptance: interrupted writes, missing partitions, hash mismatches, stale normalization/configuration and rollback tests cannot expose a mixed release; clean isolated installation exercises required extras.
3. **Qualify one real-source family.** Select domain, seasons, sources and preset thresholds. Acceptance: bounded retained-source replay, independently matched tides/currents/gauges as appropriate, measured temporal coverage and documented uncertainty; null/composite support and provider-day conversions reconcile.
4. **Expose the consumer profile.** Declare units, reductions and as-of eligibility. Acceptance: unique fully qualified keys, water-weight reconciliation, no unsupported averaging, unchanged consumer row counts and explicit rejection of unknown availability for forecasting. Expand families only after equivalent gates.

## Unresolved decisions

Review Hydrology ownership, first family/domain, scientific thresholds, forecast ambition, provider rights and portable tide dependencies. A historical OrcaCast pilot is not standalone qualification.

## Definition of done

Done means fail-closed operation, complete immutable evidence, a qualified scientific method and a lossless audited H3 consumer projection for a bounded release. A successful process exit or one available metric does not satisfy that definition.
