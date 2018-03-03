from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from datetime import datetime

e = create_engine('sqlite:///test.db')
app = Flask(__name__)
api = Api(app)


class test(Resource):
    def get(self):
        # Connect to databse
        conn = e.connect()
        # Perform query and return JSON data
        query = conn.execute("select Name from test")
        x = query.cursor.fetchall()
        conn.close()
        return {'name': [i[0] for i in x]}


api.add_resource(test, '/test')

if __name__ == '__main__':
     app.run()



