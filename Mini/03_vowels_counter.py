"""
CONTADOR DE VOCALES
Crea un programa que cuente cuantas
vocales tiene una cadena de texto.
"""

vowels = "aeiou"
counter = 0

text = input(
    "Introduce una cadena de texto: ")

for char in text.lower():
    if char in vowels:
        counter += 1

print(f"Total vocales: {counter}")