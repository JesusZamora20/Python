class Pokemon:
  pass
  def __init__(self, name, type):
    self.name = name
    self.type = type

  def description(self):
    return '{} is a pokemon type {}'.format(self.name, self.type)

class Pikachu(Pokemon):
  def attack(self, attacktype):
    return "{} attck type {}".format(self.name, attacktype)

class Charmander(Pokemon):
  def attack(self, attacktype):
    return "{} attack type {}".format(self.name, attacktype)

new_pokemon = Pikachu('jesu', 'electric')
print(new_pokemon.description())
print(new_pokemon.attack('impactrueno'))
    
