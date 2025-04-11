import uuid
class Employee:
    def __init__(self, name, department, designation, gross_salary, tax, bonus):
        self.id = str(uuid.uuid4()) # to get random employee ID using uuid
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = self.calculate_net_salary()
# to calculate the net salary
    def calculate_net_salary(self):
        return self.gross_salary - self.tax + self.bonus
    def __str__(self):
        return (f"ID: {self.id}\nName: {self.name}\nDepartment: {self.department}"
                f"\nDesignation: {self.designation}\nGross Salary: {self.gross_salary}"
                f"\nTax: {self.tax}\nBonus: {self.bonus}\nNet Salary: {self.net_salary}")