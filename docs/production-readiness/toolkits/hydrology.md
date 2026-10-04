# Hydrology toolkit charter and roadmap

Status: Draft for Tyler review, not adopted policy. Date: 2026-10-04.

## Purpose and desired outcome

Provide reproducible freshwater measurements and geographic context that applications can connect to coastal questions without overstating what gauges establish. The desired application output is a logical date × H3 × metric table, preserving source, gauge, catchment, and temporal dimensions needed for unique identity. Static H3 × metric products may describe approved catchment or outlet context with explicit applicability.

The proposed MVP is one approved stream-gauge source, its native time series, and an auditable H3 projection with catchment/outlet context. Marine influence already has an implementation in oceanography; the ownership boundary must be decided before creating a second pipeline.

## Boundaries and non-goals

Preserve gauge/site coordinates, station changes, catchment identity, source method, and gauge-to-outlet relationships. Discharge is not automatically runoff depth; rainfall is not automatically runoff. Summing nested gauges, multiplying discharge across cells, or uniformly spreading a river measurement across marine waters requires a defensible method and explicit review. The MVP excludes rainfall-runoff modeling, flood prediction, plume calibration, and application-specific ecological suitability.

## Native data and application-facing H3 products

Keep native source series and metadata losslessly, with an auditable mapping to the H3 application projection. Gauge location, catchment extent, outlet location, and modeled marine influence have different spatial support. Use distinct products or explicit roles rather than collapsing them into an ambiguous cell metric. Required gauge/catchment/source dimensions remain in row identity.

Reuse the proposed [.github contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md). Its identity, H3 support, time boundaries, units, missingness, provenance, rights, checksums, and immutable publication are the proposed interchange basis; native manifests remain authoritative until explicit adoption. Long versus wide layout, cadence, and H3 resolution remain product-specific until approved. Preserve provider-day boundaries and instantaneous versus interval meaning; a date label cannot replace time support. Forecast issue/lead time, ensembles, and unsupported structures require a reviewed profile or contract revision, not dropped dimensions or optional metadata hiding required semantics.

## Current verified baseline

The complete [toolkit-hydrology tree at 0d0aaf1d8f032aa4dcd32a230974379c47420abf](https://github.com/MarineCast/toolkit-hydrology/tree/0d0aaf1d8f032aa4dcd32a230974379c47420abf) contains a README and banner only. There is no source, schema, package, test, workflow, or output implementation; the reviewed repository had no Actions runs. No tests were run for this charter.

[Oceanography at c378eb7f580e34bad0161cc023d4ecb5cd90238f](https://github.com/MarineCast/toolkit-oceanography/blob/c378eb7f580e34bad0161cc023d4ecb5cd90238f/src/oceanography/build.py) orchestrates river influence among seven families. Its resolution 8 water-path kernels aggregate water-area weights to resolution 6. Provider-day versus UTC discharge semantics and unknown availability remain unresolved, and the influence kernels are uncalibrated. That work is an existing research dependency, not a hydrology implementation or validated coastal transport model.

## Known and proposed metric families

No metric family is implemented in this repository. Proposed first metrics are source-defined discharge observations or estimates with units, gauge identity, time support, quality, and revision status. Stage is a separate optional quantity requiring vertical datum and source definition. Catchment and outlet geography are proposed static context, not measurements of marine exposure.

## Science, quality and rights

Missing or invalid gauge data remain null with a reason, never zero discharge. Retain provisional status, revisions, unit/datum conversions, source coverage, and partial-period treatment. Keep observation, source availability, retrieval, processing, and release identities separate; unknown historical availability cannot establish forecast eligibility. Source access and redistribution rights require approval before publication.

## Dependencies

Dependencies are a selected source contract, stable gauge/catchment/outlet references, oceanography ownership agreement, reproducible spatial support, and consumer acceptance rules. Validate duplicate times, gaps, timezones, unit changes, station moves, implausible values, and downstream aggregation. Scientific observations and derived influence interpretations remain separately labeled.

## Phased milestones and acceptance tests

1. **Agree scope and ownership.** Acceptance: Tyler approves the source/rights, native measurement, responsible maintainer, and boundary with oceanography; extraction or continued dependency is explicit.
2. **Build the native adapter.** Acceptance: synthetic fixtures preserve gauge identity, provider-day semantics, units/datum, gaps, partial periods, and revisions; an authorized retained sample reconciles to its source.
3. **Export a bounded H3 product.** Acceptance: gauge/outlet/catchment roles are explicit, complete keys are unique, native evidence remains accessible, contract/artifact checks pass, and incompatible spatial or temporal joins fail.
4. **Qualify one release.** Acceptance: an installable entry point reproduces an approved sample with configuration, rights, checksums, immutable publication, negative fixtures, and a verified consumer round-trip.

The acceptance suite must run in CI, including clean package installation and synthetic/offline contract tests; document any live or native-runtime checks separately.

## Unresolved decisions

Open decisions include source, ownership, geographic scope, gauge-to-outlet mapping, revisions, historical availability, cadence, resolution, and physical layout. No deadline is committed.

## Definition of done

The MVP is done when one approved gauge product and its spatial context are reproducible and safely consumable without implying calibrated marine influence. Scientific qualification and data validation must accompany schema validation. Tyler approval is required before this draft governs work.
