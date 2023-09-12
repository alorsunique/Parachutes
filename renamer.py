

import os

from mutagen.easyid3 import EasyID3

cur_dir = os.getcwd()
environment_dir = os.path.join(cur_dir, "Environment")

if not os.path.exists(environment_dir):
    os.mkdir(environment_dir)

specialChar = "\/?:*"

for fileHandle in os.listdir(environment_dir):
    print(fileHandle)
    split_tup = os.path.splitext(fileHandle)

    src_file = os.path.join(environment_dir, fileHandle)

    audio = EasyID3(src_file)

    numberHold = str(audio['tracknumber'])
    print(numberHold)
    numberHold = numberHold[2:-2]
    if "/" in numberHold:
        numberSplit = numberHold.split("/")
    else:
        numberSplit = numberHold.split(" ")

    if int(numberSplit[0]) < 10:
        numberString = "0" + str(int(numberSplit[0]))
    else:
        numberString = str(int(numberSplit[0]))

    titleHold = str(audio['title'])
    titleHold = titleHold[2:-2]

    for character in specialChar:
        titleHold = titleHold.replace(character, "")

    titleString = titleHold

    newFileNameString = numberString + ". " + titleString + split_tup[1]

    print(newFileNameString)

    newFileName = os.path.join(environment_dir, newFileNameString)

    print(newFileName)

    os.rename(src_file, newFileName)
