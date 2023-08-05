from pytube import YouTube
from moviepy.editor import AudioFileClip
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
    filepath = os.path.join(destination, filename)

    if extension == "mp4":
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(output_path=destination, filename=filename)
    elif extension == "mp3":
        yt.streams.filter(only_audio=True).first().download(output_path=destination, filename=filename)
        audio_clip = AudioFileClip(filepath)
        wav_file_path = os.path.join(filepath.split(".")[0] + ".wav")
        print(filepath,wav_file_path)
        audio_clip.write_audiofile(wav_file_path, codec="pcm_s16le")
        audio_clip.close()
        os.remove(filepath)

    print("Download complete")

    return filepath

def main():
    
    while True:
        destination = os.path.join(r'C:\Users\taris\Desktop\Youtube Download\dl')
        link = input("paste the link:")
        extension = input("type the desired file extension (f.ex 'mp3'/'mp4')")
        get_video(link, destination, extension)

main()