import collections
import requests

MovieResult = collections.namedtuple(
    'MovieResult', "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")


def search_movies(search_text):
    if not search_text or not search_text.strip():
        raise ValueError()

    url = f'http://movie_service.talkpython.fm/api/search/{search_text}'

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    movies.sort(key=lambda m: -m.year)

    return movies
