from flask import Flask
import pymysql
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, JC!'

if __name__ == '__main__':
  app.run()
