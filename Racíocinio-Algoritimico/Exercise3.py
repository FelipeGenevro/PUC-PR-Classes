#Algoritmo que calcula quantos dias totais o usuário ja viveu a partir dos anos, meses e dias vividos

age = int(input('Digite quantos anos de vida você tem: '))
months = int(input('Digite quantos meses de vida você tem: '))
days = int(input('Digite quantos dias de vida você tem: '))

age_to_days = age * 365
months_to_days = months * 30

total_days = age_to_days + months_to_days + days

print(f'Você já viveu {total_days} dias')