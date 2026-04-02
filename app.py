import streamlit as st
import joblib

# Load data
data = joblib.load('movies.pkl')
similarity = joblib.load('similarity.pkl')

# =========================
# 🎨 NETFLIX STYLE CSS
# =========================
st.markdown("""
    <style>
    body {
        background-color: #141414;
        color: white;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: red;
    }
    .movie-card {
        background-color: #1f1f1f;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🎬 Netflix Style Recommender</div>', unsafe_allow_html=True)
st.write("Find movies similar to your taste 🍿")

# =========================
# SELECT MOVIE
# =========================
movie_list = data['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

# =========================
# RECOMMEND FUNCTION
# =========================
def recommend(movie):
    index = data[data['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommendations = []
    for i in movies_list:
        recommendations.append(data.iloc[i[0]].title)
    return recommendations

# =========================
# BUTTON
# =========================
if st.button("🍿 Recommend"):
    results = recommend(selected_movie)

    st.subheader("Top Picks For You")

    cols = st.columns(5)

    for i, movie in enumerate(results):
        with cols[i % 5]:
            st.markdown(f"""
                <div class="movie-card">
                    🎬 <br><br>
                    <b>{movie}</b>
                </div>
            """, unsafe_allow_html=True)