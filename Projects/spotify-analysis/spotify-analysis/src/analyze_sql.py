# src/analyze_data.py
from collections import Counter
import json

def load_tracks(filename="tracks.json"):
    """Загружаем список треков из файла"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def find_common_artists(playlists: dict):
    """Находит общих исполнителей между плейлистами"""
    sets = {name: set(track["artist"] for track in tracks) 
            for name, tracks in playlists.items()}
    common = set.intersection(*sets.values())
    return common

def top_artists(tracks, n=5):
    """Находит топ-n исполнителей по частоте"""
    artists = [t["artist"] for t in tracks]
    counter = Counter(artists)
    return counter.most_common(n)


if __name__ == "__main__":
    # Загружаем собранные данные
    playlists = load_tracks()

    # Общие исполнители
    common = find_common_artists(playlists)
    print(f"👥 Общие исполнители: {list(common)}\n")

    # Топ-5 для каждого плейлиста
    for pl_name, pl_tracks in playlists.items():
        print(f"🏆 Топ-5 исполнителей ({pl_name}):")
        for artist, count in top_artists(pl_tracks, n=5):
            print(f"  {artist}: {count} треков")
        print()

    # Топ-5 общий (все плейлисты вместе)
    all_tracks = []
    for pl_tracks in playlists.values():
        all_tracks.extend(pl_tracks)

    print("🌍 Общий топ-5 исполнителей (все плейлисты):")
    for artist, count in top_artists(all_tracks, n=5):
        print(f"  {artist}: {count} треков")
