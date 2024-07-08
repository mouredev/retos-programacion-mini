"""
DECIMAL A BINARIO
Crea un programa se encargue de
transformar un número decimal a binario.
"""

def decimal_to_binary(decimal):

    binary = ""

    while decimal > 0:
        binary = f"{decimal % 2}{binary}"
        decimal //= 2

    return "0" if binary == "" else binary

print(decimal_to_binary(387))