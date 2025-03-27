from personaje import Personaje


class warrior(Personaje):
    def __init__(self, nombre, salud):
        super().__init__(nombre, salud)
        self.arma = None
        
    def Weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.nombre} ha equipado : {weapon.nombre}")
        
    def Atack(self, objetivo):
        if self.weapon:
            print(f"{self.nombre} ataca con {self.weapon.nombre}")
            objetivo.damage(self.weapon.damagef)
        else:
            print(f"{self.nombre} no tiene arma equipada")