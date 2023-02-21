import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Qwerty@21",
  database="resource_monitoring"
)

print("Database successfully connected...")