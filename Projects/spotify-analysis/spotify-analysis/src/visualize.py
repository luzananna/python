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

    # Создаём папку charts, если её нет
    charts_dir = os.path.join(os.path.dirname(__file__), "..", "charts")
    os.makedirs(charts_dir, exist_ok=True)

    # === 1. Топ-5 исполнителей в каждом плейлисте ===
    for pl_name, pl_tracks in playlists.items():
        top = top_artists(pl_tracks, n=5)
        df = pd.DataFrame(top, columns=["Исполнитель", "Количество"])

        plt.figure(figsize=(8, 5))
        plt.bar(df["Исполнитель"], df["Количество"], color="skyblue")
        plt.title(f"Топ-5 исполнителей ({pl_name})")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()

        filepath = os.path.join(charts_dir, f"top5_{pl_name.replace(' ', '_')}.png")
        plt.savefig(filepath)
        plt.close()
        print(f"💾 Сохранено: {filepath}")

    # === 2. Общий топ-5 исполнителей ===
    all_tracks = []
    for tr in playlists.values():
        all_tracks.extend(tr)

    top_all = top_artists(all_tracks, n=5)
    df_all = pd.DataFrame(top_all, columns=["Исполнитель", "Количество"])

    plt.figure(figsize=(8, 5))
    plt.bar(df_all["Исполнитель"], df_all["Количество"], color="lightgreen")
    plt.title("🌍 Общий топ-5 исполнителей (все плейлисты)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()

    filepath = os.path.join(charts_dir, "top5_all.png")
    plt.savefig(filepath)
    plt.close()
    print(f"💾 Сохранено: {filepath}")

    # === 3. Пересечение исполнителей ===
    pl_names = list(playlists.keys())
    set1 = set([t["artist"] for t in playlists[pl_names[0]]])
    set2 = set([t["artist"] for t in playlists[pl_names[1]]])

    plt.figure(figsize=(6, 6))
    venn2([set1, set2], set_labels=(pl_names[0], pl_names[1]))
    plt.title("👥 Общие исполнители между плейлистами")

    filepath = os.path.join(charts_dir, "common_artists.png")
    plt.savefig(filepath)
    plt.close()
    print(f"💾 Сохранено: {filepath}")
