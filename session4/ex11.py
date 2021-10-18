"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""


def dec_txt(func):
    def wrapper():
        file_write = open("output11.txt", "w")
        file_write.write(func())
        file_write.close()

    return wrapper


@dec_txt
def f():
    return "CMI"


f()
print("Am apelat functia si am scris in fisierul text")

