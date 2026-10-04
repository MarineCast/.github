# MarineCast Production Readiness Assessment

Repository review and proposed delivery plan

Prepared for Tyler  |  4 October 2026

## The requested outputs are partly implemented

Seven of the eleven toolkits contain substantive implementations. Several already produce static H3 tables or time by H3 metric tables. Four repositories remain scaffolds. MarineCast does not yet have a verified, uniformly consumable production release across all eleven toolkits.

The next step is to agree the shared product contract and qualify one complete producer to consumer path, while fixing known correctness and publication blockers. A universal long table is not a prerequisite. Existing wide tables can satisfy the requested logical dimensions when metric identities, units, keys, time and support are explicit.

### What the review changes

- Seascape, Human and Governance already expose static H3 matrices. Viewshed already provides H3 reductions of its pair tables. Marine Mammals already produces period by H3 count products. These should be completed and adapted, rather than rebuilt solely for table shape.

- Viewshed has a current-main lineage defect and a source-derived visible-count defect. Human current-main CI fails. Oceanography needs fail-closed publication. These warrant concrete acceptance work before unattended use.

- Hydrology, AIS, Salmon and Acoustics need first products. AIS functionality in Human and river-related functionality elsewhere require ownership decisions before duplicate implementations are started.

- A valid export is distinct from validated scientific meaning and actual use by OrcaCast. Neither green CI nor a successful feature join establishes calibrated occurrence, abundance, detection probability or covariate use in a model.

### Decision requested

Approve the proposed implementation sequence and select a first product, bounded geographic domain, H3 resolution and consumer cadence. The user requirement is dynamic date × H3 × metric or static H3 × metric. It does not yet fix daily versus weekly cadence, resolution, long versus wide storage, or scientific eligibility thresholds.

### Evidence boundary

This assessment is a read-only inspection of repository source, contracts, schemas, tests and existing GitHub Actions evidence at the snapshots in the final register. No repository changes, fresh tests, provider acquisition, regional pipeline runs, benchmarks or scientific validation were performed for this assessment. Findings are evidence-based readiness judgments, not an exhaustive audit.

## Production readiness by toolkit

Readiness describes the inspected implementation, not scientific certification. Existing H3 tables are credited below. Extra dimensions and native products must remain available wherever reducing them would change meaning.

| Toolkit | Existing output | Readiness and next acceptance |
| --- | --- | --- |
| Seascape | Static wide H3 matrix, R6/R8; native graphs and objects. | Advanced exporter. Qualify a source-backed release with current methods; preserve exact support, QC and uncertainty. |
| Viewshed | Static source–target pairs and role-qualified H3 summaries, default R7. | Implemented with blocking defects. Fix stale-factor lineage and visible counts; qualify sensitivity and input coverage. |
| Meteorology | Daily mixed R4/R5 matrix; hourly weather by valid time and H3. | Advanced research producer. Align declared spatial profiles and qualify real-source compatibility, availability and accuracy. |
| Oceanography | Daily per-family H3 metrics and QC at R5/R6; seven families. | Implemented with publication gaps. Stabilize schemas, preflight and fail-closed atomic releases before live qualification. |
| Hydrology | None in dedicated repository. | Scaffold. Decide gauge/catchment versus marine-influence ownership; implement one native and justified H3 product. |
| Human | Static R7 matrix; daily/weekly R6 and R7 opportunity products. | Implemented, current CI blocked. Repair runtime/import checks; preserve grid, proxy and source-rights limits. |
| AIS | None in dedicated repository; AIS code exists in Human. | Scaffold. Resolve extraction/ownership; establish licensed traffic metrics with receiver and temporal coverage. |
| Governance | Static supplied-grid H3 counts, geometry fractions and attribute sets. | Bounded reference exporter. Validate six real-source families and atomic publication; legal-time semantics remain separate. |
| Marine Mammals | Observation facts; daily/weekly H3 counts, R4/R5/R6; annual pod census. | Implemented count layer. Expose an eligible consumer profile, retain variants and verify support, rights and reporting meaning. |
| Salmon | None. | Scaffold. Define one native species/stock/site product and justify any marine H3 proxy. |
| Acoustics | None. | Scaffold. Define a calibrated sensor measurement or detection product with effort and footprint semantics. |

### What complete means

A selected product is production-ready only after its schema and semantics are stable, the installed producer and adapter are verified, publication fails safely, source rights and provenance are sufficient, and a bounded real-data validation meets reviewed tolerances. Completion applies to named products and supported domains, not automatically to every capability suggested by a repository name.

The next sections give concrete work and acceptance criteria. The final register pins all eleven toolkit snapshots and separates existing CI evidence from verification still to be run.

## Spatial foundations

### Seascape

The static matrix is one row per H3\_INDEX and H3\_RESOLUTION with namespaced product metric columns, currently defaulting to R6 and R8. It resolves an immutable audited schema 3 release, verifies checksums and support, preserves nulls and separate quality evidence, and writes atomically. Bathymetry pixels are aggregated directly at each resolution. R8 water-overlap support and the R6 parent union are not interchangeable sampling definitions.

Exact-head CI passes, including Linux and macOS ARM64 clean-consumer checks, tests, documentation and notebook checks. Release v0.1.1 exists. Python support is narrowly 3.14 and rasterio is capped below 1.5.2. The macOS runner concern is future maintenance, not a current failed gate.

Production acceptance: publish a bounded source-backed schema 3 release using current methods; verify exact unique H3 support, units, datum, vintages, rights, checksums and selected raw-source values against independent calculations. Recent corrected methods and optional additions are fixture-tested, while checked-in catalogs describe older materializations. Unsupported hardness and habitat quantities must stay unavailable. Qualify the native runtime and replacement ARM64 runner, then verify a consumer adapter without inventing dates or dropping QC and uncertainty.

Evidence: [Matrix implementation](https://github.com/MarineCast/toolkit-seascape/blob/162bc906a3e6cd73146870e9c2e343cacf62e0bb/src/seascape/metric_matrix.py)  |  [Support tests](https://github.com/MarineCast/toolkit-seascape/blob/162bc906a3e6cd73146870e9c2e343cacf62e0bb/tests/test_metric_matrix.py)  |  [Scientific coverage](https://github.com/MarineCast/toolkit-seascape/blob/162bc906a3e6cd73146870e9c2e343cacf62e0bb/docs/capability-coverage.md)

### Viewshed

Native outputs are static source H3 by target H3 pairs with land and water roles, normally R7 within a 30 km candidate universe. Per-source and per-target H3 summaries already exist. Preserve role, reduction, candidate population and the pair companion. Summed opportunity scores can exceed one and are not probabilities. Noncandidate absence is not modeled zero; KNOWLEDGE\_TIME\_UTC describes build knowledge, not observation time.

Blocking source finding: overwrite finalization can combine retained factors with current configuration without trusted producer-lineage validation, relabeling stale factors. PR 11 addresses this but was unmerged at review. A separate source-derived count defect uses n\_unique over values including null, so blocked groups can count an extra source. This was inferred from code and documented Polars semantics; it was not locally reproduced.

Production acceptance: merge lineage checks with mutation, reuse, overwrite and rollback regressions; fix counts so all-blocked groups are zero and mixed/all-visible groups are exact; compare role-qualified H3 output with pair reductions. Existing exact-head CI passes. Committed San Juan evidence covers 5,424 pairs but reports 9.69 percent missing mapped-land canopy pixels using zero-height fallback. Require sensitivity envelopes, independent line-of-sight checks, coverage thresholds and a bounded production-scale run before scientific qualification.

Evidence: [H3 summaries](https://github.com/MarineCast/toolkit-viewshed/blob/0c0c33b60ab34f6e22d87ff235538d82112f2589/src/viewshed_toolkit/pipeline/finalize/aggregate.py)  |  [Finalization lineage](https://github.com/MarineCast/toolkit-viewshed/blob/0c0c33b60ab34f6e22d87ff235538d82112f2589/src/viewshed_toolkit/pipeline/finalize/final_artifacts.py#L1137-L1250)  |  [Visible counts](https://github.com/MarineCast/toolkit-viewshed/blob/0c0c33b60ab34f6e22d87ff235538d82112f2589/src/viewshed_toolkit/pipeline/weights/view_score.py)  |  [Existing real-run evidence](https://github.com/MarineCast/toolkit-viewshed/blob/0c0c33b60ab34f6e22d87ff235538d82112f2589/docs/reports/real-data-examples-validation.md)

Evidence: [Unmerged PR 11](https://github.com/MarineCast/toolkit-viewshed/pull/11)  |  [Polars null count semantics](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.n_unique.html)

## Environmental producers

### Meteorology

The daily matrix joins DATE, H3\_INDEX and H3\_RESOLUTION with component prefixes and coverage checks. Weather and lunar products are R5; daylight is R4. It is a valid mixed-resolution table, not a spatially aligned R5 cube. Land and water support also differs from Oceanography’s wet-only domain. Hourly weather is a separate valid-time by H3 product requiring complete 23, 24 or 25 hour local days; it is not included in the daily matrix.

Weather values use nearest native-grid samples, not cell-area averages. The daily path uses six samples and distinguishes f00 analysis from f01 precipitation-rate provenance; its precipitation estimate is not a measured 24 hour accumulation. Availability uses an assumed lag, not measured provider publication. Units, transformations, missingness and limits are documented, and generation publication is transactional.

Existing exact-head CI passes Linux Python 3.11 to 3.13 and a clean outside-checkout wheel on synthetic daily inputs. Committed evidence records 168 synthetic hours and 75,600 rows over 450 cells. Real HRRR compatibility and empirical acceptance remain NOT\_RUN; earlier buoy and astronomy comparisons are limited, and northern-domain evidence is incomplete.

Acceptance: after stable contract and error behavior, qualify the existing hourly path using a budgeted set of full-core GRIB inputs across eras, seasons and daylight-saving transitions. Publish a supported-domain map and immutable replay; compare matched station or buoy values with reviewed height, time and QC rules and predeclared tolerances. Keep installation, source compatibility and scientific accuracy as separate checks.

Evidence: [Daily matrix](https://github.com/MarineCast/toolkit-meteorology/blob/3bbcee964ffdb4ba99c8cc427797749df6e481c3/src/meteorology/daily_matrix.py)  |  [Hourly product](https://github.com/MarineCast/toolkit-meteorology/blob/3bbcee964ffdb4ba99c8cc427797749df6e481c3/src/meteorology/hourly_weather/product.py)  |  [Recorded qualification status](https://github.com/MarineCast/toolkit-meteorology/blob/3bbcee964ffdb4ba99c8cc427797749df6e481c3/docs/IMPLEMENTATION_TRACKER.md)

### Oceanography

Seven daily families cover tide proxies, SalishSeaCast currents, river influence, satellite SST and chlorophyll, HYCOM currents and DFO harmonics. Family tables use DATE, H3\_INDEX and H3\_RESOLUTION at R5 or R6 with metric QC. Satellite pixel-centre assignment and cosine-latitude weighting are not exact polygon intersections. Tide and river kernels use R8 water paths with water-area aggregation to R6.

Blocking source findings: caught build errors can produce unavailable tables without stable metric columns; the CLI ignores family status and can return success; data and manifests publish separately. The catalog omits newer families, preflight is incomplete, and fingerprints omit normalization and configuration helpers. FEATURE\_STATUS means any metric is available, not every metric. Provider-day discharge and UTC semantics differ; availability is unknown and forecast eligibility is false. A seven-day chlorophyll composite can contain one valid day.

Acceptance: enforce identical success and unavailable schemas for all seven families, complete the registry and preflight, fail required families with a nonzero exit, and publish one atomic generation with rollback and comprehensive portable fingerprints. Then qualify bounded seasonal replay against independent tides, currents and gauges. Existing research CI passes, but system-site wheel smoke, optional tide dependencies and standalone live replay remain unqualified.

Evidence: [Family orchestration](https://github.com/MarineCast/toolkit-oceanography/blob/c378eb7f580e34bad0161cc023d4ecb5cd90238f/src/oceanography/build.py)  |  [CLI result handling](https://github.com/MarineCast/toolkit-oceanography/blob/c378eb7f580e34bad0161cc023d4ecb5cd90238f/src/oceanography/cli.py)  |  [Metric catalog](https://github.com/MarineCast/toolkit-oceanography/blob/c378eb7f580e34bad0161cc023d4ecb5cd90238f/config/feature_catalog.yaml)

### Hydrology

The dedicated repository contains only README and banner assets, with no implemented output or CI. Decide ownership of native gauges and catchments versus Oceanography’s marine influence. The first product needs provider-day rules, units, gauge-to-mouth provenance, explicit nulls, an installable CLI and a reproducible source fixture. H3 gauge location alone does not validate marine influence.

## Human activity and governance

### Human

Human is implemented. Its static R7 matrix outer-joins population, boat-launch access, public-shore access and places with checksum and key validation. Missing support stays null. Population retains US 2020 and Canada 2021 vintages; places count catalog records rather than deduplicated physical sites. The export explicitly remains model-ineligible and performs no marine transfer.

Daily and weekly AIS and land or target-water opportunity tables exist at R6; water-source opportunity uses R7. Ferry and viewability intermediates retain route or source-target dimensions. Vessel-hour proxies are neither exact durations nor measured observer effort. Legacy AIS rights, endpoint and completeness are unresolved. Direct observer effort, reporting capture, whale-watch tracks and reconstructed sea state remain unavailable; ferry and passenger AIS are not deduplicated.

Current-main CI fails on Python 3.11 and 3.14. The inspected 3.11 log has 325 passed, 2 failed and 6 skipped: unavailable GDAL ViewshedGenerate and a stale OrcaCast import test. Later wheel and smoke steps do not run. Acceptance: repair the independent-package test, provision supported GDAL and OSRM, pass both CI versions and installed-wheel/native tests without silently skipped production prerequisites, then verify sanctioned grid conversion, units, conservation and null semantics. Opportunity outputs require separate held-out effort or detection validation.

Evidence: [Static export](https://github.com/MarineCast/toolkit-human/blob/c3431e7263c3ec48a3e157adca306baeefd67c32/src/human/static_matrix.py)  |  [Observation contract](https://github.com/MarineCast/toolkit-human/blob/c3431e7263c3ec48a3e157adca306baeefd67c32/src/human/activity_and_effort/observation_opportunity_contract.py)  |  [AIS source limits](https://github.com/MarineCast/toolkit-human/blob/c3431e7263c3ec48a3e157adca306baeefd67c32/src/human/activity_and_effort/ais/DATA_SOURCES.md)

### AIS

The dedicated AIS repository contains only README and AGENTS files, with no implemented exporter, package or CI. Decide whether to extract and harden Human’s AIS adapter or keep shared ownership. Then implement one licensed traffic product with receiver and temporal coverage. Acceptance must cover distinct-vessel reductions, duplicate pings, time zones, unknown versus zero, retained-source fixtures and an installable wheel. Traffic must not be relabeled measured observer effort.

### Governance

Six native geometry families are implemented; the 24-entry catalog also includes planned families. The optional static H3 exporter already provides counts, unioned polygon coverage fractions, line metres, point counts and attribute sets on a supplied grid. Partial or unknown inventories retain null intersections. Attribute sets are not aligned feature records, and antimeridian grids are unsupported.

Exact-main CI, installed-wheel and outside-checkout smoke pass. This is an unfiltered inventory snapshot, not effective-date legal reconstruction; outputs remain model-ineligible. Native multi-file publication has no global atomic generation pointer. Acceptance: validate all six real-source products, rights and freshness against independent overlays; publish a checksum-bound atomic generation. Add reviewed effective and knowledge-time rules only if date-specific regulation is required. Geometry coverage is not legal protection probability.

Evidence: [H3 export](https://github.com/MarineCast/toolkit-governance/blob/c2f340ff249f191c891a83eec5e2e6e61c7e406c/src/governance/h3_matrix.py)  |  [Native contracts](https://github.com/MarineCast/toolkit-governance/blob/c2f340ff249f191c891a83eec5e2e6e61c7e406c/docs/CONTRACTS.md)  |  [H3 semantics](https://github.com/MarineCast/toolkit-governance/blob/c2f340ff249f191c891a83eec5e2e6e61c7e406c/docs/h3-matrix.md)

## Biological and acoustic products

### Marine Mammals

Implemented products focus on killer-whale observations and annual Southern Resident census data. Native observation Parquet is keyed by observation ID, with location, time provenance, labels, uncertainty, quality and rights. Count post-processing already produces period by H3 resolution by cell by ecotype or pod products, defaulting to R4, R5 and R6 at daily and weekly cadence. Observation counts, source-report counts, observed or imputed measures and mature or provisional measures remain distinct.

Verified source-record coverage can permit no-report zeros; it does not establish biological absence or measured observation effort. Unverified coverage is unavailable and blocks the current dense-grid path. Relative reported activity is a smoothed reporting proxy, not abundance, occupancy or calibrated occurrence probability. Pod-associated counts can overlap. Annual census is year by pod and has no justified native H3 attribution.

Existing exact-head CI passes, including offline tests and installed-wheel checks. Count grids need configured cell support and, where used, Seascape water networks and certified imputation. The convenient product exporter publishes observations and a report, so expose the existing H3 count layer through a documented consumer profile. Current release profiles default to nonpublic eligibility; internal-only or unknown-rights inputs cannot be assumed redistributable.

Acceptance: preserve ecotype, pod and processing variants; reconcile daily and weekly totals, expected mass, overlapping pods, unavailable cell-periods and immutable lineage. Document all prerequisites, verify rights and complete a reviewed real-data qualification. A table-shape adapter alone does not establish scientific eligibility.

Evidence: [Count products](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/tools/observations/post_process/counts.py#L352-L420)  |  [Coverage contract](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/tools/observations/post_process/counts.py#L53-L101)  |  [Relative activity meaning](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/tools/observations/post_process/aggregation.py#L909-L926)  |  [Release eligibility](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/cetaceans/killer_whales/observations/release.py#L71-L137)

### Salmon

The repository has only a README and no source, schema, package, exporter, tests or CI. Start with one defensible native product retaining species, stock or run, site or watershed, period and measurement type. Passage, escapement, catch and marine prey availability are distinct quantities. A site-to-H3 assignment locates a measurement; it does not measure prey throughout that marine cell.

Acceptance: installable package and CLI, documented source rights, synthetic and retained-source fixtures, duplicate and partial-period tests, and a justified H3 transformation with support and uncertainty. Treat any marine prey proxy as a separately versioned scientific method.

### Acoustics

The repository has a README and banner but no implementation or CI. Choose one measurement or detection product and retain station, deployment, calibration, band, depth, interval, units, classifier version and operating effort. Hydrophone location is not its detection footprint. No recording effort means unavailable; valid-effort nondetection is not animal absence.

Acceptance: native schema and package first, then one justified H3 export with effort-gap, support-boundary, duplicate and partial-period fixtures. Keep acoustic measurements distinct from species detections and qualify the source and method before release.

## Proposed common product contract

Extend the existing MarineCast shared contract v0.1. It already covers identity, spatial support, time, units, missingness, rights, checksums and immutable publication, but remains proposed. Add reviewed profiles for forecast issue and lead times, ensembles, mixed-resolution products and multi-artifact releases; do not create a competing universal schema.

Evidence: [Proposed contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md)

| Contract element | Proposed minimum |
| --- | --- |
| Logical grain | Dynamic valid instant or interval × H3 × qualified metric; static H3 × qualified metric. Keep depth, role, species, source, forecast vintage and other essential axes as columns or part of a registered metric identity. |
| Representation | Long and wide layouts are both valid. Require unambiguous unique keys and lossless conversion for a declared slice. Native observations, pairs, graphs and geometry remain companion products. |
| Space | Canonical H3 string, explicit resolution, domain/support fingerprint, wet-subset versus full-cell meaning and assignment method. Conversion requires a reviewed method; no implicit averaging. |
| Time and availability | Declare native cadence, time zone/calendar and instant or half-open interval. Retain valid, issue, available-at, revision and as-of times separately. Static releases retain reference period, vintage and applicability. |
| Metric registry | Namespaced identity, definition, units and datum, statistic, processing mode, allowed spatial/temporal reductions, weights and denominator. Unknown, partial, not applicable and zero remain distinct. |
| Evidence and publication | Contract, scientific method and product versions, immutable data release ID, code/package version, config hash, source versions and rights, quality/uncertainty, artifact checksums and checksum algorithm. Publish complete manifests atomically. |

### The OrcaCast adapter is an explicit additional contract

Current OrcaCast accepts checksum-pinned static or ISO-week features at its configured resolution, default R6, with H3 or H3 by ecotype keys. It validates joins, collisions and support; it performs no implicit resampling. Its naive UTC-calendar Monday keys need explicit construction from the shared timezone-aware interval model. AVAILABLE\_AT\_UTC must precede each origin; a static snapshot must be available before the earliest origin.

Checked-in selections are empty, so no all-toolkit operational binding is established. Current maintained models use events and cells for recent-prevalence and seasonal-climatology forecasts. Joining environmental features does not make those models consume covariates. A validated covariate-consuming model is separate downstream work.

Evidence: [Inputs](https://github.com/MarineCast/orcacast/blob/177bd7ad18c646ccd28fcf8d809344252581f231/src/orcacast/inputs.py)  |  [Join validation](https://github.com/MarineCast/orcacast/blob/177bd7ad18c646ccd28fcf8d809344252581f231/src/orcacast/datasets.py)  |  [Empty selections](https://github.com/MarineCast/orcacast/blob/177bd7ad18c646ccd28fcf8d809344252581f231/config/inputs.yaml)  |  [Maintained models](https://github.com/MarineCast/orcacast/blob/177bd7ad18c646ccd28fcf8d809344252581f231/src/orcacast/models/sightings/maintained.py)

## Proposed implementation sequence

Sequence work by dependencies and demonstrated acceptance, rather than by repository age or table layout. This is a proposed plan, not approval to edit repositories or a delivery-date estimate. Each batch should leave a reproducible artifact and a documented decision about scientific eligibility.

| Batch | Work | Acceptance evidence |
| --- | --- | --- |
| 1 | Adopt shared profiles and build one golden producer → adapter → OrcaCast fixture. Select bounded domain, resolution, cadence and qualified metrics. | Contract and metric registry reviewed; installed artifact joins without row expansion, value loss, unit drift or future-data leakage. |
| 2 | Fix Viewshed lineage and counts, Human CI/runtime, and Oceanography fail-closed publication. Close Seascape current-method verification and runtime maintenance. | Merged fixes plus negative fixtures; clean wheel/native smoke; atomic complete release; independent checks on a bounded source-backed Seascape candidate. |
| 3 | Qualify a bounded Meteorology real-source product in parallel once error and contract behavior are stable. | Reviewed variables, units, intervals, rights and coverage; reproducible provider fixture and adapter checks at the selected resolution. |
| 4 | Complete the seven implemented producers and their consumer profiles. Add missing availability, support, registry, provenance and quality handling. | Each selected product passes all release checks below; real-data scientific limitations and permitted uses remain explicit. |
| 5 | Bootstrap Hydrology, AIS, Salmon and Acoustics with one defensible native-to-H3 product each. Resolve Human/AIS and river-data ownership first. | Package, CLI, documented source contract, tests and CI; justified transformation and bounded real-source qualification before widening scope. |

### Release checks shared across every toolkit

- Keys and joins: reject duplicates, omitted variant axes, incompatible resolution/support and row-expanding joins. Round-trip wide and long representations without changing the qualified data.

- Time and leakage: test UTC and local-day boundaries, daylight-saving transitions, partial intervals, late availability, future forecast issuance and revised historical or static vintages.

- Scientific semantics: preserve null versus zero and quality states; reproduce documented weights and denominators; reject unsupported reductions and units. Keep proxy labels intact.

- Publication and operation: reject missing partitions, stale factors, hash mismatches and mutable release substitutions. Verify clean installation, restart/rollback behavior and an independently checked bounded real-data artifact.

- Consumer and model: feature joins must not change observation support or targets. Demonstrate actual covariate consumption and held-out predictive validity separately from successful table assembly.

Evidence: [Existing join-guard tests](https://github.com/MarineCast/orcacast/blob/177bd7ad18c646ccd28fcf8d809344252581f231/tests/test_phase2.py)

## Snapshot and evidence register

All repository links in this report are pinned to the reviewed default-branch commits below unless explicitly identified as a pull request or Actions run. CI status is the existing run result inspected during the review, not a new execution. Main branches, open pull requests and provider data may change after this snapshot.

| Repository | Reviewed commit |
| --- | --- |
| [toolkit-seascape](https://github.com/MarineCast/toolkit-seascape/tree/162bc906a3e6cd73146870e9c2e343cacf62e0bb) | 162bc906a3e6cd73146870e9c2e343cacf62e0bb |
| [toolkit-viewshed](https://github.com/MarineCast/toolkit-viewshed/tree/0c0c33b60ab34f6e22d87ff235538d82112f2589) | 0c0c33b60ab34f6e22d87ff235538d82112f2589 |
| [toolkit-meteorology](https://github.com/MarineCast/toolkit-meteorology/tree/3bbcee964ffdb4ba99c8cc427797749df6e481c3) | 3bbcee964ffdb4ba99c8cc427797749df6e481c3 |
| [toolkit-oceanography](https://github.com/MarineCast/toolkit-oceanography/tree/c378eb7f580e34bad0161cc023d4ecb5cd90238f) | c378eb7f580e34bad0161cc023d4ecb5cd90238f |
| [toolkit-hydrology](https://github.com/MarineCast/toolkit-hydrology/tree/0d0aaf1d8f032aa4dcd32a230974379c47420abf) | 0d0aaf1d8f032aa4dcd32a230974379c47420abf |
| [toolkit-human](https://github.com/MarineCast/toolkit-human/tree/c3431e7263c3ec48a3e157adca306baeefd67c32) | c3431e7263c3ec48a3e157adca306baeefd67c32 |
| [toolkit-ais](https://github.com/MarineCast/toolkit-ais/tree/57d705867668dd5e1c73e1977adb8d62fd6d8dea) | 57d705867668dd5e1c73e1977adb8d62fd6d8dea |
| [toolkit-governance](https://github.com/MarineCast/toolkit-governance/tree/c2f340ff249f191c891a83eec5e2e6e61c7e406c) | c2f340ff249f191c891a83eec5e2e6e61c7e406c |
| [toolkit-marine-mammals](https://github.com/MarineCast/toolkit-marine-mammals/tree/5670419ad69972dc2e9096c1bb81f15d94f7000a) | 5670419ad69972dc2e9096c1bb81f15d94f7000a |
| [toolkit-salmon](https://github.com/MarineCast/toolkit-salmon/tree/807d5405474036b19555e0ac133591460f824392) | 807d5405474036b19555e0ac133591460f824392 |
| [toolkit-acoustics](https://github.com/MarineCast/toolkit-acoustics/tree/cbfce32d51a2368e24ded4f1d8b603fd55482eaa) | cbfce32d51a2368e24ded4f1d8b603fd55482eaa |
| [orcacast](https://github.com/MarineCast/orcacast/tree/177bd7ad18c646ccd28fcf8d809344252581f231) | 177bd7ad18c646ccd28fcf8d809344252581f231 |
| [.github](https://github.com/MarineCast/.github/tree/c434bc37317def4e523d0af6704a41e742b8837a) | c434bc37317def4e523d0af6704a41e742b8837a |

### Existing exact snapshot CI

[Seascape run 36844408374](https://github.com/MarineCast/toolkit-seascape/actions/runs/36844408374)  Passed

[Viewshed run 37158597891](https://github.com/MarineCast/toolkit-viewshed/actions/runs/37158597891)  Passed

[Meteorology run 37120074793](https://github.com/MarineCast/toolkit-meteorology/actions/runs/37120074793)  Passed

[Oceanography run 36842634076](https://github.com/MarineCast/toolkit-oceanography/actions/runs/36842634076)  Passed research checks

[Human run 36844920597](https://github.com/MarineCast/toolkit-human/actions/runs/36844920597)  Failed on Python 3.11 and 3.14

[Governance run 36840934121](https://github.com/MarineCast/toolkit-governance/actions/runs/36840934121)  Passed

[Marine Mammals run 36146567334](https://github.com/MarineCast/toolkit-marine-mammals/actions/runs/36146567334)  Passed

Hydrology and AIS returned no Actions runs. Salmon and Acoustics contain no CI workflows. A passing run verifies only its configured checks. Human’s current failure supersedes historical passing-test or packaging summaries.

Future qualification should record the new code SHA, release and manifest IDs, commands, data vintage, measured results and reviewer decision before changing a readiness claim.
