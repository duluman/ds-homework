"""
    Ex. 16: Scrieti o functie upper care sa intoarca un text uppercase complet,
    primind un parametru my_str (string).
    --> f('cmi') --> 'CMI'

    Scrieti o functie lower care sa intoarca un text lowercase complet,
    primind un parametru my_str (string).
    --> f('CMI') --> 'cmi'

    Veti primi un input de la tastatura, un string.

    Scrieti o alta functie call_changers, care sa primeasca o functie ca si
    parametru, iar daca inputul are un numar par de caractere, va printa inputul
    cu uppercase, altfel, va printa inputut lowercase.

    Exemplu:
        - veti primi input: 'ceva'
            ---> CEVA
        - veti primi input: 'cEVa1'
            ---> ceva1
"""


def f_upper(my_string):

    return my_string.upper()


def f_lower(my_string):

    return my_string.lower()


def f_mesaj():

    mesaj = input("Hai sa discutam: ")
    return mesaj


def call_changers(f):

    if len(f) % 2 == 0:
        mesaj_modificat = f_upper(f)
    else:
        mesaj_modificat = f_lower(f)

    return mesaj_modificat


print(call_changers(f_mesaj()))


