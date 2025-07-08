'''
Author: Shravan Kumar Pandey
Email: shravankumarpandey825412@gmail.com
Date: 08-07-25
'''

import pickle
import streamlit as st
import requests
import os
import gdown  # make sure this is in your requirements.txt

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=50e2c908d241970d7fca932cafd2db9a&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else ""
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Ensure 'artifacts' folder exists
os.makedirs("artifacts", exist_ok=True)

# Download similarity.pkl from Google Drive if not exists
similarity_path = "artifacts/similarity.pkl"
if not os.path.exists(similarity_path):
    file_id = "14spL3-d24xgGcFPgTJj4KuTMkvUmWIex"
    gdown.download(f"https://drive.google.com/uc?id={file_id}", similarity_path, quiet=False)

# Load data
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))

# UI
st.header('Movie Recommender System Using Machine Learning')
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

