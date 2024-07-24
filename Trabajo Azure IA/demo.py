import streamlit as st
import pandas as pd
import numpy as np
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment, Dataset


# Funciones para cargar datos
def load_rating_data(file):
    data = pd.read_csv(file)
    return data
def load_movie_data(file):
    data = pd.read_csv(file)
    return data


def generate_random_genres(num_movies):
    genres = ['Action', 'Drama', 'Comedy', 'Adventure', 'Horror']
    return np.random.choice(genres, num_movies)

def perform_clustering(df):
    from sklearn.cluster import KMeans
    

    kmeans = KMeans(n_clusters=3, random_state=0).fit(df[['Rating']])
    df['Cluster'] = kmeans.labels_
    
    return df

# Función para la interfaz administrativa
def interface_administrativa():
    st.title('Interfaz Administrativa - Recomendador de Películas')

    uploaded_rating_file = st.sidebar.file_uploader("Cargar archivo de Rating CSV", type=["csv"])
    uploaded_movie_file = st.sidebar.file_uploader("Cargar archivo de Películas CSV", type=["csv"])

    if uploaded_rating_file is not None and uploaded_movie_file is not None:
        st.sidebar.success('Archivos cargados correctamente!')
        df_ratings = load_rating_data(uploaded_rating_file)
        df_movies = load_movie_data(uploaded_movie_file)

        df = pd.merge(df_ratings, df_movies[['Movie_ID', 'Name', 'Year']], on='Movie_ID', how='left')
        df.drop_duplicates(inplace=True)

        if 'Genre' not in df.columns:
            df['Genre'] = generate_random_genres(len(df))

        st.subheader('Datos Cargados (Deduplicados):')
        st.write(df)

        st.subheader('Clustering de Películas Más Vistas:')
        df_clustered = perform_clustering(df)
        st.write(df_clustered[['Name', 'Rating', 'Cluster']])

        st.subheader('Recomendaciones por Categorías:')
        categories = df['Genre'].unique()
        selected_category = st.selectbox('Selecciona una categoría:', categories)
        recommended_movies = df[df['Genre'] == selected_category]['Name'].tolist()
        st.write(recommended_movies)

        st.subheader('Películas Más Vistas:')
        top_movies = df.sort_values(by='Rating', ascending=False)['Name'].head(10).tolist()
        st.write(top_movies)

# Función para la interfaz de usuario experimentado
def interface_usuario_experimentado():
    st.title('Interfaz Usuario Experimentado - Recomendador de Películas')

    uploaded_rating_file = st.sidebar.file_uploader("Cargar archivo de Rating CSV (Solo para visualización)", type=["csv"])
    uploaded_movie_file = st.sidebar.file_uploader("Cargar archivo de Películas CSV (Solo para visualización)", type=["csv"])

    if uploaded_rating_file is not None and uploaded_movie_file is not None:
        st.sidebar.success('Archivos cargados correctamente!')
        df_ratings = load_rating_data(uploaded_rating_file)
        df_movies = load_movie_data(uploaded_movie_file)

        df = pd.merge(df_ratings, df_movies[['Movie_ID', 'Name', 'Genre']], on='Movie_ID', how='left')

        st.subheader('Datos Cargados:')
        st.write(df)

        st.subheader('Recomendaciones por Categorías:')
        categories = df['Genre'].unique()
        selected_category = st.selectbox('Selecciona una categoría:', categories)
        recommended_movies = df[df['Genre'] == selected_category]['Name'].tolist()
        st.write(recommended_movies)

        st.subheader('Películas Más Vistas:')
        top_movies = df.sort_values(by='Rating', ascending=False)['Name'].head(10).tolist()
        st.write(top_movies)

# Función para la interfaz básica
def interface_basica():
    st.title('Interfaz Básica - Recomendador de Películas')

    df_movies = load_movie_data('movies_data.csv')
    df_ratings = load_rating_data('ratings_data.csv')

    df = pd.merge(df_ratings, df_movies[['Movie_ID', 'Name', 'Genre']], on='Movie_ID', how='left')

    st.subheader('Datos Cargados:')
    st.write(df)

    st.subheader('Recomendaciones por Categorías:')
    categories = df['Genre'].unique()
    selected_category = st.selectbox('Selecciona una categoría:', categories)
    recommended_movies = df[df['Genre'] == selected_category]['Name'].tolist()
    st.write(recommended_movies)

    st.subheader('Películas Más Vistas:')
    top_movies = df.sort_values(by='Rating', ascending=False)['Name'].head(10).tolist()
    st.write(top_movies)

# Función principal para seleccionar la interfaz
def main():
    st.sidebar.title('Selecciona una Interfaz')
    interface_option = st.sidebar.radio('', ('Administrativa', 'Usuario Experimentado', 'Básica'))

    if interface_option == 'Administrativa':
        interface_administrativa()
    elif interface_option == 'Usuario Experimentado':
        interface_usuario_experimentado()
    elif interface_option == 'Básica':
        interface_basica()

if __name__ == '__main__':
    main()
