from datetime import datetime
from pytube.cli import on_progress
from pytube import YouTube, streams

class Conversor():
    def conversorMP3(self):
        for url in self._urls:
            try:
                self._number += 1
                yt = YouTube(url,
                             on_progress_callback = on_progress)
                aud = yt.streams.filter(only_audio=True).last()
                name = f"AUD-{self._datetime}WA00000000"
                name = name[:-len(str(self._number))]
                name = name + str(self._number) + ".mp3"
                print(f"{yt.title} ----- {name}")
                aud.download(filename=name, output_path=self._pathsafe)
                print("\n")
            except Exception as e:
                self._number -= 1
                continue


    def conversorMP4(self):
        for url in self._urls:
            try:
                self._number += 1
                yt = YouTube(url,
                             on_progress_callback = on_progress)
                aud = yt.streams.last()
                name = f"AUD-{self._datetime}WA00000000"
                name = name[:-len(str(self._number))]
                name = name + str(self._number) + ".mp4"
                print(f"{yt.title} ----- {name}")
                aud.download(filename=name, output_path=self._pathsafe)
                print("\n")
            except Exception as e:
                self._number -= 1
                continue

if __name__ == "__main__":
    con = Conversor()
    con.load_config()
    con.load_urls("./link.txt")
    con.conversorMP3()
    con.write_config()
