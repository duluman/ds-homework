"""
    Ex. 5: Scrieti o functie cu un singur parametru (o lista) care sa
    adauge 1 tuturor elementelor din lista.

    Raspunsul corect:
        - func([1, 2, 3])
            ---> [2, 3, 4]

    Observatii:
        - functia trebuie sa fie MAXIM o linie de cod (2, daca luam in calcul
        si definitia functiei)
        - hint: list comprehensions (google it if you don't know it already)
"""


def add_1(a_list):
    return [x+1 for x in a_list]


print(add_1([2, 5, 6]))
print(add_1([1, 2, 3]))

# input mode

lista = []
while True:
    print(f'Adauga element in lista ta. {lista} \n Daca vrei sa te opresti tasteaza 0 \n ')
    element = int(input())
    if element == 0:
        break
    lista.append(element)

print(f"Lista ta este: {lista}")
print(f"Lista modificata este: {add_1(lista)}")
