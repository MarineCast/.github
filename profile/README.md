# MarineCast

**Reusable data infrastructure for marine wildlife modeling and forecasting.**

MarineCast is an open scientific software ecosystem for building reproducible spatial and temporal data products used in marine-species models. It brings together independent data toolkits and species-specific applications, with shared conventions for provenance, spatial support, temporal semantics, and validation.

The ecosystem is being extracted and generalized from OrcaCast, a killer whale modeling and forecasting project focused on the Pacific Northwest.

> **Build the marine environment once. Use it across many species models.**

## Organization structure

MarineCast separates reusable data processing from species-specific science:

- **Toolkits** acquire, normalize, process, and validate environmental and human-activity data independently of any species application.
- **Marine-mammal workflows** combine reusable observation/population tools with species-specific interpretation and label-imputation policies.
- **Applications** consume those products and own occurrence-model assumptions, forecasting features, calibration, evaluation, and forecasts.
- **Shared conventions** connect the repositories through explicit data contracts and provenance. They are an ecosystem design goal, not a separate toolkit or application.

### Data and spatial toolkits

Toolkit repositories use the `toolkit-<domain>` naming convention. The scope below describes each toolkit's role; it does not imply that every listed capability is implemented.

| Repository | Scope | Current status |
| --- | --- | --- |
| [toolkit-marine-mammals](https://github.com/MarineCast/toolkit-marine-mammals) | Marine-mammal observations, label imputation and population census processing | Installable toolkit with killer-whale workflow, CLI and offline tests; other species remain extension points |
| [toolkit-viewshed](https://github.com/MarineCast/toolkit-viewshed) | Terrain, canopy, distance, and static physical marine viewability | Implemented Python package with configuration, tests, and methodology documentation |
| [toolkit-seascape](https://github.com/MarineCast/toolkit-seascape) | Bathymetry, marine geomorphology, coastal geometry, and derived seascape features | Python package, acquisition/build CLI and offline tests; application integration pending |
| [toolkit-oceanography](https://github.com/MarineCast/toolkit-oceanography) | Ocean temperature, salinity, currents, tides, waves, and related products | Incomplete research package extracted from OrcaCast; see its TODO for implemented scope and remaining work |
| [toolkit-meteorology](https://github.com/MarineCast/toolkit-meteorology) | HRRR weather, daylight, lunar and atmospheric H3 products | Installable `meteorology` package, CLI and offline tests; application integration pending |
| [toolkit-ais](https://github.com/MarineCast/toolkit-ais) | Vessel tracks, vessel activity, traffic density, and maritime-use products | Initial repository |
| [toolkit-human](https://github.com/MarineCast/toolkit-human) | Population, access, activity, and reporting-opportunity products | Extracted Python research package with CLI and offline tests |
| [toolkit-acoustic](https://github.com/MarineCast/toolkit-acoustic) | Acoustic observations and derived marine soundscape products | Initial repository |
| [toolkit-governance](https://github.com/MarineCast/toolkit-governance) | Native-geometry marine protected areas, jurisdictional references and fisheries management | Installable `governance` package, CLI and offline tests; six implemented collections, broader catalog still planned |

The [`.github` repository](https://github.com/MarineCast/.github) hosts this organization profile. See each toolkit's repository for its implementation, usage, and development status.

### Species applications

OrcaCast is the originating application for the MarineCast ecosystem. It combines whale observations with environmental and human-activity information to model and forecast killer whale activity. Reusable processing is being separated into the toolkits above while species-specific modeling remains with the application.

The application layer is still being organized. Other species applications are future possibilities, not current MarineCast repositories listed here.

## How the pieces fit together

```text
External data sources
        │
        ▼
MarineCast toolkits
  ├── toolkit-seascape
  ├── toolkit-oceanography
  ├── toolkit-meteorology
  ├── toolkit-ais
  ├── toolkit-human
  ├── toolkit-acoustic
  ├── toolkit-governance
  ├── toolkit-marine-mammals
  └── toolkit-viewshed
        │
        ▼
Validated, versioned data products
        │
        ├── Research analyses
        │
        └── Species applications, such as OrcaCast
                    │
                    ▼
            Species-specific features
                    │
                    ▼
            Models and evaluation
                    │
                    ▼
              Forecast products
```

This is the intended integration pattern; toolkit interfaces and shared contracts are still evolving.

## Design principles

### Species-neutral upstream data

Environmental measurements should describe the marine system rather than encode assumptions about a particular species. Bathymetry and distance to a canyon belong in a MarineCast data product. A claim that canyons increase habitat suitability belongs in a downstream species model, where it can be tested.

### Reproducible data products

Generated datasets should document:

- Source data and retrieval dates.
- Code version and configuration.
- Geographic and temporal coverage.
- Units, spatial support, and variable definitions.
- Validation checks and known limitations.

### Clear scientific boundaries

MarineCast distinguishes measurements from interpretation:

- Vessel traffic is not observer effort.
- Physical viewability is not detection probability.
- Hydrophone detections require validation and interpretation before supporting animal-presence claims.
- Weather conditions are not sighting probability.
- Habitat characteristics are not species preferences.
- Regulatory reference geometry is not controlling legal authority or evidence of compliance.

Those relationships belong in downstream models where they can be explicitly tested.

### Independent but interoperable

Each toolkit should support its own acquisition, normalization, processing, validation, and publication workflow without requiring OrcaCast or another species application to be installed. Shared conventions should make the resulting products usable across applications without hiding their assumptions or limitations.

## Repository conventions

As toolkits develop, repositories should provide the documentation and interfaces appropriate to their scope, typically:

```text
README.md
AGENTS.md
pyproject.toml
src/
tests/
configs/
docs/
examples/
```

Where appropriate, include a Python API, command-line interface, documented configuration, offline or synthetic test fixtures, data schemas, provenance metadata, validation reports, and reproducible examples.

Large source and generated datasets should generally not be committed directly to Git.

## Project status

MarineCast is under active development. Repository boundaries, interfaces, and schemas may evolve as reusable components are extracted from OrcaCast.

Current priorities are:

- Developing `toolkit-viewshed` as a reference reusable package.
- Validating regional seascape rebuilds and integrating the extracted toolkit into applications.
- Validating regional meteorology rebuilds and integrating its extracted products into applications.
- Validating the extracted oceanography and human-activity packages; building out AIS and acoustics.
- Validating governance source coverage and regional rebuilds while preserving legal and temporal provenance.
- Defining common dataset and provenance contracts.
- Keeping occurrence modeling and forecasting in applications, separate from toolkit observation-label imputation.

MarineCast is a collection of focused tools that share enough conventions to work together. Each repository may mature at a different pace.

## Contributing

Issues, scientific references, data-source recommendations, validation approaches, and code contributions are welcome. Start with the relevant toolkit's documentation and contribution guidance where available.

## License

Licensing is defined independently by each MarineCast repository. Source datasets may have separate licenses, attribution requirements, or redistribution restrictions from the software that processes them.
