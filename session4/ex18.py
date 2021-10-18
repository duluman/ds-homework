"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""


def suma_recursiva(lista):

    if len(lista) == 1:
        return lista[-1]

    else:
        return lista[-1] + suma_recursiva(lista[0:-1])


print(suma_recursiva([1, 2, 3]))
print(suma_recursiva([1, 3, 5, 7]))

