import os
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from datetime import datetime
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
 
app = Flask(__name__)
api = Api(app)

@app.route('/', methods = ['POST'])
def Test():
    if request.method == 'POST':
        message = str(DATABASE_URL)
        returrn message 
        
if __name__ == '__main__':
     app.run()



