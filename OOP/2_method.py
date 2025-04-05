#methods

class Mathematics:
    def add(self):
        self.n1 = 2
        self.n2 = 3

s = Mathematics()
s.add()

class Clothes:
    def __init__(self):
        self.brand = "Nike"
        self.size = "M"
        self.color = "Black"

shoe = Clothes()
print(shoe.brand)
print(shoe.size)
print(shoe.color)
#----------------------

class Calculator:
    def __init__ (self, n1, n2):
        self.add = n1 + n2
        self.substract = n1 - n2
        self.multiply = n1 * n2
        self.divide = n1 / n2

operation = Calculator(4,2)
print(operation.add)
print(operation.substract)
print(operation.multiply)
print(operation.divide)







