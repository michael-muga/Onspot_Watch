from distutils.debug import DEBUG


class Config:
    pass
    NEWS_API_URL = 'https://newsapi.org/v2/{}?q=apple&from=2022-02-27&to=2022-02-27&sortBy=popularity&apikey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True