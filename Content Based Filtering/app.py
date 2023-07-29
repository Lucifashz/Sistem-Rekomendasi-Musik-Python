import streamlit as st
import pickle
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="Rekomendasi Musik", layout="wide")


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

        percentage_musics.append(i[1])
        recommended_musics.append(musics.iloc[i[0]].artist_n_song)
        # fetch track from URI
        recommended_musics_tracks.append(fetch_track(uri))
    return percentage_musics, recommended_musics, recommended_musics_tracks


musics_dict = pickle.load(open('music_dict.pkl', 'rb'))
musics = pd.DataFrame(musics_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Music Recommender System')

selected_music_name = st.selectbox(
    'Masukkan lagu yang anda inginkan',
    musics['artist_n_song'].values)

if st.button('Recommend'):
    percentage, names, track = recommend(selected_music_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.text(percentage[0])
        components.html(track[0], height=400,)

        st.text(names[5])
        st.text(percentage[6])
        components.html(track[5], height=400,)

    with col2:
        st.text(names[1])
        st.text(percentage[1])
        components.html(track[1], height=400,)

        st.text(names[6])
        st.text(percentage[6])
        components.html(track[6], height=400,)

    with col3:
        st.text(names[2])
        st.text(percentage[2])
        components.html(track[2], height=400,)

        st.text(names[7])
        st.text(percentage[7])
        components.html(track[7], height=400,)

    with col4:
        st.text(names[3])
        st.text(percentage[3])
        components.html(track[3], height=400,)

        st.text(names[8])
        st.text(percentage[8])
        components.html(track[8], height=400,)

    with col5:
        st.text(names[4])
        st.text(percentage[4])
        components.html(track[4], height=400,)

        st.text(names[9])
        st.text(percentage[9])
        components.html(track[9], height=400,)
