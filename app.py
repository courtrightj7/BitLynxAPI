import os
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from datetime import datetime
import pymysql

DATABASE_URL = os.environ['DATABASE_URL']
#DATABASE_URL = 'TEST'
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')
 
app = Flask(__name__)
api = Api(app)

@app.route('/test', methods = ['GET'])
def Test():
    if request.method == 'GET':
        message = str(DATABASE_URL)
        return message 
        
if __name__ == '__main__':
     app.run()



