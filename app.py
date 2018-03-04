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
connection = pymysql.connect(host='us-cdbr-iron-east-05.cleardb.net',
                             user='b38e4d31767903',
                             password='c17681',
                             db='heroku_4c8e33f241f2945',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/test', methods = ['GET'])
def Test():
    if request.method == 'GET':
        message = str(DATABASE_URL)
        returrn message 
        
if __name__ == '__main__':
     app.run()



