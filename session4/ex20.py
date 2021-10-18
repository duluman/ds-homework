"""
    Ex. 20: Deschideti fisierul .json creat la exercitiul anterior, cititi
    continutul si returnati un dictionar (dictionarul de acolo).

    Toate astea le veti face intr-o functie read_from_file(file), unde
    file este numele fisierului primit dat ca parametru.
"""
import json


def read_from_file(file):

    try:

        open_file = open(file, "r")

        dict_from_file = open_file.readline()
        print(dict_from_file)
        print(type(dict_from_file))  # <class 'str'>
        open_file.close()

        # with open(file, "r") as read_file:
        #
        #     x = json.load(read_file)
        #
        #     print(type(x))

    except:
        print("Nu exista fisierul acesta!")


read_from_file(input("Cum se numeste fisierul? \n \t"))