# Marine mammal observations charter and roadmap

Status: Draft for Tyler review, not adopted. Assessment date: 2026-10-04. Milestones are proposed acceptance gates without delivery dates.

## Purpose and desired outcome

Provide traceable marine-mammal observations and carefully qualified summaries for MarineCast applications. The initial implemented scope is killer-whale observations and Southern Resident annual census. Consumers must distinguish reports, observations, inferred labels and population census, with uncertainty and source rights intact.

## Boundaries and non-goals

Reported sightings and relative reporting activity do not establish abundance, occupancy or calibrated occurrence probability. Source completeness does not measure observer effort or detection probability. Label imputation is not a new occurrence. Other species, telemetry and acoustic namespaces are extension points, not implemented coverage. Census values must never receive invented H3 attribution.

## Native data and application-facing H3 products

The [native observation schema](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/tools/schemas/observations.py) uses `OBSERVATION_ID`, retaining dates/times, coordinates, species/ecotype, source, uncertainty, quality, rights and imputation provenance. Native annual census remains nonspatial year × pod. Preserve both before deriving logical date × H3 × metric application products.

Map application profiles to the [proposed organization contracts v0.1](https://github.com/MarineCast/.github/blob/c434bc37317def4e523d0af6704a41e742b8837a/contracts/README.md). Native manifests remain authoritative pending adoption. Long versus wide layout, cadence and resolution require product-specific approval. Preserve ecotype/pod, observation status and source dimensions through qualified metrics or explicit axes; do not collapse them to meet a superficial key.

Propose a reviewed profile/revision for valid and availability times, source vintage/identity, code/configuration identity, release identity and artifact checksums. Forecast issue/horizon and multi-artifact semantics are deferred in v0.1, requiring explicit review if needed. Preserve unknown, unavailable, partial and not-applicable states; null never automatically means zero.

## Current verified baseline

The assessed head is `5670419ad69972dc2e9096c1bb81f15d94f7000a`. [Count exports](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/tools/observations/post_process/counts.py#L352-L420) are sparse period × H3 resolution × cell × ecotype bucket/detail or pod, defaulting to daily/weekly R4/R5/R6. They distinguish unique observations from source-report counts and observed, hard-imputed, expected, mature, provisional and unknown categories. Pod overlap can double-count if totals are naively summed.

The [aggregation implementation](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/tools/observations/post_process/aggregation.py) supports dense `REPORTED_SIGHTING` and network-smoothed `RELATIVE_REPORTED_ACTIVITY`, also named `RELATIVE_SIGHTING_INTENSITY`. Unverified coverage is `UNAVAILABLE`; dense generation is guarded because its schema cannot represent unavailable support. The product exporter emits observations plus a report, not a universal long metric table.

[Census code](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/cetaceans/killer_whales/demography/census.py) reconciles reported/calculated annual J/K/L and all-pod values without spatial attribution. [Exact-head CI](https://github.com/MarineCast/toolkit-marine-mammals/actions/runs/36146567334) succeeds, including offline, installed-wheel and clean public-install checks. Real production data were not qualified by this assessment; no new tests were executed for this draft.

## Known and proposed metric families

Implemented families are distinct-observation counts, source-report counts, qualified count variants, relative reported activity and nonspatial annual census. Proposed work adapts existing count products for consumers, documents coverage and availability, and validates real-data reconciliation. New biological interpretations or species coverage require separate scientific scope and acceptance criteria.

## Science, quality and rights

Verified source-record coverage can support a no-report zero, never biological absence. Keep counts separate from smoothing and imputation. Require overlap-aware totals, uncertainty retention, exclusion audits and documented source completeness. [Release profiles](https://github.com/MarineCast/toolkit-marine-mammals/blob/5670419ad69972dc2e9096c1bb81f15d94f7000a/src/marine_mammal_toolkit/cetaceans/killer_whales/observations/release.py#L71-L137) default nonpublic and include internal-only/unknown-rights inputs. Publication requires explicit source-level rights clearance and approved output scope; software installation success is not permission to publish data.

## Dependencies

Spatial products depend on configured water-cell support, Seascape networks/domains and certified imputation where applicable. Consumer readiness also depends on independent reporting-coverage evidence, source availability histories, contract decisions and release-rights review.

## Phased milestones and acceptance tests

1. Approve product boundaries. Accept a reviewed count profile, native companions, metric definitions, dimensions, cadence/resolution and rights scope mapped to contracts v0.1.
2. Implement a lossless adapter. Accept unique qualified keys, daily/weekly reconciliation, observed/inferred separation, pod-overlap fixtures, mass/support checks and explicit rejection of unavailable dense support.
3. Validate consumer safety. Accept availability-aware historical selection, immutable lineage/checksums, row-preserving joins and fixtures proving nulls cannot become unsupported zeros. Retain census separately.
4. Qualify a bounded release. Accept independent real-source reconciliation, documented coverage limitations, passing package/release tests, reproducible artifacts and source-specific publication decisions. Model eligibility requires its own scientific review.

## Unresolved decisions

Tyler must approve priority observation profiles, ecotype/pod presentation, source-coverage thresholds, availability evidence, publication audience and whether additional species or inference methods are in scope.

## Definition of done

A product is done when reviewed semantics, reproducible artifacts, source rights, coverage/uncertainty and passing acceptance evidence travel together, and a consumer example preserves native distinctions without interpreting reporting activity as animal abundance or absence.
