# MarineCast production readiness tracking

**Assessment snapshot: 2026-10-04. Approved for repository tracking. The eleven toolkit charters remain drafts for Tyler review, not adopted policy.**

This index records the supplied read-only assessment and proposed roadmaps. It does not approve the implementation sequence, adopt a charter, establish production readiness, or authorize toolkit changes, source acquisition, dataset publication or deployment. Milestones describe acceptance gates without delivery dates. Status below is the assessment's dated judgment at its reviewed SHAs, not a claim about later default-branch changes.

- [Production Readiness Assessment](assessment.md): complete Markdown transcription of the nine-page source, including four tables, qualifications, evidence links, reviewed SHAs and existing CI observations.
- [Toolkit charter package](charter-package.md): the supplied shared conventions, review decisions and adoption guidance, with links adapted for this tracking location.
- [Snapshot and evidence register](assessment.md#snapshot-and-evidence-register): eleven toolkit revisions plus OrcaCast and this documentation repository.

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

The [existing contract v0.1](../../contracts/README.md) remains proposed. These documents build on it and propose reviewed profiles or revisions where needed; they do not introduce a second shared schema. Native manifests, scientific contracts and owning-toolkit instructions remain authoritative until explicit adoption. Existing tracking such as Meteorology's implementation tracker, Seascape's capability inventory and the pinned toolkit contracts remains linked in the assessment and roadmaps. Before any future adoption, reconcile those sources and existing commitments in the owning repository rather than overwriting its roadmap.

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
