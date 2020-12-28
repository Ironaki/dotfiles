#!/usr/bin/env python3
"""
Update configurations in `_config.json` to `config.json`.
If configuration is not in `config.json`, it will be inserted.
If configuration is in `_config.json`, it will not be updated.

Print the diff if exists.
"""
import json
import os
import shutil
import sys
from difflib import unified_diff


def main():
    # Backup file for diff
    shutil.copy("config.json", "config.bak.json")

    with open("_config.json") as f:
        add_configs = json.load(f)

    with open("config.bak.json") as f:
        configs = json.load(f)
        configs |= add_configs  # Python 3.9 dict update

    with open("config.json", "w") as f:
        json.dump(configs, f, indent=4)

    # Print diff
    with open("config.json") as new_file, open("config.bak.json") as old_file:
        for delta in unified_diff(
            old_file.readlines(),
            new_file.readlines(),
            fromfile="config.json",
            tofile="config.json",
        ):
            print(delta, end="")

    # Remove backup file
    os.remove("config.bak.json")


if __name__ == "__main__":
    if sys.version_info < (3, 9):
        print("Please install python version >= 3.9")
        exit()
    main()
