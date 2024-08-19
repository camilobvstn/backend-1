from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre: str, rut: str, edad: int):
        super().__init__(nombre, rut, edad)
    