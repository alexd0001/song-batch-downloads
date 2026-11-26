# Song Batch — Next steps

Ideas for future versions, not features shipped in the current beta. Implementation order and LUNA API support still need validation.

## Song boundaries and tails

Adjust each song's start and end independently of its session markers. Add optional pre-roll, an end tail and short fades. Preview the exact resulting range and make overlaps explicit before export or project creation.

## Loudness analysis per song

Measure integrated LUFS and true peak, compare the selected songs and suggest individual Song-level adjustments. Apply suggestions only after the user's choice. Define the measurement point and headroom policy clearly; manual gain adjustment alone is not loudness normalization or limiting.

## Review and open song projects

Show a preflight summary with each selected name, range, duration, destination, level mode and naming conflict. Offer direct opening of a completed LUNA version or separate session after the full session has been restored. Preserve recovery and unsaved-work safeguards when switching projects.

## Export presets

Save named presets such as Listening MP3 and Master WAV, with format, bit depth or bitrate, naming rules and destination preferences. Keep the current 44.1 kHz export policy explicit.

## Multiple formats in one batch

Create WAV and MP3 for each selected song from a shared native render where possible. Track conversion progress and failures separately, preserve originals and avoid overwriting existing output.

## Batch report and targeted retry

Summarize completed files, project versions, ranges, level adjustments and failures. Save a report and retry selected failed entries after checking that the source session, markers and settings still match.

## Implemented in 0.6.5 Beta

Song-project creation can retain the original native mix with a saved Song Batch adjustment, or apply the selected Song level permanently to the new project's Main trim. Permanent mode clears the new marker adjustment to 0 dB, avoiding double gain. This choice is available for both LUNA versions and separate song sessions.
