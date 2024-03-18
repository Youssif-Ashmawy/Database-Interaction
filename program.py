import psycopg2
from psycopg2 import sql

# Function to establish connection to PostgreSQL database
def connect():
    conn = psycopg2.connect(
        dbname="your database name", # Database name
        user="your usename", # Username
        password="your password", # Password
        host="your host" # Host
    )
    return conn

# Function to retrieve all students from the database
def getAllStudents():
    conn = connect()  # Establish a connection to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute("SELECT * FROM students")  # Execute SQL query to select all students
    rows = cur.fetchall()  # Fetch all rows from the result set
    cur.close()  # Close the cursor
    conn.close()  # Close the database connection
    return rows

# Function to add a new student to the database
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()  # Establish a connection to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",  # Execute SQL query to insert a new student
                (first_name, last_name, email, enrollment_date))  # Pass parameters for the query
    conn.commit()  # Commit the transaction
    cur.close()  # Close the cursor
    conn.close()  # Close the database connection

# Function to update a student's email
def updateStudentEmail(student_id, new_email):
    conn = connect()  # Establish a connection to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s",  # Execute SQL query to update student's email
                (new_email, student_id))  # Pass parameters for the query
    conn.commit()  # Commit the transaction
    cur.close()  # Close the cursor
    conn.close()  # Close the database connection

# Function to delete a student from the database
def deleteStudent(student_id):
    conn = connect()  # Establish a connection to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute("DELETE FROM students WHERE student_id = %s",  # Execute SQL query to delete a student
                (student_id,))  # Pass parameters for the query
    conn.commit()  # Commit the transaction
    cur.close()  # Close the cursor
    conn.close()  # Close the database connection

# Test the functions
if __name__ == "__main__":
    # Current data stored in the student table 
    print("[Current data stored in the student table]")
    students = getAllStudents()  # Retrieve all students from the database
    for student in students:
        print(student)  # Print each student's information

    # Add a new student
    addStudent("Youssif", "Ashmawy", "youssif.ashmawy@example.com", "2023-09-03")

    print("-------------------------------------------------------------------------------------") # Seperate the old and new results
    # Current data stored in the student table after adding a new student called Youssif
    print("[Current data stored in the student table after adding a new student called Youssif]")
    students = getAllStudents()  # Retrieve all students from the database after modifications
    # Retrieve all students and print them
    for student in students:
        print(student)  # Print each student's information

    # Update a student's email
    updateStudentEmail(1, "john.doe.new@example.com")

    print("-------------------------------------------------------------------------------------") # Seperate the old and new results
    # Current data stored in the student table after updating student 1's email
    print("[Current data stored in the student table after updating student 1's email]")
    students = getAllStudents()  # Retrieve all students from the database after modifications
    # Retrieve all students and print them
    for student in students:
        print(student)  # Print each student's information

    # Delete a student
    deleteStudent(3)

    print("-------------------------------------------------------------------------------------") # Seperate the old and new results
    # Current data stored in the student table after deleting student 3 
    print("[Current data stored in the student table after deleting student 3]")
    students = getAllStudents()  # Retrieve all students from the database after modifications
    # Retrieve all students and print them
    for student in students:
        print(student)  # Print each student's information

    
