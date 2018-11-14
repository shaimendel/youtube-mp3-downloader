# youtube-mp3-downloader
Small Python Utility To Convert Youtube URLs To MP3 Files (For Windows)

## Preparation
- pip install youtube_dl
- Put ffprobe.exe near the py file (download from https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20181023-305e523-win64-static.zip, in bin folder)

## Instructions
- Edit the links.txt file and put your own youtube links, one in a line
- run youtube_downloader.py
- The mp3 files will be downloaded to your local folder


## CMD output example
[youtube] wyTBNTHZIdU: Downloading webpage

[youtube] wyTBNTHZIdU: Downloading video info webpage

[download] Destination: Funniest Bloopers - Friends-wyTBNTHZIdU.webm

[download] 100% of 5.43MiB in 00:01

[ffmpeg] Destination: Funniest Bloopers - Friends-wyTBNTHZIdU.mp3

Deleting original file Funniest Bloopers - Friends-wyTBNTHZIdU.webm (pass -k to keep)

[youtube] XVrilSIQO_8: Downloading webpage

[youtube] XVrilSIQO_8: Downloading video info webpage

[download] Destination: 12 Harry Potter Actors Who Were Replaced In The Sequels-XVrilSIQO_8.webm

[download] 100% of 7.07MiB in 00:01

[ffmpeg] Destination: 12 Harry Potter Actors Who Were Replaced In The Sequels-XVrilSIQO_8.mp3

Deleting original file 12 Harry Potter Actors Who Were Replaced In The Sequels-XVrilSIQO_8.webm (pass -k to keep)
