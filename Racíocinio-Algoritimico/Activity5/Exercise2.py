soma = 0

while True:
    numero = int(input("digite um numero para somar:"))
    if numero == 0:
        break
    else:
        soma += numero
    print(f"soma: {soma}")
