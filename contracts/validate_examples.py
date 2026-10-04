#!/usr/bin/env python3
"""Validate bounded synthetic contract fixtures, not production releases or legal claims."""
import copy
import csv
import hashlib
import json
import math
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import h3
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).resolve().parent
STATES = {"observed", "unknown", "unavailable", "not_applicable", "partial"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON property: {key}")
        result[key] = value
    return result


def load(path):
    def bad_constant(value):
        raise ValueError(f"Non-standard JSON number: {value}")
    return json.loads(path.read_text(), object_pairs_hook=unique_object,
                      parse_constant=bad_constant)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(value, field):
    if value == "":
        return None
    kind = field["type"]
    if kind == "integer":
        return int(value)
    if kind == "number":
        return float(value)
    if kind == "boolean":
        require(value in ("true", "false"), "Invalid CSV boolean")
        return value == "true"
    if kind == "date":
        return date.fromisoformat(value)
    if kind == "datetime":
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        require(parsed.tzinfo is not None, "Naive artifact timestamp")
        return parsed
    return value


def artifact_rows(manifest, directory):
    artifact = manifest["artifact"]
    path = (directory / artifact["path"]).resolve()
    require(path.is_relative_to(directory.resolve()), "Artifact escapes fixture directory")
    require(path.is_file(), "Artifact missing")
    require(digest(path) == artifact["sha256"], "Artifact checksum mismatch")
    require(artifact["format"] == "csv", "Fixture runner handles CSV only")
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        require(len(columns) == len(set(columns)), "Duplicate CSV columns")
        require(set(columns) == set(manifest["fields"]), "Artifact column mismatch")
        rows = []
        for row in reader:
            require(None not in row and None not in row.values(), "Malformed CSV row")
            rows.append({name: decode(value, manifest["fields"][name])
                         for name, value in row.items()})
    return rows


def validate_rows(manifest, rows):
    fields = manifest["fields"]
    keys = manifest["identity"]["primary_key"]
    indexes = manifest["spatial"]["index_fields"]
    require(set(keys) <= set(fields), "Unknown primary-key field")
    require(set(indexes) <= set(keys), "H3 fields missing from key")
    require(len(rows) == manifest["artifact"]["row_count"], "Row-count mismatch")
    seen = set()
    expected_types = {"integer": int, "number": (int, float), "boolean": bool,
                      "string": str, "date": date, "datetime": datetime}
    for row in rows:
        require(set(row) == set(fields), "Row column mismatch")
        for name, field in fields.items():
            value = row[name]
            if value is None:
                require(field["nullable"], f"Null non-nullable field: {name}")
            else:
                kind = field["type"]
                require(isinstance(value, expected_types[kind]), f"Wrong type: {name}")
                if kind in ("integer", "number"):
                    require(type(value) is not bool and math.isfinite(value), f"Non-finite number: {name}")
                    if "minimum" in field:
                        require(value >= field["minimum"], f"Below minimum: {name}")
                    if "maximum" in field:
                        require(value <= field["maximum"], f"Above maximum: {name}")
                if "enum" in field:
                    require(value in field["enum"], f"Invalid enum: {name}")
            if field["nullable"]:
                reason = field["missing_reason_field"]
                require(reason in fields and reason in row, f"Unknown status: {name}")
                reason_def = fields[reason]
                require(reason_def["type"] == "string" and not reason_def["nullable"], "Invalid status definition")
                require(set(reason_def.get("enum", [])) == STATES and len(reason_def["enum"]) == len(STATES), "Wrong status enum")
                state = row[reason]
                require(state in STATES, f"Invalid status: {name}")
                if state == "observed":
                    require(value is not None, f"Observed null: {name}")
                elif state != "partial":
                    require(value is None, f"Non-null missing value: {name}")
        key = tuple(row[name] for name in keys)
        require(None not in key and key not in seen, "Null/duplicate primary key")
        seen.add(key)
        for name in indexes:
            cell = row[name]
            require(isinstance(cell, str) and cell == cell.lower() and h3.is_valid_cell(cell), "Invalid H3 index")
            require(h3.get_resolution(cell) == manifest["spatial"]["resolution"], "Wrong H3 resolution")
        temporal = manifest["temporal"]
        if temporal["type"] == "interval":
            start, end = row[temporal["start_field"]], row[temporal["end_field"]]
            require(start.tzinfo is not None and end.tzinfo is not None and start < end, "Invalid interval")
            if "label_field" in temporal:
                require(row[temporal["label_field"]] == start.astimezone(ZoneInfo(temporal["timezone"])).date(), "Wrong fixture date label")


def validate_reference_source(manifest, rows, directory):
    source_path = directory / "synthetic-boundaries.geojson"
    source = load(source_path)
    source_version = "synthetic-boundaries.geojson@sha256=" + digest(source_path)
    require(manifest["provenance"]["sources"][0]["source_version"] == source_version, "Native source fingerprint mismatch")
    config = load(directory / "synthetic-config.json")
    features = source["features"]
    ids = [feature["properties"]["feature_id"] for feature in features]
    require(len(ids) == len(set(ids)), "Duplicate native feature ID")
    for feature in features:
        props = feature["properties"]
        ring = [[lng, lat] for lat, lng in h3.cell_to_boundary(props["fixture_h3"])]
        ring.append(ring[0])
        require(feature["geometry"] == {"type": "Polygon", "coordinates": [ring]}, "Synthetic boundary no longer matches declared cell")
        require(props["effective_from"] is None and props["effective_to"] is None, "Fixture acquired unsupported effective dates")
    by_cell = {row["h3_index"]: row for row in rows}
    require(set(by_cell) == {item["h3_index"] for item in config["cells"]}, "Source universe mismatch")
    for item in config["cells"]:
        row = by_cell[item["h3_index"]]
        expected, available = item["expected_sources"], item["available_sources"]
        coverage = len(available) / len(expected) if expected else None
        require(row["source_inventory_coverage_fraction"] == coverage, "Coverage denominator mismatch")
        if available:
            count = sum(feature["properties"]["fixture_h3"] == item["h3_index"] and
                        feature["properties"]["source_id"] in available for feature in features)
            require(row["reference_feature_count"] == count, "Count not traceable to native fixture")


def validate_artifact(manifest, path, rows=None):
    original = artifact_rows(manifest, path.parent)
    require(digest(path.parent / "synthetic-config.json") == manifest["provenance"]["configuration"]["sha256"], "Configuration checksum mismatch")
    rows = original if rows is None else rows
    validate_rows(manifest, rows)
    if manifest["product"]["quantity_kind"] == "reference_geometry":
        validate_reference_source(manifest, rows, path.parent)
    return rows


def update(document, pointer, value):
    parts = pointer.lstrip("/").split("/")
    current = document
    for part in parts[:-1]:
        current = current[part]
    current[parts[-1]] = value


def main():
    schemas = {"0.1": load(ROOT / "product-manifest.schema.json"),
               "0.2": load(ROOT / "v0.2/product-manifest.schema.json")}
    expected = copy.deepcopy(schemas["0.1"])
    expected["title"] = "MarineCast data-product manifest v0.2 (reference geometry extension)"
    expected["properties"]["contract_version"]["const"] = "0.2"
    expected["properties"]["product"]["properties"]["quantity_kind"]["enum"].append("reference_geometry")
    require(schemas["0.2"] == expected, "v0.2 expanded beyond the approved version/title/category delta")
    validators = {}
    for version, schema in schemas.items():
        Draft202012Validator.check_schema(schema)
        validators[version] = Draft202012Validator(schema, format_checker=FormatChecker())
    old_paths = sorted((ROOT / "examples").glob("*.manifest.json"))
    require(len(old_paths) == 4, "Unexpected v0.1 fixture inventory")
    for path in old_paths:
        manifest = load(path)
        validators["0.1"].validate(manifest)
        validate_artifact(manifest, path)
        converted = copy.deepcopy(manifest)
        converted["contract_version"] = "0.2"
        validators["0.2"].validate(converted)
        validate_artifact(converted, path)
        print(f"PASS v0.1 artifact and v0.2 compatibility: {path.name}")
    path = ROOT / "v0.2/examples/governance-reference.manifest.json"
    base = load(path)
    validators["0.2"].validate(base)
    rows = validate_artifact(base, path)
    print("PASS v0.2 Governance schema, artifact, source geometry and coverage")
    cases = load(path.parent / "negative-cases.json")
    require(cases["base_manifest"] == path.name, "Wrong negative fixture base")
    for case in cases["cases"]:
        manifest = copy.deepcopy(base)
        mutated_rows = copy.deepcopy(rows)
        for pointer, value in case.get("manifest_updates", {}).items():
            update(manifest, pointer, value)
        for mutation in case.get("row_updates", []):
            mutated_rows[mutation["row"]][mutation["field"]] = mutation["value"]
        phase = "schema"
        try:
            validators[case.get("schema_version", "0.2")].validate(manifest)
            phase = "artifact"
            validate_artifact(manifest, path, mutated_rows)
        except (ValidationError, ValueError) as error:
            require(phase == case["phase"], f"Wrong rejection phase for {case['name']}: {error}")
            print(f"PASS rejected {case['name']} ({phase})")
        else:
            raise ValueError(f"Accepted negative fixture: {case['name']}")
    print(f"PASS: both schema definitions, 4 legacy artifacts, 4 v0.2 compatibility cases, 1 new source-backed artifact, {len(cases['cases'])} negatives")


if __name__ == "__main__":
    main()
