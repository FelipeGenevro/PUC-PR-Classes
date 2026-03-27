#Algoritmo que calcula o peso ideal de cada pessoa baseado no sexo e na altura

sexo = input("Digite o seu sexo (M/F):").upper()
altura = float(input("Digite sua altura :"))



if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"seu peso ideal é {peso_ideal:.2f} kgs")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"seu peso ideal é {peso_ideal:.1f} kgs")
else:
    print("Digite um sexo Válido (M/F)")


