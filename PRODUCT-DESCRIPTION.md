# Song Batch Beta

**One live session. Every song ready for its next step.**

A great live recording deserves more than one long file. Song Batch turns LUNA’s session markers into a practical song-by-song workflow: listen, adjust individual output levels, export stereo mixes and create dedicated song versions or separate sessions.

## Selected songs. Individual levels. One batch.

Choose the marker ranges you want to export and preview each song directly in LUNA. Use the seekable playback controls to check a passage, or open the channel mixer beneath the song to monitor and adjust your session’s buses and Main output.

Give each song its own saved **Song level**, from **−24 to +12 dB**. The same additional Main output trim is used for preview and native rendering, so your chosen adjustment follows the song into its export. The baseline trim is restored afterwards; the Main fader and its automation stay unchanged. This is a manual gain adjustment, not automatic loudness normalization or limiting. Positive gain can cause clipping.

Song Batch renders the **Main stereo mix through LUNA**, then prepares your chosen delivery format with FFmpeg:

- **WAV:** 16-bit, 24-bit or 32-bit float.
- **MP3:** 128, 192, 256 or 320 kbit/s.
- **44.1 kHz** for all audio exports.
- Marker-based filenames with optional prefix, suffix, custom text and numbering.
- Native render files retained in a **LUNA Originals** subfolder.

Preview can include Main and multiple buses. Audio export uses the Main stereo mix. Ordinary channel-mixer adjustments affect the actual session mix; the dedicated Song level is saved individually for each marker.

## From a full live set to individual song projects

The recording is one session. Your next mix may be just one song.

Select the markers you want in **Song projects**, then choose how to organize the results:

- **LUNA versions:** create a named song version inside the current session, keeping your work together.
- **Separate sessions:** create an individual session per song, with an optional destination folder.

Each selected marker starts a song and the next marker ends it. Song Batch retains that song’s material, crops it to the marker range and moves it to **0:00**. Supported playlists, channel, bus, Main and plug-in automation, plus clip-relative gain envelopes, are processed with the song. The original marker name becomes the version or session name. The saved Song level is carried over to the new start marker for use in Song Batch.

Before processing, Song Batch saves a **Song Batch – Full session** checkpoint. Once the selected songs are created, it reopens and verifies that checkpoint. You can move from managing a long live set to working on a focused song, with the full-session checkpoint available for recovery.

## Current beta scope

Song-project creation currently requires constant tempo, time signature and key. Frozen channels and lyrics, chord or section tracks are not supported. Source media files remain untrimmed, so separate sessions may require substantial disk space. Song sessions keep the original session sample rate; audio exports use 44.1 kHz.

Keep independent backups and leave the session, markers and mix unchanged while a batch is running. Per-song level adjustment requires compatible Main automation and an unautomated Main trim. Song Batch validates these conditions before applying the adjustment.

**macOS only · LUNA 3.1.2+ · Node.js 22+ · FFmpeg and FFprobe required separately**

An independent LUNA Add On by **trinidub** · **alex@trinidub.de**.

## Short listing description

Turn a LUNA live session into individual songs. Batch-export selected marker ranges as stereo WAV or MP3 at 44.1 kHz, with saved per-song level adjustments and customizable filenames. Create marker-named LUNA versions or separate song sessions, with each song’s material starting at 0:00. Song Batch saves a full-session checkpoint before project creation and reopens it afterwards. macOS beta by trinidub.
