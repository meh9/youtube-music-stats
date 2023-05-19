"""
Parse watch-history.json from Google Takeout, count how many times each song has been played, 
and write the stats to a CSV, sorted in reverse order first by Listens then by Artist-Title.
"""

import argparse
import csv
import json
from typing import Any

infile_default: str = "watch-history.json"
outfile_default: str = "history.csv"

parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description="Produce listening statistics from Youtube Music history."
)
parser.add_argument(
    "-f",
    "--infile",
    nargs="?",
    type=argparse.FileType("r"),
    default=infile_default,
    const=infile_default,
    help=f"specify a file to read other than the default '{infile_default}'",
)
parser.add_argument(
    "-o",
    "--outfile",
    nargs="?",
    type=argparse.FileType("w"),
    default=outfile_default,
    const=outfile_default,
    help=f"specify a file to write the output to other than the default '{outfile_default}'",
)
args: argparse.Namespace = parser.parse_args()

data: list[dict[str, Any]] = []
pruned: dict[tuple[str, str], int] = {}

with args.infile as f:
    data = json.load(f)

for entry in data:
    if (
        entry["header"] == "YouTube Music"
        and entry["title"] != "Visited YouTube Music"
        and "https://www.youtube.com/watch?v=" not in entry["title"]
        and entry["title"] != "Watched a video that has been removed"
    ):
        title: str = entry["title"][8::]

        artist: str = entry["subtitles"][0]["name"].replace(" - Topic", "")
        artist_title: tuple[str, str] = (artist, title)

        if artist_title in pruned:
            pruned[artist_title] = pruned[artist_title] + 1
        else:
            pruned[artist_title] = 1

total_plays: int = 0

with args.outfile as csvfile:
    history_writer = csv.writer(csvfile, dialect="excel", quoting=csv.QUOTE_MINIMAL)
    history_writer.writerow(["Artist", "Title", "Listens"])

    sorted_dict: dict[tuple[str, str], int] = dict(
        sorted(pruned.items(), key=lambda item: (item[1], item[0]), reverse=True)
    )
    for song, listens in sorted_dict.items():
        total_plays += listens
        history_writer.writerow([song[0], song[1], listens])

print(f"{total_plays} total plays across all tracks")
