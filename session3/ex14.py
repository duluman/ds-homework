"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate litere are acest sring.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 3
"""

variabila = input()

# v1
print(len(variabila))

# v2
litere = 0
lista_mea = variabila
for i in lista_mea:
    litere += 1

print(litere)

