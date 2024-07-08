"""
CONVERSOR DE TEMPERATURAS
Crea un conversor entre
grados Celsius y Fahrenheit. 
"""

print("Conversor de Temperaturas:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

choice = input("Elige una opción: ")

degrees = float(input("Temperatura: "))

if choice == "1":
    fahrenheit = (degrees * 9/5) + 32
    print(f"{degrees}°C son {fahrenheit}°F.")
elif choice == "2":
    celsius = (degrees - 32) * 5/9
    print(f"{degrees}°F son {celsius}°C.")
else:
    print("Opción no válida.")