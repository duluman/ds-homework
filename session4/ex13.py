"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""


def dex_txt(func):
    def wrapper():
        mesaj = func()
        mesaj_nou = ""
        verificator = 0
        for litera in mesaj:
            if verificator % 2 == 0:
                mesaj_nou += litera.upper()
            else:
                mesaj_nou += litera

            verificator += 1

        return mesaj_nou

    return wrapper()


@dex_txt
def f():
    return 'cmi'


print(f)