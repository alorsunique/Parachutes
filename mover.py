

import os
import shutil

from mutagen.easyid3 import EasyID3


cur_dir = os.getcwd()
environment_dir = os.path.join(cur_dir, "Environment")
move_dir = os.path.join(cur_dir, "Move")

if not os.path.exists(environment_dir):
    os.mkdir(environment_dir)

if not os.path.exists(move_dir):
    os.mkdir(move_dir)

specialChar = "\/?:*<>"

for to_move in os.listdir(environment_dir):
    print(to_move)
    src_to_move = os.path.join(environment_dir, to_move)

    audio = EasyID3(src_to_move)
    print(audio)

    if 'albumartist' in audio:
        albumArtistHold = str(audio['albumartist'])
    elif 'artist' in audio:
        albumArtistHold = str(audio['artist'])

    albumArtistHold = albumArtistHold[2:-2]


    albumHold = str(audio['album'])
    albumHold = albumHold[2:-2]


    for character in specialChar:
        albumArtistHold = albumArtistHold.replace(character,"")
        albumHold = albumHold.replace(character, "")


    print(albumHold)
    print(albumArtistHold)

    albumArtistMove = os.path.join(move_dir,albumArtistHold)
    print(albumArtistMove)

    albumMove = os.path.join(albumArtistMove,albumHold)
    print(albumMove)

    if not os.path.exists(albumArtistMove):
        os.mkdir(albumArtistMove)

    if not os.path.exists(albumMove):
        os.mkdir(albumMove)

    shutil.move(src_to_move, albumMove)



