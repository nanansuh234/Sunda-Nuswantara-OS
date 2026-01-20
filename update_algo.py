import requests
import json
import os

API_KEY = os.getenv('YT_API_KEY')

# Gue udah cariin Channel ID asli dari list lo biar gak boros kuota
CHANNELS = [
    'UC1sz4pommnQQY5xKZ9VadxQ', # Channel lo (Nanan Suhendar)
    'UC0_5B6uV7_C39_mE_P3O6vQ', # Liputan6
    'UCdnzTAYHi7uGuxpnbNoKovA', # KONTAN TV
]

def get_latest_videos():
    all_videos = []
    for c_id in CHANNELS:
        try:
            # Langsung ambil video tanpa cari ID lagi
            v_url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={c_id}&part=snippet,id&order=date&type=video&maxResults=2"
            v_res = requests.get(v_url).json()
            
            if 'items' in v_res:
                for item in v_res['items']:
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
