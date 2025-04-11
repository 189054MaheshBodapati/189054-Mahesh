from employee import Employee
from employee_manager import EmployeeManager
import storage

def main():
    manager = EmployeeManager()
    manager.employees = storage.load_from_file()

    while True:
        print("\nEmployee Management CLI Application")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Delete Employee")
        print("5. Save & Exit")

        choice = input("Enter choice: ")
# Add the employee details
        if choice == '1':
            name = input("Name: ")
            department = input("Department: ")
            designation = input("Designation: ")
            gross = float(input("Gross Salary: "))
            tax = float(input("Tax: "))
            bonus = float(input("Bonus: "))
            emp = Employee(name, department, designation, gross, tax, bonus)
            manager.add_employee(emp)
            print("Employee added successfully!")
# View all the employee details using choice 2
        elif choice == '2':
            employees = manager.view_all_employees()
            if not employees:
                print("No employees found.")
            for emp in employees:
                print("\n" + str(emp))
# search using employee ID to get the employee details
        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            emp = manager.search_by_id(emp_id)
            if emp:
                print(emp)
            else:
                print("Employee not found.")
# delete the employee details
        elif choice == '4':
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)
            print("Employee deleted (if existed).")
# save all the employee details and exit 
        elif choice == '5':
            storage.save_to_file(manager.employees)
            print("Data saved. Exiting...")
            break
# To handle the invalid input
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()