import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Shai8586023487",
    database="student_db"
)
cursor = conn.cursor()

# Fetch and display all student records
select_query = "SELECT * FROM students;"
cursor.execute(select_query)
students = cursor.fetchall()

print("Record Fetched Successfully!")

for student in students:
    print(student)

# Close the cursor and connection
cursor.close()
conn.close()