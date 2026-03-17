#Algoritmo para calcular o valor de D.

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

r = (a + b)**2
s = (b + c)**2

d = (r + s) // 2

print(f"o valor de D é {d:.2f}")