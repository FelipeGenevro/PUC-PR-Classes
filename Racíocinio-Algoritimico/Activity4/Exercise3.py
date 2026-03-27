#algoritmo que simula um jogo de impar ou par com 2 jogadores

numero_jogador1 = int(input("Qual o seu número, jogador 1? (de 1 a 5) "))
numero_jogador2 = int(input("Qual o seu número, jogador 2? (de 1 a 5) "))

palpite_jogador1 = input("Qual o seu palpite, ímpar ou par, jogador 1?")
palpite_jogador2 = input("Qual o seu palpite, ímpar ou par, jogador 2?")


if 1 <= numero_jogador1 <= 5 and 1 <= numero_jogador2 <= 5:


    if palpite_jogador1 == palpite_jogador2:
        print(f"os dois jogadores tiverem o mesmo palpite: {palpite_jogador1}! Tentem novamente!")
        exit()

    soma = numero_jogador1 + numero_jogador2

    impar_ou_par = soma % 2
    resultado = "desconhecido"

    if impar_ou_par == 1:
        resultado = "ímpar"
    elif impar_ou_par == 0:
        resultado = "par"

    if palpite_jogador1 == resultado:
        print(f"Jogador 1 venceu ({palpite_jogador1} ; {soma})")
    elif palpite_jogador2 == resultado:
        print(f"Jogador 2 venceu ({palpite_jogador2} ; {soma})")

else:
    print("insira números válidos! entre 1 e 5")