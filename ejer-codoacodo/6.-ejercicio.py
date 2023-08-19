"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""


class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # Getter
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_dni(self):
        return self.dni

    # Setter
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_edad(self, edad):
        self._edad = edad

    def set_dni(self, dni):
        self._dni = dni

    def mostrar(self):
        print(f"Nombre: {self._nombre} - Edad: {self._edad} - DNI: {self._dni}")


p = Persona("Andres", 26, "21952629")
p1 = Persona("Mariana", 21, "19526291")
print(Persona.mostrar(p))
print(Persona.mostrar(p1))


def es_mayor_de_edad(self):
    if self._edad >= 18:
        return True
    else:
        return False
