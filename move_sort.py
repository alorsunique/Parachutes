# This script should move the files to their respective albums

import os
import shutil
from pathlib import Path

from mutagen.easyid3 import EasyID3

script_path = Path(__file__).resolve()
project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(str(resources_text.readline()).replace('"', ''))

input_dir = resources_dir / "Input"
move_dir = resources_dir / "Move"

special_characters = "\/?:*<>"

for file in input_dir.iterdir():
    print(f"File: {file.name}")
    source_to_move = file

    audio = EasyID3(source_to_move)

    if 'albumartist' in audio:
        album_artist = str(audio['albumartist'])
    elif 'artist' in audio:
        album_artist = str(audio['artist'])

    album_artist = album_artist[2:-2]

    album = str(audio['album'])
    album = album[2:-2]

    for character in special_characters:
        album_artist = album_artist.replace(character, "")
        album = album.replace(character, "")

    print(f"{album_artist} | {album}")

    album_artist_dir = move_dir / album_artist
    album_dir = album_artist_dir / album

    if not os.path.exists(album_artist_dir):
        os.mkdir(album_artist_dir)

    if not os.path.exists(album_dir):
        os.mkdir(album_dir)

    shutil.move(source_to_move, album_dir)
