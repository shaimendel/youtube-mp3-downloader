from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'no_warnings': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with open('links.txt', 'r') as links:
	links_list = [link.strip() for link in links.readlines() if link.strip()]

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links_list)