# Approved application delivery defaults

**Approved by Tyler on 2026-10-04. This is the default target for application-facing toolkit products; toolkit conformance and application integration require separate evidence.**

Tyler approved the delivery shape with “Yes that is exactly what I mean. Let's make that the default contract.” He then approved daily dynamic delivery: “Then for time resolution -> yes let's default to daily for every dynamic variables”. Tyler also approved UTC calendar days with “yes utc makes sense to me.” These decisions narrow the application-facing target while preserving the broader [manifest contract v0.1](README.md). They do not adopt the eleven [draft toolkit charters](../docs/production-readiness/README.md), authorize implementation or migration, or establish scientific readiness.

## Approved defaults

| Aspect | Default target convention |
| --- | --- |
| Physical format | Wide Parquet: qualified metrics are columns, alongside identity, support and quality fields needed to interpret them. |
| Dynamic grain and cadence | Daily application-facing output for every dynamic variable: one row per H3 cell and declared UTC daily valid interval for a specified product variant. Each metric has a documented, scientifically valid daily aggregation or representation. |
| Daily calendar and label | UTC midnight inclusive to the next UTC midnight exclusive, using timezone-aware UTC boundary timestamps. The daily date label is the UTC interval-start date; it does not replace the boundaries. |
| Static grain | One row per H3 cell for a specified product variant, with metric columns and a declared reference period/applicability. Do not fabricate a row-level date. |
| Resolution | One H3 resolution per published table. Viewshed and related Human/viewability variables retain R7 under the approved exception below. Broader numerical policy and assignments remain pending; the exploratory direction is not approval of fixed R6 or R5/R4 assignments. |
| Metric naming | Readable `lower_snake_case` names with quantity, statistic and unit where applicable; precise definitions remain in the manifest. Identifiers, status and categorical fields do not acquire invented physical units. |
| Missingness and status | Missing values stay null, never become zero. Each metric has an accurate status distinguishing valid, unavailable, unknown, not applicable or partial; v0.1 encodes valid as `observed`. Partial estimates carry defined coverage. |
| Companion manifest | Describe units, methods, source data, quality rules and versions, together with v0.1 identity, spatial/temporal support, missingness, provenance, rights, configuration, exact artifact checksums and limitations. |
| Necessary dimensions | Preserve species, depth, source/target roles and other distinguishing dimensions in native companions or explicit, independently identifiable product variants, with auditable projections or reductions. |

The default grain applies within a fully specified variant. Species or depth layers cannot become duplicate cell/day rows in an apparently unqualified product. Publish separately identified variants with recoverable native evidence, or propose a reviewed richer profile with those dimensions in its key. A directed source-target companion remains a pair product; a cell summary needs an explicit role and scientifically justified reduction. Never discard axes, select arbitrary first rows, or hide row-varying identity in manifest metadata to fake unique cell keys. A manifest may describe a constant variant, but cannot replace distinguishing values that vary across rows.

Wide storage does not make unlike quantities interchangeable. Definitions retain units, datum, statistic, support, missingness and quality. Preserve unknown, unavailable, partial and not-applicable states separately from observed zero. Native observations, pairs, rasters, graphs, geometry and nonspatial records remain available where required; the application table must have a traceable relationship to them.

## Daily delivery and native temporal support

Daily is the approved application cadence, not a claim that every source observes daily. Preserve the native sampling/reporting cadence and intervals in companion evidence. Each daily metric must define its statistic or representation, weighting, completeness, partial-period handling and relation to native evidence; a date label alone cannot establish that meaning.

For subdaily sources, specify an appropriate daily reduction rather than dropping samples or assuming an arithmetic mean fits every quantity. Slower sources require a declared interval-applicability or carry-forward rule only where scientifically justified; otherwise affected days remain unavailable with explicit reasons. Retain the original observation interval, vintage and availability, label carried values by their actual interpretation, and avoid future-data leakage. Do not invent daily observations, divide monthly totals arbitrarily, silently forward-fill, or imply daily measurement support that the source lacks.

UTC calendar days are approved: each daily interval is **[00:00 UTC, next 00:00 UTC)**. Declare `temporal.timezone` as `UTC` and represent boundary timestamps as timezone-aware UTC values, using RFC 3339 `Z`/`+00:00` strings or equivalent aware Parquet timestamps. The daily date label is the UTC date of the inclusive interval start, with its field and definition declared in the manifest. For example, label `2026-10-04` denotes `[2026-10-04T00:00:00Z, 2026-10-05T00:00:00Z)`. A label cannot replace actual interval boundaries or make unlike temporal support compatible.

Explicitly labeled local-day exceptions require a reviewed aggregation/profile and declared calendar zone, boundaries and label meaning. Local days can be 23 or 25 hours; do not silently relabel them as UTC days or merely change their date labels. Mapping native local-day support to the UTC target requires a justified transformation; preserve the original support and report unavailable output where the evidence cannot support the conversion. Existing v0.1 local-day/native products remain valid under their contracts but do not automatically conform to the UTC default.

The UTC decision does not approve an aggregation method or global completeness threshold. Metrics in one row must have compatible declared daily support; incompatible support requires separate products or a reviewed transformation. Slower native applicability remains documented even when a justified daily representation is provided.

## Metric naming and definitions

Tyler approved readable quantity/statistic/unit naming, illustrated by `temperature_mean_c`, `wind_speed_mean_m_s` and `depth_mean_m`, with full definitions in the manifest. Use readable `lower_snake_case` names; include statistic and unit components where they actually apply. Identifiers, status and categorical fields must not invent physical units or numerical statistics to fit the pattern.

Names and manifest definitions must identify the exact quantity. Air versus water temperature, measurement height, depth sign/vertical datum, statistic, support and unit cannot remain ambiguous. For example, use an air/water qualifier where needed instead of placing indistinguishable `temperature_mean_c` quantities in one consumer namespace; the manifest retains the precise scientific definition and method. A unit suffix does not authorize conversion or establish what a measurement means.

Keep v0.1's namespaced product identity and explicit variant identity for collision prevention. Consumers must qualify fields by their product/variant and reject ambiguous column collisions; a readable column name alone is not a global registry. Exact product names and any shared registry still require review. This documentation decision does not rename existing toolkit fields, migrate data or approve code changes; future mappings must be explicit and independently validated.

## Approved missingness and coverage semantics

Tyler approved the missingness proposal with “Yes this works”: missing values remain null rather than becoming zero; each metric has a status distinguishing valid, unavailable, unknown, not applicable or partial; zero represents a genuinely valid zero; partial estimates include coverage. These are approved semantic defaults, not evidence that existing producers already support them.

For v0.1 manifests and artifacts, map the user-facing word **valid** to the existing enum code **`observed`**. This code already covers a valid measurement or derived result, including a true zero; it does not imply that a value is a raw observation. Retain source/method provenance and labels that distinguish measurements, estimates and derived quantities. Do not rename the v0.1 enum to `valid`, add a new `missing` code, or change schema version `0.1` by implication.

| User-facing meaning | v0.1 code | Value rule |
| --- | --- | --- |
| Valid | `observed` | Non-null valid measurement or derived result; numeric values are finite. Zero is allowed only when valid for the defined quantity and support. |
| Unavailable | `unavailable` | Null; expected source or result was unavailable. |
| Unknown | `unknown` | Null; reason or state is unknown. |
| Not applicable | `not_applicable` | Null; the quantity does not apply to the row. |
| Partial | `partial` | Finite estimate or null from incomplete support, accompanied by explicit coverage meaning/evidence and a documented interpretation. |

A missing value is null and must be classified by its actual reason; absence is not observed zero. Each metric needs a non-null status accurate for that metric on every row. A shared status column is permitted only when its state is correct for **every referencing metric on every row**. Otherwise use separate per-metric status columns; family-level availability cannot stand in for metric-level completeness.

For nullable metrics, v0.1's declared `missing_reason_field` links to the status column with the existing exact enum. For non-nullable metrics, declare any profile-required status column and its relationship in existing field descriptions; v0.1 forbids `missing_reason_field` when `nullable` is false. Review the profile's semantic associations without inventing unknown core fields or relaxing strict validation.

Partial coverage must describe what was available against what was expected: support interval/domain, numerator, denominator, units, weighting and calculation method, including the metric-specific gaps and effect on the estimate. Counts, duration, area or another justified measure may be appropriate; no universal percentage, minimum threshold or averaging rule is selected. A finite partial estimate must carry inspectable coverage for its declared support. Partial null outputs retain available coverage evidence and explicit gaps; unknown coverage is reported as unknown rather than fabricated. Coverage and quality fields are declared and preserved with their metric relationship in the manifest and consumer round-trip.

This approval does not implement statuses/coverage, certify a producer, or approve toolkit migration. Product-specific coverage methods, acceptance thresholds and scientific eligibility remain reviewed decisions. The v0.1 schema, `observed` semantics and existing fixtures remain unchanged.

## Relationship to manifest contract v0.1

This is a delivery profile and decision record, not a new manifest schema version. The v0.1 JSON Schema and synthetic examples are unchanged. Valid CSV, instantaneous, directed-pair and other native/legacy products within v0.1's scope remain valid under that contract; they do not automatically meet this narrower wide-Parquet static/daily-interval target. Existing native contracts remain authoritative until an owning toolkit deliberately implements and validates a mapping.

For a conforming cell product, map its complete unique, non-null key to `identity.primary_key`, its single index field/chosen resolution to `spatial`, all columns to `fields`, and its finished Parquet artifact to `artifact`. Dynamic keys include both interval boundaries as v0.1 requires; the approved daily profile uses half-open **[start, end)** UTC calendar intervals and the UTC interval-start date label. Static products use v0.1's applicability meaning. Labels cannot replace boundaries. UTC calendar approval leaves the scientific aggregation method pending; v0.1's broader timezone and optional-label scopes remain unchanged.

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

## Approved R7 exception

Tyler approved: “viewshed can stay at res 7 (and the related human variables).” Viewshed and related Human/viewability variables therefore retain R7. This is a specific approved resolution exception, not a decision that all Human products move to R7; AIS and unrelated Human products are not reassigned by it. The exact mapping of named Human products to this viewability-related scope must be documented in their conformance records without widening the approval.

Each published table still declares one resolution. Cross-resolution use requires an explicit adapter and reviewed support/reduction rules, with validation of keys, row counts, units, nulls and scientific meaning. Do not silently join R7 with coarser cells, copy coarse values into R7/R6 as if they gained detail, or claim that a cross-resolution adapter is already implemented. This exception does not change the approved daily application cadence for dynamic variables or the static grain for static variables.

## Decisions still pending

Approval selects the delivery shape, daily dynamic cadence, UTC calendar boundaries/labels, readable metric naming pattern, missingness/status semantics with partial coverage and scoped R7 exception. Product review must still decide:

- Interval aggregation/representation, weighting, completeness and partial-period rules; any explicitly labeled local-day exception requires a reviewed aggregation/profile. The default UTC calendar and boundaries are approved.
- Broader numerical H3 resolution policy and product assignments beyond the approved R7 exception, geographic domain and spatial support/assignment or conversion methods. No fixed R6 or R5/R4 assignments are approved.
- Exact per-product metric names, any common registry and explicit field mappings/migrations; the readable quantity/statistic/unit naming pattern is approved, with full manifest definitions.
- Product-specific coverage calculations, QC implementation and code changes; semantic status defaults are approved through the unchanged v0.1 codes, including `observed` for valid values.
- Forecast profiles, issue/lead-time and ensemble handling; this approval does not approve a forecast profile.
- Scientific thresholds, source qualification, rights, release audience and product eligibility.

The decision does not select a first producer, source, delivery date or implementation sequence. It does not turn a feature join into evidence of actual model covariate use or predictive validity.

## Exploratory resolution direction

Tyler described this discussion as “just thinking out loud here”: R6 is the usual starting point under consideration, with scientifically justified per-product R5 or R4 exceptions where appropriate. Weather, oceanography and other time-varying products with many metrics are candidates for that tradeoff, not assigned resolutions. Broader policy and R6/R5/R4 product choices remain pending, beyond the separately approved R7 exception.

Evaluate native spatial support/detail, scientifically important gradients retained or lost, and expected cell counts, daily row counts, metric width, memory and storage costs. Coarser resolution needs a defensible product-specific method; cost alone does not establish scientific adequacy. Each published table still declares one resolution. Consumers require an explicit mapping that preserves support and meaning; do not force R6 replication of coarse values or treat it as added detail. Any conversion or join remains subject to the existing compatibility and acceptance checks.

## Conformance and tracking

Record adoption separately for each named product/variant, with its code SHA, native-to-profile mapping, daily interpretation where dynamic, method version, software version, generated-data release identity, sources/configuration, manifest/artifact hashes, validation commands/results and reviewer decision. Verify key uniqueness, dimension preservation, units/support, per-metric value/status consistency, partial-coverage meaning, null-versus-zero behavior, publication/recovery and a consumer round-trip without row expansion, silent resampling or future-data leakage. Scientific qualification remains a separate gate for the claimed use.

The [production readiness hub](../docs/production-readiness/README.md) retains the original dated assessment and drafts. Approval of these defaults is not evidence that any toolkit already conforms; no adoption status is changed by this documentation decision.
