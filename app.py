import os
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from datetime import datetime
import pymysql
from sqlalchemy import create_engine

DATABASE_URL = os.environ['DATABASE_URL']
#DATABASE_URL = 'TEST'
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')
 
app = Flask(__name__)
api = Api(app)
e = create_engine('mysql://b38e4d31767903:c17681@us-cdbr-iron-east-05.cleardb.net/heroku_4c8e33f241f2945')

@app.route('/test', methods = ['GET'])
def Test():
    if request.method == 'GET':
        message = str(DATABASE_URL)
        return message 
        
if __name__ == '__main__':
     app.run()



