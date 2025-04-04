#classes

class Auto:
    brand = ""
    model = 2004
    plate = ""

taxi = Auto()
print(taxi.model)

#----------------------
class Jugadores:
    j1 = "Messi"
    j2 = "Cristiano"

class Jugadores2:
    j1 = "James"
    j2 = "Bale"

#----------------------

class Nombre:
    pass

jesus = Nombre()
yola = Nombre()

jesus.edad = 20
jesus.sexo = "Masculino"
jesus.pais = "Colombia"

yola.edad = 19
yola.sexo = "Femenino"  
yola.pais = "venezuela"

print(jesus.edad, jesus.sexo, jesus.pais)
