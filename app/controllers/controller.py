# file main 
# created by: mbdrian on Aug 20, 2018

from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html", title = 'ToyStory')