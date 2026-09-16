"""Report sizes/paths only for Git-visible text files; never emit source content."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess


def inventory(repo):
    names = subprocess.check_output(
        ['git', '-C', str(repo), 'ls-files', '-z', '--cached', '--others', '--exclude-standard']
    ).decode().split('\0')
    rows, groups, hashes = [], defaultdict(int), defaultdict(list)
    for name in sorted(set(names) - {''}):
        path = repo / name
        if path.is_symlink() or not path.is_file():
            continue
        raw = path.read_bytes()
        if b'\0' in raw:
            continue
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            continue
        row = dict(path=name, bytes=len(raw), characters=len(text),
                   lines=len(text.splitlines()), words=len(text.split()))
        rows.append(row)
        group = '/'.join(Path(name).parts[:3]) if name.startswith('src/') else Path(name).parts[0]
        groups[group] += len(raw)
        if raw:
            hashes[hashlib.sha256(raw).hexdigest()].append(name)
    return dict(repository=repo.name, text_files=len(rows), total_bytes=sum(r['bytes'] for r in rows),
                agents=next((r for r in rows if r['path'] == 'AGENTS.md'), None),
                largest_files=sorted(rows, key=lambda r: r['bytes'], reverse=True)[:8],
                largest_source_areas=sorted(((k, v) for k, v in groups.items() if k.startswith('src/')),
                                            key=lambda kv: kv[1], reverse=True)[:5],
                exact_duplicate_groups=[v for v in hashes.values() if len(v) > 1],
                files=rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workspace', type=Path)
    args = parser.parse_args()
    repos = [args.workspace / 'Toolkits' / ('toolkit-' + n)
             for n in ('viewshed', 'seascape', 'meteorology', 'oceanography')]
    print(json.dumps([inventory(p) for p in repos], indent=2))


if __name__ == '__main__':
    main()
