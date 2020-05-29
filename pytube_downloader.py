from pytube import YouTube
link = "'https://youtu.be/9bZkp7q19f0'"

# Directly Download
# YouTube(link).streams.first().download()

yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
