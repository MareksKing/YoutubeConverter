from pytube import YouTube

link = "https://www.youtube.com/watch?v=F0Gkr4MBEO0"
yt = YouTube(link)
audio = yt.streams.get_audio_only()
video = yt.streams.get_highest_resolution()
audio.download('~/Downloads')
print("Done!")