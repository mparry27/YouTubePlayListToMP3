import youtube_dl

def run():
    # Ask the user for the video they want to download
    playlist_url = 'https://www.youtube.com/playlist?list=PLuOGikDXZn9uWveEbG20k9cGP3cIwANGk'

    # Download Playlist and convert to mp3
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'download_archive': 'archive.txt',
        'outtmpl': '/Music/%(title)s.mp3',
        'writeinfojson': True,
        'writethumbnail': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([playlist_url])

    # add meta data to mp3


if __name__ == '__main__':
    run()