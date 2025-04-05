class Person:

    def __init__(self, age, name, country):
        self.age = age
        self.name = name
        self.country = country
        self.atwork = False
    
    def description(self):
        return "{} has {} and lives in {}".format(self.name, self.age, self.country)
    
    def comment(self, phrase):
        return "{} said: {}".format(self.name, phrase)
    
    def work(self):
        self.atwork = True
    
engineer = Person(27, "Jesus", "Colombia")
print(engineer.description())
print(engineer.comment("Hello, how are you?"))

#modify an attribute
print(engineer.atwork)
engineer.work()
print(engineer.atwork)