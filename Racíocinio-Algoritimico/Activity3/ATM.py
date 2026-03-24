#Algoritmo que simula um ATM com capacidade de saque

valor_saque = int(input('Digite o valor do saque (apenas valores inteiros): '))

notas_100 = 0
notas_50 = 0
notas_10 = 0
notas_5 = 0
notas_1 = 0

if valor_saque < 10:
    print('o valor mínimo de saque é R$10,00')
    exit()
elif valor_saque > 600:
    print('O valor máximo de saque é R$600,00')
    exit()

while valor_saque >= 100:
    notas_100 += 1
    valor_saque -= 100

while valor_saque >= 50:
    notas_50 += 1
    valor_saque -= 50

while valor_saque >= 10:
    notas_10 += 1
    valor_saque -= 10

while valor_saque >= 5:
    notas_5 += 1
    valor_saque -= 5

while valor_saque >= 1:
    notas_1 += 1
    valor_saque -= 1

print("você receberá:")
print(f"{notas_100} nota(s) de R$100,00")
print(f"{notas_50} nota(s) de R$50,00")
print(f"{notas_10} nota(s) de R$10,00")
print(f"{notas_5} nota(s) de R$5,00")
print(f"{notas_1} nota(s) de R$1,00")