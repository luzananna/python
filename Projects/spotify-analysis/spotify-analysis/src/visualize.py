# src/visualize.py
import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib_venn import venn2


def load_tracks(filename="tracks.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def top_artists(tracks, n=5):
    artists = [t["artist"] for t in tracks]
    counter = Counter(artists)
    return counter.most_common(n)


if __name__ == "__main__":
    playlists = load_tracks()

    # create charts/ folder one level above src/
    charts_dir = os.path.join(os.path.dirname(__file__), "..", "charts")
    os.makedirs(charts_dir, exist_ok=True)

    # 1) Top-5 artists for each playlist
    for pl_name, pl_tracks in playlists.items():
        top = top_artists(pl_tracks, n=5)
        df = pd.DataFrame(top, columns=["Artist", "Count"])

        plt.figure(figsize=(8, 5))
        plt.bar(df["Artist"], df["Count"])
        plt.title(f"Top-5 artists ({pl_name})")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()

        filepath = os.path.join(
            charts_dir,
            f"top5_{pl_name.replace(' ', '_')}.png"
        )
        plt.savefig(filepath)
        plt.close()
        print(f"Saved: {filepath}")

    # 2) Global top-5 (all playlists together)
    all_tracks = []
    for tr in playlists.values():
        all_tracks.extend(tr)

    top_all = top_artists(all_tracks, n=5)
    df_all = pd.DataFrame(top_all, columns=["Artist", "Count"])

    plt.figure(figsize=(8, 5))
    plt.bar(df_all["Artist"], df_all["Count"])
    plt.title("Global top-5 artists (all playlists)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    filepath = os.path.join(charts_dir, "top5_all.png")
    plt.savefig(filepath)
    plt.close()
    print(f"Saved: {filepath}")

    # 3) Venn-диаграмма пересечения артистов
    pl_names = list(playlists.keys())
    set1 = {t["artist"] for t in playlists[pl_names[0]]}
    set2 = {t["artist"] for t in playlists[pl_names[1]]}

    plt.figure(figsize=(6, 6))
    venn2([set1, set2], set_labels=(pl_names[0], pl_names[1]))
    plt.title("Common artists between playlists")

    filepath = os.path.join(charts_dir, "common_artists.png")
    plt.savefig(filepath)
    plt.close()
    print(f"Saved: {filepath}")