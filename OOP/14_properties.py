class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def getname(self):
        return self.__name
    def getsalary(self):
        return self.__salary
    
    def setname(self, name):
        self.__name = name
    def setsalary(self, salary):
        self.__salary = salary

    def delname(self):
        del self.__name
    def delsalary(self):
        del self.__salary


employee_one = Employee("Juan", 1000)
employee_two = Employee("Pedro", 2000)
print(employee_one.getname(), "," ,employee_one.getsalary())
print(employee_two.getname(), "," ,employee_two.getsalary())

employee_one.setname("Jose")
employee_one.setsalary(1500)
print(employee_one.getname(), "," ,employee_one.getsalary())



