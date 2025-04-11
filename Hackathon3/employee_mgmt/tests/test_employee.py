import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):

    def setUp(self):
        # Common employee used across multiple tests
        self.emp = Employee("TestUser", "TestDept", "Tester", 30000.0, 10.0, 5000.0)
### Test if net salary is correctly calculated as:gross_salary - tax + bonus
    def test_net_salary_calculation(self):
        expected_net = 30000.0 - 10.0 + 5000.0
        self.assertEqual(self.emp.net_salary, expected_net)
## Test that each Employee instance gets a unique ID and it's of string type.
    def test_unique_id_generated(self):
        emp2 = Employee("Another", "Dept", "Dev", 25000, 10, 5000)
        self.assertNotEqual(self.emp.id, emp2.id)
        self.assertTrue(isinstance(self.emp.id, str))
## Test the __str__ method for readable string output of Employee
    def test_string_representation(self):
        result = str(self.emp)
        self.assertIn("Name: TestUser", result)
        self.assertIn("Department: TestDept", result)
        self.assertIn("Net Salary:", result)
### Ensure important attributes have correct data types
    def test_data_types(self):
        self.assertIsInstance(self.emp.gross_salary, float)
        self.assertIsInstance(self.emp.tax, float)
        self.assertIsInstance(self.emp.bonus, float)
        self.assertIsInstance(self.emp.net_salary, float)

if __name__ == '__main__':
    unittest.main()