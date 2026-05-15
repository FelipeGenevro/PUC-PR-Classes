def converter_hora(hora, minuto):

    if hora == 0:
        return 12, minuto, 'A'

    elif hora < 12:
        return hora, minuto, 'A'

    elif hora == 12:
        return 12, minuto, 'P'

    else:
        return hora - 12, minuto, 'P'


def exibir_hora(hora, minuto, periodo):

    if periodo == 'A':
        print(f"Horário convertido: {hora}:{minuto:02d} A.M.")
    else:
        print(f"Horário convertido: {hora}:{minuto:02d} P.M.")


while True:

    hora = int(input("Digite a hora (0-23): "))
    minuto = int(input("Digite os minutos (0-59): "))

    nova_hora, novo_minuto, periodo = converter_hora(hora, minuto)

    exibir_hora(nova_hora, novo_minuto, periodo)

    repetir = input("Deseja converter outro horário? (S/N): ").upper()

    if repetir != 'S':
        print("Programa encerrado.")
        break