import os
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from datetime import datetime
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

try:
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
except:
    pass
 
app = Flask(__name__)
api = Api(app)

@app.route('/', methods = ['GET'])
def Test():
    if request.method == 'GET':
        if conn:
            message = 'Successful'
        else:
            message = 'Unsuccessful'

        
if __name__ == '__main__':
     app.run()



