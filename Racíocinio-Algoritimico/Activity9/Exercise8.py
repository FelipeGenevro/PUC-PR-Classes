def contar_numeros(numero):
    total = 0
    for i in numero:
        total += 1

    print(f"Total de numeros: {total}")

numero = str(input("Digite um numero: "))
contar_numeros(numero)