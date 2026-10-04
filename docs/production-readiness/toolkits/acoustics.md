# Acoustics toolkit charter and roadmap

Status: Draft for Tyler review, not adopted policy. Date: 2026-10-04.

## Purpose and desired outcome

Provide traceable acoustic measurements and, where separately supported, effort-aware detection products. Applications should receive logical date × H3 × metric tables while retaining the sensor, deployment, frequency, depth, window, and method dimensions needed to interpret each value. Static H3 × metric context may describe a station inventory or other approved reference product with declared applicability.

The MVP requires an explicit choice: one calibrated station/deployment band-and-window acoustic-level product, or one separately defined effort-aware species-detection product. Combining those into a general occurrence or disturbance score is outside this proposed first release.

## Boundaries and non-goals

Preserve sensor and deployment identity, calibration reference, frequency bounds, depth, window boundaries, units and reference quantities, processing configuration, and effort. Detection products also preserve species labels, classifier/version, confidence or threshold definitions, and evaluation evidence. Raw recordings remain native evidence subject to rights and retention limits. The MVP excludes propagation modeling, source attribution, behavioral disturbance, animal abundance, and cell-wide occurrence claims unless later approved as distinct scientifically validated work.

## Native data and application-facing H3 products

Retain native measurements and metadata losslessly, with an auditable application projection rather than destructive simplification. A sensor's H3 cell locates the instrument; it does not define the acoustic footprint or detection range. Multiple sensors, deployments, bands, or classifiers in a cell remain separate where they change row identity. Aggregation of logarithmic acoustic levels requires a documented physically appropriate method, not an unexplained arithmetic average.

Reuse the proposed [.github contract v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md). Its identity, H3 support, time, units, missingness, provenance, rights, checksums, and immutable publication rules are the proposed interchange basis. Native manifests remain authoritative until explicit adoption. Long versus wide layout, cadence, and H3 resolution remain product-specific until approved. Preserve window intervals; a date label cannot replace them. Static context has no invented observation date. Forecast issue/lead time and ensembles require a reviewed profile or contract revision. Unsupported dimensions cannot disappear or hide in optional extensions to obtain schema conformance.

## Current verified baseline

The complete [toolkit-acoustics tree at cbfce32d51a2368e24ded4f1d8b603fd55482eaa](https://github.com/MarineCast/toolkit-acoustics/tree/cbfce32d51a2368e24ded4f1d8b603fd55482eaa) contains a README and banner only. It has no source, schema, export, package, tests, or CI implementation. No live source or calibration pipeline is established by that evidence. No tests were run for this charter; the following capabilities are proposed.

## Known and proposed metric families

Proposed physical families include calibrated acoustic levels for explicit frequency bands and time windows. Proposed biological families include detection counts or durations with classifier identity, validation, thresholds, and recording effort. These are separate products with different scientific meanings.

## Science, quality and rights

No recording means unavailable data, not silence. Nondetection under documented recording and classifier effort does not establish animal absence. Missing results stay null with a reason; a valid zero requires a defined measurable quantity and observation support. Keep physical sound measurements, model detections, and downstream interpretation distinct.

Record source availability, retrieval, recording interval, processing, and release identities independently. Validate clock drift, gaps, clipping, calibration validity, frequency support, depth changes, recording duty cycle, and window completeness. Detection releases additionally require evidence appropriate to the classifier and operating conditions. Approve recording access, redistribution, location sensitivity, and attribution before publication; derived products do not automatically escape source restrictions.

## Dependencies

Dependencies are an approved source owner and rights, station/deployment metadata, calibration or classifier evidence, and explicit consumer expectations.

## Phased milestones and acceptance tests

1. **Choose the bounded MVP.** Acceptance: Tyler approves either the calibrated-level or detection product, its intended use, source contract, rights, scientific reviewer, and minimum metadata.
2. **Establish native fixtures.** Acceptance: synthetic cases cover missing recordings, true measured values, partial windows, changed deployments, units, and calibration or classifier versions; an authorized sample is traceable to source evidence.
3. **Implement the application projection.** Acceptance: full keys and H3 support are explicit; bands, windows, effort, and method dimensions survive a consumer round-trip; invalid units, missing-reason conflicts, and duplicate keys are rejected.
4. **Release one validated product.** Acceptance: a clean-installed entry point demonstrates the selected scientific checks, source rights, manifest/artifact validation, reproducible configuration, checksums, and immutable publication procedure together.

The acceptance suite must run in CI, including clean package installation and synthetic/offline contract tests; document any live or native-runtime checks separately.

## Unresolved decisions

Open decisions include MVP branch, source, recording retention, calibration requirements, classifier acceptance, uncertainty, cadence, resolution, and physical layout. No schedule is promised.

## Definition of done

The MVP is done when a consumer can reproduce and interpret one approved acoustic product without confusing sensor location with footprint, missing effort with silence, or nondetection with absence. Tyler must review this charter before its proposals become governing policy.
