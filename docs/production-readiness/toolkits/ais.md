# AIS toolkit charter and roadmap

Status: Draft for Tyler review, not adopted policy. Date: 2026-10-04.

## Purpose and desired outcome

Provide reproducible vessel-activity measurements that applications can join with environmental products without confusing vessel presence, sampling coverage, and human observation effort. The desired application output is a logical date × H3 × metric table, with additional identity dimensions retained wherever they distinguish observations. Static H3 × metric products are appropriate only for genuinely static reference context with declared applicability.

The first decision is ownership: either this repository becomes the maintained AIS producer through an agreed extraction from toolkit-human, or it remains a documented entry point to that producer. This draft does not authorize a competing adapter.

## Boundaries and non-goals

Distinct vessel counts cannot be summed across dates or cells. Distinct MMSI/hour proxies do not measure exact vessel duration, observer effort, or sightings. Ping-weighted speed depends on message frequency and filtering. AIS reception is an incomplete observation process; absence of messages cannot establish absence of vessels. Species occurrence, collision risk, disturbance, and detectability estimates are downstream interpretations requiring separately reviewed methods.

## Native data and application-facing H3 products

Retain native vessel/message identifiers, source, timestamps, position, units, filtering decisions, and aggregation inputs under their access restrictions. Publish an application projection with an auditable mapping to those native measures. Preserve dimensions needed to prevent false joins; H3 locates accepted observations and does not establish full-cell coverage.

Reuse the proposed [.github contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md). Its identity, H3 support, time boundaries, units, missingness, provenance, rights, checksums, and immutable publication rules are the starting point, not evidence of adoption. Native manifests remain authoritative until explicit adoption. Long versus wide layout, cadence, and application H3 resolution remain product-specific decisions. Daily/weekly resolution 6 is the current implementation baseline, not a universal requirement. Null never means zero. Record source retrieval, availability, version, and processing identities separately from observation time. Forecast issue/lead time and ensembles require a reviewed profile or contract revision; required semantics cannot be hidden in optional extensions.

## Current verified baseline

The complete [toolkit-ais tree at 57d705867668dd5e1c73e1977adb8d62fd6d8dea](https://github.com/MarineCast/toolkit-ais/tree/57d705867668dd5e1c73e1977adb8d62fd6d8dea) contains only AGENTS.md and README.md. It has no source, schema, export, package, tests, or CI implementation; the reviewed repository had no Actions runs.

The existing [AIS implementation in toolkit-human at c3431e7263c3ec48a3e157adca306baeefd67c32](https://github.com/MarineCast/toolkit-human/tree/c3431e7263c3ec48a3e157adca306baeefd67c32/src/human/activity_and_effort/ais) produces daily and weekly H3 resolution 6 products, including distinct vessels, distinct MMSI/hour proxies, and ping-weighted valid speed. Source endpoint, license, and completeness remain unresolved in its [source documentation](https://github.com/MarineCast/toolkit-human/blob/c3431e7263c3ec48a3e157adca306baeefd67c32/src/human/activity_and_effort/ais/DATA_SOURCES.md). These are code-backed capabilities in toolkit-human, not evidence that toolkit-ais is implemented or operational. No tests were run for this charter.

## Known and proposed metric families

Known metric families are vessel counts, activity proxies, and speed summaries. Proposed additions include explicit reception coverage and quality summaries, only when the source can support them. Classification-specific metrics require documented classifications and retained category dimensions.

## Science, quality and rights

Raw tracks and identifiers need a privacy and access review before release. Validate duplicate messages, implausible positions/speeds, time boundaries, sparse reception, category changes, and cross-cell/count aggregation. Publish limitations and coverage with every product.

## Dependencies

Dependencies are toolkit-human ownership, an approved source contract, authorized retention and redistribution, and explicit consumer acceptance rules.

## Phased milestones and acceptance tests

1. **Agree ownership and source.** Acceptance: Tyler approves the repository boundary, source rights, accountable maintainer, and one product definition; toolkit-human migration or continued ownership is explicit.
2. **Stabilize the existing measurements.** Acceptance: synthetic fixtures reproduce defined counts and speed weighting, distinguish missing coverage from zero, and demonstrate that daily distinct counts cannot simply produce weekly counts.
3. **Implement the application projection.** Acceptance: native-to-H3 mapping, full keys, units, interval semantics, missing reasons, manifest, artifact validation, and a consumer round-trip pass; deliberately incompatible inputs are rejected.
4. **Release one bounded product.** Acceptance: a clean-installed entry point processes an authorized source sample into an immutable, checksummed release with reproducible configuration, documented coverage, and a verified recovery procedure.

The acceptance suite must run in CI, including clean package installation and synthetic/offline contract tests; document any live or native-runtime checks separately.

## Unresolved decisions

Open decisions include extraction versus delegation to toolkit-human, source selection, rights, privacy controls, coverage estimation, metric names, cadence, resolution, and physical layout. No schedule is committed.

## Definition of done

The MVP is done when one owned, reproducible vessel-activity product meets those acceptance gates, preserves native evidence, and can be consumed without inventing effort or completeness. Passing schema validation alone is insufficient. Tyler must approve this charter before it governs repository work.
