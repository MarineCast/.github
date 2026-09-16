# Synthetic v0.1 examples

These fixtures illustrate the [proposed contract](../README.md). They are hand-authored, not
toolkit exports. Distribution names reflect local toolkit documentation; version and Git revision
values are explicitly fictitious. No external data or genuine producer build is represented.

| Manifest | What it demonstrates |
| --- | --- |
| [seascape-static](seascape-static.manifest.json) | Static cell support, depth sign/datum, true zero versus unavailable/null. |
| [meteorology-utc](meteorology-utc.manifest.json) | A 24-hour UTC interval with a date label and a partial estimate. |
| [meteorology-local-day](meteorology-local-day.manifest.json) | A 23-hour local day across daylight saving, with the same date label as the UTC example but different absolute support. |
| [viewshed-pairs](viewshed-pairs.manifest.json) | Directed source/target pairs, source roles, bounded physical weights and unknown/null. |

Each manifest references its adjacent CSV and fingerprints its exact bytes and the shared
[synthetic configuration](synthetic-config.json). CSV empty cells mean null. The H3 cells are
real index strings; the measurements are invented. Fixture tables are CC0-1.0.

The meteorology examples intentionally use an illustrative hourly statistic. They do not redefine
the toolkit's six-snapshot HRRR aggregation. UTC and local-day tables must not be joined on `date`
as if they described identical intervals. Likewise, viewshed weights must not be interpreted as
sighting probabilities merely because they lie in [0, 1].

Run the structural validation command in the specification with format checking enabled. Full
adoption also requires the artifact-level and scientific compatibility checks described there.
