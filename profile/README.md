# MarineCast 🌊🐋

**Reusable data infrastructure for marine wildlife modeling and forecasting.**

MarineCast is an open scientific software ecosystem for building reproducible spatial and temporal data products used in marine-species models.

The project is a forecasting system for killer whale presence in the Pacific Northwest, but the underlying environmental and human-activity data pipelines are intentionally being developed as independent, reusable tools.

The long-term goal is simple:

> **Build the marine environment once. Use it across many species models.**

---

## Ecosystem

MarineCast separates general-purpose data engineering from species-specific modeling.

```text
                         MarineCast
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
     Data Toolkits      Shared Standards   Applications
          │                 │                 │
          ▼                 ▼                 ▼
     Seascape          Data contracts       OrcaCast
     Oceanography      Provenance            HumpbackCast
     Meteorology       Spatial conventions   GreyWhaleCast
     AIS               Temporal semantics    ...
     Human activity
     Viewshed
```

Data and spatial toolkits
MarineCast data packages are designed to be usable independently of any particular species model.
Repository	Purpose
viewshed-toolkit	Terrain, canopy, distance, and physical marine viewability modeling
seascape-toolkit	Bathymetry, marine geomorphology, coastal geometry, and derived seascape features
oceanography-toolkit	Ocean temperature, salinity, currents, tides, waves, and related products
meteorology-toolkit	Historical and forecast meteorological data products
ais-toolkit	Vessel tracks, vessel activity, traffic density, and maritime-use products
human-layer-toolkit	Population, access, recreation, infrastructure, and human-presence indicators
Some of these repositories are planned and may not yet exist.
Species applications
Species-specific projects consume MarineCast data products while retaining their own ecological assumptions, features, models, calibration, and evaluation.
OrcaCast
OrcaCast is the first MarineCast application.
It combines whale observations with environmental, oceanographic, seascape, prey, human-activity, acoustic, and observation-effort information to model and forecast killer whale activity.
Future applications could reuse the same underlying infrastructure for other species without duplicating the data-processing stack.
Examples might include:
OrcaCast
HumpbackCast
GreyWhaleCast
...
Design principles
Species-neutral upstream data
Environmental measurements should describe the marine system rather than encode assumptions about a particular species.
For example:
bathymetry → MarineCast data layer
distance to canyon → MarineCast data layer

"canyons increase SRKW habitat suitability"
    → OrcaCast modeling assumption
That separation allows the same data product to support multiple scientific questions.
Reproducible data products
Generated datasets should carry enough information to answer:
What source data were used?
When were they retrieved?
What code produced the output?
What configuration was used?
What geographic and temporal domain does it represent?
What units and spatial support does each variable use?
What validation checks were performed?
Clear scientific boundaries
MarineCast distinguishes measurements from interpretation.
Examples:
vessel traffic ≠ observer effort
physical viewability ≠ detection probability
hydrophone detection ≠ confirmed animal presence
weather conditions ≠ sighting probability
habitat characteristics ≠ species preference
Those relationships belong in downstream models where they can be explicitly tested.
Independent but interoperable
Each toolkit should be able to:
Acquire
   ↓
Normalize
   ↓
Process
   ↓
Validate
   ↓
Publish
   ↓
Consume
without requiring OrcaCast or another species application to be installed.
At the same time, packages should share common conventions for provenance, spatial support, temporal semantics, schemas, and validation.
Architecture
A typical MarineCast workflow looks like:
External data sources
        │
        ▼
┌───────────────────────────────┐
│ MarineCast data toolkits      │
│                               │
│ seascape                      │
│ meteorology                   │
│ oceanography                  │
│ AIS                           │
│ human activity                │
│ viewshed                      │
└───────────────┬───────────────┘
                │
                ▼
       Versioned data products
                │
        ┌───────┼────────┐
        │       │        │
        ▼       ▼        ▼
    OrcaCast   Future   Research
               models   analyses
        │
        ▼
 Species-specific features
        │
        ▼
 Models + evaluation
        │
        ▼
 Forecast products
Repository conventions
MarineCast repositories should generally include:
README.md
AGENTS.md
pyproject.toml

src/
tests/
configs/
docs/
examples/
Where appropriate, repositories should also provide:
a Python API
a command-line interface
documented configuration
offline or synthetic test fixtures
data schemas
provenance metadata
validation reports
reproducible example workflows
Large source and generated datasets should generally not be committed directly to Git.
Project status
MarineCast is under active development.
The architecture is currently being extracted and generalized from the existing OrcaCast codebase. Interfaces, schemas, and repository boundaries may evolve while the shared ecosystem is established.
Current priorities include:
Establishing viewshed-toolkit as a reference reusable package.
Separating reusable seascape processing from OrcaCast.
Defining common dataset and provenance contracts.
Modularizing meteorological, oceanographic, AIS, and human-activity pipelines.
Keeping species-specific modeling logic within applications such as OrcaCast.
Philosophy
MarineCast is not intended to be one enormous marine-science package.
Instead, it is a collection of focused tools that agree on enough conventions to work together.
Small tools
+
explicit contracts
+
reproducible data
+
species-specific science
=
MarineCast
Projects
🐋 OrcaCast
Killer whale presence modeling and forecasting.
👁️ Viewshed Toolkit
Reproducible terrain, canopy, distance, and marine-viewability modeling.
🌊 Additional MarineCast toolkits
Seascape, oceanography, meteorology, vessel activity, and human-use layers are being developed as the ecosystem evolves.
Contributing
MarineCast is currently evolving rapidly.
Issues, ideas, scientific references, data-source recommendations, validation approaches, and code contributions are welcome as individual repositories are opened for broader collaboration.
License
Licensing is defined independently by each MarineCast repository.
Source datasets may have separate licenses, attribution requirements, or redistribution restrictions from the software that processes them.
