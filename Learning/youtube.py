import pytube
#from pytube import YouTube
import os

# link = "https://www.youtube.com/watch?v=mpjREfvZiDs"
# yt = pytube.YouTube(link)
# stream = yt.streams.first()
# stream.download()
# video_name = stream.default_filename
# os.rename(video_name, 'newvideo.mp4')

def download():
    link = input("Enter the youtube link you want to donwload: ")
    name = input("Name the vidoe: ")
    yt = pytube.YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    video_name = stream.default_filename
    os.rename(video_name, name + ".mp4")

download()
