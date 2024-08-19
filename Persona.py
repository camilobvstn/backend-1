class Persona:
    def __init__(self,nombre:str, rut:str,edad:int):
        self.__nombre=nombre
        self.__rut=rut
        self.__edad=edad
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre:str):
        self.__nombre=nombre
    
    def get_rut(self):
        return self.__rut
    def set_rut(self,rut:str):
        self.__rut=rut

    def get_edad(self):
        return self.__edad
    def set_edad(self,edad:int):
        self.__edad=edad



