#OOP

class Employee(object):
    "Employee Class"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def introduce(self):
        print(self.name+" gets a salary of "+str(self.salary))
        
        
john = Employee("John",50000)
john.introduce()