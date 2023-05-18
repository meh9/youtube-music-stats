import csv
import json
 
f = open("watch-history.json", encoding="utf8")
 
data = json.load(f)
pruned = {}
 
for entry in data:
    if (entry["header"] == "YouTube Music") and (entry["title"] != "Visited YouTube Music") and ("https://www.youtube.com/watch?v=" not in entry["title"]) and (entry["title"] != "Watched a video that has been removed"):
        
        title = entry["title"][8::]
 
        artist = entry["subtitles"][0]["name"].replace(" - Topic", "")
        artist_title = (artist, title)
 
        if artist_title in pruned:
            pruned[artist_title] = pruned[artist_title] + 1
        else:
            pruned[artist_title] = 1
 
total_plays = 0
 
with open("history.csv", "w", newline="") as csvfile:
    history_writer = csv.writer(csvfile, dialect="excel", quoting=csv.QUOTE_MINIMAL)
    history_writer.writerow(["Artist", "Title", "Listens"])

    for song, listens in dict(sorted(pruned.items(), key=lambda item: item[1], reverse=True)).items():
        total_plays += listens
        history_writer.writerow([song[0], song[1], listens])
 
print(f'{total_plays} total plays across all tracks')