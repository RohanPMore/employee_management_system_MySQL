from modules.employee import add_employee, update_employee, delete_employee
from modules.department import add_department, get_all_departments
from modules.salary import calculate_payroll, generate_department_salary_report

def main_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Add Department")
    print("5. View All Departments")
    print("6. Calculate Payroll")
    print("7. Department Salary Report")
    print("8. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            department_id = int(input("Enter department ID: "))
            position = input("Enter position: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            salary = float(input("Enter salary: "))
            add_employee(first_name, last_name, email, department_id, position, hire_date, salary)

        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            first_name = input("Enter first name (leave blank to skip): ")
            last_name = input("Enter last name (leave blank to skip): ")
            email = input("Enter email (leave blank to skip): ")
            department_id = input("Enter department ID (leave blank to skip): ")
            position = input("Enter position (leave blank to skip): ")
            salary = input("Enter salary (leave blank to skip): ")

            update_employee(employee_id, first_name or None, last_name or None, email or None,
                            int(department_id) if department_id else None,
                            position or None,
                            float(salary) if salary else None)

        elif choice == '3':
            employee_id = int(input("Enter employee ID to delete: "))
            delete_employee(employee_id)

        elif choice == '4':
            department_name = input("Enter department name: ")
            add_department(department_name)

        elif choice == '5':
            departments = get_all_departments()
            print("\nDepartments:")
            for department in departments:
                print(f"ID: {department[0]}, Name: {department[1]}")

        elif choice == '6':
            calculate_payroll()

        elif choice == '7':
            generate_department_salary_report()

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
