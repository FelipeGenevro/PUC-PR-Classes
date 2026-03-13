#Algoritmo para calcular a média ponderada entre 3 notas de um ano de peso 2, 3 e 5, respectivamente.

nota1 = float(input('Digite sua primeira nota (peso 20%): '))
nota2 = float(input('Digite sua segunda nota (peso 30%): '))
nota3 = float(input('Digite sua terceira nota (peso 50%): '))

Result = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5) / 1 #0,2 + 0,3 + 0,5 = 1

print(f"sua média final foi {Result:.1f} pontos")