import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

data = pd.read_csv('movies.csv')

data['genre'] = data['genre'].fillna('')

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['genre'])

similarity = cosine_similarity(tfidf_matrix)

joblib.dump(similarity, 'similarity.pkl')
joblib.dump(data, 'movies.pkl')

print("✅ Model prepared successfully!")