from distutils.debug import DEBUG


class Config:
    pass
    NEW_API_URL = 'https://api.newsapi.org/3/news/{}?api_key={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True