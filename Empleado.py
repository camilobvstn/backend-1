from Persona import Persona
from Tienda import Tienda

class Empleado(Persona):
    def __init__(self, nombre: str, rut: str, edad: int,sueldo:int):
        super().__init__(nombre, rut, edad)
        self.__sueldo=sueldo
        self.__tienda=None

    def get_sueldo(self):
        return self.__sueldo
    def set_sueldo(self,sueldo:int):
        self.__sueldo=sueldo
        

    def get_tienda(self):
        return self.__tienda
    def set_tienda(self,tienda:Tienda):
        self.__tienda=tienda