#initialising the app
from flask import Flask, app

app = Flask(__name__)

from app import views