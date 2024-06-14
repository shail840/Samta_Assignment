import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Shai8586023487",
    database="student_db"
)
cursor = conn.cursor()

# Update the student's grade
update_query = """
UPDATE students
SET grade = %s
WHERE first_name = %s;
"""
new_grade = (97.0, "Alice")
cursor.execute(update_query, new_grade)
conn.commit()

print("Record Updated Successfully!")