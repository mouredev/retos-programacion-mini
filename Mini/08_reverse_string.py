"""
INVERSIÓN DE CADENAS
Crea una función que invierta
una cadena de texto.
"""

def reverse_string(text):
    reversed_string = ""
    for char in text:
        reversed_string = char + reversed_string
    return reversed_string

print(reverse_string("Hola, mundo!"))