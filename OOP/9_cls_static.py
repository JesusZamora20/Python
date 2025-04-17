import math

class Cake:
    def __init__(self, ingredients, size):
        self.ingredients = ingredients
        self.size = size

    def __repr__(self):
        return (f'cake made of {self.ingredients} ,' f'size is {self.size}')

    def area(self): 
        return self.sizearea(self.size)
        
    @classmethod
    def chocolate_cake(cls):
        return cls(['powder','milk','chocolate'],2)

    @classmethod
    def vanilla_cake(cls):
        return cls(['powder','milk','vanilla'],3)

    @staticmethod
    def sizearea(a):
        return a ** 2 *math.pi
    

print(Cake.vanilla_cake())
newcake = Cake(['powder','milk','strawberries'],5)
print(newcake.ingredients, newcake.sizearea(3))
