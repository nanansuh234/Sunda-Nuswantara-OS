import requests
import json
import os

API_KEY = os.getenv('YT_API_KEY')
# List Channel ID yang mau lo "paksain" jadi algoritma bareng
CHANNELS_NAMES = [
    "Warta Kota Production", "Liputan6", "Just Pranks", "Firstpost", 
    "Muzen - Musik Netizen", "Planet News", "Peaceful Rest", "Muse Asia",
    "Times Of India", "Status Coup News", "4K Relaxation Channel", "YHS Media",
    "Music Brokers", "Animortis", "Animus Morphosis", "Heisei Sound System",
    "The Pedia", "Johnny 5 Music", "Kaitoo74", "Artificial Harmony",
    "Af Music cover", "VinylByte", "Astral Atom", "Nanda Pradika",
    "Baku Hantam", "Askjapan", "JV Music Collaboration", "Grim Fuel",
    "FAITH IN A FLASH", "Tanah Jawa Dwipa", "Kabar Langit", "MIKIRO",
    "Pandji Pragiwaksono", "Pandangan Mata", "Cozy Day ASMR 癒し", "BENCANA POPULER",
    "Grey District Audio", "MIND LIFT", "MATA KETIGA", "Ghibli Silent Days",
    "ANTARA News", "tribunjabar video", "Business Inspiration", "Benn Jordan",
    "Ferry Irwandi", "Kompascom Reporter on Location", "yomikez", "Aura Haruno",
    "GESARA news", "GEMBULIKUM", "Sekilas Uang", "TOP PINK", "Kompas.com",
    "Aini Musik", "The Royal Nation", "Bennix", "guru gembul", "Anonymous Prophet",
    "Dokumentari", "Dongeng uNick LaLa (DNL)", "Fajrul Fx", "Yann Animasi",
    "MASAFUMI KAWAMOTO", "The Dodo", "ERA MAHDI", "Ghibran Arrazi", "slob",
    "KAUM HADI", "Anons Super", "Ricky Suwarno", "VoxAlchemy", "Ngaji Roso (Mas Hendra)",
    "KONTAN TV", "Watchdoc Unity", "Muhammad Hamdan AlGhozali", "Mr. Ledger",
    "Bale Films", "Liputan 6 SCTV Daerah", "𝓢𝓪𝓽𝓻𝓲𝓪 𝓝𝓾𝓼𝓪𝓷𝓽𝓪𝓻𝓪💫", "YUSHA CHANNEL",
    "MerdekaDotCom", "INFO AWIBISANA", "Esha P", "MICHAEKAL", "Pena Cakra",
    "Fittest Flat Earther", "Permata Islam", "Caveine", "Anak Bapak Aing",
    "Prof Jiang Uncut", "Bossman Mardigu", "Old World Ledger", "FINMUSIC",
    "Tempodotco", "Inti channel", "GAGAL GAJIAN", "TUKANG AB", "FASKHO OFFICIAL",
    "Channel Anak TUHAN", "Matt Peci Channel"
]

# Tambahkan ID channel lo sendiri sebagai prioritas utama
MY_CHANNEL_ID = 'UC1sz4pommnQQY5xKZ9VadxQ'

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
