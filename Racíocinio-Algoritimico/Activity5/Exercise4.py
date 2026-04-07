#Algoritmo que solicita 10 números e informa quantos são pares e quantos são ímpares

impar = 0
par = 0

for i in range(10):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Você digitou {par} número(s) par(es) e {impar} número(s) impar(es).")