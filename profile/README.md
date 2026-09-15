# OrcaCast 🌊🐋

**Reusable data infrastructure for marine wildlife modeling and forecasting.**

OrcaCast is an open scientific software ecosystem for building reproducible spatial and temporal data products used in marine-species models.

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
