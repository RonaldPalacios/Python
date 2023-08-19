"""Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
"""


def get_int_iterativa():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Valor no válido ingrese un numero entero")


def get_int_recursiva():
    try:
        numero = int(input("Ingrese un numero entero: "))
        return numero
    except ValueError:
        print("Valor no válido , intentelo de nuevo")
        return get_int_recursiva()


get_int_recursiva()
get_int_iterativa()
