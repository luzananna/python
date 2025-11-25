# Spotify Top 10 Analysis 🎶

## О проекте
Учебный проект для анализа чарта Spotify (Top 50 Global).  
Данные берутся через **Spotify API**, сохраняются в SQLite и визуализируются.

## Используемые технологии
- Python 3.11
- Spotipy (работа с API Spotify)
- SQLite (хранение данных)
- Matplotlib (визуализация)

## Структура
- `src/fetch_data.py` – получение данных из API
- `src/load_to_db.py` – сохранение в SQLite
- `src/analyze_sql.py` – SQL-запросы
- `src/visualize.py` – графики

## Как запустить
```bash
git clone <repo>
cd spotify-analysis
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
