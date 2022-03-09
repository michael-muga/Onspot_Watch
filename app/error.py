from flask import render_template
from app import app

@app.errorhandler(404)
def page_error(error):

    return render_template('pageerror.html'),404