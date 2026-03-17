#algoritmo que satisfaz a equação linear proposta pelo professor em sala

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))
f = float(input("Digite o valor de f: "))

det = (a * e) - (b * d)

if det == 0:
    print("O sistema não possui solução, pois ae - bd = 0.")
else:
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det

    print(f"Valor de x = {x:.2f}")
    print(f"Valor de y = {y:.2f}")