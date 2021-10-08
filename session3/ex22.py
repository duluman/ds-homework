"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""

mesaj = input()
mesaj_editat = ''
index_count = 0
for i in mesaj:

    if index_count % 2 == 0:
        mesaj_editat += i.upper()
    else:
        mesaj_editat += i

    index_count += 1

print(mesaj_editat)

