#algoritmo que calcula o IMC individual a partir do peso e da altura

peso = float(input("Digite o seu peso :"))
altura = float(input("Digite sua altura :"))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Você está abaixo do peso ideal")
elif 18.5 <= IMC <= 25:
    print("Você está no peso ideal")
elif 25 <= IMC <= 30:
    print("Você está acima do peso ideal")
if IMC > 30:
    print("Você está obeso1")
