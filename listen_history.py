"""
Parse watch-history.json from Google Takeout, count how many times each song has been played, 
and write the stats to a CSV.
"""

import csv
import json
from typing import Any

data: list[dict[str, Any]] = []
pruned: dict[tuple[str, str], int] = {}

with open("watch-history.json", "r", encoding="utf8") as f:
    data = json.load(f)

for entry in data:
    if (
        (entry["header"] == "YouTube Music")
        and (entry["title"] != "Visited YouTube Music")
        and ("https://www.youtube.com/watch?v=" not in entry["title"])
        and (entry["title"] != "Watched a video that has been removed")
    ):
        title: str = entry["title"][8::]

        artist: str = entry["subtitles"][0]["name"].replace(" - Topic", "")
        artist_title: tuple[str, str] = (artist, title)

        if artist_title in pruned:
            pruned[artist_title] = pruned[artist_title] + 1
        else:
            pruned[artist_title] = 1

total_plays: int = 0

with open("history.csv", "w", encoding="utf8") as csvfile:
    history_writer = csv.writer(csvfile, dialect="excel", quoting=csv.QUOTE_MINIMAL)
    history_writer.writerow(["Artist", "Title", "Listens"])

    for song, listens in dict(
        sorted(pruned.items(), key=lambda item: item[1], reverse=True)
    ).items():
        total_plays += listens
        history_writer.writerow([song[0], song[1], listens])

print(f"{total_plays} total plays across all tracks")
