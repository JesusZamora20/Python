course = 'python'
print("Tutorials of % s"%course)

name = "Victor"
age = 25
print("hi, my name is % s and i'm % s years old"%(name,age))
print("Whats up, i am {} and my age is {}".format(name,age))
print(f"Whats up, i am {name} and my age is {age}")

class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"The student name is {self.name} {self.lastname} and the age is {self.age}."

student = Student("jesus", "bermudez", 23)
print(f"{student}")
