import unittest
import os
import storage
from employee import Employee

class TestStorage(unittest.TestCase):

    def setUp(self):
        # Setup test data and file name
        self.emp1 = Employee("Test User", "QA", "Tester", 30000.0, 10.0, 5000.0)
        self.emp2 = Employee("Another User", "Dev", "Developer", 40000.0, 1000.0, 3000.0)
        self.test_file = "test_employees.pkl"

    def test_save_and_load_single_employee(self):
        ##Test saving and loading a single employee
        storage.save_to_file([self.emp1], filename=self.test_file)
        loaded = storage.load_from_file(filename=self.test_file)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, self.emp1.name)

    def test_save_and_load_multiple_employees(self):
        ### Test saving and loading multiple employees
        storage.save_to_file([self.emp1, self.emp2], filename=self.test_file)
        loaded = storage.load_from_file(filename=self.test_file)
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[1].designation, "Developer")

    def test_file_creation_on_save(self):
        ### Test that file is actually created when saving
        storage.save_to_file([self.emp1], filename=self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_load_from_nonexistent_file(self):
        ### Test loading from a non-existent file returns empty list
        fake_file = "no_such_file.pkl"
        result = storage.load_from_file(filename=fake_file)
        self.assertEqual(result, [])

    def tearDown(self):
        # Cleanup after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()