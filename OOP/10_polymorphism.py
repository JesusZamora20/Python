class Animals:
    def __init__(self, name):
        self.name = name

    def type(self):
        pass

class Lion(Animals):
    def type(self):
        print("savage animal")

class Dog(Animals):
    def type(self):
        print("Domestic animal")

new_animal = Lion("Alex")
new_animal.type()
        
