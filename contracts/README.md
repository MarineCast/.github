# MarineCast data-product contract v0.1

**Status: proposed; no toolkit adoption or OrcaCast integration is established by this spec.**
This is a small interchange contract for species-neutral tabular products. It supplements the
[infrastructure requirements](../INFRASTRUCTURE.md#data-integration-requirements); each toolkit
continues to own its science, native schemas, validation and publication workflow.

The goal is agreement on meaning before integration. Identically named `h3_index`, `date`, and
`value` columns are insufficient: consumers must agree on grain, units, support, time boundaries,
missingness and provenance before joining products.

## Scope and files

- [product-manifest.schema.json](product-manifest.schema.json): JSON Schema Draft 2020-12 for
  one manifest describing one complete table artifact.
- [examples/](examples/): synthetic JSON manifests, small CSV tables and the exact configuration
  bytes they fingerprint. They illustrate the proposal, not existing toolkit exports or real data.

v0.1 covers single-resolution H3 cell, centroid, cell-subset and directed cell-pair tables in
Parquet or CSV, with static, instantaneous or interval time support. Raster, mixed-resolution,
forecast issue/lead-time, ensembles and multi-artifact publication contracts are deferred. Do
not force those products into this schema or discard dimensions to make them fit. Additional
profiles require a reviewed contract revision. Existing toolkit manifests remain authoritative
until a toolkit explicitly implements this proposal.

There is no `marinecast-core` package, shared runtime, registry or new execution service. Start
with independent implementations in two or three toolkits, then consider extracting shared code
only where actual duplication demonstrates a need.

## Required meaning

The words **must** and **reject** describe conformance requirements for future adopters; they do
not claim that existing producers or consumers enforce them today.

| Block | Required agreement |
| --- | --- |
| `contract_version` | Exact manifest contract version (`0.1` here); distinct from product or package version. |
| `product` | Stable namespaced ID, semantic product version, description, and kind of quantity. |
| `producer` | Toolkit repository, installed distribution name/version, full Git revision and dirty-tree state. |
| `identity` | What one row represents and the complete, unique, non-null primary key. |
| `spatial` | H3 resolution, index columns, support, domain, CRS and spatial assignment/aggregation method. |
| `temporal` | Static meaning or explicit time columns, zone and interval semantics. |
| `fields` | Every column's logical type, meaning, units, nullability and statistic. |
| `provenance` | Creation time, configuration fingerprint, sources, coverage, rights and processing method. |
| `artifact` | Manifest-relative file path, format, SHA-256 of exact file bytes and row count. |
| `limitations` | Known gaps and scientific/reproducibility limits; use an empty list only when none are known. |

### Identity and spatial support

Keys must reference declared fields and be unique across the entire artifact. Additional axes
(source role, depth, etc.) belong in the key when needed to distinguish rows. Never join by row
order or resolve duplicates with an arbitrary first row.

H3 indices are canonical lowercase strings, validated as cells at the declared resolution.
`index_fields` must be included in the primary key. `cell_pair` has exactly two ordered index
fields: source then target; reversing them changes meaning. Combined viewshed source roles need
a role key such as `source_type` in addition to `source_h3` and `target_h3`.

`crs: EPSG:4326` describes geographic reference, not planar area or distance units. `method` must
explain centroid sampling, area aggregation, wet-cell subsets, or directed pair calculations as
applicable. `domain` must identify the intended cell universe and exclusions; production use
must pin a reproducible definition or fingerprinted support artifact. An absent row does not
mean zero, and a table's observed rows alone do not establish complete domain coverage.

### Time and aggregation

- `static` means no row-level time axis; `meaning` must state the reference period or applicability.
  It does not mean the source never changes. Retrieval and creation times are not valid times.
- `instant` requires a declared, non-null `datetime` time field in the key.
- `interval` requires non-null `datetime` start and end fields, both in the key, with start < end.
  Intervals are always **[start, end)**. `aggregation` states sampling cadence, weighting,
  completeness requirements and treatment of partial observations. Per-field `statistic` states
  whether values are means, sums, maxima, samples or other explicitly defined operations.
- `timezone` is `UTC` or an IANA zone used to interpret the time axis or construct interval
  boundaries. Datetimes in artifacts must be RFC 3339 strings with offsets (or equivalent
  timezone-aware Parquet timestamps). Naive timestamps are rejected. Compare absolute instants.
- An optional interval `label_field` must be a non-null `date` or `string` column with a
  `label_definition`. It is a convenience label; it cannot replace the interval boundaries.
  A local calendar day can have 23 or 25 hours. Consumers must not relabel it as a UTC day.

Overlapping intervals, repeated samples and conversion between daily and weekly support require
an explicit downstream aggregation rule. Never shift source dates to fill requested coverage.
Forecast products need a future profile preserving issue time, lead time and valid time separately.

### Values and missingness

`units` must name the actual unit, use `1` for dimensionless measurements, and use JSON `null`
only when units do not apply (identifiers, labels, timestamps or status codes). Descriptions
must state sign/direction conventions, vertical datum where relevant, categories, and the
physical quantity. `minimum`/`maximum` are inclusive and apply to non-null numeric values;
`enum` defines non-null string categories. Numeric values must be finite. Bounds of [0, 1]
are appropriate only when the field's scientific definition requires them.

Each nullable field must name a declared, non-null string `missing_reason_field`. That column
must declare exactly these codes in its `enum`:

| Code | Value interpretation |
| --- | --- |
| `observed` | A valid value, including true zero or a valid derived result. |
| `unknown` | Null; reason or state is not known. |
| `unavailable` | Null; expected source or result was unavailable. |
| `not_applicable` | Null; the quantity does not apply to this row. |
| `partial` | Null or a finite estimate from incomplete support; interpretation and coverage rule must be documented. |

`observed` requires a non-null value; `unknown`, `unavailable`, and `not_applicable` require
null. A shared reason column is allowed only if its state is correct for every referencing
field on every row. Additional quality or coverage columns may be declared, but cannot silently
collapse these states. Nulls must never be replaced with zero or numeric sentinels.

Parquet uses native nulls. CSV uses UTF-8, a header, comma delimiters, standard double-quote
escaping, and empty cells exclusively for null; literal empty strings are not supported.
CSV booleans are `true`/`false`, dates are `YYYY-MM-DD`, and datetimes follow the rule above.
Consumers decode the declared logical types before validation.

Environmental conditions, physical viewability, human/vessel activity, reporting, detection,
acoustic observations and species occurrence remain distinct. A dimensionless weight is not
automatically a probability. Any downstream interpretation must document its assumptions.

### Provenance, rights and publication

Each source needs an ID, version (explicit `null` when unavailable), retrieval time, spatial and
temporal coverage, license, attribution and redistribution terms. Unknown rights must say so;
they are not permission to redistribute. Missing source versions or dirty code must be reflected
in `limitations`; consumers decide whether their reproducibility policy permits them.
`processing` must describe the scientific transformation or pin a versioned method reference.

The configuration SHA-256 covers the exact effective configuration bytes, including defaults
and overrides; `description` must identify their encoding and how they are retained/retrieved.
Fingerprints are evidence of identity, not a guarantee of recoverability. Multiple sources and
upstream products must be listed explicitly, with upstream versions and artifact hashes pinned
in their source IDs/version metadata rather than a mutable `latest` reference.

Artifact paths are relative to the manifest directory, with no absolute paths, URI schemes or
parent traversal. Readers must also reject symlink escapes. Checksums cover exact artifact bytes,
not decoded rows. Producers must finish and validate the artifact before exposing its manifest;
publish the immutable pair using the owning toolkit's documented completion/atomicity mechanism.
This spec does not standardize transactions across products. A checksum mismatch, absent file or
unvalidated staging manifest is not a consumable product.

## Validation and consumer acceptance

**Schema-valid is not data-valid or scientifically compatible.** Use a Draft 2020-12 validator
with format checking enabled. JSON is the canonical manifest encoding; reject duplicate object
keys and non-standard numeric constants. A producer may serialize equivalent JSON-compatible
YAML, but its loader must preserve strings/nulls and reject duplicate keys and custom tags.

The schema checks structure, required metadata, H3 resolution bounds, hash syntax and conditional
time support. It cannot inspect files, interpret prose, enforce column references or prove rights.
Producer validation and consumer acceptance must additionally check:

1. Artifact containment, existence, hash, row count, exact declared column set and logical types.
2. All column references, complete/non-null/unique keys, H3 validity/resolution and intended domain.
3. Time types, zone validity, boundary ordering, labels and declared temporal support.
4. Finite/range/category checks, units, missing-reason enums and row-level value/status consistency.
5. Source/configuration availability, coverage, method and limitations required by the consumer.
6. Expected product ID/version, quantity kind, spatial and temporal alignment, and planned join
   cardinality. Reject incompatible products; never infer compatibility from column names alone.

An example structural check, from this repository, in an environment with `jsonschema` installed:

```sh
python - <<'PY'
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
root = Path('contracts')
schema = json.loads((root / 'product-manifest.schema.json').read_text())
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema, format_checker=FormatChecker())
for path in sorted((root / 'examples').glob('*.manifest.json')):
    validator.validate(json.loads(path.read_text()))
    print(path, 'schema valid')
PY
```

This checks manifest structure only. Toolkit adoption must include artifact-level checks and
negative fixtures for duplicate keys, wrong resolution, UTC/local-day mismatch, null-to-zero
conversion, status disagreement and checksum mismatch.

## Versioning and adoption

Consumers explicitly allow supported contract versions; `0.1` is not an implicit compatibility
promise for later drafts. Product versions use `major.minor.patch`: changes to grain, units,
support, missingness, sign conventions or scientific calculations require a major increment;
additive optional information may be minor; metadata corrections without semantic changes may
be patch. Consumers still check fields explicitly. Package versions identify software and are
not substitutes for product versions. New data/configuration builds may retain the product
version if meaning is unchanged; their artifact hash and provenance identify the specific build.

Unknown core properties are rejected. Optional `extensions` uses producer-owned namespaced keys;
extensions cannot override core meaning or carry information required for safe interpretation.

Suggested first adopters are seascape, meteorology and viewshed, exercising static cells, local-day
intervals and directed pairs. Each adoption should document the mapping from its native contract,
emit a sidecar without silently changing scientific outputs, and validate a consumer round-trip.
Record adoption only after those checks pass. Oceanography and OrcaCast integration follow their
own readiness and input requirements. No implementation or migration is performed by this draft.
