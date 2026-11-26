import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('downloads', Path(__file__).with_name('collect-downloads.py'))
downloads = importlib.util.module_from_spec(spec)
spec.loader.exec_module(downloads)


class DownloadTests(unittest.TestCase):
    def snapshot(self, timestamp='2026-11-26T06:23:00Z', count=7):
        calls = []
        def api(endpoint):
            calls.append(endpoint)
            if '/assets?' in endpoint:
                return [{'id': 10, 'name': 'Song.lunaaddon', 'download_count': count},
                        {'id': 11, 'name': 'Helper.zip', 'download_count': 4},
                        {'id': 12, 'name': 'SHA256SUMS.txt', 'download_count': 20}]
            return [{'id': 1, 'draft': False, 'prerelease': True, 'tag_name': 'v1', 'published_at': '2026-11-25T00:00:00Z'},
                    {'id': 2, 'draft': True}]
        snapshot = downloads.collect('owner/repo', api, timestamp)
        self.assertEqual(len(calls), 2)
        return snapshot

    def test_versions_keep_addon_and_helper_counts_separate_and_exclude_checksums(self):
        snapshot = self.snapshot()
        self.assertEqual(len(snapshot['releases']), 1)
        text = downloads.render(snapshot)
        self.assertIn('| v1 | 7 | 4 |', text)
        self.assertIn('checksum (excluded)', text)
        self.assertIn('not installations', text)

    def test_same_day_replaces_snapshot_but_next_day_keeps_history_and_asset_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            downloads.save(self.snapshot(), root)
            downloads.save(self.snapshot('2026-11-26T12:00:00Z', 8), root)
            self.assertEqual(len(list((root / 'history').glob('*.json'))), 1)
            downloads.save(self.snapshot('2026-11-27T06:23:00Z', 9), root)
            self.assertEqual(len(list((root / 'history').glob('*.json'))), 2)
            latest = json.loads((root / 'latest.json').read_text())
            asset = next(a for a in latest['releases'][0]['assets'] if a['id'] == 10)
            self.assertEqual(asset['downloads'], 9)
            self.assertEqual(len((root / 'history.csv').read_text().splitlines()), 7)

    def test_markdown_names_are_escaped(self):
        self.assertEqual(downloads.md('A|B\n<img>'), 'A\\|B &lt;img&gt;')
        with self.assertRaises(ValueError):
            downloads.collect('../bad/repo', lambda _: [])


if __name__ == '__main__':
    unittest.main()
