#initialising the app
from flask import Flask, app
from .config import DevConfig
app = Flask(__name__)

#setting up configurations
app.config.from_object(DevConfig)

from app import views