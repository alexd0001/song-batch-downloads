# Song Batch

**A faster rough-mix workflow for an entire concert or live act, built around song markers.**

Work through a complete live recording in one place: identify the songs, preview the mix, adjust each song’s output level and batch-export stereo rough mixes. Use your own markers or let **Detect songs** analyze the Main mix and propose song boundaries for review.

Once you have listened and decided which songs deserve further work, select **one, several or all songs**. Keep them as named session versions in the original LUNA package, or split the selection into independent song sessions, each starting at **0:00**. You do not have to split the whole concert just to develop a few chosen songs.

## A practical live-recording workflow

1. Open the full concert or live-act session.
2. Use existing markers, or analyze the Main mix to propose missing song markers.
3. Review the boundaries, preview songs and adjust their individual output levels.
4. Export the selected stereo rough mixes in a batch for listening or review.
5. Choose which songs to develop further and create their session versions or separate sessions.

## 1. Choose your songs using markers

Each marker starts a song. The next marker in the session marks its end. Select which songs to process; you do not have to export or create projects for the whole set.

For example, a song starting at 12:30 and ending at the next marker at 17:45 has a duration of 5:15. Skipping another song does not extend this range: the end is always the next marker, even when that marker is not selected. Optionally include the final marker through the end of the session, or use it only as an end boundary.

Your marker names become the basis for song names, exported filenames and project names.

### No markers yet? Detect songs and review the results

**Detect songs** renders the current Main stereo mix to a temporary analysis file and looks for pauses below your chosen level threshold. Set the silence threshold, minimum pause length and minimum song length. Analysis does not create or delete markers by itself.

Review the proposed song names and start positions, edit them if needed, and use **Preview / pause** to check a boundary. Then choose how to handle existing markers:

- **Keep existing markers · add missing boundaries** (default): existing marker identities, names, colors, comments and positions are preserved. Suggestions within one second of an existing marker are skipped. Existing boundaries may still subdivide a detected song.
- **Replace existing markers with reviewed boundaries:** create a new marker layout from the reviewed proposal, including a final **End** marker. Replacing an existing layout requires typing **REPLACE**. Original markers and their saved song levels are backed up before the change.

Press **Create reviewed markers** to apply the result. The successful edit is grouped into one LUNA undo transaction. The app checks for marker, tempo or material changes since analysis and refuses stale proposals. Marker backups are kept in **marker-backups** under the helper runtime directory (in the portable package: **Song Batch Helper/runtime/marker-backups**). The final End marker is treated as a boundary: after creation, Song Batch switches off “Include the last marker through the session end” to avoid exporting an extra tail as a song. Temporary analysis audio is removed after the operation.

This is pause/level detection, not musical identification or title recognition. Initial names are **Song 01**, **Song 02**, and so on. Applause, quiet musical sections and seamless transitions can produce missed or incorrect boundaries. Always review the proposal, and leave the session unchanged while analysis is running.

## 2. Preview and adjust individual song levels

Play or pause a song and use its seek slider to check a particular passage. The channel mixer opens beneath the selected song, with buses and Main shown by default. It provides volume, pan, mute, solo, live meters and a resettable clip indicator. You can select Main and multiple buses for preview; stereo exports use the Main mix.

The dedicated **Song level** control saves an individual adjustment for each song, from **−24 to +12 dB**. The same adjustment is used for preview and audio export. It is applied through additional Main trim, with the original trim restored afterwards. The Main fader and its automation are unchanged by this adjustment.

Song level is manual gain adjustment, not automatic loudness normalization or limiting. Positive gain may clip. Ordinary channel-mixer controls change the actual session mix and are not saved separately per song.

## 3. Batch-export stereo files

Export one stereo file for each selected marker range, using LUNA’s native render process followed by FFmpeg conversion.

- **WAV:** 16-bit, 24-bit or 32-bit float.
- **MP3:** 128, 192, 256 or 320 kbit/s.
- **Sample rate:** 44.1 kHz for all audio exports.
- **Filenames:** use marker names, optional text before or after the name, custom text and numbering.
- **Original renders:** retained in a **LUNA Originals** subfolder.

Use this when you want listening copies or stereo mix files. To continue editing each song as a LUNA project, use **Song projects** instead.

## 4. Create song projects: versions or separate sessions

Both choices create an editable song project from the selected marker range. The material outside that song range is removed from the resulting timeline, and the retained material is shifted so that the song begins at **0:00**. Supported playlists, automation and clip-gain envelopes are processed with the song. Source media files on disk remain untrimmed.

### Option A — LUNA session versions: keep the songs in one session package

Choose **LUNA versions · in this session** to create a named session version for each selected song inside the existing LUNA session package.

For example, a session called **Friday Live** with markers **Opening Song**, **Slow Jam** and **Finale** gains three song versions with those names. Opening the **Slow Jam** version gives you that song’s retained material starting at 0:00. The full recording remains available through the saved full-session checkpoint.

These are **versions of the entire session**, not V1/V2 track takes or alternate playlists on an individual channel. They do not create a separate project package for each song. Choose this option when you want to keep the full set and its individual song projects together, and switch between them through LUNA’s session Versions controls.

### Option B — Separate sessions: give each song its own project package

Choose **Separate sessions · one per song** to create an independent LUNA session package for each selected song. You can choose a destination folder. Each result is named from its marker and contains that song’s timeline starting at 0:00.

In the same example, **Opening Song**, **Slow Jam** and **Finale** become separate LUNA sessions that you open individually. Choose this option when you want to organize and continue working on each song as its own project.

Separate sessions may take substantial disk space because source media is not shortened to the song’s duration. When moving a song session to another computer, check that its required media, plug-ins and authorizations are available; creating a separate session is not a guarantee of a self-contained transfer package.

| Your aim | Choose |
| --- | --- |
| Listening copies or finished stereo mix files | Audio export |
| Individual song projects kept within the existing session package | LUNA session versions |
| One independent LUNA project package per song | Separate sessions |

### What happens to the full recording?

Before project creation, Song Batch saves a **Song Batch – Full session** checkpoint. After processing, it reopens and verifies that checkpoint, returning you to the full recording. The new song versions or sessions remain available to open afterwards.

Only selected songs are created. Existing version-name conflicts are rejected rather than silently overwritten. If creation is cancelled, Song Batch finishes the current song before returning to the full session. Recovery information is retained if the process is interrupted. Keep independent backups and leave the session unchanged while a batch is running.

## 5. Choose the level used in new projects

The **Level in new projects** selector applies to both session versions and separate sessions:

- **Keep original mix · retain Song Batch adjustment:** the new project keeps the original native Main trim. Its saved Song level is carried to the new start marker and is applied when you preview or export through Song Batch. Ordinary LUNA playback keeps the original mix level.
- **Apply Song level permanently to Main trim:** the song’s adjustment is added to the new project’s native Main trim before saving. It then affects ordinary LUNA playback too. The new marker’s Song level is reset to **0 dB** to avoid applying the same adjustment twice. The Main fader is unchanged.

Example: with an original Main trim of 0 dB and a Song level of −3 dB, the first option keeps Main trim at 0 dB and stores −3 dB in Song Batch. The second saves Main trim at −3 dB and stores 0 dB in Song Batch. The full-session checkpoint restores the original session’s mix and stored adjustments afterwards.

## 6. Installation and requirements

**macOS only · LUNA 3.1.2+ · Node.js 22+ · FFmpeg and FFprobe**

Download both the **.lunaaddon** and the **macOS Helper ZIP** from the [latest release](https://github.com/alexd0001/song-batch-downloads/releases/latest). Install the required external tools separately. Extract the helper onto your Mac’s internal drive, run **Start Song Batch.command** and keep its Terminal window open while using Song Batch. Import the .lunaaddon into LUNA and open the Add On with a session loaded.

The helper is required; importing the Add On alone does not start it. No development checkout or npm install is needed for the prepared download. This portable helper does not install a login service. Do not close it during an export or project-creation job.

## Current limitations and verification

Song-project creation requires constant tempo, time signature and key. Frozen channels and lyrics, chord or section tracks are not supported. New song projects keep the session’s original sample rate; audio exports use 44.1 kHz.

Nonzero song-level adjustments require Main automation in Read or Off, no Main-trim automation and sufficient available trim range. Unsupported settings are rejected before applying the adjustment.

Automated tests cover song detection, existing-marker preservation, stale-proposal rejection, replacement confirmation and recovery after marker-write failures, as well as the project-level choices. A generated audio fixture verifies the FFmpeg pause analysis. Native end-to-end detection verification could not complete because LUNA failed to load the isolated test session; no successful native detection test is claimed. The interface was checked for both project types; read-only preflight was verified on LUNA 3.1.2.4699. Permanent level persistence in newly saved native versions or sessions still needs a dedicated end-to-end check. The packaged release has not been fully tested on a second Mac.

## Planned enhancements

[Next steps](NEXT-STEPS.md) include song-boundary controls and tails, loudness analysis, a project review screen, export presets, multiple output formats and batch reports. These are planned features, not part of the current release.

An independent LUNA Add On by **trinidub** · **alex@trinidub.de**.

## Short description for Discover

Build rough mixes from a complete concert or live recording using song markers. Use existing markers or detect and review suggested boundaries, preview songs, adjust their levels and batch-export stereo WAV or MP3 files. Create named session versions within the original session package, or independent LUNA sessions for individual songs, each starting at 0:00. A full-session checkpoint is saved before project creation and reopened afterwards. macOS only; companion helper required.
