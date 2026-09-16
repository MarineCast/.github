# Context footprint audit — 2026-09-15

## Method and limits

Repomix was not on PATH and was not installed. No Repomix token-count run occurred. The fallback
`python3 agent-evals/context_inventory.py /path/to/MarineCast` (from this documentation checkout)
counts bytes, characters, words and lines of Git-visible UTF-8 files, including current untracked
instruction files; ignored caches and binary files are excluded. It prints metadata only. No
repository content was packed into model context. Sizes are not actual Codex token consumption.
The before snapshot was captured at task start, including the earlier progressive Graphify edits.
Architecture/methodology documents and generated reports were retained.

## Instruction footprint

| AGENTS location | Lines before → after | Characters before → after |
| --- | ---: | ---: |
| `AGENTS.md` | 78 → 90 | 5,183 → 5,967 |
| `.github/AGENTS.md` | 38 → 41 | 2,307 → 2,585 |
| `Toolkits/toolkit-viewshed/AGENTS.md` | 303 → 117 | 17,683 → 7,356 |
| `Toolkits/toolkit-seascape/AGENTS.md` | 115 → 92 | 7,066 → 5,502 |
| `Toolkits/toolkit-meteorology/AGENTS.md` | 114 → 92 | 6,951 → 5,423 |
| `Toolkits/toolkit-oceanography/AGENTS.md` | 115 → 93 | 7,041 → 5,511 |

Viewshed moves conditional instructions into five skills. Loading all five would defeat the
purpose: routing should load only applicable guidance. Skill metadata itself has a discovery cost.
The smaller toolkit routers retain their domain safeguards and route to existing documentation;
no symmetric empty skills were added. Shared short navigation rules remain in each standalone clone;
optional installation/evaluation detail lives once in the organization docs.

## Largest contributors

### toolkit-viewshed

Git-visible text snapshot: 213 files, 5,401,651 bytes.

| File | Bytes |
| --- | ---: |
| `analysis/salish_sea/report.html` | 3,558,366 |
| `src/viewshed_toolkit/pipeline/weights/terrain/runner.py` | 64,939 |
| `src/viewshed_toolkit/pipeline/weights/terrain/gdal.py` | 54,337 |
| `src/viewshed_toolkit/pipeline/weights/terrain/los.py` | 50,265 |
| `src/viewshed_toolkit/pipeline/finalize/final_artifacts.py` | 48,692 |

Largest source areas: `src/viewshed_toolkit/pipeline` (1,289,060 bytes); `src/viewshed_toolkit/_internal` (70,220 bytes); `src/viewshed_toolkit/resources` (10,001 bytes).

Architecture reference `ARCHITECTURE.md`: 12,093 bytes; retain and load by task.
Exact nonempty duplicate groups: 1 (content hashes).

### toolkit-seascape

Git-visible text snapshot: 221 files, 3,322,659 bytes.

| File | Bytes |
| --- | ---: |
| `config/feature_catalog.yaml` | 369,046 |
| `src/seascape/resources/config/feature_catalog.yaml` | 369,046 |
| `config/model_feature_policy.yaml` | 320,443 |
| `src/seascape/resources/config/model_feature_policy.yaml` | 320,443 |
| `docs/products.md` | 206,842 |

Largest source areas: `src/seascape/resources` (897,483 bytes); `src/seascape/hydrologic_connectivity` (247,548 bytes); `src/seascape/spatial_support` (208,845 bytes).

Architecture reference `docs/ARCHITECTURE.md`: 4,458 bytes; retain and load by task.
Exact nonempty duplicate groups: 4 (content hashes).

### toolkit-meteorology

Git-visible text snapshot: 92 files, 736,134 bytes.

| File | Bytes |
| --- | ---: |
| `config/feature_catalog.yaml` | 65,777 |
| `src/meteorology/resources/config/feature_catalog.yaml` | 65,777 |
| `src/meteorology/surface_weather/download.py` | 35,496 |
| `src/meteorology/surface_weather/time_series_map.py` | 34,412 |
| `config/model_feature_policy.yaml` | 31,992 |

Largest source areas: `src/meteorology/surface_weather` (162,075 bytes); `src/meteorology/resources` (101,858 bytes); `src/meteorology/core` (74,003 bytes).

Architecture reference `docs/ARCHITECTURE.md`: 3,487 bytes; retain and load by task.
Exact nonempty duplicate groups: 6 (content hashes).

### toolkit-oceanography

Git-visible text snapshot: 45 files, 221,140 bytes.

| File | Bytes |
| --- | ---: |
| `src/oceanography/build.py` | 22,403 |
| `src/oceanography/inspect.py` | 21,105 |
| `src/oceanography/download.py` | 12,798 |
| `LICENSE` | 11,595 |
| `src/oceanography/regional_sources.py` | 11,145 |

Largest source areas: `src/oceanography/build.py` (22,403 bytes); `src/oceanography/inspect.py` (21,105 bytes); `src/oceanography/download.py` (12,798 bytes).

Architecture reference `docs/ARCHITECTURE.md`: 2,267 bytes; retain and load by task.
Exact nonempty duplicate groups: 3 (content hashes).

## Actions and interpretation

- Viewshed’s 3.56 MB rendered report is tracked intentionally, and already excluded by
  `.graphifyignore`. Avoid it during normal code navigation; inspect it only for report/visual tasks.
- Seascape’s feature catalogs and model-policy YAML dominate context. Packaged/editable copies are
  required parity contracts, not redundant files to delete. Search the relevant field and its owner.
- Meteorology has similar intentional packaged-config duplication; scope acquisition and map reads.
- Oceanography’s main build/inspection modules are comparatively concentrated. Read symbol ranges
  after structural lookup; this audit does not justify a source refactor.
- No tracked Graphify cache was found. Existing ignore policies are retained. Generated product docs
  can be large and useful; do not treat their size alone as evidence they should be removed.
- AGENTS boilerplate originally repeated detailed installation/hook/sharing explanations. Common
  setup is now on demand; standalone operational safeguards remain local.

## Optional Repomix follow-up (not run)

After an operator provides Repomix, check its installed `--help` and run in one toolkit at a time:

```sh
repomix --version
repomix --help
repomix --token-count-tree 1000 --top-files-len 10 --output /dev/null
```

Keep default ignore/security rules. Capture only the counts/tree summary, never packed output.
Repomix need not use `.graphifyignore`, so verify exclusions and use `--ignore` explicitly when
a scope should omit rendered reports/assets. Audit their footprint separately rather than hiding it.
The [upstream CLI reference](https://repomix.com/guide/command-line-options) documents these flags.
Record the installed version, tokenizer and included paths. Do not introduce Repomix as routine
retrieval or a toolkit dependency. Actual savings require the [20-task benchmark](../agent-evals/README.md).
