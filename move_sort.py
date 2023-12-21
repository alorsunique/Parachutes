# This script should move the files to their respective albums

import os
import shutil
from pathlib import Path

from mutagen.easyid3 import EasyID3

resources_dir_text = "Resources_Path.txt"

entry_list = []
with open(resources_dir_text, 'r') as reader:
    entry_list.append(reader.read())
    reader.close()

resources_dir = Path(entry_list[0])
input_dir = resources_dir / "Input"
move_dir = resources_dir / "Move"

specialChar = "\/?:*<>"

for file in input_dir.iterdir():
    print(f"File: {file.name}")
    src_to_move = file

    audio = EasyID3(src_to_move)

    if 'albumartist' in audio:
        album_artist = str(audio['albumartist'])
    elif 'artist' in audio:
        album_artist = str(audio['artist'])

    album_artist = album_artist[2:-2]

    album = str(audio['album'])
    album = album[2:-2]

    for character in specialChar:
        album_artist = album_artist.replace(character, "")
        album = album.replace(character, "")

    print(f"{album_artist} | {album}")

    album_artist_dir = move_dir / album_artist
    album_dir = album_artist_dir / album

    if not os.path.exists(album_artist_dir):
        os.mkdir(album_artist_dir)

    if not os.path.exists(album_dir):
        os.mkdir(album_dir)

    shutil.move(src_to_move, album_dir)
