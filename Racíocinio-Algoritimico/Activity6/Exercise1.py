#algoritmo que calcula o decaimento de um material radioativo

massa_final = float(input("Digite a massa do material, em gramas: "))
tempo = 0

if massa_final <= 0.5:
    print("A massa inicial já é menor ou igual a 0.5g")
else:
    while massa_final > 0.5:
        massa_final = massa_final / 2  # agora divide a massa atual
        tempo += 50

    print(f"Massa final: {massa_final:.4f} g")
    print(f"Tempo total: {tempo} segundos")