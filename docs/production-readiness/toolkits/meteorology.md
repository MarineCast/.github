# Meteorology: proposed charter and roadmap

**Draft for Tyler review · 2026-10-04 · Not adopted policy.** Milestones are proposed acceptance gates, not delivery commitments or completed validations.

## Purpose and desired outcome

Provide reproducible weather and astronomical context with explicit spatial, temporal and availability semantics. Deliver application-facing **date/interval × H3 × metric** products from preserved native evidence. A convenient daily label must not conceal the actual observation window, source sampling, local calendar or forecast vintage.

## Boundaries and non-goals

Own meteorological/astronomical quantities and declared transformations. Do not interpret weather as observer effort or detection probability. Nearest native-grid samples are point samples, not cell-area averages. A sampled precipitation estimate is not measured 24-hour accumulation. Future forecast products must retain issue, valid and lead times separately; they cannot be represented safely by a date alone.

## Native data and application-facing H3 products

Retain source grid/sample identity, height where relevant, valid time and processing mode. Do not silently resample R4 into R5 or wet-only support. Long/wide layout, consumer cadence, resolution and permitted reductions remain open decisions. Preserve units, vector conventions, sample counts, coverage and quality alongside values.

## Current verified baseline

Reviewed snapshot: [`3bbcee964ffdb4ba99c8cc427797749df6e481c3`](https://github.com/MarineCast/toolkit-meteorology/tree/3bbcee964ffdb4ba99c8cc427797749df6e481c3).

The [daily matrix](https://github.com/MarineCast/toolkit-meteorology/blob/3bbcee964ffdb4ba99c8cc427797749df6e481c3/src/meteorology/daily_matrix.py) outer-joins component-prefixed fields by `DATE`, `H3_INDEX`, `H3_RESOLUTION`. Weather/lunar products use R5 and daylight R4; the result is not one spatially aligned R5 cube. It validates native resolution and common dates, preserving unsupported combinations as null. Meteorology's land-and-water domain also differs from wet-only ocean support.

The separate [hourly product](https://github.com/MarineCast/toolkit-meteorology/blob/3bbcee964ffdb4ba99c8cc427797749df6e481c3/src/meteorology/hourly_weather/product.py) uses H3 × valid UTC time, local dates and complete 23/24/25-hour days; it is not included in the daily matrix. It retains decoded-grid evidence/crosswalks. Availability is based on an assumed lag, not observed provider publication.

Existing [exact-head CI](https://github.com/MarineCast/toolkit-meteorology/actions/runs/37120074793) passed Linux Python 3.11–3.13 and clean external-wheel synthetic daily checks. Transactional generations/checksums exist. The [implementation tracker](https://github.com/MarineCast/toolkit-meteorology/blob/3bbcee964ffdb4ba99c8cc427797749df6e481c3/docs/IMPLEMENTATION_TRACKER.md) records synthetic evidence; full real-source compatibility and empirical acceptance remain unqualified. No fresh runs occurred in this review.

## Known and proposed metric families

- **Implemented:** daily weather, lunar and daylight families; hourly weather with retained source samples. Weather includes temperature, wind, visibility, pressure and precipitation-related fields with declared units and limits.
- **Known method limits:** daily weather samples six nearest-grid time points; f00 analyses and f01 precipitation-rate provenance differ. Wind direction follows mean U/V and is null for calm conditions.
- **Proposed:** qualify the existing hourly path first; add a reviewed reduction to the selected consumer cadence. Genuine forecast products require a separate approved forecast profile and source qualification.

## Science, quality and rights

Adopt the proposed [MarineCast contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md) only through reviewed mapping and round-trip tests. Mixed-resolution and forecast/ensemble profiles are deferred there; use separate conforming products or a reviewed revision, never drop dimensions. Preserve native manifests and distinguish contract/product/code versions, release identity, configuration, source vintage and artifact checksums.

Availability assumptions must be explicit and conservative; historical replay cannot use later revised or later-issued data. Null, partial, unavailable and observed zero remain distinct.

## Dependencies

Dependencies include supported acquisition/geospatial runtimes, provider coverage/rights, retained GRIB evidence and independent comparison stations/buoys.

## Phased milestones and acceptance tests

1. **Fix product scope and error contracts.** Select variables, domain, source eras and acceptable cadence/resolution. Acceptance: reviewed metric register, unsupported-domain map, deterministic failures and fixture tests for units, vectors, missingness and mixed resolutions.
2. **Qualify hourly acquisition.** Run a bounded, budgeted full-core GRIB sample spanning relevant seasons/source eras and DST. Acceptance: reproducible immutable replay, exact timestamp/sample identity, 23/24/25-hour completeness and explicit failure for missing expected evidence.
3. **Validate scientific quantities.** Compare matched stations/buoys using reviewed location, height, time and quality rules. Acceptance: preset thresholds, bias/error/coverage results, retained disagreements and supported-domain limits; precipitation labels match their actual statistic.
4. **Publish and adapt.** Define allowed temporal/spatial reductions and availability policy. Acceptance: vector/interval reconciliation, no future-data leakage, checksum/mutation/rollback negatives, clean install and row-preserving consumer join. Prove actual model use separately.

## Unresolved decisions

Review first variables/domain, source budget, empirical thresholds, source-publication versus assumed availability, forecast scope and grid/cadence conversion. Northern-domain coverage needs explicit qualification rather than extrapolation.

## Definition of done

Done means one bounded, rights-cleared, reproducible real-source product passes software, source-compatibility, scientific and consumer gates separately. Synthetic volume and green CI alone do not establish meteorological accuracy.
