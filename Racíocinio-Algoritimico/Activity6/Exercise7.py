"""
7. Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
conjunto de palavras
"""


while True:
    palavra = input("Digite uma palavra: ")

    if palavra == "":
        break

    letras = 0

    for caractere in palavra:
        if caractere.lower() == "a":  # trata maiúscula/minúscula
            letras += 1

    if letras > 0:
        print(f"Há {letras} letras 'A' na palavra")
    else:
        print("Não há letras 'A' na palavra")