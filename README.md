# Song Batch

**Fast rough mixes for a full concert or live act, built around song markers.**

By **trinidub** · alex@trinidub.de · macOS only

Turn LUNA markers into individual stereo exports, named song versions or separate song sessions. Preview selected songs, save an individual output level for each one and prepare a whole set in one batch.

## Detect songs and create markers

Use existing markers or choose **Detect songs** to analyze a reference audio track directly, or render the full Main mix for pause detection. Set the silence threshold, minimum pause and minimum song length, then review and preview the proposed names and start positions.



### Quick detection — skip the Main render

**Quick detection · audio track** is the default analysis method. Choose a full-length reference audio track, ideally a stereo recording containing the entire concert, then press **Detect songs**. Song Batch reads the visible audio pieces directly from their source files, including source offsets, cuts and timeline gaps. It does not bounce the Main mix or run channel/bus plug-ins. Track faders, clip gain and fades are not modeled, so the selected reference waveform may differ from the audible Main mix.

The graphical review, boundary editing and marker Keep/Replace options remain the same. Audition still plays the current Main mix in LUNA. A sparse instrument track can suggest false pauses; choose a suitable recording and review the result. If source audio is unavailable or a clip cannot be mapped directly, choose **Full mix detection · render Main**. Quick detection never silently starts a full render.

### Review boundaries on the waveform

The **Main mix overview** displays real peak data from the selected reference track or analyzed Main render. Gold lines mark proposed song starts and the final End; gray dashed lines show existing markers. Drag a proposed boundary to adjust it, or enter its time in seconds. Adjacent starts define the song ranges, and boundaries cannot cross.

Zoom from **1× to 16×**, scroll horizontally and click the waveform to audition that position in LUNA. Play/pause, Stop and the moving cursor help check transitions before creating markers. Arrow keys move the focused boundary by one second; Shift uses ten seconds and Alt uses 0.1 seconds. This is a coarse peak overview rather than a sample-level editor. Existing markers remain unchanged until you apply the reviewed proposal.

**Keep existing markers** adds missing boundaries while preserving your layout. **Replace existing markers** requires typing **REPLACE** and backs up the original layout first. Markers are only written after you press **Create reviewed markers**. Analysis alone leaves them unchanged. This is pause/level detection, not song-title recognition; applause, quiet passages and seamless transitions need manual checking.

Work through the full concert or live act, adjust per-song levels and export selected stereo rough mixes. After listening, choose one, several or all songs to develop further. Split only that selection into session versions or independent sessions starting at 0:00; the full concert does not have to become separate projects.

## Export with individual song levels

Select the marker ranges to export. Set each song’s saved **Song level** from −24 to +12 dB; the same additional Main trim is applied during preview and native rendering, then its baseline is restored. This is manual gain adjustment, not loudness normalization or limiting. Positive gain can clip. Ordinary channel-mixer adjustments affect the actual session mix.

Export the Main stereo mix through LUNA, followed by FFmpeg conversion to **WAV (16/24-bit or 32-bit float)** or **MP3 (128/192/256/320 kbit/s)**, at **44.1 kHz**. Filenames can use marker names, custom text and numbering. Native renders are retained in a LUNA Originals subfolder.

## Song projects: versions or independent sessions

Want to continue mixing each song instead of exporting audio only? Select its marker in **Song projects**. Both project modes retain the selected marker range, shift the song to **0:00** and use its marker name. Supported playlists, automation and clip gain are processed with it.

### LUNA session versions — all songs in the same session package

Choose **LUNA versions · in this session** to save each song as a named version of the entire session inside the original LUNA session package. Open a song through LUNA’s session Versions controls to work on that song at 0:00.

For example, your **Friday Live** session can hold a full-session checkpoint plus song versions called **Opening Song**, **Slow Jam** and **Finale**. They stay together in one session package. These are session versions, not V1/V2 takes on individual tracks.

### Separate sessions — one project package per song

Choose **Separate sessions · one per song** to create independent LUNA session packages, with an optional destination folder. In the same example, **Opening Song**, **Slow Jam** and **Finale** become separate sessions that you open and organize individually.

Source media remains untrimmed, so these sessions can take substantial disk space. Check required media and plug-ins before moving them to another computer.

| What you want | Use |
| --- | --- |
| One stereo listening or mix file per song | Audio export |
| Song projects kept in the original session package | LUNA session versions |
| Independently organized song project packages | Separate sessions |

### Full-session checkpoint and song levels

Before project creation, Song Batch saves a **Song Batch – Full session** checkpoint. It reopens and verifies that checkpoint afterwards, returning to the full recording. The created results remain available to open separately.

For either project type, **Level in new projects** offers two choices:

- **Keep original mix · retain Song Batch adjustment:** native Main trim stays unchanged; the song’s adjustment remains available for Song Batch preview and export.
- **Apply Song level permanently to Main trim:** the adjustment becomes part of the new project’s native mix, including ordinary LUNA playback. The new marker’s Song level is reset to **0 dB** to prevent double gain. The Main fader is unchanged.

The full-session checkpoint restores the original mix and saved song adjustments. Keep independent backups and leave the session unchanged during processing.

[Read the detailed user description, with an example and operating instructions](PRODUCT-DESCRIPTION.md).

## Download and install

Get both files from the [latest release](https://github.com/alexd0001/song-batch-downloads/releases/latest):

1. **Song-Batch-0.9.1.lunaaddon**
2. **Song-Batch-macOS-Helper-0.9.1.zip**

Requirements: **macOS, LUNA 3.1.2+, Node.js 22+, FFmpeg and FFprobe**. Install these separately; they are not bundled. No developer checkout or npm install is needed.

Extract the helper ZIP onto your Mac’s internal drive. Open **Song Batch Helper**, double-click **Start Song Batch.command**, and keep its Terminal window open. Import the .lunaaddon file into LUNA and open Song Batch from Add Ons. Open a session to work with markers. The dashboard is also available at http://localhost:8791/.

This portable helper does not register a login service. Do not close its Terminal or change the session, markers or mix while an export or project-creation job is running. See the helper README for operating instructions. If port 8791 is already in use, use your existing Song Batch helper rather than starting a second one.

## Current limitations

Song-project creation requires constant tempo, time signature and key. Frozen channels and lyrics, chord or section tracks are not supported. Source media remains untrimmed, so separate sessions may use substantial disk space. Song sessions keep their original sample rate; audio exports use 44.1 kHz. Main automation must be compatible and Main trim must not be automated for per-song level adjustment.

Sessions, audio, credentials and plug-in authorizations are not included.

## License and source

This repository distributes application downloads and documentation. Development source remains private. See [LICENSE](LICENSE) for limited evaluation permission and [third-party notices](THIRD-PARTY-NOTICES.md) for SDK terms. Delivered JavaScript remains inspectable. Independent utility; not an official Universal Audio product.

## Next steps

[Planned enhancements](NEXT-STEPS.md): song boundaries and tails, loudness analysis, project review, export presets, multiple formats and batch reports. These are not included in the current release.

## Download statistics

[View download counts by version and file](stats/README.md). Updated daily, with downloadable CSV data and saved daily snapshots. These are aggregate GitHub downloads, not installations or unique users; repeat downloads and verification downloads are included. No tracking is added to the apps.
