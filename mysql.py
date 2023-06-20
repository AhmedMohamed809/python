import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Kmona",
  password="12345"
)

print(mydb)