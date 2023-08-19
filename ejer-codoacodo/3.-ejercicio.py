# . Escribir un programa que reciba una cadena de caracteres y
# devuelva un diccionario con cada palabra que contiene y
# la cantidad de veces que aparece (frecuencia).


def Diccionario(texto):
    textos = texto.split()
    repetidos = {}

    for textos in textos:
        if textos in repetidos:
            repetidos[textos] += 1
        else:
            repetidos[textos] = 1

    return repetidos


print(Diccionario("Hello world Hello by new world"))
