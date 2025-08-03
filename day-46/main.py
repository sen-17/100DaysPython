from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://www.billboard.com/charts/hot-100"
SONGS = "http://open.spotify.com/track"
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = CLIENT_ID,
    client_secret= CLIENT_SECRET,
    redirect_uri= REDIRECT_URI,
    scope= SCOPE
    ))

ask_user = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD: ")

headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(f"{URL}/{ask_user}" , headers=headers)
contents = response.text

soup = BeautifulSoup(contents , "html.parser")
song_elements = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in song_elements]

track_uris = []
for title in song_titles:
    try:
        results = sp.search(q = title , type="track", limit=1)
        tracks = results["tracks"]["items"]

        uri = tracks[0]["uri"]
        name = tracks[0]["name"]
        artist = tracks[0]["artists"][0]["name"]

        track_uris.append(uri)
    except (KeyError, IndexError) as e:
        print(f"Error parsing track data for: {title} | Error: {e}")
    except Exception as e:
        print(f"Unexpected error for: {title} | Error: {e}")

user_id = sp.current_user()["id"]
playlist_name = f"{ask_user} 100 Billboard"
playlist = sp.user_playlist_create(user=user_id, name = playlist_name, public=False)
playlist_id = playlist["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)

    
    



