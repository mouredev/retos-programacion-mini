"""
FACTORIAL
Crea una función que calcule
el factorial de un número.
"""

def factorial(n: int) -> int:

    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result = result * i

    return result

print(factorial(5))