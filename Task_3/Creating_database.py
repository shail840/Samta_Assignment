import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Shai8586023487",
    database="student_db"
)
cursor = conn.cursor()