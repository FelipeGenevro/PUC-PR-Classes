"""
Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
tempo necessário para que a população do país A ultrapasse a população do país B
"""

pop_a = 5000000
pop_b = 7000000

taxa_a = 0.03
taxa_b = 0.02

anos = 0

while pop_a <= pop_b:
    pop_a = pop_a * (1 + taxa_a)
    pop_b = pop_b * (1 + taxa_b)
    anos += 1

print(f"População A: {int(pop_a)}")
print(f"População B: {int(pop_b)}")
print(f"Tempo necessário: {anos} anos")