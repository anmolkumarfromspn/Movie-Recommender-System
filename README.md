# Movie-Recommender-System

## Project Objective

The objective of this machine learning-based movie recommendation system project is to develop a personalized movie recommendation system that enhances user engagement and satisfaction by offering tailored movie suggestions. This project involves data collection, exploratory data analysis, feature engineering, and the selection and training of appropriate recommendation models. The system will be deployed with a user-friendly interface, allowing users to interact with it and provide feedback for continuous improvement. The success of this project will be measured by the system's ability to provide accurate and relevant movie recommendations, its deployment, and its responsiveness to user feedback, ultimately contributing to an improved user experience on a media or streaming platform.

## Data Description

Two datasets of 5000 movies were used to develop this project. The data is scrapped from TMDB (The Movie DataBase) website.

Dataset 1:-
tmdb_5000_movie.csv
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/2bc1a163-9efe-43c4-9a23-76c414ce2edd)

This dataset contains all necessary details of 5000 movies that can be required as features to create this ML model like - budget	genres,	homepage,	id,	keywords,	original_language,	original_title,	overview,	popularity,	production_companies,	production_countries,	release_date,	revenue	runtime,	spoken_languages,	status,	tagline	title,	vote_average,	vote_count

Dataset 2:- 
tmdb_5000_credits.csv
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/15f52dd4-e2f4-45b3-9327-e8e45300cfa4)

This dataset contains the movie credits information like crew, cast, etc. 

Both Datasets are available on kaggle: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

## Data Cleaning/Preprocessing

Various important pythoin libraries were used in this project from reading datasets to extracting only needed features, data preprocessing by applying NLP using NLTK to storing model and data with the help of pickle library.
Here are some important key steps followed in this project: -

### Data Preprocessing

Step 1:-
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/9ffddd82-c95c-45d8-8f8a-752238e5d7c4)

Step 2:-
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/62fc1dfc-3900-4d85-91f6-d9de6e5adfe7)

Step 3:-
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/9ee9c99d-5542-4b75-8de3-bd30313c0216)

Step 4:-
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/11237607-35cc-4ba4-9768-19e2489af86e)

Step 5:-
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/54ffc9f5-064f-49c4-8c9e-99760092c155)

## Model Building

Step 1:-
Turned every movie into a vector so that user can extract nearest neighbour movie vector which is the required similar output.
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/08e51972-b129-4707-b61c-2e1def2efea2)

Step 2:-
Defined a recommender function which will take a movie name as an input and retuyrn top 5 most similart movies' names as an output (recommendations)
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/07b5644b-40b3-43ec-8797-9e4c7dd98ca8)

### Storing Model and Data
Used pickle library to store data and similarity vector array.
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/3ba8989c-199f-4dcc-a104-3736582a84aa)

### Developing Main Python App

#### Backend
Using pickle to load dumped ML model and data
Using pandas to read and fetch the data
Using a special library "movieposters" to get real time high-quality movie posters so there must not be a need to store 5000 high-quality movie posters locally.
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/6ef9035c-941d-41ac-8667-55cc0fc2a0ea)

#### Frontend
Used Streamlit library to build a strong and visually appealing frontend.
![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/30614e0f-923c-48e5-bd4e-bb33a687420f)

## Movie Recommender System 

Working Demo Video Lnk- https://bit.ly/3E9DMoP

![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/56f99f42-bda8-4c26-8d67-9563fc580a27)

There is a selectbox on the project page using which user type in any movie name and then select it.
By clicking of the recommend button user gets top 5 similar movies in results.

![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/42da4279-0be7-4d48-a171-8c27dd83b47d)

![image](https://github.com/anmolkumarfromspn/Movie-Recommender-System/assets/128449996/7c0f79f6-e69b-46b5-9b6a-0a5aa269c8a8)

Recommendations are based on many factors like - Movie titles, Directors, Actors, Movie Descriptions, etc.

## Evaluation Metrics

This project model is working on the basis of cosine similary and nearest neighbour vector suggestion technique so no statistical model was trained over this dataset to achive this outcome. So getting accuracy score is not possible in this project but this project makes sure that the recommendations (outputs) are provided with the highest similarity to the input. 

## Tools used

![image](https://github.com/anmolkumarfromspn/Instahyre-Job-Analytics-Job-Finder/assets/128449996/541d02e0-3d09-4070-825d-f799e6367866)

## Future Scope

In the evolving landscape of entertainment, the Machine Learning Movie Recommender System aims to further enhance its capabilities. The future scope of this project includes a focus on advanced personalization techniques, delving into deeper user profiling to understand preferences on a granular level. Additionally, exploring the integration of emerging technologies like natural language processing and sentiment analysis for user reviews and feedback will contribute to a more holistic and accurate recommendation system, keeping users engaged and satisfied with their movie choices.

## Challenges

Learning NLTK Library and data preprocessing techniques to prepare the data for best model building can result in many ways or techniques. So choosing best techniques for this model among variuos available and applying them each and noticing accuracy manually was a real challenge in this project. 

## Key Learnings

1. NLTK Library
2. Cosine Similarity Index
3. Data Preprocessing
4. TFIDF/Count Vectorizer
5. Streamlit Library

## Conclusion

In conclusion, this Movie Recommender System project has successfully demonstrated the capability of machine learning in providing personalized movie recommendations. Through data collection, preprocessing, and the implementation of collaborative and content-based filtering techniques, we achieved accurate and relevant movie suggestions. The user-friendly interface allowed for seamless interaction, and while there is room for improvement, this project underscores the practicality and potential of recommendation systems in meeting the increasing demand for personalized content recommendations in the real world.

--------------------------------------------------------------------------------------------------

*Contact Mail: aktwenty5@gmail.com*

*Linkedin: https://bit.ly/45XlMKn*


