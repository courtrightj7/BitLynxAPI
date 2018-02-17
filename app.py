from flask import Flask
import pymysql
app = Flask(__name__)

@app.route('/')
def hello_world():
  connection = pymysql.connect(host='35.224.87.205',
                             user='courtrightj7',
                             password='Omerta77!',
                             connect_timeout='1000',
                             db='BitLynx',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
  cursor = connection.cursor()
  sql = "SELECT `id`, `password` FROM `testtable` WHERE `email`=%s"
  cursor.execute(sql, ('webmaster@python.org',))
  result = cursor.fetchone()
  connection.close()
  return result

if __name__ == '__main__':
  app.run()


