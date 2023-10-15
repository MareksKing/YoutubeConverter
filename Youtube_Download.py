from pytube import YouTube
import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--link", help="Youtube link")
parser.add_argument("--location", help="Download location")
parser.add_argument("--type", help="Download type")
args = parser.parse_args()

link = args.link
location = args.location
download_type = args.type


yt = YouTube(link)
if download_type == "Audio only":
    audio = yt.streams.get_audio_only()
    audio.download(location, filename_prefix="Audio")
    print("Done!")
else:
    if yt.streams.get_by_itag(137) != None:
        audio = yt.streams.get_audio_only()
        audio.download(location, filename="audiotemp.mp3")
        print("Audio done")
        video = yt.streams.get_by_itag(137)
        video.download(location, filename="videotemp.mp4")
        print("Video done")
        os.chdir(location)
        subprocess.call(['ffmpeg', '-i', 'videotemp.mp4','-i','audiotemp.mp3', '-c:v', 'copy', '-c:a', 'aac', f'{video.title}.mp4'])
        os.remove(location+"/videotemp.mp4")
        os.remove(location+"/audiotemp.mp3")
    else:
        video = yt.streams.get_highest_resolution()
        video.download(location)
    print("Download done!")

