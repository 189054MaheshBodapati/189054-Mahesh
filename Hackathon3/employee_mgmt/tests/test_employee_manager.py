import unittest
from employee import Employee
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.manager = EmployeeManager()
        self.emp1 = Employee("Bodapati", "WSIV", "Tester", 30000.0, 10.0, 5000.0)
        self.emp2 = Employee("Prathiksha", "WSIV", "Graphics Validation Engineer", 25000.0, 10.0, 5000.0)
        self.manager.add_employee(self.emp1)
        self.manager.add_employee(self.emp2)
## Test if employees are correctly added to the manager
    def test_add_employee(self):
        self.assertEqual(len(self.manager.employees), 2)
        self.assertIn(self.emp1, self.manager.employees)
## Test the search_by_id function to find the correct employee
    def test_search_employee_by_id(self):
        found_emp = self.manager.search_by_id(self.emp1.id)
        self.assertIsNotNone(found_emp)
        self.assertEqual(found_emp.name, "Bodapati")
## Test if an employee can be deleted by ID
    def test_delete_employee(self):
        self.manager.delete_employee(self.emp1.id)
        self.assertIsNone(self.manager.search_by_id(self.emp1.id))
        self.assertEqual(len(self.manager.employees), 1)
## Test if all employees can be viewed and are of correct type
    def test_view_all_employees(self):
        all_emps = self.manager.view_all_employees()
        self.assertEqual(len(all_emps), 2)
        self.assertTrue(all(isinstance(emp, Employee) for emp in all_emps))

if __name__ == "__main__":
    unittest.main()