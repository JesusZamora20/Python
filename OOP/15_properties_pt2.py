class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def __getname(self):
        return self.__name
    def __getsalary(self):
        return self.__salary
    
    def __setname(self, name):
        self.__name = name
    def __setsalary(self, salary):
        self.__salary = salary

    def __delname(self):
        del self.__name
    def __delsalary(self):
        del self.__salary

    name = property(fget= __getname,
                        fset= __setname,
                        fdel= __delname,
                        doc="This is the name of the employee")

    salary = property(fget= __getsalary)

employee_one = Employee("Juan", 1000)
employee_two = Employee("Pedro", 2000)

employee_one.name = "Jose"

print(employee_one.name, "," ,employee_one.salary)


