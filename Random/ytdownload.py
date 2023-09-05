import pytube
import os
from tqdm import tqdm

# Prompt the user to enter the URL of the video
url = input("Enter the URL of the YouTube video: ")

# Prompt the user to enter the desired format
format = input("Enter the desired format (mp4 or mp3): ")

# Create a YouTube object from the URL
yt = pytube.YouTube(url)

# Prompt the user to select the desired quality
if format == "mp4":
    video_streams = yt.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').desc()
    print("Available video qualities:")
    for i, stream in enumerate(video_streams):
        print(f"{i+1}. {stream.resolution}")
    quality = int(input("Select the desired quality (1-{}): ".format(len(video_streams))))
    stream = video_streams[quality-1]
elif format == "mp3":
    audio_streams = yt.streams.filter(only_audio=True).order_by('abr').desc()
    print("Available audio qualities:")
    for i, stream in enumerate(audio_streams):
        print(f"{i+1}. {stream.abr}")
    quality = int(input("Select the desired quality (1-{}): ".format(len(audio_streams))))
    stream = audio_streams[quality-1]
else:
    print("Invalid format. Please enter either mp4 or mp3.")
    exit()

# Download the stream with a progress bar
print("Downloading...")
progress_bar = tqdm(total=stream.filesize)
stream.download(filename="download")
progress_bar.close()

# Get the absolute file path of the downloaded file
file_path = os.path.abspath("download." + stream.subtype)

# Convert the mp4 file to mp3 if the format is mp3
if format == "mp3":
    mp3_file_path = os.path.splitext(file_path)[0] + ".mp3"
    os.system(f"ffmpeg -i {file_path} {mp3_file_path}")
    os.remove(file_path)
    print("Video downloaded successfully in mp3 format.")
else:
    print("Video downloaded successfully in mp4 format.")