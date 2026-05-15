"""
2. Faça um Programa que leia um valor de 10 números reais e mostre-os na ordem inversa.
"""

numbers = []

for i in range(10):
    n = float(input("Digite um número real:"))
    numbers.append(n)

numbers.sort(reverse=True)
print(numbers)