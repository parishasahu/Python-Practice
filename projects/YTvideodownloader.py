from pytubefix import YouTube
from pytubefix.cli import on_progress

def download_yt_video(url ,Quality):
    
    
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    if Quality == "highest":
        ys = yt.streams.get_highest_resolution()
        print("This is highest resolu")
    else:
        ys = yt.streams.get_lowest_resolution()
        print("This is lowest resolu")
    ys.download()


for i in range (1,4):
    download_yt_video(input("enter url: "), input(" enter Quality : "))

