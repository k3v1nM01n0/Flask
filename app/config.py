class Config:
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True 