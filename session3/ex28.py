"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""

mesaj = int(input())

suma = 0

for i in range(mesaj+1):
    suma += i

print(suma)
