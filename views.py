from flask import render_template
from app import app

@app.route('/')
def index():
    return "True"
    # return render_template('index.html')

