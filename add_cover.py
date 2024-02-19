import os
from pathlib import Path

from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3

script_path = Path(__file__).resolve()
project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(str(resources_text.readline()).replace('"', ''))

input_dir = resources_dir / "Input"
image_path = str(input(f"Image Path: "))

for file in input_dir.iterdir():
    with open(image_path, 'rb') as cover_image:
        album_cover_bytes = cover_image.read()

    mutagen_audio = MP3(file, ID3=ID3)
    mutagen_audio.tags.delall('APIC')  # Delete existing album art
    mutagen_audio.tags.add(APIC(mime='image/jpeg', type=3, desc=u'Cover', data=album_cover_bytes))
    mutagen_audio.save()
