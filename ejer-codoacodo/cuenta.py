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
