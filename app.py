from Setup import config
from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)
mysql = MySQL(user=config.username, password=config.password, db=config.db)
mysql.init_app(app)
 
@app.route("/")
def index():
  cur = mysql.get_db().cursor()
  cur.execute("SELECT * FROM author")
  res = cur.fetchone()
  cur.close()
  print(res)
  return ("<p>Hello World! " + res[1] + " </p>")
