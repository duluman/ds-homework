"""
    Veti primi 2 numere intregi de la tastatura (x si y).
    Va trebui sa le convertiti si apoi sa printati valorea lui x la puterea y.

    exemplu:
        Veti primi: 2 si 3
        Veti printa: 8
"""

x = int(input())
y = int(input())

# v1
print('Rezultatul este {}'.format(x**y))


# v2
putere = x ** y

print(f'{x} la puterea lui {y} = {putere}')
