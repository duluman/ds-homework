"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

mesaj = input()
vocale = ['a', 'ă', 'â', 'î','e', 'i', 'o', 'u']
numaratoare = 0
for element in mesaj.lower():
    if element in vocale:
        numaratoare = numaratoare + 1

print(numaratoare)