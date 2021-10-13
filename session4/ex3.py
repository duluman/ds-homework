"""
    Ex. 3: Completati functia de mai jos, in asa fel incat sa intoarca
    o lista cu elementele pana la X (X fiind un parametru al functiei).

    Observatii:
        - X este un numar intreg (intotdeauna)
        - nu aveti voie sa folositi range()

    Rezultatul trebuie sa arate asa:
        - pentru x = 3 --> [0, 1, 2]
"""


def func(x):
    n = 0
    lista_mea = []
    while n < x:
        lista_mea.append(n)
        n = n + 1
    return lista_mea


print(func(3))


# input mode

numar = int(input("Spune-mi un numar si iti voi afisa o lista cu toate numerele pana la cel ales: \n \t"))

print(func(numar))