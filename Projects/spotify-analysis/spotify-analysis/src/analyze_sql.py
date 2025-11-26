# src/analyze_data.py
from collections import Counter
import os
import json
from collections import Counter

def load_tracks(filename="tracks.json"):
    """Load playlists dictionary with tracks from a JSON file."""
    base_dir = os.path.dirname(__file__)   
    path = os.path.join(base_dir, "..", filename) 
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)    


def find_common_artists(playlists: dict):
    """Return artists that appear in all playlists."""
    artist_sets = {
        name: set(track["artist"] for track in tracks)
        for name, tracks in playlists.items()
    }
    common = set.intersection(*artist_sets.values())
    return common


def top_artists(tracks, n=5):
    """Return the top-n most frequent artists in the given list of tracks."""
    artists = [t["artist"] for t in tracks]
    counter = Counter(artists)
    return counter.most_common(n)


if __name__ == "__main__":
    # Load collected playlist data
    playlists = load_tracks()

    # Common artists among all playlists
    common = find_common_artists(playlists)
    print(f"Common artists across all playlists: {list(common)}\n")

    # Top-5 artists for each playlist
    for pl_name, pl_tracks in playlists.items():
        print(f"Top-5 artists ({pl_name}):")
        for artist, count in top_artists(pl_tracks, n=5):
            print(f"  {artist}: {count} tracks")
        print()

    # Combined Top-5 artists across *all* playlists
    all_tracks = []
    for pl_tracks in playlists.values():
        all_tracks.extend(pl_tracks)

    print("Global Top-5 Artists (all playlists combined):")
    for artist, count in top_artists(all_tracks, n=5):
        print(f"  {artist}: {count} tracks")
        