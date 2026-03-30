#algoritmo que calcula o valor de A e A' a partir de a, b e c em Bhaskara

import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Verifica se é equação do 2º grau
if a == 0:
    print("Não é uma equação do segundo grau (A não pode ser 0).")
else:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Não há soluções reais (delta < 0).")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print(f"os resultados são A = {x1} e A' = {x2}")