# 🎧 Spotify Data Analysis

A mini data-analysis project exploring audio features of songs.
Using Pandas for data processing and Matplotlib for visualizations.

## Project Overview

This project analyzes a dataset of Spotify tracks and provides insights into:
	- Most popular songs
	- Artists with the highest average popularity
	- Loudest and most energetic tracks
	- Ranking songs based on multiple musical features
	- Visual comparison of top songs using bar charts

The goal was to practice data cleaning, data manipulation, and basic visualization using real-world data.

## Features Implemented

The project loads and processes a Spotify dataset using pandas, where the data is cleaned, filtered, and prepared for analysis. From the full dataset, only meaningful musical attributes—such as loudness, speechiness, and acousticness—were selected. Irrelevant columns were removed, and the remaining tracks were sorted by popularity to simplify further evaluation.

The analysis includes extracting the top 10 most popular tracks, identifying artists with the highest average popularity, and finding songs that stand out based on specific characteristics, such as the loudest track, the most energetic one, and the one with the highest valence (happiness score).

A combined musical score was calculated for each track, where all features were first normalized to ensure fair comparison across different scales. This score helps determine the “best” tracks based on overall musical attributes rather than popularity alone.

The project also includes a simple data visualization: a bar chart created with Matplotlib, comparing loudness levels among top artists, providing an intuitive graphical summary of the dataset.

## Structure
data_cleaning.py     # Removing columns, sorting, preprocessing
feature_stats.py     # Max loudness/energy/valence, top tracks
scoring.py           # Combined normalized feature score
visualization.py     # Matplotlib chart


