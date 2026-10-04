# Human activity and observation opportunity charter and roadmap

Status: Draft for Tyler review, not adopted. Assessment date: 2026-10-04. Milestones are proposed gates, not delivery commitments.

## Purpose and desired outcome

Produce traceable human activity, access and observation-opportunity inputs for MarineCast applications. Consumers should be able to distinguish where people or platforms could observe from where observation and reporting actually occurred. Success means reproducible, documented products whose limitations survive downstream joins and modeling.

## Boundaries and non-goals

This toolkit does not establish whale abundance, occupancy, detection probability or measured observer effort from population, ferry service or AIS traffic. Direct observer effort, reporting capture, whale-watch tracks and reconstructed sea state remain unavailable. Ferry and passenger AIS are not deduplicated. AIS ownership between this repository and toolkit-ais remains an explicit decision; no extraction is presumed.

## Native data and application-facing H3 products

Preserve source tables, vintages, route identities, source/target cells and manifests. The application target is logical date × H3 × metric, or static H3 × metric, using the [proposed organization contracts v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md). This is not approval of a universal physical schema. Long versus wide storage, cadence and resolution require product-specific approval. Intermediate dimensions must survive until a documented reduction applies.

Native manifests remain authoritative pending adoption. Propose a reviewed contract profile/revision retaining observation/service time, availability, source vintage/identity, code/configuration identity and release/artifact checksums. Forecast issue/horizon semantics are deferred in v0.1 and need explicit revision if required; do not label historical proxies forecasts. Preserve distinct unknown/unavailable/not-applicable/partial statuses and nulls, never automatic zeros. Keep measurements separate from interpretations.

## Current verified baseline

The assessed head is `c3431e7263c3ec48a3e157adca306baeefd67c32`. The [static exporter](https://github.com/MarineCast/toolkit-human/blob/c3431e7263c3ec48a3e157adca306baeefd67c32/src/human/static_matrix.py) produces unique `(H3_INDEX, H3_RESOLUTION)` R7 rows, with wide population, boat-launch, public-shore and places components. Outer joins retain nulls; native manifests and artifact checksums are checked. Population retains US-2020 and Canada-2021 vintages. Places count catalog records, not deduplicated sites. Products remain research/model-ineligible with no marine transfer.

Dynamic AIS and land/target-water opportunity use daily or weekly R6; water-source opportunity uses R7. Ferry intermediates retain `service_date × route_key × source_h3`; static viewability retains source-cell × target-cell pairs. The [opportunity contract](https://github.com/MarineCast/toolkit-human/blob/c3431e7263c3ec48a3e157adca306baeefd67c32/src/human/activity_and_effort/observation_opportunity_contract.py) separates physical viewability, platform activity, weather and reporting.

[Exact-head CI](https://github.com/MarineCast/toolkit-human/actions/runs/36844920597) fails both Python versions. The inspected Python 3.11 log reports 325 passed, 2 failed and 6 skipped: unavailable GDAL `ViewshedGenerate` and a stale `orcacast` import. Wheel/smoke stages did not run. No tests were executed to prepare this draft.

## Known and proposed metric families

Implemented families include static access/population, viewability, service/platform opportunity, distinct AIS vessels, distinct MMSI-hour proxies and valid ping-weighted speed. MMSI-hour proxies are not exact durations. Proposed work is an approved application adapter, explicit units/reductions, coverage indicators and availability-safe exports. Calibrated effort or detection metrics require new evidence and separate review.

## Science, quality and rights

The [AIS source record](https://github.com/MarineCast/toolkit-human/blob/c3431e7263c3ec48a3e157adca306baeefd67c32/src/human/activity_and_effort/ais/DATA_SOURCES.md) leaves acquisition, license and completeness unresolved. Require source-specific rights and completeness evidence before publication. Preserve provenance and missingness through temporal/spatial aggregation. Conservation tests establish arithmetic behavior, not empirical detection validity. Keep research restrictions until independent validation supports a narrower approved use.

## Dependencies

Dependencies include approved H3 domains, source rights and inventories, supported GDAL/OSRM environments, consumer contract decisions and the AIS ownership decision. Viewability and opportunity interpretation additionally depend on defensible source/target geometry and weather/reporting inputs.

## Phased milestones and acceptance tests

1. Repair baseline execution. Accept when both supported CI versions, installed-wheel/outside-checkout smoke and relevant GDAL/OSRM integration checks pass; each remaining skip has an owner and documented limitation.
2. Specify application products. Accept reviewed metric units, keys, cadence, resolution, null/zero rules and lossless dimension mappings against contracts v0.1.
3. Build and validate adapters. Accept unique requested keys, duplicate/timezone fixtures, weekly completeness checks, R6-to-R7 conservation and retained-source reproducibility with checksum-bound artifacts.
4. Review release eligibility. Accept source-rights evidence, real-data coverage checks, freshness rules and held-out validation appropriate to each claimed use. Unsupported effort/detection claims stay excluded.

## Unresolved decisions

Tyler must approve AIS ownership, priority consumer products, grid/reduction rules, physical format, source licensing path, publication scope and criteria for any model-eligible interpretation.

## Definition of done

A product is done only when its approved contract, reproducible artifact, passing gates, provenance, rights and limitations are reviewable together, and a consumer fixture demonstrates correct availability-aware use without dropping dimensions or turning unknowns into zero.
