# Importing necessary libraries

import pandas as pd
import streamlit as st
import pickle
import movieposters as mp


# Backend

# Defining Movie Recommendation Function

def recommend(title):
    movie_index = movies[movies['title'] == title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movies_list:

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Loading stored files using pickle

similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)


# Frontend


# Title of the Movie Recommender System Homepage

st.title("Movie Recommender System")

# Creating a selectbox for user to choose a movie to show recommendations based upon

option = st.selectbox("Please choose a movie to get recommendations",
                      movies['title'].values)

# Creating a "Recommend" button

if st.button("Recommend"):
    recommendations = recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.image(mp.get_poster(title=recommendations[0]))
        st.text(recommendations[0])

    with col2:

        st.image(mp.get_poster(title=recommendations[1]))
        st.text(recommendations[1])

    with col3:

        st.image(mp.get_poster(title=recommendations[2]))
        st.text(recommendations[2])

    with col4:

        st.image(mp.get_poster(title=recommendations[3]))
        st.text(recommendations[3])

    with col5:

        st.image(mp.get_poster(title=recommendations[4]))
        st.text(recommendations[4])

