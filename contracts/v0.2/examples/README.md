# Synthetic reference geometry fixture

All geometry, values, rosters, dates and producer identities here are invented. The fixture is CC0-1.0; no real provider data, legal authority, toolkit adoption or real-source validation is represented. It illustrates the [v0.2 contract](../README.md), not an operational Governance release.

- [governance-reference.manifest.json](governance-reference.manifest.json): version `0.2`, product kind `reference_geometry`, static single-resolution H3 summary, provenance/rights and effective-time limitations.
- [governance-reference.csv](governance-reference.csv): six wide synthetic rows with feature count, independent metric status and source-roster coverage fields. CSV exercises the broader schema; approved application delivery remains wide Parquet. R6 is an illustrative fixture resolution, not an approved assignment.
- [synthetic-boundaries.geojson](synthetic-boundaries.geojson): two invented cell-boundary polygons with feature/source identity. This is retained native source evidence, not a new geometry artifact type supported by the H3 manifest.
- [synthetic-config.json](synthetic-config.json): exact expected/available source rosters, scientific method version and immutable synthetic data release identity. The manifest fingerprints these bytes and the native source bytes.
- [negative-cases.json](negative-cases.json): declarative mutations of the positive fixture with expected schema/artifact rejection phases. The runner applies mutations only in memory and preserves original files.

## Meaning of the rows

The count is a distinct native-feature count among available sources in the cell. It is a reference inventory quantity, not a probability, absence of regulation or compliance finding. Synthetic polygons are exactly the declared H3 boundaries; validation checks their coordinates and reconciles counts to retained feature IDs. It does not run or validate real-source overlay software.

Coverage is **available source count / expected source count**, equally weighted for this fixture only. A known 0/1 coverage is a valid derived zero even when the feature count is unavailable. A 1/2 roster yields a partial count with coverage 0.5. This is source-roster coverage, not geographic completeness. Unknown/undefined expected support remains null; no universal coverage threshold is selected.

| Case | Feature count/status | Coverage/status |
| --- | --- | --- |
| Complete roster with one feature | `1`, `observed` | `1`, `observed` |
| Complete bounded roster with no feature | `0`, `observed` | `1`, `observed` |
| One of two expected sources available | `1`, `partial` | `0.5`, `observed` |
| Expected source unavailable | null, `unavailable` | `0`, `observed` |
| Source state unknown | null, `unknown` | null, `unknown` |
| Quantity not applicable | null, `not_applicable` | null, `not_applicable` |

Separate status columns matter: the feature count and coverage fraction do not always have the same state. `observed` means valid measured/derived under the existing contract, not necessarily a raw observation. Effective dates are null in the invented native features. Snapshot/retrieval times cannot be used as legal effective times or evidence of historical availability.

## Negative cases

Schema negatives reject unknown kinds, unsupported/mismatched versions, and `reference_geometry` under v0.1. Artifact negatives reject an invalid status code (`valid` instead of the unchanged `observed` code), observed-null or unavailable-non-null values, incorrectly shared status, checksum mismatch and duplicate cell keys. Row mutations target semantic validation after validating the original fixture bytes; the schema itself cannot inspect table values.

Run the [documented validator command](../README.md#fixtures-and-validation) from the repository root. Passing these fixtures proves only the tested structural/artifact behavior; it does not establish live producer support, source rights, legal applicability or scientific eligibility.
