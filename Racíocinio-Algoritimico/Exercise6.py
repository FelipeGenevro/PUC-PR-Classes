#Algoritmo que calcula a duração de um evento em Horas, minutos e segundos a partir do total em segundos.

sec = int(input('Digite a quantidade de segundos: '))

Minutes = sec // 60
hours = Minutes // 60
Seconds = Minutes % 60

while Minutes >= 60:
    hours += 1
    Minutes -= 60

print(f"o evento durou {hours} horas, {Minutes} minutos e {Seconds} segundos!")