import time
import dotenv 
dotenv.load_dotenv()
import os
import yt_dlp

def search_youtube(query, max_results=1):
    search_query = f"ytsearch{max_results}:{query}"
    
    with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
        info = ydl.extract_info(search_query, download=False)
    
    results = []
    for entry in info["entries"]:
        title = entry["title"]
        url = entry["webpage_url"]
        results.append((title, url))

    return results


import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials # type: ignore
scope = "ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=os.getenv('SPOTIFY_CLIENT_ID'), client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'), redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI')))



result = sp.playlist('0bbkoJ3jrVAXFfn4l5jFXk')
if not os.path.exists("songs"):
    os.mkdir("songs")
# print(result['tracks']['items'])
for item in result['tracks']['items']:
    print(item['track']['external_urls']['spotify'])
    time.sleep(2)
    for title, url in search_youtube(item['track']['name'] + ' ' + item['track']['artists'][0]['name']):
        print(f"{title}: {url}")
        
        os.system(f"yt-dlp -x --audio-format mp3 --audio-quality 0 \"{url}\" -o \"./songs/%(title)s.%(ext)s\"")
