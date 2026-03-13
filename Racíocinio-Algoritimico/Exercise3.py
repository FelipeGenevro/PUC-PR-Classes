import datetime

#Algoritmo que calcula quantos dias o usuário ja viveu a partir da data de nascimento

birth = int(input('Digite o ano de nascimento: '))
month = int(input('Digite o mês de nascimento: '))
day = int(input('Digite o dia de nascimento: '))

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

calculation_years = current_year - birth
calculation_months = current_month - month
calculation_days = current_day - day

final_year = calculation_years * 365
final_month = calculation_months * 30

final_age = final_year + final_month + calculation_days

print(f'Você já viveu {final_age} dias')