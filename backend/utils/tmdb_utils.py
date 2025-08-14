import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
API_URL = os.getenv("TMDB_API_URL")

# Returns metadata for movie postercards
def get_tmdb_metadata(imdb_id):

    # Check API vars are available
    if not API_KEY or not API_URL: 
        print("Error: API params not found")
        return {
            "poster": "",
            "rating": "N/A",
            "overview": "Not found",
            "tmdb_id": ""
        }   

    #url = f"https://api.themoviedb.org/3/find/{imdb_id}"
    url = str(API_URL) + str(imdb_id)
    params = {
        "api_key": str(API_KEY),
        "external_source": "imdb_id"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("movie_results"):
        movie = data["movie_results"][0]
        return {
            "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}",
            "rating": movie.get("vote_average"),
            "overview": movie.get("overview", ""),
            "tmdb_id": movie.get("id")
        }

    return {
        "poster": "",
        "rating": "N/A",
        "overview": "Not found",
        "tmdb_id": ""
    }