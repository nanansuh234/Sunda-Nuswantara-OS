import requests
import json
import os

API_KEY = os.getenv('YT_API_KEY')
# List Channel ID yang mau lo "paksain" jadi algoritma bareng
CHANNELS = ['UC...', 'UC...'] 

def get_videos():
    all_videos = []
    for channel_id in CHANNELS:
        url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=5"
        res = requests.get(url).json()
        if 'items' in res:
            for item in res['items']:
                all_videos.append({
                    'title': item['snippet']['title'],
                    'videoId': item['id']['videoId'],
                    'thumbnail': item['snippet']['thumbnails']['high']['url'],
                    'channel': item['snippet']['channelTitle']
                })
    
    with open('data.json', 'w') as f:
        json.dump(all_videos, f, indent=4)

if __name__ == "__main__":
    get_videos()