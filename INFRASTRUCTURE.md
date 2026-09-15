# MarineCast infrastructure and repository contracts

## Purpose and status

MarineCast separates species-neutral data processing from species-specific modeling and forecasting.
This guide owns cross-repository architecture and coordination context. Toolkit architecture,
configuration, methodology, and API documentation remain authoritative for their implementations.

**Inventory verified against local checkouts and configured remotes on 2026-09-15.** Remote release
status, deployment, and end-to-end application integration were not verified. Recheck repository
contents before treating this snapshot as current implementation evidence.

## Current organization

| Repository | Responsibility | Observed implementation |
| --- | --- | --- |
| [.github](https://github.com/MarineCast/.github) | Organization profile and shared guidance | Documentation repository |
| [toolkit-viewshed](https://github.com/MarineCast/toolkit-viewshed) | Static terrain, canopy, and distance viewability | Python package, CLI, configuration, tests, and methodology docs |
| [toolkit-seascape](https://github.com/MarineCast/toolkit-seascape) | Bathymetry, geomorphology, and coastal geometry | Installable `seascape` package, acquisition/build CLI, configuration and offline tests; OrcaCast integration deferred |
| [toolkit-oceanography](https://github.com/MarineCast/toolkit-oceanography) | Ocean properties, currents, tides, and waves | Initial repository; README only before agent guidance |
| [toolkit-meteorology](https://github.com/MarineCast/toolkit-meteorology) | HRRR weather, daylight, lunar and atmospheric H3 products | Installable `meteorology` package, CLI and offline tests; application integration deferred |
| [toolkit-ais](https://github.com/MarineCast/toolkit-ais) | Vessel tracks and maritime activity | Initial repository; README only before agent guidance |
| [toolkit-human](https://github.com/MarineCast/toolkit-human) | Population, access, recreation, and human activity | Initial checkout with no implementation files before agent guidance |
| [toolkit-acoustic](https://github.com/MarineCast/toolkit-acoustic) | Acoustic observations and marine soundscape products | Initial repository; README only before agent guidance |

OrcaCast is the originating species application. The local `Apps/` grouping is empty at this
snapshot; this inventory does not establish an application repository or deployment in the
MarineCast organization. Additional species applications remain possibilities.

### Local workspace and independent clones

The local workspace groups independent checkouts under `.github/`, `Toolkits/toolkit-*/`, and
`Apps/`. These grouping directories are not an organization monorepo, an import hierarchy, or a
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
- Applications own observation interpretation, ecological assumptions, species-specific feature
  engineering, model fitting, calibration, evaluation, and forecast presentation.
- Applications may consume toolkit APIs or documented products. Toolkits must not require an
  application checkout, private application modules, or its research datasets to install or test.
- Cross-toolkit dependencies must be explicit and justified in the consuming toolkit's documentation
  and dependency configuration. Do not import modules through sibling filesystem paths.
- Shared conventions live here as design requirements until implemented by an owning repository.
  There is currently no shared-schema package or organization-wide execution service established
  by this inventory. Introduce common code only with a clear owner and compatibility plan.

## Data integration requirements

These are requirements for new integrations, not a claim that all repositories already implement
one uniform schema, manifest format, spatial grid, or publication mechanism.

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

## Execution, storage, and publishing boundaries

- There is no common install command, test runner, or runtime environment for this workspace.
  Follow each implemented toolkit's own setup and CI configuration.
- `toolkit-viewshed` currently requires Python 3.11+ and compatible GDAL/Rasterio for real geospatial
  execution. Its own `AGENTS.md` documents focused checks and workflow-specific effects.
- `toolkit-seascape` now owns the seascape producers extracted from OrcaCast. Its README documents
  installation, workspace configuration, acquisition and candidate-release commands. Regional
  rebuild and application integration remain separate validation steps.
- `toolkit-meteorology` now owns the extracted HRRR acquisition, offline weather and astronomy
  producers. Its README documents independent workspace initialization and per-family transactional
  publication. Future-weather forecasting, regional rebuilds and application integration are not verified.
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
