import mysql.connector

def create_database():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',   # Your MySQL username
        password='password'  # Your MySQL password
    )
    cursor = conn.cursor()

    # Create Database
    cursor.execute("CREATE DATABASE IF NOT EXISTS employee_management")
    cursor.execute("USE employee_management")

    # Create Employees Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        employee_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100) UNIQUE,
        department_id INT,
        position VARCHAR(100),
        hire_date DATE,
        salary DECIMAL(10, 2),
        FOREIGN KEY (department_id) REFERENCES Departments(department_id)
    )
    ''')

    # Create Departments Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        department_id INT AUTO_INCREMENT PRIMARY KEY,
        department_name VARCHAR(100)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
