"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""


def dec_txt(func):
    def wrapper(arg):
        file_write = open("output12.txt", "w")
        text_x = str(arg)
        file_write.write(text_x)
        file_write.close()

    return wrapper


@dec_txt
def f(x):
    print(x)


f(47744)