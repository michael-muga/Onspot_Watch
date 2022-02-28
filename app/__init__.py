#initialising the app
from ensurepip import bootstrap
from flask import Flask, app
from .config import DevConfig
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=True)

#setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

from app import views