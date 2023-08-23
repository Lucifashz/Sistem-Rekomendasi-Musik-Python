import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


st.set_page_config(page_title="Rekomendasi Musik", layout="wide")

musics = pd.read_csv('new_df.csv')

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(musics['tags']).toarray()
similarity = cosine_similarity(vectors)


def fetch_track(uri):
    track = """<iframe src="https://open.spotify.com/embed/track/{}" width="260" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>""".format(
        (uri))
    return track


def recommend(music):
    music_index = musics[musics['artist_n_song'] == music].index[0]
    distances = similarity[music_index]
    musics_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:11]

    recommended_musics = []
    recommended_musics_tracks = []
    percentage_musics = []
    for i in musics_list:
        uri = musics.iloc[i[0]].uri

        percentage_musics.append(round(i[1], 2))
        recommended_musics.append(musics.iloc[i[0]].artist_n_song)
        # fetch track from URI
        recommended_musics_tracks.append(fetch_track(uri))
    return percentage_musics, recommended_musics, recommended_musics_tracks


st.title('Sistem Rekomendasi Musik')
selected_music_name = st.selectbox(
    'Masukkan lagu yang anda inginkan',
    musics['artist_n_song'].values)

if st.button('Recommend'):
    percentage, names, track = recommend(selected_music_name)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader(names[0])
        st.subheader(percentage[0])
        components.html(track[0], height=400,)

        st.subheader(names[3])
        st.subheader(percentage[3])
        components.html(track[3], height=400,)

        st.subheader(names[6])
        st.subheader(percentage[6])
        components.html(track[6], height=400,)

        st.subheader(names[9])
        st.subheader(percentage[9])
        components.html(track[9], height=400,)

    with col2:
        st.subheader(names[1])
        st.subheader(percentage[1])
        components.html(track[1], height=400,)

        st.subheader(names[4])
        st.subheader(percentage[4])
        components.html(track[4], height=400,)

        st.subheader(names[7])
        st.subheader(percentage[7])
        components.html(track[7], height=400,)

    with col3:
        st.subheader(names[2])
        st.subheader(percentage[2])
        components.html(track[2], height=400,)

        st.subheader(names[5])
        st.subheader(percentage[5])
        components.html(track[5], height=400,)

        st.subheader(names[8])
        st.subheader(percentage[8])
        components.html(track[8], height=400,)
