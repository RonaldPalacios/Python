"""
En este ejemplo, la clase CuentaJoven tiene un nuevo atributo bonificacion y un método adicional 
es_titular_valido() para validar que el titular sea mayor de edad pero menor de 25 años. 
También se sobrescribe el método retirar() para que sólo se pueda retirar dinero si el titular es válido. 
Finalmente, se redefine el método mostrar() para incluir la información adicional de la bonificación. 
Al utilizar super() en el constructor y en el método retirar(), estamos aprovechando la funcionalidad ya existente de la clase Cuenta.
"""

from cuenta import Cuenta
from personas import Persona

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        edad = self.get_titular().get_edad()
        return edad >= 18 and edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        print("Cuenta Joven")
        print("Titular:", self.get_titular().get_nombre())
        print("Cantidad:", self.get_cantidad())
        print("Bonificación:", self.__bonificacion)

# Creamos una instancia de la clase Persona
persona = Persona("Juan", 20, "12345678A")

# Creamos una instancia de la clase CuentaJoven
cuenta_joven = CuentaJoven(persona, 1000.0, 5.0)

# Mostramos los datos de la cuenta joven
cuenta_joven.mostrar()

# Modificamos la bonificación de la cuenta joven
cuenta_joven.set_bonificacion(10.0)

# Retiramos dinero de la cuenta joven
cuenta_joven.retirar(500.0)

# Mostramos de nuevo los datos de la cuenta joven
cuenta_joven.mostrar()
