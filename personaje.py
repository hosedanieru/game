class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        
    def damage(self, cantidad):
        self.salud -= cantidad
        print(f"{self.nombre} ha recibido {cantidad} de daño. Salud: {self.salud}")
        
    def Con_vida(self):
        return self.salud > 0
    
    def __str__(self):
        return f"Personaje: {self.nombre}, Salud: {self.salud}"