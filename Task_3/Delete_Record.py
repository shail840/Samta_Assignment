import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Shai8586023487",
    database="student_db"
)
cursor = conn.cursor()

# Delete the student record
delete_query = """
DELETE FROM students
WHERE last_name = %s;
"""
last_name_to_delete = ("Smith",)
cursor.execute(delete_query, last_name_to_delete)
conn.commit()

print("Record Deleted Successfully!")