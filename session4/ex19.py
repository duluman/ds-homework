"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""
import random


def get_me_letters():
    """
    elemente aleatoare
    stringul sa aiba intre 3 si 6 caractere
    """

    x = random.randint(3, 6)

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


def random_d_keys():
    """
    dictionar de 4 elemente aleatoare
    key sa fie intre 0 si 10
    :return:
    """
    my_dict = {}

    i = 0

    while i < 4:
        random_key = random.randint(1, 10)

        if random_key not in my_dict.keys():
            my_dict[random_key] = get_me_letters()
            i += 1

    return my_dict


def write_json(func):
    """
    functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el un dictionar
    """

    file_write = open(f"{func}.json", "a")
    file_write.write(str(random_d_keys()))
    file_write.write("\n")
    file_write.close()


write_json(input("Cum sa se numeasca fisierul? \n \t"))