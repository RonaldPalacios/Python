"""Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
"""


def Diccionario(texto):
    textos = texto.split()
    repetidos = {}

    for textos in textos:
        if textos in repetidos:
            repetidos[textos] += 1
        else:
            repetidos[textos] = 1

    return repetidos


def PalabraMasUsada(palabras):
    mas_usada = max(palabras, key=palabras.get)
    veces = palabras[mas_usada]

    return (mas_usada, veces)


texto = input("INGRESE UN TEXTO: ")
palabras = Diccionario(texto)
print(PalabraMasUsada(palabras))
