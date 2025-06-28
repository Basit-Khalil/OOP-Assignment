class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Basit", 50000, "123-45-6789")

print("Public Name:", emp.name)

print("Protected Salary:", emp._salary)

try:
    print("Private SSN:", emp.__ssn)
except AttributeError:
    print("Private SSN: Cannot access directly!")

print("Private SSN (via name mangling):", emp._Employee__ssn)