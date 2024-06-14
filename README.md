## Task 1: Calculate Area with Conditions
 ![Database Created](Task_1/Output.png)




## Task 2: Generate Fibonacci Series
![Database Created](Task_2/Output.png)







## Task 3: MySQL Database Operations with Python

1. Creating Database using SQL commands in MySQL database.
    ```
    CREATE DATABASE student_db;
    ```
    ![Database Created](Task_3/Created_Database.png)
2. Creating Tables in Database.
   ```
   USE student_db;
   ```
   ```
   CREATE TABLE students (student_id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(50),last_name VARCHAR(50),age INT,grade DECIMAL(5,2));
   ```
    ![Tables_created](Task_3/Creating_tables.png)

3. Executing the Insert_query and adding the first record into the database table.
    ![Database Created](Task_3/Inserting_data.png)

4. Executiing the update_query to update the Record.
    ![Database Created](Task_3/Updating_data.png)

5. Executing the Delete_query to delete the same Record.
    ![Database Created](Task_3/Deleted_the_updated_data.png)

6. Fetching all the data by executing the fetch_query.py file.
    ![Database Created](Task_3/Fetching_record.png)
