import requests
import json
import os

API_KEY = os.getenv('YT_API_KEY')
# Kita tes 5 channel besar dulu biar pasti jalan
CHANNELS_NAMES = ["Liputan6", "Firstpost", "Pandji Pragiwaksono", "Ferry Irwandi", "KONTAN TV"]

def get_latest_videos():
    all_videos = []
    for name in CHANNELS_NAMES:
        try:
            # Cari ID
            s_url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&q={name}&type=channel&part=id&maxResults=1"
            s_res = requests.get(s_url).json()
            if 'items' in s_res and s_res['items']:
                c_id = s_res['items'][0]['id']['channelId']
                # Ambil Video
                v_url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={c_id}&part=snippet,id&order=date&type=video&maxResults=1"
                v_res = requests.get(v_url).json()
                if 'items' in v_res:
                    item = v_res['items'][0]
                    all_videos.append({
                        'title': item['snippet']['title'],
                        'videoId': item['id']['videoId'],
                        'thumbnail': item['snippet']['thumbnails']['high']['url'],
                        'channel': item['snippet']['channelTitle']
                    })
        except:
            continue
    
    with open('data.json', 'w') as f:
        json.dump(all_videos, f, indent=4)

if __name__ == "__main__":
    get_latest_videos()
