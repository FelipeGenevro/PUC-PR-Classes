#Algoritmo que solicita 5 números e retorna o menor e o maior entre eles

numbers = []

for i in range(5):
    numbers.append(int(input("Digite um número: ")))

numbers.sort()

print(f"o menor número informado é {numbers[0]:,} e o maior é {numbers[-1]:,}")
