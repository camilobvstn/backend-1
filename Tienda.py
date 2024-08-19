from Productos import Producto
from Empleado import Empleado

class Tienda :
    def __init__(self,nombre:str,direccion:str,area:str,valor:int): #el init se crea cuando la clase tiene parametros
        self.__nombre=nombre#asi se puede poner privado 
        self.__productos=[]
        self.__empleado=[]
        self.__direccion=direccion
        self.__area=area
        self.__valor=valor
        
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre:str):
        self.__nombre=nombre

    def get_productos(self):
        return self.__productos
    def set_productos(self,productos):
        self.__productos=productos

    def get_empleado(self):
        return self.__empleado
    def set_empleado(self,empleado):
        self.__empleado=empleado
    
    def get_direccion(self):
        return self.__direccion
    def set_direccion(self,direccion:str):
        self.__direccion=direccion
    
    def get_area(self):
        return self.__area
    def set_area(self,area:str):
        self.__area=area
    
    def get_valor(self):
        return self.__valor
    def set_valor(self,valor:int):
        self.__valor=valor
    
    def __str__(self):
        return "" + self.__nombre

    def mostrar_valor(self):
        txt =""
        txt += self.nombre + "$"+self.__valor
        return txt
    
    def agregar_producto(self,producto:Producto):
        self.__productos.append(producto)
        print("El producto se registro correctamente.")

    def eliminar_productos(self,producto:Producto):
        if producto in self.__productos:
            self.__productos.remove(producto)
        else:
            print("El producto no existe.")



    def agregar_empleado(self,empleado:Empleado):
        self.__empleado.append(empleado)
        print("El empleado se registro correctamente.")

    def eliminar_empleado(self,empleado:Empleado):
        if empleado in self.__empleado:
            self.__empleado.remove(empleado)
        else:
            print("El empleado no existe.")