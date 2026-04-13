"""
10. Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
consideração os anos bissextos)
"""

def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dias_no_mes(mes, ano):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if eh_bissexto(ano) else 28

def dias_totais(dia, mes, ano):
    total = 0

    # soma dias dos anos anteriores
    for a in range(1, ano):
        total += 366 if eh_bissexto(a) else 365

    # soma dias dos meses anteriores
    for m in range(1, mes):
        total += dias_no_mes(m, ano)

    # soma os dias
    total += dia

    return total


# Entrada
d1 = int(input("Dia da primeira data: "))
m1 = int(input("Mês da primeira data: "))
a1 = int(input("Ano da primeira data: "))

d2 = int(input("Dia da segunda data: "))
m2 = int(input("Mês da segunda data: "))
a2 = int(input("Ano da segunda data: "))

# Cálculo
dias1 = dias_totais(d1, m1, a1)
dias2 = dias_totais(d2, m2, a2)

diferenca = abs(dias2 - dias1)

print(f"Diferença em dias: {diferenca}")