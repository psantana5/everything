from TikTokApi import TikTokApi
import requests

# Ask the user for the TikTok video URL
url = input("Enter the TikTok video URL: ")

# Create a TikTokApi instance and get the video URL
api = TikTokApi()
video_url = api.get_video_by_url(url)

# Download the video and save it to disk
response = requests.get(video_url)
with open('video.mp4', 'wb') as f:
    f.write(response.content)