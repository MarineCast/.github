# MarineCast infrastructure and repository contracts

## Purpose and status

MarineCast separates species-neutral data processing from species-specific modeling and forecasting.
This guide owns cross-repository architecture and coordination context. Toolkit architecture,
configuration, methodology, and API documentation remain authoritative for their implementations.

**Inventory verified against local checkouts and configured remotes on 2026-09-15.** Remote release
status, deployment, and end-to-end application integration were not verified. Recheck repository
contents before treating this snapshot as current implementation evidence.

The governance entry and extraction boundaries were refreshed on 2026-09-16 against its local
package, offline tests and installed wheel. This does not revalidate the other toolkit entries.
The marine-mammal ownership entry was also refreshed on 2026-09-16 against its local extraction;
the toolkit migration document records validation scope separately from production readiness.

## Current organization

| Repository | Responsibility | Observed implementation |
| --- | --- | --- |
| [.github](https://github.com/MarineCast/.github) | Organization profile and shared guidance | Documentation repository |
| [toolkit-marine-mammals](https://github.com/MarineCast/toolkit-marine-mammals) | Observation acquisition, normalization, label imputation and population census processing | Installable `marine_mammal_toolkit`; killer-whale workflow, CLI and offline tests extracted from OrcaCast; other species are extension points |
| [toolkit-viewshed](https://github.com/MarineCast/toolkit-viewshed) | Static terrain, canopy, and distance viewability | Python package, CLI, configuration, tests, and methodology docs |
| [toolkit-seascape](https://github.com/MarineCast/toolkit-seascape) | Bathymetry, geomorphology, and coastal geometry | Installable `seascape` package, acquisition/build CLI, configuration and offline tests; OrcaCast integration deferred |
| [toolkit-oceanography](https://github.com/MarineCast/toolkit-oceanography) | Ocean properties, currents, tides, and waves | Incomplete `oceanography` research package, CLI, offline tests and prioritized TODO; seascape inputs and further validation required |
| [toolkit-meteorology](https://github.com/MarineCast/toolkit-meteorology) | HRRR weather, daylight, lunar and atmospheric H3 products | Installable `meteorology` package, CLI and offline tests; application integration deferred |
| [toolkit-ais](https://github.com/MarineCast/toolkit-ais) | Vessel tracks and maritime activity | Initial repository; README only before agent guidance |
| [toolkit-human](https://github.com/MarineCast/toolkit-human) | Population, access, recreation, and human activity | Installable `human` research package extracted from OrcaCast; CLI, offline tests and local Graphify navigation; regional/application integration unverified |
| [toolkit-acoustic](https://github.com/MarineCast/toolkit-acoustic) | Acoustic observations and marine soundscape products | Initial repository; README only before agent guidance |
| [toolkit-governance](https://github.com/MarineCast/toolkit-governance) | Native-geometry marine protected areas, jurisdictional references and fisheries management | Installable `governance` package, CLI, six implemented collections, offline tests and local Graphify graph; 18 catalog entries remain planned |

OrcaCast is the originating species application, located locally at `Modeling/OrcaCast`.
The `Apps/` grouping remains empty. This local checkout does not establish a public application
repository or deployment in the MarineCast organization. Additional applications remain possibilities.

### Local workspace and independent clones

The local workspace groups independent checkouts under `.github/`, `Toolkits/toolkit-*/`, and
`Modeling/OrcaCast` (and the empty `Apps/` grouping). These directories are not an organization monorepo, an import hierarchy, or a
required installation layout. Each toolkit must remain usable from its own checkout.

The parent workspace `AGENTS.md` guides local work across checkouts. Each repository's `AGENTS.md`
travels with that repository and explicitly directs agents to this guide when relevant. GitHub's
organization `.github` repository does not automatically supply agent instructions to sibling
repositories. Do not assume a linked document has been loaded without reading it.

## Ownership and dependency direction

The intended integration is:

```text
External sources → Domain toolkits → Validated data products
                                           ├→ Research analyses
                                           └→ Species applications → Models → Forecast products
```

- Toolkits own source acquisition, source-specific normalization, domain calculations, product
  validation, and provenance for their outputs.
- Marine-mammal source interpretation and observation-label imputation live in the toolkit's
  species implementation. Killer-whale features and acceptance policy compose reusable engines.
  Binary SRKW/Transient imputation preserves known-Other handling and abstention; it is not an
  occurrence forecast or a general multiclass model.
- Applications own ecological assumptions, occurrence/forecast feature engineering, forecast-model
  fitting, calibration, evaluation, and presentation. Imputation research moved with its producer;
  occurrence-model research remains in OrcaCast.
- Applications may consume toolkit APIs or documented products. Toolkits must not require an
  application checkout, private application modules, or its research datasets to install or test.
- Cross-toolkit dependencies must be explicit and justified in the consuming toolkit's documentation
  and dependency configuration. Do not import modules through sibling filesystem paths.
- Shared conventions live here as design requirements until implemented by an owning repository.
  There is currently no shared-schema package or organization-wide execution service established
  by this inventory. Introduce common code only with a clear owner and compatibility plan.
- `toolkit-governance` owns marine regulatory/reference geometry and its native product contracts.
  It has no OrcaCast runtime dependency. International-boundary reconciliation requires explicitly
  provisioned source/spatial-support inputs; source availability and regional rebuilds are separate
  checks. This guide and the proposed `.github/contracts/` H3 specification remain owned here.

## Data integration requirements

These are requirements for new integrations, not a claim that all repositories already implement
one uniform schema, manifest format, spatial grid, or publication mechanism.

The proposed [data-product contract v0.1](contracts/README.md) turns these requirements into a
small manifest specification, JSON Schema and synthetic examples for H3 tables. It is not an
implemented ecosystem standard. Trial it independently in two or three toolkits before extracting
shared code; no `marinecast-core` package is introduced. Toolkit adoption and application
integration require separate validation.

| Contract | What producers and consumers must agree on |
| --- | --- |
| Identity and grain | What one row represents, durable keys, uniqueness, and join cardinality |
| Spatial support | CRS, geometry/grid definition, resolution, domain, and point versus area support |
| Temporal support | Time zone, valid time, interval boundaries, aggregation window, and forecast issue time where applicable |
| Values | Units, valid ranges, categorical meanings, and quality flags |
| Missingness | Unknown, unavailable, partial coverage, not applicable, and observed zero remain distinguishable |
| Provenance | Source identifier/version, retrieval time, source coverage, code revision, configuration, and relevant fingerprints |
| Compatibility | Schema/product version, changes in scientific meaning, and migration or rejection behavior |
| Validation | Required fields, key uniqueness, finite/range checks, spatial/temporal alignment, and documented limitations |
| Publication | Artifact locations, completion indicators, atomicity guarantees, and reuse/invalidation rules |
| Rights | Source license, attribution, redistribution restrictions, and software license |

Do not join on row order, hide duplicate keys with arbitrary first-row selection, shift source
dates to fit a requested interval, or fill missing coverage with zero. Validate source timestamps
and intended time support. Forecast issue time and forecast valid time are different fields.

For viewshed specifically, products use `source_h3 × target_h3` identity within a source role;
combined roles also require `source_type`. Its bounded static weights describe physical
viewability. This is a local contract, not a universal key or value range for every toolkit.

### Scientific interpretation boundaries

Keep vessel traffic separate from observer effort; human access separate from actual presence
and reporting; physical viewability separate from detection probability; acoustic detections
separate from validated species-presence inference; and environmental features separate from
habitat preference. Downstream transformations must state and test the assumptions that connect
these quantities.

Governance reference geometry, controlling legal authority, effective dates and source vintage
are also distinct. Native geometry has no implicit H3 resolution; governance fields remain
model-ineligible by default. The proposed H3 contract v0.1 does not cover these native products.

## Execution, storage, and publishing boundaries

- There is no common install command, test runner, or runtime environment for this workspace.
  Follow each implemented toolkit's own setup and CI configuration.
- `toolkit-marine-mammals` owns the six sightings sources, canonical state, imputation, counts,
  model grids, intensity and census processing. OrcaCast uses its installed APIs. Canonical configs
  ship in the wheel; data/model/output roots remain explicitly external. Existing data, manifests,
  generated research outputs and model files were not relocated. Legacy Joblib models require a
  refit and do not acquire certification through migration. Seascape supplies the public water
  network API; its data base and named-area workspace must be explicitly configured. No live
  acquisition, production refit, production-artifact rewrite or production promotion accompanied
  the source migration. See the toolkit's migration document for observed checks and limits.
- `toolkit-viewshed` currently requires Python 3.11+ and compatible GDAL/Rasterio for real geospatial
  execution. Its own `AGENTS.md` documents focused checks and workflow-specific effects.
- `toolkit-seascape` now owns the seascape producers extracted from OrcaCast. Its README documents
  installation, workspace configuration, acquisition and candidate-release commands. Regional
  rebuild and application integration remain separate validation steps.
- `toolkit-meteorology` now owns the extracted HRRR acquisition, offline weather and astronomy
  producers. Its README documents independent workspace initialization and per-family transactional
  publication. Future-weather forecasting, regional rebuilds and application integration are not verified.
- `toolkit-oceanography` contains extracted research producers and offline tests. Its root `TODO.txt`
  tracks incomplete research and production hardening; regional execution requires externally
  provisioned seascape products. Package installation does not establish a complete ocean pipeline.
- `toolkit-human` owns extracted population, access, calendar, AIS/ferry and reporting-opportunity
  producers. Its legacy observation geometry remains separate from `toolkit-viewshed`; equivalence
  is not established. `toolkit-ais` remains a scaffold. See the human README for setup and limits.
- `toolkit-governance` contains the extracted native-geometry producers, configuration, catalog and
  tests. Its README and workflow docs describe explicit workspaces and per-file atomic outputs;
  there is no whole-family transaction. Historical local products were preserved as migration
  evidence, not recertified. Live acquisition, regional rebuilds and application integration were
  not run during extraction. Its Graphify cache is local-only, like the other implemented toolkits.
- The remaining initial repositories have no verified executable entry points or test suites. Do not invent
  commands or describe successful execution before implementation exists.
- Keep large source data, generated products, credentials, and private research inputs outside
  tracked source. Document configured locations without embedding workstation-specific paths.
- Read the owning workflow's acquisition, overwrite, cleanup, and promotion rules before running
  it. Use dedicated output locations for experiments and preserve validated artifacts.
- Viewshed's paired and explicit component workflows have different promotion and cleanup
  guarantees. Read its API and pipeline documentation; do not generalize either across toolkits.
- No shared artifact registry, production scheduler, hosting platform, or deployment process is
  verified here. Product publication and software deployment require an explicit destination and
  a documented process in the owning repository.
- Code publishing and dataset redistribution are separate actions. Check applicable source rights
  before placing example data or generated products in a public repository.

## Cross-repository change workflow

1. Identify the producer, consumer, and contract being changed; inspect each checkout's status and
   instructions. Preserve unrelated work.
2. Read the owning schemas, configuration, producers, and consumers. Record the current behavior
   and proposed compatibility impact before changing an interface.
3. Keep the change in the responsible repository. Coordinate consumer changes when necessary;
   make required product/schema version changes explicit.
4. Validate with small synthetic or offline fixtures where possible. Check product meaning,
   missingness, cardinality, determinism, and failure handling as appropriate to the change.
5. Run integration validation only with the required inputs and an understood output destination.
   Unit tests alone do not establish a successful regional build or application integration.
6. Update affected documentation and report checks per repository, unrun paths, missing inputs,
   and whether artifacts or deployments were actually inspected.

For prose-only edits, validate references and `git diff --check` in each changed repository;
regional processing and package test suites are unnecessary.

## Maintaining this guide

Update the dated inventory when repositories gain implementations or application locations are
established. Update [profile/README.md](profile/README.md) when public organization structure or
status changes. Keep implementation commands and detailed science in their owning repositories;
link to those sources instead of maintaining competing copies here.
