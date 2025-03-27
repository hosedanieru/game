from personaje import Personaje
class sorcerer(Personaje):
    def __init__(self, nombre, salud):
        super().__init__(nombre, salud)
        self.enchantments = []
        
    def aprender_enchantment(self, enchantment):
        self.enchantments.append(enchantment)
        print(f"{self.nombre} ha aprendido {enchantment.nombre}")
        
    def atack_enchantment(self, objetivo):
        if self.enchantments:
            enchatment = self.enchantments[0]
            print(f"{self.nombre} lanza {enchatment.nombre}")
            objetivo.damage(enchatment.poder)
        else:
            print(f"{self.nombre} no tiene conjuros")