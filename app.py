from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from datetime import datetime

e = create_engine('sqlite:///BitLynx.db')
app = Flask(__name__)
api = Api(app)

@app.route('/Login', methods = ['POST'])
def Login():
 
    if request.method == 'POST':
        data = request.form # a multidict containing POST data
        username = str(data['username'])
        password = str(data['password'])
        
        conn = e.connect()
        # Perform query and return JSON data
        SQL = "select CustomerID from LoginTable where UserName = '" + username + "' and Password = '" + password +"'"
        
        query = conn.execute(SQL)
        x = query.cursor.fetchall()
        conn.close()
        return str(type(x))
        #if len(x) > 0:
        #    return {'CustomerID': [i[0] for i in x]}
        #else:
        #    return {'message': 'User does not exist'}

if __name__ == '__main__':
     app.run()



