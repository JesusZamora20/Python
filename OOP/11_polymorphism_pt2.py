# Polymorphism by funciton

class Tomato:
    def type(self):
        print("vegetable")
    def color(self):
        print("red")

class Apple:
    def type(self):
        print("fruit")
    def color(self):
        print("green")
    
def function(obj):
    obj.type()
    obj.color()

new_apple = Apple()
new_tomato = Tomato()
function(new_apple)
function(new_tomato)

#polymorphism by methods
print("-----------------")
class Colombia:
    def capital(self):
        print("Bogota")
    def language(self):
        print("Spanish")

class Brazil:
    def capital(self):
        print("Brasilia")
    def language(self):
        print("Portuguese")

colombian = Colombia()
brazilian = Brazil()

for country in (colombian, brazilian):
    country.capital()
    country.language()


print("-----------------")

#polymorphism by inheritance
class birds:
    def fly(self):
        print("most of the birds can fly")

class parrot(birds):
    def fly(self):
        print("parrots can fly")

class penguin(birds):
    def fly(self):
        print("penguins cannot fly")

bird = birds()
parrot = parrot()
penguin = penguin()

bird.fly()
parrot.fly()
penguin.fly()
