class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("Error: el nombre debe ser una cadena de caracteres")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
        else:
            print("Error: la edad debe ser un número entero positivo")

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 8 and dni.isdigit():
            self.__dni = dni
        else:
            print("Error: el DNI debe ser una cadena de 8 dígitos")

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)

    def es_mayor_de_edad(self):
        return self.__edad >= 18


# Creamos un objeto persona con los datos vacíos
p = Persona()

# Seteamos los atributos utilizando los setters
p.set_nombre("Juan")
p.set_edad(25)
p.set_dni("12345678")

# Mostramos los datos utilizando el método mostrar()
p.mostrar()

# Verificamos si es mayor de edad utilizando el método es_mayor_de_edad()
print("¿Es mayor de edad?", p.es_mayor_de_edad())