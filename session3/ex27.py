"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
import random

mesaj = input()
litere_mari = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

litere_mici = []

for litera in litere_mari:
    litere_mici += litera.lower()

mesaj_criptat = ''

for i in range(int(mesaj)):
    mesaj_criptat += random.choice(litere_mici+litere_mari)

print(mesaj_criptat)