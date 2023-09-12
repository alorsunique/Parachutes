# This script should rename the music file appropriately given that the info are in the metadata

import os
from pathlib import Path

from mutagen.easyid3 import EasyID3

project_dir = Path.cwd()
current_dir = project_dir
current_dir = project_dir.parent.parent

resources_dir = current_dir / "PycharmProjects Resources" / "Parachutes Resources"

if not os.path.exists(resources_dir):
    os.mkdir(resources_dir)

input_dir = resources_dir / "Input"


if not input_dir.exists():
    os.mkdir(input_dir)

specialChar = "\/?:*"

for file in input_dir.iterdir():
    print(f"File: {file.name}")

    file_handle = os.path.splitext(file.name)[1]

    src_file = file

    audio = EasyID3(src_file)

    track_number = str(audio['tracknumber'])
    print(f"Track Number: {track_number}")
    track_number = track_number[2:-2]

    if "/" in track_number:
        number_split = track_number.split("/")
    else:
        number_split = track_number.split(" ")

    if int(number_split[0]) < 10:
        number_string = "0" + str(int(number_split[0]))
    else:
        number_string = str(int(number_split[0]))

    title = str(audio['title'])
    title = title[2:-2]

    for character in specialChar:
        title = title.replace(character, "")

    title_string = title

    new_file_name = f"{number_string}. {title_string}{file_handle}"

    print(f"New Name: {new_file_name}")

    new_file_dir = input_dir / new_file_name

    # newFileName = os.path.join(environment_dir, new_file_name)

    os.rename(src_file, new_file_dir)
