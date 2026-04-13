#Algoritmo que pede 5 números pro usuário e retorna eles em ordem crescente usando LAÇOS

numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            # troca
            temp = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = temp

print("Números em ordem crescente:")
for n in numeros:
    print(n)