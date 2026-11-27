# Download statistics

Last collected: **2026-11-27T12:06:26Z** (UTC).

**Downloads, not installations or unique users.** Re-downloads, updates, automated clients and our own verification downloads are included. USB/offline transfers are not counted. Add-On and helper/setup downloads are shown separately; do not add them together to estimate users.

Collected daily by GitHub Actions from GitHub’s aggregate release counters. No tracking was added to the apps, and no personal download information is collected by this script.

## By version

| Version | Add-On downloads | Helper/setup downloads |
| --- | ---: | ---: |
| v0.6.6 | 0 | 0 |
| v0.6.5 | 8843 | 2 |
| v0.6.4 | 308 | 2 |

## By file

| Version | File | Category | Downloads |
| --- | --- | --- | ---: |
| v0.6.6 | SHA256SUMS.txt | checksum (excluded) | 0 |
| v0.6.6 | Song-Batch-0.6.6.lunaaddon | add-on | 0 |
| v0.6.6 | Song-Batch-macOS-Helper-0.6.6.zip | helper/setup | 0 |
| v0.6.5 | SHA256SUMS.txt | checksum (excluded) | 2 |
| v0.6.5 | Song-Batch-0.6.5.lunaaddon | add-on | 8843 |
| v0.6.5 | Song-Batch-macOS-Helper-0.6.5.zip | helper/setup | 2 |
| v0.6.4 | SHA256SUMS.txt | checksum (excluded) | 2 |
| v0.6.4 | Song-Batch-0.6.4.lunaaddon | add-on | 308 |
| v0.6.4 | Song-Batch-macOS-Helper-0.6.4.zip | helper/setup | 2 |

## History and interpretation

- [Current counters as CSV](downloads.csv) · [Current snapshot as JSON](latest.json).
- [Daily snapshots](history/) · [Full daily history as CSV](history.csv). One snapshot per UTC day; another run on the same day replaces that day’s snapshot.
- Collection begins with the first saved snapshot. Its counters already include downloads made before collection started. Historical daily downloads before that point cannot be reconstructed.
- For the same asset ID, a difference between snapshots is the counter change between observations, not a unique-user or installation count.
- Deleted/replaced assets can reset or disappear from current counters. Saved older snapshots retain their earlier observations; compare asset IDs before calculating differences.
- Checksums and other support files are listed for transparency but excluded from the version summary. Source-code ZIP/TAR downloads are not release assets and are not included.
- The job reads metadata only; collecting these statistics does not download the packages or increase their counters.
- Scheduled runs can be delayed or disabled by GitHub. Check the collection timestamp and the repository’s Actions tab.

[GitHub release API documentation](https://docs.github.com/en/rest/releases/releases#list-releases)
