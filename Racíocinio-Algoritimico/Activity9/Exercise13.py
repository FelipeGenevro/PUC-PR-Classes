def desenhar_moldura(linhas=1, colunas=1):
    # Garante valores entre 1 e 20
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    # Linha superior
    print("+" + "-" * colunas + "+")

    # Meio da moldura
    for _ in range(linhas):
        print("|" + " " * colunas + "|")

    # Linha inferior
    print("+" + "-" * colunas + "+")


# Input do usuário
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

desenhar_moldura(linhas, colunas)