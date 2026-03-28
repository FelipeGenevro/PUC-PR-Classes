#algoritmo que retorna o valor da passagem de acordo com o tipo de passagem e o destino do cliente, baseando-se nos
#valores passados em uma tabela pelo professor

local = input("Qual a sua região de destino?")
tipo_passagem = input("Gostaria de Ida ou Ida e volta?")

if local == "Norte":

    if tipo_passagem == "Ida":
        print("o valor da sua passagem será de R$500 reais")
    elif tipo_passagem == "Ida e volta":
        print("o valor da sua passagem será de R$900 reais")

elif local == "Nordeste":

    if tipo_passagem == "Ida":
        print("o valor da sua passagem será de R$350 reais")
    elif tipo_passagem == "Ida e volta":
        print("o valor da sua passagem será de R$650 reais")

elif local == "Centro-Oeste":

    if tipo_passagem == "Ida":
        print("o valor da sua passagem será de R$350 reais")
    elif tipo_passagem == "Ida e volta":
        print("o valor da sua passagem será de R$600 reais")

elif local == "Sul":

    if tipo_passagem == "Ida":
        print("o valor da sua passagem será de R$300 reais")
    elif tipo_passagem == "Ida e volta":
        print("o valor da sua passagem será de R$550 reais")