#!/usr/bin/env python3
"""Collect aggregate GitHub release counters; never download the release assets."""
import argparse
import csv
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
import re
import subprocess


def api_pages(endpoint):
    result = subprocess.run(
        [os.environ.get('GH_BINARY', 'gh'), 'api', '--paginate', '--slurp', endpoint],
        check=True, capture_output=True, text=True,
    )
    pages = json.loads(result.stdout)
    if not isinstance(pages, list) or any(not isinstance(page, list) for page in pages):
        raise ValueError('Expected paginated GitHub lists')
    return [item for page in pages for item in page]


def category(name):
    lower = name.lower()
    if lower.endswith('.lunaaddon'):
        return 'add-on'
    if lower.endswith('.zip'):
        return 'helper/setup'
    if 'sha256' in lower or 'checksum' in lower:
        return 'checksum (excluded)'
    return 'other (excluded)'


def collect(repository, api=api_pages, sampled_at=None):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Expected owner/repository')
    sampled_at = sampled_at or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    releases = []
    for release in api(f'repos/{repository}/releases?per_page=100'):
        if release['draft']:
            continue
        release_id = int(release['id'])
        assets = []
        # Fetch asset pages explicitly as well as release pages.
        for asset in api(f'repos/{repository}/releases/{release_id}/assets?per_page=100'):
            count = asset['download_count']
            if type(count) is not int or count < 0:
                raise ValueError('Invalid download counter')
            assets.append({
                'id': int(asset['id']), 'name': asset['name'],
                'category': category(asset['name']), 'downloads': count,
            })
        releases.append({
            'id': release_id, 'version': release['tag_name'],
            'published_at': release['published_at'], 'prerelease': release['prerelease'],
            'assets': sorted(assets, key=lambda asset: asset['name']),
        })
    releases.sort(key=lambda release: (release['published_at'] or '', release['id']), reverse=True)
    return {'schema': 1, 'repository': repository, 'sampled_at': sampled_at, 'releases': releases}


def flat_rows(snapshot):
    for release in snapshot['releases']:
        for asset in release['assets']:
            yield [snapshot['sampled_at'], release['version'], release['id'], asset['id'],
                   asset['name'], asset['category'], asset['downloads']]


def csv_text(snapshots):
    text = io.StringIO(newline='')
    writer = csv.writer(text, lineterminator='\n')
    writer.writerow(['sampled_at_utc', 'version', 'release_id', 'asset_id', 'file', 'category', 'downloads'])
    for snapshot in snapshots:
        writer.writerows(flat_rows(snapshot))
    return text.getvalue()


def md(value):
    return str(value).replace('\\', '\\\\').replace('|', '\\|').replace('\n', ' ').replace('\r', ' ').replace('`', "'").replace('<', '&lt;').replace('>', '&gt;')


def render(snapshot):
    lines = ['# Download statistics', '', f"Last collected: **{snapshot['sampled_at']}** (UTC).", '',
             '**Downloads, not installations or unique users.** Re-downloads, updates, automated clients and our own verification downloads are included. USB/offline transfers are not counted. Add-On and helper/setup downloads are shown separately; do not add them together to estimate users.', '',
             'Collected daily by GitHub Actions from GitHub’s aggregate release counters. No tracking was added to the apps, and no personal download information is collected by this script.', '',
             '## By version', '', '| Version | Add-On downloads | Helper/setup downloads |',
             '| --- | ---: | ---: |']
    for release in snapshot['releases']:
        totals = {kind: sum(asset['downloads'] for asset in release['assets'] if asset['category'] == kind)
                  for kind in ['add-on', 'helper/setup']}
        lines.append(f"| {md(release['version'])} | {totals['add-on']} | {totals['helper/setup']} |")
    lines += ['', '## By file', '', '| Version | File | Category | Downloads |', '| --- | --- | --- | ---: |']
    for release in snapshot['releases']:
        for asset in release['assets']:
            lines.append(f"| {md(release['version'])} | {md(asset['name'])} | {asset['category']} | {asset['downloads']} |")
    lines += ['', '## History and interpretation', '',
              '- [Current counters as CSV](downloads.csv) · [Current snapshot as JSON](latest.json).',
              '- [Daily snapshots](history/) · [Full daily history as CSV](history.csv). One snapshot per UTC day; another run on the same day replaces that day’s snapshot.',
              '- Collection begins with the first saved snapshot. Its counters already include downloads made before collection started. Historical daily downloads before that point cannot be reconstructed.',
              '- For the same asset ID, a difference between snapshots is the counter change between observations, not a unique-user or installation count.',
              '- Deleted/replaced assets can reset or disappear from current counters. Saved older snapshots retain their earlier observations; compare asset IDs before calculating differences.',
              '- Checksums and other support files are listed for transparency but excluded from the version summary. Source-code ZIP/TAR downloads are not release assets and are not included.',
              '- The job reads metadata only; collecting these statistics does not download the packages or increase their counters.',
              '- Scheduled runs can be delayed or disabled by GitHub. Check the collection timestamp and the repository’s Actions tab.',
              '', '[GitHub release API documentation](https://docs.github.com/en/rest/releases/releases#list-releases)', '']
    return '\n'.join(lines)


def atomic_write(path, text):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(text, encoding='utf-8')
    temporary.replace(path)


def save(snapshot, directory):
    history = directory / 'history'
    history.mkdir(parents=True, exist_ok=True)
    content = json.dumps(snapshot, indent=2, ensure_ascii=False, allow_nan=False) + '\n'
    atomic_write(history / (snapshot['sampled_at'][:10] + '.json'), content)
    atomic_write(directory / 'latest.json', content)
    atomic_write(directory / 'downloads.csv', csv_text([snapshot]))
    snapshots = [json.loads(file.read_text(encoding='utf-8')) for file in sorted(history.glob('*.json'))]
    atomic_write(directory / 'history.csv', csv_text(snapshots))
    atomic_write(directory / 'README.md', render(snapshot))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', default=os.environ.get('GITHUB_REPOSITORY'))
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'stats')
    args = parser.parse_args()
    if not args.repo:
        parser.error('--repo or GITHUB_REPOSITORY is required')
    snapshot = collect(args.repo)
    save(snapshot, args.output)
    print(f"Recorded {len(snapshot['releases'])} published releases for {snapshot['repository']}.")


if __name__ == '__main__':
    main()
