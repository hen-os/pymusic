from pytube import YouTube
from pytube.cli import on_progress

def mp3_conversor(pathFile, nameFile, url):
    yt = YouTube(url,
        on_progress_callback = on_progress)
    aud = yt.streams.last()
    aud.download(filename=nameFile, output_path=pathFile)
    return f"{yt.title} ----- {nameFile}"

