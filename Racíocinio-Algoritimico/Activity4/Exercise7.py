#algoritmo que retorna ao usuario a data de aniversario no formato de acordo com a escolha dele

dia = int(input("Que dia você nasceu?"))
mes = int(input("Que mes você nasceu? (digite apenas números)"))
ano = int(input("Que ano você nasceu?"))

print("Como você prefere exibir sua data de nascimento?")
print("1 - Data Simples (01/01/2001)")
print("2 - Data Abreviadda (01/jan/2001)")
print("3 - Data Comppleta (01 de janeiro de 2001)")
opcao = int(input("OBS: digite apenas o número da opção"))

meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

nome_mes = meses[mes-1]

if opcao == 1:
    print(f"{dia}/{mes}/{ano}")
elif opcao == 2:
    print(f"{dia}/{nome_mes}/{ano}")
elif opcao == 3:
    print(f"{dia} de {nome_mes} de {ano}")
