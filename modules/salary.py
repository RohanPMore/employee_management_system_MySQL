from db.database import Database

def calculate_payroll():
    db = Database()
    query = '''
    SELECT first_name, last_name, salary
    FROM Employees
    '''
    employees = db.fetch_query(query)
    db.close()

    print("\nPayroll Report:")
    print("=================")
    for employee in employees:
        print(f"{employee[0]} {employee[1]}: ${employee[2]:,.2f}")

def generate_department_salary_report():
    db = Database()
    query = '''
    SELECT Departments.department_name, SUM(Employees.salary) AS total_salary
    FROM Employees
    JOIN Departments ON Employees.department_id = Departments.department_id
    GROUP BY Departments.department_name
    '''
    report = db.fetch_query(query)
    db.close()

    print("\nDepartment Salary Report:")
    print("===========================")
    for department in report:
        print(f"Department: {department[0]}, Total Salary: ${department[1]:,.2f}")
