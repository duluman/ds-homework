"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa introduceti toate elemente intr-o lista si s-o afisati, dupa
    care va trebui sa creati un set (vezi ce e un set) din lista respectiva
    si sa il printati si pe acela.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa prima data: [1, 3, 4, 5, 5]
        Veti prina a doua oara: {1, 3, 4, 5}
"""

"""
A set is an unordered collection of unique elements, while a list is ordered and can contain duplicates. 
Converting a list to a set creates a new set with the same elements as the list, but with duplicates removed.
"""

mesaj = input()

lista_mea = []
while mesaj != 'exit':

    lista_mea.append(int(mesaj))

    mesaj = input()

print(lista_mea)

setul_meu = set(lista_mea)
print(setul_meu)

