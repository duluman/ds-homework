"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti daca acel string este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: stringul se citeste la fel de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 'center'
        Veti printa: False

        Veti primi: 'cojoc'
        Veti printa: True
"""

mesaj = input()

# v1
if mesaj == mesaj[::-1]:
    print('True')
else:
    print('False')

# v2
mesaj_inversat = ''
for i in range(len(mesaj)):
    mesaj_inversat += mesaj[-1-i]

if mesaj == mesaj_inversat:
    print('True')
else:
    print('False')
