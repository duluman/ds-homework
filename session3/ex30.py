"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""

"""
dacă există paranteze rotunde, pătrate și acolade, se execută întâi operațiile dintre parantezele rotunde, 
apoi cele dintre parantezele pătrate și apoi cele dintre acolade.
"""

mesaj = input()

deschis = ['{', '[', '(']
inchis = [')', ']', '}']

if len(mesaj) % 2 == 1 or mesaj[0] in inchis or mesaj[-1] in deschis:
    print('v1 - False!')
else:

    mesaj_temporar = ''
    while True:
        if '()' in mesaj:

            mesaj_temporar = mesaj[0:mesaj.index('()')] + mesaj[mesaj.index('()') + 2:]

        elif '[]' in mesaj:
            mesaj_temporar = mesaj[0:mesaj.index('[]')] + mesaj[mesaj.index('[]') + 2:]

        elif '{}' in mesaj:
            mesaj_temporar = mesaj[0:mesaj.index('{}')] + mesaj[mesaj.index('{}') + 2:]

        if len(mesaj) == 0:
            print('True ^_^ ')
            break
        elif len(mesaj) == 2:
            if mesaj[0] in inchis or mesaj[1] in deschis:
                print('v2 - False!!')
                break
            elif mesaj[0] in deschis[-1] and mesaj[1] in inchis[1:]:
                print('v3 - False!!')
                break
            elif mesaj[0] in deschis[1] and (mesaj[1] in inchis[0] or mesaj[1] in inchis[-1]):
                print('v4 - False!!')
                break
            elif mesaj[0] in deschis[0] and (mesaj[1] in inchis[0] or mesaj[1] in inchis[1]):
                print('v5 - False!!')
                break
        else:
            mesaj = mesaj_temporar



