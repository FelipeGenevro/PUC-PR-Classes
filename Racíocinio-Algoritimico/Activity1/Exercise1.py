import math

#Algoritmo para cálculo da distância entre dois ponto em um Plano Cartesiano.

x1 = float(input("Digite o Ponto X1: "))
y1 = float(input("Digite o Ponto Y1: "))

x2 = float(input("Digite o Ponto X2: "))
y2 = float(input("Digite o Ponto Y2: "))

Result = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f'a disntância entre dois pontos é {Result:2f}')
