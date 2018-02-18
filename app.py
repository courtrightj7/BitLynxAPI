from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
app = Flask(__name__)

@app.route('/')
def hello_world():)
  return "Hello World"

if __name__ == '__main__':
  app.run()


