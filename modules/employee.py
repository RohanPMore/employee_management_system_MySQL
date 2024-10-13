from db.database import Database

def add_employee(first_name, last_name, email, department_id, position, hire_date, salary):
    db = Database()
    query = '''
    INSERT INTO Employees (first_name, last_name, email, department_id, position, hire_date, salary)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    db.execute_query(query, (first_name, last_name, email, department_id, position, hire_date, salary))
    db.close()
    print(f"Employee '{first_name} {last_name}' added successfully!")

def update_employee(employee_id, first_name=None, last_name=None, email=None, department_id=None, position=None, salary=None):
    db = Database()
    query = "UPDATE Employees SET "
    fields = []
    params = []
    
    if first_name:
        fields.append("first_name = %s")
        params.append(first_name)
    if last_name:
        fields.append("last_name = %s")
        params.append(last_name)
    if email:
        fields.append("email = %s")
        params.append(email)
    if department_id:
        fields.append("department_id = %s")
        params.append(department_id)
    if position:
        fields.append("position = %s")
        params.append(position)
    if salary:
        fields.append("salary = %s")
        params.append(salary)

    query += ", ".join(fields) + " WHERE employee_id = %s"
    params.append(employee_id)
    db.execute_query(query, tuple(params))
    db.close()
    print(f"Employee with ID {employee_id} updated successfully!")

def delete_employee(employee_id):
    db = Database()
    query = 'DELETE FROM Employees WHERE employee_id = %s'
    db.execute_query(query, (employee_id,))
    db.close()
    print(f"Employee with ID {employee_id} deleted successfully!")
