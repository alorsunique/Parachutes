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
image_path = str(input(f"Image Path: "))

for file in input_dir.iterdir():

    with open(image_path, 'rb') as cover_image:
        album_cover_bytes = cover_image.read()

    mutagen_audio = MP3(file, ID3=ID3)
    mutagen_audio.tags.delall('APIC')  # Delete existing album art
    mutagen_audio.tags.add(APIC(mime='image/jpeg', type=3, desc=u'Cover', data=album_cover_bytes))
    mutagen_audio.save()