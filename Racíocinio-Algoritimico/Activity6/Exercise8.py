"""
 Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal
"""


binario = input("Digite um número em binário: ")

decimal = 0
potencia = 0

for digito in reversed(binario):
    decimal += int(digito) * (2 ** potencia)
    potencia += 1

print(f"Valor em decimal: {decimal}")