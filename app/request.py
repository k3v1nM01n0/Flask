from app import app
import urllib.request, json
from .models import movie

movie = movie.Movie

api_key = app.config['MOVIE_API_KEY']
base_url = app.config("MOVIE_API_BASE_URL")