import pickle
import pandas as pd
import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from utils.tmdb_utils import get_tmdb_metadata

# Paths
MODEL_PATH = os.path.join(os.path.dirname(__file__), '.', 'models')

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)
CORS(app)

# Models and data
with open(os.path.join(MODEL_PATH, "movie_recommender.pkl"), "rb") as f:
    recommender = pickle.load(f)

model = recommender['model']
features = recommender['features']
df = pd.read_csv('./resources/imdb_filtered.csv')


@app.route('/recommend', methods=['POST'])
@limiter.limit("10 per minute")
@limiter.limit("50 per hour")
def recommend():
    data = request.get_json()
    movie_title = data.get('movie')

    if not movie_title:
        return jsonify({'error': 'Missing movie title'}), 400

    recommendations = _gather_recommendations(movie_title)

    # Collect recommendations metadata
    results = []
    for title in recommendations:
        row = df[df['title'] == title].iloc[0]
        imdb_id = row['imdb_id']

        meta = get_tmdb_metadata(imdb_id)
        meta['title'] = title
        meta['imdb_id'] = imdb_id
        results.append(meta)

    return jsonify({'recommendations': results})

# Use model to find n recommendations
def _gather_recommendations(movie_title, n=10):
    title_lower = movie_title.lower()
    title_series = df['title'].str.lower()

    matches = title_series[title_series == title_lower]

    if matches.empty:
        print(f"Movie '{movie_title}' not found in dataset.")
        return []

    movie_index = matches.index[0]
    _, indices = model.kneighbors(features[movie_index], n_neighbors=n + 1)
    return df.iloc[indices[0][1:]]['title'].tolist()

if __name__ == '__main__':
    app.run(debug=True)