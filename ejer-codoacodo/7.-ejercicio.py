"""
El constructor de la clase recibe dos parámetros: titular (que es un objeto de la clase Persona) y cantidad (opcional, con valor 0.0 si no se especifica).
Los atributos de la clase son privados, por lo que se utilizan los métodos getters para acceder a ellos.
El método mostrar() imprime en pantalla los datos de la cuenta.
El método ingresar() recibe una cantidad y la suma a la cantidad actual de la cuenta, siempre y cuando la cantidad sea mayor que 0. Si no lo es, no se hace nada.
El método retirar() recibe una cantidad y la resta a la cantidad actual de la cuenta, siempre y cuando la cantidad sea mayor que 0. Si no lo es, no se hace nada. La cuenta puede quedar en números rojos.

"""
from personas import Persona

class Cuenta:
    def __init__(self, nombre = Persona(), cantidad = 0):
        self.__titular = nombre
        self.__cantidad = cantidad

    
    @property
    def titular(self):
        return self.__titular

    @titular.setter   
    def titular(self, nombre):
        self.__titular = nombre

    @property
    def cantidad(self):
        self.__cantidad

    @cantidad.setter   
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print (f"Apellido y Nombre: {self.__titular}. Saldo en la cuenta: {self.__cantidad}")

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
        
    def retirar(self, cantidad):
        self.__cantidad = self.__cantidad - cantidad



usuario2 = Cuenta("Juliana Ortiz", 500)
usuario2.ingresar(45000)
usuario2.retirar(5000)
usuario2.mostrar()

