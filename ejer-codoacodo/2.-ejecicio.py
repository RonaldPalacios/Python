# Escribir una función que calcule el mínimo común múltiplo entre dos números
# MCM: es el numero positivo mas pequeño que es multiplo de 2 numeros


def mcm(x, y):
    z = max(
        x, y
    )  # con esto tomamos el multiplo mayor, asi me aseguro tener un multiplo mayor

    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        z += 1


print(mcm(10, 20))
print(mcm(15, 27))
