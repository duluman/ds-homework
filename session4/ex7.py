"""
    Ex. 7: Scrieti o functie care sa primeasca trei parametri
        - prefix (string)
        - word (string)
        - suffix (string)
    Si trebuie sa intoarca cuvantul cu prefixul si sufixul adaugate.

    Raspuns:
        - pentru prefix = 'a', suffix = 'b' si word = 'x'
            ---> 'axb'

    Observatii:
        - functia trebuie sa aiba MAXIM 1 linie de cod ca si body
"""


def cuvant_compus(prefix, word, suffix):
    return prefix + word + suffix


print(cuvant_compus('a', 'x', 'b'))

# input mode

prefix = input("Tasteaza prefixul: ")
word = input("Tasteaza cuvantul: ")
suffix = input("Tasteaza sufixul: ")

print(cuvant_compus(prefix, word, suffix))