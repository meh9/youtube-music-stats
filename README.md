# youtube-music-stats
Get stats from your Youtube Music history

Simple python script to process your Youtube Music history and tell you what you listen to most (and least).

The Youtube Music stats file needs to be downloaded from Google Takeout, here: https://takeout.google.com/settings/takeout

Remember to set the data format to JSON before downloading.

There's some screenshots at the bottom to help.

### Requirements
It has none - Python has batteries included already.

### Running
Save your `watch-history.json` that you downloaded from Google Takeout in the root directory next to the script.

Then simply run the script with something like:
```
python3 listen_history.py
```

### Google Takeout reference screenshots
<img width="350" alt="history" src="https://raw.githubusercontent.com/meh9/youtube-music-stats/main/history.png">
<img width="350" alt="file_format" src="https://raw.githubusercontent.com/meh9/youtube-music-stats/main/file_format.png">
