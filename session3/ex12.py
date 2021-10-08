"""
    Veti primi un input de la tastatura, (numar intreg). Folosind acel input,
    va trebui sa afisati o lista cu toate elementele pana la acel numar, daca
    acel numar este par, altfel, veti afisa o lista cu patratele tuturor
    numerelor pana la acel numar.

    exemplu:
        Veti primi 6, veti afisa [1, 2, 3, 4, 5]
        Veti primi 5, veti afisa [1, 4, 9, 16]
"""

val_no = int(input())

# solutia 1

list_v1 = []
for element in range(1, val_no):

    if val_no % 2 == 0:
        list_v1.append(element)
    else:
        list_v1.append(element**2)

print(list_v1)

# solutia 2

list_v2 = []

i = 1
while i != val_no:
    if val_no % 2 == 0:
        list_v2.append(i)
    else:
        list_v2.append(i**2)
    i += 1

print(list_v2)