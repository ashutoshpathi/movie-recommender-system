import streamlit as st
import pickle
import pandas as pd
import requests

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")


movies_df = pickle.load(open('movies.pkl', 'rb')) 
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_titles = movies_df['title'].values            

import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie_id {movie_id}: {e}")
        return None




def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id

        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movies_posters

st.title("🎬 Movie Recommender System")
st.markdown("### Find movies similar to your favorites")

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_titles,
    index=None,
    placeholder="Search a movie..."
)

if st.button("✨ Show Recommendation"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    cols = st.columns(5, gap="large")
    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            if poster:
                st.image(poster, use_container_width=True)
            else:
                st.write("🚫 Poster not available")
                st.markdown(f"<div style='text-align:center; font-weight:bold'>{name}</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div style='text-align:center; font-weight:bold; color:white'>{name}</div>",
                unsafe_allow_html=True
            )
