import os
import json
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Download keys from .env
load_dotenv()

# Ccreates an authorization mechanism via OAuth (login to Spotify)
spotify = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_ID"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-read-private user-library-read"
))

def get_playlist_id_by_search(query: str) -> str | None:
    results = spotify.search(q=query, type="playlist", limit=5)
    items = results.get("playlists", {}).get("items", [])

    #filter None
    items = [p for p in items if p is not None]
    if not items:
        print(f"Playlist '{query}' is not found")
        return None
    print(f"Playlists found for '{query}': {[p.get('name') for p in items if p]}")
    return items[0]["id"]

def fetch_top_tracks(query: str, limit: int = 10):
    playlist_id = get_playlist_id_by_search(query)
    if not playlist_id:
        print(f"Playlist '{query}' is not found")
        return []
    
    results = spotify.playlist_tracks(playlist_id, limit=limit)
    items = results.get("items", [])

    tracks = []
    for item in items:
        track = item.get("track")
        if not track:
            continue

        track_id = track.get("id")
        if not track_id:
            print(f"Пропущен трек без id: {track.get('name')}")
            continue

        tracks.append({
            "id": track_id,
            "name": track["name"],
            "artist": track["artists"][0]["name"],
        })    
    return tracks

if __name__ == "__main__":
    queries = ["Top 50 Global", "Top 50 Czech REpubliic"]

    playlists = {}
    for q in queries:
        print(f"Download: {q} ...")
        playlists[q] = fetch_top_tracks(q, limit=50)
    
    with open("tracks.json", "w", encoding="utf-8") as f:
        json.dump(playlists, f, ensure_ascii=False, indent=2)
    print(f"\n Данные сохранены в tracks.json ({sum(len(v) for v in playlists.values())} tracks) ")
    