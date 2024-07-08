"""
PAR O IMPAR
Crea un programa que compruebe si
un número entero es par o impar.
"""

try: 
    number = int(input(
        "Introduce un número entero:"))

    if number % 2 == 0:
        print(f"Es {number} par")
    else:
        print(f"Es {number} impar")
except ValueError:
    print("Entrada no válida")