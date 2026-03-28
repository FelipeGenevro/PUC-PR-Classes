#algoritmo que calcula o valor de A e A' a partir de a, b e c em Bhaskara

a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

delta = (b ** 2) - 4 * a * c

formula_mais = (b * -1) + (delta * 0.5) / 2 * a

formula_menos = (b * -1) - (delta * 0.5) / 2 * a

if delta < 0:
   print("não há soluções possiveis, pois o delta é maior que 0")

print(f"os resultados são A = {formula_mais} e A' = {formula_menos}")