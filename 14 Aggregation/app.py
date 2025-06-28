class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_employee_details(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def show_department_details(self):
        print(f"Department: {self.department_name}")
        self.employee.show_employee_details()

# Creating Employee object
employee1 = Employee("Basit Khalil", "Software Engineer")

department1 = Department("IT", employee1)

department1.show_department_details()