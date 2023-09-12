import os

from mutagen.easyid3 import EasyID3

cur_dir = os.getcwd()
environment_dir = os.path.join(cur_dir, "Environment")

if not os.path.exists(environment_dir):
    os.mkdir(environment_dir)


for file in os.listdir(environment_dir):
    print(file)

    split_tup = os.path.splitext(file)

    src_file = os.path.join(environment_dir, file)

    audio = EasyID3(src_file)

    print(audio)

    audio["artist"] = "LALALA"

    print(audio)
    print(audio["artist"])

    audio.save()