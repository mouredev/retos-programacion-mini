"""
IMC
Crea una calculadora del
índice de masa corporal.
"""

weight = float(input("Peso en kg: "))
height = float(input("Altura en m: "))

imc = weight / (height ** 2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Peso bajo")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")