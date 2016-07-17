from flask import Flask, render_template, jsonify, request
from werkzeug import secure_filename
import os
from models import *
#from twitter import * 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', text='', entites='')

@app.route('/get_data')
def get_data():
    filename = request.args.get('file')
    return jsonify(data=getFileData(filename))

'''
@app.route('/twitter')
def twitter():
    keyword = request.args.get('keyword')
    return jsonify(tweets=get_tweets(keyword))
'''

@app.route('/notes/', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join("files/", filename))
    response = extract_entity(filename)
    return render_template('index.html', text=response['text'], entities=response['entities'])
app.run(host='0.0.0.0', debug=True)


