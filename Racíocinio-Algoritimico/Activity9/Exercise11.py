def data_por_extenso(data):
    meses = [
        "janeiro", "fevereiro", "março", "abril",
        "maio", "junho", "julho", "agosto",
        "setembro", "outubro", "novembro", "dezembro"
    ]

    try:
        # Separando dia, mês e ano
        dia, mes, ano = map(int, data.split("/"))

        # Verifica se o mês é válido
        if mes < 1 or mes > 12:
            return None

        # Dias máximos de cada mês
        dias_mes = [31, 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]

        # Verifica ano bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias_mes[1] = 29

        # Verifica se o dia é válido
        if dia < 1 or dia > dias_mes[mes - 1]:
            return None

        return f"{dia} de {meses[mes - 1]} de {ano}"

    except:
        return None


# Input do usuário
data_usuario = input("Digite uma data no formato DD/MM/AAAA: ")

resultado = data_por_extenso(data_usuario)

if resultado:
    print("Data formatada:", resultado)
else:
    print("Data inválida.")