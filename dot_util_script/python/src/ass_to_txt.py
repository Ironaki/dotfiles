#!/usr/bin/env python3

from glob import glob
from sys import argv


def process(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    processed = []
    for line in lines:
        processed.append(line.split(",,")[-1])

    fp_split = file_path.split("/")
    fp_split[-1] = f"sub_{fp_split[-1]}.txt"

    with open("/".join(fp_split), "w") as f:
        f.writelines(processed)


if __name__ == "__main__":
    if not argv[1:]:
        for fp in glob("subs/*"):
            process(fp)
            print(f"Converting {fp}")
    else:
        for fp in argv[1:]:
            process(fp)
            print(f"Converting {fp}")
