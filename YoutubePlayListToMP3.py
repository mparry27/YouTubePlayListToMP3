import youtube_dl
from mutagen.easyid3 import EasyID3
import os

def download():
    # Ask the user for the video they want to download
    playlist_url = 'https://www.youtube.com/playlist?list=PLuOGikDXZn9v6vBW_7Hx_0sRmxy3JYRuW'

    # Download Playlist and convert to mp3
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'download_archive': 'archive.txt',
        'outtmpl': '/Music/%(title)s.mp3',
        'writeinfojson': True,
        'writethumbnail': True,
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([playlist_url])

def metadata():
    # add meta data to mp3
    for song in os.listdir('Music'):
        if(os.path.splitext(song)[-1] == '.mp3'):
            audiofile = easyID3(os.path(song))
            audiofile['title'] = os.path(song)
            audiofile.save()

def run():
    #download()
    metadata()

if __name__ == '__main__':
    run()