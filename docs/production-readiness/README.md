# MarineCast production readiness tracking

**Assessment snapshot: 2026-10-04. Approved for repository tracking. The eleven toolkit charters remain drafts for Tyler review, not adopted policy.**

This index records the supplied read-only assessment and proposed roadmaps. It does not approve the implementation sequence, adopt a charter, establish production readiness, or authorize toolkit changes, source acquisition, dataset publication or deployment. Milestones describe acceptance gates without delivery dates. Status below is the assessment's dated judgment at its reviewed SHAs, not a claim about later default-branch changes.

- [Production Readiness Assessment](assessment.md): complete Markdown transcription of the nine-page source, including four tables, qualifications, evidence links, reviewed SHAs and existing CI observations.
- [Toolkit charter package](charter-package.md): the supplied shared conventions, review decisions and adoption guidance, with links adapted for this tracking location.
- [Snapshot and evidence register](assessment.md#snapshot-and-evidence-register): eleven toolkit revisions plus OrcaCast and this documentation repository.

## Approved delivery decision

On 2026-10-04 Tyler approved the [default application delivery profile](../../contracts/application-delivery-profile.md): wide Parquet, **daily UTC** cell × valid interval rows for every dynamic variable or static cell rows with metric columns, one H3 resolution per table, and a companion manifest covering units, methods, sources, quality rules and distinct versions/releases. Necessary dimensions remain in native companions or explicit product variants; they cannot be silently collapsed to obtain cell keys. Native cadence is retained, and daily aggregation or representation must be scientifically valid. Slower sources need a justified declared applicability/carry-forward rule or unavailable days, never invented daily observations or silent filling.

The daily UTC interval is midnight inclusive to the next midnight exclusive, with aware UTC timestamps and a date label equal to the interval-start UTC date. Explicitly labeled local-day exceptions require a reviewed aggregation/profile and cannot be silently relabeled UTC.

These later approvals resolve the default physical layout, delivery grain, daily cadence, UTC day calendar/boundaries, readable metric naming and missingness/status semantics left open in the original assessment and drafts. Interval aggregation, broader numerical resolution policy, exact product metric names/shared registry, product-specific coverage methods, QC code changes, forecast profiles and scientific thresholds remain pending. The assessment and eleven source drafts remain dated review artifacts; broad charter adoption, toolkit conformance and the implementation sequence are not approved by these decisions. The existing v0.1 schema and native/legacy formats remain valid within their stated scope.

The [metric naming convention](../../contracts/application-delivery-profile.md#metric-naming-and-definitions) is approved: readable `lower_snake_case` quantity/statistic/unit names where applicable, with precise manifest definitions and namespaced product/variant identity to prevent collisions. Identifiers/status/categories do not invent physical units. Existing fields are not renamed; the missingness decision below maps the user-facing word valid to the unchanged v0.1 code `observed`.

The [missingness semantics](../../contracts/application-delivery-profile.md#approved-missingness-and-coverage-semantics) are approved: missing/unknown/unavailable/not-applicable values are null, never default zero; each metric has accurate status, and partial estimates carry defined coverage. User-facing valid maps to v0.1 `observed`, which includes valid derived results without implying raw observation. Shared statuses must be correct for all referencing metrics on every row. Coverage meaning, denominator and method are explicit; no universal percent threshold or producer conformance is claimed.

Tyler also approved the [R7 exception](../../contracts/application-delivery-profile.md#approved-r7-exception): Viewshed and related Human/viewability variables retain R7. This does not reassign all Human products, including unrelated AIS/activity products. Cross-resolution consumer use requires explicit validated adapters; no existing adapter implementation is implied.

The [resolution direction](../../contracts/application-delivery-profile.md#exploratory-resolution-direction) is explicitly exploratory: R6 as a usual starting point, with scientifically justified per-product R5/R4 possibilities that balance native detail, retained gradients and cell/row/memory/storage costs. Weather and oceanography are candidates for review, not assigned resolutions. Broader policy and R6/R5/R4 assignments remain pending; consumer mapping must be explicit without forced R6 replication.

## Reference geometry contract extension

Tyler approved adding [`reference_geometry` in manifest v0.2](../../contracts/v0.2/README.md) for source-backed geometry inventories/reference overlays and explicit H3 projections. The separately versioned schema preserves v0.1 and adds no other quantity kinds or arbitrary native/raster/forecast/multi-artifact scope. These products do not assert controlling legal authority, regulatory applicability or compliance.

The [synthetic Governance fixtures](../../contracts/v0.2/examples/README.md) and validator exercise both versions, provenance/rights limitations and value/status consistency; they are not real-source validation or Governance adoption. Native data releases can retain native manifests until an adopter verifies v0.2. Approved delivery defaults and the original dated assessment/eleven roadmaps remain intact.

## Toolkit status and proposed next milestones

The assessment credits seven substantive implementations and identifies four scaffolds. Readiness is product- and domain-specific; existing exporters and passing CI do not establish scientific certification. Each roadmap retains its native-product boundaries, unresolved decisions and full acceptance tests.

| Toolkit repository | Assessment status at reviewed snapshot | Next proposed roadmap milestone | Draft roadmap |
| --- | --- | --- | --- |
| [toolkit-seascape](https://github.com/MarineCast/toolkit-seascape) | Advanced static H3 exporter; current methods still need source-backed qualification. | Agree one bounded product, metric/support register, domain, resolution and permitted uses. | [Seascape](toolkits/seascape.md) |
| [toolkit-viewshed](https://github.com/MarineCast/toolkit-viewshed) | Implemented pairs and H3 summaries with blocking lineage and visible-count defects. | Restore trustworthy correctness with reviewed lineage/count fixes and reuse, overwrite and rollback regressions. | [Viewshed](toolkits/viewshed.md) |
| [toolkit-meteorology](https://github.com/MarineCast/toolkit-meteorology) | Advanced research producer; real-source compatibility and empirical accuracy remain unqualified. | Fix product scope and error contracts, including variables, source eras, domain, cadence and resolution. | [Meteorology](toolkits/meteorology.md) |
| [toolkit-oceanography](https://github.com/MarineCast/toolkit-oceanography) | Seven implemented families with schema, preflight and publication gaps. | Make failures safe with a complete registry, stable unavailable schemas and nonzero required-family failures. | [Oceanography](toolkits/oceanography.md) |
| [toolkit-hydrology](https://github.com/MarineCast/toolkit-hydrology) | Dedicated repository is a scaffold without an implemented output or CI. | Agree scope, source rights, maintainer and gauge/catchment versus marine-influence ownership. | [Hydrology](toolkits/hydrology.md) |
| [toolkit-human](https://github.com/MarineCast/toolkit-human) | Implemented static/dynamic products; reviewed current-main CI is blocked. | Repair baseline execution and pass supported CI, installed-wheel and relevant GDAL/OSRM checks. | [Human](toolkits/human.md) |
| [toolkit-ais](https://github.com/MarineCast/toolkit-ais) | Dedicated repository is a scaffold; AIS implementation exists in Human with unresolved source limits. | Agree ownership and source before extracting or creating an adapter. | [AIS](toolkits/ais.md) |
| [toolkit-governance](https://github.com/MarineCast/toolkit-governance) | Bounded reference exporter with six implemented native families; legal-time reconstruction is separate. | Confirm source roster, consumer grid, metrics, completeness, resolution and refresh policy. | [Governance](toolkits/governance.md) |
| [toolkit-marine-mammals](https://github.com/MarineCast/toolkit-marine-mammals) | Implemented observation/count layer and nonspatial annual census; consumer eligibility still needs qualification. | Approve the count profile, retained dimensions, native companions and rights scope. | [Marine mammals](toolkits/marine-mammals.md) |
| [toolkit-salmon](https://github.com/MarineCast/toolkit-salmon) | README-only scaffold without an implemented product or CI. | Select one measurement and approved source contract with rights, identifiers and limitations. | [Salmon](toolkits/salmon.md) |
| [toolkit-acoustics](https://github.com/MarineCast/toolkit-acoustics) | README/banner scaffold without an implemented product or CI. | Choose either a calibrated-level or effort-aware detection MVP with reviewed source and metadata. | [Acoustics](toolkits/acoustics.md) |

## Relationship to existing documentation

The [infrastructure guide](../../INFRASTRUCTURE.md) continues to own shared architecture and coordination; its inventory dates precede this assessment. The later snapshot is recorded here without rewriting that inventory or the public profile. In particular, the drafts use the verified plural repository name `toolkit-acoustics` and include `toolkit-hydrology`; the older inventory's planned singular `toolkit-acoustic` entry is historical context, not a rename or ownership decision.

The [existing contract v0.1](../../contracts/README.md) remains proposed; the separately [approved delivery defaults](../../contracts/application-delivery-profile.md) narrow the target without changing its schema. These documents build on it and propose reviewed profiles or revisions where needed; they do not introduce a second shared schema. Native manifests, scientific contracts and owning-toolkit instructions remain authoritative until explicit adoption. Existing tracking such as Meteorology's implementation tracker, Seascape's capability inventory and the pinned toolkit contracts remains linked in the assessment and roadmaps. Before any future adoption, reconcile those sources and existing commitments in the owning repository rather than overwriting its roadmap.

Tracking approval is distinct from charter adoption. Future readiness changes should identify the new code SHA, generated-data release and manifest identities, commands, data vintage, measured results and reviewer decision, as required by the assessment. A successful consumer join also remains distinct from actual model covariate use and predictive validity.

## Source provenance and transcription

The supplied Library files were materialized and checked as readable before conversion. Original binary files and rendered page images are not duplicated in this repository.

| Source file | SHA-256 of supplied bytes | Tracking representation |
| --- | --- | --- |
| MarineCast Production Readiness Assessment.docx | `95fa22c3717371610e0d8427df97b6959b4a19032f11e60ec28cd494e6181dce` | [assessment.md](assessment.md) |
| MarineCast Toolkit Charter Drafts.zip | `7e3688e10440e0173f234a0fac06f26b17d0988aca232d5fe03a31a1aba3a290` | [charter-package.md](charter-package.md) and eleven [roadmaps](#toolkit-status-and-proposed-next-milestones) |

Assessment body text, table cells, hyperlink labels/targets and heading hierarchy are retained. Repeated page headers, the page-number footer and layout-only page breaks are omitted for Markdown. All eleven roadmap files are byte-for-byte copies of their ZIP members. The package README retains its content with local roadmap links relocated and an explicit tracking-location note.

## Checks for this documentation change

- Confirmed all eleven draft files, source-body/table transcription, all 51 assessment hyperlinks, reviewed SHA consistency and retained draft/acceptance language.
- Checked local relative links and Markdown table structure, inspected the documentation diff and ran `git diff --check`.
- Verified `.github`, OrcaCast and all eleven toolkit repository names/URLs against live GitHub metadata on 2026-10-04. This availability check does not revalidate readiness or scientific claims.
- No fresh toolkit tests, native-runtime checks, provider acquisitions, regional runs, benchmarks, source-backed scientific qualification or model evaluation were run. Repository guidance does not require Python tests or regional pipelines for prose-only changes. No Actions workflows are present in this documentation checkout; CI/status for the pushed documentation SHA is reported in the PR handoff separately from the historical toolkit CI register.
