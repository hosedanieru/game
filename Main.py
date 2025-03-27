from Warrior import warrior
from Sorcerer import sorcerer
from Sword import sword
from Magic import magic

#CREAR PERSONAJES
guerrero = warrior("Andres", 100)
hechicero = sorcerer("Daniel", 80)

#CREAR OBJETOS
espada = sword("Excalibur", 20)
conjuro = magic("Armagedon", 30)

#EQUIPAR
guerrero.Weapon(espada)
hechicero.aprender_enchantment(conjuro)

#ACCIONES
guerrero.Atack(hechicero)
hechicero.atack_enchantment(guerrero)

