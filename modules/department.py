from db.database import Database

def add_department(department_name):
    db = Database()
    query = '''
    INSERT INTO Departments (department_name)
    VALUES (%s)
    '''
    db.execute_query(query, (department_name,))
    db.close()
    print(f"Department '{department_name}' added successfully!")

def get_all_departments():
    db = Database()
    query = 'SELECT * FROM Departments'
    departments = db.fetch_query(query)
    db.close()
    return departments
