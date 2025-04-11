class EmployeeManager:
    def __init__(self):
        self.employees = []
# Add the employee details
    def add_employee(self, employee):
        self.employees.append(employee)
# View all the employee details
    def view_all_employees(self):
        return self.employees
# search the employee details using ID
    def search_by_id(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None
# Delete employee details 
    def delete_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.id != emp_id]