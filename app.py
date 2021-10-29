from Setup import config
import mysql.connector as connector

def main():
  conn = connector.connect(
    user = config.username,
    password = config.password,
    database = config.db)

  cur = conn.cursor()

  cur.execute("SELECT * FROM author")
  row = cur.fetchone()
  print(row)



  

if __name__ == "__main__":
    main()
