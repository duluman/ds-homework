"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""


def alfabet(string):
    new_string = ""

    for item in string:
        new_string += chr(ord(item)+1)

    return new_string


print(alfabet('aabbcc'))

# input mode

mesaj = input("Hai sa criptam mesajul tau! \n Tasteaza cateva caractere: \n \t")
print(alfabet(mesaj))