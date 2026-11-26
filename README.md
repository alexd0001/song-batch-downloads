# Song Batch Beta

**One live session. Every song ready for its next step.**

By **trinidub** · alex@trinidub.de · macOS only

Turn LUNA markers into individual stereo exports, named song versions or separate song sessions. Preview selected songs, save an individual output level for each one and prepare a whole set in one batch.

## Export with individual song levels

Select the marker ranges to export. Set each song’s saved **Song level** from −24 to +12 dB; the same additional Main trim is applied during preview and native rendering, then its baseline is restored. This is manual gain adjustment, not loudness normalization or limiting. Positive gain can clip. Ordinary channel-mixer adjustments affect the actual session mix.

Export the Main stereo mix through LUNA, followed by FFmpeg conversion to **WAV (16/24-bit or 32-bit float)** or **MP3 (128/192/256/320 kbit/s)**, at **44.1 kHz**. Filenames can use marker names, custom text and numbering. Native renders are retained in a LUNA Originals subfolder.

## Every song starts at 0:00

Choose markers in **Song projects**, then create named **LUNA versions within the current session** or **separate sessions per song**. Each marker range is cropped and shifted to 0:00, including supported playlists, automation and clip gain. Results use the marker names. The saved Song level is carried to the new start marker for use in Song Batch.

Choose **Keep original mix** to retain the adjustment only for Song Batch preview/export, or **Apply Song level permanently to Main trim** to save it into each new project’s native mix. Permanent mode resets that project’s Song level to **0 dB**, avoiding a second adjustment. The Main fader is unchanged.

A **Song Batch – Full session** checkpoint is saved first, then reopened and verified after processing. Independent backups remain recommended.

[Read the full feature description](PRODUCT-DESCRIPTION.md).

## Download and install

Get both files from the [latest release](https://github.com/alexd0001/song-batch-downloads/releases/latest):

1. **Song-Batch-0.6.5.lunaaddon**
2. **Song-Batch-macOS-Helper-0.6.5.zip**

Requirements: **macOS, LUNA 3.1.2+, Node.js 22+, FFmpeg and FFprobe**. Install these separately; they are not bundled. No developer checkout or npm install is needed.

Extract the helper ZIP onto your Mac’s internal drive. Open **Song Batch Helper**, double-click **Start Song Batch.command**, and keep its Terminal window open. Import the .lunaaddon file into LUNA and open Song Batch from Add Ons. Open a session to work with markers. The dashboard is also available at http://localhost:8791/.

This portable helper does not register a login service. Do not close its Terminal or change the session, markers or mix while an export or project-creation job is running. See the helper README for operating instructions. If port 8791 is already in use, use your existing Song Batch helper rather than starting a second one.

## Current beta limits

Song-project creation requires constant tempo, time signature and key. Frozen channels and lyrics, chord or section tracks are not supported. Source media remains untrimmed, so separate sessions may use substantial disk space. Song sessions keep their original sample rate; audio exports use 44.1 kHz. Main automation must be compatible and Main trim must not be automated for per-song level adjustment.

Sessions, audio, credentials and plug-in authorizations are not included. The release passed 38 automated tests. Earlier isolated LUNA checks covered rendering, level restoration, song-project creation and checkpoint restoration. The new level-mode UI was checked for both project types, and read-only preflight was verified against LUNA 3.1.2.4699. Permanent level persistence in newly saved native versions/sessions still needs a dedicated end-to-end check; the open user session was not used for this test. This package has not been fully tested on a second Mac.

## License and source

This repository distributes beta downloads and documentation. Development source remains private. See [LICENSE](LICENSE) for limited evaluation permission and [third-party notices](THIRD-PARTY-NOTICES.md) for SDK terms. Delivered JavaScript remains inspectable. Independent utility; not an official Universal Audio product.

## Next steps

[Planned enhancements](NEXT-STEPS.md): song boundaries and tails, loudness analysis, project review, export presets, multiple formats and batch reports. These are not included in the current beta.
