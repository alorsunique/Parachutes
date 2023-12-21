from pathlib import Path

from mutagen.flac import FLAC
from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3
from pydub import AudioSegment
from pydub.utils import mediainfo

resources_dir_text = "Resources_Path.txt"

entry_list = []
with open(resources_dir_text, 'r') as reader:
    entry_list.append(reader.read())
    reader.close()

resources_dir = Path(entry_list[0])

input_dir = resources_dir / "Input"
flac_convert_workspace_dir = resources_dir / "FLAC Workspace"

for file in input_dir.iterdir():

    audio = AudioSegment.from_file(file, "flac")
    audio_info = mediainfo(file)
    output_path = flac_convert_workspace_dir / f"{file.stem}.mp3"
    audio.export(output_path, format="mp3", bitrate="320k", tags=audio_info["TAG"])

    mutagen_flac_audio = FLAC(file)
    album_cover_data = mutagen_flac_audio.pictures

    if album_cover_data:
        album_cover_bytes = album_cover_data[0].data

        mutagen_MP3_audio = MP3(output_path, ID3=ID3)
        mutagen_MP3_audio.tags.delall('APIC')  # Delete existing album art
        mutagen_MP3_audio.tags.add(APIC(mime='image/jpeg', type=3, desc=u'Cover', data=album_cover_bytes))
        mutagen_MP3_audio.save()
    else:
        print('No album art found in the FLAC file.')
