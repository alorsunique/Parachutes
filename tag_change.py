# This script should be able to change any tag within the MP3 file
# This is set to change the album artist as of now to merge duplicates
# with slight variation

import os
from pathlib import Path

from mutagen.easyid3 import EasyID3

resources_dir_text = "Resources_Path.txt"

entry_list = []
with open(resources_dir_text, 'r') as reader:
    entry_list.append(reader.read())
    reader.close()

resources_dir = Path(entry_list[0])
input_dir = resources_dir / "Input"

artist = input(f"Input Artist: ")

for file in input_dir.iterdir():
    print(f"File: {file.name}")

    file_handle = os.path.splitext(file.name)[1]

    src_file = file

    audio = EasyID3(src_file)

    audio["artist"] = artist
    audio["albumartist"] = artist

    audio.save()
