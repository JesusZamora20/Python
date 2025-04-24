class Mamifero:
    def __init__(self, name):
        print(name, " es un animal de sangre caliente")

class Perro(Mamifero):
    def __init__(self):
        print("El perro es el mejor amigo del hombre")
        super().__init__("bobby")

nuevo_perro = Perro()
