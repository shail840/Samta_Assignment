import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Shai8586023487",
    database="student_db"
)
cursor = conn.cursor()

# Create a new student record
insert_query = """
INSERT INTO students (first_name, last_name, age, grade)
VALUES (%s, %s, %s, %s);
"""
student_data = ("Alice", "Smith", 18, 97)
cursor.execute(insert_query, student_data)
conn.commit()

print("Record Inserted Successfully!")