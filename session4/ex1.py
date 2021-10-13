"""
    Ex. 1: Functia de mai jos returneaza X la puterea Y.
    Modificati aceasta functie incat sa intoarca X la puterea Y la puterea Z.
"""


def power(x, y, z):
    return (x ** y) ** z


print(power(2, 3, 2))

print("Iti pot calcula X la puterea lui Y la puterea lui Z:")

mesaj = []
for i in range(3):
    x = int(input())
    mesaj.append(x)


print(power(mesaj[0], mesaj[1], mesaj[2]))


