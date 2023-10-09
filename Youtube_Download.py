from pytube import YouTube
import argparse

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
    video = yt.streams.get_by_itag(137)
    # video = yt.streams.filter(progressive=True).las
    video.download(location, filename_prefix="Video")
    print("Download done!")

