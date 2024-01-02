from pytube import YouTube
from sys import argv
from moviepy.editor import VideoFileClip, AudioFileClip
import os, time

link = input("Enter video link : ")
video = YouTube(link)

print("Title : ", video.title, "\nViews : ", video.views, "\nAuthor : ", video.author)

vd = video.streams.get_highest_resolution()
aud = video.streams.filter(only_audio=True).first() 
size = round(vd.filesize_mb)
deci = int(input(f"File size is {size} MB. Download (1 = yes, 0 = no) ? "))

if deci == 1:
    vd.download(filename="Video.mp4")
    out_file = aud.download(filename="Audio.mp3")

    video_clip = VideoFileClip("Video.mp4")
    audio_clip = AudioFileClip("Audio.mp3")
    final_clip = video_clip.set_audio(audio_clip)
    name = input("Enter file name (leave blank to use default) : ")
    if not name:
        name = "Combined"
    final_clip.write_videofile(name + ".mp4")
    video_clip.close()
    audio_clip.close()
    final_clip.close()
    time.sleep(1)
    deci2 = int(input("Download finished ! Delete junk (1 = yes, 0 = no) ? "))

    if deci2 == 1:
        os.remove("Video.mp4")
        os.remove("Audio.mp3")
        print("Process finished.")
    elif deci2 == 0:
        print("Process finished.")
elif deci == 0:
    print("Download aborted.")