#algoritmo de um jogo de pedra, papel e tesoura que o usuário escolha o número de pontos para vencer.

pontos_maximos = int (input("Digite a quantidade de pontos para vencer: "))
pontos_jogador1 = 0
pontos_jogador2 = 0

while pontos_jogador1 <= pontos_maximos or pontos_jogador2 > pontos_maximos:
    jogador1 = input("Jogador 1 - escolha Pedra, Papel ou Tesoura: ")
    jogador2 = input("Jogador 2 - escolha Pedra, Papel ou Tesoura: ")
    if jogador1 == jogador2:
        print("ambos jogadores escolheram o mesmo item")

    elif jogador1 == "Pedra" and jogador2 == "Tesoura":
        pontos_jogador1 = pontos_jogador1 + 1
        print("-----------------------------")
        print("jogador 1 ganhou + 1 ponto")
        print(f"jogador 1: {pontos_jogador1}")
        print(f"jogador 2: {pontos_jogador2}")
        print("-----------------------------")
    elif jogador2 == "Pedra" and jogador1 == "Tesoura":
        pontos_jogador2 = pontos_jogador2 + 1
        print("-----------------------------")
        print("jogador 2 ganhou + 1 ponto")
        print(f"jogador 1: {pontos_jogador1}")
        print(f"jogador 2: {pontos_jogador2}")
        print("-----------------------------")

    elif jogador1 == "Tesoura" and jogador2 == "Papel":
        pontos_jogador1 = pontos_jogador1 + 1
        print("-----------------------------")
        print("jogador 1 ganhou + 1 ponto")
        print(f"jogador 1: {pontos_jogador1}")
        print(f"jogador 2: {pontos_jogador2}")
        print("-----------------------------")
    elif jogador2 == "Tesoura" and jogador1 == "Papel":
        pontos_jogador2 = pontos_jogador2 + 1
        print("-----------------------------")
        print("jogador 2 ganhou + 1 ponto")
        print(f"jogador 1: {pontos_jogador1}")
        print(f"jogador 2: {pontos_jogador2}")
        print("-----------------------------")

    elif jogador1 == "Papel" and jogador2 == "Pedra":
        pontos_jogador1 = pontos_jogador1 + 1
        print("-----------------------------")
        print("jogador 1 ganhou + 1 ponto")
        print(f"jogador 1: {pontos_jogador1}")
        print(f"jogador 2: {pontos_jogador2}")
        print("-----------------------------")
    elif jogador2 == "Papel" and jogador1 == "Pedra":
        pontos_jogador2 = pontos_jogador2 + 1
        print("-----------------------------")
        print("jogador 2 ganhou + 1 ponto")
        print(f"jogador 1: {pontos_jogador1}")
        print(f"jogador 2: {pontos_jogador2}")
        print("-----------------------------")

    if pontos_jogador1 == pontos_maximos:
        print("-----------------------------")
        print("Jogador 1 ganhou!!")
        print(f"jogador 1: {pontos_jogador1}")
        print(f"jogador 2: {pontos_jogador2}")
        print("-----------------------------")
        break
    elif pontos_jogador2 == pontos_maximos:
        print("-----------------------------")
        print("Jogador 2 ganhou!!")
        print(f"jogador 1: {pontos_jogador1}")
        print(f"jogador 2: {pontos_jogador2}")
        print("-----------------------------")
        break