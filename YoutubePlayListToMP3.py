import youtube_dl
import os

def download():
    # Load youtube playlist from txt file
    playlist = open("playlisturl.txt", "r")
    playlist_url = playlist.read()

    # Download Playlist and convert to mp3
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'download_archive': 'archive.txt',
        'outtmpl': '/Music/%(title)s.mp3',
        #'writeinfojson': True,
        #'writethumbnail': True,
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([playlist_url])

def run():
    download()

if __name__ == '__main__':
    run()