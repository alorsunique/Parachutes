# This script should be able to change any tag within the MP3 file
# This is set to change the album artist as of now to merge duplicates
# with slight variation

import os
from pathlib import Path
from mutagen.easyid3 import EasyID3

project_dir = Path.cwd()
current_dir = project_dir
current_dir = current_dir.parent.parent

resources_dir = current_dir / "PycharmProjects Resources" / "Parachutes Resources"

if not os.path.exists(resources_dir):
    os.mkdir(resources_dir)

input_dir = resources_dir / "Input"

if not input_dir.exists():
    os.mkdir(input_dir)

artist = input(f"Input Artist: ")

for file in input_dir.iterdir():
    print(f"File: {file.name}")

    file_handle = os.path.splitext(file.name)[1]

    src_file = file

    audio = EasyID3(src_file)

    audio["artist"] = artist
    audio["albumartist"] = artist

    audio.save()
