# Governance reference charter and roadmap

Status: Draft for Tyler review, not adopted. Assessment date: 2026-10-04. The gates below propose scope and acceptance, not deadlines.

## Purpose and desired outcome

Provide reproducible governance-reference geometry and bounded H3 summaries for MarineCast applications. A consumer should know which source-backed features intersect a cell, what the summary measures, how complete the inventory is and which uses remain unsupported. The intended result is an auditable reference product with explicit coverage and rights.

## Boundaries and non-goals

The present product is an inventory snapshot, not authoritative legal advice or effective-date legal history. An intersection does not by itself establish which regulation applies to a person, vessel or activity. A 24-entry catalog is not evidence of 24 implemented source families. Model eligibility, legal interpretation and historical reconstruction require separate approval and evidence.

## Native data and application-facing H3 products

Preserve native source-backed feature IDs, unique geometry-part IDs, geometry, attributes and EPSG:4326 coordinates. The target is logical static H3 × metric; date × H3 × metric is appropriate only for a separately specified temporal product. Use the [proposed organization contracts v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md), rather than creating a competing common schema. Native manifests remain authoritative pending adoption; additional semantics require a reviewed profile/revision.

Long versus wide layout, resolution and refresh cadence remain product-specific decisions. Preserve source and feature dimensions until an explicit aggregation applies. Partial or unknown empty intersections remain null, not zero; unavailable and not-applicable statuses stay distinct. Retain native records where independent attribute sets cannot express feature-level relationships. Separate measured geometry from legal interpretation.

## Current verified baseline

The assessed head is `c2f340ff249f191c891a83eec5e2e6e61c7e406c`. Six native geometry families are implemented; additional catalog entries are plans. The [H3 exporter](https://github.com/MarineCast/toolkit-governance/blob/c2f340ff249f191c891a83eec5e2e6e61c7e406c/src/governance/h3_matrix.py) already provides one row per supplied H3 cell/resolution, with feature counts, unioned polygon/full-cell coverage fraction, unioned line metres, point counts, statuses and attribute sets.

The exporter checks grid, configuration, raw-source and artifact provenance. Attribute lists are independent sets, not aligned feature records. Named-roster completeness does not establish complete geographic coverage. Antimeridian grids are unsupported. All rows remain research/model-ineligible. Native multi-file publishing lacks a global atomic generation pointer.

[Exact-head CI](https://github.com/MarineCast/toolkit-governance/actions/runs/36840934121) passes both Python versions, wheel building and outside-checkout smoke; the inspected Python 3.11 log reports 29 passed. Existing tests cover overlay union, missingness, keys, checksums, configuration drift and overwrite safety. This draft does not claim additional tests or production-source validation were run.

## Known and proposed metric families

Implemented metrics are geometric inventory summaries: feature counts, union coverage fractions, line length and point counts, alongside status and attribute sets. Proposed work includes a validated consumer-grid product, documented freshness/coverage indicators and atomic release publication. Date-specific governance metrics are a separately reviewed extension requiring effective-time and knowledge-time semantics, not a rename of snapshot fields.

## Science, quality and rights

Validate each source's authority, license, redistribution terms, vintage and geographic scope. Compare real-source overlays with independent calculations, including overlapping polygons, multipart features, boundaries and empty/partial cases. Document full-cell denominators and union behavior. Require grid-level coverage evidence independently of named-roster completeness. Unsupported antimeridian requests must fail explicitly rather than silently omit geometry.

## Dependencies

Dependencies are the six source families, an approved consumer grid, reviewed organization contracts and source-rights/freshness decisions. Proposed traceability retains source identity/vintage, extraction and availability times, code SHA, configuration identity, release identity and artifact checksums. Effective dates need explicit evidence; availability is not legal validity. Forecast issue/horizon semantics are deferred in v0.1 and inapplicable to the snapshot. Temporal or multi-artifact publication needs an explicitly reviewed profile/revision.

## Phased milestones and acceptance tests

1. Confirm product scope. Accept a reviewed source roster, consumer grid, metric registry, units, completeness definitions, resolution, format and refresh policy mapped to contracts v0.1.
2. Validate current implementation. Accept reproducible exports for all six implemented real-source families, independently checked overlays, rights/freshness evidence and fixtures for nulls, overlap, geometry parts and unsupported geography.
3. Make releases coherent. Accept generation manifests binding every file/checksum, an atomic current-generation pointer, failure-injection tests showing readers cannot mix generations, and passing installed-package CI.
4. Assess temporal extension separately. Proceed only after approval; accept effective/knowledge-time source evidence, boundary-date and unknown-date fixtures, and an availability-safe consumer example without retrospective leakage.

## Unresolved decisions

Tyler must approve geographic coverage, priority source families, consumer resolution, completeness thresholds, publication rights, refresh ownership and whether temporal legal reconstruction belongs in this repository.

## Definition of done

A release is done when its approved scope is reproducible from identified sources, geometric summaries and missingness are validated, coherent publication is verified, and consumers can inspect provenance, rights, coverage limitations and permitted interpretation before use.
