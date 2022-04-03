from flask import Flask, jsonify, request
import pandas as pd 
import os
from flask_cors import CORS

os.system('cls')

app = Flask(__name__)
CORS(app)

df = pd.read_csv('final.csv')

data = [{
    'name' : df['original_title'].tolist(),
    'genres' : df['genres'].tolist(),
    'director' : df['director'].tolist(),
    'poster-link' : df['poster_link'].tolist()
}]

@app.route('/getmoviesdetails')
def getmoviesdetails():
    return jsonify({
        'data' : data
    })

if (__name__ == '__main__'):
    app.run(debug=True)