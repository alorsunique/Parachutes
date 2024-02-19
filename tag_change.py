# This script should be able to change any tag within the MP3 file
# This is set to change the album artist as of now to merge duplicates
# with slight variation

import os
from pathlib import Path

from mutagen.easyid3 import EasyID3

script_path = Path(__file__).resolve()
project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(str(resources_text.readline()).replace('"', ''))

input_dir = resources_dir / "Input"

artist = input(f"Input Artist: ")

for file in input_dir.iterdir():
    print(f"File: {file.name}")

    file_handle = os.path.splitext(file.name)[1]

    source_file = file

    audio = EasyID3(source_file)

    audio["artist"] = artist
    audio["albumartist"] = artist

    audio.save()
