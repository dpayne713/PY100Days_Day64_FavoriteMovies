import requests
import os

class TheMovieDatabase():
    def __init__(self):
        self.v3key = os.environ['TMD_V3_KEY']
        self.v4key = os.environ['TMD_V4_KEY']
        self.endpoint = "https://api.themoviedb.org/3/search/movie"
        self.search_data = None

    def search_for_movie(self, movie_name, **kwargs):
        """searches for movie name returns list of id's"""
        year = kwargs.get('year', None)
        params= {
            "api_key": self.v3key,
            "language": "en-US",
            "query": movie_name,
            "year": year,
            "include_adult": True,
        }
        with requests.get(self.endpoint, params=params) as response:
            response.raise_for_status()
            data = response.json()['results']


        self.search_data = data[:10]

        return self.search_data

