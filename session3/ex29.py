"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""

mesaj = input()
vocale = ['a', 'e', 'i', 'o', 'u', 'ă', 'î', 'â']
suma_vocale = 0

for litera in mesaj:
    if litera in vocale:
        suma_vocale += 1

suma_consoane = len(mesaj) - suma_vocale

print(f'{suma_vocale} (pentru vocale)')
print(f'{suma_consoane} (pentru consoane)')
