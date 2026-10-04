# MarineCast manifest contract v0.2 reference geometry

**Tyler approved adding `reference_geometry` on 2026-10-04. The extension is recorded as version `0.2`; toolkit adoption and application integration remain separately evidenced.**

The [v0.2 schema](product-manifest.schema.json) adds one quantity category to the [v0.1 contract](../README.md). The original [v0.1 schema](../product-manifest.schema.json) and [examples](../examples/README.md) are unchanged. The only schema differences are the version constant (`0.2`), title and addition of `reference_geometry` to `product.quantity_kind`. No other quantity categories, properties, formats or spatial/temporal scopes are added.

## Reference geometry meaning

`reference_geometry` describes **source-backed boundary/geometry inventories or reference overlays**. It can describe a declared H3 projection of native geometry, such as feature counts, unioned area fractions, line length or point counts, with explicit support, denominator, method, source identity and limitations. A reference category is not an environmental condition or probability simply because it has numeric columns.

These products do **not** establish controlling legal authority, regulatory applicability or compliance. A geometry intersection, source name or inventory record alone cannot determine which rule governs a person, vessel, location or activity. Preserve source authority statements as attributed evidence, not a new claim that the output is controlling. Quantity classification does not authorize legal interpretation or make a product model-eligible.

Retain native feature IDs, geometry-part identity, geometry, attributes, coordinate reference, source vintage and provenance where needed to recover the summary's meaning. Independent attribute sets must not masquerade as aligned feature records. Counts and overlay fractions state their universe, union/deduplication behavior and spatial support; partial or unknown inventories do not become complete empty intersections. Roster coverage is distinct from geographic completeness.

## Native and H3 boundaries

The category's scientific meaning includes native reference inventories, but this schema remains an **H3 table manifest**. Native geometries continue to use their owning toolkit's native contracts/manifests. They may be retained as pinned source evidence or companions; do not put arbitrary GeoJSON, rasters or an artifact bundle into `artifact` and claim v0.2 conformance.

v0.2 retains the existing scope: one single-resolution H3 cell, centroid, cell-subset or directed-pair CSV/Parquet table with static, instant or interval support. Forecast issue/lead-time, ensembles, mixed-resolution tables and multi-artifact generation protocols remain deferred. All other [v0.1 meaning, validation and acceptance requirements](../README.md#required-meaning) apply unchanged, including complete keys, units, null/status consistency, source rights, recoverable provenance and exact artifact checksums.

The [approved application delivery defaults](../application-delivery-profile.md) remain wide Parquet, static cell rows or daily UTC cell/interval rows, readable metric names, preserved variants and accurately qualified missingness/coverage. The scoped R7 exception remains specific to Viewshed and related Human/viewability variables; broader resolution policy is still exploratory. A CSV/pair/native fixture can illustrate the broader manifest contract without satisfying that narrower application delivery profile.

## Time, rights and limitations

Distinguish source vintage, retrieval, processing, publication/availability and applicability. Static reference snapshots retain their reference period and limitations; retrieval or creation time is not a legal effective date. Unknown effective-time evidence must be explicit. A date-specific legal reconstruction requires separately reviewed source evidence and methods; this category addition does not approve one.

Sources retain version/fingerprint, coverage, license, attribution and redistribution terms. Unknown rights remain unknown and are not permission to publish. An adopter must preserve source-level restrictions and limitations through projection. Scientific method version, software version, semantic product version and immutable generated-data release identity remain distinct under the approved delivery profile.

## Version selection and adoption

- v0.1 consumers continue to select the unchanged `contracts/product-manifest.schema.json` and require `contract_version: "0.1"`. They cannot accept `reference_geometry` or silently reinterpret it as another kind.
- v0.2 consumers explicitly select `contracts/v0.2/product-manifest.schema.json` and require `contract_version: "0.2"`. The eight original kinds remain supported, but the version must match. Consumers supporting both versions dispatch on an explicit allowlist rather than a mutable latest schema.
- Changing only a manifest version does not establish adoption. Validate the native-to-H3 mapping, generated artifact and consumer acceptance against the chosen version, with code SHA, method/software/release identities, commands/results and reviewer decision.
- An individual Governance data release may remain under its native manifest until its adopter implements and verifies v0.2. This change edits no toolkit or final data and recertifies no existing release.

## Fixtures and validation

The [synthetic Governance example](examples/README.md) is backed by retained invented geometry/configuration. It demonstrates true zero, partial coverage and null states, with rights/provenance and effective-time limitations. It contains no real provider evidence or real Governance output.

From the repository root, in a dedicated environment:

```sh
python3 -m venv /tmp/marinecast-contract-validation
/tmp/marinecast-contract-validation/bin/python -m pip install -r contracts/validation-requirements.txt
/tmp/marinecast-contract-validation/bin/python contracts/validate_examples.py
```

The runner checks both Draft 2020-12 schema definitions with format checking, all four original artifacts, their compatibility under v0.2 with an in-memory version change, the new Governance schema/artifact/source fixture, and ten negative cases. It checks CSV columns/types, keys, H3 validity/resolution, finite/range/enum values, per-metric status relationships, interval labels, hashes and fixture-source coverage. The schema delta is constrained to the three documented changes.

This is a bounded synthetic-fixture runner, not a complete production validator, Parquet reader, arbitrary-geometry overlay engine, rights verifier or legal/scientific certification. Real-source qualification, adopter validation and any production publication remain separate work. Missing validator dependencies cause failure; they are not treated as passing checks.
