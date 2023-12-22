# Parachutes
---
Handle certain task for audio files. The following are

1. Rename MP3 file
    - If the MP3 file has metadata on song title and song number, it can be renamed to follow the format `[Number]. [Song Title]` 
2. Sort MP3 file
    - Same with rename, if the MP3 file has the metadata, it will be sorted accordingly. Artist and album name data will be checked. If the MP3 file has those, it will be moved to a folder with the following structure `[Artist]\[Album]`
3. Add custom album art
     - All MP3 files in the input folder will have their album art changed to a selected custom image. Only requires a path to the image file
4. Convert FLAC to 320kbps MP3
     - Will create an MP3 file for a given FLAC file with a bitrate of 320kbps. The generated MP3 file can then be used in the previous three options in order to rename the file, sort it by album, or change the album art
