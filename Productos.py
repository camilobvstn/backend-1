from Tienda import Tienda

class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__tienda=None


    def set_tienda(self,tienda:Tienda):
        self.__tienda=tienda
    
    def get_tienda(self):
        return self.__tienda
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio
    
    def get_stock(self):
        return self.__stock
    
    def set_stock(self,stock):
        self.__stock=stock
    
    def mostrar_valor(self):
        txt =""
        txt += self.nombre + "$"+self.__precio
        return txt