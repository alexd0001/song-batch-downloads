# Song Batch

**Turn one long LUNA recording into individual songs, ready to listen to, export or mix.**

Song Batch uses your session markers to organize a live set, rehearsal or long recording into songs. Choose the songs you need, preview them inside LUNA and set an individual output level for each one. Then export stereo files, create song versions inside the original session, or create separate LUNA sessions for individual songs.

## 1. Choose your songs using markers

Each marker starts a song. The next marker in the session marks its end. Select which songs to process; you do not have to export or create projects for the whole set.

For example, a song starting at 12:30 and ending at the next marker at 17:45 has a duration of 5:15. Skipping another song does not extend this range: the end is always the next marker, even when that marker is not selected. Optionally include the final marker through the end of the session, or use it only as an end boundary.

Your marker names become the basis for song names, exported filenames and project names.

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

Automated tests cover the project-level choices, including prevention of double gain and rollback on a storage failure. The interface was checked for both project types; read-only preflight was verified on LUNA 3.1.2.4699. Permanent level persistence in newly saved native versions or sessions still needs a dedicated end-to-end check. The packaged release has not been fully tested on a second Mac.

## Planned enhancements

[Next steps](NEXT-STEPS.md) include song-boundary controls and tails, loudness analysis, a project review screen, export presets, multiple output formats and batch reports. These are planned features, not part of the current release.

An independent LUNA Add On by **trinidub** · **alex@trinidub.de**.

## Short description for Discover

Turn a long LUNA recording into individual songs. Preview selected marker ranges, adjust each song’s level and batch-export stereo WAV or MP3 files. Create named session versions within the original session package, or independent LUNA sessions for individual songs, each starting at 0:00. A full-session checkpoint is saved before project creation and reopened afterwards. macOS only; companion helper required.
