import random


def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print(f"Você tirou {dado1} + {dado2} = {soma}")
    return soma


def jogar_craps():
    print("=== Jogo de Craps ===")

    primeira_jogada = lancar_dados()

    if primeira_jogada == 7 or primeira_jogada == 11:
        print("Natural! Você ganhou!")

    elif primeira_jogada == 2 or primeira_jogada == 3 or primeira_jogada == 12:
        print("Craps! Você perdeu!")

    else:
        ponto = primeira_jogada
        print(f"Seu ponto é {ponto}")
        print("Continue jogando até tirar esse número novamente.")
        print("Se tirar 7 antes, você perde.")

        while True:
            jogada = lancar_dados()

            if jogada == ponto:
                print("Você tirou seu ponto novamente!")
                print("Você ganhou!")
                break

            elif jogada == 7:
                print("Você tirou 7 antes do ponto.")
                print("Você perdeu!")
                break


jogar_craps()