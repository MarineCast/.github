# Approved application delivery defaults

**Approved by Tyler on 2026-10-04. This is the default target for application-facing toolkit products; toolkit conformance and application integration require separate evidence.**

Tyler approved the delivery shape with “Yes that is exactly what I mean. Let's make that the default contract.” He then approved daily dynamic delivery: “Then for time resolution -> yes let's default to daily for every dynamic variables”. These decisions narrow the application-facing target while preserving the broader [manifest contract v0.1](README.md). They do not adopt the eleven [draft toolkit charters](../docs/production-readiness/README.md), authorize implementation or migration, or establish scientific readiness.

## Approved defaults

| Aspect | Default target convention |
| --- | --- |
| Physical format | Wide Parquet: qualified metrics are columns, alongside identity, support and quality fields needed to interpret them. |
| Dynamic grain and cadence | Daily application-facing output for every dynamic variable: one row per H3 cell and declared daily valid interval for a specified product variant. Each metric has a documented, scientifically valid daily aggregation or representation. |
| Static grain | One row per H3 cell for a specified product variant, with metric columns and a declared reference period/applicability. Do not fabricate a row-level date. |
| Resolution | One H3 resolution per published table. The numerical resolution remains pending; this decision does not select R6 or any other value. |
| Companion manifest | Describe units, methods, source data, quality rules and versions, together with v0.1 identity, spatial/temporal support, missingness, provenance, rights, configuration, exact artifact checksums and limitations. |
| Necessary dimensions | Preserve species, depth, source/target roles and other distinguishing dimensions in native companions or explicit, independently identifiable product variants, with auditable projections or reductions. |

The default grain applies within a fully specified variant. Species or depth layers cannot become duplicate cell/day rows in an apparently unqualified product. Publish separately identified variants with recoverable native evidence, or propose a reviewed richer profile with those dimensions in its key. A directed source-target companion remains a pair product; a cell summary needs an explicit role and scientifically justified reduction. Never discard axes, select arbitrary first rows, or hide row-varying identity in manifest metadata to fake unique cell keys. A manifest may describe a constant variant, but cannot replace distinguishing values that vary across rows.

Wide storage does not make unlike quantities interchangeable. Definitions retain units, datum, statistic, support, missingness and quality. Preserve unknown, unavailable, partial and not-applicable states separately from observed zero. Native observations, pairs, rasters, graphs, geometry and nonspatial records remain available where required; the application table must have a traceable relationship to them.

## Daily delivery and native temporal support

Daily is the approved application cadence, not a claim that every source observes daily. Preserve the native sampling/reporting cadence and intervals in companion evidence. Each daily metric must define its statistic or representation, weighting, completeness, partial-period handling and relation to native evidence; a date label alone cannot establish that meaning.

For subdaily sources, specify an appropriate daily reduction rather than dropping samples or assuming an arithmetic mean fits every quantity. Slower sources require a declared interval-applicability or carry-forward rule only where scientifically justified; otherwise affected days remain unavailable with explicit reasons. Retain the original observation interval, vintage and availability, label carried values by their actual interpretation, and avoid future-data leakage. Do not invent daily observations, divide monthly totals arbitrarily, silently forward-fill, or imply daily measurement support that the source lacks.

The calendar timezone and UTC-versus-local day boundaries remain unchosen. Once selected for a product, declare exact interval start/end boundaries and the calendar/zone; local days can be 23 or 25 hours. Daily delivery does not approve a timezone, aggregation method or global completeness threshold. Metrics in one row must have compatible declared daily support; incompatible support requires separate products or a reviewed transformation. Slower native applicability remains documented even when a justified daily representation is provided.

## Relationship to manifest contract v0.1

This is a delivery profile and decision record, not a new manifest schema version. The v0.1 JSON Schema and synthetic examples are unchanged. Valid CSV, instantaneous, directed-pair and other native/legacy products within v0.1's scope remain valid under that contract; they do not automatically meet this narrower wide-Parquet static/daily-interval target. Existing native contracts remain authoritative until an owning toolkit deliberately implements and validates a mapping.

For a conforming cell product, map its complete unique, non-null key to `identity.primary_key`, its single index field/chosen resolution to `spatial`, all columns to `fields`, and its finished Parquet artifact to `artifact`. Dynamic keys include both interval boundaries as v0.1 requires; use its half-open **[start, end)** semantics and explicit zone. Static products use its applicability meaning. A date label is optional convenience and cannot replace boundaries. These existing rules do not select the still-pending day calendar or aggregation method.

Retain v0.1's strict validation: reject unknown core properties, duplicate JSON keys, non-standard numbers, incomplete keys, incompatible support, invalid value/status combinations and artifact hash mismatches. Schema validity alone does not verify artifacts, scientific meaning, rights or consumer compatibility. Follow the [validation and consumer acceptance checks](README.md#validation-and-consumer-acceptance); this approval neither relaxes them nor invents toolkit adoption.

Forecast issue/lead-time, ensembles, mixed-resolution tables and multi-artifact generation protocols remain outside v0.1's established scope. Native companions use their owning contracts; this decision does not add a transaction schema for them. If a required structure cannot be represented faithfully, review a profile/contract revision rather than changing v0.1 incompatibly, dropping dimensions or hiding required interpretation in optional extensions.

## Distinct version and release identities

The companion manifest and pinned, recoverable references must distinguish these identities. None substitutes for another.

| Identity | Meaning |
| --- | --- |
| Manifest contract version | Encoding and validation contract, currently `0.1` when that schema is used. This decision does not increment it. |
| Semantic product version | Product meaning and compatibility under the existing v0.1 versioning rules. |
| Scientific method version | Scientific calculation, including support, transformations, reductions and assumptions. |
| Software/package version and Git revision | Implementation used to produce the artifact, including dirty-tree state. |
| Immutable generated-data release identity | Particular generated data release, distinct from a reusable product definition or package release. |
| Source versions, effective configuration and artifact checksums | Input vintages, settings and exact bytes associated with the release. Record the checksum algorithm. |

v0.1 provides product/producer versions, code revision, processing/source/configuration provenance and artifact SHA-256. It has no dedicated core `scientific_method_version` or `data_release_id` fields. Record those identities explicitly through semantically appropriate existing descriptive fields or pinned method/release references, and verify recoverability during conformance review. The current schema does not enforce their contents. Dedicated machine-validated fields require a reviewed schema revision; do not add undeclared core fields or repurpose a software version or artifact hash as a method version or release ID.

## Decisions still pending

Approval selects the delivery shape and daily dynamic cadence. Product review must still decide:

- Calendar timezone and UTC-versus-local day boundaries; interval aggregation/representation, weighting, completeness and partial-period rules.
- Numerical H3 resolution, geographic domain and spatial support/assignment or conversion methods. R6 has not been approved.
- Global metric naming or a common registry; individual metrics still need unambiguous qualified definitions.
- QC implementation or code changes; existing v0.1 missing-reason semantics remain in force.
- Forecast profiles, issue/lead-time and ensemble handling; this approval does not approve a forecast profile.
- Scientific thresholds, source qualification, rights, release audience and product eligibility.

The decision does not select a first producer, source, delivery date or implementation sequence. It does not turn a feature join into evidence of actual model covariate use or predictive validity.

## Conformance and tracking

Record adoption separately for each named product/variant, with its code SHA, native-to-profile mapping, daily interpretation where dynamic, method version, software version, generated-data release identity, sources/configuration, manifest/artifact hashes, validation commands/results and reviewer decision. Verify key uniqueness, dimension preservation, units/support, null-versus-zero behavior, publication/recovery and a consumer round-trip without row expansion, silent resampling or future-data leakage. Scientific qualification remains a separate gate for the claimed use.

The [production readiness hub](../docs/production-readiness/README.md) retains the original dated assessment and drafts. Approval of these defaults is not evidence that any toolkit already conforms; no adoption status is changed by this documentation decision.
