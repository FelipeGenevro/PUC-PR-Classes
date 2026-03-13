#algoritmo para retornar quantos anos, meses e dias o usuario tem a partir da numero de dias vividos.

days = int(input('Digite a quantidade de dias vividos por você: '))

years = days // 365
months_x = days % 365
months = months_x // 12
day = months % 12

print(f"você tem {years} anos, {months} meses e {day} dias")