from Setup import config
from flaskext.mysql import MySQL
from flask import Flask
from queries import *

app = Flask(__name__)
mysql = MySQL(user=config.username, password=config.password, db=config.db)
mysql.init_app(app)
 
def execute_query(query):
  cur = mysql.get_db().cursor()
  cur.execute(query)
  response = cur.fetchall()
  cur.close()
  return list(response)

@app.route("/author/id/<int:id>")
def get_author_by_id(id):
  query = select_all_where_author_id(id)
  result = execute_query(query)
  return str(result)

@app.route("/students/id/<int:student_id>")
def get_student_by_id(student_id):
  query = select_all_where_student_id(student_id)
  result = execute_query(query)
  return str(result)

@app.route("/book/name/<string:bookname>")
def get_books_by_name(bookname):
  query =  select_all_where_book_name(bookname)
  result = execute_query(query)
  return str(result)

@app.route("/loans/id/<int:id>")
def get_loan_by_id(id):
  query = select_all_where_loan_id(id)
  result = execute_query(query)
  return str(result)

@app.route("/loans")
def get_all_loans():
  query = select_all_loans_where_not_returned()
  result = execute_query(query)
  return str(result)