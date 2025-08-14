import pandas as pd
import numpy as np
import math
import re
import pickle

from scipy.sparse import csr_matrix, hstack

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load model and data
with open("models/movie_recommender.pkl", "rb") as f:
    recommender = pickle.load(f)

model = recommender['model']
features = recommender['features']
df = recommender['df']


def recommend(title, n=10):
    
    # Account for case
    title_lower=title.lower()
    title_series = df['title'].str.lower()

   # Find matching index
    matches = title_series[title_series == title_lower]

    if matches.empty:
        print(f"Movie '{title}' not found in dataset.")

        
        partial_matches = title_series[title_series.str.contains(title_lower[:4])]

        if not partial_matches.empty:
            print("\n🔍 Did you mean:")
            suggestions = df.loc[partial_matches.index, 'title'].tolist()
            for title in suggestions[:5]:
                print(f"  - {title}")
            
        return []


    # Get the correct index using the lowercased match
    movie_index = matches.index[0]
    
    # Get recommendations
    distances, indices = model.kneighbors(features[movie_index], n_neighbors=n + 1)

    # Output recommended movies
    results = df.iloc[indices[0][1:]]['title'].tolist()
    print(f"\n Recommendations for '{title}':")
    for i, title in enumerate(results, 1):
        print(f"{i}. {title}")
    return results


if __name__ == "__main__":

    while True:
        movie = input("Enter a movie title: ")
        recommend(movie, n=10)