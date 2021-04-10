from pytube import YouTube

link = input("Enter the Youtube video link you want to download: ")
yt = YouTube(link)

print("Title: ", yt.title)

ys = yt.streams.get_highest_resolution()

ys.download()
print("Download completed!")
