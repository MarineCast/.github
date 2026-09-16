"""Validate routing files and local links without executing toolkit pipelines (requires PyYAML)."""
import argparse
import csv
import re
from pathlib import Path
import subprocess
import yaml


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workspace', type=Path)
    args = parser.parse_args()
    root = args.workspace.resolve()
    manifest = yaml.safe_load((root / 'WORKSPACE.yaml').read_text())
    assert manifest['version'] == 1
    docs = [root / 'AGENTS.md']
    expected = {'viewshed': 'viewshed_toolkit', 'seascape': 'seascape',
                'meteorology': 'meteorology', 'oceanography': 'oceanography'}
    for name, entry in manifest['repositories'].items():
        repo = (root / entry['path']).resolve()
        assert repo.is_relative_to(root) and (repo / '.git').exists(), name
        assert (repo / 'AGENTS.md').is_file(), name
        docs.append(repo / 'AGENTS.md')
        if entry['graphify']:
            assert entry['package'] == expected[name.removeprefix('toolkit-')]
            assert (repo / 'src' / entry['package'] / '__init__.py').exists()
            assert (repo / 'graphify-out/graph.json').is_file()
            subprocess.run(['git', '-C', str(repo), 'check-ignore', '-q', 'graphify-out/graph.json'], check=True)
        if entry['status'] == 'scaffold':
            assert not (repo / '.agents').exists(), name
    assert not (root / '.git').exists()
    assert not (root / 'graphify-out').exists()
    skills = list((root / 'Toolkits/toolkit-viewshed/.agents/skills').glob('*/SKILL.md'))
    assert len(skills) == 5
    for skill in skills:
        text = skill.read_text()
        metadata = yaml.safe_load(text.split('---', 2)[1])
        assert metadata['name'] == skill.parent.name
        assert metadata.get('description')
        docs.append(skill)
    docs.extend((root / '.github/docs').glob('*.md'))
    docs.extend((root / '.github/agent-evals').glob('*.md'))
    docs.append(root / '.github/README.md')
    links = 0
    for doc in docs:
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if '://' in target or target.startswith('#'):
                continue
            target = target.split('#')[0]
            assert (doc.parent / target).exists(), (doc.relative_to(root), target)
            links += 1
    results = root / '.github/agent-evals/results.csv'
    with results.open(newline='') as handle:
        reader = csv.DictReader(handle)
        assert 'source_files_opened' in reader.fieldnames
        assert 'task_success' in reader.fieldnames
        rows = list(reader)
    print(f'Validated {len(manifest["repositories"])} repository routes, {len(skills)} skills, '
          f'{links} local links, {len(rows)} benchmark rows; no pipelines run.')


if __name__ == '__main__':
    main()
