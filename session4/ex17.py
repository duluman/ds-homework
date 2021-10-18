"""
    Ex. 17: Scrieti un decorator care scrie outputul unei functii intr-un fisier
    "output17.data", dar sa nu suprascrie fisierul daca scriptul e rulat de
    mai multe ori, iar contentul nou sa fie pe o noua linie.

    Scrieti o functie f care sa primeasca un intreg (x) ca parametru si sa
    genereze un string aleator din x litere.

    Decorati f cu decoratorul de mai sus.

    Exemplu:
        la prima rulare, x = 3, stringul generat = 'cmi', fisierul arata asa:
            cmi
        la a doua rulare, x = 6, stringul generat = 'cmicmi', fisierul arata:
            cmi
            cmicmi
        la a treia rulare, x = 1, stringul generat = 'b', fisierul arata asa:
            cmi
            cmicmi
            b
"""
import random


def dec_txt(func):

    def wrapper(x):
        file_write = open("output17.txt", "a")
        file_write.write(func(x))
        file_write.write("\n")
        file_write.close()

    return wrapper


@dec_txt
def get_me_letters(x):
    random_word = ""
    litere_mari = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    litere_mici = []

    for litera in litere_mari:
        litere_mici += litera.lower()

    for i in range(x):
        random_word += random.choice(litere_mari + litere_mici)

    return random_word


mesaj = int(input("Spune-mi un numar pentru a scrie in fisier: \n \t"))

get_me_letters(mesaj)