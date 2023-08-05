from pytube import YouTube
import os
import re

def remove_symbols(string):
    return re.sub(r'[^a-zA-Z0-9 ]', '', string).replace(' ', '_')

def get_video(link, destination, extension = 'mp4'):

    try:
        yt = YouTube(link)
        print("Downloading...")
    except:
        raise Exception("Invalid link")
    
    filename = remove_symbols(yt.title)+ f".{extension}"

    if extension == "mp4":
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(output_path=destination, filename=filename)
    elif extension == "mp3":
        yt.streams.filter(only_audio=True).first().download(output_path=destination, filename=filename)
    print("Download complete")

    return os.path.join(destination, filename)

def main():
    
    while True:
        destination = 'dl'
        link = input("paste the link:")
        extension = input("type the desired file extension (f.ex 'mp3'/'mp4')")
        get_video(link, destination, extension)

main()