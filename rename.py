# This script should rename the music file appropriately given that the info are in the metadata

import os
from pathlib import Path

from mutagen.easyid3 import EasyID3

script_path = Path(__file__).resolve()
project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(str(resources_text.readline()).replace('"', ''))

input_dir = resources_dir / "Input"

special_characters = "\/?:*"

for file in input_dir.iterdir():
    print(f"File: {file.name}")

    file_extension = file.suffix

    source_file = file

    audio = EasyID3(source_file)

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

    for character in special_characters:
        title = title.replace(character, "")

    title_string = title

    new_file_name = f"{number_string}. {title_string}{file_extension}"

    print(f"New Name: {new_file_name}")

    new_file_path = input_dir / new_file_name

    os.rename(source_file, new_file_path)
