#creating index page view function
from ast import excepthandler
from flask import render_template
from app import app

@app.route('/')
def index():

    Title = "Home - Get the latest and Upto date news as they happen from all around the world"
    return render_template('index.html',title = Title)

@app.route('/news/<int:news_id>')
def news(news_id):

    return render_template('news.html',id = news_id)