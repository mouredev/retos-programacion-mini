"""
RETO VIRAL 12345678
Simula el reto viral 12345678.
Crea una función que cuente de
1 a 8, eliminando cada vez un
dígito y mostrando un espacio en
blanco en su lugar, de manera
ascendente y descendente.
"""

for i in range(1, 9):
    print(" " * (i - 1), end="")
    for j in range(i, 9):
        print(j, end="")
    print()

for i in range(8, 0, -1):
    print(" " * (i - 1), end="")
    for j in range(i, 9):
        print(j, end="")
    print()