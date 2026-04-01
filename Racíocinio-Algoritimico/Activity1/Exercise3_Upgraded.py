import datetime

birth_day = int(input('Digite o dia de nascimento: '))
birth_month = int(input('Digite o mês de nascimento: '))
birth_year = int(input('Digite o ano de nascimento: '))

birth_date = datetime.date(birth_year, birth_month, birth_day)
today = datetime.date.today()

difference = today - birth_date

print(f'Você já viveu {difference.days} dias')