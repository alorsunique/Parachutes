import os
from pathlib import Path

resources_dir_text = "Resources_Path.txt"

with open(resources_dir_text, 'a') as writer:
    pass

entry_list = []

with open(resources_dir_text, 'r') as reader:
    entry_list.append(reader.read())

if entry_list[0]:
    resources_dir = Path(str(entry_list[0]).replace('"', ''))
    print(f"Resources Directory: {resources_dir}")

    if not resources_dir.exists():
        os.mkdir(resources_dir)

    input_dir = resources_dir / "Input"
    if not input_dir.exists():
        os.mkdir(input_dir)

    flac_convert_workspace_dir = resources_dir / "FLAC Workspace"
    if not flac_convert_workspace_dir.exists():
        os.mkdir(flac_convert_workspace_dir)

    move_dir = resources_dir / "Move"
    if not move_dir.exists():
        os.mkdir(move_dir)
else:
    print(f"No directory")