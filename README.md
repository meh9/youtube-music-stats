# youtube-music-stats
Get stats from your Youtube Music history

Simple python script to process your Youtube Music history and tell you what you listen to most (and least). The statistics data is saved to a CSV file so you can open it in Excel or your spreadsheet of choice, or pass it in to other tools.

The Youtube Music stats file that the script takes as input needs to be downloaded from Google Takeout: https://takeout.google.com/settings/takeout

In Google Takeout, you do not need anything else but the very last option `YouTube and YouTube Music` ticked - so consider using the `Deselect all` at the top. Remember to set the data format to JSON before downloading - see screenshots at the bottom of this page for further guidance.


### Requirements
It has none - Python has batteries included already.


### Running
Save your `watch-history.json` that you downloaded from Google Takeout in the root directory next to the script.

Then simply run the script with something like:
```
python3 listen_history.py
```
When the script runs successfully, it will finish by telling you your total number of tracks played - that means it worked!

There should now be a file named `history.csv`.

You can optionally tell it to use different file names for input and output:
```
% python3 listen_history.py --help       
usage: listen_history.py [-h] [-f [INFILE]] [-o [OUTFILE]]

Produce listening statistics from Youtube Music history.

options:
  -h, --help            show this help message and exit
  -f [INFILE], --infile [INFILE]
                        specify a file to read other than the default 'watch-history.json'
  -o [OUTFILE], --outfile [OUTFILE]
                        specify a file to write the output to other than the default 'history.csv'
```


### Google Takeout reference screenshots
<img width="350" alt="history" src="https://raw.githubusercontent.com/meh9/youtube-music-stats/main/history.png">
<img width="350" alt="file_format" src="https://raw.githubusercontent.com/meh9/youtube-music-stats/main/file_format.png">
