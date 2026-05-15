"""
3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []
for i in range(1, 5):
    n = float(input(f"Digite sua {i}º nota: "))
    notas.append(n)

media = sum(notas) / len(notas)
print(f"sua média é de {media:.2f} pontos")